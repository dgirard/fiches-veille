---
themes: [architecture-construction, outils-plateformes, agents-codage-ia-skills, qualite-securite]
source: "Block Engineering"
---
# petersen-block-buzz-projects-forge-souveraine-2026-08-18

## Veille

Billet d'annonce produit de **Block Engineering** signé **Thomas Petersen** (*Principal Designer & Builder*), publié le **18 août 2026**, ~1 800 mots en treize sections courtes, présentant **Buzz Projects** — une **forge logicielle hébergée sur son propre relais** : dépôts Git, branches, pull requests, issues, revue et fusion, projets multi-dépôts, fil d'activité, le tout lié aux canaux de conversation. Chapeau et thèse du billet : *« Coding agents are the terminal for your computer. Buzz is the terminal for your network. »* Trois apports. **(A) Une doctrine de la confiance fondée sur la preuve *ex post* plutôt que sur l'autorisation *ex ante*** : d'un côté *« No forced guardrails, no limitations on what your agents are allowed to help you with »*, de l'autre *« Every push, review, approval, and merge is a signed Nostr event. If an agent authors a patch, you can see which agent produced it and which human authorized that agent to act »* ; la section se clôt sur une piste déclarée — *« we are already exploring ideas around agent trust protocols informed by past behavior »*. **(B) Une interopérabilité Git sans outillage propriétaire** : *« These are standard git repositories… You can fetch, clone, pull, and push over plain Smart HTTP, with no custom tooling or wrapper CLI required »*, la clé Nostr servant d'identité unique — *« The same npub that signs your messages signs your pushes. »* **(C) Une distinction entre surface d'exécution et présence réseau** : *« A terminal gives an agent somewhere to execute commands and change files, but it does not give it a persistent place in the network. Buzz does. »* Le billet ne produit aucun chiffre et ne comporte aucun lien sortant ; il se qualifie six fois de préliminaire (*« still very basic »*, *« fairly elementary »*, *« still under experiments »*) et Projects vit sous l'onglet **Experiments** de Buzz Desktop.

## Titre Article

Projects in Buzz

## Date

2026-08-18

## URL

https://engineering.block.xyz/blog/projects-in-buzz

## Keywords

Buzz, Buzz Projects, Block, Block Engineering, Thomas Petersen, forge logicielle, software forge, relais, relay, Nostr, npub, identité portable, événement signé, signed Nostr event, git hébergé, hosted git, Smart HTTP, fetch clone pull push, sans outillage propriétaire, projet multi-dépôts, pull request, issue, revue de code, diff, merge, CI, notes de version, fil d'activité, onglet Experiments, Buzz Desktop, liaison projet-canal, contexte partagé, context is all you need, historique de contribution, historique vérifiable, réputation d'agent, agent trust protocols, comportement passé, autorisation ex ante, preuve ex post, no forced guardrails, souveraineté, protocole ouvert, terminal pour votre réseau, présence persistante dans le réseau, fragmentation de l'outillage, bêta, expérimental, AIArchitecture

## Authors

**Thomas Petersen** — *« Principal Designer & Builder »* chez **Block**, auteur unique et signataire du billet ; première apparition dans le corpus. Publié le **18 août 2026** sur le blog **Block Engineering**. Troisième signature Block sur Buzz en un mois, après Tyler Longwell (21 juillet) et Atish Patel (6 août), et la première non-ingénieur.

## Ton

**Profil** : manifeste produit en visite guidée — ~1 800 mots, treize sections courtes titrées par des slogans, une capture d'écran par fonctionnalité. Public : utilisateurs existants de Buzz Desktop (*« If you've used Buzz Desktop recently and happened to click on the Experiments tab… »*) et, en creux, quiconque évalue une alternative à GitHub. Une démonstration commentée assortie d'une position, ni exposé de design ni benchmark.

**Style** : la page est encadrée de fausses invites shell — `$ cd ~`, `$ find .`, `$ git blame`, `$ cat content.md`, `$ echo "Copyright 2026 Block, Inc."` : le chapeau annonce *« Buzz is the terminal for your network »* et la mise en page le met en scène. Les titres de section sont des thèses plutôt que des descriptions (*« Context is (almost) all you need »*, *« All conversations lead to projects and back »*, *« Your project, your relay »*, *« Autonomy, sovereignty and the big picture »*) ; le *« (almost) »* du premier est le seul hedge du texte et n'est jamais développé. L'auto-limitation est systématique : six désaveux explicites, dont un *Disclaimer* nominatif en dernière ligne — *« Buzz is still in beta and Buzz Projects is still under experiments, so treat it accordingly. »* La prose est écrite vite, avec deux phrases cassées dans l'original : l'une sans sujet grammatical (*« Whether we are talking repos, branches, pull requests, issues, CI, or all the related conversations gives you and your agents unique identities that you control »*), l'autre avec un verbe amputé (*« new scenarios we have solve »*). Le « nous » du produit remplace le « je » de l'ingénieur : *« We believe those things belong together »*, *« we think this distinction will become increasingly important »*.

**Formules-marqueurs** :
- ***« Coding agents are the terminal for your computer. Buzz is the terminal for your network. »***
- ***« Software development tools are fragmented in ways the work itself is not. »***
- ***« The history becomes part of the project itself. »***
- ***« No forced guardrails, no limitations on what your agents are allowed to help you with. »***
- ***« a software forge that lives on your relay, letting you own all the relationships »***
- ***« The same npub that signs your messages signs your pushes. »***
- ***« no two agents in Buzz work the same way because they have different context. They have different context because they have a different history. »***
- ***« Every push, review, approval, and merge is a signed Nostr event. »***
- ***« more than a set of colored squares on a profile »***
- ***« agent trust protocols informed by past behavior »***
- ***« A terminal gives an agent somewhere to execute commands and change files, but it does not give it a persistent place in the network. Buzz does. »***
- ***« either way the protocol is open and the events are yours »***

**Position épistémique** : doctrine de conception illustrée par des captures d'écran, sans aucune donnée — pas un utilisateur, pas un dépôt, pas une durée, pas un coût, pas un benchmark — et sans aucun lien sortant sur toute la page. Citable comme position architecturale de Block sur ce que devrait être une forge à l'ère des agents ; ne l'est ni comme preuve de fonctionnement, ni comme indication d'adoption.

## Pense-betes

- **Date / source** : **18 août 2026**, blog **Block Engineering**, ~1 800 mots, signé **Thomas Petersen** (*Principal Designer & Builder*). Aucun lien sortant, aucun chiffre.
- **Cadrage clé** : Buzz Projects est une forge dont la **conversation est un artefact de premier rang** — les projets sont liés aux canaux, et *« Instead of reconstructing why something happened after the fact, the history is already there. »*

### Le modèle de confiance : deux paragraphes à lire ensemble

| Section du billet | Verbatim | Ce qu'il installe |
|---|---|---|
| *First Class Citizens* | *« No forced guardrails, no limitations on what your agents are allowed to help you with. No limits to how much you can delegate to your agents in the network. »* | suppression de la contrainte préalable |
| *Weaving it all together* | *« Every push, review, approval, and merge is a signed Nostr event. If an agent authors a patch, you can see which agent produced it and which human authorized that agent to act. »* | enregistrement signé de l'acte |
| même paragraphe, fin | *« we are already exploring ideas around agent trust protocols informed by past behavior »* | dérivation de la confiance depuis l'historique |

La position est architecturale : dans un réseau où la délégation est illimitée, l'autorisation *a priori* passe mal à l'échelle, la signature oui. C'est la version « réseau » de ce que [[longwell-block-buzz-workspace-agents-nostr-2026-07-21]] posait en juillet au niveau de l'identité (*« authorization does not erase authorship »*). Deux limites que le billet n'aborde pas : un enregistrement *ex post* ne prévient pas le premier dommage, et un historique signé prouve ce qui a été fait, non l'exhaustivité de ce qui est présenté — un registre négatif (PR refusées, régressions, incidents) serait nécessaire à une réputation, et n'est pas mentionné.

### Ce que la signature garantit, et ce qu'elle ne garantit pas

| Garanti | Non garanti |
|---|---|
| l'événement a bien été produit par cette clé | que la clé ait produit **tout** ce qu'on en montre |
| l'intégrité de chaque événement isolé | l'**exhaustivité** du lot présenté |
| le lien agent → humain autorisant | la **découvrabilité** des événements hors du relais d'origine |

Point d'architecture à ne pas attribuer à ce billet : le relais est source unique de vérité, sans réplication ni échange pair-à-pair. Cela vient de l'`ARCHITECTURE.md` de Block consolidé dans [[buzz-block-panorama-deep-research-2026-08-12]], et non de ce texte, qui n'en dit rien. Conséquence : la souveraineté proposée est un **droit de sortie**, pas une garantie de disponibilité.

### Interopérabilité Git : l'affirmation la plus vérifiable

Verbatim : *« These are standard git repositories, like you already know them… You can fetch, clone, pull, and push over plain Smart HTTP, with no custom tooling or wrapper CLI required. Your Nostr key is your identity throughout the process… You do not need another account, another identity, a separate token, or a GitHub account connected in the background. »*

Conséquences : le coût de sortie est faible par construction (un `git clone` récupère le code) et l'identité unique supprime la gestion de jetons. Nuance à conserver : **seul le code est standard** — la conversation, la revue, la liaison PR↔canal et l'historique de contribution vivent dans des *event kinds* Nostr propres à Buzz. Test réalisable en dix minutes : `clone` puis `push` depuis un client Git nu contre un relais Buzz, sans le CLI `buzz`.

### Inventaire annoncé vs inventaire livré

Le premier paragraphe énumère six fragments à réunir ; la section *« What's next? »* liste ce qui existe.

| Fragment nommé en ouverture | Présent dans l'inventaire du 18 août |
|---|---|
| *« A bug report lands in one tool »* | oui — issues |
| *« The discussion happens in another »* | oui — canaux liés au projet |
| *« The fix lives on a branch somewhere else »* | oui — *hosted git*, multi-dépôts |
| *« Review happens in a comment thread attached to a diff »* | oui — PR, revues, commentaires en ligne |
| *« CI runs in another system »* | **non** — citée dans les promesses, absente de l'inventaire |
| *« Release notes get written later »* | **non** |

Six fragments annoncés, quatre traités. Ne pas reprendre la liste « repos, branches, pull requests, issues, CI, or all the related conversations » comme un inventaire de fonctionnalités livrées.

### Distinction à réutiliser : exécuter n'est pas être présent

| Ce qu'un terminal donne à un agent | Ce qu'une présence réseau ajoute |
|---|---|
| exécuter, écrire des fichiers | une **identité stable** que d'autres peuvent adresser |
| un état local, jetable | un **historique attaché** qui survit à la session |
| agir | **être tenu pour responsable** de ce qui a été fait |

Cadre utile pour arbitrer entre un agent-outil (qu'on invoque) et un agent-membre (qu'on adresse). Corollaire non traité par le billet : une présence persistante est aussi une surface d'attaque persistante — voir [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]].

### « Context is (almost) all you need »

Verbatim : *« The more context we can make available, the better equipped the agents are, the more intelligent the whole network becomes. »* La monotonie est postulée sans être argumentée : ni le coût du contexte, ni sa dégradation, ni sa sélection ne sont discutés, et le *« (almost) »* n'est jamais explicité. À mettre en regard du budget de tokens chiffré chez Block même par [[patel-block-buzz-teams-tokens-benchmarks-2026-08-06]].

### Seule affirmation d'effet du billet

*« We've already seen a number of examples where agents understood context humans didn't and helped course correct otherwise unproductive directions. »* Aucun exemple, aucun nombre, aucun critère de succès. Formulation correcte pour une reprise : *« Block rapporte, sans les documenter, des cas où des agents ont réorienté des directions improductives à partir du contexte de canal. »* Fiche à rouvrir si Block publie ces cas.

### Hygiène de citation

1. Citable comme **intention architecturale** de Block ; pas comme preuve de fonctionnement ni d'adoption.
2. Toujours porter la maturité annoncée : onglet **Experiments**, *« fairly elementary »*, Buzz *« still in beta »*.
3. Distinguer les fonctionnalités montrées en capture, celles inventoriées dans *« What's next? »*, et celles seulement nommées dans les phrases de promesse (CI, notes de version).
4. Les *« agent trust protocols »* sont une piste déclarée, sans schéma ni critère ni calendrier.

## RésuméDe400mots

Billet d'annonce de **Block Engineering** signé **Thomas Petersen** (*Principal Designer & Builder*), publié le **18 août 2026**, présentant **Buzz Projects** — la brique forge de **Buzz**, le workspace humains+agents de Block bâti sur **Nostr**.

**Le problème posé.** *« Software development tools are fragmented in ways the work itself is not. »* Le rapport de bug est dans un outil, la discussion dans un autre, le correctif sur une branche, la CI ailleurs, la revue dans un fil de commentaires, les notes de version reconstituées après coup. **La thèse : tout cela est une seule conversation, et l'historique doit faire partie du projet.**

**Ce que Projects apporte.** Une **forge hébergée sur votre propre relais** : dépôts Git standards accessibles en `fetch/clone/pull/push` sur **Smart HTTP**, *« with no custom tooling or wrapper CLI required »* ; **la clé Nostr comme identité unique** — *« the same npub that signs your messages signs your pushes »*, sans jeton séparé ni compte GitHub ; des **projets multi-dépôts** pouvant inclure des dépôts qu'on ne possède pas (*« you just won't have authority over it »*) ; issues, pull requests, diffs, commentaires en ligne, revue et fusion ; un **fil d'activité** à l'échelle du serveur ; et la **liaison de tout projet à un nombre quelconque de canaux**, de sorte que *« le contexte autour d'un changement ne disparaît pas au moment où les agents se mettent à écrire du code »*. Depuis un canal, on peut confier une issue à un agent ou lui demander d'ouvrir une PR, laquelle renvoie à la conversation qui l'a produite ; l'agent sollicite l'humain via l'**Inbox**.

**La doctrine, en deux temps que le billet n'assemble pas.** D'un côté, **aucune contrainte préalable** : *« No forced guardrails, no limitations on what your agents are allowed to help you with. »* De l'autre, **un enregistrement signé de tout acte** : *« Every push, review, approval, and merge is a signed Nostr event »*, avec la trace de **quel agent** a produit un patch et **quel humain** l'y avait autorisé. D'où la projection finale : l'historique de contribution devient *« more than a set of colored squares on a profile »*, un **historique vérifiable attaché à une clé**, et Block déclare **explorer des *« agent trust protocols informed by past behavior »***. **La confiance bascule de l'autorisation *ex ante* à la preuve *ex post*.** Le cadre associé est net : *« A terminal gives an agent somewhere to execute commands and change files, but it does not give it a persistent place in the network. Buzz does. »*

**Réserves.** **Aucun chiffre, aucun lien sortant, aucune spécification** dans tout le texte ; **CI et notes de version sont promises mais absentes de l'inventaire** ; Projects vit sous **l'onglet Experiments** et le billet se disqualifie six fois — *« Buzz is still in beta and Buzz Projects is still under experiments, so treat it accordingly. »*

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Thomas Petersen | PERSONNE | travaille_chez | Block | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Block | ORGANISATION | publie | Buzz Projects | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Buzz Projects | TECHNOLOGIE | fait_partie_de | Buzz | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Buzz Projects | TECHNOLOGIE | est_instance_de | forge logicielle souveraine | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Buzz Projects | TECHNOLOGIE | utilise | Nostr | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Buzz Projects | TECHNOLOGIE | utilise | Git | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Buzz Projects | TECHNOLOGIE | utilise | Smart HTTP | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Buzz Projects | TECHNOLOGIE | observé_dans | Buzz Desktop | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| clé Nostr | TECHNOLOGIE | permet | authentification Git par clé Nostr | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Buzz Projects | TECHNOLOGIE | résout | fragmentation de l'outillage de développement | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Buzz Projects | TECHNOLOGIE | réduit | reconstruction a posteriori du contexte | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Buzz Projects | TECHNOLOGIE | permet | historique de contribution vérifiable | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| historique de contribution vérifiable | CONCEPT | est_basé_sur | événement Nostr signé | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| protocoles de confiance des agents | CONCEPT | est_basé_sur | historique de contribution vérifiable | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | affirme_que | "we are already exploring ideas around agent trust protocols informed by past behavior" | CITATION | 0.96 | DYNAMIQUE | déclaré_article |
| Thomas Petersen | PERSONNE | affirme_que | "Coding agents are the terminal for your computer. Buzz is the terminal for your network." | CITATION | 0.98 | STATIQUE | déclaré_article |
| Thomas Petersen | PERSONNE | affirme_que | "No forced guardrails, no limitations on what your agents are allowed to help you with." | CITATION | 0.97 | STATIQUE | déclaré_article |
| Thomas Petersen | PERSONNE | affirme_que | "A terminal gives an agent somewhere to execute commands and change files, but it does not give it a persistent place in the network." | CITATION | 0.97 | ATEMPOREL | déclaré_article |
| Thomas Petersen | PERSONNE | affirme_que | « la clé Nostr qui signe les messages signe aussi les pushes Git, sans compte ni jeton supplémentaire » | AFFIRMATION | 0.96 | STATIQUE | déclaré_article |
| Thomas Petersen | PERSONNE | prédit | « l'historique de contribution deviendra un historique vérifiable attaché à la clé du contributeur, portable entre projets et entre réseaux » | AFFIRMATION | 0.90 | DYNAMIQUE | déclaré_article |
| Thomas Petersen | PERSONNE | affirme_que | « des agents ont compris un contexte que des humains n'avaient pas et ont réorienté des directions improductives » | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| Buzz Projects | TECHNOLOGIE | s_applique_à | souveraineté organisationnelle | CONCEPT | 0.90 | ATEMPOREL | inféré |
| Buzz Projects | TECHNOLOGIE | concurrence | GitHub | TECHNOLOGIE | 0.86 | DYNAMIQUE | inféré |
| Buzz Projects | TECHNOLOGIE | s_oppose_à | autorisation ex ante des agents | CONCEPT | 0.85 | ATEMPOREL | inféré |
| souveraineté organisationnelle | CONCEPT | s_applique_à | relais Buzz | TECHNOLOGIE | 0.88 | ATEMPOREL | inféré |
| Buzz | TECHNOLOGIE | affine | forge logicielle souveraine | CONCEPT | 0.84 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Thomas Petersen | PERSONNE | rôle | Principal Designer & Builder chez Block ; première fiche du corpus | AJOUT |
| Block | ORGANISATION | rôle | Éditeur de Buzz ; troisième signature interne sur le produit en un mois | MISE_A_JOUR |
| Buzz | TECHNOLOGIE | statut | Workspace humains+agents sur Nostr, en bêta au 18 août 2026 | MISE_A_JOUR |
| Buzz Projects | TECHNOLOGIE | catégorie | Forge logicielle hébergée sur relais : multi-dépôts, git, PR, issues, historique de contribution | AJOUT |
| Buzz Projects | TECHNOLOGIE | maturité | Expérimental — onglet Experiments de Buzz Desktop, « fairly elementary », CI et notes de version absentes de l'inventaire | AJOUT |
| Buzz Desktop | TECHNOLOGIE | rôle | Client où Projects est exposé sous l'onglet Experiments | AJOUT |
| Nostr | TECHNOLOGIE | rôle | Substrat d'identité et d'événements signés de la forge | AJOUT |
| Git | TECHNOLOGIE | rôle | Dépôts standards hébergés sur le relais, sans wrapper propriétaire | AJOUT |
| Smart HTTP | TECHNOLOGIE | rôle | Transport de fetch/clone/pull/push vers un dépôt Buzz | AJOUT |
| clé Nostr | TECHNOLOGIE | rôle | Identité unique : signe les messages et les pushes Git | AJOUT |
| authentification Git par clé Nostr | CONCEPT | définition | Une seule paire de clés pour la conversation et le dépôt — ni jeton dédié, ni compte GitHub tiers | AJOUT |
| relais Buzz | TECHNOLOGIE | limite | Source de vérité unique — la souveraineté promise est un droit de sortie, pas une redondance | AJOUT |
| forge logicielle souveraine | CONCEPT | définition | Forge vivant sur un relais possédé, dont les identités et les événements appartiennent à l'utilisateur | AJOUT |
| historique de contribution vérifiable | CONCEPT | définition | Historique signé attaché à une clé, présenté comme portable entre projets et réseaux | AJOUT |
| historique de contribution vérifiable | CONCEPT | limite | Prouve ce qui a été fait, jamais ce qui ne l'a pas été : exhaustivité et registre négatif non garantis | AJOUT |
| protocoles de confiance des agents | CONCEPT | statut | Piste de recherche déclarée par Block — aucun critère, schéma ni calendrier publié | AJOUT |
| autorisation ex ante des agents | CONCEPT | définition | Restriction préalable de ce qu'un agent a le droit de faire — explicitement écartée par le billet | AJOUT |
| souveraineté organisationnelle | CONCEPT | précision | Propriété des événements et droit de sortie, distincts de la disponibilité et de la résistance à l'altération | AJOUT |
| fragmentation de l'outillage de développement | CONCEPT | définition | Dispersion du bug, de la discussion, de la branche, de la CI, de la revue et des notes de version entre outils distincts | AJOUT |
| reconstruction a posteriori du contexte | CONCEPT | définition | Coût de retrouver après coup pourquoi une décision a été prise ; ce que la liaison projet↔canal prétend supprimer | AJOUT |
| événement Nostr signé | CONCEPT | portée | Push, revue, approbation et fusion ; porte l'agent auteur et l'humain qui l'a autorisé | AJOUT |
| GitHub | TECHNOLOGIE | rôle | Référence implicite dont le billet se démarque (« colored squares on a profile ») | AJOUT |
