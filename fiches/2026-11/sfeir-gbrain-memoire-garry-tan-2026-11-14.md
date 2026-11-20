---
themes: [agents-codage-ia-skills, outils-plateformes]
source: SFEIR
---
# sfeir-gbrain-memoire-garry-tan-2026-11-14

## Veille

Article SFEIR AI publié sur sfeir.com le **14 novembre 2026** (~1 300 mots), consacré à **GBrain**, dépôt créé le 5 avril 2026 par **Garry Tan** (président et CEO de Y Combinator), en TypeScript sous licence **MIT** (**32 865 étoiles** au 14 novembre). Trois apports : (A) le fonctionnement — les pages restent des fichiers Markdown du dépôt ; GBrain les indexe dans **PGLite** (jusqu'à ~50 000 pages) ou Postgres + pgvector, construit un **graphe typé** de liens extraits sans LLM et une chronologie, et les expose par CLI et serveur MCP ; (B) les frontières — la base est un index reconstructible, mais les pages créées en base, l'historique et l'état opérationnel demandent une sauvegarde ; le mode équipe (10 à 50 personnes) borne lui-même son cloisonnement ; (C) des chiffres d'instance datés et non vérifiables (17 888 pages en avril, 155 795 en novembre, ~220 000 annoncées en août). L'article cite Cathryn Lavery : *« gbrain is not memory. It's a library. »* Il signale deux questions ouvertes (fraîcheur des notes, flux vers les fournisseurs d'embeddings) et propose un essai en une heure. Volet de la série SFEIR sur la mémoire d'agent, à côté des fiches sur [[OpenClaw]].

## Titre Article

GBrain : la mémoire de Garry Tan, en Markdown et sous licence MIT

## Date

2026-11-14

## URL

https://www.sfeir.com/articles/gbrain-memoire-garry-tan-markdown-mit/

## Keywords

GBrain, Garry Tan, Y Combinator, mémoire d'agent, Markdown, dépôt Git, PGLite, Postgres, pgvector, graphe typé, MCP, CLI, OpenClaw, Hermes Agent, Claude Code, Codex, Cursor, dream, autopilot, embeddings, Voyage, gbrain-evals, gstack, réversibilité, cerveau d'équipe

## Authors

SFEIR AI (voix éditoriale de SFEIR), article publié sur sfeir.com, site éditorial du groupe SFEIR.

## Ton

Fiche outil en français, de registre descriptif et vérificateur, pour des équipes techniques qui envisagent une mémoire d'agent. L'article s'appuie presque entièrement sur le README et l'API GitHub, et date chaque compteur. Il distingue soigneusement ce que l'outil fait de ce qu'il laisse à la charge de l'utilisateur, avec un point de vocabulaire (l'outil indexe, le dépôt appartient à l'utilisateur). Les affirmations de l'auteur du dépôt sont attribuées (« Tan publie », « le README affirme ») et les incohérences entre sources sont signalées sans être tranchées (chiffre du talk supérieur au README, étoiles du premier jour divergentes). Les limites sont citées depuis la documentation même du projet. La conclusion est pratique : cinq étapes pour tester l'outil en une heure, dont la suppression et la reconstruction de l'index.

## Pense-betes

- **Identité** : dépôt `garrytan/gbrain`, créé le 5 avril 2026 (*« GBrain v0.1.0 — Postgres-native personal knowledge brain »*), TypeScript, MIT ; 32 865 étoiles, 4 906 forks au 14 novembre 2026.
- **Trois fonctions** : indexation Postgres (PGLite en WebAssembly par défaut, Postgres + pgvector pour le partagé) ; graphe typé de liens (`works_at`, `attended`) extrait sans LLM + chronologie par page ; exposition CLI et MCP (`gbrain serve`).
- **Commandes** : `init`, `import`, `query`, `embed`, `graph-query`, `dream`, `autopilot`. Recherche par mots-clés sans clé d'API ; sémantique via Voyage par défaut, OpenAI ou modèle local.
- **Agents** : né pour OpenClaw et Hermes Agent (fichier `INSTALL_FOR_AGENTS.md`) ; `gbrain setup claude-code` / `codex` ; Cursor via MCP. Le README conseille désormais de l'ajouter à l'agent existant. Offre hébergée payante optionnelle gbrain.io.
- **Réversibilité bornée** : le dépôt porte le Markdown, la base est reconstructible ; mais pages créées en base, faits non résolus, historique et état opérationnel exigent une sauvegarde.
- **Mode équipe** : autorisations par source et par opération, filtres de visibilité ; les fichiers locaux et identifiants partagés de la base forment une autre frontière, non isolée ; les tests couvrent des chemins précis, pas une garantie générale.
- **Chiffres de l'instance de Tan** (auto-déclarés) : 17 888 pages (24 avril) → 146 646 (23 mai) → ~220 000 (talk du 6 août) → 155 795 (14 novembre).
- Ne pas confondre avec **gstack** (configuration Claude Code de Tan, 141 469 étoiles). Dépôt compagnon `gbrain-evals`.
- **Questions ouvertes** : fraîcheur (un index retrouve une note fausse aussi vite qu'une juste) ; coûts et flux vers des fournisseurs externes.
- À relier : [[Hermes]], [[Agent-Memory]].

## RésuméDe400mots

L'article présente GBrain, un outil open source créé par Garry Tan, président et CEO de Y Combinator, en avril 2026. Écrit en TypeScript et publié sous licence MIT, le dépôt comptait près de 33 000 étoiles à la mi-novembre 2026. Il se décrit comme le cerveau d'agent de Tan pour OpenClaw et Hermes Agent.

Le principe est de laisser les pages sous forme de fichiers Markdown dans un dépôt appartenant à l'utilisateur. GBrain les lit et fait trois choses : il les indexe dans une base Postgres (PGLite, compilée en WebAssembly, pour un usage personnel jusqu'à environ 50 000 pages ; Postgres avec pgvector pour un usage partagé), il construit un graphe typé de liens entre pages et une chronologie, extraits sans appel à un modèle de langage, et il expose le tout aux agents par une ligne de commande et un serveur MCP. La recherche par mots-clés fonctionne sans clé d'API ; la recherche sémantique passe par un fournisseur d'embeddings.

Claude Code et Codex disposent d'une commande d'installation dédiée, Cursor se branche comme client MCP. Le README recommande désormais d'ajouter GBrain à l'agent déjà utilisé plutôt que de monter un agent dédié, et mentionne une offre hébergée payante facultative.

SFEIR insiste sur une distinction : GBrain est l'outil, le dépôt de Markdown reste lisible sans lui. La réversibilité a cependant une limite indiquée par le projet : certaines données ne vivent que dans la base et doivent être sauvegardées. L'article cite une formule de Cathryn Lavery selon laquelle GBrain n'est pas une mémoire mais une bibliothèque : décider quoi écrire, corriger ou jeter reste le travail de l'agent et de son propriétaire.

Conçu pour une personne, GBrain revendique aussi un usage d'équipe avec autorisations et filtres de visibilité, mais sa documentation précise que ce cloisonnement ne couvre pas toutes les frontières de confiance. L'article reproduit les tailles successives de l'instance de Tan, auto-déclarées et non vérifiables, et relève qu'elles ne forment pas une série cohérente.

Deux questions restent ouvertes : la fraîcheur des notes, que GBrain traite par un cycle de maintenance nocturne dont l'efficacité en entreprise reste à mesurer, et les coûts et flux de données vers des fournisseurs de modèles externes. L'article conclut par un protocole d'essai en cinq étapes sur un dépôt privé de dix fichiers.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | GBrain : la mémoire de Garry Tan, en Markdown et sous licence MIT | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Garry Tan | PERSONNE | a_créé | GBrain | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Garry Tan | PERSONNE | dirige | Y Combinator | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| GBrain | TECHNOLOGIE | utilise | PGLite | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| GBrain | TECHNOLOGIE | utilise | pgvector | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| GBrain | TECHNOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| GBrain | TECHNOLOGIE | permet | graphe typé de liens entre pages Markdown | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| GBrain | TECHNOLOGIE | s_applique_à | OpenClaw | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| GBrain | TECHNOLOGIE | s_applique_à | Hermes Agent | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| GBrain | TECHNOLOGIE | s_applique_à | Claude Code | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| GBrain | TECHNOLOGIE | mesure | 32 865 étoiles GitHub au 14 novembre 2026 | MESURE | 0.92 | STATIQUE | déclaré_article |
| Cathryn Lavery | PERSONNE | affirme_que | gbrain is not memory. It's a library. | CITATION | 0.9 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la base de GBrain est un index reconstructible, mais l'historique et l'état opérationnel exigent une sauvegarde | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Garry Tan | PERSONNE | a_créé | gstack | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| GBrain | TECHNOLOGIE | concurrence | TencentDB Agent Memory | TECHNOLOGIE | 0.72 | DYNAMIQUE | inféré |
| SFEIR | ORGANISATION | recommande | tester GBrain en une heure sur un dépôt privé et mesurer la reconstruction de l'index | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| GBrain | TECHNOLOGIE | catégorie | Index et graphe de mémoire d'agent sur dépôt Markdown, MIT, CLI + MCP | AJOUT |
| Garry Tan | PERSONNE | rôle | Président et CEO de Y Combinator | AJOUT |
| PGLite | TECHNOLOGIE | catégorie | Postgres compilé en WebAssembly, base par défaut de GBrain | AJOUT |
| Cathryn Lavery | PERSONNE | support | Little Might | AJOUT |
| gstack | TECHNOLOGIE | catégorie | Configuration Claude Code publiée par Garry Tan | AJOUT |
| Hermes Agent | TECHNOLOGIE | catégorie | Agent personnel compatible GBrain | AJOUT |
