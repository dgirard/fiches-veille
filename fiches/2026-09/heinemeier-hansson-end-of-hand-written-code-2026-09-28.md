---
themes: [agents-codage-ia-skills, economie-marche, philosophie-societe]
source: "Thought Economics"
---
# heinemeier-hansson-end-of-hand-written-code-2026-09-28

## Veille

Entretien long format (**25 min de lecture**) de **David Heinemeier Hansson**, créateur de **Ruby on Rails** et copropriétaire de **37signals**, par **Vikas Shah** dans *Thought Economics*, publié le **28 septembre 2026**, cinq jours après la keynote d'ouverture de **Rails World** à Austin où il a annoncé que 37signals passait *« pencils down »* sur le code écrit à la main. **(A)** Le renversement, daté : à l'été 2025 il déclarait à **Lex Fridman** ne pas laisser l'IA écrire son code ; ce qui l'a fait changer d'avis est l'arrivée fin 2025 des agents de codage, et *« le changement est vraiment devenu vertical, à mon avis, ces trois ou quatre derniers mois »*. **(B)** L'argument de fond n'est pas technique mais politique : les programmeurs étaient devenus *« une classe cléricale »* médiatrice de l'accès à la machine, et l'agent joue le rôle de Luther — *« Agent Luther »* — en supprimant l'intermédiaire. Il en tire une conséquence sur lui-même : ses compétences de codeur ne sont plus *« économiquement viables comme levier indépendant »*. **(C)** Le tri des modèles d'affaires : le client-side est *« déjà parti »* (Adobe), le client-serveur tient encore parce que *« les gens n'ont aucune envie de faire tourner leurs propres serveurs »*, les moats de plomberie tiennent (Shopify, *« systèmes de paiement, d'expédition, de taxes »*), et **Salesforce** et **SAP** sont *« en sérieuse difficulté »* puisqu'*« il n'y a plus de valeur dans le code, seulement dans les intuitions de process »*. **(D)** **Omarchy**, sa distribution Linux à agents intégrés : version **Quattro** écrite exclusivement par agents, **200 000 téléchargements en 18 jours**, **4 000 plugins** en quatre semaines, **21,7 M$** de promesses de dons. **(E)** La clôture prospective : AGI atteint, *« poches d'ASI »*, robots, et *« que faites-vous quand vous n'avez plus rien à faire ? »*. À lire contre [[lecun-still-far-from-human-level-ai-llm-2026-09-25]] sur le même mois.

## Titre Article

The End of Hand-Written Code: A Conversation with David Heinemeier Hansson (DHH) on AI, Omarchy and the Future of Programming

## Date

2026-09-28

## URL

https://thoughteconomics.com/david-heinemeier-hansson/

## Keywords

fin du code écrit à la main, pencils down, agents de codage, codage agentique, prêtrise des programmeurs, classe cléricale, désintermédiation, Agent Luther, Omarchy, Quattro, Linux sur le desktop, ordinateur malléable, plugins, distribution à agents intégrés, CRUD, applications client-serveur, moat, douves logicielles, SaaS en difficulté, Salesforce, SAP, Adobe, formats de fichiers, interopérabilité, vibe coding, logiciel sur mesure, artisanat logiciel, analogie de la photographie, métier à tisser mécanique, révolution industrielle, AGI, ASI, revenu universel, abondance, problème de l'existence

## Authors

David Heinemeier Hansson, créateur de Ruby on Rails et copropriétaire de 37signals, interrogé par Vikas Shah dans *Thought Economics*.

## Ton

**Profil** : entretien écrit en six questions longues, publié par une revue d'entretiens généralistes britannique dont l'intervieweur est lui-même administrateur de sociétés. Le format est celui de l'accord : Shah abonde, apporte ses propres exemples (*« je pourrais monter ça en une demi-heure avec Fable »*) et ne contredit jamais. La rédaction intercale quatre notes de bas de texte glosant *Agent Luther*, *vibe coding*, l'AGI et la liste des modèles cités.

**Style** : oral d'ingénieur transcrit, à la première personne, fondé sur des analogies historiques longues plutôt que sur des démonstrations — le portraitiste et le Kodak Brownie, Luther et le clergé, le métier à tisser, les chevaux de trait, l'agriculture de subsistance passée de 97 % à moins de 2 % de la population active. Superlatifs répétés (*« vastly, shockingly better »*, *« vastly, vastly, vastly dwarfs »*). L'argumentation procède par renversement de charge de la preuve : *« si vous ne le croyez pas, c'est que vous n'avez pas passé assez de temps avec ces systèmes, ou que vos informations sont périmées »*.

**Position épistémique** : conversion revendiquée et datée, assortie d'une clause de révision — *« ce que je dis maintenant, je ne l'aurais pas dit en février »*, et *« je ne veux pas faire de prédictions, parce que celles que j'ai faites l'an dernier ont l'air désastreuses »*. Les affirmations sur la capacité des modèles sont des jugements d'usage personnel, sans benchmark ni mesure. Les chiffres cités (200 000 téléchargements, 4 000 plugins, 21,7 M$, 15 000 Md$ d'économie dépendant du noyau Linux) viennent de son propre projet ou d'une estimation non sourcée. Deux positions de l'auteur sont adjacentes à ses intérêts et énoncées comme telles : il siège au conseil de **Shopify**, dont il décrit le moat comme tenable, et promeut Omarchy, dont il décrit la catégorie comme gagnante.

## Pense-betes

- **L'annonce opérationnelle, à retenir avant les analogies** : 37signals est passé *« pencils down »* sur le code écrit à la main. Ce n'est pas une prévision mais une décision d'entreprise, prise par l'auteur d'un framework sur lequel reposent, selon son décompte, plus d'un demi-billion de dollars de capitalisation (**Shopify**, **GitHub**, **Airbnb**, **Coinbase**).
- **La chronologie de la conversion**, utile pour dater la bascule d'un praticien de référence : été 2025, il dit à Lex Fridman que les programmeurs *« apprennent avec leurs doigts »* et refuse l'IA dans son code ; fin 2025, arrivée des agents capables d'écrire, tester et réparer seuls ; quatre mois avant l'entretien, il démarre Quattro sans écrire *« virtuellement une seule ligne »* ; août 2026, retour chez Fridman avec un OS qu'il n'a pas codé. Le mouvement se mesure en mois, pas en années.
- **La thèse du 97 % CRUD.** L'argument de capacité ne porte pas sur les cas limites : *« la plupart des programmeurs travaillent sur des systèmes assez rudimentaires appelés CRUD — create, read, update, delete. C'est en gros 97 % des applications du monde. »* Les domaines où l'humain bat encore l'agent existent mais sont *« très petits »* et *« ce n'est pas ce que font la plupart des programmeurs »*. C'est le même déplacement de la question que dans [[felker-evaporation-software-engineering-agentic-builder-2026-09-14]].
- **La grille de survie des éditeurs, en quatre cases** — la partie la plus directement réutilisable. (1) **Client-side pur** (Photoshop, Lightroom, Illustrator, Premiere) : *« je détesterais être dans les chaussures d'Adobe »*, alternatives open source vibe-codées à venir en masse, *« on vit sur du temps emprunté »*. (2) **Client-serveur** : tient encore, non pour des raisons techniques mais parce que personne ne veut administrer de serveurs — réserve explicite, *« ça changera peut-être quand ils feront assez confiance à leurs agents »*. (3) **Plomberie intégrée** (Shopify : paiements, expédition, taxes) : complexité absorbée et revendue si bon marché qu'*« il semble à peine valoir les tokens »* de la répliquer. (4) **Abonnements chers à faible process** (Salesforce, SAP) : *« en sérieuse difficulté »*, *« il n'y a plus de valeur dans le code, seulement dans les intuitions de process — et je ne suis pas sûr que leurs intuitions de process soient si bonnes »*. Prolonge la décomposition de la SaaSpocalypse dans [[corrot-mirakl-pirates-de-lia-2026-09-20]], qui aboutit au même tri par la nature de l'actif.
- **Le second barrage, non technique** : même répliquable, un logiciel demande *« votre goût, votre diligence, votre perspicacité et votre attention »* pour être maintenu et avancé. C'est la réserve que DHH oppose lui-même à l'idée que tout logiciel deviendra sur mesure — à confronter à [[lee-robinson-personal-software-2025-01-01]].
- **La mort des formats comme barrière.** LibreOffice a demandé des années ; *« si vous vouliez créer un éditeur de texte compatible Word sur Omarchy, vous pourriez avoir fini cet après-midi »*. Conséquence énoncée : la valeur des formats de fichiers et des protocoles s'effondre, *« parce que les agents parlent toutes les langues »* — au sens propre aussi, le site d'Omarchy a été traduit en 50 langues par agent, domaines achetés compris.
- **Pourquoi Linux et pas Windows/macOS**, argument d'ingénierie à garder : les 40 millions de lignes du noyau sont dans le pré-entraînement de tous les modèles de frontière, qui connaissent donc le système de l'intérieur ; sur les OS fermés, l'agent ne peut travailler qu'aux marges. L'avantage n'est plus idéologique mais informationnel.
- **Le mécanisme d'Omarchy à copier ailleurs** : au premier démarrage, choix de l'agent par défaut (Claude, Codex, Grok) ; à chaque crash, une notification *« voulez-vous que l'IA regarde ? »* ; l'agent diagnostique, distingue bug local / bug applicatif / bug de la distribution, propose le correctif et ouvre une pull request en amont — *« la boucle est fermée »*. Résultats affichés en quatre semaines : **4 000 plugins**, faits en majorité par des non-programmeurs.
- **L'argument d'échelle qu'il oppose aux grands éditeurs** : quelques centaines de milliers d'utilisateurs Omarchy équipés d'agents représentent *« quelques dizaines de millions de programmeurs »* face aux *« quelques dizaines de milliers »* d'Apple et Google. Formulation à manier avec prudence — elle convertit des utilisateurs en équivalents-ingénieurs sans passer par la question de la coordination.
- **Ce qui reste de l'artisanat, selon lui** : un avantage de pilotage (mieux prompter, mieux orienter) qui *« rétrécit constamment »* — *« moindre que la semaine dernière, et bien moindre qu'il y a trois mois »* ; et l'analogie agricole, 97 % de paysans devenus moins de 2 %, avec ce corollaire qu'il assume : *« il est très important que ces deux derniers pour cent sachent ce qui se passe »*, et même de plus en plus à mesure qu'on dépend de la machine. La conclusion sociale est un aveu plutôt qu'un programme : *« que faites-vous quand vous n'avez plus rien à faire ? »*, avec un scepticisme sur le revenu universel (*« les études ne sont pas très flatteuses »*).
- **Ce que l'entretien ne fournit pas**, à noter avant de citer : aucune mesure, aucun protocole, aucun cas d'échec agentique, et une seule voix. Les affirmations fortes — modèles supérieurs à *« virtuellement tout programmeur sur Terre »*, AGI atteint, *« poches d'ASI »*, meilleurs juristes que programmeurs — sont des impressions d'usage d'un praticien très exposé, non des résultats.

## RésuméDe400mots

Vikas Shah interroge David Heinemeier Hansson, créateur de Ruby on Rails et copropriétaire de 37signals avec Jason Fried, cinq jours après une keynote de Rails World où il a annoncé que son entreprise cessait d'écrire du code à la main. L'entretien, publié le 28 septembre 2026, ouvre sur la question du rendre-capable ou du rendre-dépendant. Sa réponse est franche : l'IA rend les gens « massivement plus capables », et l'inquiétude sur l'externalisation de la pensée est vieille de 2 500 ans, du papyrus au rock'n'roll, toujours démentie.

Vient l'argument central, qui est de pouvoir plutôt que de technique. Les programmeurs, dit-il, ont formé une classe cléricale médiatisant l'accès à l'ordinateur ; les agents jouent le rôle de Luther et suppriment l'intermédiaire, ce qui explique selon lui le scepticisme d'une partie de la communauté open source, dont la prémisse était pourtant le contrôle de son propre logiciel. L'analogie qu'il a développée sur scène est celle du portrait peint : trois mois de maître-peintre réservés aux aristocrates, puis deux mille milliards d'images prises chaque année. Le monde y a gagné ; les portraitistes photoréalistes, non.

Sur la capacité des modèles, il est catégorique : les modèles de frontière, surtout combinés entre eux, dépassent presque tous les programmeurs sur un large spectre. La plupart des applications sont du CRUD, soit 97 % du parc. Il date la bascule des trois ou quatre derniers mois et reconnaît que ses propres compétences ne valent plus comme levier économique.

Il trie ensuite les modèles d'affaires. Le logiciel purement client est condamné — il ne voudrait pas être Adobe. Le client-serveur résiste parce que personne ne veut administrer de serveurs. Les plateformes à plomberie profonde, comme Shopify dont il est administrateur, gardent un moat. Salesforce et SAP, eux, sont « en sérieuse difficulté » : il n'y a plus de valeur dans le code, seulement dans les intuitions de process.

Omarchy occupe la seconde moitié. Distribution Linux dont la version Quattro a été écrite exclusivement par agents, elle intègre un agent au cœur du système : choix de l'agent au premier démarrage, diagnostic automatique des crashes, correctif et pull request en amont. En quatre semaines, plus de 4 000 plugins créés en majorité par des non-programmeurs. L'avantage de Linux est que ses 40 millions de lignes sont dans le pré-entraînement des modèles.

Il termine sur l'artisanat — un avantage de pilotage qui rétrécit, et une minorité qui devra comprendre la machine — puis sur les robots, l'abondance et « le problème de l'existence ».

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Vikas Shah | PERSONNE | publie | entretien The End of Hand-Written Code | DOCUMENT | 0.96 | STATIQUE | déclaré_article |
| David Heinemeier Hansson | PERSONNE | a_créé | Ruby on Rails | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| David Heinemeier Hansson | PERSONNE | a_créé | Omarchy | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| David Heinemeier Hansson | PERSONNE | dirige | 37signals | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| 37signals | ORGANISATION | affirme_que | l'entreprise passe « pencils down » sur le code écrit à la main | AFFIRMATION | 0.95 | STATIQUE | déclaré_article |
| David Heinemeier Hansson | PERSONNE | affirme_que | les programmeurs formaient une classe cléricale médiatisant l'accès à la machine, que les agents désintermédient comme Luther a désintermédié le clergé | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| agents de codage | TECHNOLOGIE | surpasse | virtuellement tout programmeur sur Terre sur un large spectre de compétences | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| David Heinemeier Hansson | PERSONNE | affirme_que | les systèmes CRUD représentent environ 97 % des applications du monde | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| David Heinemeier Hansson | PERSONNE | affirme_que | "Mes compétences de programmation ne sont plus économiquement viables comme levier indépendant pour créer des choses" | CITATION | 0.95 | DYNAMIQUE | déclaré_article |
| David Heinemeier Hansson | PERSONNE | prédit | Salesforce et SAP sont en sérieuse difficulté, la valeur ayant quitté le code pour les seules intuitions de process | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| David Heinemeier Hansson | PERSONNE | prédit | les applications purement client-side comme celles d'Adobe vivent sur du temps emprunté face aux alternatives open source vibe-codées | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Shopify | ORGANISATION | utilise | moat de plomberie sur les systèmes de paiement, d'expédition et de taxes | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| applications client-serveur | CONCEPT | résout | la réticence des utilisateurs à administrer eux-mêmes serveurs, bases et sauvegardes | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Omarchy | TECHNOLOGIE | est_instance_de | distribution à agents intégrés au cœur du système | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Omarchy Quattro | TECHNOLOGIE | est_variante_de | Omarchy | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Omarchy Quattro | TECHNOLOGIE | mesure | plus de 200 000 téléchargements en 18 jours et 21,7 M$ de promesses de dons à la fondation fin septembre 2026 | MESURE | 0.93 | STATIQUE | déclaré_article |
| Omarchy Quattro | TECHNOLOGIE | mesure | plus de 4 000 plugins créés en quatre semaines, en majorité par des non-programmeurs | MESURE | 0.92 | STATIQUE | déclaré_article |
| Omarchy | TECHNOLOGIE | permet | diagnostic automatique d'un crash par l'agent, correctif et ouverture d'une pull request en amont | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Omarchy | TECHNOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Linux | TECHNOLOGIE | permet | un avantage agentique décisif, ses 40 millions de lignes étant dans le pré-entraînement de tous les modèles de frontière | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| agents de codage | TECHNOLOGIE | réduit | la valeur des formats de fichiers et des protocoles comme barrière à l'entrée | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| David Heinemeier Hansson | PERSONNE | affirme_que | "Les moats historiques qui protégeaient Adobe, Microsoft et les autres éditeurs de ce type de logiciel ont complètement disparu" | CITATION | 0.94 | DYNAMIQUE | déclaré_article |
| David Heinemeier Hansson | PERSONNE | affirme_que | les modèles sont encore meilleurs juristes que programmeurs, la rédaction et l'analyse de contrats étant stupéfiantes | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| David Heinemeier Hansson | PERSONNE | affirme_que | l'AGI est atteinte et des poches d'ASI existent déjà dans des tranches du développement logiciel | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Ordinateur malléable | CONCEPT | permet | à l'utilisateur final de réécrire son système d'exploitation au même niveau que son concepteur | AFFIRMATION | 0.91 | ATEMPOREL | déclaré_article |
| Artisanat de la programmation | CONCEPT | s_applique_à | une minorité restante, sur le modèle des 97 % de paysans devenus moins de 2 % après la révolution industrielle | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| David Heinemeier Hansson | PERSONNE | affirme_que | l'avantage de comprendre la machine pour mieux prompter et orienter rétrécit constamment | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| David Heinemeier Hansson | PERSONNE | s_oppose_à | thèse d'une externalisation dommageable de la pensée, démentie selon lui depuis le papyrus | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| David Heinemeier Hansson | PERSONNE | affirme_que | "Que faites-vous quand vous n'avez plus rien à faire ?" | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| David Heinemeier Hansson | PERSONNE | s_oppose_à | le revenu universel, dont les études menées jusqu'ici ne sont pas flatteuses | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| Lex Fridman | PERSONNE | référence | David Heinemeier Hansson | PERSONNE | 0.92 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| David Heinemeier Hansson | PERSONNE | rôle | Créateur de Ruby on Rails (2003), copropriétaire de 37signals, administrateur de Shopify depuis novembre 2024, créateur d'Omarchy ; annonce la fin du code écrit à la main chez lui après trente ans de pratique | MISE_A_JOUR |
| Vikas Shah | PERSONNE | rôle | Fondateur de *Thought Economics*, administrateur de sociétés et entrepreneur britannique ; mène l'entretien en six questions, sur un registre d'accord | AJOUT |
| entretien The End of Hand-Written Code | DOCUMENT | forme | Entretien écrit de 25 min de lecture publié par *Thought Economics* le 28 septembre 2026, avec notes éditoriales glosant Agent Luther, le vibe coding et l'AGI | AJOUT |
| Omarchy | TECHNOLOGIE | catégorie | Distribution Linux gratuite conçue pour être pilotée par des agents, agent choisi au premier démarrage, diagnostic de crash et pull request automatisés ; site traduit en 50 langues par agent | AJOUT |
| Omarchy Quattro | TECHNOLOGIE | fabrication | Quatrième version, écrite exclusivement par agents en trois mois sans ligne de code manuelle ; 200 000 téléchargements en 18 jours, 4 000 plugins en quatre semaines, 21,7 M$ de promesses de dons | AJOUT |
| 37signals | ORGANISATION | position | Éditeur de Basecamp ; passé « pencils down » sur le code écrit à la main, annoncé à Rails World le 23 septembre 2026 | AJOUT |
| Ruby on Rails | TECHNOLOGIE | portée | Framework web créé en 2003 ; les entreprises parties de Rails (Shopify, GitHub, Airbnb, Coinbase) pèsent selon l'auteur plus d'un demi-billion de dollars | AJOUT |
| Ordinateur malléable | CONCEPT | définition | Machine dont l'utilisateur final peut modifier ou réécrire le système lui-même via un agent, au même niveau que son concepteur — impossible sur OS fermés, tenable sur Linux | AJOUT |
| Artisanat de la programmation | CONCEPT | état | Subsiste comme pratique et comme joie, mais perd sa centralité économique ; reste nécessaire une minorité qui comprend la machine, à la manière des moins de 2 % d'agriculteurs | AJOUT |
| Salesforce | ORGANISATION | exposition | Donnée « en sérieuse difficulté » avec SAP : plus de valeur dans le code, seulement dans des intuitions de process jugées incertaines | AJOUT |
| Shopify | ORGANISATION | exposition | Moat jugé tenable grâce à la complexité absorbée des systèmes de paiement, d'expédition et de taxes ; l'auteur siège à son conseil | AJOUT |
| Linux | TECHNOLOGIE | avantage agentique | 40 millions de lignes intégralement présentes dans le pré-entraînement des modèles de frontière ; noyau le plus revu de l'histoire, estimation de 15 000 Md$ d'économie en dépendant | AJOUT |
| Lex Fridman | PERSONNE | rôle | Podcasteur auprès de qui DHH a exprimé en été 2025 son refus de l'IA dans son code, puis en août 2026 la publication d'un OS qu'il n'a pas écrit | AJOUT |
