# numind-nuextract-foundation-model-structured-extraction-2024-06-24

## Veille
NuExtract NuMind - modèle fondation extraction structurée JSON petit format

## Titre Article
NuExtract: A Foundation Model for Structured Extraction

## Date
2024-06-24

## URL
https://numind.ai/blog/nuextract-a-foundation-model-for-structured-extraction

## Keywords
extraction structurée, JSON, modèle de langage, NLP, fine-tuning, LLM compact, open source, MIT, zéro-shot

## Authors
Alexandre Constantin, Liam Cripwell, Etienne Bernard

## Ton
Profil : Article technique de blog d'entreprise, registre scientifique vulgarisé, perspective recherche appliquée.
Style : Ton enthousiaste mais rigoureux, appuyé sur des métriques comparatives précises. Utilise des comparaisons chiffrées percutantes (100x plus petit, 35x plus efficace) pour démontrer la proposition de valeur. Autorité construite sur la méthodologie et les benchmarks. Public cible : praticiens ML, développeurs NLP, décideurs techniques évaluant des solutions d'extraction.

## Pense-betes
- Modèles de 0.5B à 7B paramètres rivalisant avec des LLM 100x plus grands
- NuExtract-tiny surpasse GPT-3.5 tout en étant 100x plus petit
- NuExtract-large atteint l'équivalence GPT-4o avec 100x moins de paramètres
- Dataset d'entraînement : 50 000 exemples générés à partir de C4 avec Llama 3 70B
- Profondeur d'arbre d'extraction jusqu'à 9 niveaux hiérarchiques
- Licence MIT - open source
- Fonctionne en zéro-shot ou avec fine-tuning spécialisé
- Cas d'usage : dossiers médicaux, documents juridiques, rapports financiers
- Avantages : coûts d'inférence réduits, déploiement local/privé possible

## RésuméDe400mots
NuMind présente NuExtract, un modèle de langage spécialisé dans la conversion de texte en données JSON structurées. L'innovation majeure réside dans la création de modèles compacts (de 0.5 milliard à 7 milliards de paramètres) qui égalent ou surpassent les performances de LLM génériques cent fois plus volumineux.

Le modèle excelle dans l'extraction d'informations complexes à partir de documents variés, organisant les données de manière hiérarchique. Les cas d'usage typiques incluent l'analyse de dossiers médicaux, de documents juridiques et de rapports financiers. NuExtract peut fonctionner en mode zéro-shot pour des tâches générales ou être affiné pour des problématiques métier spécifiques.

La méthodologie de création du dataset constitue un élément clé du succès. L'équipe a exploité 300 000 textes anglais issus du dataset C4, utilisant Llama 3 70B pour générer les templates d'extraction et les annotations. Ce processus a produit 50 000 exemples d'entraînement de qualité, avec des arbres d'extraction pouvant atteindre 9 niveaux de profondeur hiérarchique.

Les résultats de performance démontrent l'efficacité de l'approche. NuExtract-tiny surpasse GPT-3.5 malgré une taille 100 fois inférieure. La version standard NuExtract dépasse Llama3-70B tout en étant 35 fois plus compacte. NuExtract-large atteint l'équivalence avec GPT-4o pour une réduction de taille d'un facteur 100.

Ces performances ouvrent des avantages pratiques considérables par rapport aux alternatives propriétaires. Les coûts d'inférence sont drastiquement réduits grâce à la taille compacte des modèles. Le déploiement local ou privé devient réalisable, répondant aux exigences de confidentialité de nombreuses organisations. La capacité de fine-tuning permet d'adapter facilement le modèle à des domaines spécifiques sans expertise ML approfondie.

Le modèle est distribué sous licence MIT, permettant une utilisation libre dans des contextes commerciaux et de recherche. Cette approche open source positionne NuExtract comme une alternative crédible aux API d'extraction propriétaires, particulièrement pour les organisations soucieuses de maîtriser leurs coûts et leurs données.

L'article illustre une tendance importante : les modèles spécialisés de taille modeste peuvent rivaliser avec les géants généralistes sur des tâches ciblées, ouvrant la voie à des déploiements plus économiques et souverains.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| NuMind | ORGANISATION | a_créé | NuExtract | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| NuExtract | TECHNOLOGIE | effectue | extraction structurée JSON | CONCEPT | 0.97 | DYNAMIQUE | déclaré_article |
| NuExtract-tiny | TECHNOLOGIE | surpasse | GPT-3.5 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| NuExtract-large | TECHNOLOGIE | atteint_équivalence | GPT-4o | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| NuExtract | TECHNOLOGIE | est_basé_sur | Llama 3 70B | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| NuExtract | TECHNOLOGIE | utilise | dataset C4 | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| NuExtract | TECHNOLOGIE | distribué_sous | licence MIT | CONCEPT | 0.98 | STATIQUE | déclaré_article |
| Alexandre Constantin | PERSONNE | a_créé | NuExtract | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Liam Cripwell | PERSONNE | a_créé | NuExtract | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Etienne Bernard | PERSONNE | a_créé | NuExtract | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| NuExtract | TECHNOLOGIE | réduit | coûts d'inférence | CONCEPT | 0.90 | ATEMPOREL | inféré |
| modèles spécialisés compacts | CONCEPT | rivalise_avec | LLM généralistes | CONCEPT | 0.88 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| NuMind | ORGANISATION | secteur | NLP / extraction structurée | AJOUT |
| NuExtract | TECHNOLOGIE | catégorie | modèle de langage spécialisé extraction JSON | AJOUT |
| NuExtract | TECHNOLOGIE | taille | 0.5B à 7B paramètres | AJOUT |
| NuExtract-tiny | TECHNOLOGIE | catégorie | version compacte NuExtract | AJOUT |
| NuExtract-large | TECHNOLOGIE | catégorie | version large NuExtract | AJOUT |
| GPT-3.5 | TECHNOLOGIE | catégorie | LLM généraliste | AJOUT |
| GPT-4o | TECHNOLOGIE | catégorie | LLM généraliste | AJOUT |
| Llama 3 70B | TECHNOLOGIE | rôle | génération dataset entraînement | AJOUT |
| Alexandre Constantin | PERSONNE | rôle | auteur NuExtract | AJOUT |
| Liam Cripwell | PERSONNE | rôle | auteur NuExtract | AJOUT |
| Etienne Bernard | PERSONNE | rôle | auteur NuExtract | AJOUT |
