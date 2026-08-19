---
themes: [architecture-construction, outils-plateformes, agents-codage-ia-skills, qualite-securite]
source: "Block Engineering"
---
# petersen-block-buzz-projects-forge-souveraine-2026-08-18

## Veille

Billet d'annonce produit de **Block Engineering** signé **Thomas Petersen** (*Principal Designer & Builder*), publié le **18 août 2026**, présentant **Buzz Projects** — une **forge logicielle hébergée sur votre propre relais** : dépôts Git, branches, pull requests, issues, revue et fusion, projets multi-dépôts, fil d'activité, le tout lié aux canaux de conversation. Chapeau du billet, qui est aussi sa thèse : *« Coding agents are the terminal for your computer. Buzz is the terminal for your network. »* ⭐⭐ **Le sujet annoncé est une forge ; le vrai sujet est une doctrine de la confiance qui bascule de l'autorisation *ex ante* à la preuve *ex post*** — et elle est énoncée dans **deux paragraphes qui ne se citent jamais l'un l'autre**. Le premier supprime la contrainte préalable : *« No forced guardrails, no limitations on what your agents are allowed to help you with. No limits to how much you can delegate to your agents in the network. »* Le second installe l'enregistrement : *« Every push, review, approval, and merge is a signed Nostr event. If an agent authors a patch, you can see which agent produced it and which human authorized that agent to act »*, puis, en une phrase glissée en fin de section, la conséquence la plus lourde du billet — *« we are already exploring ideas around **agent trust protocols informed by past behavior** »*. → **Buzz ne restreint pas ce qu'un agent a le droit de faire ; il enregistre de façon signée ce qu'il a fait, et propose d'en dériver la confiance.** ⚠️ **La limite de ce modèle est structurelle et le billet ne l'aborde pas** : un historique *ex post* n'empêche pas le premier dommage, et une réputation qu'on présente soi-même prouve ce qu'on a fait, jamais ce qu'on n'a pas fait. ⭐⭐ **Deuxième renversement, corpus-only** : c'est le **quatrième texte Buzz du corpus** et **le seul sans un seul chiffre** — ni benchmark, ni coût, ni adoption, ni spécification, **et sans un seul lien sortant**. Là où [[longwell-block-buzz-workspace-agents-nostr-2026-07-21]] apportait un protocole model-checké en TLA+ et [[patel-block-buzz-teams-tokens-benchmarks-2026-08-06]] des tableaux de prix et de scores, ce billet apporte **des captures d'écran et une doctrine**. ⭐ **À son crédit, il ne prétend pas le contraire** : il se disqualifie lui-même six fois (*« still very basic »*, *« fairly elementary »*, *« isn't as built out as the CLI tools yet »*, *« some shortcomings »*, *« still under experiments »*, plus un *Disclaimer* final). **Citer l'intention de conception, jamais l'état du produit.**

## Titre Article

Projects in Buzz

## Date

2026-08-18

## URL

https://engineering.block.xyz/blog/projects-in-buzz

## Keywords

Buzz, Buzz Projects, Block, Block Engineering, Thomas Petersen, forge logicielle, software forge, forge souveraine, relais, relay, Nostr, npub, clé Nostr, identité portable, événement signé, signed Nostr event, git hébergé, hosted git, Smart HTTP, fetch clone pull push, sans outillage propriétaire, no wrapper CLI, pas de token séparé, pas de compte GitHub, projet multi-dépôts, multi repo, dépôt que l'on ne possède pas, autorité sur le dépôt, pull request, issue, revue de code, inline comments, diff, merge, CI, notes de version, fil d'activité, activity feed, onglet Experiments, Buzz Desktop, Inbox, liaison projet-canal, bind to channels, conversation comme artefact, contexte partagé, context is all you need, index de recherche commun, même système d'identité, historique de contribution, contribution history, colored squares, historique vérifiable, verifiable history, réputation d'agent, protocoles de confiance des agents, agent trust protocols, comportement passé, past behavior, qui a autorisé l'agent, authorship vs authorization, autorisation ex ante, preuve ex post, garde-fous, no forced guardrails, absence de bac à sable, souveraineté, sovereignty, votre relais votre domaine, opérateur hébergeur, protocole ouvert, les événements sont à vous, terminal pour votre réseau, place persistante dans le réseau, persistent place in the network, surface d'exécution, fragmentation de l'outillage, agents conscients les uns des autres, agents aware of each other, course correct, bêta, expérimental, aucun chiffre, aucun lien sortant, AIArchitecture

## Authors

**Thomas Petersen** — *« Principal Designer & Builder »* chez **Block**. Auteur unique, signataire du billet ; **absent du corpus jusqu'ici** — c'est sa première fiche.

⚠️ **Ce que le dispositif d'énonciation implique.**

1. **Troisième signature Block sur Buzz en un mois, et la première non-ingénieur.** Le corpus tient désormais trois auteurs pour un même produit, et **leur fonction prédit le registre du texte** :
   | Date | Auteur | Fonction affichée | Ce que le billet apporte |
   |---|---|---|---|
   | **21 juil.** | Tyler Longwell | *« Building multi-player AI at Block »* | protocole Git sur stockage objet, **spécifié en TLA+ et model-checké**, suite de conformité |
   | **6 août** | Atish Patel | *« Building AI solutions @ Block »* | **12 compositions d'équipes**, coûts en dollars, scores Terminal-Bench, mode de défaillance nommé |
   | **18 août** | **Thomas Petersen** | ***Principal Designer & Builder*** | **visite guidée + doctrine**, captures d'écran, zéro mesure |
   → ⭐ **Ce n'est pas un reproche, c'est un calibrage.** Un designer publie une intention de conception ; c'est le bon auteur pour ce sujet. **Mais la conséquence de citation est directe** : les deux premiers billets sont opposables sur les faits, celui-ci ne l'est que sur les intentions.
2. **Le « nous » du produit remplace le « je » de l'ingénieur.** Longwell écrivait à la première personne et partait d'un échec vécu (son premier agent Slack chez Block). Petersen écrit exclusivement *« we »* : *« We believe those things belong together »*, *« we think this distinction will become increasingly important »*. **Passage du témoignage à la doctrine d'entreprise** — ce qui rend le texte plus citable comme position de Block, et moins comme retour d'expérience.
3. **Aucun lien sortant, sur toute la page.** Vérifié : les seuls `href` du document sont des ancres internes de sommaire, des assets et le pied de page corporate. **Ni dépôt, ni documentation, ni NIP, ni spécification, ni note de version.** Pour un billet qui annonce une forge *open source* hébergeable, c'est l'absence la plus notable — et elle contraste avec les deux précédents.
4. **Le billet est une sollicitation de retours, pas un lancement.** *« it's far enough along that we want to get your feedback. The good, the bad, the ugly, and the truth! »* — et Projects vit sous **l'onglet Experiments** de Buzz Desktop. ⚠️ **Ne pas le fiche comme une disponibilité générale.**
5. **Ce que le corpus permet de voir et que le billet ne dit pas.** Trois des affirmations du texte ont déjà été **qualifiées, chiffrées ou contredites** par [[buzz-block-panorama-deep-research-2026-08-12]], qui a consolidé l'état public de Buzz six jours plus tôt à partir de l'`ARCHITECTURE.md` de Block. **Le lecteur du seul billet ne peut pas les voir** ; elles sont traitées en pense-bêtes.

## Ton

**Profil** : **manifeste produit en visite guidée** — ~1 800 mots, treize sections courtes titrées par des slogans, une capture d'écran par fonctionnalité. Public : utilisateurs existants de Buzz Desktop (*« If you've used Buzz Desktop recently and happened to click on the Experiments tab… »*) et, en creux, quiconque évalue une alternative à GitHub. Ni exposé de design, ni benchmark, ni tribune : **une démonstration commentée assortie d'une position.**

**Style** : cinq traits.

1. **Le terminal n'est pas une métaphore du texte, c'est le design system de la page.** Le billet est encadré de fausses invites shell — `$ cd ~`, `$ find .`, `$ git blame`, `$ cat content.md`, `$cat tags`, `$ echo "Copyright 2026 Block, Inc."`. ⭐ **Venant d'un *Principal Designer*, c'est l'argument porté par la mise en page avant de l'être par la prose** : le chapeau dit *« Buzz is the terminal for your network »*, et la page se lit comme un terminal. **Cohérence rare ; à noter comme un fait de communication, pas comme une preuve technique.**
2. **Des titres de section qui sont des thèses, pas des descriptions.** *« Context is (almost) all you need »*, *« All conversations lead to projects and back »*, *« Weaving it all together »*, *« Your project, your relay »*, *« Autonomy, sovereignty and the big picture »*. ⚠️ **Le « (almost) » du premier est le seul hedge de tout le texte** — et il n'est jamais développé : on ne saura pas ce qui manque au contexte.
3. **L'auto-limitation systématique, et elle est honnête.** Six désaveux explicites, dont un *Disclaimer* nominatif en dernière ligne : *« Buzz is still in beta and Buzz Projects is still under experiments, so treat it accordingly. »* ⭐ **C'est plus prudent que la moyenne des annonces produit du corpus**, et cela doit être porté dans toute reprise — l'omettre rendrait la citation moins honnête que la source.
4. **La prose est visiblement écrite vite, et deux phrases sont cassées dans l'original.** *« Whether we are talking repos, branches, pull requests, issues, CI, or all the related conversations gives you and your agents unique identities that you control »* — **la phrase n'a pas de sujet grammatical**. Et *« which in turn will lead to new scenarios we have solve »* — verbe amputé. **Ce n'est pas un document relu comme une spécification ; c'est un billet de blog.** Le calibrer comme tel.
5. **L'argument le plus fort est placé le plus bas et présenté comme une aparté.** Les *« agent trust protocols informed by past behavior »* arrivent au dernier paragraphe de l'avant-dernière section de fond, introduits par *« we are already exploring ideas around »*. ⭐ **Placer sa proposition la plus lourde dans une incise exploratoire la met à l'abri de la contestation** — elle n'est pas présentée comme une affirmation. Le même procédé rhétorique que la note de terminologie de [[ng-ai-engineering-skills-map-2026-08-14]], quatre jours plus tôt.

**Formules-marqueurs** : *« Coding agents are the terminal for your computer. Buzz is the terminal for your network. »* · *« Software development tools are fragmented in ways the work itself is not. »* · *« We believe those things belong together as one complete story. »* · *« The history becomes part of the project itself. »* · *« agents are aware of each other and can help keep an eye out for things humans otherwise might miss »* · *« No forced guardrails, no limitations on what your agents are allowed to help you with. »* · *« Context is (almost) all you need »* · *« a software forge that lives on your relay, letting you own all the relationships »* · *« The same npub that signs your messages signs your pushes. »* · *« You don't need to own the repo to include it, you just won't have authority over it. »* · *« no two agents in Buzz work the same way because they have different context. They have different context because they have a different history. »* · *« the context surrounding a change does not have to disappear the moment agents start writing code »* · *« Instead of reconstructing why something happened after the fact, the history is already there. »* · *« Every push, review, approval, and merge is a signed Nostr event. »* · *« you can see which agent produced it and which human authorized that agent to act »* · *« more than a set of colored squares on a profile »* · *« agent trust protocols informed by past behavior »* · *« A terminal gives an agent somewhere to execute commands and change files, but it does not give it a persistent place in the network. Buzz does. »* · *« either way the protocol is open and the events are yours »* · *« The good, the bad, the ugly, and the truth! »*

**Position épistémique** : **doctrine de conception illustrée, sans aucune donnée.** Aucun chiffre d'aucune sorte n'apparaît dans le texte — pas un utilisateur, pas un dépôt, pas une durée, pas un coût, pas un benchmark. Les fonctionnalités sont attestées par des captures d'écran, non par des mesures. ⚠️ **Citer ce billet comme la position architecturale de Block sur ce que devrait être une forge à l'ère des agents. Ne jamais le citer comme preuve que Buzz Projects fonctionne, ni comme indication d'adoption.**

## Pense-betes

- **⭐⭐ La thèse réelle du billet tient dans deux paragraphes qui ne se répondent jamais : la confiance passe de l'autorisation *ex ante* à la preuve *ex post*.** Mis côte à côte, ils forment une doctrine cohérente que le texte n'assemble pas.
  | Paragraphe | Verbatim | Ce qu'il installe |
  |---|---|---|
  | *First Class Citizens* | *« **No forced guardrails**, no limitations on what your agents are allowed to help you with. No limits to how much you can delegate to your agents in the network. »* | **suppression de la contrainte préalable** |
  | *Weaving it all together* | *« Every push, review, approval, and merge is a **signed Nostr event**. If an agent authors a patch, you can see **which agent produced it and which human authorized that agent to act**. »* | **enregistrement infalsifiable de l'acte** |
  | même paragraphe, fin | *« we are already exploring ideas around **agent trust protocols informed by past behavior** »* | **dérivation de la confiance depuis l'historique** |
  → **La position est architecturale et elle est défendable** : dans un réseau où la délégation est illimitée, l'autorisation *a priori* ne passe pas à l'échelle, alors que la signature, oui. C'est la version « réseau » de ce que [[longwell-block-buzz-workspace-agents-nostr-2026-07-21]] posait en juillet au niveau de l'identité — *« authorization does not erase authorship »*. ⚠️ **Mais elle a deux trous que le billet n'ouvre pas** : (1) **un enregistrement ne prévient pas** — un `push` destructeur signé reste un `push` destructeur, et la traçabilité est un recours, pas un contrôle ; (2) voir le pense-bête suivant sur la falsifiabilité. **À opposer terme à terme à l'anneau de contraintes de [[sfeir-code-review-anneau-contraintes-2026-07-30]] et au SDLC sécurisé de [[clinton-anthropic-secure-ai-native-sdlc-2026-07-21]], qui font exactement le pari inverse : contraindre en amont.**

- **⭐⭐ Le trou logique de la réputation d'agent : on peut prouver ce qu'on a fait, jamais ce qu'on n'a pas fait.** Verbatim : *« contribution history can therefore become **more than a set of colored squares on a profile**. It can become a **verifiable history attached to a contributor's key that moves with them across projects and across the network**. »* → **La signature rend vérifiable un historique *présenté* ; rien ne rend cet historique *complet*.**
  | Ce que la signature garantit | Ce qu'elle ne garantit pas |
  |---|---|
  | l'événement produit **a bien** été produit par cette clé | que la clé ait produit **tout** ce qu'on en montre |
  | l'intégrité de chaque événement pris isolément | l'**exhaustivité** du lot présenté |
  | le lien agent → humain autorisant | la **découvrabilité** des événements sur un autre relais |
  → ⚠️ **Conséquence directe et non traitée** : *« informed by past behavior »* suppose un **registre négatif** — PR refusées, revues rejetées, régressions, incidents — et c'est exactement la partie qu'une partie qui se présente elle-même n'apporte pas. **Un système de réputation alimenté par le sujet lui-même mesure une activité, pas une fiabilité.** ⭐ **Et c'est le même mécanisme de panne que le corpus a déjà documenté deux fois cette semaine** : le *« pass nu »* de [[dumortier-marketing-ai-os-verification-2026-08-12]] (un vérificateur qui ne déclare pas sa couverture certifie ce qu'il ignore) et le principe de [[williams-adlc-4-prosecution-not-code-review-2026-06-12]] (la revue doit chercher à **réfuter**, pas à confirmer). **Le correctif est le même dans les trois cas : exiger la déclaration de ce qui n'a pas été vu.** ⭐ **Question à poser à Block, et bon test pour tout système de réputation d'agent** : *l'historique porte-t-il les échecs, et qui les y met ?*

- **⭐⭐ « Portable across the network » et l'architecture de Buzz ne disent pas la même chose — le corpus permet de trancher, le billet non.** Le texte promet un historique *« that moves with them across projects and across the network »* et une souveraineté par le relais : *« a project can live on your relay under your domain. You can run that relay yourself or use an operator to host it for you, but either way **the protocol is open and the events are yours** »*. Or [[buzz-block-panorama-deep-research-2026-08-12]] a établi, `ARCHITECTURE.md` en main : *« The relay is the single source of truth… There is no peer-to-peer event exchange, no gossip, no replication. »*
  | Promesse du billet | Ce que l'architecture documentée permet |
  |---|---|
  | historique **portable entre réseaux** | événements signés donc **vérifiables**, mais **ni répliqués ni découvrables** hors du relais d'origine |
  | *« the events are yours »* | **droit de sortie** et propriété des données |
  | souveraineté | **souveraineté organisationnelle**, pas redondance : un relais unique reste un **point de défaillance unique** |
  | historique comme socle de confiance | événements *tamper-**evident***, pas *tamper-**resistant*** — **un opérateur de relais compromis peut supprimer** |
  → ⚠️ **Formulation correcte à retenir : la souveraineté vendue ici est un droit de sortie, pas une garantie de disponibilité.** Et le point qui compte le plus : **le socle du modèle de confiance *ex post* est exactement aussi souverain que l'opérateur de votre relais** — si vous déléguez l'hébergement, vous déléguez la mémoire dont dépend la réputation. **C'est la question à poser en premier dans toute évaluation d'adoption.** À croiser avec la doctrine de garde-fou de [[girard-shieldstral-mistral-doctrine-garde-fou-2026-08-07]] et les critères de cloud de confiance de [[sfeir-airbus-scaleway-cloud-confiance-souverainete-2026-07-16]].

- **⭐ L'inventaire réel de ce qui existe contredit en partie la promesse d'ouverture — et le billet fournit lui-même les deux listes.** Le premier paragraphe énumère **six** fragments à réunir ; la section *« What's next? »* énumère ce qui existe. La comparaison est faisable ligne à ligne.
  | Fragment nommé en ouverture | Présent dans l'inventaire du 18 août ? |
  |---|---|
  | *« A bug report lands in one tool »* | ✅ issues |
  | *« The discussion happens in another »* | ✅ canaux liés au projet |
  | *« The fix lives on a branch somewhere else »* | ✅ *hosted git*, multi-dépôts |
  | *« Review happens in a comment thread attached to a diff »* | ✅ PR avec revues et fusions, commentaires en ligne |
  | *« **CI runs in another system** »* | ⚠️ **absent** — la CI est citée deux fois dans les promesses, **jamais dans l'inventaire** |
  | *« **Release notes get written later** »* | ⚠️ **absent** |
  → ⭐ **C'est-à-dire : le billet ouvre sur une fragmentation en six points et en résout quatre.** Les deux manquants ne sont pas mineurs — **la CI est précisément l'endroit où un agent produit ou casse une preuve**, et c'est le maillon qui manque pour que la « conversation complète » couvre la vérification. ⚠️ **Ne pas reprendre « repos, branches, pull requests, issues, CI, or all the related conversations » comme une liste de fonctionnalités livrées** : c'est une liste d'intentions, et la phrase qui la porte est celle qui n'a pas de sujet grammatical. Rapprocher de l'usine logicielle de [[lassiege-usine-logicielle-heure-ia-2026-07-28]], dont la CI est le pivot.

- **⭐ La revendication d'interopérabilité Git est la plus vérifiable du billet — et la plus facile à tester.** Verbatim : *« These are **standard git repositories**, like you already know them… You can **fetch, clone, pull, and push over plain Smart HTTP, with no custom tooling or wrapper CLI required**. Your Nostr key is your identity throughout the process… **The same npub that signs your messages signs your pushes.** You do not need another account, another identity, a separate token, or a GitHub account connected in the background. »*
  → ⭐ **Ce que ça vaut, et pourquoi c'est la phrase la plus importante pour un décideur** : (1) **le coût de sortie est faible par construction** — un `git clone` suffit à récupérer le code, ce qui rend le pari beaucoup moins engageant qu'il n'en a l'air ; (2) **l'identité unique supprime la gestion de jetons**, qui est le point de fuite habituel des agents — c'est la réponse concrète au problème de 2025 posé par Longwell (*« We have been letting bots play dress-up as us »*) ; (3) c'est un **contrat de portabilité** au sens de [[janakiram-agent-platform-portability-contract-2026-07-20]] : ce qui est standard reste récupérable, ce qui est propriétaire (issues, PR, réputation, événements de canal) ne l'est pas. ⚠️ **La nuance à ne pas perdre** : **seul le code est standard.** La conversation, la revue, la liaison PR↔canal et l'historique de contribution — c'est-à-dire **tout ce que ce billet présente comme la valeur ajoutée** — vivent dans des *event kinds* Nostr propriétaires à Buzz. **Le verrou n'est pas dans le dépôt, il est dans le contexte.** ⭐ **Test à faire avant toute adoption** : `git clone` puis `push` depuis un client Git nu contre un relais Buzz, sans le CLI `buzz`. C'est la seule affirmation du billet qu'on peut réfuter en dix minutes.

- **⭐ « Context is (almost) all you need » : une hypothèse forte présentée comme une évidence, et le corpus a de quoi la nuancer.** Verbatim : *« **The more context we can make available, the better equipped the agents are, the more intelligent the whole network becomes.** »* → ⚠️ **La monotonie est postulée, jamais argumentée.** Le billet ne discute ni le coût du contexte, ni sa dégradation, ni sa sélection — trois questions qui sont précisément le cœur de l'ingénierie de contexte. Et il ne dit jamais ce que recouvre son propre *« (almost) »*. **Trois contrepoints du corpus, à poser en regard** : la compétence n°1 de [[ng-ai-engineering-skills-map-2026-08-14]] (l'enjeu est de **mesurer et gouverner**, pas d'accumuler) ; l'invariant de journalisation de [[deepseek-harness-everything-is-a-plugin-2026-08-13]] (*« model-visible means logged »* — **c'est la visibilité qui doit être assertée, pas la quantité**) ; et le budget de tokens de [[patel-block-buzz-teams-tokens-benchmarks-2026-08-06]], qui a chiffré ce que coûte le contexte non maîtrisé chez Block même. ⭐ **La formulation défendable, et probablement celle que Petersen a en tête** : ce n'est pas *plus* de contexte qui rend le réseau intelligent, c'est **le contexte pertinent au moment de la décision** — et un index de recherche partagé est un moyen de sélection, pas d'accumulation. **Reprendre la thèse sous cette forme, pas sous la sienne.**

- **⭐ La distinction conceptuelle à retenir et à réutiliser : une surface d'exécution n'est pas une présence dans le réseau.** Verbatim : *« This is an important distinction from giving an agent access to a development machine. **A terminal gives an agent somewhere to execute commands and change files, but it does not give it a persistent place in the network.** Buzz does. »*
  | Ce qu'un terminal donne à un agent | Ce qu'une présence réseau lui donne en plus |
  |---|---|
  | exécuter, écrire des fichiers | une **identité stable** que d'autres peuvent adresser |
  | un état local, jetable | un **historique attaché** qui survit à la session |
  | agir | **être tenu pour responsable** de ce qu'il a fait |
  → ⭐ **C'est la contribution conceptuelle la plus nette du billet et elle est transposable hors de Buzz.** Elle nomme ce qui manque à un agent enfermé dans un `--dangerously-skip-permissions` sur un poste : non pas de la capacité, mais de l'**adressabilité** et de la **redevabilité**. **Bon cadre pour arbitrer entre un agent-outil (qu'on invoque) et un agent-membre (qu'on adresse)** — la même frontière que [[girard-acp-deux-protocoles-un-sigle-2026-08-02]] traite au niveau des protocoles et que [[cloudflare-wallets-agentic-commerce-2026-08-04]] traite au niveau du moyen de paiement. ⚠️ **Et la question qui suit immédiatement, absente du billet** : une présence persistante dans le réseau est aussi une **surface d'attaque persistante**. Voir [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]].

- **⭐ Le seul élément quasi empirique du texte est une anecdote sans exemple, et elle mérite d'être poursuivie.** Verbatim : *« **We've already seen a number of examples where agents understood context humans didn't and helped course correct otherwise unproductive directions.** »* → ⚠️ **Aucun exemple n'est donné. Ni combien, ni lesquels, ni comment on a su que la correction était bonne.** C'est pourtant **la seule affirmation d'effet de tout le billet**, et la plus intéressante : un agent qui infirme la direction prise par des humains à partir du contexte du canal. ⭐ **Formulation correcte pour une reprise** : *« Block rapporte, sans les documenter, des cas où des agents ont réorienté des directions improductives à partir du contexte de canal. »* **Ne pas en faire un résultat.** **Fiche à rouvrir si Block publie ces cas** — ce serait le premier retour d'expérience mesuré sur l'agent-relecteur-de-direction, et il n'existe rien d'équivalent dans le corpus.

- **⚠️ Hygiène de citation pour cette fiche — cinq règles.**
  1. **Ne jamais citer ce billet comme preuve de fonctionnement ou d'adoption.** Zéro chiffre, zéro mesure, zéro lien, zéro spécification. **Ce qui est citable : l'intention architecturale de Block.**
  2. **Toujours porter la maturité annoncée.** Projects est sous **l'onglet Experiments** de Buzz Desktop, *« fairly elementary »*, *« still under experiments »*, Buzz lui-même *« still in beta »*. **La source est explicite là-dessus ; l'omettre serait moins honnête qu'elle.**
  3. **Distinguer les trois listes de fonctionnalités du billet** : celles qui sont montrées en capture, celles qui sont inventoriées dans *« What's next? »*, et celles qui ne sont que nommées dans les phrases de promesse (**CI**, notes de version). **Seule la deuxième est un inventaire.**
  4. **Ne pas attribuer à ce billet les faits d'architecture.** Le relais unique, l'absence de réplication, `--dangerously-skip-permissions`, l'absence de chiffrement de bout en bout sur le relais hébergé, la granularité de permission par canal : tout cela vient de [[buzz-block-panorama-deep-research-2026-08-12]] et de l'`ARCHITECTURE.md` de Block, **pas de ce texte**, qui n'en dit rien.
  5. **Les *« agent trust protocols »* sont une piste déclarée, pas un mécanisme.** Aucun schéma, aucun critère, aucun calendrier, aucun tiers évaluateur. **Formulation correcte** : *« Block déclare explorer des protocoles de confiance des agents fondés sur le comportement passé. »*

- **Ce que ce billet change, et ne change pas, pour la lecture du dossier Buzz.** ⭐ **Il change ceci** : Buzz cesse d'être un espace de conversation avec du Git à côté et devient **une forge dont la conversation est un artefact de premier rang** — la promesse de juillet (*« A conventional forge preserves the diff and a green check. Buzz also preserves why the obvious fix was wrong »*) reçoit ici son implémentation produit. ⚠️ **Il ne change pas ceci** : aucune des limites documentées le 12 août n'est adressée, et **aucune n'est mentionnée**. **Le dossier Buzz reste, au 18 août 2026, un dossier de conception remarquable et de preuves absentes** — trois billets d'éditeur, un rapport interne, et toujours aucune mesure d'usage produite par un tiers. **C'est le manque le plus structurant de tout le dossier, et il se creuse à chaque publication.**

## RésuméDe400mots

Billet d'annonce de **Block Engineering** signé **Thomas Petersen** (*Principal Designer & Builder*), publié le **18 août 2026**, présentant **Buzz Projects** — la brique forge de **Buzz**, le workspace humains+agents de Block bâti sur **Nostr**.

**Le problème posé.** *« Software development tools are fragmented in ways the work itself is not. »* Le rapport de bug est dans un outil, la discussion dans un autre, le correctif sur une branche, la CI ailleurs, la revue dans un fil de commentaires, les notes de version reconstituées après coup. **La thèse : tout cela est une seule conversation, et l'historique doit faire partie du projet.**

**Ce que Projects apporte.** Une **forge hébergée sur votre propre relais** : dépôts Git standards accessibles en `fetch/clone/pull/push` sur **Smart HTTP**, *« with no custom tooling or wrapper CLI required »* ; **la clé Nostr comme identité unique** — *« the same npub that signs your messages signs your pushes »*, sans jeton séparé ni compte GitHub ; des **projets multi-dépôts** pouvant inclure des dépôts qu'on ne possède pas (*« you just won't have authority over it »*) ; issues, pull requests, diffs, commentaires en ligne, revue et fusion ; un **fil d'activité** à l'échelle du serveur ; et la **liaison de tout projet à un nombre quelconque de canaux**, de sorte que *« le contexte autour d'un changement ne disparaît pas au moment où les agents se mettent à écrire du code »*. Depuis un canal, on peut confier une issue à un agent ou lui demander d'ouvrir une PR, laquelle renvoie à la conversation qui l'a produite ; l'agent sollicite l'humain via l'**Inbox**.

**La doctrine, en deux temps que le billet n'assemble pas.** D'un côté, **aucune contrainte préalable** : *« No forced guardrails, no limitations on what your agents are allowed to help you with. »* De l'autre, **un enregistrement signé de tout acte** : *« Every push, review, approval, and merge is a signed Nostr event »*, avec la trace de **quel agent** a produit un patch et **quel humain** l'y avait autorisé. D'où la projection finale : l'historique de contribution devient *« more than a set of colored squares on a profile »*, un **historique vérifiable attaché à une clé**, et Block déclare **explorer des *« agent trust protocols informed by past behavior »***. **La confiance bascule de l'autorisation *ex ante* à la preuve *ex post*.** Le cadre associé est net : *« A terminal gives an agent somewhere to execute commands and change files, but it does not give it a persistent place in the network. Buzz does. »*

**Réserves.** ⚠️ **Aucun chiffre, aucun lien sortant, aucune spécification** dans tout le texte ; **CI et notes de version sont promises mais absentes de l'inventaire** ; Projects vit sous **l'onglet Experiments** et le billet se disqualifie six fois — *« Buzz is still in beta and Buzz Projects is still under experiments, so treat it accordingly. »*

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
