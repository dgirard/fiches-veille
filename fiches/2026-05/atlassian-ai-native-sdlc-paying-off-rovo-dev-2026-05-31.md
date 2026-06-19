# atlassian-ai-native-sdlc-paying-off-rovo-dev-2026-05-31

## Veille

Étude data d'Atlassian (Inside Atlassian) mesurant le retour réel d'un **SDLC AI-native** outillé par **Rovo Dev**. Sur 3 400 dépôts de 2 500 clients (quasi-expérience avec appariement par score de propension), les dépôts adoptants mergent **19 % de PR en plus par mois** ; jusqu'à **37-51 %** sur les dépôts peu/moyennement actifs et **59-87 %** quand **3 à 5 membres** de l'équipe adoptent l'outil. Côté efficience, les développeurs gagnent **2-3 h/semaine** (≈10 % des 24 h consacrées au code et à la revue), soit 20-30 h/semaine réinvesties pour une équipe de 10. La thèse : résoudre le « paradoxe de la productivité » de Solow (1987) en passant de **métriques d'usage** (tokens) à des **métriques d'impact** (throughput, heures gagnées, taux d'échec, satisfaction). Recommandation : démarrer par une **équipe** (pas un individu) et mesurer 2-3 mois après.

## Titre Article

The AI-native SDLC is paying off: 19% more PRs and 2–3 hours saved per developer per week

## Date

2026-05-31

## URL

https://www.atlassian.com/blog/ai-at-work/ai-native-sdlc-paying-off-per-developer-per-week

## Keywords

SDLC AI-native, Rovo Dev, agents de codage, productivité des développeurs, PR throughput, débit de pull requests, heures gagnées, paradoxe de la productivité, Solow, quasi-expérience, score de propension, métriques d'impact, métriques d'usage, tokens, change failure rate, satisfaction développeur, Teamwork Graph, contexte, adoption d'équipe, mesure, DevEx, DORA

## Authors

Robbie Geoghegan, Fan Jiang (Atlassian)

## Ton

Profil : article de blog d'entreprise (Inside Atlassian) co-signé par deux data scientists, perspective « nous » d'éditeur mesurant son propre produit, registre data-driven et rigoureux (méthodologie quasi-expérimentale explicitée), niveau technique modéré, public cible dirigeants ingénierie, EM, DevEx/platform leads et décideurs achat outillage IA. Le ton conjugue **autorité méthodologique** (taille d'échantillon, appariement par propension, percentile conservateur pour les estimations d'enquête) et **argumentaire commercial assumé** : l'article démontre la valeur de Rovo Dev tout en se présentant comme un cadre de mesure généralisable. La rhétorique s'appuie sur des **chiffres calibrés et nuancés** (fourchettes, segmentation par activité du dépôt et par nombre d'adoptants) plutôt que sur des promesses absolues, ce qui renforce sa crédibilité. Cadrage intellectuel via la citation de Solow (1987, « you can see the computer age everywhere but in the productivity statistics ») qui positionne l'IA dans la lignée des débats sur le paradoxe de la productivité, et résout le paradoxe par un déplacement des métriques (usage → impact). Métaphore implicite du partenariat humain-agent à chaque étape du cycle.

## Pense-betes

- **Thèse centrale** : le SDLC AI-native « paie » — mais seulement si on le mesure par l'**impact** (débit de PR, heures gagnées, qualité, satisfaction), pas par l'**usage** (tokens consommés).
- **Chiffre phare** : les dépôts adoptant **Rovo Dev** mergent **+19 % de PR par mois** vs non-adoptants.
- **Effet d'amplification par l'activité** : **+37-51 %** de débit sur les dépôts à activité faible/moyenne.
- **Effet d'équipe (clé)** : quand **3 à 5 membres** adoptent l'outil, le gain **double** à **+59-87 %**. → l'adoption collective surpasse l'adoption individuelle.
- **Efficience** : **2-3 h/semaine** gagnées par développeur sur le code et la revue, soit **~10 %** des ~24 h consacrées à ces tâches → **20-30 h/semaine** réinvesties pour une équipe de 10.
- **Contexte d'usage** : **93 %** des développeurs utilisent des outils IA ; **~30 %** du code est écrit par l'IA ; **96 %** des développeurs Atlassian interrogés sont utilisateurs de Rovo Dev.
- **SDLC AI-native en 5 étapes** (agent + humain) : **Plan** (l'agent propose découpages techniques et estimations à valider) → **Orchestrate** (coordonner humains et agents) → **Code** (agents autonomes sur du travail bien cadré, PR prêtes à relire) → **Review** (l'agent revoit contre les standards d'équipe avant l'humain) → **Operate** (copilotes d'incident always-on : triage d'alertes, fixes proposés).
- **Cadre de mesure à 4 dimensions** : **Speed** = PR throughput ; **Efficiency** = heures gagnées ; **Quality** = change failure rate ; **Satisfaction** = satisfaction développeur.
- **Paradoxe de la productivité (Solow, 1987)** : « you can see the computer age everywhere but in the productivity statistics » → l'IA adoptée massivement sans mesure claire ; résolution = passer des **métriques d'usage** aux **métriques d'impact**.
- **Rôle du contexte (Teamwork Graph)** : une IA riche en contexte délivre des résultats **+44 % plus précis** en consommant **−48 % de tokens** → le contexte bat la consommation brute.
- **Méthodologie** : 3 400 dépôts / 2 500 clients ; **quasi-expérience** avec appariement par score de propension ; enquête sur **6 200+** développeurs Atlassian, estimations prises au **20e percentile** (conservatrices) ; équipes Atlassian internes = **1,35×** plus de PR mergées assistées par Rovo Dev que les clients externes.
- **Recommandation actionnable** : « Start with a team, not an individual. Pick a repo with 3–5 engineers who will actively use the product. Measure throughput and time savings 2-3 months after implementation. » → mesurer **après l'effet de nouveauté**.
- **À relier** : converge avec DORA (métriques delivery), la doctrine FinOps token→outcome (Tokenomics Foundation, Gupta), *Failing Faster* (qualité), et l'idée que l'adoption d'équipe/harness > l'outil individuel (Eight Levels, Rafal).

## RésuméDe400mots

Atlassian publie, sur son blog Inside Atlassian, une étude data co-signée par deux data scientists (Robbie Geoghegan, Fan Jiang) qui mesure le retour réel d'un **SDLC AI-native** outillé par son agent **Rovo Dev**. L'enjeu posé d'emblée est le « paradoxe de la productivité » formulé par Robert Solow en 1987 (« on voit l'ère informatique partout sauf dans les statistiques de productivité ») : l'IA est massivement adoptée — 93 % des développeurs utilisent des outils IA, près de 30 % du code est écrit par l'IA — mais son impact reste flou tant qu'on le mesure en **usage** (tokens) plutôt qu'en **impact**.

Les résultats, issus d'une quasi-expérience sur 3 400 dépôts de 2 500 clients (appariement par score de propension), sont chiffrés et segmentés. Les dépôts adoptant Rovo Dev mergent **19 % de pull requests en plus par mois** que les non-adoptants. Le gain monte à **37-51 %** sur les dépôts à activité faible ou moyenne, et **double à 59-87 %** lorsque **3 à 5 membres** de l'équipe adoptent l'outil : l'adoption collective surpasse nettement l'adoption individuelle. Côté efficience, une enquête auprès de plus de 6 200 développeurs (estimations prises au 20e percentile, donc conservatrices) établit un gain de **2-3 heures par semaine** sur les tâches de code et de revue, soit environ 10 % des 24 heures qu'elles mobilisent — c'est-à-dire 20-30 heures hebdomadaires réinvesties pour une équipe de dix.

L'article propose un **SDLC AI-native en cinq étapes** où l'agent épaule l'humain : Plan (découpages et estimations proposés), Orchestrate (coordination humains/agents), Code (agents autonomes sur du travail bien cadré, PR prêtes à relire), Review (revue contre les standards d'équipe avant l'humain) et Operate (copilotes d'incident always-on). Il l'accompagne d'un **cadre de mesure à quatre dimensions** : Speed (débit de PR), Efficiency (heures gagnées), Quality (change failure rate) et Satisfaction (satisfaction développeur) — pour ne pas réduire la valeur à la seule vélocité.

Deux points renforcent l'argument. D'abord le rôle du **contexte** : grâce au Teamwork Graph d'Atlassian, une IA riche en contexte fournit des résultats 44 % plus précis en consommant 48 % de tokens en moins. Ensuite la **recommandation opérationnelle** : commencer par une équipe (pas un individu), choisir un dépôt avec 3-5 ingénieurs réellement utilisateurs, et mesurer le débit et les gains de temps 2-3 mois après le déploiement, une fois l'effet de nouveauté dissipé. Le message de fond : la valeur de l'IA est réelle mais conditionnée à une mesure d'impact rigoureuse et à une adoption d'équipe.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Atlassian | ORGANISATION | publie | The AI-native SDLC is paying off | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Robbie Geoghegan | PERSONNE | travaille_chez | Atlassian | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Fan Jiang | PERSONNE | travaille_chez | Atlassian | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Atlassian | ORGANISATION | mesure | +19 % de PR mergées par mois pour les dépôts adoptant Rovo Dev | MESURE | 0.95 | STATIQUE | déclaré_article |
| Atlassian | ORGANISATION | mesure | 2-3 heures gagnées par développeur et par semaine | MESURE | 0.93 | STATIQUE | déclaré_article |
| Rovo Dev | TECHNOLOGIE | améliore | débit de pull requests des équipes | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| adoption par 3 à 5 membres | CONCEPT | améliore | gain de débit de PR (+59-87 %) | MESURE | 0.9 | DYNAMIQUE | déclaré_article |
| SDLC AI-native | METHODOLOGIE | fait_partie_de | partenariat humain-agent sur cinq étapes | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| SDLC AI-native | METHODOLOGIE | utilise | Rovo Dev | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Atlassian | ORGANISATION | recommande | démarrer par une équipe (3-5 ingénieurs), pas un individu, et mesurer 2-3 mois après | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Atlassian | ORGANISATION | recommande | passer des métriques d'usage (tokens) aux métriques d'impact | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| article | DOCUMENT | référence | paradoxe de la productivité de Solow (1987) | CITATION | 0.88 | ATEMPOREL | déclaré_article |
| Teamwork Graph | TECHNOLOGIE | améliore | précision de l'IA (+44 %) avec −48 % de tokens | MESURE | 0.87 | DYNAMIQUE | déclaré_article |
| cadre de mesure à 4 dimensions | METHODOLOGIE | s_applique_à | Speed, Efficiency, Quality, Satisfaction | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| équipes Atlassian internes | ORGANISATION | surpasse | clients externes (1,35× plus de PR assistées mergées) | MESURE | 0.85 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Atlassian | ORGANISATION | secteur | Éditeur logiciel (collaboration, ingénierie) | AJOUT |
| Rovo Dev | TECHNOLOGIE | catégorie | Agent de codage IA d'Atlassian | AJOUT |
| Robbie Geoghegan | PERSONNE | rôle | Senior Data Scientist, Atlassian | AJOUT |
| Fan Jiang | PERSONNE | rôle | Principal Data Scientist, Atlassian | AJOUT |
| SDLC AI-native | METHODOLOGIE | définition | Cycle de dev en 5 étapes (Plan, Orchestrate, Code, Review, Operate) où agents et humains s'associent | AJOUT |
| cadre de mesure à 4 dimensions | METHODOLOGIE | définition | Speed (PR throughput), Efficiency (heures gagnées), Quality (change failure rate), Satisfaction | AJOUT |
| Teamwork Graph | TECHNOLOGIE | rôle | Couche de contexte Atlassian améliorant précision et efficience en tokens de l'IA | AJOUT |
| paradoxe de la productivité | CONCEPT | définition | Solow (1987) : adoption massive d'une techno sans gain visible dans les statistiques de productivité | AJOUT |
| métriques d'impact | CONCEPT | rôle | Mesurer la valeur de l'IA par le résultat (throughput, heures, qualité) plutôt que l'usage (tokens) | AJOUT |
