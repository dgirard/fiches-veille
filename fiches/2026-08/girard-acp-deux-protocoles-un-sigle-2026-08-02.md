---
themes: [agents-codage-ia-skills, architecture-construction, outils-plateformes]
source: "Didier Girard"
---
# girard-acp-deux-protocoles-un-sigle-2026-08-02

## Veille

Note de veille de **Didier Girard** datée du **2 août 2026**, partie d'une question de collègue (« c'est quoi ACP ? ») pour traiter un problème qui n'est pas terminologique mais **documentaire**. **Trois protocoles se disputent le sigle**, sans aucune intersection technique : **Agent Client Protocol** (client ↔ agent — Zed, août 2025, JSON-RPC 2.0 sur stdio, Apache-2.0, « ce que LSP a fait pour les langages »), **Agentic Commerce Protocol** (agent ↔ commerçant — OpenAI + Stripe, 29 sept. 2025, face à l'**UCP** de Google du 11 janv. 2026 adossé à **AP2**), et **Agent Communication Protocol** (agent ↔ agent — IBM Research / BeeAI, marginal mais polluant les recherches). **Le cœur de la note n'est pas le démêlage mais son échec constaté** : l'auteur cherche « ACP » dans sa base de connaissances de veille et obtient **douze résultats, tous sur le protocole de commerce, zéro sur celui de Zed** — *« nos agents de veille avaient indexé le sigle sans le désambiguïser »*. D'où une règle d'ingénierie de la connaissance : ***« on n'indexe jamais un sigle seul »*** — l'entité est « Agent Client Protocol », « ACP » n'est **qu'un alias**, porté par trois entités distinctes. Suit une clarification structurante (**MCP relie un agent à ses outils, ACP relie un client à un agent ; les deux s'empilent**) puis le cas d'école : **Buzz**, publié par **Block** le 21 juillet 2026 sous Apache-2.0 — espace de travail auto-hébergeable bâti sur **Nostr**, où chaque participant humain ou agent est une **paire de clés** et chaque message, étape de workflow ou push git un **événement signé** dans un journal append-only. Architecture entièrement protocolaire (`buzz-acp` harnais ACP sur stdio, `buzz-agent` agent ACP appelant un LLM, `buzz-dev-mcp` serveur MCP shell + édition), d'où l'agnosticisme d'agents : **Goose, Claude Code et Codex** se branchent par le même harnais, et **Hermes** (Nous Research) s'y est raccordé sans que Block écrive une ligne — *« N+M au lieu de N×M, tenue en production »*. La note se clôt sur la question de l'**abonnement Claude** face aux agents tiers, avec une chronologie 2026 en cinq temps et une **règle de conception** qui vaut au-delà du cas : la ligne n'est pas juridique mais **architecturale** — ***« qui consomme, et pour le compte de qui »*** (un agent `owner-only` consomme votre abonnement pour vous ; un agent `anyone` dans un canal partagé fait passer les requêtes de vos collègues par votre compte). **Vérification menée sur ce corpus** : la thèse tient, et plus durement que ce que la note affirme — non seulement « Agent Client Protocol » y est **totalement absent**, mais le sigle nu `ACP` **est déjà typé comme entité** dans deux fiches, et la page KB `Agentic-Commerce-Protocol` **attribue déjà le protocole à Google** alors qu'il est d'OpenAI + Stripe. La collision décrite n'est pas un risque à venir : elle a **déjà produit une erreur d'attribution** dans le graphe.

## Titre Article

ACP : deux protocoles, un sigle, zéro rapport

## Date

2026-08-02

## URL

*Aucune URL — texte fourni directement par l'auteur, non publié au moment de la mise en fiche. Source archivée dans `raw-data/girard-acp-deux-protocoles-un-sigle-2026-08-02.md`.*

## Keywords

ACP, Agent Client Protocol, Agentic Commerce Protocol, Agent Communication Protocol, homonymie de sigle, désambiguïsation, collision documentaire, ingénierie de la connaissance, alias d'entité, entité nue, indexation, piège à doublon, Zed, JetBrains, LSP, Language Server Protocol, JSON-RPC 2.0, stdio, Apache-2.0, registre d'agents, spécification versionnée, gouvernance de protocole, N+M vs N×M, découplage éditeur agent, interopérabilité, portabilité d'agents, MCP, Model Context Protocol, empilement de protocoles, OpenAI, Stripe, UCP, Universal Commerce Protocol, AP2, Agent Payments Protocol, commerce agentique, IBM Research, BeeAI, Buzz, Block, Jack Dorsey, Goose, Codex, Claude Code, Hermes, Nous Research, Nostr, paire de clés, événement signé, journal append-only, auto-hébergement, souveraineté, substrat multi-agent, harnais, buzz-acp, buzz-agent, buzz-dev-mcp, abonnement Claude, Agent SDK, claude -p, OAuth, Consumer Terms, OpenClaw, crédits Agent SDK, clé API, usage ordinaire et individuel, owner-only, anyone, qui consomme pour le compte de qui

## Authors

**Didier Girard** — auteur de la note. Écrit ici depuis la position de **praticien de la veille outillée** : le déclencheur est une question de collègue, le matériau principal est le comportement observé de sa propre base de connaissances, et la conclusion est une **règle de curation** adoptée en interne. Le texte alterne donc deux voix — l'explicateur de protocoles et l'ingénieur de la connaissance qui constate un défaut chez lui et en tire une norme.

## Ton

**Profil** : note de clarification technique, registre **praticien**, format court et dense. Ni analyse de marché ni prise de position — un **démêlage utile** doublé d'un retour d'expérience méthodologique. Public : ingénieurs, architectes, et quiconque tient un corpus documentaire sur ces sujets.

**Style** : structure en **cinq mouvements** (les trois ACP → le vrai risque → ne pas confondre avec MCP → le cas Buzz → la question de l'abonnement), chacun autonome et citable séparément. Trois traits :

1. **L'ouverture par la question réelle** — *« Un collègue me demande cette semaine : "c'est quoi ACP ?" »*. Pas d'exposition abstraite : le problème est daté, incarné, et la réponse est annoncée comme piégée avant d'être donnée.
2. **L'aveu comme argument**. Le passage le plus fort de la note est celui où l'auteur **rapporte un échec de son propre outillage** (« douze résultats, tous sur le mauvais protocole »). C'est ce qui transforme une curiosité de vocabulaire en problème d'ingénierie — et ce qui donne son autorité à la règle qui suit. Registre rare : on publie rarement le trou dans son propre dispositif.
3. **La chute opérationnelle**. Chaque section se termine par quelque chose qu'on peut appliquer — la règle d'indexation, le tableau MCP/ACP, le drapeau `owner-only` vs `anyone`. Aucun développement n'est laissé sans traduction.

**Formules-marqueurs** : *« deux protocoles, un sigle, zéro rapport »*, *« question simple, réponse piégée »*, *« on n'indexe jamais un sigle seul »*, *« un piège à doublon parfait »*, *« Zed a lancé la chose, puis l'a laissée partir »*, *« N+M au lieu de N×M, tenue en production »*, *« la distinction n'est pas juridique, elle est architecturale »*, *« qui consomme, et pour le compte de qui »*, *« autant la trancher au moment de la conception plutôt qu'à la lecture des CGU »*.

**Position épistémique** : **prudente et sourcée**. L'auteur borne explicitement sa compétence sur la partie contractuelle et renvoie aux sources primaires plutôt qu'à son interprétation. Le texte donne sept liens pour un format court — densité de sourçage inhabituelle pour une note de ce calibre.

## Pense-betes

- **Le démêlage, à mémoriser une fois pour toutes** :
  | Sigle | Nom complet | Relie | Origine |
  |---|---|---|---|
  | ACP #1 | **Agent Client Protocol** | un **client** à un **agent** | Zed, août 2025 |
  | ACP #2 | **Agentic Commerce Protocol** | un **agent** à un **commerçant** | OpenAI + Stripe, 29 sept. 2025 |
  | ACP #3 | **Agent Communication Protocol** | un **agent** à un **agent** | IBM Research / BeeAI |
  → **Aucune intersection technique.** Et la ressemblance de surface est maximale (« protocole », « agents », « open source », « 2025-2026 »), ce qui fait précisément le piège.

- **L'analogie qui porte** : ACP #1 est à l'agent ce que **LSP** est au langage. Avant, N éditeurs × M agents = **N×M** intégrations sur mesure ; après, chacun parle le protocole et **N+M** suffit. C'est l'argument d'interopérabilité classique, et c'est le seul qui compte pour décider d'adopter.

- **MCP vs ACP — le tableau à réutiliser tel quel** : **MCP** relie un agent à ses **outils et données** ; **ACP** relie un **client** à un **agent**. **Ils s'empilent** : le client parle ACP à l'agent, l'agent parle MCP à ses outils. Confusion fréquente, dissipée en deux lignes.

- **La règle de curation — le vrai livrable de la note** : ***« on n'indexe jamais un sigle seul »***. L'entité canonique est le **nom complet** ; le sigle n'est qu'un **alias**, et un alias peut être porté par plusieurs entités. C'est directement applicable à ce dépôt — voir [`docs/reference/ontologie-kg.md`](docs/reference/ontologie-kg.md) (règles de désambiguïsation) et `scripts/entity_aliases.tsv`.

- **VÉRIFICATION MENÉE SUR CE CORPUS (2026-08-02) — la thèse tient, en pire** :
  1. *« Zéro sur le protocole de Zed »* → **confirmé exactement**. Au moment de la vérification, la chaîne « Agent Client Protocol » était **absente de `fiches/` et de `kb/`** ; « Zed » n'apparaissait que dans une fiche sans rapport ([[powered-by-claude-anthropic-partners-2025-07-09]]). **→ Lacune comblée le même jour** par [[agentclientprotocol-introduction-2026-08-02]] (source primaire), [[dethlefsen-zed-anthropic-subscription-changes-2026-05-14]] et [[sawers-thenewstack-anthropic-pause-agent-sdk-subscription-2026-06-16]].
  2. *« Douze résultats »* → **non reproductible au grep** : **3 fiches** contiennent le token `ACP` (thilen-opascope-ai-shopping-assistant-agentic-commerce-protocols-2026-02-10, marette-agentic-commerce-optimization-acp-ucp-2026-02-23, ragsdale-merit-open-agentic-commerce-protocols-2026-03-19), pour **32 occurrences**. Le « douze » vient vraisemblablement d'un moteur de recherche sémantique, pas d'un grep. **Le chiffre ne se vérifie pas ; la conclusion qualitative, si** — et c'est elle qui porte.
  3. **Le piège était déjà armé, pas seulement possible** : contrairement à la règle proposée, le sigle nu **`ACP` était typé comme entité** dans le graphe, sujet de triples dans deux fiches (thilen-opascope-ai-shopping-assistant-agentic-commerce-protocols-2026-02-10, ragsdale-merit-open-agentic-commerce-protocols-2026-03-19), à côté d'une variante `Agentic Commerce Protocol (ACP)` — soit **trois entités pour un même protocole**. Le jour où une fiche sur l'ACP de Zed aurait typé `ACP` en entité, les deux protocoles auraient fusionné en une seule page KB. **→ Corrigé le 2 août 2026** : les variantes ont été normalisées vers `Agentic Commerce Protocol`, et symétriquement pour `UCP` → `Universal Commerce Protocol` et `ACS` → `Agentic Commerce Suite`. La règle de la note n'était donc pas préventive ici : elle était **corrective**.
  4. **Défaut déjà matérialisé, et plus grave** : la page `kb/Agentic-Commerce-Protocol.md` porte l'attribut **« catégorie : Protocole commerce agentique **Google** »** et la relation **`Google a_créé → Agentic Commerce Protocol` (confiance 0,99)**. Or l'ACP est **OpenAI + Stripe** ; le protocole de Google est **UCP** (+ AP2). **La confusion que la note décrit entre deux ACP a déjà produit, dans ce corpus, une erreur d'attribution entre l'ACP d'OpenAI et le protocole de Google.** → **Correctif à passer sur les fiches sources** (le KB étant généré, il ne se corrige pas à la main).

- **Gouvernance d'ACP #1 — nuance à apporter** : la note écrit *« Zed a lancé la chose, puis l'a laissée partir »*. Le mouvement d'ouverture est **réel et vérifiable** (organisation propre, spécification versionnée, registre public, implémentation JetBrains). Mais les sources publiques décrivent plutôt une **gouvernance partagée Zed × JetBrains** — le registre d'agents a été **co-lancé** par les deux en **janvier 2026**, et ACP reste présenté côté Zed comme *son* standard ouvert et la fonctionnalité phare de Zed 1.0. **Ouverture, oui ; dépossession, non.** Nuance sans conséquence pour l'argument d'interopérabilité, mais à ne pas surjouer en prise de parole.
  **Détail infirmé depuis, par la source primaire** : le numéro **ACP 1.2** n'est pas corroboré — la navigation de la spécification expose **`v1` (Latest)** et **`v2` (Draft)**, cf. agentclientprotocol-introduction-2026-08-02. Citer **v1 / v2 draft**. L'URL de registre `cdn.agentclientprotocol.com/registry` reste non confirmée (les sources publiques pointent `agentclientprotocol.com/registry`).

- **Buzz — le cas concret, vérifié et exact** : publié par **Block** le **21 juillet 2026**, **Apache-2.0**, dépôt `github.com/block/buzz`. Espace de travail **auto-hébergeable** sur **Nostr** ; chaque participant humain ou agent est une **paire de clés** (Schnorr) ; chaque message, étape de workflow et push git est un **événement signé** dans un journal **append-only**. Trois briques protocolaires : **`buzz-acp`** (harnais traduisant les événements Buzz vers un agent, en ACP sur stdio), **`buzz-agent`** (agent ACP appelant un LLM et utilisant des outils MCP), **`buzz-dev-mcp`** (serveur MCP shell + édition de fichiers). **Trois harnais livrés d'origine : Goose (Block), Claude Code (Anthropic), Codex (OpenAI).** Relay auto-hébergeable — argument de **souveraineté des données** explicite chez Block.

- **Pourquoi Buzz est la bonne illustration** : ce n'est pas « un produit qui utilise ACP », c'est **la démonstration que le découplage tient**. Trois agents de trois éditeurs concurrents branchés par **le même harnais**, et un quatrième (**Hermes**, Nous Research) raccordé **sans que Block écrive une ligne**. La promesse N+M cesse d'être un argument d'architecture pour devenir un fait observable. *(Nuance : côté Hermes, la source publique cadre l'ajout comme un **mode serveur ACP** ouvrant Zed, JetBrains, Neovim et autres — le bénéfice pour Buzz est une conséquence d'ACP, pas une intégration ciblée. Ce qui **renforce** l'argument plutôt qu'il ne l'affaiblit.)*

- **La lecture d'architecture d'entreprise** : Buzz donne un **substrat multi-agent souverain, auditable, sans dépendance SaaS tierce** — journal signé, relay chez soi, identités cryptographiques. C'est une réponse possible à la question « où va vivre la collaboration humain-agent dans le SI ». À rapprocher de la convergence des plateformes d'agents des hyperscalers analysée dans janakiram-agent-platform-portability-contract-2026-07-20 : **Buzz est l'option auto-hébergée du même besoin de portabilité**.

- **Abonnement Claude et agents tiers — chronologie 2026 telle que rapportée** (**reprise des sources de la note, non revérifiée ici**) : 9 janv. blocage technique silencieux des tokens OAuth d'abonnement hors outils officiels → 17-20 févr. formalisation dans la doc et les Consumer Terms (épisode **OpenClaw**) → 4 avril application pleine → 13-14 mai annonce de **crédits Agent SDK séparés** (20 $ Pro / 100 $ Max 5x / 200 $ Max 20x) pour le 15 juin → **15 juin : changement suspendu le jour même de son entrée en vigueur**. **État rapporté au 2 août 2026** : l'Agent SDK, `claude -p` et les applications tierces bâties dessus **puisent dans les limites de l'abonnement** ; le crédit séparé **n'existe pas**. → **Cet état est daté par construction : le revérifier avant toute décision.**

- **La règle qui survivra aux CGU — la meilleure idée de la note** : la ligne tracée par Anthropic sépare l'usage **« ordinaire et individuel »** du **routage de requêtes d'autrui** via des identifiants Free/Pro/Max. Traduction : un agent en **`owner-only`** consomme **votre** abonnement **pour vous** — dans les clous ; un agent en **`anyone`** dans un canal partagé fait passer les requêtes de **vos collègues** par **votre compte** — hors des clous, et c'est le moment de basculer sur une **clé API facturée à l'usage**. **La distinction n'est pas juridique, elle est architecturale : *qui consomme, et pour le compte de qui*. À trancher à la conception, pas à la lecture des CGU.**
  **Rapprochement à faire** : c'est **exactement l'ambient authority** de valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20, transposée de l'autorisation à la facturation. Un agent qui hérite des permissions de son humain et agit pour le compte d'un tiers pose le même problème de frontière, qu'il s'agisse d'accéder à un document ou de consommer un quota. **La question « pour le compte de qui ? » est le même invariant dans les deux cas.**

- **Méta / à relier** : côté commerce, les trois fiches qui portent l'homonymie — ragsdale-merit-open-agentic-commerce-protocols-2026-03-19, marette-agentic-commerce-optimization-acp-ucp-2026-02-23, thilen-opascope-ai-shopping-assistant-agentic-commerce-protocols-2026-02-10 — plus nrf-2026-commerce-agentique-ucp-deep-research-2026-01-13 et google-agentic-commerce-ap2-payment-protocol-2025-09-16 sur le camp Google. Côté Block/Goose : block-goose-mcp-ui-future-agentic-interfaces-2025-08-25 et mcp-ui-future-agentic-interfaces-goose-2025-08-25. Sur la normalisation ouverte de la couche agent : openai-agentic-ai-foundation-linux-2025-12-09.
  **Consigne de graphe issue de cette fiche** : **ne jamais créer d'entité `ACP`**. Les trois entités canoniques sont **Agent Client Protocol**, **Agentic Commerce Protocol** et **Agent Communication Protocol** ; « ACP » ne doit apparaître que comme alias explicitement rattaché à l'une d'elles.

## RésuméDe400mots

Note de veille du **2 août 2026**, née d'une question de collègue — *« c'est quoi ACP ? »* — dont l'auteur montre qu'elle n'a pas de réponse simple : **trois protocoles se disputent le sigle**, sans la moindre intersection technique.

**Agent Client Protocol** relie **un client à un agent**. Introduit par **Zed** en août 2025, il fait pour les agents ce que **LSP** a fait pour les langages : il découple l'éditeur de l'agent. Avant, N éditeurs × M agents imposaient **N×M** intégrations sur mesure ; après, chacun parle le protocole et **N+M** suffit. JSON-RPC 2.0 sur stdio, Apache-2.0. La note souligne que le protocole a quitté l'orbite de son créateur — organisation propre, registre d'agents, spécification versionnée, implémentation JetBrains.

**Agentic Commerce Protocol** n'a rien à voir : il relie **un agent à un commerçant** (découverte, panier, paiement). Annoncé par **OpenAI et Stripe** le 29 septembre 2025, il fait face à l'**UCP** de **Google** (11 janvier 2026), adossé à **AP2** pour le paiement. Enjeu : la couche « Visa/Mastercard » du commerce agentique. **Agent Communication Protocol** (IBM Research / BeeAI), agent-à-agent, complète le tableau et pollue les recherches.

**Le problème constaté est documentaire.** L'auteur cherche « ACP » dans sa base de veille : **douze résultats, tous sur le protocole de commerce, zéro sur celui de Zed**. Les agents d'indexation avaient traité le sigle sans le désambiguïser. D'où la règle adoptée : ***« on n'indexe jamais un sigle seul »*** — l'entité est le nom complet, le sigle n'est qu'un **alias**, ici porté par trois entités distinctes. La note dissipe au passage une confusion voisine : **MCP** relie un agent à ses **outils**, **ACP** relie un **client** à un **agent**, et les deux **s'empilent**.

**Le cas concret est Buzz**, publié par **Block** le 21 juillet 2026 sous Apache-2.0 : un espace de travail auto-hébergeable sur **Nostr** où humains et agents partagent les mêmes canaux, chaque participant étant une **paire de clés** et chaque événement — message, étape de workflow, push git — étant **signé** dans un journal append-only. L'architecture agents est entièrement protocolaire (`buzz-acp`, `buzz-agent`, `buzz-dev-mcp`), d'où l'agnosticisme : **Goose, Claude Code et Codex** par le même harnais, et **Hermes** raccordé sans une ligne de code côté Block. *« N+M au lieu de N×M, tenue en production. »*

**La chute porte sur l'abonnement Claude** face aux agents tiers, après une année 2026 agitée (blocage OAuth, crédits séparés annoncés puis suspendus le jour de leur entrée en vigueur). La ligne retenue sépare l'usage **ordinaire et individuel** du **routage des requêtes d'autrui**. Sa formulation vaut au-delà du cas : *« la distinction n'est pas juridique, elle est architecturale : **qui consomme, et pour le compte de qui** »* — à trancher à la conception plutôt qu'à la lecture des CGU.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Didier Girard | PERSONNE | affirme_que | trois protocoles distincts se partagent le sigle ACP sans aucune intersection technique | AFFIRMATION | 0.97 | DYNAMIQUE | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | permet | de relier un client à un agent, en découplant l'éditeur de l'agent | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | s_inspire_de | Language Server Protocol | TECHNOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Zed | ORGANISATION | a_créé | Agent Client Protocol | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| JetBrains | ORGANISATION | utilise | Agent Client Protocol | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | utilise | JSON-RPC 2.0 sur stdio | TECHNOLOGIE | 0.94 | ATEMPOREL | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | réduit | le nombre d'intégrations de N×M à N+M | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Agentic Commerce Protocol | TECHNOLOGIE | permet | de relier un agent à un commerçant (découverte, panier, paiement) | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| OpenAI | ORGANISATION | a_créé | Agentic Commerce Protocol | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Stripe | ORGANISATION | a_créé | Agentic Commerce Protocol | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Universal Commerce Protocol | TECHNOLOGIE | concurrence | Agentic Commerce Protocol | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Universal Commerce Protocol | TECHNOLOGIE | utilise | Agent Payments Protocol | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Agent Communication Protocol | TECHNOLOGIE | permet | l'interopérabilité agent-à-agent | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | recommande | ne jamais indexer un sigle seul : l'entité est le nom complet, le sigle n'est qu'un alias | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| homonymie de sigle | CONCEPT | s_oppose_à | la qualité d'un corpus de veille indexé automatiquement | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Model Context Protocol | TECHNOLOGIE | s_applique_à | la liaison entre un agent et ses outils et données | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | converge_avec | Model Context Protocol | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | publie | Buzz | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | utilise | Nostr | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | utilise | Agent Client Protocol | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | permet | de brancher Goose, Claude Code et Codex par le même harnais | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | permet | un substrat multi-agent auto-hébergeable et auditable, sans dépendance SaaS tierce | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Nous Research | ORGANISATION | utilise | Agent Client Protocol | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Didier Girard | PERSONNE | affirme_que | la frontière entre usage individuel et routage de requêtes d'autrui est architecturale, pas juridique — qui consomme, et pour le compte de qui | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | les limites Pro et Max supposent un usage ordinaire et individuel de Claude Code et de l'Agent SDK | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | s_oppose_à | le routage de requêtes d'utilisateurs tiers via des identifiants Free, Pro ou Max | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Agent Client Protocol | TECHNOLOGIE | définition | Protocole ouvert reliant un client (éditeur) à un agent de codage ; JSON-RPC 2.0 sur stdio, Apache-2.0, introduit par Zed en août 2025 — le « LSP des agents ». Alias « ACP » (homonyme, à ne jamais employer seul) | AJOUT |
| Agentic Commerce Protocol | TECHNOLOGIE | correction | Protocole reliant un agent à un commerçant (découverte, panier, paiement), créé par **OpenAI et Stripe** le 29 septembre 2025 — et **non par Google**, dont le protocole concurrent est UCP. Alias « ACP » (homonyme) | MISE_A_JOUR |
| Agent Communication Protocol | TECHNOLOGIE | définition | Protocole d'interopérabilité agent-à-agent d'IBM Research / BeeAI ; troisième porteur du sigle ACP, marginal dans le débat mais polluant les recherches | AJOUT |
| homonymie de sigle | CONCEPT | définition | Défaut d'indexation où un acronyme porté par plusieurs entités distinctes est traité comme une entité unique, fusionnant des corpus sans intersection technique | AJOUT |
| règle du sigle jamais seul | CONCEPT | définition | Règle de curation : l'entité canonique est le nom complet, le sigle n'est qu'un alias rattaché explicitement à une entité — un même alias pouvant être porté par plusieurs entités | AJOUT |
| Buzz | TECHNOLOGIE | définition | Espace de travail auto-hébergeable de Block (21 juillet 2026, Apache-2.0) bâti sur Nostr, où humains et agents partagent les mêmes canaux ; chaque participant est une paire de clés, chaque événement est signé dans un journal append-only | AJOUT |
| buzz-acp | TECHNOLOGIE | rôle | Harnais traduisant les événements Buzz vers un agent, en ACP sur stdio — brique qui rend Buzz agnostique en agents | AJOUT |
| Nostr | TECHNOLOGIE | rôle | Protocole de messagerie ouvert et résistant à la censure, substrat d'identité et de journal signé de Buzz | AJOUT |
| Block | ORGANISATION | rôle | Éditeur de Goose (agent open source) et de Buzz ; publie sous Apache-2.0 avec relay auto-hébergeable | MISE_A_JOUR |
| Universal Commerce Protocol | TECHNOLOGIE | positionnement | Protocole de commerce agentique de Google (11 janvier 2026), adossé à AP2 pour le paiement — concurrent de l'Agentic Commerce Protocol d'OpenAI/Stripe | MISE_A_JOUR |
| Didier Girard | PERSONNE | rôle | Auteur de la note ; praticien de la veille outillée, tire une règle de curation d'un défaut constaté dans son propre corpus | AJOUT |
