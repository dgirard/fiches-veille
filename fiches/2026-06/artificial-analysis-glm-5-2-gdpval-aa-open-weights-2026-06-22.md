# artificial-analysis-glm-5-2-gdpval-aa-open-weights-2026-06-22

## Veille

Annonce-benchmark d'**Artificial Analysis** (plateforme d'évaluation indépendante de modèles IA, via X/Twitter + page modèle) : **GLM-5.2** de **Z.ai** (Zhipu AI, @Zai_org) devient **le meilleur modèle à poids ouverts** et se hisse **#3 au classement général** de **GDPval-AA**, un benchmark de *travail de connaissance économiquement valorisable* du monde réel (tâches longue-horizon, multi-tours, agentiques). GLM-5.2 marque **1524 Elo**, derrière les seuls **Claude Fable 5 (1783)** et **Claude Opus 4.8 (1615)**, et à parité avec **GPT-5.5 (xhigh, 1509)**. Il devance d'une large marge le modèle ouvert suivant (**MiniMax-M3, 1408**) et de nombreux modèles propriétaires : **Gemini 3.5 Flash (1357)**, **Qwen 3.7 Max (1289)**, **Muse Spark (1158)**. Les tâches sont réellement agentiques : **~31 tours par tâche** en moyenne sur **1 999 matchs**. La même hiérarchie tient sur l'**Artificial Analysis Intelligence Index** (1er open weights), l'**Agentic Index** (#3) et **AA-Briefcase** (#3, devant GPT-5.5 xhigh, derrière Fable 5). Point saillant : un modèle **open weights** sous **licence MIT**, **MoE 753 Mds de paramètres / 40 Mds actifs**, contexte **1M tokens**, tarifé **1,40 $/4,40 $ par 1M tokens** entrée/sortie, rivalise avec la frontière propriétaire sur le travail agentique — un vrai pas pour les modèles ouverts.

## Titre Article

GLM-5.2 leads open weights models and sits at #3 overall on GDPval-AA, a real-world agentic work benchmark

## Date

2026-06-22

## URL

https://artificialanalysis.ai/models/glm-5-2

## Keywords

GLM-5.2, Z.ai, Zhipu AI, modèles à poids ouverts, open weights, GDPval-AA, benchmark agentique, travail de connaissance, Elo, tâches multi-tours, longue-horizon, Artificial Analysis Intelligence Index, Agentic Index, AA-Briefcase, Mixture of Experts, licence MIT, contexte 1M tokens, raisonnement, coût par token, frontière propriétaire, Claude Fable 5, MiniMax-M3

## Authors

Artificial Analysis (@ArtificialAnlys)

## Ton

Profil : annonce-benchmark factuelle et chiffrée, perspective d'un **évaluateur tiers indépendant** (Artificial Analysis), diffusée sous forme de fil X/Twitter adossé à une page modèle détaillée, registre data-driven et neutre en anglais, niveau technique élevé, public cible ingénieurs ML, décideurs techniques, acheteurs d'API et observateurs du marché des modèles de fondation. Le ton est celui du **comparatif de performance objectivé** : des classements (Elo, index), des nombres précis (1524, ~31 tours, 1 999 matchs, 1,40 $/4,40 $) et une méthode explicite (mêmes briefs donnés à plusieurs modèles, livrables rendus tels quels). L'autorité tient à la **réputation de neutralité** d'Artificial Analysis et à la transparence méthodologique (rendu des livrables produits, multiplicité des index croisés). La rhétorique, sans emphase commerciale, laisse les chiffres porter la thèse implicite : l'écart entre modèles **ouverts** et **propriétaires** se referme sur le terrain le plus exigeant — le travail agentique économiquement utile. Métaphore implicite : le benchmark comme « épreuve professionnelle » (tâches d'un superviseur de magasin, etc.) plutôt que test académique abstrait. Le seul jugement de valeur explicite — *« a real step for open models »* — est mesuré et adossé au rapport prix/performance.

## Pense-betes

- **Fait central** : **GLM-5.2** (Z.ai / Zhipu AI) = **#1 des modèles à poids ouverts** et **#3 au général** sur **GDPval-AA** avec **1524 Elo**.
- **Podium GDPval-AA** : 1. **Claude Fable 5 (1783)** ; 2. **Claude Opus 4.8 (1615)** ; 3. **GLM-5.2 (1524)** — à parité avec **GPT-5.5 (xhigh, 1509)**.
- **Domination open weights** : le modèle ouvert suivant, **MiniMax-M3**, n'est qu'à **1408** (large marge).
- **Devance des modèles propriétaires** : **Gemini 3.5 Flash (1357)**, **Qwen 3.7 Max (1289)**, **Muse Spark (1158)**.
- **GDPval-AA = quoi** : performance sur du **travail de connaissance réel et économiquement valorisable**, via des tâches **longue-horizon, multi-tours** ; couvre du travail professionnel ET créatif (ex. liste de tâches quotidienne d'un superviseur de magasin retail, document IEC…). Méthode : mêmes briefs donnés à GLM-5.2 + 3 modèles frontière propriétaires (Fable 5, GPT-5.5, Gemini 3.5 Flash), **livrables rendus exactement tels que produits**.
- **Vraiment agentique** : GLM-5.2 a moyenné **~31 tours par tâche** sur **1 999 matchs**.
- **Cohérence multi-index** : 1er open weights sur l'**Artificial Analysis Intelligence Index**, **#3 sur l'Agentic Index**, **#3 sur AA-Briefcase** (sur AA-Briefcase : top open weights, devant GPT-5.5 xhigh, derrière seulement Fable 5).
- **Specs (page modèle)** : **MoE 753 Mds params / 40 Mds actifs**, **modèle de raisonnement** (extended thinking), contexte **1M tokens**, **texte→texte**, **licence MIT** (usage commercial), poids sur Hugging Face, **sorti le 16 juin 2026**.
- **Économie** : **1,40 $ / 4,40 $** par 1M tokens (entrée/sortie), **cache hit 0,26 $** (-81 %), taux mélangé **~0,90 $/1M** ; débit **106,3 tokens/s**, TTFT **1,36 s** ; coût total de l'éval **982,90 $**. → Argument prix/perf : la frontière agentique à tarif open weights.
- **Thèse implicite** : la convergence ouvert/propriétaire se joue désormais sur le **travail agentique utile**, pas seulement sur les benchmarks académiques.
- **À relier** : prolonge la course aux modèles frontière (Opus 4.8, Fable 5) ; signal marché « open weights chinois » (cf. fiches Qwen / MiniMax) ; pertinent pour le débat **coût des agents** et la souveraineté/self-hosting.

## RésuméDe400mots

Artificial Analysis — plateforme d'évaluation indépendante de modèles d'IA — publie (fil X/Twitter du 22 juin 2026 + page modèle détaillée) un comparatif plaçant **GLM-5.2**, le dernier modèle de **Z.ai** (Zhipu AI), au sommet des modèles à **poids ouverts** et **#3 au classement général** de **GDPval-AA**. Ce benchmark mesure la performance sur du **travail de connaissance réel et économiquement valorisable**, à travers des tâches **longue-horizon et multi-tours**, conçues comme de véritables épreuves professionnelles (par exemple la liste de tâches quotidienne d'un superviseur de magasin, ou un document technique IEC) couvrant du travail professionnel comme créatif.

GLM-5.2 obtient **1524 Elo**, derrière les seuls **Claude Fable 5 (1783)** et **Claude Opus 4.8 (1615)**, et à parité avec **GPT-5.5 en réglage xhigh (1509)**. Surtout, il domine le camp ouvert d'une **large marge** : le meilleur modèle ouvert suivant, **MiniMax-M3**, ne marque que **1408**. GLM-5.2 devance aussi plusieurs modèles propriétaires — **Gemini 3.5 Flash (1357)**, **Qwen 3.7 Max (1289)** et **Muse Spark (1158)**.

La nature **agentique** des tâches est soulignée : GLM-5.2 a moyenné **~31 tours par tâche** sur **1 999 matchs**. La méthode d'Artificial Analysis consiste à donner les **mêmes briefs** à GLM-5.2 et à trois modèles frontière propriétaires (Fable 5, GPT-5.5, Gemini 3.5 Flash), puis à **rendre chaque livrable exactement tel que produit**. Le résultat est cohérent sur l'ensemble des index maison : GLM-5.2 est **1er des open weights** sur l'**Intelligence Index**, **#3 sur l'Agentic Index** et **#3 sur AA-Briefcase** (où il est le meilleur modèle ouvert, devant GPT-5.5 xhigh et derrière seulement Fable 5).

La page modèle complète le tableau : GLM-5.2 est un **Mixture of Experts** de **753 milliards de paramètres** (dont **40 milliards actifs**), un **modèle de raisonnement** à contexte **1M tokens**, distribué sous **licence MIT** (usage commercial, poids sur Hugging Face), sorti le **16 juin 2026**. Côté économie : **1,40 $ / 4,40 $** par million de tokens (entrée/sortie), un cache hit à **0,26 $** (-81 %), un débit de **106,3 tokens/s** et un temps au premier token de **1,36 s**.

Le message porté par les chiffres est clair : qu'un modèle **open weights** à ce tarif rivalise avec la frontière propriétaire sur du **travail agentique réellement utile** constitue, selon Artificial Analysis, *« a real step for open models »*. La convergence ouvert/propriétaire ne se joue plus seulement sur les tests académiques, mais sur la valeur économique produite en conditions agentiques.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Z AI | ORGANISATION | a_créé | GLM-5.2 | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| GLM-5.2 | TECHNOLOGIE | mesure | 1524 Elo sur GDPval-AA (#3 au général, #1 open weights) | MESURE | 0.95 | DYNAMIQUE | déclaré_article |
| Claude Fable 5 | TECHNOLOGIE | surpasse | GLM-5.2 | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Opus 4.8 | TECHNOLOGIE | surpasse | GLM-5.2 | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| GLM-5.2 | TECHNOLOGIE | surpasse | MiniMax-M3 | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| GLM-5.2 | TECHNOLOGIE | surpasse | Gemini 3.5 Flash | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| GLM-5.2 | TECHNOLOGIE | concurrence | GPT-5.5 | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| GLM-5.2 | TECHNOLOGIE | mesure | ~31 tours par tâche sur 1 999 matchs | MESURE | 0.85 | DYNAMIQUE | déclaré_article |
| GDPval-AA | DOCUMENT | mesure | travail de connaissance économiquement valorisable en tâches multi-tours longue-horizon | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Artificial Analysis | ORGANISATION | publie | GDPval-AA | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| GLM-5.2 | TECHNOLOGIE | est_instance_de | modèle à poids ouverts | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| GLM-5.2 | TECHNOLOGIE | utilise | architecture Mixture of Experts (753 Mds params / 40 Mds actifs) | CONCEPT | 0.9 | STATIQUE | déclaré_article |
| GLM-5.2 | TECHNOLOGIE | mesure | tarif 1,40 $ / 4,40 $ par 1M tokens (entrée/sortie) | MESURE | 0.9 | DYNAMIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | affirme_que | qu'un modèle open weights rivalise avec la frontière propriétaire sur le travail agentique est un vrai progrès | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| GLM-5.2 | TECHNOLOGIE | catégorie | LLM à poids ouverts, MoE 753 Mds/40 Mds actifs, raisonnement, contexte 1M, MIT, sorti 2026-06-16 | AJOUT |
| Z AI | ORGANISATION | secteur | Labo IA (Zhipu AI, Chine), créateur de la famille GLM | AJOUT |
| Artificial Analysis | ORGANISATION | rôle | Plateforme d'évaluation indépendante de modèles IA (index Intelligence/Agentic, GDPval-AA, AA-Briefcase) | AJOUT |
| GDPval-AA | DOCUMENT | rôle | Benchmark de travail de connaissance réel/agentique (Elo, multi-tours, livrables rendus) | AJOUT |
| AA-Briefcase | DOCUMENT | rôle | Éval agentique de travail de connaissance d'Artificial Analysis (GLM-5.2 #3, top open weights) | AJOUT |
| Claude Fable 5 | TECHNOLOGIE | rôle | #1 GDPval-AA (1783 Elo) | AJOUT |
| Claude Opus 4.8 | TECHNOLOGIE | rôle | #2 GDPval-AA (1615 Elo) | AJOUT |
| MiniMax-M3 | TECHNOLOGIE | rôle | 2e meilleur modèle open weights sur GDPval-AA (1408 Elo) | AJOUT |
