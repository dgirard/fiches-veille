# ng-the-batch-350-coding-agents-software-work-acceleration-2026-04-24

## Veille
Édito d'Andrew Ng dans The Batch n°350 qui pose une **hiérarchie d'accélération par les coding agents** selon le type de travail logiciel : **Frontend (max) > Backend (modéré) > Infrastructure (faible) > Recherche (minimal)**. Justification par la *verifiability* implicite (TypeScript/JavaScript fluents + boucle agent–navigateur autonome côté frontend) et par les zones d'ombre des LLMs (corner cases / sécurité / migrations DB pour le backend, tradeoffs réseau opaques pour l'infra, formation d'hypothèses irréductible pour la recherche). Numéro complété par 4 actualités structurantes : **GLM-5.1 (Z.ai)** modèle 754B/40B-actifs MIT capable de tâches autonomes de 8h (leader SWE-Bench Pro 58,4%) ; **Digit (Agility Robotics) chez Schaeffler** premier déploiement industriel d'humanoïdes (5'9"/143lb, 10–25$/h vs 20$/h humain) ; **révolte anti-data-centers** (~64Md$ bloqués mai-2024 / mars-2025, moratoire Maine 20MW+, cocktail molotov chez Sam Altman) ; et **"assistant axis"** (Christina Lu, MATS / Oxford / Anthropic) qui réduit la dérive de persona et les jailbreaks (Qwen3 32B : 83%→41% ; Llama 3.3 70B : 65%→33%) sans dégrader IFEval/GSM8k/MMLU-Pro/EQ-Bench.

## Titre Article
The Batch n°350 — How Coding Agents Accelerate Different Types of Software Work (Andrew Ng) + GLM-5.1, Digit chez Schaeffler, anti-data-center revolt, assistant axis

## Date
2026-04-24

## URL
https://www.deeplearning.ai/the-batch/issue-350/

## Keywords
Andrew Ng, The Batch, DeepLearning.AI, coding agents, accélération différentielle, frontend development, backend development, infrastructure, recherche, TypeScript, JavaScript, navigateur autonome, corner cases, sécurité, migrations DB, hypothèses formation, GLM-5.1, Z.ai, 754B paramètres, 40B actifs, MoE, SWE-Bench Pro, Arena Code, CyberGym, GPQA Diamond, MIT license, HuggingFace, prompt caching, Agility Robotics, Digit, Schaeffler, robot humanoïde, manufacturing, Caroline du Sud, RGB depth cameras, LiDAR, IMU, McKinsey 5 millions humanoïdes 2040, anti-data-center, moratoire Maine, Port Washington Wisconsin, Festus Missouri, Ohio amendement constitutionnel, cocktail molotov Altman, Indianapolis tirs, closed-loop cooling, off-grid generation, Christina Lu, MATS, Oxford, Anthropic, assistant axis, activation capping, persona drift, jailbreak resistance, Qwen3 32B, Llama 3.3 70B, Gemma 2 27B, IFEval, GSM8k, MMLU-Pro, EQ-Bench, hiérarchie d'accélération, verifiability, jagged frontier

## Authors
Andrew Ng (édito principal — fondateur DeepLearning.AI, Stanford, ex-Google Brain, ex-Baidu) ; rédaction The Batch (DeepLearning.AI) pour les sections actualités

## Ton
**Profil** : Newsletter hebdomadaire IA, format digest 5 sections (1 édito + 4 actualités), perspective troisième personne journalistique pour les news + première personne réflexive pour l'édito. Public cible : praticiens ML/IA, ingénieurs, dirigeants tech, communauté DeepLearning.AI. Niveau : intermédiaire-accessible, sans jargon excessif mais avec spécifications techniques concrètes (paramètres, benchmarks, prix API).

**Style** : L'édito de Ng adopte un ton pédagogique-prescriptif typique de l'auteur — il pose une **taxonomie** (frontend / backend / infra / recherche) et la justifie par des arguments structurels (fluence linguistique des LLMs, capacité de boucle de test autonome, profondeur de la connaissance domaine requise). Pas de hype : Ng calibre les attentes, *"calibrer les attentes et l'organisation des équipes autour des capacités IA"*. Style direct, propositions courtes, citations clés en italique (*"coding agents are fluent in popular frontend languages like TypeScript and JavaScript"*, *"relatively limited"* pour l'infra). C'est de l'**éducation managériale** plus que du tutoriel technique : Ng s'adresse aux décideurs qui doivent allouer des ressources et organiser des équipes IA-augmentées.

Les sections actualités adoptent un format "fact-sheet" : développeur, innovation, specs, performances, contexte marché. Elles sont denses en chiffres (754B/40B, 1,40$/0,26$/4,40$ par million de tokens, 200 humanoïdes en 2026 → 5M en 2040, 64Md$ bloqués, 83%→41% jailbreaks). Cette densité chiffrée est la signature The Batch : **veille structurée pour praticiens** plutôt qu'analyse éditoriale longue.

Le numéro mis ensemble forme un **panorama de l'avril 2026 en IA appliquée** : où les agents accélèrent (logiciel par segment), où ils s'autonomisent (modèles 8h), où ils s'incarnent (robotique industrielle), où ils rencontrent une résistance physique (data centers), où ils dérivent (alignement / persona).

## Pense-betes

- **Numéro 350 de The Batch** publié le 24 avril 2026, ~15 minutes de lecture, édito signé Andrew Ng.
- **Hiérarchie d'accélération par les coding agents** (du plus accéléré au moins accéléré) :
  1. **Frontend** — *"coding agents are fluent in popular frontend languages like TypeScript and JavaScript"*. Boucle agent-navigateur autonome (l'agent test ses sorties dans un browser, itère). Quand le design est spécifié, l'implémentation est rapide.
  2. **Backend** — accélération **modérée**. Le développeur doit guider le modèle à travers les *corner cases*, les considérations de sécurité, et les migrations de base de données. Bugs subtils + effets en aval = supervision humaine expérimentée requise.
  3. **Infrastructure** — accélération **la moins forte**. Les LLMs ont une connaissance *"relatively limited"* des complexités et tradeoffs d'infra. Tests, expérimentation, debug de misconfigurations réseau exigent une expertise ingénieure profonde au-delà des capacités actuelles des agents.
  4. **Recherche** — accélération **minimale** malgré les bénéfices code. Les agents accélèrent la génération de code et l'orchestration d'expériences, mais le travail conceptuel (formation d'hypothèses, interprétation, itération) reste humain.
- **Conclusion managériale** : *"Understanding these distinctions helps organizations calibrate expectations and team organization around AI capabilities."*
- **Lecture en miroir avec Karpathy** (fiche [karpathy-vibe-coding-agentic-engineering-software-3-0-2026-04-29](karpathy-vibe-coding-agentic-engineering-software-3-0-2026-04-29.md)) : Ng propose une hiérarchie *par domaine*, Karpathy une explication *par verifiability* — domaines à signal de vérification fort (frontend rendu visuel, math/code) peakent ; domaines flous (infra, recherche conceptuelle) lag. **Les deux cadres sont congruents.**

### Actualité 1 — GLM-5.1 (Z.ai) : agent autonome 8h
- **Architecture** : MoE, **754B paramètres totaux**, **40B actifs par token**.
- **Contexte** : 200 000 tokens en input, 128 000 en output.
- **Licence** : MIT, poids ouverts (HuggingFace).
- **Prix API** : 1,40$ / 0,26$ (cached) / 4,40$ par million de tokens (input/cached/output).
- **Capacité distinctive** : tient autonomement jusqu'à **8 heures** sur une tâche unique, avec boucle plan→exécution→évaluation et abandon adaptatif après des centaines d'appels d'outils si l'approche échoue (au lieu de terminer prématurément).
- **Performances** : leader **SWE-Bench Pro 58,4%** (vs concurrents 54-57%) ; 3e Arena Code (1530 Elo) ; record CyberGym 68,7 ; trail GPQA Diamond 86,2% vs Gemini 3.1 à 94,3%.
- **Marché** : Z.ai a augmenté ses tarifs API ~40% et doublé le coût de l'abonnement coding — narrowing competitive gap avec proprio.

### Actualité 2 — Digit (Agility Robotics) sur ligne de production Schaeffler
- **Premier déploiement opérationnel** d'humanoïdes en industrie (Caroline du Sud, pièces auto).
- **Specs Digit** : 1m75 (5'9"), 65kg (143lb), jambes bipèdes inverted-knee, grippers 4 doigts, capteurs RGB depth + LiDAR + IMU.
- **Régime** : deux shifts de 4h avec recharge ; tâches spécifiées comme *workflows* (pas commandes moteur directes) — transfert de bin.
- **Économie** : Agility chiffre **10–25$/h opérationnel** vs **~20$/h** poste entry-level humain. Schaeffler prévoit des **centaines de déploiements** US + Europe d'ici 2030.
- **Contexte global** : ~200 humanoïdes en usine en 2026 ; **projection McKinsey : 5 millions en 2040**.
- **Effet emploi** : recherche suggère **restructuration plus que suppression** — promotion vers rôles supervision.

### Actualité 3 — Révolte anti-data-centers
- **Ampleur** : ~**64 Md$** de projets data-centers bloqués/retardés entre **mai 2024 et mars 2025**.
- **Législation** : Maine — moratoire installations ≥20MW jusqu'en 2027 (loi en attente signature gouverneur). Wisconsin (Port Washington) — premier référendum US exigeant **vote populaire** pour incitations fiscales aux mégaprojets. Missouri (Festus) — électeurs **ont évincé** des conseillers municipaux qui avaient approuvé un data center 6 Md$. Ohio — proposition d'amendement constitutionnel interdisant les installations ≥25MW.
- **Griefs** : pression sur le réseau électrique, hausse tarifs énergie résidentielle, consommation d'eau, nuisances sonores, impact voisinage, empreinte environnementale.
- **Incidents violents** : (1) **cocktail molotov sur la maison de Sam Altman** à San Francisco ; (2) coups de feu sur la résidence d'un conseiller d'Indianapolis qui avait soutenu un data center de 500M$.
- **Atténuants techniques** : closed-loop cooling économe en eau ; alimentation off-grid privée croissante.
- **Tension stratégique** : tech companies voient le data-center comme infrastructure de souveraineté IA face à la Chine — d'où expansion rapide malgré résistance locale.

### Actualité 4 — "Assistant axis" (Christina Lu, MATS / Oxford / Anthropic)
- **Problème** : LLMs entraînés comme assistants subissent une **dérive de persona** ("persona drift") en conversations longues ou émotionnellement chargées — adoption de traits alternatifs.
- **Solution** : un **"assistant axis"** = vecteur dérivé des outputs de couches qui mesure l'adhésion au persona assistant entraîné. Permet détection ET correction de la déviation.
- **Méthodologie** : 1200 questions de probing de caractère + 1375 system prompts alternatifs ; mesures sur Gemma 2 27B / Qwen3 32B / Llama 3.3 70B ; **"activation capping"** = contraindre les outputs dans les paramètres du persona assistant à l'inférence.
- **Résultats jailbreak** :
  - Qwen3 32B : réponses nocives **83% → 41%**
  - Llama 3.3 70B : réponses nocives **65% → 33%**
- **Préservation des perfs** : IFEval, GSM8k, MMLU-Pro, EQ-Bench **stables ou améliorés** — l'alignement renforcé ne compromet pas la capacité.
- **Exemple impact** : conversation de 30 tours autour d'idéations suicidaires — modèle non modifié glisse en ton inadapté ; version *capped* maintient frontières thérapeutiques + guidance compatissante.
- **Implication** : moyen pratique et léger de **stabiliser le persona** sans réentraîner — adjacent à la veille Anthropic sur character training (cf. [anthropic-measuring-political-bias-claude-2025-11-13](../2025-11/anthropic-measuring-political-bias-claude-2025-11-13.md)).

## RésuméDe400mots

Le 350e numéro de **The Batch**, newsletter hebdomadaire de DeepLearning.AI publiée le 24 avril 2026, s'ouvre sur un édito d'**Andrew Ng** structurant une **hiérarchie d'accélération par les coding agents** selon le type de travail logiciel. Ng pose un classement explicite : le **frontend** bénéficie de l'accélération maximale (les agents sont *"fluent in popular frontend languages like TypeScript and JavaScript"* et peuvent itérer en boucle navigateur autonome) ; le **backend** voit une accélération **modérée** (corner cases, sécurité, migrations DB nécessitent supervision humaine expérimentée) ; l'**infrastructure** profite **peu** des agents (les LLMs ont une connaissance *"relatively limited"* des tradeoffs réseau et système) ; et la **recherche** reste largement humaine sur le travail conceptuel d'hypothèse, d'interprétation et d'itération. Ng en tire une consigne managériale : calibrer attentes et organisation d'équipe selon ces différentiels.

Le numéro couvre ensuite quatre actualités structurantes. **GLM-5.1 de Z.ai** est un modèle MoE 754B paramètres (40B actifs), licence MIT, capable de tenir autonomement jusqu'à **8 heures** sur une tâche unique grâce à une boucle plan-exécution-évaluation. Il prend la tête de **SWE-Bench Pro à 58,4%** (vs 54-57% concurrents) et trône premier sur CyberGym (68,7), tout en restant en retrait sur le raisonnement (GPQA Diamond 86,2% vs Gemini 3.1 à 94,3%). Z.ai a parallèlement augmenté ses tarifs API d'environ 40%.

**Agility Robotics** déploie ses humanoïdes **Digit** sur les lignes de production de **Schaeffler** en Caroline du Sud — premier déploiement industriel opérationnel. Coût opérationnel chiffré 10-25$/h face à ~20$/h pour un poste entry-level humain. McKinsey projette 5 millions d'humanoïdes en usine d'ici 2040 (vs ~200 en 2026).

La **révolte anti-data-centers** prend de l'ampleur : ~64 Md$ de projets bloqués/retardés entre mai 2024 et mars 2025, moratoire dans le Maine pour les installations ≥20MW, premier référendum populaire au Wisconsin, conseillers évincés au Missouri. Deux incidents violents ont marqué : cocktail molotov sur la maison de Sam Altman à San Francisco, et coups de feu chez un conseiller d'Indianapolis. Les griefs portent sur le réseau électrique, les tarifs énergie, la consommation d'eau et les nuisances.

Enfin, des chercheurs (Christina Lu, MATS, Oxford, Anthropic) introduisent l'**"assistant axis"** — vecteur d'adhésion au persona entraîné permettant l'**activation capping**. Résultats : réponses nocives chez Qwen3 32B passent de 83% à 41%, chez Llama 3.3 70B de 65% à 33%, sans dégrader IFEval/GSM8k/MMLU-Pro/EQ-Bench.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Andrew Ng | PERSONNE | affirme_que | les coding agents accélèrent le frontend plus que le backend, l'infra et la recherche | CONCEPT | 0.98 | STATIQUE | déclaré_article |
| Andrew Ng | PERSONNE | dirige | DeepLearning.AI | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| The Batch | EVENEMENT | publie | numéro 350 | EVENEMENT | 0.99 | STATIQUE | déclaré_article |
| Frontend development | CONCEPT | est_accéléré_par | coding agents | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Coding agents | TECHNOLOGIE | maîtrise | TypeScript et JavaScript | TECHNOLOGIE | 0.96 | ATEMPOREL | déclaré_article |
| Infrastructure | CONCEPT | est_peu_accélérée_par | LLMs actuels | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| Recherche scientifique | CONCEPT | reste | majoritairement humaine | CONCEPT | 0.90 | ATEMPOREL | inféré |
| Z.ai | ORGANISATION | a_publié | GLM-5.1 | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| GLM-5.1 | TECHNOLOGIE | utilise | architecture MoE 754B / 40B actifs | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| GLM-5.1 | TECHNOLOGIE | tient_autonome | jusqu'à 8 heures par tâche | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| GLM-5.1 | TECHNOLOGIE | leader_de | SWE-Bench Pro à 58,4% | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| Agility Robotics | ORGANISATION | déploie | Digit chez Schaeffler | EVENEMENT | 0.98 | STATIQUE | déclaré_article |
| Digit | TECHNOLOGIE | coûte | 10-25$/h opérationnel | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| Humanoïdes en usine | CONCEPT | passeront_de | ~200 (2026) à 5 millions (McKinsey 2040) | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Mouvement anti-data-center | CONCEPT | a_bloqué | ~64 Md$ de projets entre mai 2024 et mars 2025 | EVENEMENT | 0.93 | STATIQUE | déclaré_article |
| Maine | LIEU | a_voté | moratoire data centers ≥20MW jusqu'en 2027 | EVENEMENT | 0.90 | STATIQUE | déclaré_article |
| Sam Altman | PERSONNE | a_subi | cocktail molotov à son domicile (SF) | EVENEMENT | 0.92 | STATIQUE | déclaré_article |
| Christina Lu | PERSONNE | a_proposé | l'assistant axis et l'activation capping | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Activation capping | METHODOLOGIE | réduit | jailbreaks Qwen3 32B de 83% à 41% | CONCEPT | 0.96 | STATIQUE | déclaré_article |
| Activation capping | METHODOLOGIE | préserve | IFEval, GSM8k, MMLU-Pro, EQ-Bench | CONCEPT | 0.94 | STATIQUE | déclaré_article |
| Hiérarchie d'accélération de Ng | CONCEPT | est_congruente_avec | verifiability framework de Karpathy | CONCEPT | 0.85 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Andrew Ng | PERSONNE | rôle | Fondateur DeepLearning.AI, auteur de l'édito | AJOUT |
| The Batch | EVENEMENT | type | Newsletter hebdomadaire IA, numéro 350 | AJOUT |
| DeepLearning.AI | ORGANISATION | secteur | Éducation IA / médias techniques | AJOUT |
| Z.ai | ORGANISATION | secteur | Modèles de fondation chinois (open-weights) | AJOUT |
| GLM-5.1 | TECHNOLOGIE | catégorie | Modèle MoE 754B/40B-actifs, licence MIT | AJOUT |
| Agility Robotics | ORGANISATION | secteur | Robotique humanoïde industrielle | AJOUT |
| Digit | TECHNOLOGIE | catégorie | Robot humanoïde bipède 1m75 / 65kg | AJOUT |
| Schaeffler | ORGANISATION | secteur | Pièces automobiles (Caroline du Sud, Allemagne) | AJOUT |
| Sam Altman | PERSONNE | rôle | CEO OpenAI, cible d'incident violent | MISE_A_JOUR |
| Christina Lu | PERSONNE | rôle | Chercheuse MATS / Oxford, en collaboration Anthropic | AJOUT |
| Assistant axis | CONCEPT | catégorie | Vecteur d'adhésion au persona assistant entraîné | AJOUT |
| Activation capping | METHODOLOGIE | catégorie | Contrainte d'outputs à l'inférence pour stabiliser persona | AJOUT |
| SWE-Bench Pro | EVENEMENT | catégorie | Benchmark agents codage, GLM-5.1 leader 58,4% | MISE_A_JOUR |
| Hiérarchie d'accélération | CONCEPT | catégorie | Frontend > Backend > Infra > Recherche (Ng 2026) | AJOUT |
| Mouvement anti-data-center | CONCEPT | catégorie | Opposition citoyenne et législative US 2024-2025 | AJOUT |
