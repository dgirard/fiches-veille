---
themes: [architecture-construction, strategie-frameworks]
source: "Rapport interne · [HTML long](https://raw.githack.com/dgirard/fiches-veille/main"
---
# x-algorithm-teardown-growth-recommendations-2026-05-16

## Veille

Rapport interne de teardown du release open-source **`xai-org/x-algorithm`** (15 mai 2026) — l'algorithme **For You feed** de **X (ex-Twitter)** en 2026, avec quatre pistes de recommandations growth audience-tunées (personal/founder, brand/company, framework généralisé, livrable client/consulting). **Thèse-pivot** : ***« The famous 2023 weight table — replies count more than likes by a big multiplier — describes a system that no longer exists in this form. »*** L'algorithme 2026 est un **transformeur (Phoenix, dérivé Grok-1)** qui apprend les poids depuis ton historique d'engagement, scoré contre une **surface multi-actions à 19 dimensions**, gatée par un service offline de content understanding (**Grox**). **La forme du scoring importe désormais beaucoup plus que les nombres — et les nombres eux-mêmes ne sont pas dans le release public**. **Architecture en 4 composants** : (1) **Home Mixer** (Rust, orchestrateur request-time, hydrate → source → filter → score → select → filter) ; (2) **Thunder** (Rust, in-memory store Kafka-fed des posts récents, lookups sub-ms des candidats in-network) ; (3) **Phoenix** (JAX ML, retrieval two-tower + ranking transformeur, ~Grok-1 dérivé) ; (4) **Grox** (offline, classifieurs spam/safety/PTOS/banger + embedder multimodal v5). **Les 19 actions prédites par Phoenix** (changement-clé vs 2023) : favorite, reply, repost, photo_expand, click, profile_click, vqv (video quality view gated by min duration), share, share_via_dm, share_via_copy_link, dwell, quote, quoted_click, follow_author, not_interested, block_author, mute_author, report, dwell_time (continuous). **Score final** = `Σ (weight × P(action))` modifié par **3 multiplicateurs structurels** : (a) **OON_WEIGHT_FACTOR < 1** (pénalité out-of-network), (b) **author diversity decay** `(1-floor) × decay_factor^position + floor` (atténuation exponentielle des posts répétés du même auteur dans un même render), (c) **video duration gate** (vqv ne contribue que si `video_duration_ms > MIN_VIDEO_DURATION_MS`). **Caveat capital** : **aucune valeur numérique des poids** (`FAVORITE_WEIGHT`, `OON_WEIGHT_FACTOR`, `AUTHOR_DIVERSITY_DECAY`, `MIN_VIDEO_DURATION_MS`...) n'est dans le release — tout est `crate::params::*`, géré par un feature-switch service interne X pour A/B testing. ***« Anyone telling you 'replies are worth N.N× more than likes in 2026' is fabricating a number that is not derivable from the OSS release. »*** **Différences-clés vs 2023** : (1) suppression de toute feature hand-engineered (*« We have eliminated every single hand-engineered feature and most heuristics from the system »*) ; (2) un seul modèle prédisant 19 actions vs plusieurs modèles 1 action chacun ; (3) Grox sépare content understanding et ranking ; (4) nouveaux signaux first-class (dwell continu, vqv gated, follow_author, 3 variantes de share) ; (5) two-tower OON retrieval (vs SimClusters+heuristics) avec embeddings multimodaux text+image+ASR-video. **Three layers of reach** (framework généralisé) : Eligibility (binary, Grox+filtres) → Retrieval (probabilistic, two-tower ANN) → Ranking (continuous, weighted-sum + multipliers). **Two laws of mechanical growth** : (1) In-network is multiplicative, OON is additive ; (2) The model's job is to predict you, not reward you. **Boundary d'honnêteté assumée** : checkpoint Phoenix released = mini (2 layers, 4 heads, 256-dim, corpus 537K posts sports), pas le modèle prod ; intégrations Thrift stubbées (`panic!("Not implemented")` dans `candidate_features.rs`) ; brand-safety lists, topic ID mappings, language penalties, ad-blending rules absents du public.

## Titre Article

How the X Algorithm Actually Works in 2026 — and What That Means for Growth

## Date

2026-05-16

## URL

- **Rapport long (HTML, Sharp Artisan, FR)** : https://raw.githack.com/dgirard/fiches-veille/main/docs/report/x-algorithm-growth-report.html
- **Slides 16:9 (HTML, Sharp Artisan, FR, 22 slides)** : https://raw.githack.com/dgirard/fiches-veille/main/docs/report/x-algorithm-slides.html
- **Source markdown** : `docs/report/x-algorithm-growth-report.md`
- **Repo source analysé** : https://github.com/xai-org/x-algorithm (release 15 mai 2026)

## Keywords

X algorithm 2026, xai-org/x-algorithm, For You feed, Phoenix transformer, Grok-1 derived, Home Mixer Rust, Thunder Kafka in-memory store, Grox offline content understanding, JAX ML service, two-tower retrieval, multimodal post embedder v5, ASR transcript video, candidate isolation attention, 19 actions surface, favorite reply repost share, dwell continuous vs binary, vqv video quality view, follow_author prediction, share_via_dm share_via_copy_link, NEGATIVE_FEEDBACK_INDICES not_interested block mute report, weighted scorer formula, OON_WEIGHT_FACTOR out-of-network penalty, NEW_USER_OON_WEIGHT_FACTOR onboarding bias, author_diversity_scorer exponential decay, decay_factor position floor formula, MIN_VIDEO_DURATION_MS video gate, hand-engineered features eliminated, user action sequence transformer input, mutual_follow_jaccard_hydrator, following_replied_users_hydrator, AuthorSocialgraphFilter bidirectional block, MutedKeywordFilter, PreviouslySeenPostsFilter, IneligibleSubscriptionFilter paywall, VFFilter visibility filter, DedupConversationFilter, Grox task_spam_detection, task_post_safety_screen_deluxe, task_safety_ptos_policy, task_banger_screen, task_reply_ranking, params.rs absent OSS, weights not in release, mini Phoenix checkpoint 2 layers 4 heads 256-dim, 537K sports posts corpus, Thrift to_thrift not implemented stub, brand-safety brand lists absent, topic ID mappings absent, language penalties absent, ad blending rules absent, three layers of reach eligibility retrieval ranking, action surface as product question, transformer as fairness mechanism, author-diversity decay as structural feature, negative signals one-shot vetoes cumulative cost, eligibility-time silent exclusion, in-network multiplicative OON additive, model predicts not rewards, personal founder voice growth tactics, brand company account playbook, generalized framework seven pillars, client consulting deliverable evidence table, action-targeted content design, author distribution playbook, video specification subtitled ASR-friendly, topic-embedding consistency, eligibility-gate audit, negative-signal hygiene, follower-acquisition reframing OON-to-Thunder conversion, May 15 2026 release, ads module brand-safety tracking, NEGATIVE_SCORES_OFFSET, WEIGHTS_SUM, NEGATIVE_WEIGHTS_SUM, NewUserAgeThresholdSecs, NEW_USER_MIN_FOLLOWING, structural model not quantitative predictor, semantic clarity over keyword overlap, embedding neighborhood density, 70/30 topical core exploratory split, employee amplification Thunder source union, product overhang feed render, candidate isolation batch-independent cacheable scores, P(action) per-user per-post not global, going viral as population-level outcome

## Authors

Rapport interne **non signé** (typique des deliverables d'analyse interne / brouillon de livrable client). Sources primaires citées : (a) le repo public **`xai-org/x-algorithm`** (release 15 mai 2026), (b) les `README.md` du repo et de ses sous-modules (`home-mixer/`, `phoenix/`, `thunder/`, `grox/`), (c) le code source Rust (Home Mixer, Thunder) et Python/JAX (Phoenix, Grox) inspecté directement avec citations file:line. Le rapport est explicitement écrit en posture *"what we observe in the public source release, and what it implies for measurable growth interventions"* — registre de teardown analytique avec discipline d'honnêteté épistémique (section A.3 *"Honesty boundary"* listant exhaustivement ce qui n'est pas dérivable de l'OSS).

## Ton

**Profil** : Teardown technique d'un release open-source d'algorithme de recommandation, structuré en deux parties asymétriques (**Part 1 — Teardown** descriptive et citationnelle, **Part 2 — Recommendations** prescriptive et audience-segmentée) suivies d'un **Appendix** (file index, glossaire, honesty boundary). Format hybride entre **livre blanc consulting** (evidence table, recommended cadence Month 1/2/3, executive summary pour cover page) et **rétro-engineering documentaire** (citations file:line, distinction sign vs magnitude, discussion explicite des `panic!("Not implemented")` stubs). Volumétrie : ~470 lignes markdown, ~12000 mots, dense.

**Public** : Quatre audiences explicitement adressées par Part 2 (A=personal/founder, B=brand/company, C=generalized framework, D=client/consulting deliverable). Auditoire englobant : créateurs sur X, équipes growth/marketing de marques, analystes algorithmes, consultants growth, cadres de plateformes concurrentes, chercheurs en systèmes de recommandation.

**Style** : Voix **analytique-désillusionnée** d'expert qui a lu le code et refuse l'industrie du *"X algorithm hacks"*. Trois marqueurs distinctifs :

1. **Honnêteté épistémique aggressive** — Le rapport répète, en gras et en italique à plusieurs endroits, que les valeurs numériques des poids ne sont pas dans le release : ***« Anyone telling you 'replies are worth N.N× more than likes in 2026' is fabricating a number that is not derivable from the OSS release »***. Une section entière (A.3) est dédiée à *« what we cannot know from the OSS »*. Les claims de magnitude sont marqués `(directional)` ; les claims de direction (sign, presence d'un gate) sont cités file:line. Cette discipline est l'autorité même du texte.

2. **Citations file:line systématiques** — Chaque affirmation structurelle vient avec sa source : `home-mixer/scorers/oon_scorer.rs:20-23`, `phoenix/runners.py:233-252`, `author_diversity_scorer.rs:29-31`. La section *Evidence table* du livrable consulting (Part 2.D) liste 14 claims principaux avec leurs file:line. Posture *"if a creator pushes back, cite X"* (Part 2.A pillier 7).

3. **Architecture en piliers transposables** — Les 7 piliers (in-network advantage, P(action) framing, high-weight actions, diversity decay, negative signals, two-tower retrievability, Grox/VF eligibility) sont **rigoureusement les mêmes** entre les recommandations Personal, Brand, et le framework généralisé — seules les tactiques par pilier changent. Effet : les sections sont **comparables ligne à ligne**, ce qui valide la grille d'analyse comme une grille et non comme une liste improvisée.

**Métaphores et formules-clés** :
- ***« The shape of scoring matters far more than the numbers »*** — phrase-pivot du caveat épistémique.
- ***« Going viral is a population-level outcome of many independent personal predictions clearing the bar, not a single metric Phoenix optimizes »*** — démantèlement de l'imaginaire du « post viral ».
- ***« Borderline content doesn't get 'demoted' in the 2026 system. It gets disqualified at hydration time and never reaches scoring »*** — la différence structurelle 2023 → 2026 la plus politiquement chargée (eligibility-time silent exclusion vs visibility filtering).
- ***« Three layers of reach »*** : Eligibility (binary) → Retrieval (probabilistic) → Ranking (continuous). Cadre pédagogique de Part 2.C.
- ***« Two laws of mechanical growth »*** : *In-network is multiplicative, OON is additive* ; *The model's job is to predict you, not reward you*.
- ***« Eligibility-time exclusion is the silent killer »*** — phrase la plus politique du rapport.
- ***« There is no signal to the creator that a Grox classifier excluded their post from candidate pools »*** — implication transparency.
- ***« The optimal cadence is non-monotonic in post count »*** — anti-intuitif growth.
- ***« Subtitle your videos for the model, not just for the viewer »*** — tactique concrète embedder-aware.
- ***« Stop optimizing for total likes; total likes are a population artifact »*** — recadrage du KPI primaire.

**Position épistémique** : Le rapport refuse simultanément (a) le **technosolutionnisme growth-hack** (*"5 secrets to game the algorithm"*) qui prétend des magnitudes non dérivables ; (b) le **scepticisme conspirationniste** (*"on ne peut rien savoir, tout est boîte noire"*) qui ignore ce qui est lisible dans le code. Posture intermédiaire : *« structural levers that are documented in code »* — on peut prescrire à partir de la **forme** du système même quand on n'a pas les **paramètres**. Cette position est rare et méthodologiquement solide.

**Autorité construite par** : (a) **traçabilité file:line** sur chaque claim structurel ; (b) **discipline du caveat** (sections *Limitations and honest disclosures* dans le livrable client, *Honesty boundary* en appendice) ; (c) **comparabilité interne** des recommandations (mêmes piliers, audiences différentes) ; (d) **refus explicite de la fabrication numérique** (le rapport pointe spécifiquement les analyses qui inventent des poids comme malhonnêtes) ; (e) **identification proactive des stubs** (`panic!("Not implemented")` dans `candidate_features.rs`, modèle mini Phoenix entraîné sur 537K posts sports) — le rapport vend autant ses limites que ses claims.

**Public et impact attendu** : Le rapport est calibré pour **outiller un consultant ou un growth lead** avec un cadre méthodologique opérable face à des clients/équipes qui demandent *"comment marche l'algo X en 2026"*. La structure quadruple (personal/brand/framework/client) suggère un usage de **boîte à outils modulaire** : tu prends la section qui correspond à ton interlocuteur. Le **livrable consulting (Part 2.D)** est presque tel quel un *brief client* prêt à l'envoi, avec evidence table, recommended interventions priorisées, cadence Month 1/2/3, et section *limitations and honest disclosures* obligatoire. Cible primaire : praticiens growth/consulting. Cible secondaire : analystes algorithmes, journalistes tech, équipes plateformes concurrentes voulant comparer leur architecture.

## Pense-betes

- **Source primaire** : release open-source **`xai-org/x-algorithm`** du **15 mai 2026**. Le rapport date du 2026-05-16 (probable J+1 du release). Date d'ajout dossier veille : 2026-05-16 (= aujourd'hui).

- **4 composants architecturaux** :
  - **Home Mixer** (`x-algorithm/home-mixer/`) — orchestrateur Rust request-time, pipeline `hydrate → source → hydrate → filter → score → select → filter`.
  - **Thunder** (`x-algorithm/thunder/`) — Rust in-memory store Kafka-fed des posts récents, lookups sub-millisecond pour candidats **in-network**. Fichiers clés : `thunder/main.rs`, `thunder/post_store.rs`, `thunder/kafka_utils.rs`.
  - **Phoenix** (`x-algorithm/phoenix/`) — service JAX ML, **deux rôles** : (1) **retrieval two-tower** pour OON, (2) **ranking** transformeur dérivé Grok-1 prédisant 19 actions.
  - **Grox** (`x-algorithm/grox/`) — service **offline** de content understanding, classifieurs (spam, safety, PTOS, banger, reply ranking) + embedder multimodal v5. **Ne sit pas dans le hot path** ; écrit au feature store, Home Mixer hydrate les signaux.

- **Pipeline Home Mixer (architecture quoted from README)** :
  1. Query hydration (User Action Sequence + User Features)
  2. Candidate sources (Thunder in-network + Phoenix retrieval OON + ads + who-to-follow + topics + MoE + prompts)
  3. Hydration (core metadata, author info, media, engagement counts)
  4. Filtering pre-scoring (dedupe, age, self, blocks, mutes, paywall, already-seen)
  5. Scoring (Phoenix Scorer P(action) for each of 19 actions → Weighted Scorer Σ(weight × P) → Author Diversity → OON Scorer)
  6. Selection (sort by final score, select top K)
  7. Post-selection filters (VFFilter for deletes/spam/violence/gore, conversation dedup)

- **Les 19 actions prédites par Phoenix** (`phoenix/runners.py:233-252`, `home-mixer/candidate_pipeline/candidate.rs:30-51` `PhoenixScores`) :
  - **Positifs** : 0 favorite, 1 reply, 2 repost, 3 photo_expand, 4 click, 5 profile_click, 6 vqv (gated), 7 share, 8 share_via_dm, 9 share_via_copy_link, 10 dwell, 11 quote, 12 quoted_click, 13 follow_author, 18 dwell_time (continuous)
  - **Négatifs** (`NEGATIVE_FEEDBACK_INDICES = [14, 15, 16, 17]`) : 14 not_interested, 15 block_author, 16 mute_author, 17 report

- **Nouveaux signaux first-class vs 2023** : continuous `dwell_time` (et pas seulement binaire), `vqv_score` (gated by `MIN_VIDEO_DURATION_MS`), `follow_author_score` (Phoenix prédit *"ce post fera-t-il gagner un follower à son auteur"*), 3 variantes de share (`share`, `share_via_dm`, `share_via_copy_link`).

- **Formule de score** (`home-mixer/scorers/weighted_scorer.rs:44-91`) :
  ```
  score = Σ_i (weight_i × P(action_i))
        × OON_WEIGHT_FACTOR (if OON, else 1)
        × diversity_multiplier(position)
        + offset_score()  (keeps negative aggregates well-ordered)
  ```
  où `vqv_weight` est remplacé par 0 si `video_duration_ms ≤ MIN_VIDEO_DURATION_MS`.

- **Caveat CAPITAL — les poids ne sont pas dans le release** :
  - `FAVORITE_WEIGHT`, `REPLY_WEIGHT`, `RETWEET_WEIGHT`, `OON_WEIGHT_FACTOR`, `NEW_USER_OON_WEIGHT_FACTOR`, `AUTHOR_DIVERSITY_DECAY`, `AUTHOR_DIVERSITY_FLOOR`, `MIN_VIDEO_DURATION_MS`, `NEGATIVE_SCORES_OFFSET`, `WEIGHTS_SUM`, `NEGATIVE_WEIGHTS_SUM` sont tous référencés comme `crate::params::*`.
  - **Aucun `params.rs` n'existe dans le repo** (vérifié par `grep -rn` exhaustif).
  - Géré par un **feature-switch / parameter service interne** X pour A/B testing et tuning sans code change.
  - **Implication** : seules les **directions** (positif vs négatif, gate vs soft adjustment, présence vs absence d'un multiplicateur) sont citables. Les **magnitudes** sont fabriquées.

- **3 multiplicateurs structurels** (importance > weights individuels) :
  - **OON penalty** (`oon_scorer.rs:20-23`) : `score = base_score × OON_WEIGHT_FACTOR if OON else base_score`. Comment de la ligne 7 : *« Prioritize in-network candidates over out-of-network candidates »*. **Codification de "followers matter"**.
  - **New-user OON exception** (`ranking_scorer.rs:220-239`) : si compte < `NewUserAgeThresholdSecs` ET follows ≥ `NEW_USER_MIN_FOLLOWING`, la pénalité OON est remplacée par `NEW_USER_OON_WEIGHT_FACTOR`. **Biais structurel** sur ce que voient les nouveaux comptes (et donc ce que les nouveaux comptes peuvent atteindre).
  - **Author diversity decay** (`author_diversity_scorer.rs:29-31`) : `multiplier(position) = (1 - floor) × decay_factor^position + floor`. Position = nombre de posts du même auteur déjà apparus plus haut dans la liste triée. **Le meilleur post d'un auteur garde son score, chaque suivant est atténué exponentiellement** sans descendre sous `floor`. **Implication cadence** : structurelle, pas heuristique.

- **Video duration gate** (`weighted_scorer.rs:72-81`) : `vqv_score` n'entre dans la somme pondérée que si `video_duration_ms > MIN_VIDEO_DURATION_MS`. **Hard gate, pas soft penalty** : les clips trop courts ne reçoivent simplement pas la contribution VQV.

- **What never enters the ranker** (reach perdue invisible) :
  - **Pre-scoring filters** : `DropDuplicatesFilter`, `CoreDataHydrationFilter`, `AgeFilter`, `SelfpostFilter`, `RepostDeduplicationFilter`, `IneligibleSubscriptionFilter` (paywall), `PreviouslySeenPostsFilter`, `PreviouslyServedPostsFilter`, `MutedKeywordFilter`, `AuthorSocialgraphFilter` (block dans les deux sens, **y compris l'auteur cité d'un quote tweet**).
  - **Post-selection filters** : `VFFilter` (deleted/spam/violence/gore), `DedupConversationFilter`.
  - **Grox offline gates** (eligibility, **pas** modificateurs de score) : `task_spam_detection.py` / `classifiers/content/spam.py`, `task_post_safety_screen_deluxe.py`, `task_safety_ptos_policy.py`, `task_banger_screen.py` (positif), `task_reply_ranking.py`.
  - **Point architectural fondamental** : *« Borderline content doesn't get 'demoted' in the 2026 system. It gets disqualified at hydration time and never reaches scoring. This is materially different from the 2023 system's reduced-reach / visibility-filtering model. »*

- **What Phoenix actually learns from** :
  - **L'input le plus conséquent = la séquence d'actions de l'utilisateur** (`user_action_seq_query_hydrator.rs`), pas le candidat post.
  - **Candidate-isolation attention** (`phoenix/recsys_model.py`) : les candidats peuvent attendre la séquence d'actions de l'utilisateur, **mais pas entre eux** → scores **per-user per-post**, **batch-independent**, **cacheables**.
  - **Pas de single "this post is good" global** : *"the same post predicted to earn a like from User A at probability p₁ is predicted at p₂ for User B"*.
  - **Going viral** = outcome population-level de prédictions personnelles indépendantes, pas une métrique optimisée.
  - **Hand-engineered features supprimées** (`README` ligne 55) : *"We have eliminated every single hand-engineered feature and most heuristics from the system."*
  - **Deux signaux explicitement hydratés** quand même : `mutual_follow_jaccard_hydrator.rs` (Jaccard followers viewer ∩ followers auteur candidat), `following_replied_users_hydrator.rs` (un follow du viewer a répondu au candidat).

- **OON retrieval (two-tower)** : ton historique d'action → embedding user, posts candidats → embeddings post (depuis `grox/embedder/multimodal_post_embedder_v5.py` qui encode text+images+ASR transcript du vidéo en 1024-dim normalisé). **Ta discoverability par des strangers est fonction de la proximité d'embedding entre tes posts et ceux que ton audience cible engage déjà.**

- **5 différences load-bearing vs 2023** :
  1. **Pas de feature hand-engineered** (2023 avait verified status, paid subscribers, network distance explicites).
  2. **Un modèle prédisant 19 actions** vs plusieurs modèles 1 action chacun.
  3. **Grox sépare content understanding et ranking** (`grox/plan_master.py` orchestre 9 plans parallèles).
  4. **Nouveaux signaux first-class** (dwell continu, vqv gated, follow_author, 3 variantes share).
  5. **Two-tower OON retrieval** (vs SimClusters + heuristics 2023).

### 7 piliers (récurrents Personal / Brand / Framework)

1. **In-network advantage** (`oon_scorer.rs:20-23`) — OON × factor < 1.
2. **P(action) framing** (`phoenix/recsys_model.py`) — per-user probabilities.
3. **High-weight actions** (`weighted_scorer.rs:49-67`) — choisir lesquelles déclencher parmi 19.
4. **Diversity decay** (`author_diversity_scorer.rs:29-31`) — `(1-floor) × decay_factor^position + floor`.
5. **Negative signals** (`weighted_scorer.rs:64-67` + `AuthorSocialgraphFilter` + `MutedKeywordFilter`) — soustractions directes + hard gates.
6. **Two-tower retrievability** (`phoenix_source.rs` + `multimodal_post_embedder_v5.py`) — embedding proximity vers ton audience cible.
7. **Grox / VF eligibility** (`grox/plan_master.py` + `home-mixer/filters/vf_filter.rs`) — exclusion silencieuse, pas démotion.

### Recommandations Personal / Founder (Part 2.A) — synthèse

- **Pillar 1** : convertir relations IRL en follows (DM, podcasts cross-promo, newsletters footers, replies) = tax OON → lookup Thunder déterministe.
- **Pillar 2** : nommer **une action cible par post** (reply, follow, dwell, share). *"When you can't articulate which action you're aiming at, the post is unlikely to score well for any of them."*
- **Pillar 3** : trigger high-weight actions perso :
  - Reply : questions à réponse défendable (pas *"what do you think?"*).
  - Dwell time : threads et long-form (continuous dwell signal index 18).
  - Profile click : stranger qui veut savoir qui tu es (bio-relevant signaling).
  - Follow-author : *"here is my premise and I will defend it across many future posts"*.
- **Pillar 4** : **publier ton meilleur post en premier** (le 1er garde le score plein, le 2e est atténué). Ne pas stacker, espacer.
- **Pillar 5** : éviter mute/block des followers chauds (négatif **cumulatif** sur tous tes posts futurs pour cet utilisateur).
- **Pillar 6** : multimodal (text + image + video) = 3 shots d'embedding.
- **Pillar 7** : trop de @mentions / link spam patterns → spam classifier silent exclusion.

### Recommandations Brand / Company (Part 2.B) — synthèse

- **Pillar 1** : **employee amplification** = union des in-network de chaque employé via Thunder.
- **Pillar 2** : reporter **action distribution per post** vs impressions totales.
- **Pillar 3** : actions brand-relevant :
  - Click (index 4) + quoted click (index 12) = trafic site.
  - **VQV** (index 6) = vidéos qui clear `MIN_VIDEO_DURATION_MS`. *"Cutting a video too short kills the contribution entirely."*
  - **Share via DM** (index 8) + **share via copy-link** (index 9) = pricing teardowns, product comparisons, controversy forwarded privately.
  - Follow-author (index 13) = un post/semaine *follow magnet*.
- **Pillar 4** : *« A 'drumbeat' of four posts spaced 30 minutes apart underperforms the single best one of them, alone »*. Coordonner brand + CEO + employés (auteurs distincts) **bat** brand seul posting 2x.
- **Pillar 5** : `home-mixer/ads/` module ajouté 15 mai 2026 = **brand-safety tracking**. Organic posts près de sensitive content → risque adjacency.
- **Pillar 6** : **topical consistency over weeks** (embedding dilué si trop de sujets), multimodal posts, **subtitle videos for the ASR path**.
- **Pillar 7** : `task_spam_detection.py` keye sur low-follower / low-quality reply patterns → brands qui répliquent lourdement sur big posts peuvent être flaggés. **Reply substantively or not at all.**

### Framework généralisé (Part 2.C)

- **Three layers of reach** :
  1. **Eligibility** (Grox + filtres) — binary, in/out, no optimization beyond not being excluded.
  2. **Retrieval** (two-tower OON) — probabilistic, optimisé par **quoi** tu postes (topic, embedding, multimodal).
  3. **Ranking** (weighted sum + multipliers) — continuous, optimisé par **comment** tu postes (action triggered, cadence).
- **Action surface as product question** : 19 actions = 4 catégories (social: like/reply/quote/share ; private: DM-share, copy-link, dwell, photo expand ; identity: follow, profile click ; rejection: not-interested/block/mute/report). Un post qui ne cible aucune relation = prédit ~0 partout.
- **Transformer as fairness mechanism** : per-user probabilities → "good content" n'est pas une propriété globale. *Probabilistic targeting, not deterministic quality.*
- **Author-diversity decay as structural feature** : *« publishing more posts per day past a threshold reduces, not increases, total reach »*. Cadence optimale **non-monotone** en post count.
- **Negative signals as one-shot vetoes** : un mute coûte le post ET tous les suivants à cet utilisateur (entry permanente dans sa action sequence).
- **Eligibility-time exclusion = silent killer** : pas de signal au créateur quand un Grox classifier exclut. Diagnostic = analyse comparative de reach.
- **Two laws** :
  - **Law 1** : *In-network is multiplicative, OON is additive.* Followers compound on every future post.
  - **Law 2** : *The model's job is to predict you, not reward you.* Begging engagement / manufactured controversy → dégrade ta prédictabilité → downgrade des posts futurs.

### Livrable Consulting (Part 2.D) — points-clés

- **Executive summary** prêt cover page.
- **Evidence table** : 14 claims principaux, chacun avec file:line.
- **7 interventions recommandées ordered by expected impact** (toutes *directional*) :
  1. Action-targeted content design (target_action annoté en calendrier éditorial).
  2. Author distribution playbook (audit cadence vs decay, multi-account amplification).
  3. Video specification (`MIN_VIDEO_DURATION_MS` A/B test client-side, subtitles).
  4. Topic-embedding consistency (70/30 core/exploratory).
  5. Eligibility-gate audit (échantillon posts underperforming → check gate types).
  6. Negative-signal hygiene (quantifier mute rate cumulative cost).
  7. Follower-acquisition reframing (OON-to-Thunder conversion = multiplicative future reach).
- **Cadence** : M1 calendar+playbook+video / M2 topical audit + follower test / M3 cohort measurement + gate recalibration / Trimestriel : re-read `xai-org/x-algorithm`.
- **Limitations and honest disclosures (mandatory)** : weights non dérivables, mini checkpoint (2 layers, 4 heads, 256-dim), Thrift stubs (`panic!("Not implemented")`), brand-safety lists / topic ID mappings / language penalties / ad blending rules absents. *« The client should treat this report as a structural model, not a quantitative predictor. »*

### Honesty boundary (Appendix A.3) — ce qu'on ne peut PAS savoir

- **Valeurs numériques des poids** (toutes externes, pas de `params.rs`).
- **Comportement modèle production** : checkpoint released = 2 layers, 4 heads, 256-dim, **537K-post sports corpus**, prod Phoenix est plus gros et continuously trained.
- **Stub intégrations** : `panic!("Not implemented: to_thrift for ...")` dans `candidate_features.rs` et `user_features.rs`. **Le public code ne tourne pas end-to-end contre les services internes X.**
- **Policy data** : brand-safety brand lists, topic ID mappings, language-penalty tables, ad-blending rules, muted-keyword corpora, classifier weights spam/safety/PTOS = absent.
- **Continuous retraining cadence** : OSS = static snapshot, prod = continuously updated.

### Liens avec les fiches existantes

- **Convergence avec [[wallace-wells-nyt-magazine-ai-populism-altman-backlash-no-one-ready-2026-05-08]]** : le rapport documente factuellement la **mécanique structurelle** d'un algorithme qui façonne l'information politique à l'échelle de masse, là où Wallace-Wells documente la **réception populaire / backlash** des oligarques tech (incluant Musk). Le rapport montre que **"who reaches whom" est désormais déterminé par des transformers entraînés sur des sequences d'action personnelles** — et que la **silent exclusion** (eligibility-time, sans signal) est un mode d'opération assumé.
- **Convergence avec [[ng-the-batch-352-no-ai-jobpocalypse-2026-05-08]]** : même posture épistémique anti-narrative, discipline de *"ce qui est dérivable des faits vs ce qui est fabriqué"*. Ng démantèle le narratif jobpocalypse ; ce rapport démantèle les narratifs de growth-hack basés sur des poids fabriqués.
- **Convergence implicite avec [[mensch-mistral-commission-enquete-vulnerabilites-numeriques-souverainete-ia-2026-05-13]]** : Mensch parle de **dépendance aux services numériques étrangers** comme risque de vassalisation. Le release d'algorithme `xai-org/x-algorithm` est un précédent ambigu — opensource partiel d'un système qui régit la conversation publique, mais avec **les paramètres opérationnels (les weights) intentionnellement absents**.
- **Anti-narrative growth-hack** : ce rapport est la **réponse documentaire** à l'industrie des "X algorithm secrets / 5 tactics to game the For You feed". Discipline de la citation file:line vs anecdote.
- **Pattern Anthropic-vs-X transparency** : ce rapport peut servir de **point de comparaison** méthodologique pour évaluer la transparence relative des releases d'algorithmes des grands labs (Anthropic Mythos, OpenAI evals, xAI grok-1, xai-org/x-algorithm). **Forme de la transparence** : assez de code pour décrire l'architecture, pas assez de paramètres pour reproduire le comportement.

## RésuméDe400mots

Le 15 mai 2026, xAI publie en open-source `xai-org/x-algorithm`, l'algorithme **For You feed** de **X**. Ce rapport interne en fait un teardown technique en deux parties : **(1) un démontage du système** avec citations file:line, et **(2) quatre pistes de recommandations growth** segmentées par audience (personal/founder, brand, framework généralisé, livrable consulting).

**Thèse-pivot** : la fameuse *« table de poids 2023 »* (*"replies count more than likes by a big multiplier"*) **décrit un système qui n'existe plus**. L'algorithme 2026 est un **transformeur (Phoenix, dérivé Grok-1)** qui apprend les pondérations depuis l'historique d'engagement personnel et score chaque candidat contre une **surface de 19 actions distinctes**, gatée par un service offline (**Grox**). **La forme du scoring importe plus que les nombres — et les nombres ne sont pas dans le release.**

**Architecture en 4 composants** : **Home Mixer** (Rust, orchestrateur), **Thunder** (Rust, in-memory store Kafka-fed, candidats in-network sub-ms), **Phoenix** (JAX, retrieval two-tower + ranking transformeur), **Grox** (offline, classifieurs et embedder multimodal v5 text+image+ASR-video).

**Les 19 actions prédites par Phoenix** combinent positifs (favorite, reply, repost, click, profile_click, vqv gated, share, share_via_dm, share_via_copy_link, dwell, quote, quoted_click, follow_author, dwell_time continuous) et négatifs (not_interested, block, mute, report). **Score final** = `Σ (weight × P(action))` modifié par 3 multiplicateurs structurels : **OON_WEIGHT_FACTOR < 1** (pénalité out-of-network), **author diversity decay** `(1-floor) × decay_factor^position + floor`, et **video duration gate** (vqv contribue uniquement si video > `MIN_VIDEO_DURATION_MS`).

**Caveat capital** : **aucune valeur numérique des poids n'est dans le release** (tout est `crate::params::*`, pas de `params.rs`). ***« Anyone telling you 'replies are worth N.N× more than likes in 2026' is fabricating a number. »*** Seules les **directions** (signe, gate vs soft adjustment, présence) sont citables.

**Three layers of reach** : Eligibility (binary, Grox) → Retrieval (probabilistic, two-tower) → Ranking (continuous, weighted sum). **Two laws of mechanical growth** : (1) In-network est multiplicatif, OON est additif ; (2) Le job du modèle est de te **prédire**, pas de te récompenser.

**Différences vs 2023** : suppression des features hand-engineered, un modèle pour 19 actions vs plusieurs modèles, Grox sépare understanding et ranking, nouveaux signaux first-class (dwell continu, vqv gated, follow_author, 3 variantes de share), two-tower OON retrieval avec embeddings multimodaux. **Eligibility-time exclusion is the silent killer** : borderline content n'est plus démoté, il disparaît du pool de candidats sans signal au créateur.

**Honesty boundary** : checkpoint released = mini (2 layers, 4 heads, 256-dim, corpus 537K posts sports), Thrift stubs (`panic!("Not implemented")`), policy data absent. Le rapport doit être traité comme **modèle structurel**, pas prédicteur quantitatif.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| xAI | ORGANISATION | publie | x-algorithm (release open-source) | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| xAI | ORGANISATION | publie | release x-algorithm du 15 mai 2026 | EVENEMENT | 0.99 | STATIQUE | déclaré_article |
| Home Mixer + Thunder + Phoenix + Grox | TECHNOLOGIE | fait_partie_de | x-algorithm | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Home Mixer | TECHNOLOGIE | utilise | Rust | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Home Mixer | TECHNOLOGIE | dirige | pipeline For You feed (orchestration) | METHODOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Thunder | TECHNOLOGIE | permet | lookups sub-ms des posts récents in-network | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Thunder | TECHNOLOGIE | utilise | Kafka | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Phoenix | TECHNOLOGIE | est_basé_sur | Grok-1 | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Phoenix | TECHNOLOGIE | utilise | JAX | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Phoenix | TECHNOLOGIE | prédit | 19 actions par candidat | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Phoenix | TECHNOLOGIE | utilise | candidate-isolation attention | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Phoenix retrieval | TECHNOLOGIE | utilise | two-tower model | METHODOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Grox | TECHNOLOGIE | est_instance_de | service offline (hors hot path) | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Grox | TECHNOLOGIE | utilise | feature store (écriture) | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| multimodal_post_embedder_v5 | TECHNOLOGIE | utilise | text + images + ASR transcript video | CONCEPT | 0.98 | STATIQUE | déclaré_article |
| multimodal_post_embedder_v5 | TECHNOLOGIE | permet | embedding normalisé 1024-dim | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Weighted Scorer | TECHNOLOGIE | utilise | formule Σ (weight × P(action)) sur 19 actions | METHODOLOGIE | 0.99 | STATIQUE | déclaré_article |
| OON Scorer | TECHNOLOGIE | utilise | multiplicateur OON_WEIGHT_FACTOR < 1 | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Author Diversity Scorer | TECHNOLOGIE | utilise | (1-floor) × decay_factor^position + floor | METHODOLOGIE | 0.98 | STATIQUE | déclaré_article |
| vqv_score | CONCEPT | est_basé_sur | MIN_VIDEO_DURATION_MS (hard gate) | CONCEPT | 0.98 | STATIQUE | déclaré_article |
| [14, 15, 16, 17] = not_interested block mute report | CONCEPT | fait_partie_de | NEGATIVE_FEEDBACK_INDICES | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| x-algorithm 2026 | TECHNOLOGIE | utilise | dwell_time continu comme signal first-class (nouveau vs 2023) | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| x-algorithm 2026 | TECHNOLOGIE | utilise | follow_author_score comme signal first-class (nouveau vs 2023) | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| share_via_dm + share_via_copy_link | CONCEPT | est_variante_de | share standard (signaux distincts) | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| x-algorithm 2026 | TECHNOLOGIE | remplace | features hand-engineered (toutes éliminées) | METHODOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Phoenix transformer | TECHNOLOGIE | est_basé_sur | user action sequence (apprentissage) | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| Phoenix scores | CONCEPT | est_instance_de | scores per-user per-post (pas globaux) | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| "going viral" | CONCEPT | est_instance_de | population-level outcome de prédictions personnelles | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| rapport interne | DOCUMENT | affirme_que | params.rs (valeurs des poids) est absent du release open-source | AFFIRMATION | 0.99 | STATIQUE | déclaré_article |
| X | ORGANISATION | utilise | feature-switch service interne pour gérer FAVORITE_WEIGHT, REPLY_WEIGHT etc. | TECHNOLOGIE | 0.95 | DYNAMIQUE | inféré |
| rapport interne | DOCUMENT | affirme_que | quiconque cite des magnitudes de poids 2026 fabrique des chiffres | AFFIRMATION | 0.98 | ATEMPOREL | déclaré_article |
| AuthorSocialgraphFilter | TECHNOLOGIE | s_applique_à | blocks dans les deux sens incluant auteur cité du quote tweet | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Grox classifiers | TECHNOLOGIE | remplace | démotion 2023 par exclusion eligibility-time | METHODOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| rapport interne | DOCUMENT | affirme_que | l'exclusion eligibility-time est silencieuse pour le créateur (no signal) | AFFIRMATION | 0.97 | ATEMPOREL | déclaré_article |
| rapport interne | DOCUMENT | recommande | action-targeted content design (1 action cible par post) | METHODOLOGIE | 0.96 | ATEMPOREL | déclaré_article |
| rapport interne | DOCUMENT | recommande | author distribution playbook (multi-account amplification) | METHODOLOGIE | 0.96 | ATEMPOREL | déclaré_article |
| rapport interne | DOCUMENT | recommande | subtitler les vidéos pour l'ASR path (pas seulement le viewer) | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| rapport interne | DOCUMENT | recommande | 70/30 split topical core / exploratory | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| rapport interne | DOCUMENT | affirme_que | in-network is multiplicative, OON is additive | AFFIRMATION | 0.97 | ATEMPOREL | déclaré_article |
| rapport interne | DOCUMENT | affirme_que | the model's job is to predict you, not reward you | AFFIRMATION | 0.97 | ATEMPOREL | déclaré_article |
| Phoenix checkpoint released | TECHNOLOGIE | est_instance_de | mini model (2 layers, 4 heads, 256-dim) | CONCEPT | 0.98 | STATIQUE | déclaré_article |
| Phoenix checkpoint released | TECHNOLOGIE | est_basé_sur | corpus 537K posts sports (entraînement) | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| panic!("Not implemented: to_thrift for ...") stubs | CONCEPT | fait_partie_de | candidate_features.rs / user_features.rs | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| rapport interne | DOCUMENT | affirme_que | brand-safety lists, topic ID mappings, language penalties et ad blending sont absents du release | AFFIRMATION | 0.97 | STATIQUE | déclaré_article |
| home-mixer/ads/ module | TECHNOLOGIE | fait_partie_de | release x-algorithm du 15 mai 2026 | EVENEMENT | 0.94 | STATIQUE | déclaré_article |
| home-mixer/ads/ module | TECHNOLOGIE | permet | brand-safety tracking | METHODOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| author diversity decay | METHODOLOGIE | soutient | cadence optimale non-monotone en post count | CONCEPT | 0.95 | ATEMPOREL | inféré |
| mute ou block utilisateur | CONCEPT | réduit | reach de tous les posts futurs vers cet utilisateur (cumulatif) | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| NEW_USER_OON_WEIGHT_FACTOR | CONCEPT | s_applique_à | nouveaux comptes (jeune compte + min following) | CONCEPT | 0.96 | DYNAMIQUE | déclaré_article |
| rapport x-algorithm 2026 | DOCUMENT | converge_avec | démantèlement narratif jobpocalypse [[ng-the-batch-352-no-ai-jobpocalypse-2026-05-08]] | CONCEPT | 0.90 | DYNAMIQUE | inféré |
| rapport x-algorithm 2026 | DOCUMENT | converge_avec | AI populism + algorithmic information shaping [[wallace-wells-nyt-magazine-ai-populism-altman-backlash-no-one-ready-2026-05-08]] (documentation de la mécanique) | CONCEPT | 0.89 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| xAI | ORGANISATION | secteur | Laboratoire IA d'Elon Musk, opère X (ex-Twitter) et le modèle Grok | AJOUT |
| x-algorithm | TECHNOLOGIE | catégorie | Algorithme For You feed de X publié en open-source sous `xai-org/x-algorithm` le 15 mai 2026, ~4 composants Rust+Python/JAX | AJOUT |
| Home Mixer | TECHNOLOGIE | rôle | Orchestrateur Rust request-time du pipeline For You feed (hydrate → source → filter → score → select → filter) | AJOUT |
| Thunder | TECHNOLOGIE | rôle | Service Rust in-memory Kafka-fed, lookups sub-ms des posts in-network récents | AJOUT |
| Phoenix | TECHNOLOGIE | rôle | Service JAX ML, transformer dérivé Grok-1, fait à la fois retrieval (two-tower) et ranking (prédit 19 actions par candidat) | AJOUT |
| Grox | TECHNOLOGIE | rôle | Service offline de content understanding (classifieurs spam/safety/PTOS/banger + embedder multimodal v5), écrit vers feature store | AJOUT |
| Grok-1 | TECHNOLOGIE | catégorie | Modèle LLM dont Phoenix (ranker X) est dérivé, base architecture transformer | AJOUT |
| 19 actions surface | CONCEPT | définition | Vecteur 19 dimensions prédit par Phoenix par candidat : 15 positifs (favorite, reply, repost, photo_expand, click, profile_click, vqv, share, share_via_dm, share_via_copy_link, dwell, quote, quoted_click, follow_author, dwell_time) + 4 négatifs (not_interested, block_author, mute_author, report) | AJOUT |
| OON_WEIGHT_FACTOR | CONCEPT | définition | Multiplicateur < 1 appliqué au score des candidats out-of-network (oon_scorer.rs:20-23), codification de "followers matter" — valeur numérique externe au release | AJOUT |
| NEW_USER_OON_WEIGHT_FACTOR | CONCEPT | définition | Multiplicateur OON différent appliqué aux nouveaux comptes (< NewUserAgeThresholdSecs ET follow ≥ NEW_USER_MIN_FOLLOWING) — biaise ce que voient les nouveaux comptes et donc ce qu'ils atteignent | AJOUT |
| Author Diversity Decay | METHODOLOGIE | définition | Formule `(1 - floor) × decay_factor^position + floor` appliquée à chaque post répété du même auteur dans un même render — atténuation exponentielle bornée par floor, structurelle pour la cadence | AJOUT |
| MIN_VIDEO_DURATION_MS | CONCEPT | définition | Seuil hard gate : si video_duration_ms ≤ MIN_VIDEO_DURATION_MS, vqv_score est remplacé par 0 dans la somme pondérée (pas de soft penalty) | AJOUT |
| vqv (video quality view) | CONCEPT | définition | Visionnage vidéo qui clear le seuil de durée minimal — signal positif first-class introduit en 2026, n'existait pas en 2023 | AJOUT |
| dwell_time continuous | CONCEPT | définition | Signal dwell mesuré en durée continue (index 18) en 2026, vs binaire dwelled/not-dwelled en 2023 — récompense les threads et long-form | AJOUT |
| follow_author_score | CONCEPT | définition | Prédiction Phoenix (index 13) "ce post fera-t-il gagner un follower à son auteur" — nouveau signal first-class 2026 | AJOUT |
| share_via_dm + share_via_copy_link | CONCEPT | définition | Variantes share distinctes (indices 8, 9) qui mesurent le forward privé vs public, signaux haute valeur pour pricing teardowns / product comparisons / controversy forwarded privately | AJOUT |
| NEGATIVE_FEEDBACK_INDICES | CONCEPT | définition | Liste [14, 15, 16, 17] dans phoenix/runners.py = not_interested, block_author, mute_author, report — soustractions directes au score, **cumulatives** sur tous les posts futurs vers l'utilisateur concerné | AJOUT |
| AuthorSocialgraphFilter | TECHNOLOGIE | rôle | Filtre pre-scoring qui exclut posts d'auteurs bloqués/muted par viewer **ET** posts où l'auteur bloque le viewer (bidirectionnel, incluant auteur cité du quote tweet) | AJOUT |
| MutedKeywordFilter | TECHNOLOGIE | rôle | Filtre pre-scoring qui exclut posts matchant les muted keywords du viewer | AJOUT |
| VFFilter | TECHNOLOGIE | rôle | Filtre post-selection visibility — supprime deleted, spam, violence, gore avant servir | AJOUT |
| task_spam_detection.py | TECHNOLOGIE | rôle | Classifier Grok-based offline keye sur low-follower / low-quality reply patterns — risque d'exclusion silencieuse pour brand accounts qui répliquent lourdement sur big posts | AJOUT |
| task_post_safety_screen_deluxe.py | TECHNOLOGIE | rôle | Classifier Grox offline pour violence, NSFW, misinformation — exclusion eligibility-time, pas démotion | AJOUT |
| task_banger_screen.py | TECHNOLOGIE | rôle | Classifier Grox offline positif (early high-quality / viral screen) — détection upstream de posts à fort potentiel | AJOUT |
| multimodal_post_embedder_v5 | TECHNOLOGIE | définition | Embedder Grox qui encode text + images + (optional) ASR transcript du video en vecteur 1024-dim normalisé — utilisé pour two-tower retrieval | AJOUT |
| two-tower retrieval | METHODOLOGIE | définition | Pattern ML où users et items sont encodés par towers séparés dans un même espace d'embedding, matching par nearest-neighbor ANN — utilisé pour candidats OON Phoenix | AJOUT |
| candidate-isolation attention | METHODOLOGIE | définition | Masking pattern dans Phoenix ranking où candidats peuvent attendre le contexte user mais pas entre eux → scores batch-independent et cacheables | AJOUT |
| params.rs (absent) | CONCEPT | définition | Module Rust attendu contenant les valeurs de FAVORITE_WEIGHT, OON_WEIGHT_FACTOR etc. — **n'existe pas** dans le release public (vérifié par grep -rn exhaustif) | AJOUT |
| feature-switch parameter service | CONCEPT | définition | Service interne X (non publié) qui gère les valeurs numériques des paramètres, permet A/B testing et tuning sans code change — explique l'absence de params.rs | AJOUT |
| Phoenix checkpoint released | TECHNOLOGIE | définition | Mini-model open-source : 2 layers, 4 attention heads, 256-dim, entraîné sur corpus 537K posts sports — démonstrateur architectural, **pas** le modèle production | AJOUT |
| `panic!("Not implemented: to_thrift for ...")` stubs | CONCEPT | définition | Marqueurs présents dans candidate_features.rs et user_features.rs — confirment que le release public ne tourne pas end-to-end contre les services internes X | AJOUT |
| Three layers of reach | METHODOLOGIE | définition | Cadre généralisé du rapport : Eligibility (binary, Grox + filtres) → Retrieval (probabilistic, two-tower) → Ranking (continuous, weighted sum + multipliers) | AJOUT |
| Two laws of mechanical growth | METHODOLOGIE | définition | Law 1 : In-network is multiplicative, OON is additive. Law 2 : The model's job is to predict you, not reward you | AJOUT |
| Eligibility-time silent exclusion | CONCEPT | définition | Mode opératoire 2026 (vs démotion 2023) : borderline content disparaît du candidate pool sans signal au créateur — *"the silent killer"* | AJOUT |
| Action-targeted content design | METHODOLOGIE | définition | Recommandation : chaque post nomme l'action cible parmi les 19 (target_action: click / vqv / dm_share / follow / reply...), mesurer success par action distribution per post, pas impressions totales | AJOUT |
| Author distribution playbook | METHODOLOGIE | définition | Recommandation : audit cadence vs author-diversity decay, remplacer stacked single-account drumbeats par multi-account amplification (brand + employés) — chaque post entre au position=0 pour son auteur | AJOUT |
| 70/30 topical core / exploratory split | METHODOLOGIE | définition | Recommandation : 70% du contenu sur un core topical cohérent (densité d'embedding-neighborhood avec audience cible), 30% exploratoire pour découvrir nouvelles audiences sans diluer l'embedding | AJOUT |
| OON-to-Thunder conversion | CONCEPT | définition | Reframing : acquérir un follower convertit le posting de probabilistic OON retrieval en deterministic Thunder lookup pour cet utilisateur — multiplicative future reach sur tous les posts futurs | AJOUT |
| rapport interne x-algorithm growth | DOCUMENT | rôle | Teardown analytique du release `xai-org/x-algorithm` 15 mai 2026, 4 audiences (personal/brand/framework/consulting), discipline d'honnêteté épistémique (refus de fabriquer des magnitudes), citations file:line systématiques | AJOUT |
