# ssrn-persona-prompting-ai-accuracy-2025-12-07

## Veille
Étude Wharton (Generative AI Labs) : les personas experts n'améliorent pas la précision factuelle des LLM - benchmarks GPQA Diamond et MMLU-Pro - SSRN

## Titre Article
Playing Pretend: Expert Personas Don't Improve Factual Accuracy

## Date
2025-12-07

## URL
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5879722

## Keywords
prompting IA, personas, précision des LLM, benchmarking IA, GPQA Diamond, MMLU-Pro, performance IA, prompt engineering, personas experts, évaluation IA

## Authors
Savir Basil, Ina Shapiro, Dan Shapiro, Ethan Mollick, Lilach Mollick, Lennart Meincke (Generative AI Labs, The Wharton School, University of Pennsylvania)

## Ton
Profil : papier de recherche académique (working paper SSRN, Generative AI Labs de Wharton), registre scientifique et empirique, niveau technique élevé (statistiques, benchmarks).
Style : démarche expérimentale rigoureuse — protocole détaillé (25 réponses indépendantes par question et par paire modèle-prompt), intervalles de confiance à 95%, résultats rapportés par benchmark et par modèle. Ton mesuré et prudent, typique des "null results" : les auteurs réfutent une pratique répandue sans sur-généraliser et signalent leurs limites. Autorité fondée sur l'affiliation Wharton et la notoriété d'Ethan Mollick. Public cible : praticiens du prompt engineering, chercheurs, équipes IA en entreprise.

## Pense-betes
- Question testée : attribuer un persona expert à un LLM améliore-t-il sa précision sur des questions factuelles difficiles ? Réponse : non, en général
- 6 modèles testés : GPT-4o, GPT-4o-mini, o3-mini, o4-mini, Gemini 2.0 Flash, Gemini 2.5 Flash
- 2 benchmarks : GPQA Diamond (198 questions niveau doctorat) et MMLU-Pro (300 questions niveau professionnel)
- Protocole : baseline (sans persona), personas experts (physique, maths, économie, biologie, chimie, ingénierie, droit, histoire), personas "faible connaissance" (Layperson, Young Child, Toddler) ; 25 réponses indépendantes par question et par paire modèle-prompt
- Résultat principal : la plupart des conditions persona sont statistiquement indistinguables de la baseline
- Les personas faible connaissance dégradent souvent la précision ; le persona "Toddler" est nocif dans 4/6 modèles
- Exception : Gemini 2.0 Flash montre des améliorations modestes avec les 5 personas experts sur MMLU-Pro (notamment Engineering et Chemistry)
- Aligner le persona expert sur le domaine de la question n'apporte pas d'amélioration consistante
- Mode d'échec observé : les modèles Gemini Flash refusent parfois de répondre avec un persona expert hors domaine ; la sur-spécialisation conduit à sous-utiliser les connaissances réelles
- Implication pratique : privilégier des instructions spécifiques à la tâche plutôt que des personas ; les personas restent utiles pour le ton/style, pas pour la précision
- Limites : sous-ensemble de modèles, benchmarks académiques, nombre limité de personas, pas d'interaction avec d'autres techniques de prompting

## RésuméDe400mots
Cette étude du Generative AI Labs de Wharton examine si l'attribution de personas experts aux modèles d'IA améliore leurs performances sur des questions objectives difficiles à choix multiples. Les chercheurs ont testé six modèles (GPT-4o, GPT-4o-mini, o3-mini, o4-mini, Gemini 2.0 Flash, Gemini 2.5 Flash) sur deux benchmarks exigeants : GPQA Diamond (198 questions de niveau doctorat) et MMLU-Pro (300 questions de niveau professionnel).

Le protocole compare trois conditions : baseline sans persona, personas experts (expert en physique, mathématiques, économie, biologie, chimie, ingénierie, droit, histoire) et personas "faible connaissance" (Layperson, Young Child, Toddler — "un enfant de 4 ans qui croit que la lune est en fromage"). Chaque paire modèle-prompt est évaluée sur 25 réponses indépendantes par question (4 950 runs par paire sur GPQA, 7 500 sur MMLU-Pro), avec intervalles de confiance à 95%.

Les résultats sont essentiellement nuls : la plupart des conditions persona produisent des performances statistiquement indistinguables de la baseline. Sur GPQA Diamond, aucun persona expert ou faible connaissance n'améliore de façon fiable la performance ; la seule exception est un petit gain du prompt "Young Child" sur Gemini 2.5 Flash (RD = 0.098). Sur MMLU-Pro, aucun persona expert n'apporte d'amélioration statistiquement significative pour 5 des 6 modèles, et neuf différences négatives significatives sont observées. Les personas faible connaissance dégradent souvent la précision : le persona "Toddler" réduit la performance dans 4 modèles sur 6 et se révèle significativement pire que "Layperson" dans 5 modèles sur 6.

L'exception notable est Gemini 2.0 Flash, qui montre des différences positives modestes avec les cinq personas experts sur MMLU-Pro, notamment en ingénierie et en chimie. Par ailleurs, l'alignement du persona expert sur le domaine de la question n'apporte pas de bénéfice consistant. Les chercheurs identifient des modes d'échec : les modèles Gemini Flash refusent parfois de répondre lorsqu'on leur assigne un persona expert hors domaine, et des instructions de rôle trop étroites conduisent les modèles à sous-utiliser leurs connaissances réelles.

Les implications pratiques sont importantes : la pratique répandue du persona prompting est probablement inefficace pour améliorer la précision factuelle. Les organisations tireront davantage de valeur d'instructions spécifiques à la tâche, et devraient tester plusieurs variantes de prompts pour leurs problèmes concrets. Les personas peuvent toutefois conserver d'autres usages, comme moduler le ton ou le style de présentation. Les limites de l'étude (modèles et personas en nombre restreint, benchmarks académiques) ouvrent des pistes de recherche futures.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Generative AI Labs (Wharton) | ORGANISATION | publie | étude personas et précision IA | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Ethan Mollick | PERSONNE | publie | étude personas et précision IA | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Lilach Mollick | PERSONNE | publie | étude personas et précision IA | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| étude personas et précision IA | DOCUMENT | affirme_que | les personas experts n'améliorent pas la précision factuelle des LLM | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| personas faible connaissance | CONCEPT | réduit | performance des LLM | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Gemini 2.0 Flash | TECHNOLOGIE | mesure | amélioration modeste avec personas experts (MMLU-Pro) | MESURE | 0.85 | STATIQUE | déclaré_article |
| persona Toddler | CONCEPT | réduit | performance dans 4/6 modèles | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| étude personas et précision IA | DOCUMENT | utilise | 6 modèles sur GPQA Diamond et MMLU-Pro | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| étude personas et précision IA | DOCUMENT | affirme_que | la correspondance domaine-persona n'améliore pas la performance de manière consistante | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| refus de répondre avec personas hors domaine | CONCEPT | observé_dans | modèles Gemini Flash | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Generative AI Labs | ORGANISATION | affiliation | The Wharton School, University of Pennsylvania | AJOUT |
| Ethan Mollick | PERSONNE | rôle | Co-auteur, chercheur Wharton | AJOUT |
| Lilach Mollick | PERSONNE | rôle | Co-auteur, chercheur Wharton | AJOUT |
| Savir Basil | PERSONNE | rôle | Co-auteur, chercheur Wharton | AJOUT |
| GPQA Diamond | TECHNOLOGIE | catégorie | Benchmark questions PhD | AJOUT |
| MMLU-Pro | TECHNOLOGIE | catégorie | Benchmark questions professionnelles | AJOUT |
| GPT-4o | TECHNOLOGIE | catégorie | Modèle de langage (OpenAI) | AJOUT |
| Gemini 2.0 Flash | TECHNOLOGIE | catégorie | Modèle de langage (Google) | AJOUT |
| Gemini 2.5 Flash | TECHNOLOGIE | catégorie | Modèle de langage (Google) | AJOUT |
