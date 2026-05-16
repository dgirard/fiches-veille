# How the X Algorithm Actually Works in 2026 — and What That Means for Growth

A teardown of the [`xai-org/x-algorithm`](https://github.com/xai-org/x-algorithm) open-source release (May 15th, 2026), plus four audience-tuned recommendation tracks.

> **Read this first.** The famous 2023 weight table — "replies count more than likes by a big multiplier" — describes a system that no longer exists in this form. The 2026 algorithm is a transformer (Phoenix) that learns weights from your engagement history, scored against a multi-action surface, gated by an offline content-understanding service (Grox). The *shape* of scoring matters far more than the *numbers*, and the numbers themselves aren't in the open release. This report sticks to what the code shows.

---

## Part 1 — Teardown

### 1.1 The For You feed in one diagram

This is the architecture quoted directly from the upstream README (the cleanest depiction in the repo):

```
┌─────────────────────────────────────────────────────────────┐
│                  FOR YOU FEED REQUEST                       │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                       HOME MIXER                            │
│                  (Orchestration Layer)                      │
│                                                             │
│   QUERY HYDRATION                                           │
│   - User Action Sequence (engagement history)               │
│   - User Features (following list, mutes/blocks, ...)       │
│                            │                                │
│   CANDIDATE SOURCES        ▼                                │
│   - THUNDER (in-network: posts from accounts you follow)    │
│   - PHOENIX RETRIEVAL (out-of-network: two-tower ANN)       │
│   - + ads / who-to-follow / topics / MoE / prompts          │
│                            │                                │
│   HYDRATION                ▼                                │
│   - core metadata, author info, media, engagement counts    │
│                            │                                │
│   FILTERING (pre-scoring)  ▼                                │
│   - dedupe, age, self, blocks, mutes, paywall, already-seen │
│                            │                                │
│   SCORING                  ▼                                │
│   - Phoenix Scorer  : P(action) for each of 19 actions      │
│   - Weighted Scorer : Σ (weight × P(action))                │
│   - Author Diversity: attenuate repeated authors            │
│   - OON Scorer      : multiplicative penalty if OON         │
│                            │                                │
│   SELECTION                ▼                                │
│   - sort by final score, select top K                       │
│                            │                                │
│   POST-SELECTION FILTERS   ▼                                │
│   - VFFilter (deletes/spam/violence/gore), convo dedup      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  RANKED FEED RESPONSE                       │
└─────────────────────────────────────────────────────────────┘
```

Three components do almost all the work:

- **Home Mixer** (`x-algorithm/home-mixer/`) — Rust orchestrator that runs the pipeline above.
- **Thunder** (`x-algorithm/thunder/`) — Rust in-memory store of recent posts per user, fed by Kafka. Sub-millisecond lookups of in-network candidates (`thunder/main.rs`, `thunder/post_store.rs`).
- **Phoenix** (`x-algorithm/phoenix/`) — JAX ML service that does both candidate retrieval (two-tower model) and ranking (Grok-1-derived transformer).

A fourth component, **Grox** (`x-algorithm/grox/`), runs *offline* — it classifies and embeds posts on a separate path, writes those signals to the feature store, and Home Mixer hydrates them in later. Grox does not sit in the request hot path.

### 1.2 The 19 things Phoenix predicts (and why this is the headline change)

The 2023 algorithm scored each candidate against a hand-built linear combination of engagement labels with widely-leaked multipliers. The 2026 algorithm scores each candidate against the output of a learned transformer that predicts probabilities for **nineteen different actions**. From `phoenix/runners.py:233-252` and confirmed in `home-mixer/candidate_pipeline/candidate.rs:30-51` (`PhoenixScores` struct):

| Index | Action | Sign |
|---|---|---|
| 0 | `favorite_score` (like) | positive |
| 1 | `reply_score` | positive |
| 2 | `repost_score` (retweet) | positive |
| 3 | `photo_expand_score` | positive |
| 4 | `click_score` (link/post click) | positive |
| 5 | `profile_click_score` | positive |
| 6 | `vqv_score` (video quality view) | positive (gated by min duration) |
| 7 | `share_score` | positive |
| 8 | `share_via_dm_score` | positive |
| 9 | `share_via_copy_link_score` | positive |
| 10 | `dwell_score` | positive |
| 11 | `quote_score` | positive |
| 12 | `quoted_click_score` | positive |
| 13 | `follow_author_score` | positive |
| 14 | `not_interested_score` | negative |
| 15 | `block_author_score` | negative |
| 16 | `mute_author_score` | negative |
| 17 | `report_score` | negative |
| 18 | `dwell_time` (continuous duration) | positive |

The four negative-feedback actions are explicitly enumerated as `NEGATIVE_FEEDBACK_INDICES: List[int] = [14, 15, 16, 17]` in `phoenix/runners.py`.

The headline change versus 2023 is the **action surface itself**. New first-class signals: continuous `dwell_time` (not just binary dwelled / not-dwelled), `vqv_score` (a quality-thresholded video view, not a raw view), `follow_author_score` (the model learns to predict whether a post will earn its author a new follower), and three distinct share variants (in-app, via DM, via copy-link). Each of these is a separate prediction; each can be weighted independently in the score formula.

### 1.3 The scoring formula — and the weight caveat

The Weighted Scorer combines the predictions exactly as the README writes it: `Σ (weight × P(action))`. The full wiring is in `home-mixer/scorers/weighted_scorer.rs:44-91`. Concretely, the score for a candidate is:

```
favorite × FAVORITE_WEIGHT
+ reply × REPLY_WEIGHT
+ retweet × RETWEET_WEIGHT
+ photo_expand × PHOTO_EXPAND_WEIGHT
+ click × CLICK_WEIGHT
+ profile_click × PROFILE_CLICK_WEIGHT
+ vqv × (VQV_WEIGHT if video duration > MIN_VIDEO_DURATION_MS else 0)
+ share × SHARE_WEIGHT
+ share_via_dm × SHARE_VIA_DM_WEIGHT
+ share_via_copy_link × SHARE_VIA_COPY_LINK_WEIGHT
+ dwell × DWELL_WEIGHT
+ quote × QUOTE_WEIGHT
+ quoted_click × QUOTED_CLICK_WEIGHT
+ dwell_time × CONT_DWELL_TIME_WEIGHT
+ follow_author × FOLLOW_AUTHOR_WEIGHT
+ not_interested × NOT_INTERESTED_WEIGHT
+ block_author × BLOCK_AUTHOR_WEIGHT
+ mute_author × MUTE_AUTHOR_WEIGHT
+ report × REPORT_WEIGHT
```

The four negative weights are negative numbers, so they subtract. A small `offset_score()` step (`weighted_scorer.rs:83-91`) keeps negative aggregate scores well-ordered relative to positive ones.

**The caveat — and it is the single most important caveat in this report.** None of those `*_WEIGHT` constants are defined in the open-source release. They are all referenced as `crate::params::FAVORITE_WEIGHT` etc., but no `params.rs` module exists in the released code (verified by `grep -rn` across the whole repo). The weights are managed by a feature-switch / parameter service that X runs internally, which lets them A/B test and tune weights without code changes. Anyone telling you "replies are worth N.N× more than likes in 2026" is fabricating a number that is not derivable from the OSS release. What this report can tell you — and what is genuinely useful — is the **sign and the structural role** of every weight: which actions are positive, which are negative, which are gated by content properties, and which surfaces they apply to.

### 1.4 The hidden multipliers

Three structural multipliers act on the score *after* the weighted sum. These are not in the "weight table" framing because they multiply the whole score, not individual action probabilities — but they shape outcomes more than any individual weight does.

**Out-of-network penalty.** `home-mixer/scorers/oon_scorer.rs:20-23`:

```
score = base_score × OON_WEIGHT_FACTOR     if candidate is out-of-network
score = base_score                          otherwise
```

The README states `OON_WEIGHT_FACTOR < 1`, and the comment at line 7 confirms intent: *"Prioritize in-network candidates over out-of-network candidates."* This is the codified version of "followers matter": a post from an account you follow is rated against a higher ceiling than the identical post from an account you don't.

**New-user OON exception.** `home-mixer/scorers/ranking_scorer.rs:220-239`. For users whose account age is below `NewUserAgeThresholdSecs` *and* who follow at least `NEW_USER_MIN_FOLLOWING` accounts, the OON penalty is replaced by `NEW_USER_OON_WEIGHT_FACTOR`. New accounts that have done minimal onboarding (following enough people) get a different treatment of out-of-network content than mature accounts. This biases what new users see — and by extension, what new accounts can reach.

**Author diversity decay.** `home-mixer/scorers/author_diversity_scorer.rs:29-31`:

```
multiplier(position) = (1 - floor) × decay_factor^position + floor
```

Where `position` is how many posts from this author have already appeared earlier in the *sorted* candidate list. The first post from a given author keeps full score; the second is multiplied by `(1-floor)·decay + floor`; the third by `(1-floor)·decay² + floor`; and so on. With sensible parameters (the actual `AUTHOR_DIVERSITY_DECAY` and `AUTHOR_DIVERSITY_FLOOR` values are again external), this means: **the best post from a given author in a given feed render keeps its score, every subsequent post from that same author is attenuated, and the attenuation never falls below `floor`.** The implication for posting cadence is structural, not heuristic.

**Video duration gate.** `home-mixer/scorers/weighted_scorer.rs:72-81`. The `vqv_score` (video quality view) only enters the weighted sum if the video's duration exceeds `MIN_VIDEO_DURATION_MS`. Shorter clips simply don't earn the VQV contribution at all (their `vqv` weight is replaced by zero). This is a hard gate, not a soft penalty.

### 1.5 What never enters the ranker

Two layers of filters keep posts out of the scoring pipeline entirely. Reach lost here is invisible — the post was never ranked, so it never had a chance to score well.

**Pre-scoring filters** (`home-mixer/filters/`, executed sequentially before any scoring):

- `DropDuplicatesFilter` — exact duplicate post IDs.
- `CoreDataHydrationFilter` — posts that failed to hydrate.
- `AgeFilter` — older than the configured max age.
- `SelfpostFilter` — your own posts.
- `RepostDeduplicationFilter` — multiple reposts of the same content.
- `IneligibleSubscriptionFilter` — paywalled content for non-subscribers.
- `PreviouslySeenPostsFilter` — posts in the viewer's `seen_ids`.
- `PreviouslyServedPostsFilter` — posts already served in the current session.
- `MutedKeywordFilter` — posts matching the viewer's muted keywords.
- `AuthorSocialgraphFilter` — posts from authors the viewer has blocked or muted, *and* posts where the author blocks the viewer (including the quoted author of a quote tweet). The block relationship is checked in both directions.

**Post-selection filters** (after ranking, before serving):

- `VFFilter` — visibility filtering: deleted, spam, violence, gore.
- `DedupConversationFilter` — collapses multiple branches of the same conversation.

**Grox offline gates** (`x-algorithm/grox/`, run separately and written to the feature store before a post is ever candidate). These are eligibility classifiers, not score modifiers:

- `task_spam_detection.py` / `classifiers/content/spam.py` — Grok-based spam screen for low-follower / low-quality replies.
- `task_post_safety_screen_deluxe.py` — violence, NSFW, misinformation screen.
- `task_safety_ptos_policy.py` — Terms of Service violations.
- `task_banger_screen.py` — early high-quality / viral screen (positive).
- `task_reply_ranking.py` — reply quality scoring, consumed for conversation ranking.

The architectural point: borderline content doesn't get "demoted" in the 2026 system. It gets disqualified at hydration time and never reaches scoring. This is materially different from the 2023 system's reduced-reach / visibility-filtering model.

### 1.6 What Phoenix actually learns from

Phoenix's most consequential input is not the candidate post; it's **your action sequence**. `home-mixer/query_hydrators/user_action_seq_query_hydrator.rs` fetches the viewer's recent engagement history (likes, replies, shares, dwell, blocks, mutes, etc.) and passes it as a sequence to the transformer alongside the candidate set. From `phoenix/recsys_model.py` and the candidate-isolation design described in the README: candidates can attend to your action sequence, but they cannot attend to each other. The implications:

- Scores are **per-user and per-post**, not global. The same post predicted to earn a like from User A at probability p₁ is predicted to earn a like from User B at probability p₂; there's no single "this post is good" number.
- "Going viral" is a *population-level* outcome of many independent personal predictions clearing the bar, not a single metric Phoenix optimizes.
- Recency, topic affinity, social proximity, language preference, and historical author affinity are all implicit in the sequence. They are *not* hand-coded features anymore — the README, line 55: *"We have eliminated every single hand-engineered feature and most heuristics from the system."* The transformer learns them.
- Two related signals get explicit hydration even in this transformer-first world: `mutual_follow_jaccard_hydrator.rs` computes Jaccard similarity between the viewer's followers and the candidate author's followers (social proximity), and `following_replied_users_hydrator.rs` flags when a user the viewer follows has replied to a candidate. These are scaffolds that the transformer can use.

For OON retrieval (Phoenix two-tower), the input is also the action sequence: your action history becomes a user embedding, candidate posts have post embeddings, and the system retrieves posts whose embeddings are near yours. The embeddings come partly from `grox/embedder/multimodal_post_embedder_v5.py`, which encodes text + images + (optional) ASR-transcribed video into a normalized 1024-dim vector. **Your discoverability by strangers is therefore a function of how close your posts embed to posts that your target audience already engages with.**

### 1.7 What changed from the 2023 release

Five differences are large enough to be load-bearing for growth thinking:

1. **No hand-engineered features.** The 2023 release had explicit boost / penalty terms for verified status, paid subscribers, network distance, etc. The 2026 release ripped them out in favor of letting the transformer learn relevance from action sequences (README line 55, plus the Key Design Decisions section). This means "rule of thumb" advice tied to specific 2023 multipliers is not just dated — it's pointing at code that doesn't exist anymore.

2. **One model predicting many actions, instead of many models predicting one each.** Phoenix predicts the full nineteen-action vector in a single forward pass with candidate-isolation masking (so scores are batch-independent and cacheable). The 2023 system stitched separate predictors together; Phoenix is unified.

3. **Grox separates content understanding from ranking.** Spam, safety, PTOS, and "banger" classification all happen on a separate offline path (`grox/plan_master.py` orchestrates nine parallel plans) and write to feature stores. Home Mixer reads those signals as already-decided gates. The hot path doesn't do content understanding; that work has been moved upstream.

4. **New first-class engagement signals.** Continuous `dwell_time`, video quality view (`vqv_score`), `follow_author_score`, and three share variants (`share`, `share_via_dm`, `share_via_copy_link`) did not exist as discrete weights in the 2023 release. Each has a separate weight, and several relate to behaviors creators can directly influence.

5. **Two-tower OON retrieval.** Out-of-network discovery is no longer "SimClusters + heuristics"; it's a learned two-tower model where both users and posts have embeddings, and ANN search retrieves nearby candidates (`phoenix_source.rs`, `phoenix/recsys_retrieval_model.py`). The embedding for a post comes from a multimodal model that processes text, images, and optionally a transcribed audio track of any video. This makes *semantic clarity* of a post measurably more important than keyword overlap.

---

## Part 2 — Recommendations

All four audience tracks share a seven-pillar spine so they are comparable. The pillars derive directly from Part 1; if a recommendation is not grounded in one of these pillars (with a citation), it doesn't belong in the report.

| Pillar | What the code says |
|---|---|
| 1. In-network advantage | `oon_scorer.rs:20-23` — OON content is multiplied by a factor `< 1`. |
| 2. P(action) framing | `phoenix/recsys_model.py` — Phoenix predicts per-user probabilities, not global ones. |
| 3. High-weight actions | `weighted_scorer.rs:49-67` — 19 distinct weighted actions; choose which to trigger. |
| 4. Diversity decay | `author_diversity_scorer.rs:29-31` — exponential decay per repeated author per render. |
| 5. Negative signals | `weighted_scorer.rs:64-67` + `AuthorSocialgraphFilter` + `MutedKeywordFilter` — direct subtractions and hard gates. |
| 6. Two-tower retrievability | `phoenix_source.rs` + `multimodal_post_embedder_v5.py` — your reach to strangers depends on embedding proximity. |
| 7. Grox / VF eligibility | `grox/plan_master.py` + `home-mixer/filters/vf_filter.rs` — borderline content is excluded, not demoted. |

A note on confidence: claims about *direction* (positive vs negative weight, hard gate vs soft adjustment, exists vs not) are high-confidence and cited. Claims about *magnitude* (how much, how often, in what ratio) are marked `(directional)` because they cannot be derived from the OSS.

---

### 2.A — Personal / founder voice

You are one human posting from one account. Your goal is some combination of follower growth, network compounding, and conversational depth. Your time budget is small. Pick the pillars that move the needle.

**Pillar 1 — In-network advantage.** Until you have a real follower base, every post you publish is fighting the OON penalty (`oon_scorer.rs:21`). The single highest-leverage thing you can do is convert your existing real-world relationships into follows — DMs, podcast cross-promotion, newsletter footers, replies on accounts whose audience overlaps yours. Each follower converts you from "competing in the OON pool" to "served by Thunder by default" for that user.

**Pillar 2 — P(action) framing.** Stop optimizing for total likes; total likes are a population artifact. Optimize for *the next person who sees this post being likely to do the action you want them to do*. Pick **one** action per post: a reply (you're asking a question), a follow (you're posting an authority bait line that requires they see more), a dwell (you're posting a thread that pulls the eye downward), a share (you're packaging a takeaway so cleanly someone will paste it into their group chat). When you can't articulate which action you're aiming at, the post is unlikely to score well for any of them.

**Pillar 3 — Trigger high-weight actions deliberately.** Of the 19 actions, the ones a personal account has the most influence over:
- *Reply* — questions that have a specific defensible answer earn replies; vague "what do you think?" prompts do not.
- *Dwell time* — threads and longer posts earn `dwell_time` directly; one-line posts cannot. There is now a *continuous* dwell signal (index 18), not just binary dwelled / not-dwelled, so making the post worth reading slowly matters.
- *Profile click* — the post that makes a stranger want to know who you are. Bio-relevant signaling, a strong identity line, a domain claim.
- *Follow-author* — Phoenix has its own prediction for this (index 13). Posts that read like "here is my premise and I will defend it across many future posts" earn this; one-off observations do not.

**Pillar 4 — Survive the diversity decay.** The author diversity scorer (`author_diversity_scorer.rs:29-31`) sorts candidates by score then attenuates each repeated appearance from the same author in *that single feed render*. Practical rules:
- The single best post you publish in a given window keeps full score. The second-best is attenuated. So **publish your best post first**, not last.
- Don't stack posts back-to-back; spread them across the windows your audience refreshes their feed. (The actual decay parameters are external — but the structural fact that pacing matters is in the code.)
- Reposts and quotes of *other* authors don't trigger your author decay; they contribute to the diversity score under the original author's ID.

**Pillar 5 — Stay out of negative-signal land.** Four direct negative weights (`not_interested`, `block_author`, `mute_author`, `report`, indices 14-17). One mute or block subtracts from the score of your *future* content for that user (because the transformer has now seen the negative action in their sequence). Tactically: avoid the contrarian-for-its-own-sake voice that earns mutes from people who agree with you most of the time. Pick your fights; don't manufacture them.

**Pillar 6 — Two-tower retrievability.** *(sidebar for personal accounts)* If you want to reach strangers, post about topics where someone's recent engagement history includes posts like yours. Stylistic uniqueness matters less than topical embedding proximity — the v5 multimodal embedder (`grox/embedder/multimodal_post_embedder_v5.py`) is encoding the *semantic content*, not your prose voice. Cross-posting the same idea three ways (text, image, video) creates three embedding shots at being retrieved.

**Pillar 7 — Grox / VF gates.** *(sidebar for personal accounts)* Borderline content doesn't underperform; it doesn't enter the ranker at all. If a post is on the edge of spam-classification (too many @mentions, link spam patterns, repeated low-engagement replies on big accounts) it can disappear from the candidate pool for *some* users entirely. Cite `grox/classifiers/content/spam.py` if a creator pushes back.

**5-item checklist for your next 10 posts:**
1. Each post names the single action it's aiming for (reply / dwell / follow / share).
2. At least three are threads or long-form (earning `dwell_time` directly).
3. None are posted within an hour of another of your posts (diversity decay protection).
4. Two are framed to earn profile clicks (identity bait, domain claim).
5. Zero are reactive negative takes that risk earning mutes from your warm audience.

---

### 2.B — Brand / company account

You represent an organization. Decisions go through approval. You ship a content calendar. Your goal is some mix of reach, click-through to a property you control, and lead generation. You have less voice flexibility than a personal account but more production capacity and clearer KPIs.

**Pillar 1 — In-network advantage.** Same penalty (`oon_scorer.rs:21`), different tools. Two practical moves:
- *Employee amplification* — every employee who posts on the brand's behalf is an additional Thunder source for their followers. The brand account's reach is the union of every employee's in-network distribution.
- *Mutual-follow density* — `mutual_follow_jaccard_hydrator.rs` computes Jaccard similarity between viewer's followers and candidate author's followers. Brands embedded in the right communities (your customers follow each other) get a lift from this signal that an isolated brand account doesn't get.

**Pillar 2 — P(action) framing.** Stop reporting impression totals to leadership. Report on the *action distribution per post*: which action did this post earn most, and was it the action you intended? If you wanted clicks but got likes, the post was off-brief — likes aren't a brand KPI and Phoenix will under-rank the post for your future audiences accordingly.

**Pillar 3 — Trigger high-weight actions deliberately.** Brand-relevant actions to design for:
- *Click* (index 4) and *quoted click* (index 12) — the actions that drive measurable site traffic. Posts that promise a payoff that requires leaving X earn these.
- *VQV* (index 6) — video views past `MIN_VIDEO_DURATION_MS`. Cutting a video too short kills the contribution entirely. Build video assets long enough to clear the threshold *and* edited tightly enough to hold attention past it. Short hook, then substance.
- *Share via DM* (index 8) and *share via copy-link* (index 9) — these are distinct from in-app shares (index 7). Posts that get pasted into private group chats and Slack DMs are valuable enough to earn their own weights. Pricing teardowns, product comparisons, "look at this" demos, controversy that people forward privately rather than reply to publicly.
- *Follow-author* (index 13) — design at least one post per week as a *follow magnet*: "We are the team building X. This thread is a tour of what we ship next month." Phoenix predicts follow-author as a discrete probability and weights it accordingly.

**Pillar 4 — Survive the diversity decay.** Brands often violate this without realizing it:
- A "drumbeat" of four posts spaced 30 minutes apart underperforms the single best one of them, alone (`author_diversity_scorer.rs:29-31`).
- The brand account *and* the CEO posting the same announcement counts as two distinct authors — that beats one account posting twice. Coordinate across humans, don't stack on one handle.
- For launches, post the announcement once; let employees and amplification do the multi-source coverage.

**Pillar 5 — Stay out of negative-signal land.** Direct negative weights (indices 14-17) plus the harder gates: `AuthorSocialgraphFilter` includes the "author blocks viewer" case for retweets and quotes, so engaging with controversial accounts who block your audience can suppress your reach in unexpected directions. For brand safety specifically: the May 15th 2026 release added a `home-mixer/ads/` module with brand-safety tracking that respects sensitive content boundaries — meaning if your organic posts repeatedly land near sensitive content topics, you risk being adjacent to brand-safety filters that affect both your reach and your monetization.

**Pillar 6 — Two-tower retrievability.** This is the most under-used lever for brands. Concrete tactics:
- *Topical consistency over weeks.* The embedding of your account, in aggregate, is what determines whose retrieval queries surface your posts. Posting across too many topics dilutes the embedding.
- *Multimodal posts.* `multimodal_post_embedder_v5.py` encodes text + image + (optional) video ASR transcript. A post with a strong image and clear caption gets a richer embedding than text-only. A post with a video of someone *clearly speaking the keywords* gets the ASR contribution. Subtitle your videos for the model, not just for the viewer.
- *Topic-pack alignment.* New candidate sources include `phoenix_topics_source.rs` and `phoenix_moe_source.rs` — being identifiable to a topic helps your posts show up via those sources, not just the generic retrieval.

**Pillar 7 — Grox / VF gates.** For brand accounts this is compliance, not creativity:
- `task_post_safety_screen_deluxe.py` and `task_safety_ptos_policy.py` are not adjustable. Your legal-cleared post can still get quietly excluded if it triggers the classifier. Set up a watchlist of posts that mysteriously underperform and audit them as suspected exclusions, not as bad posts.
- `task_spam_detection.py` keys on low-follower / low-quality reply patterns. Brand accounts whose engagement strategy involves heavy replying on big posts can accidentally get flagged. Reply *substantively* (the model evaluates context) or not at all.

**5-item checklist for your next 10 posts:**
1. Action-intent is annotated in the calendar (`target_action: click | vqv | dm_share | follow | reply`).
2. Every video clears `MIN_VIDEO_DURATION_MS` *and* is subtitled (the embedder benefits from the ASR-readable transcript).
3. Cross-author distribution plan exists for the week (brand + at least 2 employees, never stacked).
4. Posts have a topical theme over the week, not random subject hopping (embedding consistency).
5. At least one post is purpose-built as a follow magnet for the next month's launch audience.

---

### 2.C — Generalized framework

For audiences who want the model independent of role. This section is the durable abstraction; 2.A and 2.B are the role-specific tactics.

**The three layers of reach.** The 2026 algorithm is a stack of three independent gates. A post must pass *all three* to reach a given user:

1. **Eligibility.** Pre-scoring filters and Grox offline classifiers (Part 1.5). Binary: in or out. No optimization possible here other than not being excluded.
2. **Retrieval.** For OON, the two-tower model (Part 1.6). Probabilistic: your post is or isn't near the user's embedding. Optimized by *what* you post (topic, semantic content, multimodal completeness).
3. **Ranking.** The weighted sum of nineteen learned action probabilities, modified by OON / diversity / video-gate multipliers (Parts 1.3, 1.4). Continuous: your post scores relative to other candidates. Optimized by *how* you post (which action you're triggering, when, paced across what cadence).

Most growth advice conflates layer 3 with the whole system. It is the most visible layer but it is the *last* layer; layers 1 and 2 determine whether you ever got to be scored.

**The action surface as a product question.** Phoenix predicts nineteen actions because users do nineteen distinct things. Each action is a different relationship the user can have with a post: *I will perform this socially* (like, reply, quote, share), *I will perform this privately* (DM-share, copy-link-share, dwell, photo expand), *I am declaring an identity* (follow author, profile click), *I am rejecting* (not-interested, block, mute, report). A post that doesn't pick a target relationship gets predicted near zero for all of them and scores accordingly.

**The transformer as a fairness mechanism.** Because Phoenix predicts per-user probabilities from per-user action sequences, "good content" is not a global property. Two posts that look identical to a human can have wildly different ranking outcomes for the same user because of what *that user* has historically engaged with. This is mechanically fair (no global bias toward established accounts beyond the OON factor) and personally inscrutable (no creator can know exactly why one post worked and another didn't). The honest framing is *probabilistic targeting*, not *deterministic quality*.

**The author-diversity decay as a structural feature.** It is the algorithm's answer to monoculture: prevent any single creator from dominating a user's feed in one render. The implication for creators is unintuitive: **publishing more posts per day past a threshold reduces, not increases, total reach** — each marginal post is attenuated and competes with your earlier posts in the same render. The optimal cadence is therefore non-monotonic in post count; there is a per-day plateau set by audience refresh rate, author position position, and the parameters of `(1 - floor) × decay^position + floor`.

**Negative signals as one-shot vetoes.** A mute or block doesn't just cost the post that earned it; it shows up as a negative entry in that user's action sequence forever, which Phoenix uses for every subsequent scoring decision about your content for that user. The cost is therefore *cumulative across all future posts to that user*. Avoidable mutes from sympathetic audiences are extremely expensive in expected-value terms.

**Eligibility-time exclusion is the silent killer.** Borderline content in 2026 doesn't underperform; it disappears. There is no signal to the creator that a Grox classifier excluded their post from candidate pools. The only diagnostic is comparative reach analysis across posts of varying compliance distance from policy edges.

**Two laws of mechanical growth.**
- *Law 1 — In-network is multiplicative, OON is additive.* Followers turn every future post from a probabilistic OON retrieval event into a deterministic Thunder lookup. The returns to follower acquisition compound across every post you ever publish.
- *Law 2 — The model's job is to predict you, not reward you.* Phoenix optimizes for predictive accuracy of user action, not for creator success. Growth strategies that fight what users predictably do (begging for engagement, manipulating with controversy) hurt the prediction quality of your account in the model's eyes and downgrade your future posts accordingly.

---

### 2.D — Client / consulting deliverable

For external use. Every claim cites the file the evidence lives in. The framing is "what we observe in the public source release, and what it implies for measurable growth interventions."

**Executive summary** (for the cover page).

The 2026 X For You algorithm is a three-stage system: an offline content-understanding service (Grox) gates eligibility, a two-tower retrieval model surfaces out-of-network candidates, and a Grok-1-derived transformer (Phoenix) ranks candidates by predicting nineteen distinct engagement actions per user. Ranking is `Σ (weight × P(action))` modified by a multiplicative out-of-network penalty and an author-diversity decay (citations below). The numeric weights are not in the open release. Growth interventions should target *structural levers* that are documented in code: which action a post is designed to trigger, whether content clears eligibility classifiers, whether the post's embedding sits in the right neighborhood for the target audience, and whether posting cadence respects the diversity decay.

**Evidence table.**

| Claim | Evidence (file:line) |
|---|---|
| For You candidates come from Thunder (in-network) and Phoenix retrieval (OON), then are ranked together. | `x-algorithm/README.md` lines 48-53; `home-mixer/sources/thunder_source.rs`; `home-mixer/sources/phoenix_source.rs` |
| Phoenix predicts 19 distinct action probabilities per candidate. | `home-mixer/candidate_pipeline/candidate.rs:30-51` (`PhoenixScores` struct); `phoenix/runners.py:233-252` (action index list) |
| Final score is `Σ (weight × P(action))` over the 19 actions. | `home-mixer/scorers/weighted_scorer.rs:44-91`; README line 289 |
| Numeric weights (`FAVORITE_WEIGHT` etc.) are referenced but not defined in the OSS release. | `grep -rn "FAVORITE_WEIGHT" x-algorithm/` returns only `weighted_scorer.rs:49` — the constant is referenced as `crate::params::FAVORITE_WEIGHT` and no `params.rs` exists in the repo. |
| OON content is multiplied by `OON_WEIGHT_FACTOR < 1`. | `home-mixer/scorers/oon_scorer.rs:20-23` |
| New users (under threshold age, with minimum following) get a different OON factor. | `home-mixer/scorers/ranking_scorer.rs:220-239` (`NEW_USER_OON_WEIGHT_FACTOR` branch) |
| Repeated authors in a single feed render are attenuated by exponential decay. | `home-mixer/scorers/author_diversity_scorer.rs:29-31`, formula `(1-floor)·decay_factor^position + floor` |
| Video earns the `vqv_score` weight only if `video_duration_ms > MIN_VIDEO_DURATION_MS`. | `home-mixer/scorers/weighted_scorer.rs:72-81` |
| Four explicit negative-feedback actions reduce score. | `home-mixer/scorers/weighted_scorer.rs:64-67`; `phoenix/runners.py:266-270` (`NEGATIVE_FEEDBACK_INDICES = [14, 15, 16, 17]`) |
| Blocked authors and authors who block the viewer are filtered before scoring, including in quote-tweet relationships. | `home-mixer/filters/author_socialgraph_filter.rs` |
| Content classification (spam, post-safety, PTOS) runs offline in Grox and gates eligibility via the feature store. | `x-algorithm/grox/plan_master.py`; `x-algorithm/grox/classifiers/content/spam.py`; `task_post_safety_screen_deluxe.py`; `task_safety_ptos_policy.py` |
| Phoenix uses candidate-isolation attention: candidates cannot attend to each other. | `x-algorithm/README.md` "Key Design Decisions" section; `x-algorithm/phoenix/recsys_model.py` |
| Hand-engineered features have been removed from the system. | `x-algorithm/README.md` line 55: *"We have eliminated every single hand-engineered feature and most heuristics from the system."* |
| Post embeddings are multimodal (text + images + optional ASR transcript of video). | `x-algorithm/grox/embedder/multimodal_post_embedder_v5.py` |

**Recommended interventions (ordered by expected impact, all directional pending client measurement).**

1. **Action-targeted content design.** Reorganize the client's editorial calendar so each post declares a target action from the nineteen-action set. Measure success by *action distribution per post*, not raw impressions. Expected effect: improved post-level predictive scores for the target user segment because content is congruent with the action it is being scored against.

2. **Author distribution playbook.** Audit the client's posting cadence against the author-diversity decay. Replace stacked single-account drumbeats with distributed multi-account amplification across employees, partners, and the brand handle. Expected effect: each individual post enters the ranker at `position = 0` for its author within a given render rather than `position = 1, 2, ...`.

3. **Video specification.** Establish a minimum cut length above `MIN_VIDEO_DURATION_MS` (the exact value is external — the client should A/B test cut lengths to identify the threshold empirically for their content). All videos shipped with ASR-friendly audio and burned-in subtitles to feed both `vqv` and the multimodal embedder's transcript path.

4. **Topic-embedding consistency.** Audit the client's last 90 days for topical breadth. Recommend a 70/30 split between a coherent topical core (which builds embedding-neighborhood density with the target audience) and exploratory content (which surfaces new audiences but dilutes the embedding).

5. **Eligibility-gate audit.** Sample posts from the client's archive that underperformed against their cohort and check them against the publicly documented gate types (spam patterns, safety boundaries, PTOS surface). Treat suspected silent exclusions as a separate failure mode from "ranked low."

6. **Negative-signal hygiene.** Identify the client's recurring antagonistic posting patterns and quantify their expected cost as cumulative across future posts to the muted audience. Recommend retiring patterns whose mute rate from the warm audience exceeds an internal threshold.

7. **Follower-acquisition reframing.** Reframe follower-acquisition spend as buying *multiplicative* future reach (via the OON-to-Thunder conversion) rather than as buying a single audience metric. The OON factor is a permanent tax until the user follows; one follow lifts every future post for that user.

**Limitations and honest disclosures (mandatory for the deliverable).** Numeric weights are not derivable from the OSS release. All "X is more important than Y" claims in this report describe code structure (sign, gate, multiplier presence) not magnitude. Released model artifacts are a mini Phoenix checkpoint (2 layers, 4 attention heads, 256-dim per the May 15th 2026 changelog and `phoenix/README.md`), not production weights, so direct inference against the released code demonstrates behavior shape rather than production scores. Several integrations are stubbed: `panic!("Not implemented: to_thrift for ...")` markers exist in `home-mixer/candidate_pipeline/candidate_features.rs` and `user_features.rs`, and brand-safety brand lists, topic ID mappings, language penalties, and ad blending rules are not present in the public release. The client should treat this report as a structural model, not a quantitative predictor.

**Recommended cadence for the client engagement.**
- Month 1 — implement action-targeted calendar, author-distribution playbook, video spec.
- Month 2 — embed topical consistency audit; sample test of follower-acquisition reframing.
- Month 3 — measure relative reach change cohort-on-cohort; recalibrate against the eligibility-gate audit.
- Quarterly — re-read `xai-org/x-algorithm` for upstream changes; this report assumes the May 15th 2026 release.

---

## Appendix

### A.1 Source file index

Grouped by subsystem, no line numbers (so the index doesn't rot if the repo is updated; load-bearing line numbers are kept inline in Parts 1-2).

**Home Mixer — orchestration and scoring**
- `home-mixer/README.md`
- `home-mixer/lib.rs`
- `home-mixer/scorers/weighted_scorer.rs`
- `home-mixer/scorers/ranking_scorer.rs`
- `home-mixer/scorers/oon_scorer.rs`
- `home-mixer/scorers/author_diversity_scorer.rs`
- `home-mixer/scorers/phoenix_scorer.rs`
- `home-mixer/candidate_pipeline/candidate.rs` (`PhoenixScores`, `PostCandidate`)

**Home Mixer — candidate sources**
- `home-mixer/sources/thunder_source.rs`
- `home-mixer/sources/phoenix_source.rs`
- `home-mixer/sources/phoenix_moe_source.rs`
- `home-mixer/sources/phoenix_topics_source.rs`
- `home-mixer/sources/who_to_follow_source.rs`
- `home-mixer/sources/ads_source.rs`
- `home-mixer/sources/prompts_source.rs`
- `home-mixer/sources/push_to_home_source.rs`
- `home-mixer/sources/tweet_mixer_source.rs`

**Home Mixer — hydrators**
- `home-mixer/query_hydrators/user_action_seq_query_hydrator.rs`
- `home-mixer/candidate_hydrators/mutual_follow_jaccard_hydrator.rs`
- `home-mixer/candidate_hydrators/engagement_counts_hydrator.rs`
- `home-mixer/candidate_hydrators/following_replied_users_hydrator.rs`
- `home-mixer/candidate_hydrators/language_code_hydrator.rs`
- `home-mixer/candidate_hydrators/has_media_hydrator.rs`

**Home Mixer — filters**
- `home-mixer/filters/age_filter.rs`
- `home-mixer/filters/muted_keyword_filter.rs`
- `home-mixer/filters/author_socialgraph_filter.rs`
- `home-mixer/filters/ineligible_subscription_filter.rs`
- `home-mixer/filters/vf_filter.rs`
- (plus `DropDuplicatesFilter`, `CoreDataHydrationFilter`, `SelfpostFilter`, `RepostDeduplicationFilter`, `PreviouslySeenPostsFilter`, `PreviouslyServedPostsFilter`, `DedupConversationFilter`)

**Phoenix — ranking and retrieval**
- `phoenix/README.md`
- `phoenix/run_pipeline.py`
- `phoenix/runners.py` (action indices, `NEGATIVE_FEEDBACK_INDICES`)
- `phoenix/recsys_model.py` (transformer with candidate-isolation masking)
- `phoenix/recsys_retrieval_model.py` (two-tower retrieval)

**Thunder — in-network real-time store**
- `thunder/main.rs`
- `thunder/post_store.rs`
- `thunder/thunder_service.rs`
- `thunder/kafka_utils.rs`

**Grox — offline content understanding**
- `grox/engine.py`
- `grox/plan_master.py`
- `grox/embedder/multimodal_post_embedder_v5.py`
- `grox/classifiers/content/spam.py`
- `grox/task_spam_detection.py`
- `grox/task_post_safety_screen_deluxe.py`
- `grox/task_safety_ptos_policy.py`
- `grox/task_banger_screen.py`
- `grox/task_reply_ranking.py`

**Top-level**
- `README.md`

### A.2 Glossary

- **Phoenix** — the Grok-1-derived transformer that does both ranking and retrieval. Predicts 19 actions per candidate.
- **Thunder** — the in-memory Rust service that holds recent posts and serves in-network candidates with sub-millisecond latency.
- **Grox** — the offline content-understanding service. Runs classifiers (spam, safety, PTOS) and embedders (multimodal v5). Writes results to the feature store for Home Mixer to read.
- **Home Mixer** — the Rust orchestrator that runs the request-time pipeline: hydrate → source → hydrate → filter → score → select → filter.
- **OON** — out-of-network. A candidate from an account the viewer does not follow. Subject to a multiplicative score penalty.
- **VQV** — video quality view. A video view that clears the configured minimum duration. The associated weight contributes only when `video_duration_ms > MIN_VIDEO_DURATION_MS`.
- **Two-tower** — an ML retrieval pattern where users and items are encoded by separate towers into a shared embedding space, then matched by nearest-neighbor search.
- **Candidate isolation** — the attention masking pattern in Phoenix ranking where candidates can attend to the user's context but not to each other, making scores batch-independent and cacheable.
- **VFFilter** — the post-selection visibility filter that removes deleted, spam, violence, and gore content.

### A.3 Honesty boundary (what we cannot know from the OSS)

This report deliberately avoids several claims that would require information not in the public release:

- **Numeric weight values.** `FAVORITE_WEIGHT`, `REPLY_WEIGHT`, `RETWEET_WEIGHT`, `OON_WEIGHT_FACTOR`, `NEW_USER_OON_WEIGHT_FACTOR`, `AUTHOR_DIVERSITY_DECAY`, `AUTHOR_DIVERSITY_FLOOR`, `MIN_VIDEO_DURATION_MS`, `NEGATIVE_SCORES_OFFSET`, `WEIGHTS_SUM`, `NEGATIVE_WEIGHTS_SUM`, and every other constant referenced as `crate::params::*` are external configuration. The repo contains no `params.rs` (verified). Any report — including future versions of this one — that quotes specific numerical multipliers for the 2026 algorithm is fabricating data.
- **Production model behavior.** The released Phoenix checkpoint is a mini model (2 layers, 4 heads, 256-dim per `phoenix/README.md`) trained on a 537K-post sports corpus. Production Phoenix is larger and continuously trained on full engagement traffic. Inference against the released artifacts demonstrates *what kinds of features the model uses* and *how scores behave structurally*, not what the production model returns.
- **Stub integrations.** Several Thrift serialization boundaries panic with `"Not implemented: to_thrift for ..."` (in `candidate_features.rs` and `user_features.rs`). The public code does not run end-to-end against X's internal services as-shipped.
- **Policy data.** Brand-safety brand lists, topic ID mappings, language-penalty tables, ad-blending rules, the contents of the muted-keyword corpora, and the trained spam / safety / PTOS classifier weights are not in the open release. The code paths that consume them exist; the data does not.
- **Continuous retraining cadence.** The OSS release is a static snapshot. The production model is continuously updated. Any claim about "what the algorithm is doing right now" based on reading this code is at best a structural statement; the model's specific predictions at any given moment depend on training updates that are not public.

What this report *does* claim, and where the confidence is high: the architecture (Thunder + Phoenix + Home Mixer + Grox), the candidate sources, the filter set, the 19-action surface, the structural form of the score formula, the existence and direction of the OON penalty and author-diversity decay, the existence of the video-duration gate, the offline-gate model for content classification, the role of user action sequences as Phoenix's primary input, and the deletion of hand-engineered features in favor of transformer learning. All of these are read directly from the released code and READMEs, cited inline.
