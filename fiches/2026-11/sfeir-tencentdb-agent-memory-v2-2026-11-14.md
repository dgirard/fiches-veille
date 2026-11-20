---
themes: [outils-plateformes, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-tencentdb-agent-memory-v2-2026-11-14

## Veille

Article SFEIR AI publié sur sfeir.com le **14 novembre 2026** (~1 200 mots), consacré à **TencentDB Agent Memory**, projet open source (MIT, TypeScript) de l'équipe base de données de **Tencent Cloud**, devenu hub de mémoire d'équipe avec la version **2.0.0 du 3 août 2026**. Trois apports : (A) l'architecture — **quatre actifs** (Chat Memory en niveaux L0-L3, Skill, LLM-Wiki inspiré d'Andrej Karpathy, Code-Graph) et **quatre services** (Memory Core, Panel UI, Knowledge, **Proxy** sur le port 8096, qui s'intercale entre l'agent et le modèle) ; (B) la gouvernance — visibilité *private* par défaut, *team*, *restricted* et *agent* ; agents pris en charge (Claude Code, CodeBuddy, Codex, OpenCode, WorkBuddy, DeepSeek Harness, Hermes, OpenClaw), **sans Cursor** au 14 novembre, avec une réserve sur Codex (API Responses non exposée par le Proxy) ; (C) les chiffres de l'éditeur (jusqu'à **61,38 %** de tokens en moins sur WideSearch, PersonaMem **48 % → 76 %**), signalés comme non répliqués, et **30 880 étoiles**. L'article termine par **cinq points de contrôle** pour une DSI (Proxy à auditer comme une passerelle LLM, hébergement des deux groupes de modèles, fraîcheur, export, comparaison avec Mem0, Zep et Letta). Volet de la série SFEIR sur la mémoire d'agent, à rapprocher de [[DeepSeek-Harness]].

## Titre Article

TencentDB Agent Memory v2 : une mémoire d'équipe gouvernée pour Claude Code, Codex et CodeBuddy

## Date

2026-11-14

## URL

https://www.sfeir.com/articles/tencentdb-agent-memory-v2-memoire-equipe/

## Keywords

TencentDB Agent Memory, Tencent Cloud, hub de mémoire, mémoire d'équipe, Chat Memory, L0-L3, Skill, LLM-Wiki, Code-Graph, Memory Proxy, Panel UI, visibilité private team restricted, Claude Code, Codex, CodeBuddy, WorkBuddy, OpenCode, OpenClaw, Hermes, WideSearch, PersonaMem, auto-hébergement, Mem0, Zep, Letta

## Authors

SFEIR AI (voix éditoriale de SFEIR), article publié sur sfeir.com, site éditorial du groupe SFEIR.

## Ton

Fiche produit en français, de registre documentaire, adressée aux DSI et architectes qui évaluent un hub de mémoire. L'article est construit à partir de sources primaires (releases, README de deux branches, guide d'installation, issue GitHub, API GitHub) et le signale à chaque affirmation. Il relève les écarts entre documents (le guide parle d'injection à chaque tour, le README précise que wiki et graphe sont appelés à la demande) sans trancher au-delà de ce qu'ils disent. Les chiffres de performance sont restitués avec leur périmètre exact (benchmark WideSearch seul pour les deux premiers) et qualifiés de chiffres d'éditeur. Une section lève les confusions de noms avec deux autres produits Tencent. La conclusion prend la forme d'une liste de contrôles et reconnaît ce que la série n'a pas fait (comparaison avec Mem0, Zep, Letta).

## Pense-betes

- **Chronologie** : dépôt créé le 7 avril 2026 ; v0.x (mai) = mémoire locale L0 conversation → L1 faits → L2 scénarios → L3 persona, SQLite + sqlite-vec, plugin OpenClaw ; **2.0.0** (3 août) hub d'équipe ; 2.0.1 (25 août) Codex CLI, WorkBuddy, OpenCode, DeepSeek Harness ; 2.0.2 (9 octobre) MongoDB expérimental ; 2.0.3 (26 octobre) wiki ouvert aux documents Office et PDF.
- **Quatre actifs** : Chat Memory, Skill (procédures versionnées, exportables), LLM-Wiki, Code-Graph (symboles, chaînes d'appel, impact).
- **Quatre services** : Memory Core (8420), Panel UI (8125), Knowledge (8424), **Proxy (8096)** : l'agent pointe vers le Proxy, qui injecte L2/L3, skills et connaissances dans le prompt système.
- **Visibilité** : private (défaut), team, restricted (utilisateurs, rôles, agents), agent.
- **Agents** : Claude Code, CodeBuddy, Codex, OpenCode, WorkBuddy, DeepSeek Harness, Hermes, OpenClaw, Pi ; **pas Cursor**. Issue n° 833 : Codex n'accepte que l'API Responses, non exposée par le Proxy.
- **Tencent AI sur X** : *« Model + Harness = Agent »*, *« We'd add one more term: Memory »*.
- **Chiffres éditeur** (README v1, avec OpenClaw) : −61,38 % de tokens et +51,52 % de réussite relative sur WideSearch ; SWE-bench −33 % de tokens, +9,9 % ; PersonaMem 48 % → 76 %. 30 880 étoiles, 3 021 forks.
- **Déploiement** : gratuit, Docker ; Kubernetes par modèles de configuration ; deux groupes de modèles (mémoire, Proxy). Ne pas confondre avec *Agent Long-Term Memory* (TencentDB for PostgreSQL) ni avec Tencent Cloud Agent Memory (hébergé).
- **Cinq contrôles DSI** : Proxy = passerelle LLM à auditer ; hébergement des modèles ; fraîcheur (citation Waselnuk) ; sortie (import/export général non encore livré) ; comparaison Mem0/Zep/Letta.
- À relier : [[OpenClaw]], [[Agent-Memory]].

## RésuméDe400mots

L'article présente TencentDB Agent Memory, un projet open source de l'équipe base de données de Tencent Cloud, sous licence MIT. Avec sa version 2.0.0 du 3 août 2026, le projet passe d'une mémoire locale pour un agent à un hub de mémoire partagé par une équipe. Les versions suivantes ont ajouté de nouveaux agents, un stockage MongoDB expérimental et l'ouverture du wiki aux documents bureautiques.

La version 2 organise la mémoire en quatre familles : la mémoire de conversation, distillée en quatre niveaux allant de la conversation brute au profil de l'utilisateur ; les skills, procédures versionnées et exportables ; un wiki de documents transformés en pages reliées, qui se réclame de l'idée d'Andrej Karpathy ; un graphe de code. Quatre services la mettent en œuvre, dont un Proxy placé entre l'agent et le modèle. Selon le guide d'installation, ce Proxy injecte à chaque tour une partie de la mémoire et des skills dans le prompt système ; le README précise que le wiki et le graphe de code sont appelés à la demande.

Chaque mémoire porte un niveau de visibilité : privé par défaut, équipe, restreint à une liste d'utilisateurs, de rôles ou d'agents, ou réservé à certains agents. Le projet prend en charge Claude Code, CodeBuddy, Codex, OpenCode, WorkBuddy, DeepSeek Harness, Hermes et OpenClaw, mais pas Cursor à la date de l'article. L'intégration de Codex reste partielle, le Proxy n'exposant pas l'API attendue par ce client.

Les chiffres de performance proviennent de l'éditeur : jusqu'à 61 % de tokens en moins et un taux de réussite en hausse sur un benchmark précis, une précision de personnalisation passée de 48 % à 76 %. L'article note qu'aucune réplication indépendante n'a été trouvée. Le logiciel est gratuit et s'auto-héberge avec Docker ; il demande deux groupes de modèles. Deux autres produits Tencent aux noms proches ne doivent pas être confondus avec lui.

Pour une DSI, SFEIR liste cinq points de contrôle : auditer le Proxy comme une passerelle vers les modèles puisqu'il voit tous les prompts ; vérifier où tournent les modèles utilisés ; traiter la fraîcheur des faits, que les droits d'accès ne règlent pas ; tester l'export avant d'y verser un an de contexte ; comparer avec Mem0, Zep et Letta, que la série n'a pas évalués. L'article suggère enfin de combiner le hub avec un dépôt Git qui garde les notes d'origine.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | TencentDB Agent Memory v2 : une mémoire d'équipe gouvernée | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Tencent Cloud | ORGANISATION | a_créé | TencentDB Agent Memory | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Tencent Cloud | ORGANISATION | publie | TencentDB Agent Memory 2.0.0 | EVENEMENT | 0.93 | STATIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | utilise | Memory Proxy | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | utilise | LLM-Wiki | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| LLM-Wiki | CONCEPT | s_inspire_de | Andrej Karpathy | PERSONNE | 0.85 | STATIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | utilise | Code-Graph | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | permet | droits d'accès fins sur la mémoire d'équipe | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | s_applique_à | Claude Code | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | s_applique_à | CodeBuddy | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | s_applique_à | DeepSeek Harness | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | réduit | jusqu'à −61,38 % de tokens sur WideSearch (chiffre éditeur) | MESURE | 0.8 | STATIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | améliore | PersonaMem : 48 % → 76 % (chiffre éditeur) | MESURE | 0.8 | STATIQUE | déclaré_article |
| Tencent AI | ORGANISATION | affirme_que | Model + Harness = Agent ; We'd add one more term: Memory | CITATION | 0.88 | STATIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | concurrence | Mem0 | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | concurrence | Letta | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | auditer le Memory Proxy comme une passerelle LLM et tester l'export avant adoption | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Brandon Waselnuk | PERSONNE | affirme_que | confident recall of stale facts is worse than no memory | CITATION | 0.88 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| TencentDB Agent Memory | TECHNOLOGIE | catégorie | Hub de mémoire d'équipe open source (MIT), v2.0.0 du 3 août 2026, 30 880 étoiles | AJOUT |
| Tencent Cloud | ORGANISATION | secteur | Cloud de Tencent, éditeur de TencentDB Agent Memory | AJOUT |
| Memory Proxy | TECHNOLOGIE | rôle | Intermédiaire agent-modèle (port 8096) injectant la mémoire dans le prompt système | AJOUT |
| LLM-Wiki | CONCEPT | définition | Documents transformés en pages reliées, maintenues par LLM | AJOUT |
| Code-Graph | TECHNOLOGIE | rôle | Graphe de symboles, chaînes d'appel et impact des modifications | AJOUT |
| Tencent AI | ORGANISATION | support | Compte X @TencentAI_News | AJOUT |
