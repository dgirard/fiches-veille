---
themes: [outils-plateformes, agents-codage-ia-skills, produits-services, transformation-adoption]
source: "Block"
---
# block-berd-caractere-agents-open-source-2026-08-18

## Veille

Billet du blog corporate **Block** (`block.xyz/inside`), **non signé** — l'auteur affiché est « Block » —, publié le **18 août 2026**, ~930 mots, qui annonce **l'ouverture du code de Berd**, l'application de bureau interne de Block pour travailler avec des agents, et expose la thèse de conception qui l'a guidée : **donner du caractère aux agents**, « not only through roles, instructions, skills, and tools, but through **distinctive visual identities** ». ⭐⭐ **Le sujet annoncé est une leçon de design ; le vrai sujet est un désalignement entre le problème posé et la solution montrée.** Le problème est nommé avec précision — *« the product gives people little sense of **how the agent is configured, which context and tools are available to it**, and how it differs from another agent »* : c'est un problème de **lisibilité de la configuration**. La réponse mise en avant est un **avatar animé** (les *« Gloopies »*). Or un avatar résout la **distinguabilité**, pas la lisibilité : il dit *quel* agent c'est, jamais *ce qu'il peut faire*. ⭐ **Le billet le concède lui-même en une phrase qu'il ne développe pas** — *« The avatars make the agent recognizable. **Its role, skills, and tools make it useful.** »* — et cette phrase est la contribution la plus solide du texte : **elle sépare proprement l'identité de la capacité**, alors que le reste de l'article les vend ensemble. ⚠️ **La conséquence non traitée** : un visage augmente la confiance attribuée sans augmenter la vérifiabilité. Le billet ne dit jamais comment un utilisateur voit ce qu'un agent a réellement le droit de faire. ⭐⭐ **Deuxième lecture, disponible seulement dans le corpus** : c'est le **cinquième texte Block en un mois** et le **second publié le 18 août**, le même jour que [[petersen-block-buzz-projects-forge-souveraine-2026-08-18]] — **les deux ouvrent sur le même diagnostic de fragmentation** et **les deux se terminent sur Buzz**. Celui-ci le fait explicitement : la dernière section transfère l'avenir du produit — *« What we learned from Berd will inform our continued work on Buzz »*, *« Start alone, then go multiplayer »*. ⚠️ **Ne pas en conclure que Berd est abandonné** : le texte le décrit au présent partout ailleurs et l'appel à l'action est vivant (*« Download Berd »*). **Ce qui est vrai est plus étroit : le titre annonce un rétrospectif (*« what we learned »*) et la feuille de route va à Buzz.** Apport technique net et vérifiable, en une ligne : **Berd est un client de bureau qui parle à goose via l'Agent Client Protocol** — goose tient la boucle d'agent, Berd tient l'expérience (projets, contexte, sessions, agents, configuration). ⚠️ **Zéro mesure dans tout le texte** : pas un utilisateur, pas un dépôt, pas une durée, pas un coût. Et **aucune licence n'est nommée** pour une annonce d'ouverture de code.

## Titre Article

Designing AI with character: what we learned building Berd

## Date

2026-08-18

## URL

https://block.xyz/inside/designing-ai-with-character-what-we-learned-building-berd

## Keywords

Berd, Block, open source, ouverture de code, application de bureau, desktop application, agents IA, caractère, character, identité visuelle, visual identity, avatar, Gloopies, personnages animés, anthropomorphisme, lisibilité de la configuration, configuration visible, quel contexte et quels outils, prompt box vide, empty prompt box, distinguabilité, reconnaissable, recognizable, utile, useful, rôle compétences outils, roles skills tools, projets persistants, persistent projects, contexte durable, durable context, reconstruction du contexte, goose, Claude Code, Codex, harnais d'agent, agent harness, environnement cohérent, consistent environment, fragmentation des interfaces, Agent Client Protocol, ACP, client agent, boucle d'agent, agent loop, runtime, Agentic AI Foundation, AAIF, Linux Foundation, MCP, Model Context Protocol, AGENTS.md, gouvernance neutre, vendor-neutral, Buzz, travail solo puis partagé, solo to shared, start alone then go multiplayer, multijoueur, Square, Cash App, design comme différenciateur, accessibilité non technique, approachable beyond engineering, création d'agents par conversation, agents personnels, aucun chiffre, aucune licence, blog corporate, auteur non signé, retour d'expérience rétrospectif

## Authors

**Aucun auteur nommé.** Le billet est signé **« Block »** — le champ *Author* de la page porte le nom de l'entreprise, et le champ *Tags* aussi. Publié sur **`block.xyz/inside`**, le blog **corporate**, et non sur `engineering.block.xyz`.

⚠️ **Ce que ce dispositif d'énonciation ajoute au dossier Block.** La fiche du 18 août sur *Projects in Buzz* avait posé que **la fonction de l'auteur prédit le registre du texte** et donc ce sur quoi il est opposable. Ce billet **confirme la règle en la poussant d'un cran** : pas d'auteur du tout, et le registre descend d'autant.

| Date | Signature | Fonction affichée | Support | Ce que le texte apporte |
|---|---|---|---|---|
| **21 juil.** | Tyler Longwell | ingénieur | engineering | protocole **spécifié en TLA+**, suite de conformité |
| **6 août** | Atish Patel | ingénieur | engineering | **compositions d'équipes, coûts, scores Terminal-Bench** |
| **18 août** | Thomas Petersen | *Principal Designer & Builder* | engineering | **doctrine + captures d'écran**, zéro mesure |
| **18 août** | **« Block »** | **— (aucune)** | **corporate** | **récit de marque + doctrine de design**, zéro mesure |

→ ⭐ **Ce n'est pas un reproche, c'est un calibrage de citabilité.** Un billet corporate non signé engage l'entreprise et n'engage personne : il est citable comme **position officielle de Block sur le design des agents**, jamais comme retour d'expérience d'ingénierie. ⚠️ **Corollaire pratique** : aucun interlocuteur nommé à qui poser une question, contrairement aux trois précédents.

**Le récit de filiation, qui est le vrai marqueur corporate.** Le billet inscrit Berd dans une lignée de design maison — *« Square transformed payment hardware from something sellers hid behind the counter into something they could display proudly. Cash App brought personality and cultural relevance to personal finance. »* ⭐ **C'est l'argument d'autorité du texte, et il est de nature commerciale, pas technique** : Block a un historique réel d'apport du design à des catégories qui n'en avaient pas. **À retenir comme intention de marque assumée** — *« The goal was not to disguise the technology, but to make its capabilities more visible, approachable, and personal. »*

## Ton

**Profil** : **billet de marque en forme de retour d'expérience** — ~930 mots, cinq sections courtes, ton posé et sans emphase. Public : au-delà des ingénieurs, explicitement (*« assumed a level of technical fluency that many people did not have »*). Ni exposé de conception détaillé, ni benchmark, ni tribune : **une intention de design racontée, doublée d'une annonce d'ouverture de code.**

**Style** : quatre traits.

1. **Le passé pour l'apprentissage, le présent pour le produit — et il faut lire les deux.** Les sections de bilan sont au passé (*« Berd **gave** our teams one desktop application »*, *« Berd **showed** us the importance of… »*) tandis que la description du produit reste au présent (*« Berd **is** a desktop application our teams **use** »*, *« Berd and goose **now serve** different but connected purposes »*, *« Berd **connects** to goose »*). ⚠️ **La tentation de lire une mise au placard est forte et le texte ne la porte pas.** **Formulation exacte : le titre annonce un rétrospectif, la dernière section donne la suite à Buzz, et le produit n'est jamais déclaré déprécié.**
2. **Aucune emphase, aucun superlatif, aucun chiffre.** Le registre est celui du compte rendu tranquille. C'est **plus sobre que la moyenne des annonces produit du corpus**, et cela rend le texte agréable — mais **rien n'y est réfutable** faute de matière.
3. **Six liens sortants, tous fonctionnels.** `berd.xyz`, `github.com/block/berd`, `github.com/aaif-goose/goose`, `aaif.io`, `agents.md`, `buzz.xyz`. ⭐ **Contraste net avec le billet Petersen du même jour, qui n'en avait aucun** — celui-ci est vérifiable sur ses appartenances, à défaut de l'être sur ses effets. ⚠️ **Mais aucun lien vers une documentation, une architecture ou une spécification** ; le lien dépôt est le seul point d'entrée technique.
4. **La seule phrase en surpromesse est aussi la moins étayée.** *« Just by chatting with Berd, users can easily create custom agents to do any task they want, even helping with everyday tasks like planning travel or shopping. »* — *« any task they want »*, *« easily »*, sans un exemple, sans une capture, sans un utilisateur. **C'est la phrase à ne pas reprendre.**

**Formules-marqueurs** : *« At Block, we often build the tools we need ourselves. »* · *« How do you make something as abstract as an AI agent easier to understand and shape? »* · *« The goal was not to disguise the technology, but to make its capabilities more visible, approachable, and personal. »* · *« The technology was powerful, but the experience around it was fragmented. »* · *« we didn't need another model or agent harness, we needed a consistent environment around them »* · *« Many AI interfaces begin with an empty prompt box. »* · *« Different agents can look distinct because they are distinct. »* · *« The avatars make the agent recognizable. Its role, skills, and tools make it useful. »* · *« Berd and goose now serve different but connected purposes. »* · *« Work with an agent often begins alone. »* · *« But work rarely stays private. »* · *« Start alone, then go multiplayer. »* · *« We want to see what you make, and hear what works for you. »*

**Position épistémique** : **intention de conception documentée par des captures et une filiation de marque.** ⚠️ **Citer ce billet comme la doctrine de design de Block sur l'identité des agents et comme la source de l'articulation Berd/goose/Buzz. Ne jamais le citer comme preuve que le caractère visuel améliore la compréhension d'un agent** — aucune étude, aucun test utilisateur, aucune mesure d'adoption n'est produite.

## Pense-betes

- **⭐⭐ Le désalignement central : un problème de lisibilité reçoit une réponse d'identité.** Le billet énonce le problème avec une précision remarquable, puis répond à côté.
  | Verbatim | Ce qu'il énonce |
  |---|---|
  | *« the product gives people little sense of **how the agent is configured, which context and tools are available to it**, and how it differs from another agent »* | **problème de lisibilité de la configuration** (que peut-il faire ?) |
  | *« we've designed distinctive collections of animated characters, including our flagship "Gloopies" »* | **réponse d'identité visuelle** (lequel est-ce ?) |
  | *« The avatars make the agent recognizable. **Its role, skills, and tools make it useful.** »* | **l'aveu du décalage, en une ligne** |
  → ⭐ **La distinction à extraire et à réutiliser telle quelle : distinguer n'est pas rendre lisible.** Un avatar est un **index** — il permet de retrouver et de nommer un agent parmi d'autres, ce qui est un vrai gain quand on en gère dix. Il ne dit **rien** de ses outils, de ses permissions, ni de son contexte actif. ⚠️ **Et le risque est asymétrique** : un visage cohérent et sympathique **augmente la confiance attribuée sans augmenter la vérifiabilité**. C'est le même mécanisme de panne que le *« pass nu »* de [[dumortier-marketing-ai-os-verification-2026-08-12]] — **un signal de confiance émis sans déclaration de ce qui a été couvert** — transposé de la vérification à l'interface. ⭐ **Le bon test à poser à toute interface d'agent, et que ce billet ne passe pas** : *combien de clics pour voir la liste exacte des outils que cet agent peut appeler, et ce qu'il a le droit d'écrire ?* Rapprocher de l'invariant de journalisation de [[deepseek-harness-everything-is-a-plugin-2026-08-13]] (*« model-visible means logged »*) : **c'est la visibilité de la configuration qui doit être assertée, pas l'attachement à l'agent.**

- **⭐⭐ L'articulation Berd / goose / Buzz est le contenu le plus durable du billet — et c'est une architecture en trois étages nettement posée.** Verbatim : *« goose remains the open agent framework and runtime. Berd is a desktop application built around it. **Berd connects to goose through the Agent Client Protocol.** This separation lets Berd focus on the desktop experience, including projects, context, sessions, agents, and configuration, **while goose handles the underlying agent loop.** »*
  | Étage | Rôle | Frontière |
  |---|---|---|
  | **goose** | framework et *runtime* d'agent, boucle d'agent | — |
  | **Berd** | client de bureau : projets, contexte, sessions, agents, configuration | **Agent Client Protocol** |
  | **Buzz** | l'espace partagé où le travail solo devient collaboratif | (non précisée ici) |
  → ⭐⭐ **C'est une occurrence en production de l'Agent Client Protocol, et elle vaut d'être notée pour une raison précise** : [[girard-acp-deux-protocoles-un-sigle-2026-08-02]] a établi que le corpus indexait le sigle `ACP` **exclusivement** sur l'*Agentic Commerce Protocol*, et que « Agent Client Protocol » y était **totalement absent**. Ce billet est un cas d'usage industriel de l'**ACP de Zed** documenté par un tiers, à faire compter comme tel — spécification en [[agentclientprotocol-introduction-2026-08-02]]. ⭐ **Et la thèse de la séparation vaut au-delà de Berd** : *« we didn't need another model or agent harness, **we needed a consistent environment around them** »*. **La couche qui manquait n'était ni le modèle ni le harnais, c'était le client** — exactement ce que l'analogie LSP promettait (N+M au lieu de N×M). ⚠️ **Réserve** : le billet ne dit **rien** de la façon dont Berd se connecte à Buzz, ni si la même frontière ACP y est utilisée. **Ne pas l'extrapoler.**

- **⭐ Le second billet Block du 18 août, et les deux ouvrent sur la même phrase-problème.** C'est visible seulement en lisant les deux ensemble, et cela dit quelque chose sur la stratégie éditoriale.
  | | *Projects in Buzz* (engineering) | *Designing AI with character* (corporate) |
  |---|---|---|
  | **Diagnostic d'ouverture** | *« Software development tools are **fragmented** in ways the work itself is not. »* | *« The technology was powerful, but the experience around it was **fragmented**. »* |
  | **Objet fragmenté** | les outils du cycle de développement | les interfaces et systèmes de configuration des agents |
  | **Remède** | tout ramener sur **un relais** | tout ramener dans **un client de bureau** |
  | **Chute** | Buzz | **Buzz** |
  → ⭐ **Le même mot, deux échelles, une seule destination.** **Formulation à retenir : Block instruit publiquement une thèse unique — la valeur n'est plus dans le modèle ni dans le harnais, elle est dans l'environnement qui les entoure** — et la décline au poste de travail (Berd) puis au réseau (Buzz). ⚠️ **Et la conséquence pour le dossier** : ce billet **ne comble aucun des manques du dossier Buzz** relevés le 18 août — toujours aucune mesure d'usage produite par un tiers, sur cinq textes maison en un mois. **Il l'élargit sans le documenter.**

- **⭐ Ce que Berd lègue à Buzz est écrit noir sur blanc — et c'est une liste de spécifications déguisée en bilan.** Verbatim : *« Berd showed us the importance of **private space, durable context, recognizable agent identities, reusable skills, visible configuration, and clearer visibility into an agent's configured context, tools, and capabilities**. Buzz gives those ideas somewhere to go when individual work becomes collaborative. »*
  → ⭐ **Six exigences, énoncées comme acquises côté Berd et attendues côté Buzz.** ⚠️ **Deux d'entre elles — *« visible configuration »* et *« clearer visibility into an agent's configured context, tools, and capabilities »* — sont exactement ce que le billet n'a démontré nulle part**, puisque sa démonstration porte sur l'avatar. **La liste vaut donc mieux que le texte qui la porte : c'est une bonne grille d'évaluation d'un client d'agents, à réutiliser telle quelle.** ⭐ **Et elle croise directement la question de la portabilité** de [[janakiram-agent-platform-portability-contract-2026-07-20]] : *« reusable skills »* n'a de sens que si les skills sont portables entre clients — voir le packaging de [[google-agent-plugins-packaging-skills-mcp-2026-08-06]]. **Le billet ne dit pas si les agents et skills de Berd sont transposables ailleurs.** **Question à poser en premier.**

- **⭐ « Start alone, then go multiplayer » : la seule proposition du billet qui soit une thèse produit falsifiable.** Verbatim : *« Work with an agent often begins alone. You research, experiment, gather context, and shape an idea before it is ready for other people… **But work rarely stays private.** »*
  → ⭐ **C'est une hypothèse sur le cycle de vie du travail assisté, et elle est bonne** : elle explique pourquoi un espace privé durable précède l'espace partagé, et pourquoi les deux ne sont pas le même produit. Elle répond aussi, indirectement, à la question posée par [[chatgpt-claude-desktop-vs-web-deep-research-2026-08-12]] sur ce que justifie une application de bureau — **la réponse de Block est : le contexte privé durable**. ⚠️ **Elle n'est étayée par rien** : ni observation, ni mesure, ni proportion de travail qui « devient » collaboratif. **Reprendre comme cadre de conception, jamais comme constat.** ⭐ **Et le contrepoint est disponible dans le corpus** : [[patel-block-buzz-teams-tokens-benchmarks-2026-08-06]] mesurait, chez Block même, des **compositions d'équipes** d'agents — c'est-à-dire du travail qui **commence** multijoueur. **Les deux textes de Block ne décrivent pas la même trajectoire.**

- **⚠️ L'ouverture du code est annoncée sans licence, et la comparaison avec goose est instructive.** Verbatim : *« Today, we're making Berd open source, sharing the application, and the design and technical lessons behind it for others to inspect, use, and adapt. »* **Aucune licence n'est nommée dans le billet.**
  | | goose | Berd |
  |---|---|---|
  | Dépôt au 18 août 2026 | `github.com/**aaif-goose**/goose` | `github.com/**block**/berd` |
  | Gouvernance | **Agentic AI Foundation** (Linux Foundation) | **Block** |
  | Licence annoncée dans le billet | — | **aucune** |
  → ⭐ **Le détail qui compte : goose a changé d'organisation GitHub, Berd non.** *« Open source »* et *« gouvernance neutre »* sont deux choses distinctes, et le billet ne revendique la seconde que pour goose. ⚠️ **Formulation correcte : Berd est un code ouvert publié par Block, pas un projet de fondation.** **Vérifier la licence dans le dépôt avant toute reprise** — c'est une vérification de dix minutes que ce billet n'épargne pas.

- **⚠️ Une imprécision de chronologie sur goose, à corriger en reprise.** Le billet écrit : *« In December 2025, Block joined Anthropic, OpenAI, and others to establish the Agentic AI Foundation under the Linux Foundation. **We later contributed goose** to the foundation. »* Or [[openai-agentic-ai-foundation-linux-2025-12-09]] établit que **chaque cofondateur apportait un projet dès l'annonce de fondation** — OpenAI `AGENTS.md`, Anthropic **MCP**, **Block goose**. → **Le *« later »* décrit vraisemblablement le transfert effectif du dépôt (cohérent avec l'org `aaif-goose`), pas l'engagement.** ⚠️ **Formulation correcte : goose est la contribution de Block annoncée à la fondation de l'AAIF en décembre 2025 ; le transfert du dépôt est intervenu ensuite.** **Ne pas propager le *« later »* comme s'il datait la décision.** ⭐ **Et un fait de fond à retenir** : goose est dans le corpus depuis [[block-goose-mcp-ui-future-agentic-interfaces-2025-08-25]] et [[mcp-ui-future-agentic-interfaces-goose-2025-08-25]] — **un an de continuité**, du framework agentique à la fondation neutre puis au client de bureau. **Peu d'acteurs du corpus tiennent une ligne aussi droite sur douze mois.**

- **⚠️ Hygiène de citation pour cette fiche — cinq règles.**
  1. **Ne jamais citer ce billet comme preuve d'un effet.** Zéro chiffre, zéro test utilisateur, zéro donnée d'adoption. **Ce qui est citable : la doctrine de design de Block et l'architecture Berd↔goose↔ACP.**
  2. **Ne pas déclarer Berd abandonné.** Le texte est un rétrospectif qui donne la suite à Buzz ; il décrit le produit au présent et invite à le télécharger. **Formulation exacte : le futur annoncé est celui de Buzz ; Berd n'est pas déclaré déprécié.**
  3. **Ne pas reprendre *« any task they want »***. Surpromesse sans exemple ; c'est la seule phrase du billet qui sorte du registre sobre du reste.
  4. **Ne pas attribuer à ce billet les faits d'architecture de Buzz.** Le relais unique, l'absence de réplication, les événements signés : cela vient de [[buzz-block-panorama-deep-research-2026-08-12]] et de [[petersen-block-buzz-projects-forge-souveraine-2026-08-18]], **pas d'ici** — ce texte ne dit de Buzz que sa fonction.
  5. **Vérifier la licence et l'état du dépôt `github.com/block/berd`** avant de qualifier l'ouverture. Le billet n'en dit rien.

- **Ce que ce billet ouvre dans le corpus, et qui n'y était pas.** ⭐ **C'est la première fiche à traiter le *caractère* et l'**identité visuelle** d'un agent comme une question de conception à part entière** — l'anthropomorphisme des agents n'est documenté nulle part ailleurs dans le catalogue. **Le sujet mérite d'être suivi, et la bonne question à lui poser est déjà formulable** : *à quelles conditions donner un visage à un agent améliore-t-il le jugement de l'utilisateur sur ce que l'agent peut faire, plutôt que sa disposition à lui faire confiance ?* ⚠️ **Aucun des textes du corpus, celui-ci compris, n'apporte le moindre élément de réponse empirique.** **Fiche à rouvrir si Block publie les leçons de design promises dans le dépôt** — *« sharing… the design and technical lessons behind it »* est un engagement, et il est vérifiable.

## RésuméDe400mots

Billet du blog corporate de **Block** (`block.xyz/inside`), **non signé**, publié le **18 août 2026**, qui annonce **l'ouverture du code de Berd** et expose la thèse de conception qui l'a guidée.

**Ce qu'est Berd.** *« Berd is a desktop application our teams use to work with AI agents across projects, skills, tools, and models. »* Née d'un problème interne : Block avait accès à des agents capables — **goose**, **Claude Code**, **Codex** — mais chacun imposait *« different interfaces, configuration systems, and ways of managing context »*. Conclusion tirée : *« we didn't need another model or agent harness, **we needed a consistent environment around them** »*. Berd rassemble conversations, fichiers, dossiers, instructions, agents et skills autour de **projets persistants**, pour cesser de reconstruire le contexte à chaque tâche.

**La thèse de design.** Donner du **caractère** aux agents — non seulement par les rôles, instructions, skills et outils, mais par des **identités visuelles distinctes**, dont une collection de personnages animés, les *« Gloopies »*. Le problème invoqué est celui de la boîte de saisie vide : *« the product gives people little sense of how the agent is configured, which context and tools are available to it, and how it differs from another agent »*. Le billet inscrit la démarche dans la lignée de **Square** et **Cash App** — apporter du design là où la catégorie n'en avait pas. ⚠️ **Mais le problème posé est un problème de lisibilité de la configuration, et l'avatar résout la distinguabilité** ; le texte le reconnaît en une ligne qu'il ne développe pas : *« The avatars make the agent recognizable. **Its role, skills, and tools make it useful.** »*

**L'architecture.** Berd descend de **goose**, framework d'agent open source lancé par Block en **janvier 2025**, contribué à l'**Agentic AI Foundation** (Linux Foundation, décembre 2025) aux côtés de **MCP** et d'**AGENTS.md**. Répartition explicite : *« goose remains the open agent framework and runtime. Berd is a desktop application built around it. **Berd connects to goose through the Agent Client Protocol.** »* goose tient la boucle d'agent, Berd tient l'expérience.

**La suite est Buzz.** Berd a servi à explorer le travail **solo** ; *« But work rarely stays private »*. Ce que Berd a montré — *« private space, durable context, recognizable agent identities, reusable skills, visible configuration »* — nourrira **Buzz**, l'espace partagé humains+agents. *« Start alone, then go multiplayer. »*

**Réserves.** ⚠️ **Aucun chiffre, aucun test utilisateur, aucune licence nommée** ; une surpromesse isolée (*« create custom agents to do any task they want »*) ; et un billet dont le titre annonce un rétrospectif tout en maintenant le produit au présent — **Berd n'est pas déclaré déprécié, mais la feuille de route va à Buzz**.

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
