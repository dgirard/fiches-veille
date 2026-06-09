# tatsyi-raiffeisen-ukraine-ai-engineers-different-not-just-faster-2026-05-05

## Veille
Tribune Medium d'**Hryhorii Tatsyi** (CTO, **Raiffeisen Bank Ukraine**, ~900 ingénieurs IT) qui rapporte une **étude longitudinale 12 mois** (mai 2025 → avril 2026) sur l'impact réel de l'IA générative dans une grande banque européenne. Thèse-pivot : ***"AI didn't make our engineers just faster. It made them different."*** Contrairement aux retours individuels (Frizzo, Cherny) ou méta (Curran/Intercom), c'est un **bilan organisationnel chiffré côté banque traditionnelle régulée** — corpus encore rare en 2026. Résultats : **−75 personnes (−8% effectif, dont 64 ingénieurs)** sur 12 mois, mais **plus de code livré, moins d'incidents, sécurité améliorée** ; adoption IA **62% → 83%** ; **68% des ingénieurs reçoivent ≥50% de leur code via assistance IA** ; **onboarding nouveaux ingénieurs 60-90 jours → ~40 jours** (cohérent données Anthropic 82→40 jours). Trois archétypes émergents : (1) **Copilot-only** +10-25% sur PRs, même rayon ; (2) **Multi-outils** story-points ×1.5-3, scope cross-repo +50-80% ; (3) **Claude sur stack corporate** volume code ×4.5, scope radicalement élargi. **Sept produits IA construits** qui n'existaient pas avant : Service Knowledge Hub (57 microservices, 83 releases/mois), Mobile Android workflow CI plan/implem/test, AI Agent Portal (2 085 users / 649 MAU en 87 jours, génération MCP via specs OpenAPI), Shift-left Security Plugin (−82% secrets exposés), DevPortal Backstage + agents diagnostics K8s (−68% temps résolution incidents critiques), DRAIF MCP text-to-SQL Data Lake 10 000 tables (embedding fine-tuné 2× OpenAI), Call Evaluation (>97% précision transcription, élu meilleur produit du groupe Raiffeisen). Stabilité : **incidents bloquants −70%, résolution critique −68%, alertes sécurité haute sévérité résolues +155%**. Insight stratégique central : ***"AI expanded our production possibility frontier, and we deliberately allocated the freed capacity"*** — IA ne fait pas plus vite la même chose, elle déplace **ce que l'on peut décider de faire**. Question d'évaluation à reformuler : non pas *"de combien % les KPIs existants ont augmenté"* mais ***"what your engineers built that didn't exist before"***. AI lifte les sous-performants à la baseline plus qu'elle n'accélère les top performers ; les **architectes seniors reviennent au code** après des années d'éloignement. Pertinence majeure pour COMEX banque/assurance/secteurs régulés (Raiffeisen = banque, Ukraine = contexte de guerre + résilience opérationnelle).

## Titre Article
AI didn't make our engineers just faster. It made them different.

## Date
2026-05-05

## URL
https://medium.com/@milhibisidek/ai-didnt-make-our-engineers-just-faster-it-made-them-different-95f1c1d4efd0

## Keywords
Hryhorii Tatsyi, Raiffeisen Bank Ukraine, CTO bank, étude longitudinale 12 mois, AI didn't make engineers just faster made them different, production possibility frontier, freed capacity allocation, 900 ingénieurs, −75 personnes en 12 mois, −64 ingénieurs, adoption IA 62 to 83 pourcent, 68 pourcent engineers AI assistance majoritaire, onboarding 60-90 jours vers 40 jours, three archetypes, Copilot only 10-25 pourcent, multi-tool engineers 1.5-3x story points, Claude on corporate stack 4.5x code volume, seven new products, Service Knowledge Hub, 57 microservices 83 releases per month, Mobile Android workflow CI plan implement test, AI Agent Portal 2085 users 649 MAU, MCP agents from OpenAPI specs, Shift-left Security Plugin -82 pourcent secrets exposed, DevPortal Backstage Kubernetes diagnostics, -68 pourcent critical incident resolution time, DRAIF MCP text-to-SQL Data Lake 10000 tables, embedding fine-tuned 2x OpenAI, Call Evaluation >97 pourcent transcription accuracy, best product Raiffeisen group, blocking incidents -70 pourcent, security alerts resolved +155 pourcent, AI lifts underperformers to baseline, senior architects return to active development, what your engineers built that didn't exist before, banque régulée, secteur bancaire IA, Ukraine résilience opérationnelle, étude organisationnelle, large enterprise IT 900 engineers, contraction effectif productivité maintenue, dette technique remboursée, debt repayment freed capacity, headcount contraction shipping more, deliberately allocated freed capacity, type de travail transformé pas seulement vitesse, measure AI impact

## Authors
**Hryhorii Tatsyi** — CTO de **Raiffeisen Bank Ukraine** (filiale ukrainienne du groupe bancaire autrichien Raiffeisen Bank International, RBI). Auteur Medium @milhibisidek. Profil discret côté visibilité publique (25 followers Medium au moment de la publication), mais position institutionnelle de premier plan : il dirige une organisation IT d'environ 900 ingénieurs dans une banque systémique opérant en contexte ukrainien (économie de guerre depuis 2022, résilience opérationnelle critique). L'article est sa première contribution publique d'envergure documentée sur cette plateforme.

## Ton
**Profil** : Tribune Medium **CTO-organizational case study** d'environ 17 minutes de lecture, signée par un CTO en exercice qui rapporte les résultats d'une transformation IA structurée et documentée sur 12 mois dans une banque européenne régulée. Format hybride entre **rapport de transformation interne** (chiffré, sourcé, métrique) et **essai stratégique** (thèse-pivot, ré-encadrement de la question d'évaluation). Public cible : pairs CTO/CIO/DSI de grandes organisations IT, notamment dans des secteurs régulés (banque, assurance, télécom, énergie) qui cherchent des **case studies organisationnels** plutôt que des témoignages individuels ou des promesses vendor. Public secondaire : COMEX, board members, analystes industriels, équipes RH/transformation, communautés Engineering Management.

**Style** : Voix première personne du pluriel (*"our engineers"*, *"we deliberately allocated"*) qui assume la **position institutionnelle et la responsabilité décisionnelle**. Anglais clair, factuel, **densité chiffrée élevée** (pourcentages d'adoption, volumes de PRs, cycles d'incidents, tailles d'utilisateurs, coefficients d'embedding). Registre **sobre, pédagogique, sans hype** — c'est l'éthique du *practitioner-CTO* qui rapporte ce qui a marché et ce qui a transformé l'organisation, pas un manifesto. Pas de catastrophisme non plus : Tatsyi ne dramatise pas la réduction d'effectifs, il la **contextualise** dans une **réallocation délibérée de la capacité libérée** vers features, stabilité et remboursement de dette technique.

**Aphorismes-clés** :
- ***"AI didn't make our engineers just faster. It made them different."*** (titre — symétrie *vitesse / nature du travail* qui résume la thèse).
- ***"AI expanded our production possibility frontier, and we deliberately allocated the freed capacity."*** (la phrase-pivot stratégique — économique-organisationnelle).
- ***"What your engineers built that didn't exist before."*** (la question d'évaluation reformulée — la **bonne métrique**).

**Métaphores travaillées** :
- **Production possibility frontier** — emprunt à la microéconomie qui rend visible que l'IA ne fait pas mieux la même chose, elle **déplace l'ensemble des choix possibles**. Métaphore particulièrement puissante pour COMEX et boards rompus au vocabulaire stratégique.
- **Freed capacity allocation** — le langage du *capacity planning* IT projeté sur la transformation IA : la capacité libérée est un **actif à allouer**, pas un coût à éliminer. Cadre la réduction d'effectifs comme une **réaffectation stratégique**.
- **Three archetypes** — typologie tripartite des ingénieurs (Copilot-only / Multi-outils / Claude-on-corporate-stack) qui rend tangible la **distribution inégale** de l'impact IA au sein d'une même organisation.
- **AI lifts underperformers to baseline** — formule contre-intuitive (l'IA n'accélère pas surtout les rapides, elle **rattrape les lents**) qui retourne le cliché habituel.

**Position épistémique** : équilibrée et **assumée institutionnellement**. Tatsyi rapporte des **gains massifs** sans triomphalisme et **n'élude pas** les sujets sensibles (réduction d'effectifs, redéfinition du métier). Il s'inscrit explicitement dans la lignée des études Anthropic (chiffres d'onboarding) tout en apportant un **angle banque/Europe centrale** qui manque au corpus dominant Silicon-Valley-centric. La démarche est **bayésienne** : il publie des chiffres internes vérifiables qui peuvent être contredits ou confirmés par d'autres CTO européens.

**Autorité** : construite par (a) la **position institutionnelle** (CTO d'une banque systémique régulée), (b) la **densité chiffrée et la couverture longitudinale** (12 mois, 900 ingénieurs, sept produits, métriques stabilité/sécurité), (c) la **convergence avec données Anthropic externes** (onboarding 82→40 jours), (d) la **sobriété du ton** qui inspire confiance aux pairs CTO, (e) le **contexte ukrainien** qui ajoute une dimension de **résilience opérationnelle prouvée en conditions adverses**. Limite : Tatsyi est encore peu visible publiquement (25 followers Medium), donc l'autorité repose sur le **fond chiffré** plutôt que sur la marque personnelle.

## Pense-betes

- **Date / source** : mai 2026 (relatif "2 days ago" au moment de la consultation, soit ~2026-05-05), **Medium** @milhibisidek. URL : https://medium.com/@milhibisidek/ai-didnt-make-our-engineers-just-faster-it-made-them-different-95f1c1d4efd0
- **Format** : tribune CTO **organizational case study** (~17 min lecture).
- **Auteur** : **Hryhorii Tatsyi**, **CTO Raiffeisen Bank Ukraine** — banque systémique régulée, ~900 ingénieurs IT.
- **Période d'étude** : **mai 2025 → avril 2026** (12 mois pleins).
- **Titre-aphorisme** : ***"AI didn't make our engineers just faster. It made them different."***
- **Phrase-pivot stratégique** : ***"AI expanded our production possibility frontier, and we deliberately allocated the freed capacity."***

### Cadrage organisationnel — la transformation observée

| Dimension | Avant (mai 2025) | Après (avril 2026) | Variation |
|-----------|------------------|--------------------|-----------|
| Effectif IT | ~900 ingénieurs | ~825 (−75 personnes, dont 64 ingénieurs) | **−8%** |
| Adoption IA | 62% | 83% | **+21 points** |
| Engineers ≥50% code via IA | — | 68% | nouvelle métrique |
| Onboarding (1er PR) | 60-90 jours | ~40 jours | **−~50%** |
| Volume code livré | baseline | augmenté | **↑** |
| Incidents bloquants | baseline | −70% | **↓** |
| Temps résolution critiques | baseline | −68% | **↓** |
| Alertes sécurité haute sévérité résolues | baseline | +155% | **↑** |

**Lecture** : la contraction d'effectif (−8%) **s'accompagne** d'une amélioration sur tous les axes — production, qualité, sécurité, onboarding. C'est la **donnée centrale** que Tatsyi met en évidence et qu'il **n'esquive pas politiquement**.

### Trois archétypes d'ingénieurs émergents

| Archétype | Outils | Effet productivité | Effet périmètre |
|-----------|--------|---------------------|------------------|
| **Copilot-only** | GitHub Copilot seul | +10-25% sur PRs | rayon stable |
| **Multi-outils** | combinaison plusieurs assistants IA | story-points **×1.5-3** | scope cross-repo **+50-80%** |
| **Claude sur stack corporate** | Claude Code (ou équivalent) intégré stack interne | volume code **×4.5** | scope **radicalement élargi** |

**Convergence** : architectes seniors **reviennent au code** après des années d'éloignement (cohérent avec la promesse Karpathy *"agents reduce friction to creation"* et Cherny *"best accountant writes accounting software"*).

**Insight contre-intuitif** : ***l'IA lifte les sous-performants à la baseline plutôt que d'accélérer surtout les top performers.*** Position **opposée à la lecture "tail élite 10×+"** (Cherny / Curran top 5% / Karpathy) — Tatsyi décrit un **effet de rattrapage par le bas** qui resserre la distribution. Les deux lectures sont **compatibles** : la distribution se **resserre par le bas** ET **s'élargit par le haut** (top performers qui restent à 10×+).

### Sept produits IA construits qui n'existaient pas avant

| # | Produit | Description | Métriques clés |
|---|---------|-------------|----------------|
| 1 | **Service Knowledge Hub** | Documentation auto-générée de microservices via parsing Kubernetes | **57 microservices**, **83 releases/mois** |
| 2 | **Mobile Android workflow CI** | Pipeline auto plan / implementation / test pour mobile | redesign complet du SDLC mobile |
| 3 | **AI Agent Portal** | Portail interne génération automatique d'agents MCP via specs OpenAPI | **2 085 users**, **649 MAU**, **87 jours** pour atteindre cette adoption |
| 4 | **Shift-left Security Plugin** | Détection vulnérabilités dans IDE avant commit | **−82% secrets exposés** |
| 5 | **DevPortal** | Backstage + agents IA diagnostics Kubernetes | **−68% temps résolution incidents critiques** |
| 6 | **DRAIF MCP** | Text-to-SQL sur Data Lake | **10 000 tables**, embedding fine-tuné **×2 modèles OpenAI** |
| 7 | **Call Evaluation** | Analyse transcription audio + redesign scripts | **>97% précision**, **élu meilleur produit du groupe Raiffeisen** (RBI) |

**Lecture stratégique** : ce n'est **pas** une liste d'expérimentations, c'est un **portefeuille produit** déployé en production, avec adoption interne mesurable et un produit (Call Evaluation) qui **traverse les filiales du groupe** (passage du local au global RBI).

### La thèse-pivot — production possibility frontier

> ***"AI expanded our production possibility frontier, and we deliberately allocated the freed capacity."***

- **Mot-clé 1 — "expanded"** : l'IA ne fait pas mieux la même chose, elle **agrandit l'ensemble des possibles**.
- **Mot-clé 2 — "deliberately allocated"** : la capacité libérée est **redirigée par décision managériale**, pas absorbée mécaniquement par plus du même travail.
- **Trois directions de réallocation** :
  1. **Features** (nouveaux produits — les 7 listés ci-dessus).
  2. **Stabilité** (incidents −70%, résolution −68%).
  3. **Remboursement de dette technique** (rare et capitalisable côté CTO).

### La question d'évaluation reformulée

**Mauvaise question** : *"De combien % nos KPIs existants ont-ils augmenté ?"*
**Bonne question** : ***"What did your engineers build that didn't exist before?"***

**Pourquoi cela compte** : les pourcentages sur les métriques existantes **manquent la transformation principale** — non pas vitesse mais **type de travail**. Si l'on optimise les KPIs hérités, on **rate la fenêtre stratégique** où l'IA permet de construire ce qui n'était pas adressable.

### Articulation dossier veille

#### Convergences chiffrées (médiane committée 3-5×)
- **Frizzo** (LinkedIn 2026-05-05) : 3-5× productivity multiplier sur 1 an d'usage quotidien.
- **Wescale Usine Logicielle Augmentée** (2026-05-03) : *"X3-X4 réalistes"*.
- **Curran/Intercom** (2026-04-16) : 3× productivité R&D sur 16 mois (organisation entière, 500 R&D).
- **DORA Report 2025** (2025-09-23) et **Stanford Denisov-Blanch** (2025-11-23).
- **Tatsyi/Raiffeisen** (2026-05-05) : *story-points ×1.5-3 (multi-outils), ×4.5 volume code (Claude stack corporate)*.

#### Convergence onboarding (60-90j → ~40j)
- **Tatsyi/Raiffeisen** : 60-90 jours → ~40 jours.
- **Anthropic études internes** (citées par Sun NYT 2026-04-30 et autres) : 82 jours → 40 jours.
- → Lecture juste : **convergence indépendante** entre une banque européenne et un acteur IA Silicon Valley sur le **même chiffre cible (~40 jours)**. C'est un **fait stylisé** robuste pour 2026.

#### Convergence "sept nouveaux produits" / capacité de création
- **Tatsyi** : 7 produits IA en 12 mois.
- **Cherny** (2026-05) : 100% du code généré, *"a few dozen PRs/day, 150 PRs in a single day record"*, multiples produits Anthropic Labs.
- **Curran/Intercom** (2026-04-16) : Skills-Based Plugin Architecture (153 contributeurs, **267 skills**).
- **Wescale** (2026-05-03) : *"besoins historiques restés trop coûteux peuvent enfin être adressés"*.
- → **Convergence forte** : la mesure pertinente n'est plus la vitesse sur l'existant mais le **portefeuille de nouveaux produits / nouveaux espaces adressables**.

#### Convergence "le métier change de forme"
- **Frizzo** (2026-05-05) : *"the new bottleneck is supervision"*, *"writing muscle atrophy"*.
- **Tatsyi** (2026-05-05) : *"AI didn't make our engineers just faster. It made them different"*, **trois archétypes émergents**, **architectes seniors qui reviennent au code**.
- **Karpathy** (2026-04-29) : *Software 1.0/2.0/3.0*, *"outsource thinking but not understanding"*.
- **Mornati** (2026-03-14) : *What is a Developer When We Use Coding Agents?*
- **Habert PROJ-AI** (2026-05-05) : *"directives agent + Decision Records + cinq dimensions de validation"*.
- → **Convergence transversale** : la nature du travail a changé, pas seulement la vitesse. Tatsyi apporte la **donnée organisationnelle banque** qui manquait au corpus.

#### Tension productive avec "AI lifts underperformers"
- **Cherny** (2026-05) : tail élite 10×+ (150 PRs/jour record).
- **Curran/Intercom** (2026-04-16) : top 5% à 6× le median PR throughput (≈ 18× baseline pré-IA).
- **Karpathy** (2026-04-29) : *"10× is not the speed up — people who are very good at this peak a lot more than 10×"*.
- **Tatsyi/Raiffeisen** (2026-05-05) : *"AI lifts underperformers to baseline"* — effet de **rattrapage par le bas**.
- → Lecture **compatible et féconde** : la distribution se **resserre par le bas** (Tatsyi) ET **s'élargit par le haut** (Cherny, Karpathy, Curran top 5%). Les deux phénomènes coexistent. À utiliser pour des présentations COMEX qui veulent à la fois rassurer (rattrapage) et inspirer (top performers).

#### Position FR / Europe centrale vs anglo-saxonne
- Tatsyi est **européen** (Ukraine, groupe autrichien RBI), banque **régulée**, en **contexte de guerre**.
- Sa **rigueur méthodologique** (12 mois, chiffres internes, granularité par archétype) rejoint la **prudence française** (Wescale, Habert) plus que l'**optimisme américain** (Cherny, Curran).
- À mobiliser dans les présentations FR comme **case study européen banque** complémentaire des chiffres Wescale/cabinet et Curran/SaaS.
- **Avantage rare** : un CTO de **banque systémique** qui publie ses chiffres internes — type de témoignage **quasiment absent** du corpus 2026.

### Limites à signaler

- **Pas de méthodologie chiffrée détaillée** : Tatsyi rapporte des pourcentages sans documenter précisément comment ils sont mesurés (ex: "story-points ×1.5-3" — quelle baseline ? quelle attribution ? quel ajustement biais).
- **Auteur peu visible publiquement** (25 followers Medium) — autorité reposant sur la position institutionnelle plutôt que sur la marque personnelle. À pondérer par d'autres sources si l'enjeu est de citer en COMEX.
- **Pas de discussion explicite des coûts cognitifs** (FOMO, deskilling, ownership erosion) que Frizzo nomme. Tatsyi est **organisationnel**, Frizzo est **individuel** — les deux fiches se complètent.
- **Pas de discussion des risques régulatoires** spécifiques au secteur bancaire (RGPD, DORA EU, supervision BCE/EBA) — étonnant pour un CTO de banque systémique. Sujet potentiellement écarté pour préserver la lisibilité de l'article public.
- **Convergence onboarding 82→40j avec Anthropic** : à vérifier si la donnée Anthropic citée est bien l'étude que Tatsyi mentionne (risque de cherry-picking inverse — convergence apparente sur un chiffre rond).
- **Échantillon n=1 organisation** : un seul cas, même chiffré. À répliquer chez d'autres banques européennes pour conclure à un fait stylisé sectoriel.

### À mobiliser pour

- **Présentations COMEX banque/assurance/secteurs régulés** : case study européen rare, chiffré, contre-poids à la sur-représentation Silicon Valley dans les corpus.
- **Stratégie RH / transformation** : justifier la **réallocation de capacité libérée** plutôt que la simple réduction de coûts.
- **Boards / sponsors transformation** : reformulation de la question d'évaluation (*"what did your engineers build that didn't exist before"*) — outil de **désamorçage du débat % productivité**.
- **Sourcing chiffré convergent** : 60-90j → ~40j onboarding (Anthropic + Tatsyi), 3-5× médiane committée, contraction effectif compatible avec amélioration production/qualité/sécurité.
- **Débat équité / déformation distribution productivité** : à utiliser **avec** Cherny/Karpathy/Curran top 5% pour présenter une lecture nuancée — l'IA **resserre par le bas** ET **élargit par le haut** simultanément.
- **Communauté Engineering Management** : une rare publication CTO de grande organisation IT régulée européenne sur le sujet.

## RésuméDe400mots

Hryhorii Tatsyi, CTO de **Raiffeisen Bank Ukraine** (~900 ingénieurs IT), publie en mai 2026 sur Medium un retour d'expérience longitudinal **12 mois** (mai 2025 → avril 2026) sur la transformation IA de son organisation. Le titre concentre la thèse : ***"AI didn't make our engineers just faster. It made them different."*** C'est un des **rares case studies organisationnels chiffrés côté banque européenne régulée** disponibles en 2026.

**Données centrales** : effectif IT contracté de **75 personnes (−8%, dont 64 ingénieurs)** — pourtant **plus de code livré, moins d'incidents, sécurité améliorée**. Adoption IA passée de **62% à 83%** ; **68% des ingénieurs reçoivent ≥50% de leur code via assistance IA** ; onboarding nouveaux ingénieurs **60-90 jours → ~40 jours** (cohérent données Anthropic 82→40 jours, **convergence indépendante**).

**Trois archétypes** émergents : (1) **Copilot-only** : +10-25% sur PRs, rayon stable ; (2) **Multi-outils** : story-points **×1.5-3**, scope cross-repo **+50-80%** ; (3) **Claude sur stack corporate** : volume code **×4.5**, scope radicalement élargi. Insight contre-intuitif : ***"AI lifts underperformers to baseline"*** plutôt que d'accélérer surtout les top performers — la distribution se **resserre par le bas**. Architectes seniors **reviennent au code** après des années d'éloignement.

**Sept nouveaux produits IA** (qui n'existaient pas avant) : Service Knowledge Hub (57 microservices, 83 releases/mois), Mobile Android workflow CI, AI Agent Portal (2 085 users / 649 MAU en 87 jours, génération MCP via OpenAPI), Shift-left Security Plugin (−82% secrets exposés), DevPortal Backstage + agents diagnostics K8s (−68% temps résolution incidents critiques), DRAIF MCP text-to-SQL Data Lake 10 000 tables (embedding fine-tuné ×2 OpenAI), Call Evaluation (>97% précision, **élu meilleur produit du groupe Raiffeisen International**). Stabilité : **incidents bloquants −70%, résolution critique −68%, alertes sécurité haute sévérité résolues +155%**.

**Thèse-pivot stratégique** : ***"AI expanded our production possibility frontier, and we deliberately allocated the freed capacity"*** — features, stabilité, remboursement de dette technique. **Question d'évaluation reformulée** : non pas *"de combien % les KPIs existants ont augmenté"* mais ***"what did your engineers build that didn't exist before"***.

**Articulation dossier veille** : convergence chiffrée médiane committée avec Frizzo (2026-05-05), Wescale (2026-05-03), Curran/Intercom (2026-04-16), DORA 2025, Stanford Denisov-Blanch (2025-11-23). Convergence indépendante onboarding ~40 jours avec Anthropic. Tension productive avec Cherny / Curran top 5% / Karpathy (tail élite 10×+) : la distribution **se resserre par le bas** ET **s'élargit par le haut** — les deux lectures coexistent. Convergence transversale "le métier change de forme" avec Frizzo, Karpathy, Mornati, Habert. À mobiliser pour COMEX banque/secteurs régulés, sponsors transformation, débat équité distribution productivité.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Hryhorii Tatsyi | PERSONNE | publie | AI didn't make our engineers just faster | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Hryhorii Tatsyi | PERSONNE | dirige | Raiffeisen Bank Ukraine (IT, en tant que CTO) | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Raiffeisen Bank Ukraine | ORGANISATION | mesure | ~900 ingénieurs IT | MESURE | 0.94 | DYNAMIQUE | déclaré_article |
| Raiffeisen Bank Ukraine | ORGANISATION | réduit | effectif de 75 personnes (dont 64 ingénieurs) en 12 mois | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Raiffeisen Bank Ukraine | ORGANISATION | mesure | adoption IA de 62% à 83% | MESURE | 0.95 | STATIQUE | déclaré_article |
| Onboarding Raiffeisen | CONCEPT | mesure | passage de 60-90 jours à ~40 jours | MESURE | 0.94 | STATIQUE | déclaré_article |
| Onboarding ~40 jours | CONCEPT | converge_avec | données Anthropic 82→40 jours | CONCEPT | 0.92 | DYNAMIQUE | inféré |
| Copilot-only, Multi-outils, Claude-on-corporate-stack | CONCEPT | fait_partie_de | Trois archétypes ingénieurs | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Claude sur stack corporate | CONCEPT | mesure | volume code ×4.5 | MESURE | 0.93 | DYNAMIQUE | déclaré_article |
| Multi-outils | CONCEPT | mesure | story-points ×1.5-3 | MESURE | 0.93 | DYNAMIQUE | déclaré_article |
| Copilot-only | CONCEPT | mesure | PRs +10-25% | MESURE | 0.93 | DYNAMIQUE | déclaré_article |
| AI | TECHNOLOGIE | améliore | sous-performants (rattrapage à la baseline) | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| Retour des architectes seniors au développement actif | CONCEPT | observé_dans | Raiffeisen Bank Ukraine | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Raiffeisen Bank Ukraine | ORGANISATION | a_créé | sept produits IA inédits en 12 mois | CONCEPT | 0.96 | STATIQUE | déclaré_article |
| Service Knowledge Hub | TECHNOLOGIE | s_applique_à | 57 microservices, 83 releases/mois | CONCEPT | 0.94 | DYNAMIQUE | déclaré_article |
| AI Agent Portal | TECHNOLOGIE | mesure | 2 085 users / 649 MAU en 87 jours | MESURE | 0.94 | STATIQUE | déclaré_article |
| AI Agent Portal | TECHNOLOGIE | permet | génération d'agents MCP via specs OpenAPI | TECHNOLOGIE | 0.94 | ATEMPOREL | déclaré_article |
| Shift-left Security Plugin | TECHNOLOGIE | réduit | secrets exposés de 82% | CONCEPT | 0.93 | DYNAMIQUE | déclaré_article |
| DevPortal Backstage | TECHNOLOGIE | réduit | temps résolution incidents critiques de 68% | CONCEPT | 0.93 | DYNAMIQUE | déclaré_article |
| DRAIF MCP | TECHNOLOGIE | s_applique_à | Data Lake 10 000 tables en text-to-SQL | CONCEPT | 0.93 | DYNAMIQUE | déclaré_article |
| DRAIF MCP embedding fine-tuné | TECHNOLOGIE | surpasse | modèles OpenAI (×2) | TECHNOLOGIE | 0.91 | DYNAMIQUE | déclaré_article |
| Call Evaluation | TECHNOLOGIE | mesure | >97% précision transcription | MESURE | 0.93 | DYNAMIQUE | déclaré_article |
| Groupe Raiffeisen (RBI) | ORGANISATION | recommande | Call Evaluation (élu meilleur produit du groupe) | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| Incidents bloquants Raiffeisen | CONCEPT | mesure | −70% | MESURE | 0.94 | STATIQUE | déclaré_article |
| Alertes sécurité haute sévérité résolues | CONCEPT | mesure | +155% | MESURE | 0.93 | STATIQUE | déclaré_article |
| Hryhorii Tatsyi | PERSONNE | affirme_que | "AI expanded our production possibility frontier" | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| Capacité libérée par IA | CONCEPT | s_applique_à | features + stabilité + dette technique (allocation délibérée) | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Hryhorii Tatsyi | PERSONNE | recommande | mesurer ce que les ingénieurs construisent qui n'existait pas | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Bilan Tatsyi | CONCEPT | affine | lecture "tail élite 10×" Cherny/Karpathy | CONCEPT | 0.90 | DYNAMIQUE | inféré |
| Bilan Tatsyi | CONCEPT | soutient | resserrement par le bas et élargissement par le haut simultanés de la distribution productivité | CONCEPT | 0.92 | ATEMPOREL | inféré |
| Case study Raiffeisen | CONCEPT | converge_avec | témoignage individuel Frizzo (complémentarité) | CONCEPT | 0.93 | ATEMPOREL | inféré |
| Bilan Tatsyi | CONCEPT | converge_avec | Wescale X3-X4, Curran 3×, DORA 2025 | CONCEPT | 0.92 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Hryhorii Tatsyi | PERSONNE | rôle | CTO Raiffeisen Bank Ukraine, auteur Medium @milhibisidek, témoin organisationnel banque européenne régulée 12 mois | AJOUT |
| Raiffeisen Bank Ukraine | ORGANISATION | secteur | Banque systémique régulée, filiale Raiffeisen Bank International (RBI, Autriche), ~900 ingénieurs IT, contexte ukrainien (économie de guerre depuis 2022) | AJOUT |
| Raiffeisen Bank International (RBI) | ORGANISATION | secteur | Groupe bancaire autrichien, parent de Raiffeisen Bank Ukraine | AJOUT |
| "AI didn't make our engineers just faster. It made them different" | CONCEPT | source | Aphorisme-titre Tatsyi — symétrie vitesse/nature du travail | AJOUT |
| "AI expanded our production possibility frontier" | CONCEPT | source | Phrase-pivot stratégique Tatsyi — emprunt microéconomie, rend visible que l'IA déplace l'ensemble des choix possibles, pas seulement la vitesse | AJOUT |
| "What did your engineers build that didn't exist before" | CONCEPT | source | Question d'évaluation reformulée Tatsyi — bonne métrique stratégique IA | AJOUT |
| Trois archétypes ingénieurs IA | CONCEPT | définition | (1) Copilot-only +10-25% PRs ; (2) Multi-outils story-points ×1.5-3, scope cross-repo +50-80% ; (3) Claude-on-corporate-stack volume code ×4.5, scope radicalement élargi | AJOUT |
| AI lifts underperformers to baseline | CONCEPT | source | Insight Tatsyi contre-intuitif — l'IA resserre la distribution par le bas, contre-poids à la lecture "tail élite 10×+" (Cherny/Karpathy/Curran top 5%) | AJOUT |
| Senior architects return to active development | CONCEPT | source | Observation Tatsyi — convergence avec Cherny "best accountant writes accounting software" et Karpathy reduction friction to creation | AJOUT |
| Service Knowledge Hub | TECHNOLOGIE | description | Produit interne Raiffeisen — documentation auto-générée de 57 microservices via parsing Kubernetes, 83 releases/mois | AJOUT |
| AI Agent Portal | TECHNOLOGIE | description | Produit interne Raiffeisen — portail génération automatique d'agents MCP via specs OpenAPI ; 2 085 users / 649 MAU atteints en 87 jours | AJOUT |
| Shift-left Security Plugin | TECHNOLOGIE | description | Produit interne Raiffeisen — détection vulnérabilités dans IDE avant commit ; −82% secrets exposés | AJOUT |
| DevPortal Raiffeisen | TECHNOLOGIE | description | Backstage intégré + agents IA diagnostics Kubernetes ; −68% temps résolution incidents critiques | AJOUT |
| DRAIF MCP | TECHNOLOGIE | description | Produit interne Raiffeisen — text-to-SQL sur Data Lake 10 000 tables ; embedding fine-tuné ×2 modèles OpenAI | AJOUT |
| Call Evaluation | TECHNOLOGIE | description | Produit interne Raiffeisen — analyse transcription audio >97% précision + redesign scripts data-driven ; élu meilleur produit du groupe RBI (passage filiale → groupe) | AJOUT |
| Mobile Android workflow CI | TECHNOLOGIE | description | Produit interne Raiffeisen — pipeline auto plan / implementation / test pour mobile, redesign complet du SDLC mobile | AJOUT |
| Onboarding 60-90j → ~40j | CONCEPT | convergence | Tatsyi/Raiffeisen 2026-05-05 + Anthropic études internes (citées Sun NYT 2026-04-30) — convergence indépendante banque européenne / acteur IA Silicon Valley sur le même chiffre cible (~40 jours) | MISE_A_JOUR |
| Productivité 3-5× (médiane committée) | CONCEPT | convergence | Tatsyi (story-points ×1.5-3, ×4.5 volume code Claude stack), Frizzo (LinkedIn 2026-05-05), Wescale (2026-05-03), Curran/Intercom (2026-04-16), DORA Report 2025, Stanford Denisov-Blanch (2025-11-23) | MISE_A_JOUR |
| Distribution productivité IA | CONCEPT | description | Hypothèse féconde : la distribution se resserre par le bas (Tatsyi : underperformers→baseline) ET s'élargit par le haut (Cherny 150 PRs/jour, Curran top 5% à 6× median, Karpathy "peaks much higher than 10×") — les deux phénomènes coexistent | AJOUT |
| Production possibility frontier (IA) | CONCEPT | définition | Métaphore microéconomique Tatsyi — l'IA ne fait pas mieux la même chose, elle agrandit l'ensemble des possibles ; capacité libérée à allouer délibérément | AJOUT |
| Freed capacity allocation | CONCEPT | définition | Réallocation délibérée de la capacité libérée par IA vers (1) features, (2) stabilité, (3) remboursement dette technique | AJOUT |
| Case study banque européenne régulée IA | CONCEPT | description | Tatsyi/Raiffeisen Bank Ukraine 2026-05 — corpus encore rare en 2026 où dominent les retours Silicon Valley (Cherny, Curran, Stripe) ; complémentaire Frizzo (individuel) et Wescale (cabinet FR) | AJOUT |
