# pragmatic-engineer-measure-ai-impact-dev-2025-09-16

## Veille
Pragmatic Engineer - Mesurer l'impact de l'IA - Productivité développeur - Métriques - GitHub Copilot - DX - Efficacité d'ingénierie

## Titre Article
HOW TECH COMPANIES MEASURE THE IMPACT OF AI ON SOFTWARE DEVELOPMENT

## Date
2025-09-16

## URL
https://newsletter.pragmaticengineer.com/p/how-tech-companies-measure-the-impact-of-ai?utm_source=tldrnewsletter

## Keywords
AI impact, software development, engineering efficiency, developer productivity, AI tools, metrics, GitHub Copilot, Google, Microsoft, Dropbox, Monzo, Atlassian, DX, AI Measurement Framework, Change Failure Rate, PR throughput, developer experience, CSAT, time savings

## Authors
Gergely Orosz and Laura Tacho

## Ton
**Profil:** Professionnel-Analytique | Co-auteurs expert | Éducative-Prescriptive | Intermédiaire-Expert

Orosz et Tacho adoptent une voix d'experts collaborative combinant reportage et construction de cadre méthodologique. Les données issues de 18 entreprises (Google, GitHub, Microsoft, Dropbox) ancrent empiriquement les recommandations. La structure systématique mêlant métriques core et métriques spécifiques IA révèle une pensée en framework. Les études de cas concrètes (90 % d'adoption chez Dropbox, BDD chez Microsoft, défis de Monzo) illustrent les principes abstraits. Le langage prescriptif fournit des conseils actionnables. Les avertissements explicites (risques qualité, dette de maintenabilité, limites du taux d'acceptation) témoignent d'honnêteté intellectuelle. L'article vise les leaders d'ingénierie avec un mélange de réflexion stratégique et d'implémentation tactique. Typique des analyses approfondies du Pragmatic Engineer combinant recherche sectorielle et recommandations pratiques.

## Pense-betes
- **18 grandes entreprises tech** étudiées (Google, GitHub, Microsoft, Dropbox, Monzo, Atlassian...)
- **85 % des ingénieurs utilisent des outils IA**, mais manque de métriques claires pour justifier l'investissement
- **Métriques core + spécifiques IA** : combiner l'existant (CFR, débit de PR, temps de cycle PR, expérience développeur) avec les nouvelles (taux d'adoption, CSAT, temps gagné, dépense IA)
- **Résultats Dropbox** : **90 % d'adoption IA**, les ingénieurs fusionnent **20 % de PR en plus** avec un CFR réduit
- **Segmenter les données** : utilisateurs IA vs non-IA, avant/après IA, par rôle/ancienneté/langage
- **Équilibrer vitesse et qualité** : suivre des métriques qui se contrôlent mutuellement (débit de PR + CFR)
- **Expérience développeur prioritaire** : mesurer satisfaction et expérience, crucial pour une adoption durable
- **Collecte de données à 3 couches** : données système + enquêtes périodiques + échantillonnage d'expérience
- **État d'esprit expérimental** : aborder la mesure avec un objectif clair, tester des prédictions
- **« Bad developer days » (BDD)** : métrique Microsoft évaluant l'impact de l'IA sur la pénibilité quotidienne
- **Déclin du taux d'acceptation** : plus une métrique de référence, ne capture ni maintenabilité ni bugs
- **Télémétrie d'agents** : domaine émergent appelé à évoluer significativement
- **Cas Monzo** : mesure objective difficile (rétention des données par les fournisseurs), le ressenti subjectif + des cas d'usage précis (migrations de code) démontrent une valeur claire

## RésuméDe400mots

Cette analyse approfondie explore comment **18 grandes entreprises tech**, dont Google, GitHub, Microsoft et Dropbox, mesurent l'impact de l'IA sur le développement logiciel, face au défi de justifier des investissements croissants dans les outils de codage IA. Rédigé par Gergely Orosz et Laura Tacho (CTO de DX), l'article souligne que si **85 % des ingénieurs utilisent des outils IA**, beaucoup de leaders d'ingénierie peinent à en évaluer la valeur réelle, faute de métriques claires au-delà de mesures superficielles comme les lignes de code (LOC).

**Message central : combiner les métriques**

Une mesure efficace de l'impact de l'IA exige de **combiner les métriques d'ingénierie « core » existantes et de nouvelles métriques spécifiques à l'IA**. Les entreprises ne doivent pas abandonner les métriques traditionnelles comme le Change Failure Rate, le débit de PR, le temps de cycle des PR et l'expérience développeur, car l'objectif ultime de l'IA est précisément d'améliorer ces fondamentaux de la livraison logicielle. Ces métriques core doivent être suivies conjointement avec les taux d'adoption IA, la satisfaction (CSAT) vis-à-vis des outils, le temps gagné par ingénieur et la dépense IA. **Dropbox**, par exemple, a atteint **90 % d'adoption IA** et vu ses ingénieurs fusionner **20 % de pull requests en plus** avec un taux d'échec de changement réduit.

**Segmentation et état d'esprit expérimental**

Un aspect crucial est la **ventilation des métriques par niveau d'usage de l'IA** : comparer utilisateurs IA et non-IA, et analyser les tendances dans le temps. Ce découpage par rôle, ancienneté ou langage de programmation aide à identifier les groupes qui bénéficient le plus de l'IA ou nécessitent une formation supplémentaire. L'article insiste sur l'**état d'esprit expérimental**, où les données servent à répondre à des questions précises et à tester des prédictions sur l'influence de l'IA.

**Qualité, maintenabilité, expérience développeur**

La vigilance sur la **qualité du code, la maintenabilité et l'expérience développeur** est primordiale. Les auteurs avertissent que le développement assisté par IA peut créer « le plus gros tas de dette technique » s'il n'est pas géré avec soin. Il est essentiel de suivre des métriques qui se contrôlent mutuellement, comme la vitesse avec la qualité (débit de PR et CFR). Au-delà des métriques système, les données auto-déclarées sur la « confiance dans les changements », la « maintenabilité du code » et la « perception de la qualité » sont vitales pour capturer les impacts de long terme. L'expérience développeur, souvent réduite à tort à des avantages superficiels, est critique pour réduire la friction sur tout le cycle de développement.

**Tendances émergentes et défis**

Microsoft utilise les **« bad developer days » (BDD)** pour évaluer l'impact de l'IA sur la pénibilité quotidienne, tandis que Glassdoor mesure les résultats d'expérimentation (tests A/B). Le **taux d'acceptation** des suggestions IA, autrefois métrique de référence, décline car trop étroit : il ne capture ni la maintenabilité, ni l'introduction de bugs, ni la productivité globale. L'analyse des coûts, encore peu pratiquée pour ne pas décourager l'usage, devrait être davantage scrutée à mesure que les budgets IA croissent. La **télémétrie d'agents** et la mesure au-delà de l'écriture de code sont identifiées comme des domaines appelés à évoluer fortement.

**AI Measurement Framework et couches de données**

L'article introduit l'**AI Measurement Framework**, ensemble recommandé de métriques mêlant métriques IA et métriques d'ingénierie core, avec l'expérience développeur au centre. Il préconise une collecte de données en couches : données système quantitatives (outils IA, GitHub, JIRA, CI/CD), enquêtes périodiques qualitatives et échantillonnage d'expérience sur le moment. L'expérience de **Monzo Bank** sert d'étude de cas : la mesure objective est difficile (rétention des données par les fournisseurs), mais le ressenti subjectif des ingénieurs et des cas d'usage précis comme les migrations de code démontrent une valeur claire.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Gergely Orosz | PERSONNE | publie | AI Measurement Framework | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Laura Tacho | PERSONNE | publie | AI Measurement Framework | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Laura Tacho | PERSONNE | travaille_chez | DX | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| DX | ORGANISATION | permet | mesure de l'efficacité ingénierie en entreprise | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| AI Measurement Framework | METHODOLOGIE | recommande | combiner métriques d'ingénierie core et métriques spécifiques IA | AFFIRMATION | 0.96 | STATIQUE | déclaré_article |
| Dropbox | ORGANISATION | mesure | 90% taux d'adoption IA | MESURE | 0.98 | STATIQUE | déclaré_article |
| Dropbox | ORGANISATION | mesure | augmentation 20% des PRs fusionnées | MESURE | 0.95 | STATIQUE | déclaré_article |
| Microsoft | ORGANISATION | utilise | Bad Developer Days | METHODOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| difficultés de mesure objective de l'IA | CONCEPT | observé_dans | Monzo Bank | ORGANISATION | 0.93 | DYNAMIQUE | déclaré_article |
| acceptance rate | CONCEPT | s_oppose_à | mesure pertinente de productivité IA | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| LeadDev | ORGANISATION | publie | AI Impact Report 2025 | DOCUMENT | 0.96 | STATIQUE | déclaré_article |
| METR study | DOCUMENT | s_oppose_à | perception de gain de vitesse IA | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| LOC | CONCEPT | s_oppose_à | mesure pertinente productivité | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Gergely Orosz | PERSONNE | prédit | une évolution significative de la télémétrie d'agents | AFFIRMATION | 0.82 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Gergely Orosz | PERSONNE | rôle | Auteur newsletter The Pragmatic Engineer | AJOUT |
| Laura Tacho | PERSONNE | rôle | CTO chez DX, co-auteure AI Measurement Framework | AJOUT |
| DX | ORGANISATION | secteur | Mesure productivité ingénierie et expérience développeur | AJOUT |
| AI Measurement Framework | METHODOLOGIE | origine | DX, basé sur données 400+ entreprises | AJOUT |
| Dropbox | ORGANISATION | résultat | 90% adoption IA, +20% PRs fusionnés | AJOUT |
| Microsoft | ORGANISATION | métrique distinctive | Bad Developer Days (BDDs) | AJOUT |
| Monzo Bank | ORGANISATION | défi | Opacité des données vendeurs d'outils IA | AJOUT |
| Change Failure Rate | METHODOLOGIE | catégorie | Métrique core ingénierie logicielle | AJOUT |
| acceptance rate | CONCEPT | statut | Métrique en déclin, portée trop étroite | AJOUT |
| LOC | CONCEPT | évaluation | Mauvaise mesure de productivité développeur | AJOUT |
| agent telemetry | CONCEPT | statut | Domaine émergent de mesure IA | AJOUT |
