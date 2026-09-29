---
themes: [architecture-construction, outils-plateformes]
source: "GPT Researcher Docs"
---
# elovic-gpt-researcher-context-filter-jev-2026-09-26

## Veille

Page de documentation technique de **GPT Researcher**, *« Context Filter »*, réécrite le **26 septembre 2026** par **Assaf Elovic**, créateur du projet, le jour où il a fait de **Jev** (modèle de **TypeSafe**) le filtre de contexte par défaut. Environ **2 200 mots**, dont un benchmark reproductible. **(A)** La thèse de conception : le filtre de contexte est *« le plus gros levier sur la qualité du rapport après la recherche elle-même »* : *« ce qu'il écarte, le rédacteur ne le voit jamais »*. **(B)** Le mécanisme : chaque page scrapée est découpée en blocs de **1 000 caractères**. Jev note chaque bloc sur une grille d'utilité à quatre niveaux (0 à 3), et seuls les blocs à **≥ 1,5** sont gardés, dix au plus. Sans clé API, un repli **BM25** local avec seuil relatif prend le relais. **(C)** Le benchmark : 28 tâches rejouées sur les mêmes pages. **73 %** de passages pertinents pour Jev contre **46 %** pour les embeddings, **15-10-3** en duel, au même coût (~0,115 $ par rapport). **(D)** Le résultat le plus transposable : *« le seuil compte plus que le classement »*. Sans seuil, Jev retombe à 50 %. Le gain vient de moins de bruit, pas de plus de contenu. Prolonge, côté recherche web, la comparaison des stratégies de récupération de [[comparethemarket-context-retrieval-ai-code-review-gkg-rag-2026-03-06]].

## Titre Article

Context Filter

## Date

2026-09-26

## URL

https://docs.gptr.dev/docs/gpt-researcher/gptr/context-filter

## Keywords

filtre de contexte, context filter, sélection de passages, GPT Researcher, Jev, TypeSafe, System One, score d'utilité, probabilités calibrées, seuil de sélection, BM25, recherche lexicale, embeddings, similarité cosinus, découpage en blocs, chunking, repli, fallback, benchmark rejoué, précision, comparaison par paires, LLM juge, SimpleQA, deep research, coût par rapport, bruit contextuel, context engineering

## Authors

Assaf Elovic, créateur de GPT Researcher, auteur de la page (documentation officielle docs.gptr.dev, non signée).

## Ton

**Profil** : documentation de référence d'un projet open source, rédigée par son mainteneur principal le jour même du changement de comportement par défaut. La page sert à la fois de manuel (modes, variables d'environnement, chaîne de repli) et de justification de ce choix par la mesure.

**Style** : sobre, dense, orienté ingénieur. Schéma ASCII du pipeline, requête HTTP complète, tableaux de résultats, paramètres chiffrés (k1 = 1,5, b = 0,75, 64 appels concurrents). Les formules sont courtes et démonstratives (*« a calibrated usefulness score can say 'nothing else on this page is worth including'; a similarity score can't »*).

**Position épistémique** : plus prudente que la moyenne des pages produit. Protocole publié, scripts et métriques committés, test de signe donné (p ≈ 0,008 pour Jev, p ≈ 0,12 pour le repli BM25, qualifié de *« directionnel »*). Une section de réserves précède la reproduction : 28 tâches, un seul modèle rédacteur, un seul type de rapport, rédaction et jugement par la même famille (gpt-5.4). Le choix par défaut profite à un fournisseur tiers (TypeSafe), et la page ne dit rien de la relation entre les deux projets. Le repli gratuit est toutefois documenté et mesuré comme au moins équivalent aux embeddings.

## Pense-betes

- **Où se place le filtre.** Requête → sous-requêtes → pour chacune : recherche, scraping, **filtre**, passages. Les passages de toutes les sous-requêtes sont joints puis envoyés au rédacteur. Page plafonnée à **50 000 caractères**, découpée en blocs de **1 000 caractères** avec 100 de recouvrement. Le chat sur un rapport terminé passe par la même fonction `select_context()`, le rapport étant traité comme une seule page.
- **Cinq modes** (`CONTEXT_FILTER`) : `auto` (Jev si clé, sinon keyword), `jev`, `keyword` (BM25), `embeddings`, `none`. Toute défaillance de Jev (clé absente, réseau, 429/529 après trois essais, réponse mal formée) retombe sur keyword. Aucun réglage ne laisse un run sans contexte. Sous **8 000 caractères** au total, tout passe sans filtre.
- **Jev, un « System One model »** : il ne génère pas de texte, il répond à des questions typées avec des probabilités calibrées. Grille en quatre niveaux : sans rapport / même sujet mais inutile / répond partiellement / répond directement. Le score est la moyenne pondérée (0 à 3). Seuil `JEV_MIN_SCORE` = 1,5. Coût : **0,042 $ par million de tokens d'entrée**, sortie gratuite, soit ~0,5 centime par rapport.
- ⭐ **Le seuil fait le gain, pas le modèle.** Jev forcé à remplir 10 places sans seuil : 73 % → **50 %**, à peine mieux que les embeddings. BM25 en top-10 brut : 40 %, perd contre les embeddings ; le même BM25 avec seuil relatif (≥ 50 % du meilleur bloc) : 51 %, les bat. Une mesure qui sait dire « rien d'autre ne mérite d'entrer » vaut mieux qu'un classement qui remplit toujours le budget.
- **Moins de bruit, pas plus de contenu.** Jev envoie **4,5 k tokens** contre 7,6 k pour les embeddings, pour une quantité de texte pertinent quasi identique (~3,3 k contre 3,5 k). La différence porte sur ce que le rédacteur doit ignorer. Rejoint le diagnostic du *context rot*, vu du côté de l’entrée.
- **Ne pas filtrer du tout** gagne sur les questions ouvertes (8-0 contre les embeddings), mais coûte **+65 %** par rapport (+83 % en ouvert) et envoie jusqu'à 108 k tokens. Sur les questions factuelles, aucun gain. L'écart grandit en *deep research*, qui multiplie les sous-requêtes.
- **Protocole réutilisable** : enregistrer les pages réellement vues par le filtre, les rejouer avec chaque filtre, rédacteur constant, puis juger sous trois angles (précision des passages, duel à l'aveugle dans les deux ordres, exactitude SimpleQA). Recherche et scraping, les étapes les plus bruitées, sont neutralisés.
- **SimpleQA est saturé** : 18 à 20 sur 20 pour tous les filtres. Un benchmark factuel ne départage pas des stratégies de contexte.
- ⚠️ **Réserves de la page elle-même** : 28 tâches, rapport standard seulement, rédaction et duel par la même famille de modèles. Coût du benchmark : ~41 $ de rédaction et filtrage, plus 8 à 15 $ de jugement.

## RésuméDe400mots

La page de documentation « Context Filter » de GPT Researcher, réécrite le 26 septembre 2026 par son créateur Assaf Elovic, décrit l'étape qui choisit, parmi les pages scrapées, les passages que le modèle rédacteur lira réellement. Elle la présente comme le principal levier sur la qualité d'un rapport après la recherche elle-même.

Pour chaque sous-requête, les pages sont plafonnées à 50 000 caractères et découpées en blocs de 1 000 caractères. Le filtre retient au plus dix blocs (vingt-cinq en mode mots-clés), puis les contextes des sous-requêtes sont joints et transmis au rédacteur. Le chat sur un rapport existant réutilise la même fonction.

Cinq modes sont disponibles. Par défaut, GPT Researcher utilise Jev, un modèle de TypeSafe qui ne génère pas de texte mais répond à des questions typées avec des probabilités calibrées. Chaque bloc reçoit un score d'utilité de 0 à 3 sur une grille à quatre niveaux ; seuls les blocs à 1,5 ou plus sont gardés. Les appels partent en parallèle, soixante-quatre à la fois, pour environ 1,7 seconde de filtrage médian et un demi-centime par rapport. Sans clé TypeSafe, ou en cas d'erreur, le système se replie sur un classement BM25 en Python pur, sans dépendance, qui garde les blocs atteignant la moitié du score du meilleur. Aucun réglage ne laisse un run sans contexte.

Le benchmark rejoue 28 tâches réelles, 20 questions SimpleQA et 8 questions ouvertes, sur les pages exactement enregistrées, avec le même modèle rédacteur. Seul le filtre varie. Jev atteint 73 % de passages pertinents contre 46 % pour les embeddings, et gagne 15 duels contre 3, avec 10 égalités, pour le même coût. Le repli BM25 atteint 51 % et gagne 14 contre 6, résultat jugé seulement directionnel. Sans filtre, les rapports ouverts gagnent en ampleur, mais coûtent 65 % de plus en moyenne.

Deux constats structurent la page. D'abord, le seuil compte plus que le classement : sans seuil, Jev tombe à 50 % et BM25 perd contre les embeddings. Ensuite, le gain est une réduction du bruit : Jev envoie 4,5 k tokens au lieu de 7,6 k, pour une quantité de texte pertinent équivalente. SimpleQA, saturé à 18-20 sur 20, ne départage rien.

La page liste ses limites : 28 tâches, un seul type de rapport, rédaction et jugement par la même famille de modèles. Scripts de collecte, de rejeu et de jugement sont publiés, avec les métriques par run, pour que chacun puisse refaire la mesure.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Assaf Elovic | PERSONNE | a_créé | GPT Researcher | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Assaf Elovic | PERSONNE | publie | page Context Filter | DOCUMENT | 0.9 | STATIQUE | inféré |
| GPT Researcher | TECHNOLOGIE | utilise | Jev | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| TypeSafe | ORGANISATION | a_créé | Jev | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| GPT Researcher | TECHNOLOGIE | utilise | BM25 | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| GPT Researcher | TECHNOLOGIE | utilise | filtre de contexte | METHODOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| filtre de contexte | METHODOLOGIE | améliore | la qualité des rapports de recherche, principal levier après la recherche elle-même | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Jev | TECHNOLOGIE | est_instance_de | modèle System One | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| modèle System One | CONCEPT | permet | des réponses à des questions typées sous forme de probabilités calibrées, sans génération de texte | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Jev | TECHNOLOGIE | surpasse | embeddings | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Jev | TECHNOLOGIE | mesure | 73 % de passages pertinents contre 46 % pour les embeddings, 15 victoires, 10 égalités, 3 défaites, sur 28 tâches | MESURE | 0.93 | STATIQUE | déclaré_article |
| BM25 | CONCEPT | mesure | 51 % de passages pertinents et 14-8-6 contre les embeddings avec seuil relatif, 40 % en top-10 brut | MESURE | 0.9 | STATIQUE | déclaré_article |
| page Context Filter | DOCUMENT | affirme_que | le seuil de sélection compte plus que le classement : sans seuil, la précision de Jev tombe de 73 % à 50 % | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| filtre de contexte | METHODOLOGIE | réduit | le bruit transmis au rédacteur, 4,5 k tokens contre 7,6 k pour une quantité de texte pertinent équivalente | MESURE | 0.9 | STATIQUE | déclaré_article |
| page Context Filter | DOCUMENT | affirme_que | ne pas filtrer élargit les rapports ouverts mais coûte 65 % de plus par rapport, sans gain sur les questions factuelles | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| page Context Filter | DOCUMENT | affirme_que | SimpleQA est saturé, 18 à 20 sur 20 pour tous les filtres, et ne départage pas les stratégies de contexte | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| page Context Filter | DOCUMENT | est_basé_sur | benchmark rejoué à pages constantes, jugé par gpt-5.4 et gpt-5.4-mini | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| page Context Filter | DOCUMENT | affirme_que | "A calibrated usefulness score can say 'nothing else on this page is worth including'; a similarity score can't." | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| filtre de contexte | METHODOLOGIE | fait_partie_de | context engineering | METHODOLOGIE | 0.8 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Assaf Elovic | PERSONNE | rôle | Créateur et mainteneur principal de GPT Researcher ; auteur des commits du 26 septembre 2026 faisant de Jev le filtre par défaut | AJOUT |
| GPT Researcher | TECHNOLOGIE | catégorie | Agent open source de recherche web autonome (Python, npm, serveur MCP, skill Claude) produisant des rapports sourcés à partir de sous-requêtes | AJOUT |
| Jev | TECHNOLOGIE | catégorie | Modèle de TypeSafe notant l'utilité d'un passage (0 à 3) par probabilités calibrées ; 0,042 $ par million de tokens d'entrée, ~32 k tokens d'entrée par appel | AJOUT |
| TypeSafe | ORGANISATION | secteur | Éditeur de Jev et de l'API System One (api.typesafe.ai) | AJOUT |
| filtre de contexte | METHODOLOGIE | définition | Étape de sélection des passages scrapés transmis au rédacteur : découpage en blocs de 1 000 caractères, score, seuil, budget par sous-requête, chaîne de repli | AJOUT |
| BM25 | CONCEPT | usage | Repli local de GPT Researcher : Python pur, ~20 ms par sous-requête, seuil relatif de 0,5 du meilleur bloc, jusqu'à 25 blocs | AJOUT |
| modèle System One | CONCEPT | définition | Modèle répondant à des questions typées sur une entrée avec des probabilités calibrées plutôt que par génération de texte | AJOUT |
| page Context Filter | DOCUMENT | forme | Documentation technique de GPT Researcher avec benchmark reproductible (scripts collect, replay, judge dans evals/context_filter), réécrite le 26 septembre 2026 | AJOUT |
