---
themes: [architecture-construction, outils-plateformes, qualite-securite, agents-codage-ia-skills]
source: "Deep Research"
---
# buzz-block-panorama-deep-research-2026-08-12

## Veille

Rapport de recherche interne du **12 août 2026** consolidant, en vue d'une présentation, tout ce qui est publiquement documenté sur **Buzz** — le workspace humains + agents de **Block**, lancé le **21 juillet 2026** sous licence **Apache 2.0**. Il agrège les deux billets d'ingénierie déjà fichés avec l'annonce corporate, le dépôt GitHub, la presse, X, et **trois retours d'expérience indépendants** qui constituent les seules données non auto-déclarées du dossier. **(A) Un écart de vocabulaire documenté par citation** : le tweet de lancement de **Jack Dorsey** annonce *« model-agnostic, decentralized, self-sovereign, and open source »* ; l'`ARCHITECTURE.md` de Block écrit *« The relay is the single source of truth. All reads and writes flow through it. There is no peer-to-peer event exchange, no gossip, no replication. »* Le relais est donc unique et autoritaire par communauté : la « décentralisation » de Buzz est une **souveraineté organisationnelle** — auto-hébergement et identité portable — non une redondance réseau. Formule de **TFTC** : *« Two of those three hold cleanly. The third needs a qualifier. »* **(B) Une asymétrie entre la rigueur démontrée et le risque d'exploitation.** D'un côté, un formalisme rare pour une v0.4.x/0.5.x : spécification d'isolation multi-tenant **mécanisée en TLA+**, propriétés d'autorisation vérifiées en **Tamarin**, protocole de stockage Git model-checké, journal d'audit append-only à chaîne de hash, 127 *event kinds*, NIP-01/42/98/34. De l'autre, l'appartenance au canal est l'unité de permission — *« channel membership is not fine-grained tool authorization »* (João Queirós) —, les agents tournent en `--dangerously-skip-permissions` hors bac à sable sur le poste d'un humain, et l'observabilité manque : *« Buzz tells me an agent got a message. It doesn't tell me what happens next »* (DevTools Daily, qui rapporte des kills OOM silencieux). Block l'assume : *« the agent can do anything, and security rests entirely on restricting who can tell it what to do »*. **(C) La pile technique**, absente des billets fichés : relais **Rust** (Axum WS + REST), **Postgres**, **Redis**, **S3/MinIO** via Blossom, client desktop **Tauri + React**. L'intégration agent passe par **`buzz-acp`**, harnais **ACP** qui branche goose, Codex et Claude Code et traduit **ACP ↔ MCP**, plus **`buzz-agent`**, agent maison. Le rapport se corrige lui-même sur un point : le *« +33 % de travail »* du TL;DR de Block est le **ratio de tâches terminées (20 contre 15 sur 44)**, non un gain de score — celui-ci passe de 59,1 % à 71,5 %, soit **+12,4 points**.

## Titre Article

Buzz (buzz.xyz) — Rapport de recherche pour présentation

## Date

2026-08-12

## URL

*Aucune URL publique — rapport de recherche interne non publié au moment de la mise en fiche. Source archivée dans `raw-data/buzz-block-panorama-deep-research-2026-08-12.md`.*

## Keywords

Buzz, buzz.xyz, Block, Jack Dorsey, workspace agentique, humains et agents, canal, Apache 2.0, souveraineté organisationnelle, décentralisation, relais unique, point de défaillance unique, pas de réplication, ARCHITECTURE.md, Nostr, NIP-01, NIP-42, NIP-98, NIP-34, event kinds, paire de clés, identité cryptographique, identité portable, autorisation déléguée, journal d'audit, append-only, chaîne de hash, tamper-evidence, tamper-resistance, opérateur de relais compromis, chiffrement de bout en bout, Rust, Axum, Postgres, Redis, MinIO, Blossom, Tauri, React, Git sur stockage objet, TLA+, Tamarin, vérification formelle, isolation multi-tenant, Agent Client Protocol, ACP, buzz-acp, buzz-agent, MCP, traduction ACP MCP, composabilité par protocoles, goose, Codex, Claude Code, OpenRouter, vLLM, llama.cpp, Ollama, Hive, Swarm, Terminal-Bench 2.1, Long-Horizon Terminal-Bench, dangerously-skip-permissions, autorisation par canal, observabilité des agents, OOM silencieux, mention obligatoire, app mobile, appairage QR, EXIF, NIP-PL, BuilderBot, Agentic AI Foundation, Linux Foundation, AGENTS.md, DevTools Daily, TFTC, Sundar Pichai, Justin Waldron, multiplayer agent harness, maturité v0.x, caveats

## Authors

**Deep Research Veille Interne** — rapport non signé, produit le **12 août 2026** en préparation d'une présentation. Aucune URL publique ; source archivée dans `raw-data/`.

Rapport de veille et non source primaire : ce qu'il apporte est la couche que Block ne publie pas — l'`ARCHITECTURE.md` du dépôt, les métriques GitHub, la presse, et **trois évaluations indépendantes** (João Queirós, DevTools Daily, darrenjrobinson). Chaque affirmation porte sa source, les verbatims sont donnés en anglais avec traduction, et les URL X sont distinguées selon qu'elles ont été vérifiées, vérifiées par contenu seulement, ou non retrouvées. Une section **Caveats** finale liste six réserves, dont *« Les benchmarks proviennent de Block (auto-évaluation), sur son propre setup. »* Le document est explicitement outillé pour une présentation (section Recommandations, ordre des slides) : à lire comme un livrable de préparation.

## Ton

**Profil** : rapport de recherche structuré (TL;DR → Key Findings → détails en huit sections → Recommandations → Synthèse → Caveats), registre analyste, en français avec verbatims anglais systématiquement traduits. Public : celui qui doit présenter Buzz à des pairs sans se faire prendre en défaut.

**Style** : le procédé dominant est la **mise en regard** plutôt que le jugement — le rapport place la formule marketing à côté de la documentation technique et laisse l'écart parler, le tweet de Dorsey face à l'`ARCHITECTURE.md`. La traçabilité fait office d'argument : URL complètes, dates, numéros d'issues GitHub (#2484, #2367), montants d'acquisition (Slack → Salesforce **27,7 Md$** le 21/07/2021 ; GitHub → Microsoft **7,5 Md$** le 04/06/2018), versions divergentes selon la source. Le document est construit pour résister à une question hostile en séance, et il assume sa recommandation rhétorique : *« Une slide "limites" honnête… cela renforce la crédibilité de l'exposé. »*

**Formules-marqueurs empruntées à ses sources** :
- ***« The bottleneck moved from intelligence to coordination »*** (Longwell)
- ***« authorization does not erase authorship »*** (Block)
- ***« channel membership is not fine-grained tool authorization »*** (Queirós)
- ***« Buzz tells me an agent got a message. It doesn't tell me what happens next »*** (DevTools Daily)
- ***« Two of those three hold cleanly. The third needs a qualifier »*** (TFTC)
- ***« It's the first proper multiplayer agent harness »*** (Waldron)
- ***« rough edges and giant chasms »*** (Block)

**Position épistémique** : bornée et auditée — ce qui est vérifié l'est, ce qui ne l'est pas est nommé. Point aveugle assumé : aucune donnée d'adoption en entreprise, aucun prix d'hébergement, aucun chiffre de rétention, Block n'en publiant pas. Le rapport le traduit en critère de réévaluation plutôt qu'en spéculation.

## Pense-betes

- **Date / source** : **12 août 2026**, rapport de veille interne non publié. Agrège billets Block, `ARCHITECTURE.md`, presse, X et trois retours indépendants.
- **Cadrage clé** : le vocabulaire de lancement n'est pas la documentation d'architecture. Méthode transposable : sur toute plateforme qui se dit décentralisée, lire `ARCHITECTURE.md` **avant** le billet d'annonce.

### L'écart décentralisation / architecture

| Source | Énoncé |
|---|---|
| Tweet **Jack Dorsey** | *« model-agnostic, decentralized, self-sovereign, and open source »* |
| `ARCHITECTURE.md` Block | *« The relay is the single source of truth. All reads and writes flow through it. There is no peer-to-peer event exchange, no gossip, no replication. »* |
| **TFTC** | *« Two of those three hold cleanly. The third needs a qualifier. »* |

Un relais unique par communauté constitue un point de défaillance unique. La souveraineté proposée est organisationnelle — auto-héberger, emporter son identité — non une redondance réseau.

### Rigueur démontrée vs risque d'exploitation

| Ce qui est formellement vérifié | Ce qui ne l'est pas |
|---|---|
| isolation multi-tenant **mécanisée en TLA+** | l'unité de permission est **l'appartenance au canal** |
| propriétés d'autorisation vérifiées en **Tamarin** | les agents tournent en `--dangerously-skip-permissions`, hors bac à sable |
| protocole de stockage Git model-checké | l'observabilité d'agent manque — kills OOM silencieux, tâches abandonnées paraissant actives |
| journal d'audit append-only à chaîne de hash | — |

La preuve formelle porte sur l'identité et le stockage ; le risque d'exploitation est dans l'autorisation d'outil et la visibilité. Ne pas laisser la première rassurer sur le second.

### Distinction de sécurité à retenir

***Tamper-evidence ≠ tamper-resistance.*** Les événements signés prouvent qui a fait quoi ; ils n'empêchent pas un opérateur de relais compromis de **supprimer** des événements. Sur le relais hébergé par Block, les messages ne sont pas chiffrés de bout en bout, et les fournisseurs de modèles peuvent recevoir prompts et contenus de canal. Question à poser à tout fournisseur vendant un journal d'audit « inaltérable » : inaltérable contre la modification, ou contre la suppression ?

### Correction de chiffre

Le TL;DR de Block annonce *« 33% more work »* : c'est le ratio de **tâches terminées — 20 contre 15 sur 44** —, non un gain de score. Le score passe de **59,1 % à 71,5 %**, soit **+12,4 points**, dont 11,4 issus des complétions supplémentaires. Le rapport juxtapose lui-même les deux dans sa synthèse, formulation ambiguë à ne pas recopier en slide. Détail complet, y compris le résultat négatif sur les tâches courtes, dans [[patel-block-buzz-teams-tokens-benchmarks-2026-08-06]].

### Pile technique et déploiement

Relais **Rust** (Axum WS + REST), **Postgres** (événements + recherche plein texte), **Redis** (pub/sub, présence, saisie), **S3/MinIO** (médias via Blossom), desktop **Tauri + React**. **127 event kinds** ; NIP-01 (fil), NIP-42 (auth connexion), NIP-98 (auth REST), NIP-34 (événements Git). Déploiement par Docker Compose de production (Postgres, Redis, MinIO, Caddy/TLS), Railway en un clic, ou relais hébergé gratuit de Block en beta. Rust 1.88+, Node 24+, pnpm.

### Interopérabilité

**`buzz-acp`** est un harnais **Agent Client Protocol** (né chez Zed, JSON-RPC 2.0 sur stdio, passé en gouvernance communautaire) qui branche **goose**, **Codex** et **Claude Code**, et traduit **ACP ↔ MCP** — ACP côté client/agent, MCP côté outils. S'y ajoute **`buzz-agent`**, agent maison : jusqu'à **8 sessions concurrentes**, chacune avec ses propres serveurs MCP, historique et contexte ; Anthropic Messages API, OpenRouter, ou tout endpoint compatible OpenAI (vLLM, llama.cpp, Databricks, Ollama).

Formule à garder : *« The agent does not know what MCP server it talks to. The MCP server does not know what agent is calling it. They compose through protocols, not imports. »* Pour le piège du sigle ACP, voir [[girard-acp-deux-protocoles-un-sigle-2026-08-02]].

### Généalogie

**goose** (Block, **28 janvier 2025**, Apache 2.0, CTO Dhanji Prasanna) est l'ancêtre, contribué en **décembre 2025** à l'**Agentic AI Foundation** de la Linux Foundation aux côtés de MCP et d'AGENTS.md — 27 000+ étoiles, 350+ contributeurs. **BuilderBot**, premier agent Slack interne de Block, fournit le problème d'origine : credentials partagés, changement de modèle, gestion d'identité. Block accumule une position sur la couche ouverte agentique depuis dix-huit mois.

### Enjeu de marché

**Bradley Axen** (Head of AI Capabilities, Block) : *« Every company is going to need a place where humans and agents work together. The question is whether that place is proprietary or open. »* **Justin Waldron** (cofondateur Zynga) : *« Buzz is not a slack killer. It's much bigger. It's the first proper multiplayer agent harness. »* Réception : ~25 900 étoiles GitHub (~7 600 en trois jours), tweet Dorsey à ~2,3–2,7 M vues, couverture TechCrunch / SiliconANGLE / Decrypt, soutien public de Sundar Pichai.

### Retours de terrain indépendants

| Source | Apport |
|---|---|
| **DevTools Daily** (~26/07) | workspace à deux, auto-hébergé sur VPS derrière Caddy, avec Codex, Copilot et agents Claude — consolidation réussie, passages de main agent-à-agent réels dans un même fil ; manque l'observabilité |
| **João Queirós** (23/07) | première évaluation approfondie ; origine de la formule sur l'autorisation par canal |
| **darrenjrobinson** | trois agents à identités distinctes dans un Buzz auto-hébergé, chacun avec sa keypair et sa propre facturation — *« qualitatively different from a bot integration »* |

Guides divers : les agents n'agissent que sur @mention ; sans instruction d'arrêt, deux agents peuvent boucler en réponses infinies ; l'onboarding hébergé a eu des bugs (issues #2484, #2367) rendant l'auto-hébergement plus fiable à ce stade.

### App mobile (Tom Brow, 29/07)

L'app n'héberge pas d'agents : elle **signe des messages** et se connecte directement aux relais ; l'identité vient du desktop par **appairage QR**, sans chemin d'identité autonome sur mobile. Vie privée : aucun SDK d'analytics, métadonnées **EXIF supprimées** avant upload, push selon un brouillon **NIP-PL** où les relais ne voient pas le device token et la gateway ne voit ni clés publiques, ni contenu, ni métadonnées, ni l'identité du relais. Modèle de référence pour concevoir du push sans fuite de métadonnées.

### Ce qui manque pour un usage en production

Aucun prix publié pour l'hébergement géré, aucun chiffre d'adoption entreprise, aucune autorisation fine par outil, aucune observabilité d'agent, binaires Windows non signés, docs éparses, UI de forge Git précoce. Block l'écrit : *« rough edges and giant chasms »*. Les trois seuils de réévaluation proposés : évaluer en auto-hébergé sur un projet non critique si l'équipe est déjà *agent-heavy* ; attendre l'autorisation fine par outil et l'observabilité avant toute production ; réévaluer à la publication d'un prix d'hébergement et d'une v1.0.

### Comment se servir de cette fiche

Elle est le **dossier de contexte** ; les sources primaires sont ailleurs. Pour la thèse et le modèle d'identité → [[longwell-block-buzz-workspace-agents-nostr-2026-07-21]]. Le dossier vieillit vite : releases tous les quelques jours, métriques GitHub en mouvement, statuts datés de mi-août 2026. À noter : pour aider à quitter GitHub, Buzz héberge son code sur GitHub.

## RésuméDe400mots

Rapport de recherche interne du **12 août 2026** consolidant l'état public de **Buzz**, le workspace humains+agents de **Block** lancé le **21 juillet 2026** sous **Apache 2.0**, en vue d'une présentation. Il agrège les deux billets d'ingénierie de Block, l'annonce corporate, le dépôt GitHub, la presse, X et **trois évaluations indépendantes** — cette dernière couche portant l'essentiel de la valeur ajoutée.

**Le concept.** Buzz fusionne chat d'équipe, forge Git et workflows automatisés en un seul espace où les agents sont **des membres à part entière, pas des bots**. La thèse est celle de Tyler Longwell : *« The bottleneck moved from intelligence to coordination. »* Bradley Axen (Head of AI Capabilities) en donne l'enjeu de marché : *« Every company is going to need a place where humans and agents work together. The question is whether that place is proprietary or open. »*

**L'architecture.** Relais **Rust** sur **Nostr** (NIP-01/42/98/34, 127 *event kinds*), **Postgres**, **Redis**, **S3/MinIO**, desktop **Tauri+React**. Chaque participant détient une paire de clés ; chaque message, revue, étape de workflow et événement Git est **signé** dans un journal d'audit append-only à chaîne de hash. Un formalisme rare pour une **v0.4.x/0.5.x** : isolation multi-tenant mécanisée en **TLA+**, propriétés d'autorisation vérifiées en **Tamarin**. L'intégration agent passe par **`buzz-acp`**, harnais **ACP** qui branche goose, Codex et Claude Code et **traduit ACP ↔ MCP** — *« They compose through protocols, not imports. »*

**L'écart central.** Jack Dorsey annonce *« decentralized, self-sovereign »* ; l'`ARCHITECTURE.md` de Block dit : *« The relay is the single source of truth… There is no peer-to-peer event exchange, no gossip, no replication. »* Un relais unique par communauté, donc un **point de défaillance unique** : la décentralisation est une **souveraineté organisationnelle**, pas une redondance.

**Les limites, documentées.** L'unité de permission est **l'appartenance au canal** — *« channel membership is not fine-grained tool authorization »* ; les agents tournent en **`--dangerously-skip-permissions`**, hors bac à sable ; **l'observabilité manque** (*« It doesn't tell me what happens next »*, kills OOM silencieux). Les événements signés sont *tamper-evident*, pas *tamper-resistant* : un opérateur de relais compromis peut supprimer. Sur le relais hébergé, **pas de chiffrement de bout en bout**.

**Précision de chiffre.** Le « +33 % de travail » est le **ratio de tâches terminées (20 vs 15 sur 44)**, pas un gain de score — lequel passe de 59,1 % à 71,5 %, soit **+12,4 pts**.

**Réception** : ~25 900 étoiles GitHub, tweet Dorsey à ~2,3-2,7 M vues, soutien de Sundar Pichai, et la formule de Justin Waldron : *« the first proper multiplayer agent harness »*. Caveats assumés : benchmarks **auto-évalués par Block**, aucun prix d'hébergement, aucun chiffre d'adoption.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Block | ORGANISATION | publie | Buzz | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | est_instance_de | workspace collaboratif humains-agents auto-hébergeable | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Jack Dorsey | PERSONNE | affirme_que | Buzz est model-agnostic, décentralisé, self-sovereign et open source, et vise à réduire la dépendance de Block à Slack et GitHub | CITATION | 0.95 | STATIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | s_oppose_à | la qualification de décentralisé au sens réseau : l'architecture officielle pose le relais comme source unique de vérité, sans échange pair-à-pair, sans gossip et sans réplication | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | permet | une souveraineté organisationnelle par auto-hébergement et identité portable, et non une redondance réseau | AFFIRMATION | 0.94 | ATEMPOREL | inféré |
| relais unique | CONCEPT | s_oppose_à | la disponibilité du workspace, dont il constitue le point de défaillance unique | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | utilise | Nostr | TECHNOLOGIE | 0.97 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | utilise | un relais écrit en Rust avec Postgres pour les événements et la recherche, Redis pour la présence et le pub/sub, et un stockage objet S3 ou MinIO pour les médias | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |
| Block | ORGANISATION | utilise | TLA+ | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| Block | ORGANISATION | utilise | Tamarin | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Tamarin | TECHNOLOGIE | permet | de vérifier les propriétés d'autorisation de Buzz, ce qui est inhabituel pour un logiciel encore en version 0.5.x | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | s_oppose_à | l'autorisation fine par outil : l'appartenance au canal reste l'unité de permission, un agent dans un canal pouvant faire ce que font les membres | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |
| João Queirós | PERSONNE | affirme_que | l'appartenance à un canal n'est pas une autorisation fine par outil | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | utilise | un lancement en --dangerously-skip-permissions, hors bac à sable, sur la machine d'un humain | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Block | ORGANISATION | affirme_que | l'agent peut tout faire, et la sécurité repose entièrement sur la restriction de qui peut lui donner des instructions | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | s_oppose_à | l'observabilité de l'activité des agents : le workspace signale qu'un agent a reçu un message mais pas ce qu'il en fait, des agents ayant subi des kills OOM silencieux | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| journal d'audit signé | CONCEPT | permet | de prouver qui a fait quoi, sans empêcher un opérateur de relais compromis de supprimer des événements | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| relais hébergé par Block | TECHNOLOGIE | s_oppose_à | le chiffrement de bout en bout des messages, les fournisseurs de modèles pouvant recevoir prompts et contenus de canal | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| buzz-acp | TECHNOLOGIE | utilise | Agent Client Protocol | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| buzz-acp | TECHNOLOGIE | permet | de brancher goose, Codex et Claude Code dans Buzz en traduisant entre ACP côté agent et MCP côté outils | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |
| buzz-agent | TECHNOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| buzz-agent | TECHNOLOGIE | permet | jusqu'à huit sessions concurrentes disposant chacune de ses serveurs MCP, de son historique et de son contexte, contre l'API Anthropic Messages, OpenRouter ou tout endpoint compatible OpenAI | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Block | ORGANISATION | affirme_que | l'agent ignore à quel serveur MCP il parle et le serveur MCP ignore quel agent l'appelle : ils se composent par des protocoles, pas par des imports | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| goose | TECHNOLOGIE | est_basé_sur | le programme open source de Block lancé le 28 janvier 2025, ancêtre conceptuel de Buzz | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| goose | TECHNOLOGIE | fait_partie_de | Agentic AI Foundation | ORGANISATION | 0.93 | DYNAMIQUE | déclaré_article |
| Bradley Axen | PERSONNE | affirme_que | toute entreprise aura besoin d'un lieu où humains et agents travaillent ensemble, et la question est de savoir si ce lieu est propriétaire ou ouvert | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Bradley Axen | PERSONNE | travaille_chez | Block | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | concurrence | Slack | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | concurrence | GitHub | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Justin Waldron | PERSONNE | affirme_que | Buzz n'est pas un tueur de Slack mais le premier véritable harnais d'agents multijoueur | CITATION | 0.9 | ATEMPOREL | déclaré_article |
| Deep Research Veille Interne | ORGANISATION | mesure | le gain de 33 % annoncé par Block correspond au ratio de tâches terminées, vingt contre quinze sur quarante-quatre, et non au score qui progresse de 59,1 % à 71,5 % | MESURE | 0.93 | STATIQUE | inféré |
| Deep Research Veille Interne | ORGANISATION | affirme_que | les benchmarks disponibles sur Buzz proviennent d'une auto-évaluation de Block sur son propre dispositif, sans mesure indépendante | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | s_oppose_à | un usage en production tant que l'autorisation fine par outil et l'observabilité des agents ne sont pas livrées | AFFIRMATION | 0.9 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Buzz | TECHNOLOGIE | architecture | Relais Nostr écrit en Rust (Axum WS + REST) sous Apache 2.0, avec Postgres pour les événements et la recherche plein texte, Redis pour pub/sub, présence et saisie, stockage objet S3/MinIO pour les médias via Blossom, client desktop Tauri + React ; 127 event kinds, NIP-01, NIP-42, NIP-98, NIP-34 | AJOUT |
| Buzz | TECHNOLOGIE | décentralisation | L'ARCHITECTURE.md pose le relais comme source unique de vérité, sans échange pair-à-pair, sans gossip ni réplication : un relais autoritaire par communauté, donc un point de défaillance unique. La décentralisation revendiquée est une souveraineté organisationnelle (auto-hébergement + identité portable), pas une redondance réseau | AJOUT |
| Buzz | TECHNOLOGIE | limites de sécurité | Autorisation à la maille du canal et non par outil ou action ; agents lancés en --dangerously-skip-permissions hors bac à sable ; pas d'observabilité de l'activité des agents ; journal signé tamper-evident mais non tamper-resistant ; messages non chiffrés de bout en bout sur le relais hébergé | AJOUT |
| Buzz | TECHNOLOGIE | maturité | Version 0.4.21 ou 0.4.22 au lancement selon les sources, puis 0.5.x ; dépôt créé le 6 mars 2026, premières releases publiques le 3 mai 2026, lancement public le 21 juillet 2026. Environ 25 900 étoiles GitHub à la mi-août 2026. Binaires Windows non signés, docs éparses, UI de forge Git précoce ; aucun prix publié pour l'hébergement géré | AJOUT |
| Buzz | TECHNOLOGIE | vérification formelle | Spécification d'isolation multi-tenant mécanisée en TLA+, propriétés d'autorisation vérifiées en Tamarin, protocole de stockage Git model-checké — niveau de formalisme inhabituel pour une version 0.x, mais portant sur l'identité et le stockage, non sur l'autorisation d'outil | AJOUT |
| buzz-acp | TECHNOLOGIE | définition | Harnais Agent Client Protocol inclus dans le monorepo Buzz, qui branche goose, Codex et Claude Code et traduit entre ACP côté client/agent et MCP côté outils | AJOUT |
| buzz-agent | TECHNOLOGIE | définition | Agent ACP maison de Block : parle ACP sur stdio, appelle un LLM et utilise des outils MCP ; jusqu'à huit sessions concurrentes avec serveurs MCP, historique et contexte propres ; compatible API Anthropic Messages, OpenRouter et tout endpoint compatible OpenAI (vLLM, llama.cpp, Databricks, Ollama) | AJOUT |
| Nostr | TECHNOLOGIE | usage dans Buzz | Substrat de Buzz : NIP-01 pour le format de fil, NIP-42 pour l'authentification de connexion, NIP-98 pour l'authentification REST, NIP-34 pour les événements Git, et un brouillon NIP-PL pour un push mobile où ni le relais, ni la gateway, ni Apple/Google ne voient device token, clés publiques, contenu ou métadonnées | MISE_A_JOUR |
| Tamarin | TECHNOLOGIE | définition | Outil de vérification formelle de protocoles cryptographiques, employé par Block pour vérifier les propriétés d'autorisation de Buzz | AJOUT |
| goose | TECHNOLOGIE | généalogie | Framework d'agent open source de Block lancé le 28 janvier 2025 sous Apache 2.0 par son Open Source Program Office, contribué en décembre 2025 à l'Agentic AI Foundation de la Linux Foundation aux côtés de MCP et d'AGENTS.md ; ancêtre conceptuel de Buzz, plus de 27 000 étoiles et 350 contributeurs | MISE_A_JOUR |
| Bradley Axen | PERSONNE | rôle | Head of AI Capabilities chez Block ; porte l'argument de marché du lancement de Buzz : toute entreprise aura besoin d'un lieu où humains et agents travaillent ensemble, et la question est de savoir s'il sera propriétaire ou ouvert | AJOUT |
| Tom Brow | PERSONNE | rôle | Ingénieur chez Block, auteur du billet « A Buzz on your phone » (29 juillet 2026) sur l'application mobile : pas d'hébergement d'agents, signature des messages, appairage QR depuis le desktop, aucun SDK d'analytics et suppression des métadonnées EXIF | AJOUT |
| João Queirós | PERSONNE | rôle | Auteur de la première évaluation indépendante approfondie de Buzz (23 juillet 2026), d'où vient la formule reprise partout : l'appartenance à un canal n'est pas une autorisation fine par outil | AJOUT |
| Deep Research Veille Interne | ORGANISATION | rôle | Auteur du rapport de veille interne du 12 août 2026 consolidant l'état public de Buzz en vue d'une présentation : billets d'ingénierie de Block, annonce corporate, dépôt GitHub, presse, X et trois évaluations indépendantes, avec sourçage explicite, distinction des URL vérifiées et section Caveats sur l'auto-évaluation des benchmarks | AJOUT |
