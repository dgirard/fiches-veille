---
themes: [agents-codage-ia-skills, architecture-construction, outils-plateformes]
source: "agentclientprotocol.com"
---
# agentclientprotocol-introduction-2026-08-02

## Veille

Page d'entrée de la **spécification officielle** de l'**Agent Client Protocol (ACP)** (`agentclientprotocol.com/get-started/introduction`), consultée le **2 août 2026**. Ce n'est pas un article daté mais un **artefact vivant** : la fiche est datée de son observation, pas d'une publication. **Énoncé de mission en une phrase** : *« The Agent Client Protocol (ACP) standardizes communication between code editors/IDEs and coding agents and is suitable for both local and remote scenarios. »* **Le problème posé** tient en trois lignes : agents de codage et éditeurs sont **étroitement couplés** et *« interoperability isn't the default »* — chaque éditeur doit construire une intégration sur mesure par agent, chaque agent doit implémenter des API spécifiques à chaque éditeur. Trois conséquences nommées : **integration overhead** (chaque paire agent-éditeur demande du travail sur mesure), **limited compatibility** (un agent ne touche qu'un sous-ensemble d'éditeurs), **developer lock-in** (*« choosing an agent often means accepting their available interfaces »*). **La solution est explicitement calquée sur LSP** — *« similar to how the Language Server Protocol (LSP) standardized language server integration »* — avec le bénéfice réciproque : un agent qui parle ACP fonctionne avec **tout** éditeur compatible, un éditeur qui supporte ACP gagne accès à **tout** l'écosystème d'agents ACP. **Deux modes de déploiement, et c'est le point le plus sous-estimé** : les agents **locaux** tournent en sous-processus de l'éditeur en **JSON-RPC sur stdio**, mais les agents **distants** sont prévus en **HTTP ou WebSocket** — support déclaré *« work in progress »*, avec une collaboration en cours avec des plateformes agentiques. **Filiation technique avec MCP, plus forte qu'une simple complémentarité** : ACP *« re-uses the JSON representations used in MCP where possible »*, en ajoutant des types propres aux besoins d'UX du codage agentique (l'affichage de **diffs** est l'exemple donné) ; le format par défaut du texte lisible est le **Markdown**, choisi pour ne pas exiger que l'éditeur sache rendre du HTML. **Deux constats de gouvernance et de versionnement** relevés sur la page et non dans le discours ambiant : la navigation expose **v1 (Latest)** et **v2 (Draft)** — et **non un « ACP 1.2 »** —, et la barre de navigation lie **Zed Industries *et* JetBrains** côte à côte, aux côtés d'un **ACP Registry**, de **RFDs**, d'une section **Community**, de **Publications**, d'**Updates** et d'une page **Brand**. Bibliothèques officielles annoncées : **Kotlin, Java, Python, Rust, TypeScript**, plus un volet communautaire.

## Titre Article

Agent Client Protocol — Introduction

## Date

2026-08-02

## URL

https://agentclientprotocol.com/get-started/introduction

## Keywords

Agent Client Protocol, ACP, protocole ouvert, spécification, interopérabilité, découplage éditeur agent, LSP, Language Server Protocol, JSON-RPC, stdio, sous-processus, agents locaux, agents distants, HTTP, WebSocket, work in progress, MCP, Model Context Protocol, réutilisation des représentations JSON, types personnalisés, affichage de diffs, Markdown, integration overhead, limited compatibility, developer lock-in, verrouillage développeur, N+M, écosystème d'agents, Zed Industries, JetBrains, ACP Registry, registre d'agents, RFD, request for discussion, gouvernance de protocole, v1 latest, v2 draft, versionnement de spécification, bibliothèques clientes, Kotlin, Java, Python, Rust, TypeScript, Mintlify, documentation vivante, llms.txt

## Authors

**Projet Agent Client Protocol** — spécification collective, sans signature individuelle sur cette page. La barre de navigation du site lie deux organisations au même niveau : **Zed Industries** (à l'origine du protocole) et **JetBrains**. La présence d'une section **RFDs** (*requests for discussion*), d'une page **Community** et d'un **ACP Registry** indique une structure de gouvernance ouverte plutôt qu'une documentation produit.

Documentation construite et hébergée sur **Mintlify**. La page expose un `llms.txt` en tête (*« Fetch the complete documentation index at: /llms.txt — Use this file to discover all available pages before exploring further »*) : le site est explicitement outillé pour être lu par des agents.

## Ton

**Profil** : page d'introduction de **spécification technique ouverte**, registre *standards body* plutôt que marketing produit. Très courte — deux sections (`Why ACP?`, `Overview`) — et entièrement construite pour être citée.

**Style** : la forme canonique du protocole ouvert, en trois temps mécaniques : (1) **nommer le couplage** existant, (2) **énumérer ses coûts** en trois puces symétriques, (3) **poser l'analogie légitimante**. L'analogie LSP fait tout le travail rhétorique : elle transporte un précédent que le lecteur a déjà accepté (LSP a bel et bien découplé éditeurs et langages) vers un domaine où la démonstration reste à faire. Économie de moyens remarquable — aucune promesse chiffrée, aucun bénéfice business, aucune mention de concurrent.

Deux marqueurs de sobriété qui inspirent confiance : l'aveu que le support des agents distants est *« a work in progress »*, et la justification **par la contrainte** du choix de Markdown (*« without requiring that the code editor is capable of rendering HTML »*) — on explique une décision de conception par ce qu'elle **n'impose pas** à l'implémenteur, ce qui est le bon réflexe d'un protocole qui cherche des adoptants.

**Formules-marqueurs** : *« interoperability isn't the default »*, *« Every new agent-editor combination requires custom work »*, *« choosing an agent often means accepting their available interfaces »*, *« Agents that implement ACP work with any compatible editor »*, *« This decoupling allows both sides to innovate independently »*.

## Pense-betes

- **La phrase à retenir** : *« AI coding agents and editors are tightly coupled but interoperability isn't the default. »* Tout le protocole découle de ce constat.

- **Les trois coûts du couplage** (structure à réutiliser telle quelle en présentation) : **integration overhead** — chaque combinaison agent×éditeur demande du travail sur mesure ; **limited compatibility** — un agent ne touche qu'un sous-ensemble d'éditeurs ; **developer lock-in** — choisir un agent revient à accepter ses interfaces. Les trois sont des coûts **différents** (production, diffusion, liberté), pas trois formulations du même.

- **L'analogie LSP fait le travail** : *« similar to how the Language Server Protocol standardized language server integration »*. Elle est efficace parce que le précédent est acquis. Mais elle est aussi **l'endroit où il faut être prudent** : LSP normalise un échange **largement déterministe** (positions, symboles, diagnostics) ; ACP normalise l'interface d'un agent **non déterministe**, qui négocie des permissions, produit des diffs, et dont le comportement varie d'une exécution à l'autre. La forme du problème est la même ; la nature de ce qui transite ne l'est pas. La page ne discute pas cet écart.

- **Deux modes de transport, pas un** — le point le plus sous-estimé dans les reprises :
  - **Agents locaux** : sous-processus de l'éditeur, **JSON-RPC sur stdio**. C'est le mode connu, celui que tout le monde cite.
  - **Agents distants** : hébergés en cloud ou sur infrastructure séparée, **HTTP ou WebSocket**. Déclaré *« work in progress »*, avec collaboration active avec des plateformes agentiques.
  → **Conséquence** : ACP n'est pas structurellement un protocole « poste de travail ». Sa trajectoire vise l'agent hébergé, donc l'entreprise. Résumer ACP à « du JSON-RPC sur stdio » décrit son présent, pas sa cible.

- **La relation à MCP est une filiation, pas une simple complémentarité** : *« The protocol re-uses the JSON representations used in MCP where possible. »* On dit couramment que « ACP et MCP s'empilent » (le client parle ACP à l'agent, l'agent parle MCP à ses outils) — c'est vrai côté architecture, mais **incomplet** : ACP **emprunte les structures de données de MCP**. Les deux protocoles ne sont pas seulement voisins, ils partagent un vocabulaire de sérialisation. Cf. [[girard-acp-deux-protocoles-un-sigle-2026-08-02]] pour la distinction fonctionnelle.

- **Les extensions propres au codage agentique** : ACP ajoute *« custom types for useful agentic coding UX elements, like displaying diffs »*. C'est ce qui justifie qu'ACP existe **en plus** de MCP : un diff à valider n'est pas un appel d'outil, c'est un élément d'interface qui demande une décision humaine. **Le protocole encode le moment de la revue**, pas seulement l'exécution.

- **Markdown par défaut, et la raison donnée** : *« which allows enough flexibility to represent rich formatting without requiring that the code editor is capable of rendering HTML »*. Décision de conception justifiée par la **charge qu'elle épargne à l'implémenteur** — le bon réflexe pour un protocole qui cherche l'adoption. À noter pour qui conçoit un protocole : on baisse le coût d'entrée du côté qu'on veut recruter.

- **Correction de versionnement** : la navigation de la spécification expose **`v1` (Latest)** et **`v2` (Draft)**. Elle n'expose **pas** de « ACP 1.2 ». Ce numéro, qui circule dans les reprises (et qui était consigné comme non vérifié dans [[girard-acp-deux-protocoles-un-sigle-2026-08-02]]), **n'est pas corroboré par la source primaire**. Citer **v1 / v2 draft**.

- **Correction de gouvernance** : la formule « Zed a lancé puis laissé partir » est trop forte. La barre de navigation lie **Zed Industries et JetBrains au même niveau**, et la structure du site (**ACP Registry**, **RFDs**, **Community**, **Publications**, **Updates**, **Brand**) est celle d'un **projet co-gouverné doté d'un processus**, pas d'un protocole orphelin ni d'une doc produit. La bonne formulation : **ouverture et co-gouvernance réelles, dépossession non**.

- **Signal d'écosystème** : bibliothèques officielles en **Kotlin, Java, Python, Rust, TypeScript** + volet communautaire. Le couple **Kotlin/Java** est le marqueur JetBrains — la présence des deux dit que l'implémentation IDE JVM est de première classe, pas un portage tardif.

- **Détail qui en dit long** : la page s'ouvre sur un pointeur vers **`/llms.txt`** — *« Use this file to discover all available pages before exploring further »*. La documentation d'un protocole pour agents est elle-même **outillée pour les agents**. Cohérence du dispositif, et signal faible sur ce que devient la doc technique.

- **Ce que la page ne dit pas** (à ne pas combler par inférence) : aucune date, aucun numéro de version en clair dans le corps, **aucune licence affichée sur cette page**, aucun modèle de gouvernance formalisé, aucune liste d'implémenteurs. La licence Apache-2.0 souvent citée pour ACP provient du dépôt, **pas de cette page**.

- **Méta / à relier** : source primaire des affirmations sur ACP #1 dans [[girard-acp-deux-protocoles-un-sigle-2026-08-02]] (qu'elle corrige sur le versionnement et nuance sur la gouvernance) ; à lire avec [[dethlefsen-zed-anthropic-subscription-changes-2026-05-14]], qui montre ce que l'optionalité promise ici vaut le jour où un fournisseur change ses prix ; le découplage décrit rejoint le contrat de portabilité analysé dans janakiram-agent-platform-portability-contract-2026-07-20 ; implémentation de référence côté produit dans block-goose-mcp-ui-future-agentic-interfaces-2025-08-25.
  **Désambiguïsation obligatoire** : « ACP » désigne ici **Agent Client Protocol** uniquement. Ne jamais typer le sigle comme entité — voir `docs/solutions/conventions/sigles-jamais-entites-graphe.md`.

## RésuméDe400mots

Page d'introduction de la spécification de l'**Agent Client Protocol**, consultée le 2 août 2026. Artefact vivant sans date de publication : la fiche est datée de son observation.

**Le problème.** *« AI coding agents and editors are tightly coupled but interoperability isn't the default. »* Chaque éditeur doit bâtir une intégration sur mesure pour chaque agent qu'il veut supporter, et chaque agent doit implémenter les API propres à chaque éditeur. Trois coûts distincts en découlent : l'**integration overhead** (toute combinaison agent-éditeur demande du travail spécifique), la **limited compatibility** (un agent n'atteint qu'une fraction des éditeurs), et le **developer lock-in** — *« choosing an agent often means accepting their available interfaces »*.

**La solution.** ACP normalise la communication agent-éditeur *« similar to how the Language Server Protocol (LSP) standardized language server integration »*. Le bénéfice est réciproque et c'est ce qui fait tenir l'écosystème : un agent qui implémente ACP fonctionne avec n'importe quel éditeur compatible ; un éditeur qui supporte ACP accède à tout l'écosystème d'agents ACP. *« This decoupling allows both sides to innovate independently. »*

**L'architecture.** ACP suppose que l'utilisateur est **principalement dans son éditeur** et va y chercher un agent pour une tâche précise. Deux modes de déploiement : les agents **locaux** tournent en sous-processus de l'éditeur et communiquent en **JSON-RPC sur stdio** ; les agents **distants**, hébergés en cloud ou sur infrastructure séparée, communiquent en **HTTP ou WebSocket** — support déclaré *« a work in progress »*, avec une collaboration active avec des plateformes agentiques. Le second mode est régulièrement omis dans les reprises, alors qu'il dessine la trajectoire entreprise du protocole.

**Le lien à MCP** est plus étroit qu'une complémentarité d'architecture : ACP *« re-uses the JSON representations used in MCP where possible »*, tout en ajoutant des types propres à l'UX du codage agentique — l'**affichage de diffs** est l'exemple donné. Le format par défaut du texte lisible est le **Markdown**, choisi précisément pour ne pas exiger de l'éditeur qu'il sache rendre du HTML.

**Deux constats sur la source elle-même.** La navigation expose **v1 (Latest)** et **v2 (Draft)** — et non le « ACP 1.2 » qui circule. Et elle lie **Zed Industries et JetBrains au même niveau**, à côté d'un **ACP Registry**, de **RFDs**, d'une section Community, de Publications, d'Updates et d'une page Brand : la structure d'un projet co-gouverné doté d'un processus. Bibliothèques officielles en Kotlin, Java, Python, Rust et TypeScript.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Agent Client Protocol | TECHNOLOGIE | permet | de standardiser la communication entre éditeurs de code et agents de codage | AFFIRMATION | 0.98 | ATEMPOREL | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | s_inspire_de | Language Server Protocol | TECHNOLOGIE | 0.96 | ATEMPOREL | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | résout | le couplage étroit entre agents de codage et éditeurs | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| couplage agent-éditeur | CONCEPT | s_oppose_à | l'interopérabilité par défaut | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | réduit | l'integration overhead, la compatibilité limitée et le verrouillage développeur | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | utilise | JSON-RPC sur stdio | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | utilise | HTTP ou WebSocket pour les agents distants | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | est_basé_sur | les représentations JSON de Model Context Protocol | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | utilise | Markdown | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | permet | l'affichage de diffs et autres éléments d'UX propres au codage agentique | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Zed Industries | ORGANISATION | a_créé | Agent Client Protocol | TECHNOLOGIE | 0.9 | STATIQUE | inféré |
| JetBrains | ORGANISATION | collabore_avec | Zed Industries | ORGANISATION | 0.88 | DYNAMIQUE | inféré |
| Agent Client Protocol | TECHNOLOGIE | publie | une spécification versionnée v1 (Latest) et v2 (Draft) | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| ACP Registry | TECHNOLOGIE | fait_partie_de | Agent Client Protocol | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | affirme_que | le support complet des agents distants est encore un travail en cours | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Agent Client Protocol | TECHNOLOGIE | spécification | Deux modes de transport : agents locaux en JSON-RPC sur stdio, agents distants en HTTP ou WebSocket (support en cours) ; réutilise les représentations JSON de MCP ; Markdown par défaut ; versions v1 (Latest) et v2 (Draft) | MISE_A_JOUR |
| Agent Client Protocol | TECHNOLOGIE | gouvernance | Site liant Zed Industries et JetBrains au même niveau, avec ACP Registry, RFDs, Community, Publications, Updates et Brand ; bibliothèques Kotlin, Java, Python, Rust, TypeScript | AJOUT |
| ACP Registry | TECHNOLOGIE | définition | Registre d'agents du projet Agent Client Protocol, permettant à un agent enregistré d'être découvert par tout client compatible | AJOUT |
| Language Server Protocol | TECHNOLOGIE | rôle | Précédent revendiqué par ACP : a découplé serveurs de langage et éditeurs, ACP vise le même découplage pour les agents | MISE_A_JOUR |
| verrouillage développeur | CONCEPT | définition | Situation où choisir un agent de codage revient à accepter les seules interfaces qu'il propose — l'un des trois coûts du couplage agent-éditeur | AJOUT |
