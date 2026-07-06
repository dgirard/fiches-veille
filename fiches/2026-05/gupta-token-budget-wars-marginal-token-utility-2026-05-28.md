---
cabinet_promotion_candidate: true
proposed_class: Concept
proposed_capability: capability/software-factory
notes: "Cadre économique directement mobilisable pour le positionnement Optimisation des coûts / FinOps agentique du cabinet : 'marginal token utility' + 'token-to-outcome attribution' + 'cost per completed outcome vs BPO'. Aligne avec ce qu'on observe sur le pilotage de la facture d'inférence en mission."
themes: [economie-marche]
source: "X (Jaya Gupta @JayaGup10)"
---
# gupta-token-budget-wars-marginal-token-utility-2026-05-28

## Veille
Thread X viral (**230,5K vues**, 28 mai 2026, 1h51) de **Jaya Gupta** (@JayaGup10, investisseuse — vraisemblablement Foundation Capital, auteure du cadre *Context Graphs*) intitulé ***« Token Budget Wars »***. **Thèse-pivot** : ***« Enterprise AI has moved from adoption to allocation »*** — la phase 1 de l'IA d'entreprise a prouvé que les modèles savent travailler ; la phase 2 décidera **combien de ce travail vaut la peine**. La nouvelle monnaie au sommet de l'entreprise est la **capacité à quantifier le ROI de l'IA** : *« show me the value »*. Concept canonique : ***marginal token utility*** = *« the business value created by each additional dollar of inference »* — le nombre qui compte à l'échelle, et que **la plupart des entreprises ne peuvent pas voir**. Chronologie : **Claude shippé novembre 2025**, après le lock des budgets annuels 2026 → dès le **Q1**, entreprises *« running multiples ahead of plan »* → l'inférence cesse d'être une ligne d'expérimentation pour devenir un **coût opérationnel récurrent**. Bascule **expérimentation (quelques 100K$) → infrastructure (7 chiffres, 1M$+)** : à l'échelle infra, **la variance technique produit des swings de P&L matériels — deux exécutions du même workflow sur le même input peuvent différer de 5-10× en coût de tokens** sans rien de visiblement cassé, *« a number the CFO has to explain to the CEO »*. **L'IA concurrence le travail** : 3 types de demandes budgétaires (remplacer du travail externalisé / interne / générer du revenu) → glissement vers le ***cost of a completed outcome*** (cost per resolved ticket, processed claim, reviewed contract, completed invoice, avoided hire, retained customer, dollar of revenue moved). **BPO = baseline le plus facile à benchmarker** (déjà tarifé en unités complétées) ; travail interne bien plus dur (employés polyvalents, gains diffus, résistance RH à réduire les effectifs). **Pourquoi c'est différent du SaaS** : le SaaS a appris à traiter l'usage comme proxy de valeur ; l'IA casse ce proxy — *« the signal and the noise share the same unit »* (le token), *« SaaS usage told you the software had been adopted. AI usage tells you the meter is running. It doesn't tell you whether your company is cooking »*. **Trois causes de l'invisibilité de la marginal token utility** : (1) ***retry tails*** — tokens par workflow résolu ≈ **T/p** ; passer de 90% à 70% de complétion augmente le coût effectif de ~**28%**, pas 20%, car les échecs composent ; (2) ***context inflation*** — coût d'inférence ≈ **O(n²)** en longueur de contexte (attention), doubler le contexte **quadruple** le coût de raisonnement (sur-récupération : 50 docs quand 5 suffisent) ; (3) ***routing*** — par défaut on prend le modèle le plus puissant (classification basique sur modèle de raisonnement complexe) ; sur des millions d'appels, la différence entre router les tâches faciles vers un petit modèle et tout envoyer au frontier = *« the difference between a manageable bill and a board-level problem »*. **Bifurcation sectorielle** : entreprises **software** = problème de **mesure de productivité** (déjà instrumenté : PRs, commits, deploys, incidents, cycle time, MTTR — tracke les *« AI layoffs »*) ; entreprises **non-software** = problème de **transformation** (travail opérationnel : claims, underwriting, support, compliance reviews, supply chain exceptions, payment disputes — *right under audit, not just right on average*). **La couche manquante = token-to-outcome attribution** : une couche de conversion reliant dépense d'inférence → travail effectué → outcome business, qui répond à 3 questions (coût réel incluant retries/corrections ; quelles parties du trace ont compté vs thrashing ; le travail a-t-il changé l'operating model). ***Measurement becomes memory*** : pour relier un token à un outcome il faut capturer les **decision traces** (ce que l'agent a vu, récupéré, appelé, ignoré, où il a retried, quand un humain a overridé) — *« decision rationale is one of the most perishable assets in a company »* (vit dans Slack, emails, escalation calls, têtes des gens). Les agents **créent** ces traces ; capturées d'abord pour justifier la dépense, elles deviennent *« more valuable than the cost report »* → un **context graph** (*« although I am so tired of that word these days »*). **The allocation layer is the prize** : qui possède le token-to-outcome attribution fait les **allocation calls** (quels workflows méritent plus de compute, lesquels cappés, lesquels en modèles cheaper, lesquels restent humains, lesquels remplacent le BPO). Les entreprises ne le feront pas seules — elles l'**achèteront comme une transformation** (playbook Fortune 500 : McKinsey + alumni Palantir + top-down CEO, à la manière ERP/BI/digital transformation, un *« program »* avec sponsor exécutif et une infra qui devient la **nouvelle source de vérité**). Cadre par **Charlie Munger** : *« show me the incentive and I will show you the outcome »*. Sous-thèse organisationnelle : instinct exécutif trentenaire *big teams = big jobs/scope/power* → quand l'intelligence devient la **ressource rare**, le nouveau marqueur est *« how much of it you're orchestrating »*. Pertinence directe pour le **positionnement Optimisation des coûts / FinOps agentique** : confirme empiriquement les leviers (routage modèles, prompt caching, hygiène contexte, sub-agents) et déplace le KPI vers le **coût par outcome complété**. Convergence forte avec Bain *cross-system labor* (execution data moat, Cursor), Ng *No AI jobpocalypse* (pricing ancré sur le salaire de l'employé remplacé), DORA ROI (coût par feature), Mensch/Mistral (electron→token), Ensarguet (économie de la computation), Foundation Capital *Context Graphs* (decision traces, même autrice), Wescale *Token Burning*, BFM/Girard (token = fuel de valeur).

## Titre Article
Token Budget Wars

## Date
2026-05-28

## URL
https://x.com/JayaGup10/status/2059784669382791653

## Keywords
Token Budget Wars, marginal token utility, token-to-outcome attribution, adoption to allocation, allocation layer, cost per completed outcome, cost of a completed outcome, retry tails, context inflation, model routing, Haiku Sonnet Opus routing, prompt caching, hygiène du contexte, AI ROI quantification, show me the value, inference recurring operating cost, experimentation to infrastructure, seven figures, technical variance 5-10x token cost, AI spend competes with labor, BPO benchmark, business process outsourcing, cost per resolved ticket processed claim reviewed contract, avoided hire retained customer, SaaS usage proxy value, signal and noise share the same unit, is your company cooking, T over p retry economics, completion rate 90 to 70 percent 28 percent, O(n²) attention context length, over-supplied retrieval, frontier model overpowered, software productivity measurement problem, non-software transformation problem, AI layoffs, PRs commits deploys incidents cycle time MTTR, claims underwriting compliance reviews supply chain exceptions payment disputes, right under audit, decision traces, measurement becomes memory, decision rationale perishable asset, systems of record what not why, context graph, allocation calls, capped compute, transformation program, Fortune 500 playbook, McKinsey Palantir top-down CEO, ERP BI digital transformation, new source of truth, intelligence scarce resource, orchestrating intelligence, big teams big jobs, Charlie Munger show me the incentive, Jaya Gupta, Foundation Capital, tokenmaxxing, metamates, CFO CEO board-level problem, FinOps agentique, TCO coût par feature

## Authors
**Jaya Gupta** (@JayaGup10) — investisseuse / VC. Très probablement **Foundation Capital** (le thread s'auto-réfère au cadre ***Context Graphs*** — *« ahem, context graph, although I am so tired of that word these days »* — concept porté par Foundation Capital, cf. fiche `bain-100b-saas-opportunity` qui cite *Foundation Capital — Context Graphs trillion-dollar opportunity, 2025-12-22*). Thread publié sur X le **28 mai 2026 à 1h51**, **230,5K vues**, format essai long en un seul post. Une réponse notable de **@tuning_engines** (*« DevSecFinOps for the Agentic Era »*) : *« Tokens will basically have to be managed like headcount […] model hierarchies too »*.

## Ton
**Profil** : Essai-thèse d'investisseuse à destination de fondateurs, CFO/CEO, DSI et opérateurs d'IA d'entreprise. Perspective narrative à la première personne discrète, registre **analyste-VC**, niveau technique **moyen-élevé** (assume *O(n²)*, retry tails, two-tower, mais reste lisible par un décideur). Format thread X long (un seul post dense, ~1 200 mots), structuré par sous-titres internes (*Why this is different from SaaS*, *Why marginal token utility is hard to see*, *Measurement becomes memory*, *The allocation layer is the prize*).

**Style** : Prose VC affûtée façon memo d'investissement — affirmations-pivots posées en une phrase puis déroulées, mélange de **rigueur économique** (formules *T/p*, *O(n²)*, fourchettes chiffrées 5-10×, 28%) et de **registre culturel Silicon Valley / Meta** (*tokenmaxxing*, *#metamates*, *#bearish* Jim Cramer/CNBC, *TikTok breaks at lunch*, *is your company cooking*). Autodérision sur le jargon (*« context graph, although I am so tired of that word these days »*). Clôture sur une citation-totem (Munger) — signature memo VC. Ton **prescriptif sans être militant** : pas de produit vendu frontalement, mais une thèse de marché (« the allocation layer is the prize ») qui dessine en creux une catégorie de startups à financer.

**Aphorismes-clés** :
- ***« Enterprise AI has moved from adoption to allocation. »*** (thèse-pivot).
- ***« Marginal token utility: the business value created by each additional dollar of inference. »*** (concept canonique).
- ***« The signal and the noise share the same unit. »*** (pourquoi le SaaS ne s'applique plus).
- ***« SaaS usage told you the software had been adopted. AI usage tells you the meter is running. It doesn't tell you whether your company is cooking. »***
- ***« Measurement becomes memory. »*** (decision traces → context graph).
- ***« The allocation layer is the prize. »*** (la couche qui fait les allocation calls).
- ***« Show me the incentive and I will show you the outcome. »*** (Charlie Munger, clôture).

**Métaphores travaillées** :
- ***The meter is running*** — l'inférence comme compteur de taxi qui tourne : l'usage ne prouve plus la valeur, il prouve que la dépense court. (Écho direct à la métaphore *taxi sans essence* de Girard/BFM.)
- ***Is your company cooking*** — argot pour « est-ce que ça produit vraiment » : deux factures de tokens identiques peuvent recouvrir deux opérations radicalement différentes (l'une convertit, l'autre paie du *thrash*).
- ***Token budget wars*** comme **guerre d'allocation interne** — la bataille pour la propriété des tokens heurte l'instinct exécutif trentenaire (taille d'équipe = pouvoir) ; nouveau marqueur = *« how much intelligence you're orchestrating »*.
- ***Tokens managed like headcount*** (repris en réponse) — les tokens deviennent une ressource à gérer comme des FTE, avec hiérarchies de modèles.

**Position épistémique** : analyse de **marché + cadre économique** posant une catégorie produit naissante (*token-to-outcome attribution* / *allocation layer*) ; mélange de modèles formels (retry economics, attention scaling) et d'observation terrain (Q1 2026 multiples ahead of plan). Honnêteté sur le jargon qu'elle a contribué à populariser (context graph).

**Autorité** : construite par (a) la **position d'investisseuse** qui voit plusieurs entreprises à l'échelle, (b) la **paternité du cadre Context Graphs** (auto-référence), (c) la **précision des modèles** (T/p, O(n²)), (d) le **timing** (28 mai 2026, post-bascule budgétaire Q1), (e) la **viralité** (230,5K vues) qui valide la résonance du sujet auprès des opérateurs.

## Pense-betes

- **Date / source** : **28 mai 2026** (1h51), thread X @JayaGup10, **230,5K vues**. Format essai long en un post.
- **Autrice** : **Jaya Gupta**, investisseuse (probablement **Foundation Capital** — auteure du cadre *Context Graphs*, auto-cité).
- **Thèse-pivot** : ***« Enterprise AI has moved from adoption to allocation »*** — phase 1 : les modèles savent travailler ; phase 2 : **combien de ce travail vaut la peine**.

### Le concept central — marginal token utility

> ***« the business value created by each additional dollar of inference. It's the number that matters at scale, and the number most companies cannot see. »***

- C'est le **dérivé** du ROI : pas le coût total, mais la **valeur du dollar marginal d'inférence**.
- Invisible parce que **token utility n'est pas quantifiée** : la facture ne dit pas si la dépense a remplacé du travail, généré du revenu, réduit du risque, accéléré un workflow… ou juste financé des ingénieurs en *tokenmaxxing* sur le leaderboard.

### Chronologie de la bascule

| Moment | Fait |
|--------|------|
| **Nov. 2025** | Claude shippé **après** le lock des budgets annuels 2026 |
| **Q1 2026** | Entreprises *« running multiples ahead of plan »* |
| Seuil **~quelques 100K$** | Encore de l'expérimentation |
| Seuil **7 chiffres (1M$+)** | Devient de l'**infrastructure** → swings de P&L matériels |

- **Variance technique canonique** : *« two runs of the same workflow on the same input can differ in token cost by 5-10x without anything visibly going wrong »* → à l'échelle infra, *« a number the CFO has to explain to the CEO »*.

### L'IA concurrence le travail (pas le SaaS)

- **3 types de demandes budgétaires** : remplacer travail **externalisé** / remplacer travail **interne** / générer du **revenu**.
- Glissement de l'unité : du token vers le ***cost of a completed outcome*** → cost per **resolved ticket, processed claim, reviewed contract, completed invoice, avoided hire, retained customer, dollar of revenue moved**.
- **BPO = baseline le plus facile** (déjà tarifé en unités complétées : prix par ticket/claim/invoice/review). Travail **interne = bien plus dur** (employés polyvalents, gains diffus = avoided hiring/capacité, résistance RH).
- ⚠️ Piège : *« a claim that requires three retries, human correction, and a frontier model may be more expensive than the outsourced labor it was supposed to replace »*.

### Pourquoi le SaaS ne s'applique plus

> ***« The signal and the noise share the same unit. »*** Le token (unité de facture) est **stable**, mais le travail qu'il représente **ne l'est pas**.

> ***« SaaS usage told you the software had been adopted. AI usage tells you the meter is running. It doesn't tell you whether your company is cooking. »***

### Les 3 causes de l'invisibilité — directement actionnables (FinOps)

| # | Cause | Mécanique | Levier |
|---|-------|-----------|--------|
| 1 | **Retry tails** | tokens/workflow résolu ≈ **T/p** ; 90%→70% complétion = **+~28%** coût (pas 20%, les échecs composent) | fiabiliser la complétion 1er passage |
| 2 | **Context inflation** | coût ≈ **O(n²)** en longueur contexte ; doubler le contexte **×4** le raisonnement ; sur-récupération (50 docs au lieu de 5, threads email entiers, historique périmé) | **hygiène du contexte**, retrieval ciblé |
| 3 | **Routing** | par défaut = modèle le plus fort ; classification basique sur modèle de raisonnement complexe | **routage modèles** (petit modèle pour tâches faciles) = *« manageable bill vs board-level problem »* |

→ **Recoupe exactement** les leviers du slot « Optimisation des coûts » de la matinée Claude Code (routage Haiku/Sonnet/Opus, prompt caching, hygiène contexte, sub-agents).

### Bifurcation sectorielle

| | **Software** | **Non-software** |
|--|-------------|------------------|
| Nature du problème | **Mesure de productivité** | **Transformation** |
| Pourquoi | Travail déjà instrumenté (PRs, commits, deploys, incidents, cycle time, MTTR) | Travail opérationnel (claims, underwriting, support, compliance, supply chain, payment disputes) |
| Exigence | *right on average* | ***right under audit*** |
| Symptôme | tracke les *« AI layoffs »* | unité de travail ≠ unité de coût ≠ même organisation |

### La couche manquante — token-to-outcome attribution

- **Couche de conversion** reliant : dépense d'inférence → travail effectué → outcome business.
- **3 questions** : (1) coût réel **incluant retries/corrections** ? (2) quelles parties du trace ont **compté** vs **thrashing** ? (3) le travail a-t-il **changé l'operating model** (moins de tickets/agent, cycles claims plus courts, ligne BPO réduite, embauches différées) ?
- Attribution **dans le langage du business** : pas *« this workflow cost $2.13 »* mais *« this class of claims is cheaper with agents than BPO, except when the policy requires exception documents, in which case the retry tail destroys the economics »*.

### Measurement becomes memory

> ***« Decision rationale is one of the most perishable assets in a company »*** — vit dans Slack threads, email chains, escalation calls, et la tête des gens (qui partent).

- Systems of record capturent **ce qui** s'est passé, rarement **pourquoi** (un CRM dit qu'un deal a glissé, pas le jugement non-écrit derrière le forecast).
- **Les agents créent des traces** (retrieval, tool call, retry, escalation, correction humaine, décision finale).
- Capturées d'abord pour **justifier la dépense**, elles deviennent *« more valuable than the cost report »* → un **context graph** (jargon dont l'autrice dit être *« so tired »*).

### The allocation layer is the prize

- Qui possède le token-to-outcome attribution fait les **allocation calls** : quels workflows → plus de compute / cappés / modèles cheaper / restent humains / remplacent le BPO.
- *« And once you make those calls, you control where AI spend goes inside the enterprise and get to have the trust to allocate. »*
- **Achat comme transformation** (playbook Fortune 500) : McKinsey + alumni Palantir + top-down CEO ; arrive comme ERP/BI/digital transformation, un *« program »* avec sponsor exécutif + infra = **nouvelle source de vérité**.
- Les fondateurs capables de le faire seront *« different people than the classic archetype »*.

### À mobiliser pour

- **Slot « Optimisation des coûts » (matinée Claude Code)** : citation canonique pour le passage *coût des tokens → coût par outcome complété* ; les 3 causes (retry/context/routing) structurent la partie leviers ; *« the meter is running »* et *« is your company cooking »* = punchlines pour décideurs.
- **Offre FinOps agentique cabinet** : la couche *token-to-outcome attribution* est une **catégorie produit/conseil naissante** — positionnement possible pour SFEIR (instrumenter le trace, relier au P&L).
- **Discours CFO/CEO** : *« a number the CFO has to explain to the CEO »* — cadre exactement la conversation budget IA 2026.
- **Argument decision traces / context graph** : convergence avec Foundation Capital (même autrice), Bain (execution data moat), Talisman (ontologie/governance) — *measurement becomes memory* = thèse du moat data 2026.

### Articulation dossier veille

- **Bain — cross-system labor** (2026-05) : même couple **execution data = moat** + **cost of completed outcome** ; Bain dimensionne le marché, Gupta dimensionne le **problème de mesure** qui le débloque. Tous deux citent l'IA comme **substitution de coût du travail**.
- **Ng — No AI jobpocalypse** (2026-05-08) : Ng décrit le **pricing power** (éditeurs ancrent le tarif sur le **salaire de l'employé remplacé**) ; Gupta décrit la **contrepartie acheteur** (l'IA est benchmarkée contre le BPO/le salaire). Deux faces de la même mécanique *AI spend competes with labor*.
- **DORA ROI** (2026-04-21) : *« we don't measure AI by code it writes but by bottlenecks it clears »* + *« code is a liability »* → Gupta = version **token-level** du même refus du proxy d'activité.
- **Mensch / Mistral** (2026-05-13) : *« on transforme de l'électricité en intelligence, en génération de tokens »* — économie electron→token côté offre ; Gupta = économie token→outcome côté demande.
- **Ensarguet — Economics of Computation** (2026-03-11) : *moment kilowatt-heure*, fin de l'heure-cerveau ; Gupta prolonge côté **unité de valeur du compute**.
- **Foundation Capital — Context Graphs** (2025-12-22, **même autrice**) : *measurement becomes memory* = pont explicite vers le cadre Context Graphs ; decision traces = nouveau system of record.
- **Wescale — Usine Logicielle Augmentée** (2026-05-03) : concept *Token Burning* + Manager d'Agents = pendant opérationnel FR du *thrash* de Gupta.
- **BFM / Girard** (2026-05-05) : *« token = fuel de valeur »*, primes NVIDIA en tokens, métaphore taxi — convergence directe avec *the meter is running*.
- **@tuning_engines** (réponse — *« DevSecFinOps for the Agentic Era »*) : prolongement **gouvernance/organisationnel** de la thèse. Trois idées : (1) ***« Tokens will basically have to be managed like headcount »*** — le token devient une ressource gérée comme un effectif (budget, allocation, justification) ; (2) ***model hierarchies*** — *« which model reports to which user (meaning which user can use which model in essence!) »* = un **contrôle d'accès par rôle (RBAC) sur les modèles** : qui a le droit d'utiliser Opus vs Sonnet vs Haiku ; (3) *« many organizational FTE management techniques will need application to the tokens as well »* — importer les techniques RH de **gestion des effectifs** (planification de capacité, allocation, revue) vers la gestion des tokens. → Pont direct vers le slot **Gouvernance** de la matinée (quotas/permissions par utilisateur et par modèle) et convergence avec **Uber Engineering** (identité agent, *which agent can do what*).

## RésuméDe400mots

Le 28 mai 2026, **Jaya Gupta** (investisseuse, probablement Foundation Capital) publie sur X un essai-thread viral (230,5K vues) : ***« Token Budget Wars »***. **Thèse-pivot** : *« Enterprise AI has moved from adoption to allocation »*. La phase 1 a prouvé que les modèles savent travailler ; la phase 2 décidera **combien de ce travail vaut la peine**. La nouvelle monnaie au sommet des entreprises est la **quantification du ROI de l'IA** — *« show me the value »*.

Concept canonique : ***marginal token utility*** = *« the business value created by each additional dollar of inference »* — le nombre qui compte à l'échelle, **invisible** pour la plupart des entreprises car la facture ne dit pas si la dépense a remplacé du travail, généré du revenu ou financé du *tokenmaxxing*. Chronologie : **Claude shippé novembre 2025**, après le lock des budgets 2026 ; dès le **Q1**, entreprises *« multiples ahead of plan »*. Bascule **expérimentation (100K$) → infrastructure (1M$+)** : *« two runs of the same workflow on the same input can differ in token cost by 5-10x »* — *« a number the CFO has to explain to the CEO »*.

**L'IA concurrence le travail** : on glisse du token vers le ***cost of a completed outcome*** (par ticket résolu, claim traité, contrat revu, embauche évitée…). Le **BPO** est le baseline le plus facile (déjà tarifé en unités complétées). **Pourquoi le SaaS ne s'applique plus** : *« the signal and the noise share the same unit »* ; *« SaaS usage told you the software had been adopted. AI usage tells you the meter is running. It doesn't tell you whether your company is cooking »*.

**Trois causes d'invisibilité** : (1) **retry tails** — tokens/résolution ≈ T/p, 90%→70% = +~28% ; (2) **context inflation** — coût ≈ O(n²), doubler le contexte ×4 le raisonnement ; (3) **routing** — tout envoyer au frontier model = *« board-level problem »*. **Bifurcation** : software = problème de **mesure de productivité** ; non-software = problème de **transformation** (*right under audit*).

**Couche manquante** : ***token-to-outcome attribution*** reliant inférence → travail → outcome. ***Measurement becomes memory*** : les agents créent des **decision traces** (*« decision rationale is one of the most perishable assets »*) qui deviennent *« more valuable than the cost report »* → un **context graph**. **The allocation layer is the prize** : qui le possède fait les *allocation calls* et contrôle où va la dépense IA — acheté comme une **transformation** (McKinsey + Palantir + top-down CEO, à la manière ERP/BI). Clôture Munger : *« show me the incentive and I will show you the outcome »*.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Jaya Gupta | PERSONNE | publie | Token Budget Wars | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Jaya Gupta | PERSONNE | travaille_chez | Foundation Capital | ORGANISATION | 0.75 | DYNAMIQUE | inféré |
| Jaya Gupta | PERSONNE | affirme_que | « Enterprise AI has moved from adoption to allocation » | CITATION | 0.96 | DYNAMIQUE | déclaré_article |
| Marginal token utility | CONCEPT | est_instance_de | valeur business créée par dollar marginal d'inférence | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Jaya Gupta | PERSONNE | affirme_que | Claude a été shippé en novembre 2025, après le lock des budgets annuels 2026 | AFFIRMATION | 0.93 | STATIQUE | déclaré_article |
| Inférence | CONCEPT | est_instance_de | coût opérationnel récurrent | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Jaya Gupta | PERSONNE | mesure | variance de 5-10× en coût de tokens entre deux exécutions du même workflow sur le même input | MESURE | 0.94 | ATEMPOREL | déclaré_article |
| AI spend | CONCEPT | concurrence | le travail (labor) | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Cost of completed outcome | CONCEPT | remplace | coût du token comme unité pertinente | CONCEPT | 0.94 | DYNAMIQUE | déclaré_article |
| BPO | CONCEPT | est_instance_de | baseline benchmarkable (unités complétées) | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Jaya Gupta | PERSONNE | affirme_que | « the signal and the noise share the same unit » | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Jaya Gupta | PERSONNE | mesure | retry tails : coût par résolution ≈ T/p ; 90%→70% de complétion = +~28% de coût | MESURE | 0.92 | ATEMPOREL | déclaré_article |
| Context inflation | CONCEPT | est_basé_sur | scaling O(n²) de l'attention en longueur de contexte | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Model routing | METHODOLOGIE | permet | facture gérable (vs board-level problem) | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Problème de mesure de productivité | CONCEPT | s_applique_à | entreprises software | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| Problème de transformation | CONCEPT | s_applique_à | entreprises non-software | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| Token-to-outcome attribution | CONCEPT | est_instance_de | la couche manquante | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Agents | TECHNOLOGIE | permet | decision traces | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Jaya Gupta | PERSONNE | affirme_que | les decision traces deviennent un context graph plus précieux que le cost report | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Jaya Gupta | PERSONNE | affirme_que | « the allocation layer is the prize » | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| Jaya Gupta | PERSONNE | prédit | le token-to-outcome attribution sera acheté comme une transformation (McKinsey + Palantir + top-down CEO) | AFFIRMATION | 0.91 | DYNAMIQUE | déclaré_article |
| Charlie Munger | PERSONNE | affirme_que | « show me the incentive and I will show you the outcome » | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| @tuning_engines | PERSONNE | affirme_que | « tokens will basically have to be managed like headcount » | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Model hierarchies | CONCEPT | permet | contrôle d'accès par rôle sur les modèles (quel utilisateur peut utiliser quel modèle) | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Techniques de gestion FTE | METHODOLOGIE | s_applique_à | la gestion des tokens | CONCEPT | 0.91 | DYNAMIQUE | déclaré_article |
| Token Budget Wars | DOCUMENT | converge_avec | Bain cross-system labor, Ng pricing power, DORA ROI, Foundation Capital Context Graphs | DOCUMENT | 0.90 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Jaya Gupta | PERSONNE | rôle | Investisseuse / VC (probablement Foundation Capital), autrice du thread Token Budget Wars et du cadre Context Graphs | AJOUT |
| Token Budget Wars | DOCUMENT | description | Essai-thread X 28 mai 2026 (230,5K vues) : l'IA d'entreprise passe de l'adoption à l'allocation ; phase 2 = combien de travail vaut la peine | AJOUT |
| Marginal token utility | CONCEPT | définition | Valeur business créée par chaque dollar marginal d'inférence — le nombre qui compte à l'échelle, invisible pour la plupart des entreprises | AJOUT |
| Token-to-outcome attribution | CONCEPT | définition | Couche de conversion reliant dépense d'inférence → travail effectué → outcome business ; répond au coût réel (retries inclus), au signal vs thrashing, et au changement d'operating model | AJOUT |
| Cost of completed outcome | CONCEPT | définition | Unité de coût pertinente à l'ère agentique : coût par ticket résolu / claim traité / contrat revu / facture complétée / embauche évitée / client retenu / dollar de revenu déplacé | AJOUT |
| Retry tails | CONCEPT | définition | Coût par workflow résolu ≈ T/p ; passer de 90% à 70% de complétion augmente le coût effectif de ~28% car les échecs composent | AJOUT |
| Context inflation | CONCEPT | définition | Coût d'inférence ≈ O(n²) en longueur de contexte (attention) ; doubler le contexte quadruple le coût de raisonnement ; aggravé par la sur-récupération | AJOUT |
| Model routing | METHODOLOGIE | définition | Diriger chaque tâche vers le modèle juste-suffisant ; tout envoyer au frontier model = différence entre facture gérable et problème de board | AJOUT |
| Measurement becomes memory | CONCEPT | définition | En capturant les decision traces pour justifier la dépense, l'entreprise crée un enregistrement durable de comment elle décide — un context graph plus précieux que le cost report | AJOUT |
| Allocation layer | CONCEPT | définition | Couche qui fait les allocation calls (quels workflows ont plus de compute, lesquels cappés, modèles cheaper, restent humains, remplacent le BPO) — contrôle où va la dépense IA | AJOUT |
| Decision rationale | CONCEPT | attribut | Un des actifs les plus périssables de l'entreprise : vit dans Slack, emails, escalation calls et la tête des gens qui partent | AJOUT |
| Charlie Munger | PERSONNE | citation | « Show me the incentive and I will show you the outcome » (clôture du thread) | AJOUT |
| Foundation Capital | ORGANISATION | rôle | Société d'investissement, autrice du cadre Context Graphs (auto-référencé par Gupta) ; lien probable avec l'autrice | AJOUT |
| @tuning_engines | PERSONNE | rôle | Compte X (« DevSecFinOps for the Agentic Era ») répondant au thread ; propose de gérer les tokens comme des effectifs (headcount), des model hierarchies (RBAC sur modèles) et l'application des techniques de gestion FTE aux tokens | AJOUT |
| Model hierarchies (gouvernance tokens) | CONCEPT | définition | Contrôle d'accès par rôle appliqué aux modèles : quel utilisateur a le droit d'utiliser quel modèle (Opus/Sonnet/Haiku) — pendant gouvernance du routage. Pont vers Uber agent identity et le slot Gouvernance | AJOUT |
