---
themes: [outils-plateformes, agents-codage-ia-skills, produits-services, transformation-adoption]
source: "Block"
---
# block-berd-caractere-agents-open-source-2026-08-18

## Veille

Billet du blog corporate de **Block** (`block.xyz/inside`), non signé — l'auteur affiché est **« Block »** —, publié le **18 août 2026**, ~930 mots, qui annonce **l'ouverture du code de Berd**, l'application de bureau interne de Block pour travailler avec des agents, et expose la thèse de conception qui l'a guidée : donner du caractère aux agents *« not only through roles, instructions, skills, and tools, but through distinctive visual identities »* — d'où les personnages animés maison, les *« Gloopies »*. Le billet part d'un constat de fragmentation (*« The technology was powerful, but the experience around it was fragmented »*) et d'un problème d'interface nommé avec précision : *« the product gives people little sense of how the agent is configured, which context and tools are available to it, and how it differs from another agent »*. Deux apports structurants. **(A) Une articulation en trois étages** : **goose** reste le framework et le *runtime* qui tient la boucle d'agent ; **Berd** est le client de bureau (projets, contexte, sessions, agents, configuration) ; les deux communiquent par l'**Agent Client Protocol**. **Buzz** est désigné comme la suite, quand le travail solo devient collaboratif (*« Start alone, then go multiplayer »*). **(B) Six exigences léguées à Buzz**, énoncées comme bilan : *« private space, durable context, recognizable agent identities, reusable skills, visible configuration, and clearer visibility into an agent's configured context, tools, and capabilities »* — grille directement réutilisable pour évaluer un client d'agents. Le texte distingue lui-même identité et capacité : *« The avatars make the agent recognizable. Its role, skills, and tools make it useful. »* Aucun chiffre d'usage n'est produit et aucune licence n'est nommée pour l'ouverture de code.

## Titre Article

Designing AI with character: what we learned building Berd

## Date

2026-08-18

## URL

https://block.xyz/inside/designing-ai-with-character-what-we-learned-building-berd

## Keywords

Berd, Block, open source, ouverture de code, application de bureau, desktop application, agents IA, caractère, character, identité visuelle, visual identity, avatar, Gloopies, anthropomorphisme, lisibilité de la configuration, visible configuration, prompt box vide, empty prompt box, rôle compétences outils, roles skills tools, projets persistants, contexte durable, durable context, goose, harnais d'agent, agent harness, boucle d'agent, agent loop, runtime, Agent Client Protocol, ACP, client d'agents, Agentic AI Foundation, AAIF, Linux Foundation, MCP, AGENTS.md, Buzz, start alone then go multiplayer, Square, Cash App, design, blog corporate, auteur non signé

## Authors

**Aucun auteur nommé** : le billet est signé **« Block »** — le champ *Author* de la page porte le nom de l'entreprise. Publié le **18 août 2026** sur `block.xyz/inside`, le blog **corporate**, et non sur `engineering.block.xyz`.

## Ton

**Profil** : billet de marque en forme de retour d'expérience — ~930 mots, cinq sections courtes, ton posé et sans emphase. Public explicitement élargi au-delà des ingénieurs (*« assumed a level of technical fluency that many people did not have »*). Ni exposé de conception détaillé, ni benchmark, ni tribune : une intention de design racontée, doublée d'une annonce d'ouverture de code.

**Style** : les sections de bilan sont au passé (*« Berd gave our teams one desktop application »*, *« Berd showed us the importance of… »*), tandis que la description du produit reste au présent (*« Berd is a desktop application our teams use »*, *« Berd connects to goose »*) : le titre annonce un rétrospectif, la dernière section donne la suite à Buzz, et le produit n'est jamais déclaré déprécié. Registre du compte rendu tranquille — aucun superlatif, aucun chiffre. Six liens sortants, tous fonctionnels (`berd.xyz`, `github.com/block/berd`, `github.com/aaif-goose/goose`, `aaif.io`, `agents.md`, `buzz.xyz`), mais aucun vers une documentation, une architecture ou une spécification. L'argument d'autorité est un récit de filiation de marque : *« Square transformed payment hardware from something sellers hid behind the counter into something they could display proudly. Cash App brought personality and cultural relevance to personal finance. »*

**Formules-marqueurs** :
- ***« At Block, we often build the tools we need ourselves. »***
- ***« The technology was powerful, but the experience around it was fragmented. »***
- ***« we didn't need another model or agent harness, we needed a consistent environment around them »***
- ***« Many AI interfaces begin with an empty prompt box. »***
- ***« Different agents can look distinct because they are distinct. »***
- ***« The avatars make the agent recognizable. Its role, skills, and tools make it useful. »***
- ***« The goal was not to disguise the technology, but to make its capabilities more visible, approachable, and personal. »***
- ***« Start alone, then go multiplayer. »***

**Position épistémique** : intention de conception, documentée par des captures d'écran et une filiation de marque. Citable comme **doctrine de design de Block sur l'identité des agents** et comme source de l'**articulation Berd / goose / Buzz**. Aucune étude, aucun test utilisateur, aucune mesure d'adoption n'est produit : le billet n'établit pas que le caractère visuel améliore la compréhension d'un agent.

## Pense-betes

- **Date / source** : **18 août 2026**, blog **corporate** de Block (`block.xyz/inside`), billet **non signé**, ~930 mots. Annonce l'ouverture du code de **Berd** (`github.com/block/berd`), sans licence nommée.
- **Cadrage clé** : le problème posé est un problème de **lisibilité de la configuration** — *« how the agent is configured, which context and tools are available to it, and how it differs from another agent »* — et la réponse mise en avant est une **identité visuelle** (avatars animés, les *« Gloopies »*). Le billet distingue lui-même les deux registres : *« The avatars make the agent recognizable. Its role, skills, and tools make it useful. »* Un avatar rend un agent **distinguable**, pas **lisible**.

### L'articulation en trois étages

Verbatim : *« goose remains the open agent framework and runtime. Berd is a desktop application built around it. Berd connects to goose through the Agent Client Protocol. This separation lets Berd focus on the desktop experience, including projects, context, sessions, agents, and configuration, while goose handles the underlying agent loop. »*

| Étage | Rôle | Frontière |
|-------|------|-----------|
| **goose** | framework et *runtime* d'agent, tient la boucle d'agent | — |
| **Berd** | client de bureau : projets, contexte, sessions, agents, configuration | **Agent Client Protocol** |
| **Buzz** | espace partagé où le travail solo devient collaboratif | non précisée dans le billet |

- **Occurrence en production de l'Agent Client Protocol** — l'ACP de Zed, à ne pas confondre avec l'*Agentic Commerce Protocol* : voir [[girard-acp-deux-protocoles-un-sigle-2026-08-02]] pour la désambiguïsation et [[agentclientprotocol-introduction-2026-08-02]] pour la spécification.
- **Thèse de la séparation** : *« we didn't need another model or agent harness, we needed a consistent environment around them »* — la couche manquante n'est ni le modèle ni le harnais, c'est le client. Le billet ne dit rien de la façon dont Berd se connecte à Buzz, ni si la même frontière ACP y est utilisée.

### Les six exigences léguées à Buzz

Verbatim : *« Berd showed us the importance of private space, durable context, recognizable agent identities, reusable skills, visible configuration, and clearer visibility into an agent's configured context, tools, and capabilities. Buzz gives those ideas somewhere to go when individual work becomes collaborative. »*

| # | Exigence | Démontrée dans le billet ? |
|---|----------|----------------------------|
| 1 | *private space* | non |
| 2 | *durable context* | oui — projets persistants |
| 3 | *recognizable agent identities* | oui — c'est l'objet du texte |
| 4 | *reusable skills* | non |
| 5 | *visible configuration* | non |
| 6 | *visibility into context, tools, capabilities* | non |

Liste utilisable telle quelle comme **grille d'évaluation d'un client d'agents**. Sur la portabilité des skills entre clients, à croiser avec [[janakiram-agent-platform-portability-contract-2026-07-20]] et [[google-agent-plugins-packaging-skills-mcp-2026-08-06]].

### Appartenances et écosystème

- **goose** est hébergé sous `github.com/aaif-goose/goose` — **Agentic AI Foundation** (`aaif.io`), fondation sous égide **Linux Foundation**, gouvernance neutre.
- Le billet renvoie à **MCP** et à **AGENTS.md** (`agents.md`) comme standards partagés.

### Thèse produit

*« Work with an agent often begins alone. You research, experiment, gather context, and shape an idea before it is ready for other people… But work rarely stays private. »* → *« Start alone, then go multiplayer. »* C'est la proposition la plus falsifiable du billet, et celle qui motive le passage de Berd à Buzz.

### Réserves

- **Aucun chiffre** dans tout le texte : pas d'utilisateur, pas de dépôt, pas de durée, pas de coût.
- **Aucune licence nommée** pour une annonce d'ouverture de code.
- Une phrase en surpromesse, sans exemple ni capture : *« Just by chatting with Berd, users can easily create custom agents to do any task they want, even helping with everyday tasks like planning travel or shopping. »*

## RésuméDe400mots

Billet du blog corporate de **Block** (`block.xyz/inside`), **non signé**, publié le **18 août 2026**, qui annonce **l'ouverture du code de Berd** et expose la thèse de conception qui l'a guidée.

**Ce qu'est Berd.** *« Berd is a desktop application our teams use to work with AI agents across projects, skills, tools, and models. »* Née d'un problème interne : Block avait accès à des agents capables — **goose**, **Claude Code**, **Codex** — mais chacun imposait *« different interfaces, configuration systems, and ways of managing context »*. Conclusion tirée : *« we didn't need another model or agent harness, **we needed a consistent environment around them** »*. Berd rassemble conversations, fichiers, dossiers, instructions, agents et skills autour de **projets persistants**, pour cesser de reconstruire le contexte à chaque tâche.

**La thèse de design.** Donner du **caractère** aux agents — non seulement par les rôles, instructions, skills et outils, mais par des **identités visuelles distinctes**, dont une collection de personnages animés, les *« Gloopies »*. Le problème invoqué est celui de la boîte de saisie vide : *« the product gives people little sense of how the agent is configured, which context and tools are available to it, and how it differs from another agent »*. Le billet inscrit la démarche dans la lignée de **Square** et **Cash App** — apporter du design là où la catégorie n'en avait pas. **Mais le problème posé est un problème de lisibilité de la configuration, et l'avatar résout la distinguabilité** ; le texte le reconnaît en une ligne qu'il ne développe pas : *« The avatars make the agent recognizable. **Its role, skills, and tools make it useful.** »*

**L'architecture.** Berd descend de **goose**, framework d'agent open source lancé par Block en **janvier 2025**, contribué à l'**Agentic AI Foundation** (Linux Foundation, décembre 2025) aux côtés de **MCP** et d'**AGENTS.md**. Répartition explicite : *« goose remains the open agent framework and runtime. Berd is a desktop application built around it. **Berd connects to goose through the Agent Client Protocol.** »* goose tient la boucle d'agent, Berd tient l'expérience.

**La suite est Buzz.** Berd a servi à explorer le travail **solo** ; *« But work rarely stays private »*. Ce que Berd a montré — *« private space, durable context, recognizable agent identities, reusable skills, visible configuration »* — nourrira **Buzz**, l'espace partagé humains+agents. *« Start alone, then go multiplayer. »*

**Réserves.** **Aucun chiffre, aucun test utilisateur, aucune licence nommée** ; une surpromesse isolée (*« create custom agents to do any task they want »*) ; et un billet dont le titre annonce un rétrospectif tout en maintenant le produit au présent — **Berd n'est pas déclaré déprécié, mais la feuille de route va à Buzz**.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Block | ORGANISATION | publie | Berd | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Block | ORGANISATION | a_créé | goose | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Berd | TECHNOLOGIE | est_instance_de | client de bureau pour agents | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Berd | TECHNOLOGIE | utilise | goose | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Berd | TECHNOLOGIE | utilise | Agent Client Protocol | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Agent Client Protocol | TECHNOLOGIE | permet | séparation client / boucle d'agent | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| goose | TECHNOLOGIE | fait_partie_de | Agentic AI Foundation | ORGANISATION | 0.95 | STATIQUE | déclaré_article |
| Agentic AI Foundation | ORGANISATION | fait_partie_de | Linux Foundation | ORGANISATION | 0.96 | STATIQUE | déclaré_article |
| Berd | TECHNOLOGIE | résout | fragmentation des interfaces d'agents | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Berd | TECHNOLOGIE | réduit | reconstruction du contexte à chaque tâche | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| Berd | TECHNOLOGIE | utilise | identité visuelle d'agent | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| identité visuelle d'agent | CONCEPT | permet | distinguabilité des agents | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| identité visuelle d'agent | CONCEPT | s_oppose_à | lisibilité de la configuration d'agent | CONCEPT | 0.80 | ATEMPOREL | inféré |
| Gloopies | CONCEPT | fait_partie_de | identité visuelle d'agent | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| Block | ORGANISATION | affirme_que | "The avatars make the agent recognizable. Its role, skills, and tools make it useful." | CITATION | 0.98 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | affirme_que | "we didn't need another model or agent harness, we needed a consistent environment around them" | CITATION | 0.97 | STATIQUE | déclaré_article |
| Block | ORGANISATION | affirme_que | "Work with an agent often begins alone. But work rarely stays private." | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | affirme_que | « le caractère d'un agent est à la fois visuel et fonctionnel : des agents peuvent avoir l'air distincts parce qu'ils le sont » | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | prédit | « ce qui a été appris sur Berd nourrira la suite du travail sur Buzz : commencer seul, puis passer en multijoueur » | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Berd | TECHNOLOGIE | s_applique_à | travail solo avec agents | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | s_applique_à | travail collaboratif humains-agents | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | est_basé_sur | Berd | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Berd | TECHNOLOGIE | observé_dans | Block | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | concurrence | Berd | TECHNOLOGIE | 0.78 | DYNAMIQUE | inféré |
| Berd | TECHNOLOGIE | s_oppose_à | boîte de saisie vide | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Square | TECHNOLOGIE | fait_partie_de | Block | ORGANISATION | 0.96 | STATIQUE | déclaré_article |
| Cash App | TECHNOLOGIE | fait_partie_de | Block | ORGANISATION | 0.96 | STATIQUE | déclaré_article |
| design comme différenciateur | CONCEPT | observé_dans | Square | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| lisibilité de la configuration d'agent | CONCEPT | améliore | confiance vérifiable dans un agent | CONCEPT | 0.82 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Block | ORGANISATION | rôle | Éditeur de Berd, goose et Buzz ; cinquième texte maison en un mois, premier non signé | MISE_A_JOUR |
| Berd | TECHNOLOGIE | catégorie | Application de bureau pour travailler avec des agents : projets, skills, outils, modèles | AJOUT |
| Berd | TECHNOLOGIE | statut | Code ouvert le 18 août 2026 sous `github.com/block/berd` — aucune licence nommée dans le billet | AJOUT |
| Berd | TECHNOLOGIE | limite | Aucune mesure d'usage, d'adoption ni de test utilisateur publiée | AJOUT |
| goose | TECHNOLOGIE | rôle | Framework et runtime d'agent open source, lancé par Block en janvier 2025 ; boucle d'agent sous Berd | MISE_A_JOUR |
| goose | TECHNOLOGIE | gouvernance | Transféré à l'Agentic AI Foundation — dépôt `github.com/aaif-goose/goose` | AJOUT |
| Agent Client Protocol | TECHNOLOGIE | rôle | Frontière entre le client de bureau Berd et le runtime goose | AJOUT |
| Agentic AI Foundation | ORGANISATION | rôle | Hôte vendor-neutral de goose, aux côtés de MCP et AGENTS.md, sous la Linux Foundation | MISE_A_JOUR |
| Buzz | TECHNOLOGIE | rôle | Destination déclarée des enseignements de Berd : l'espace partagé humains+agents | MISE_A_JOUR |
| identité visuelle d'agent | CONCEPT | définition | Donner à un agent une apparence distinctive pour le rendre reconnaissable parmi d'autres | AJOUT |
| identité visuelle d'agent | CONCEPT | limite | Résout la distinguabilité, pas la lisibilité : ne dit rien des outils, permissions ni contexte actif | AJOUT |
| Gloopies | CONCEPT | définition | Collection phare de personnages animés de Berd servant d'avatars d'agents | AJOUT |
| lisibilité de la configuration d'agent | CONCEPT | définition | Capacité d'un utilisateur à voir comment un agent est configuré, quel contexte et quels outils lui sont disponibles | AJOUT |
| distinguabilité des agents | CONCEPT | définition | Capacité à identifier un agent parmi d'autres ; condition nécessaire mais non suffisante de sa compréhension | AJOUT |
| boîte de saisie vide | CONCEPT | définition | Interface d'agent par défaut qui ne révèle ni configuration, ni outils, ni différence entre agents | AJOUT |
| client de bureau pour agents | CONCEPT | définition | Couche d'expérience unifiée au-dessus de plusieurs modèles et harnais — projets, contexte, sessions, configuration | AJOUT |
| séparation client / boucle d'agent | CONCEPT | définition | Le client tient l'expérience et la configuration, le runtime tient la boucle d'exécution ; frontière protocolaire | AJOUT |
| fragmentation des interfaces d'agents | CONCEPT | définition | Multiplication des interfaces, systèmes de configuration et modes de gestion du contexte entre agents concurrents | AJOUT |
| reconstruction du contexte à chaque tâche | CONCEPT | définition | Coût récurrent de réinstaller le contexte de travail faute de projets persistants | AJOUT |
| travail solo avec agents | CONCEPT | définition | Phase privée — recherche, expérimentation, mise en forme — avant que le travail soit prêt à être partagé | AJOUT |
| travail collaboratif humains-agents | CONCEPT | définition | Phase partagée : équipier ajouté, artefact publié, décision expliquée, trace conservée | AJOUT |
| design comme différenciateur | CONCEPT | définition | Doctrine Block : apporter le design à une catégorie qui n'en avait pas change qui se sent invité à l'utiliser | AJOUT |
| Square | TECHNOLOGIE | rôle | Précédent maison invoqué : le terminal de paiement passé de caché à exposé | AJOUT |
| Cash App | TECHNOLOGIE | rôle | Précédent maison invoqué : personnalité et pertinence culturelle apportées à la finance personnelle | AJOUT |
| Claude Code | TECHNOLOGIE | rôle | Agent tiers cité comme faisant partie de l'outillage fragmenté observé chez Block | MISE_A_JOUR |
| Codex | TECHNOLOGIE | rôle | Agent tiers cité comme faisant partie de l'outillage fragmenté observé chez Block | MISE_A_JOUR |
| confiance vérifiable dans un agent | CONCEPT | définition | Confiance fondée sur ce que l'utilisateur peut inspecter — outils, permissions, contexte — et non sur l'apparence | AJOUT |
