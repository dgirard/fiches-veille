# denisov-blanch-stanford-quantify-ai-roi-software-engineering-2025-11-23
## Veille
Stanford Research - AI ROI Measurement - Developer Productivity - Metrics Framework - AI Adoption Gap

## Titre Article
How to Quantify AI ROI in Software Engineering (Stanford Study / 120k Devs)

## Date
2025-11-23

## URL
https://www.youtube.com/live/cMSprbJ95jg?si=4HnxK8w1ELvSr4tz&t=9705

## Keywords
Stanford, AI ROI, Developer Productivity, Metrics, Code Quality, Tech Debt, AI Adoption, Engineering Output, Rework

## Authors
Yegor Denisov-Blanch (Researcher, Stanford)

## Ton
**Profil:** Académique-Recherche | Data-Driven | Analytique | Objectif

Le ton est celui de la recherche universitaire rigoureuse appliquée à l'industrie. L'approche est basée sur des preuves quantitatives (études longitudinales et transversales sur 120k développeurs). Le discours vise à démystifier la "hype" par des données probantes, proposant des frameworks de mesure sophistiqués (modèles ML pour évaluer l'output, indices de propreté du code). C'est un appel à la rigueur métrique pour les leaders techniques.

## Pense-betes
- **Écart grandissant ("Widening Gap")** : Les équipes performantes avec l'IA s'améliorent encore plus ("rich gets richer"), tandis que les équipes en difficulté prennent du retard. Il est crucial de savoir dans quelle cohorte on se trouve.
- **Qualité de l'usage > Quantité** : La corrélation entre le nombre de tokens utilisés et la productivité est faible. Ce qui compte, c'est *comment* l'IA est utilisée (patterns d'ingénierie).
- **Hygiène du code (Cleanliness Index)** : Un code propre, modulaire et testé amplifie les gains de l'IA. À l'inverse, l'IA utilisée sur un code sale accélère l'entropie et la dette technique.
- **Mesure du ROI** :
    - Ne pas se fier aux résultats commerciaux (trop de bruit/facteurs confondants).
    - Ne pas se fier aux métriques simplistes (lignes de code, nombre de PR). L'augmentation des PR peut masquer une baisse de qualité et une augmentation du "rework" (retravail).
- **Framework de métriques proposé** :
    - **Métrique primaire** : Engineering Output (évalué par un modèle ML simulant un panel d'experts, pas juste du volume).
    - **Métriques "Guardrails"** : Qualité, Rework/Refactoring, Santé de l'équipe (DevOps metrics). Il faut maximiser l'output tout en maintenant les guardrails sains.
- **Étude de cas (Avertissement)** : Une entreprise a vu +14% de PRs avec l'IA, mais une baisse de 9% de la qualité et une explosion (x2.5) du travail de reprise (rework). Sans mesure fine, cela ressemblait à un succès alors que le ROI était probablement négatif.

## RésuméDe400mots
Yegor Denisov-Blanch, chercheur à Stanford, présente les résultats d'une étude massive sur l'impact de l'IA sur la productivité de plus de 100 000 développeurs. L'objectif est de dépasser la "hype" pour quantifier le retour sur investissement (ROI) réel.

L'étude révèle une **fracture grandissante** : l'écart de performance entre les équipes qui réussissent avec l'IA et celles qui échouent se creuse. Contrairement aux idées reçues, la quantité d'IA utilisée (nombre de tokens) corrèle peu avec la productivité. Le facteur déterminant est la **qualité de l'environnement de code** ("Codebase Hygiene"). Un code propre, bien testé et documenté permet à l'IA d'être performante. À l'inverse, sur une base de code dégradée, l'IA risque d'accélérer l'entropie et la dette technique, demandant plus d'efforts humains pour corriger les erreurs.

Denisov-Blanch met en garde contre les métriques simplistes comme le nombre de Pull Requests (PR). Il cite l'exemple d'une entreprise ayant observé une hausse de 14% des PR, interprétée initialement comme un succès. Une analyse plus fine a révélé une baisse de 9% de la qualité du code et une multiplication par 2,5 du "rework" (retravail sur du code récent). Le gain de volume était annulé par la baisse de qualité, rendant le ROI potentiellement négatif.

Pour mesurer correctement le ROI, Stanford propose un framework :
1.  **Mesurer l'Usage** : Distinguer l'accès théorique de l'usage réel (via télémétrie fine) et identifier les "patterns" d'utilisation (usage personnel vs orchestration agentique).
2.  **Mesurer les "Engineering Outcomes"** : Utiliser une métrique primaire d'**"Engineering Output"** (basée sur un modèle ML entraîné pour reproduire l'évaluation d'experts humains, et non sur le volume de lignes) couplée à des **métriques "Guardrails"** (qualité, taux de reprise, santé de l'équipe) qu'il faut maintenir à un niveau sain.

La conclusion est que l'IA est un amplificateur : elle accélère les bonnes pratiques comme les mauvaises. Les leaders doivent mesurer précisément l'impact pour corriger le tir et investir dans l'hygiène du code pour débloquer le potentiel de l'IA.
