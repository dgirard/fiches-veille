---
themes: [agents-codage-ia-skills, architecture-construction, outils-plateformes]
source: "Google Developers Blog"
---
# google-agent-plugins-packaging-skills-mcp-2026-08-06

## Veille

Annonce **Google** du **6 août 2026** : Google rejoint comme **Core Maintainer** la spécification **Agent Plugins 1.0.0**, format d'empaquetage ouvert et *vendor-neutral* pour distribuer ensemble des **Agent Skills** et des **serveurs MCP**. La spécification a été publiée par un **TSC** dont les Core Maintainers viennent d'**Amazon, Cursor, Microsoft, OpenAI et Vercel** ; Google s'y ajoute, représenté par **Kevin Hou** (Senior Staff Engineer, Google DeepMind). Les deux briques empaquetées — Agent Skills et MCP — sont d'origine **Anthropic**, qui ne figure pas dans cette liste de mainteneurs. **Le diagnostic** tient en une phrase : *« The core problem isn't the components. It's the manifest. »* Une skill est portable, un serveur MCP est portable ; la boîte dans laquelle on les met ne l'est pas, et chaque client a dû l'inventer pour lui-même — d'où les forks, les copies de composants identiques et leur dérive. **Le format** tient en une contrainte : *« A plugin is a directory. That's the whole idea, and the restraint is the point. »* Un `plugin.json` à deux lignes utiles (`$schema` et `name`), des skills dans `skills/` au format Agent Skills, des serveurs déclarés dans `mcp.json` avec un **`type` explicite sur chaque entrée** (stdio, Streamable HTTP, ou HTTP+SSE historique) — plus de transport deviné à la forme de l'objet de configuration. La force du design est dans ce que le manifeste **ne peut pas** faire : ni déplacer les composants, ni les déclarer en ligne, donc aucun chemin de découverte à configurer et aucun ordre de précédence à apprendre. Corollaire opérationnel : les composants **échouent indépendamment** — un serveur `mcp.json` qui ne démarre pas n'emporte pas les skills du plugin, le client saute l'entrée, continue et signale l'échec. L'échappatoire assumée est le répertoire en **domaine inversé** (`com.example.client/`), espace d'extension appartenant entièrement à un client (hooks, agents, commandes) que les autres ignorent : *« le cœur portable reste petit parce que les parties non portables ont un endroit légitime où aller »*. Une section est consacrée aux cas où le format ne se justifie pas — *« Not every skill should be a Plugin »* : un seul serveur MCP vers un seul client, `mcp.json` suffit ; une seule skill, pas besoin de plugin. Ce que la v1 exclut explicitement, en *future considerations* : **aucun mécanisme d'installation, aucun protocole de distribution, aucun modèle de permissions, aucune exigence de bac à sable, aucune vérification de confiance ou de provenance, aucune UX**. Le tout s'insère dans une pile à quatre couches indépendamment adoptables — **trouver** (Agentic Resource Discovery), **décrire** (AI Catalog, qui enregistrerait le type `application/agent-plugins+json`), **empaqueter** (Agent Plugins), **exécuter** (MCP + Agent Skills). Deux produits Google livrent déjà : **Agents CLI** et **Data Agent Kit** (BigQuery, Spanner, Cloud SQL).

## Titre Article

Agent Plugins package your skills, tools, and more

## Date

2026-08-06

## URL

https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/

## Keywords

Agent Plugins, Agent Plugins 1.0.0, spécification ouverte, vendor-neutral, Core Maintainer, TSC, gouvernance de spécification, empaquetage, packaging, plugin, plugin.json, manifeste, mcp.json, SKILL.md, skills/, scripts/, references/, Agent Skills, Model Context Protocol, MCP, serveur MCP, transport explicite, stdio, Streamable HTTP, HTTP+SSE, portabilité, interopérabilité, fork de package, dérive de copies, structure de répertoire, emplacement fixe, ordre de précédence, chemin de découverte, échec indépendant, isolation de composant, domaine inversé, espace de nommage d'extension, com.example.client, échappatoire, cœur portable, Agentic Resource Discovery, ARD, découverte de ressources, AI Catalog, application/agent-plugins+json, agent card, couche de découverte, couche d'exécution, contrat d'exécution, adoption indépendante, agent-plugins.org, Agents CLI, Data Agent Kit, Google Data Cloud, BigQuery, Spanner, Cloud SQL, Antigravity, Gemini CLI, Claude Code, Cursor, Amazon, Microsoft, OpenAI, Vercel, Anthropic, Kevin Hou, Haoyu Wang, Alan Blount, Google DeepMind, absence de vérification de provenance, modèle de permissions, bac à sable, sandboxing, chaîne d'approvisionnement, infrastructure ingrate, restraint, réinvention

## Authors

Trois signataires, répartis sur trois entités Google :

- **Kevin Hou** — Senior Staff Engineer, **Google DeepMind**. Il représente Google au **TSC** de la spécification ; la fonction de mainteneur est nominative, non institutionnelle.
- **Haoyu Wang** — Staff Software Engineer, **Google Cloud Data**, côté Data Agent Kit.
- **Alan Blount** — Technical Product Manager, **Google Cloud AI**.

Publié le **6 août 2026**. Billet d'ingénierie signé, écrit à la première personne du pluriel pour Google, mais portant sur une spécification qui n'est pas de Google — ce dont la rhétorique tire parti : *« Those skills were already distributable. Now they're distributable in a format that isn't ours alone. »*

## Ton

**Profil** : billet d'annonce technique, registre **ingénieur**, argumenté par la retenue plutôt que par l'ambition. Aucun superlatif produit, aucun chiffre de performance, aucune promesse de transformation. Public : auteurs de skills et de serveurs MCP qui distribuent vers plusieurs clients.

**Style** : structure en **six mouvements** — le problème vécu (vous expédiez vers un deuxième client) → ce qu'est réellement un plugin → quand ne pas en faire un → ce que la spec exclut → la pile dans laquelle elle s'insère → ce qui est livré. Trois traits :

1. **L'ouverture en deuxième personne, sur une scène de travail.** *« You wrote a skill. You wrote a script or an MCP server to go with your skill. »* Pas d'exposé du marché : une friction, reconnaissable, puis le diagnostic en une ligne — *« The core problem isn't the components. It's the manifest. »*
2. **L'argumentation par la soustraction.** Le texte consacre plus de place à **ce que le format ne fait pas** qu'à ce qu'il fait : ce que `plugin.json` **ne peut pas** faire (relocaliser, déclarer en ligne), ce que la v1 **exclut** (installation, distribution, permissions, sandbox, provenance, UX), et une section entière pour dire **quand ne pas s'en servir**. *« The restraint is the point. »*
3. **La chute anti-héroïque.** *« Packaging is unglamorous infrastructure, and unglamorous infrastructure is exactly the kind of thing that should be shared rather than reinvented five times. »* Registre inhabituel pour un billet de plateforme : l'argument de vente est que l'objet n'est pas intéressant.

**Formules-marqueurs** : *« The core problem isn't the components. It's the manifest. »*, *« A plugin is a directory. That's the whole idea, and the restraint is the point. »*, *« Independent components fail independently. »*, *« the portable core stays small because the non-portable parts have somewhere legitimate to go »*, *« Not every skill should be a Plugin »*, *« a format that isn't ours alone »*, *« unglamorous infrastructure »*.

**Position épistémique** : **descriptive et bornée**. Le texte ne revendique aucune adoption chiffrée, ne compare à aucun concurrent, et liste ses propres angles morts dans une section dédiée plutôt qu'en note de bas de page. Ce qu'il ne fait pas non plus : discuter la sécurité de la distribution qu'il rend plus facile.

## Pense-betes

- **Lire l'annonce par la gouvernance avant la technique.** Le format compte moins que **qui le tient** : un TSC de Core Maintainers issus d'**Amazon, Cursor, Microsoft, OpenAI, Vercel**, rejoints par **Google**. Six acteurs concurrents sur une couche d'emballage. **Anthropic n'est pas dans la liste des mainteneurs** — alors que **Agent Skills** et **MCP**, les deux formats empaquetés, viennent de chez elle. Ne pas surinterpréter (l'absence de cette liste n'est pas une exclusion, et le billet ne dit rien du reste de la gouvernance), mais **le fait est là** : la couche qui rend les formats d'Anthropic distribuables se normalise ailleurs. À rapprocher de [[openai-agentic-ai-foundation-linux-2025-12-09]] sur la normalisation ouverte de la couche agent, et de [[janakiram-agent-platform-portability-contract-2026-07-20]] sur le contrat de portabilité entre plateformes.

- **Le diagnostic, réutilisable tel quel** : ***« The core problem isn't the components. It's the manifest. »*** Une skill est portable, un serveur MCP est portable ; **la boîte ne l'est pas**, et chaque client a dû l'inventer. Symptômes à reconnaître dans votre propre distribution : un fork par client, deux copies de composants identiques, et la dérive qui suit.

- **Le format en cinq lignes, à retenir** :
  ```
  reports-plugin/
  ├── plugin.json          # $schema + name : deux lignes utiles
  ├── skills/summarize/    # SKILL.md, scripts/, references/ (spec Agent Skills)
  ├── mcp.json             # un `type` explicite sur chaque entrée
  └── com.example.client/  # espace d'extension propriétaire, ignoré par les autres
  ```
  → Le `type` explicite tue une ambiguïté réelle : **plus de transport deviné à la forme de l'objet de config** (stdio / Streamable HTTP / HTTP+SSE historique).

- **La meilleure idée de design : ce que le manifeste ne peut pas faire.** `plugin.json` **ne peut ni relocaliser un composant ni le déclarer en ligne**. Conséquences : **aucun chemin de découverte à configurer**, **aucun ordre de précédence à apprendre**. C'est un choix d'ingénierie transposable bien au-delà des plugins d'agents — *toute expressivité laissée à un fichier de configuration devient une surface de divergence entre implémentations*. Ici, le format est rendu portable en lui **retirant** du pouvoir.

- **La règle d'exploitation qui en découle** : ***« Independent components fail independently. »*** Un serveur `mcp.json` qui ne démarre pas **n'emporte pas les skills** du plugin — le client saute l'entrée, continue de charger et signale l'échec. À vérifier explicitement chez tout client qui prétend implémenter la spec : c'est le genre de garantie qu'on découvre absente en production.

- **L'échappatoire en domaine inversé — et son revers.** `com.example.client/` est un **espace d'extension** possédé par un seul client (hooks, agents, commandes), ignoré par les autres. Argument affiché : *le cœur portable reste petit parce que les parties non portables ont un endroit légitime où aller*. **Le même mécanisme est le vecteur par lequel la portabilité peut se vider** : si la valeur d'usage migre progressivement dans les répertoires propriétaires, le plugin reste formellement portable et devient pratiquement mono-client. **Métrique à surveiller sur vos propres plugins** : quelle part des fonctionnalités vit hors du cœur portable.

- **La section qu'on voit rarement dans un billet de plateforme** — *« Not Every skill should be a Plugin »* : un seul serveur MCP vers un seul client → **`mcp.json` seul reste la réponse la plus simple** ; une seule skill → **pas de plugin**. Le format ne se justifie que pour **des composants qui vont ensemble et doivent voyager ensemble**. Critère à appliquer avant de convertir un dépôt existant.

- **Ce que la v1 exclut, à lire comme une liste de risques à couvrir soi-même** : **pas de mécanisme d'installation, pas de protocole de distribution, pas de modèle de permissions, pas d'exigence de bac à sable, aucune vérification de confiance ou de provenance, pas d'UX**. Le billet le justifie (les obligations d'un IDE, d'une CLI et d'une plateforme d'entreprise diffèrent) et l'assume dans les *future considerations*. **Traduction pour qui déploie** : un format standard qui rend plus facile la circulation de **code exécutable** (skills avec `scripts/`, serveurs MCP) **sans** couche de provenance déplace la charge de la chaîne d'approvisionnement entièrement sur le client et sur vous. À instruire avec [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]] et [[sfeir-anthropic-sdlc-ai-native-securise-2026-07-26]] : périmètre d'exécution, restriction de sortie réseau, revue des skills tierces.

- **La pile à quatre couches — tableau à réutiliser** :
  | Job | Couche | Ce qu'elle fait |
  |---|---|---|
  | **Trouver** | Agentic Resource Discovery | protocole ouvert : « qu'est-ce qui existe pour cette tâche ? » — traite déjà le plugin comme ressource de première classe, **avant** invocation |
  | **Décrire** | AI Catalog | format d'entrée indexé par ARD ; enregistrement proposé du type `application/agent-plugins+json` |
  | **Empaqueter** | Agent Plugins | un répertoire, des emplacements fixes |
  | **Exécuter** | MCP + Agent Skills | les contrats d'exécution, déjà portables |
  → **Chaque couche est adoptable indépendamment** : publier un plugin sans entrée de catalogue, cataloguer une ressource qui n'est pas un plugin, exécuter des skills sans plugin. *« Adopting one never obligates you to the next. »* C'est la promesse à vérifier dans les faits.
  **Consigne de graphe** (cf. girard-acp-deux-protocoles-un-sigle-2026-08-02) : **ne jamais créer d'entité `ARD`** — l'entité canonique est **Agentic Resource Discovery**, « ARD » n'est qu'un alias.

- **Ce qui est livré aujourd'hui** : **Agents CLI** (skills Google d'agent building, évaluation, déploiement, observabilité, publication — s'utilise depuis **Antigravity, Gemini CLI, Claude Code ou Cursor**) et **Data Agent Kit** (BigQuery, Spanner, Cloud SQL). Noter la formulation : *« Those skills were already distributable. Now they're distributable in a format that isn't ours alone. »* — **la nouveauté n'est pas la capacité, c'est la neutralité du contenant.**

- **Méta / à relier** : sur la brique empaquetée, agent-skills-anthropic-2025-10-16 et claude-skills-document-manipulation-willison-2025-10-10 ; sur la couche client↔agent qui s'empile au-dessus, agentclientprotocol-introduction-2026-08-02 ; sur la découverte et l'annuaire de skills en pratique, graphify-net-annuaire-ia-coding-2026-08-06 et skill-shamsi-graphify-2026-08-06 ; sur la concurrence des formats d'instruction, gao-vercel-agents-md-outperforms-skills-evals-2026-01-27 (Vercel, également Core Maintainer ici).

## RésuméDe400mots

Billet d'ingénierie de **Google** du **6 août 2026** annonçant que l'entreprise rejoint comme **Core Maintainer** la spécification **Agent Plugins 1.0.0** — un format d'empaquetage ouvert et *vendor-neutral* pour distribuer ensemble **Agent Skills** et **serveurs MCP**.

**Le fait de gouvernance d'abord.** La spécification a été publiée par un TSC de Core Maintainers venus d'**Amazon, Cursor, Microsoft, OpenAI et Vercel**. Google s'y ajoute, représenté nominativement par **Kevin Hou** (Google DeepMind). Six concurrents s'accordent sur une couche d'emballage. **Anthropic ne figure pas dans la liste des mainteneurs**, alors que les deux briques empaquetées viennent de chez elle.

**Le diagnostic.** Une skill est portable, un serveur MCP est portable — *« The core problem isn't the components. It's the manifest. »* Ce qui n'a jamais été portable, c'est la boîte : disposition des répertoires, métadonnées de manifeste, forme de la configuration MCP et inférence du transport diffèrent d'un client à l'autre. On forke, on maintient deux copies de composants identiques, et elles dérivent.

**Le format.** *« A plugin is a directory. That's the whole idea, and the restraint is the point. »* Un `plugin.json` réduit à `$schema` et `name` ; les skills dans `skills/`, au format Agent Skills ; les serveurs dans `mcp.json`, **avec un `type` explicite** sur chaque entrée (stdio, Streamable HTTP, HTTP+SSE historique). La force du design tient à ce que le manifeste **ne peut pas** faire : ni relocaliser un composant, ni le déclarer en ligne. Donc aucun chemin de découverte à configurer, aucun ordre de précédence à apprendre. Corollaire : **les composants échouent indépendamment** — un serveur qui ne démarre pas n'emporte pas les skills. Un répertoire en **domaine inversé** (`com.example.client/`) sert d'espace d'extension propriétaire, ignoré par les autres clients : le cœur portable reste petit parce que les parties non portables ont où aller.

**Les limites, assumées.** Une section entière explique **quand ne pas faire de plugin** (un seul serveur MCP, une seule skill : inutile). Une autre liste ce que la v1 exclut : **installation, distribution, permissions, sandboxing, vérification de confiance et de provenance, UX**. Justification : les obligations d'un IDE, d'une CLI et d'une plateforme d'entreprise diffèrent réellement.

**La pile.** Trouver (**Agentic Resource Discovery**), décrire (**AI Catalog**), empaqueter (**Agent Plugins**), exécuter (**MCP + Agent Skills**) — chaque couche adoptable indépendamment.

**Livré aujourd'hui** : **Agents CLI** (utilisable depuis Antigravity, Gemini CLI, Claude Code ou Cursor) et **Data Agent Kit** (BigQuery, Spanner, Cloud SQL). *« Those skills were already distributable. Now they're distributable in a format that isn't ours alone. »* Chute : *« Packaging is unglamorous infrastructure »*, et c'est précisément ce qui doit être partagé plutôt que réinventé cinq fois.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Google | ORGANISATION | collabore_avec | Agent Plugins | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Kevin Hou | PERSONNE | travaille_chez | Google DeepMind | ORGANISATION | 0.96 | DYNAMIQUE | déclaré_article |
| Kevin Hou | PERSONNE | dirige | la représentation de Google au comité de pilotage technique d'Agent Plugins | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Agent Plugins | TECHNOLOGIE | permet | d'empaqueter des Agent Skills et des serveurs MCP dans un plugin portable d'un client à l'autre | AFFIRMATION | 0.97 | ATEMPOREL | déclaré_article |
| Agent Plugins | TECHNOLOGIE | utilise | Agent Skills | TECHNOLOGIE | 0.96 | ATEMPOREL | déclaré_article |
| Agent Plugins | TECHNOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.96 | ATEMPOREL | déclaré_article |
| Amazon | ORGANISATION | publie | Agent Plugins | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Microsoft | ORGANISATION | publie | Agent Plugins | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | publie | Agent Plugins | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Vercel | ORGANISATION | publie | Agent Plugins | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Cursor | ORGANISATION | publie | Agent Plugins | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Google | ORGANISATION | affirme_que | le problème de portabilité ne vient pas des composants mais du manifeste qui les emballe | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| Agent Plugins | TECHNOLOGIE | résout | la duplication et la dérive des packages forkés pour chaque client | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Agent Plugins | TECHNOLOGIE | utilise | un répertoire à emplacements fixes plutôt qu'un manifeste expressif : plugin.json ne peut ni relocaliser ni déclarer les composants en ligne | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Agent Plugins | TECHNOLOGIE | réduit | la surface de divergence entre implémentations, en supprimant les chemins de découverte configurables et les ordres de précédence | AFFIRMATION | 0.91 | ATEMPOREL | inféré |
| Agent Plugins | TECHNOLOGIE | permet | l'échec indépendant des composants : un serveur mcp.json qui ne démarre pas n'emporte pas les skills du plugin | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| espace d'extension en domaine inversé | CONCEPT | permet | à un client d'ajouter ses fonctionnalités propriétaires sans casser la portabilité du cœur | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| espace d'extension en domaine inversé | CONCEPT | s_oppose_à | la portabilité réelle d'un plugin, si la valeur d'usage migre vers les répertoires propriétaires | AFFIRMATION | 0.82 | ATEMPOREL | inféré |
| Google | ORGANISATION | recommande | de ne pas faire de plugin pour un seul serveur MCP ni pour une seule skill : le format vaut pour des composants qui doivent voyager ensemble | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Agent Plugins | TECHNOLOGIE | s_oppose_à | la prise en charge de l'installation, de la distribution, des permissions, du bac à sable, de la vérification de provenance et de l'expérience utilisateur | AFFIRMATION | 0.96 | DYNAMIQUE | déclaré_article |
| Agentic Resource Discovery | TECHNOLOGIE | permet | à un client de demander quelles ressources existent pour une tâche, avant toute invocation | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Agentic Resource Discovery | TECHNOLOGIE | est_instance_de | couche de découverte de la pile agentique | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| AI Catalog | TECHNOLOGIE | s_applique_à | la description indexable des ressources agentiques, dont les plugins via le type application/agent-plugins+json | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Agentic Resource Discovery | TECHNOLOGIE | utilise | AI Catalog | TECHNOLOGIE | 0.89 | ATEMPOREL | déclaré_article |
| Agents CLI | TECHNOLOGIE | utilise | Agent Plugins | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Data Agent Kit | TECHNOLOGIE | utilise | Agent Plugins | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Data Agent Kit | TECHNOLOGIE | s_applique_à | la gestion des actifs de données Google Data Cloud (BigQuery, Spanner, Cloud SQL) depuis un agent de codage | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Agents CLI | TECHNOLOGIE | s_applique_à | Antigravity, Gemini CLI, Claude Code et Cursor | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Google | ORGANISATION | affirme_que | l'empaquetage est une infrastructure ingrate, qui doit être partagée plutôt que réinventée cinq fois | CITATION | 0.94 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Agent Plugins | TECHNOLOGIE | définition | Spécification ouverte et vendor-neutral (v1.0.0) empaquetant Agent Skills et serveurs MCP dans un répertoire portable : plugin.json réduit à $schema et name, skills/ au format Agent Skills, mcp.json avec type explicite par entrée, et un espace d'extension en domaine inversé par client | AJOUT |
| Agent Plugins | TECHNOLOGIE | gouvernance | Publiée par un TSC de Core Maintainers issus d'Amazon, Cursor, Microsoft, OpenAI et Vercel ; Google rejoint le groupe le 6 août 2026, représenté par Kevin Hou. Anthropic, à l'origine d'Agent Skills et de MCP, ne figure pas dans la liste des mainteneurs citée | AJOUT |
| Agent Plugins | TECHNOLOGIE | limites | La v1 ne définit ni installation, ni protocole de distribution, ni modèle de permissions, ni exigence de bac à sable, ni vérification de confiance ou de provenance, ni expérience utilisateur : ces responsabilités reviennent au client | AJOUT |
| espace d'extension en domaine inversé | CONCEPT | définition | Répertoire nommé en domaine inversé (com.example.client/) réservé aux ajouts propriétaires d'un client et ignoré par les autres ; garde le cœur portable petit en donnant aux parties non portables un emplacement légitime | AJOUT |
| Agentic Resource Discovery | TECHNOLOGIE | définition | Protocole ouvert de découverte permettant à un client de demander quelles ressources existent pour une tâche donnée, et traitant le plugin comme ressource de première classe aux côtés des agents, serveurs MCP et skills ; se situe entièrement avant l'invocation. Alias « ARD », à ne jamais employer seul comme entité | AJOUT |
| AI Catalog | TECHNOLOGIE | définition | Format d'entrée indexé par Agentic Resource Discovery ; un changement proposé y enregistre le type application/agent-plugins+json pour qu'une entrée pointe vers un plugin.json comme elle pointe déjà vers une agent card ou un mcp.json | AJOUT |
| Agents CLI | TECHNOLOGIE | définition | Outil Google empaquetant les skills maison d'agent building, évaluation, déploiement, observabilité et publication ; distribué au format Agent Plugins et utilisable depuis Antigravity, Gemini CLI, Claude Code ou Cursor | AJOUT |
| Data Agent Kit | TECHNOLOGIE | définition | Collection de plugins Google au format Agent Plugins donnant à un agent de codage l'accès aux actifs Google Data Cloud : BigQuery, Spanner, Cloud SQL | AJOUT |
| Agent Skills | TECHNOLOGIE | rôle | Contrat d'exécution déjà portable, empaqueté par Agent Plugins : une skill par sous-répertoire de skills/, avec SKILL.md, scripts/ et references/ | MISE_A_JOUR |
| Model Context Protocol | TECHNOLOGIE | rôle | Contrat d'exécution déjà portable, déclaré dans mcp.json avec un type explicite par entrée, ce qui supprime l'inférence du transport (stdio, Streamable HTTP, HTTP+SSE historique) | MISE_A_JOUR |
| Kevin Hou | PERSONNE | rôle | Senior Staff Engineer chez Google DeepMind ; représente nominativement Google au comité de pilotage technique d'Agent Plugins et cosigne l'annonce | AJOUT |
| Haoyu Wang | PERSONNE | rôle | Staff Software Engineer chez Google Cloud Data ; cosignataire de l'annonce, côté Data Agent Kit | AJOUT |
| Alan Blount | PERSONNE | rôle | Technical Product Manager chez Google Cloud AI ; cosignataire de l'annonce | AJOUT |
