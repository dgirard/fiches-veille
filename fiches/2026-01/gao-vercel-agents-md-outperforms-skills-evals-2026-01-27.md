# gao-vercel-agents-md-outperforms-skills-evals-2026-01-27
## Veille
AGENTS.md surpasse les skills dans les évaluations agents Vercel/Next.js

## Titre Article
AGENTS.md outperforms skills in our agent evals

## Date
2026-01-27

## URL
https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals

## Keywords
AGENTS.md, skills, évaluation agents IA, contexte passif, récupération active, Next.js 16, Vercel, données d'entraînement obsolètes, documentation compressée, prompt système, coding agentique, use cache, connection(), forbidden()

## Authors
Jude Gao (Vercel)

## Ton
**Profil** : Billet technique empirique, registre analytique et factuel, niveau technique avancé

**Description** : Article de blog d'ingénierie adopant une approche scientifique rigoureuse avec protocole d'évaluation, tableaux de résultats chiffrés et analyse comparative. Le ton est celui d'un ingénieur qui partage des résultats d'expérimentation avec transparence, incluant les échecs (skills non invoquées dans 56% des cas). L'argumentation est data-driven avec des pourcentages précis. Le public cible est constitué de développeurs et mainteneurs de frameworks cherchant à optimiser l'expérience de leurs utilisateurs avec les agents de codage IA.

## Pense-betes
- **Problème de fond** : les modèles IA ont des données d'entraînement obsolètes. Next.js 16 introduit des APIs (`use cache`, `connection()`, `forbidden()`) absentes des données d'entraînement, causant du code incorrect
- **Deux approches testées** :
  - **Skills** : standard ouvert pour packager les connaissances, invocables à la demande par l'agent
  - **AGENTS.md** : fichier markdown statique fournissant un contexte persistant à chaque interaction
- **Résultats clés** :
  - Sans documentation : 53% de réussite
  - Skills (comportement par défaut) : 53% (+0pp, aucun gain !)
  - Skills avec instructions explicites : 79% (+26pp)
  - **AGENTS.md avec index : 100% (+47pp)**
- **Fragilité des skills** : dans 56% des cas d'évaluation, la skill n'a jamais été invoquée par l'agent
- **Même avec instructions explicites** : le déclenchement des skills montait à 95%+ mais le succès dépendait fortement de la formulation exacte
- **Compression réussie** : documentation de 40 Ko compressée à 8 Ko (réduction 80%) avec format délimité par des pipes, sans perte de performance
- **Théorie des 3 avantages du contexte passif** :
  1. Pas de point de décision (information disponible sans choix à faire)
  2. Disponibilité constante (AGENTS.md dans le prompt système à chaque tour)
  3. Pas de problèmes d'ordonnancement (pas de séquençage d'actions)
- **Recommandations pratiques** : ne pas attendre l'amélioration des skills, compresser agressivement les index, construire des évaluations ciblant les APIs hors données d'entraînement
- **Installation** : `npx @next/codemod@canary agents-md` détecte la version, télécharge les docs et injecte l'index dans AGENTS.md
- **Nuance importante** : les skills restent utiles pour les workflows d'actions spécifiques déclenchées explicitement, mais pour les connaissances générales de framework, le contexte passif surperforme

## RésuméDe400mots
Jude Gao de Vercel présente les résultats d'une évaluation comparative entre deux approches pour transmettre aux agents IA les connaissances spécifiques aux frameworks : les skills (récupération active) et AGENTS.md (contexte passif). Le constat est sans appel : la méthode la plus simple surpasse largement la plus sophistiquée.

**Le problème** : Next.js 16 introduit de nouvelles APIs (`use cache`, `connection()`, `forbidden()`) absentes des données d'entraînement des modèles IA. Sans documentation actualisée, les agents génèrent du code incorrect dans 47% des cas.

**Skills : échec de la récupération active** : Les skills, standard ouvert pour packager les connaissances invocables à la demande, se révèlent fragiles. Dans 56% des cas d'évaluation, l'agent n'a jamais invoqué la skill disponible, produisant un taux de réussite identique à la baseline (53%). Même en ajoutant des instructions explicites forçant le déclenchement (95%+ d'invocation), le taux ne monte qu'à 79%, et les résultats varient dramatiquement selon la formulation exacte des instructions.

**AGENTS.md : victoire du contexte passif** : Un fichier markdown statique injecté dans le prompt système à chaque tour atteint 100% de réussite (build, lint et tests). Cette approche élimine trois sources de fragilité : le point de décision (l'agent n'a pas à choisir d'invoquer), les problèmes de disponibilité (l'information est toujours présente) et les enjeux d'ordonnancement (pas de séquençage d'actions nécessaire).

**Compression agressive** : L'équipe Vercel a réussi à compresser 40 Ko de documentation en un index de 8 Ko (réduction de 80%) utilisant un format délimité par des pipes, tout en maintenant le taux de réussite à 100%. Cette compression est essentielle car AGENTS.md consomme de la fenêtre de contexte à chaque interaction.

**Implications pour l'écosystème** : Les résultats suggèrent que pour les connaissances générales de framework, le contexte passif (toujours disponible) surperforme la récupération active (à la demande). Les skills conservent toutefois leur utilité pour les workflows d'actions explicites. Vercel propose une commande d'installation (`npx @next/codemod@canary agents-md`) qui détecte automatiquement la version de Next.js et génère l'AGENTS.md correspondant.

**Recommandations** : Ne pas attendre l'amélioration des skills, compresser agressivement la documentation dans les index, et construire des évaluations ciblant spécifiquement les APIs absentes des données d'entraînement. Ces résultats ont des implications directes pour tous les mainteneurs de frameworks et bibliothèques cherchant à optimiser la compatibilité avec les agents de codage IA.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Jude Gao | PERSONNE | a_publié | AGENTS.md outperforms skills in our agent evals | EVENEMENT | 0.99 | STATIQUE | déclaré_article |
| Jude Gao | PERSONNE | travaille_pour | Vercel | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| AGENTS.md | TECHNOLOGIE | atteint | taux de réussite 100% | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| skills | TECHNOLOGIE | atteint | taux de réussite 79% | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| skills | TECHNOLOGIE | surpasse | baseline sans documentation | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| AGENTS.md | TECHNOLOGIE | surpasse | skills | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| contexte passif | CONCEPT | élimine | point de décision agent | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Next.js 16 | TECHNOLOGIE | introduit | use cache | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Next.js 16 | TECHNOLOGIE | introduit | connection() | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Next.js 16 | TECHNOLOGIE | introduit | forbidden() | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Vercel | ORGANISATION | a_développé | évaluations Next.js 16 | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| documentation compressée | CONCEPT | réduit | contexte de 40 Ko à 8 Ko | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| skills | TECHNOLOGIE | n'est_pas_invoqué | dans 56% des cas d'évaluation | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| CLAUDE.md | TECHNOLOGIE | est_équivalent_à | AGENTS.md | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Jude Gao | PERSONNE | rôle | Ingénieur / Auteur chez Vercel | AJOUT |
| Vercel | ORGANISATION | secteur | Hébergement / Infrastructure web | AJOUT |
| AGENTS.md | TECHNOLOGIE | catégorie | Fichier de contexte persistant pour agents IA | AJOUT |
| skills | TECHNOLOGIE | catégorie | Standard ouvert de packaging de connaissances agent | AJOUT |
| Next.js 16 | TECHNOLOGIE | catégorie | Framework React — Vercel | AJOUT |
| contexte passif | CONCEPT | définition | Information injectée dans le prompt système sans décision d'invocation | AJOUT |
| récupération active | CONCEPT | définition | Invocation à la demande d'une ressource de connaissances par l'agent | AJOUT |
| documentation compressée | CONCEPT | taux de compression | 80% (40 Ko → 8 Ko) | AJOUT |
| CLAUDE.md | TECHNOLOGIE | catégorie | Équivalent Claude Code d'AGENTS.md | AJOUT |
| use cache | TECHNOLOGIE | catégorie | Nouvelle API Next.js 16 absente des données d'entraînement | AJOUT |
