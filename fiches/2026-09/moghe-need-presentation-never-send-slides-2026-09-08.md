---
themes: [transformation-adoption, outils-plateformes]
source: "martinfowler.com (Sumeet Gayathri Moghe)"
---
# moghe-need-presentation-never-send-slides-2026-09-08

## Veille

Premier article de la série **Never Send The Slides** sur martinfowler.com, publié le **8 septembre 2026** (~2 400 mots, cinq sections et deux encadrés), signé **Sumeet Gayathri Moghe**, global head of culture and organisational design chez **Thoughtworks** ; **Martin Fowler** en a assuré la relecture éditoriale. Le texte pose d'abord une définition — *« a presentation is an act of storytelling in which a presenter orchestrates narrative, timing, and emotion to create meaning that neither visuals nor documents can achieve on their own »* — et son corollaire : *« the slides are not the presentation »*. Il en tire une hiérarchie de cinq artefacts, condensée en fin de texte dans un tableau *cheat sheet*. **(1)** Le **document linéaire**, suffisant dans la plupart des situations d'entreprise, où il ne s'agit que de transmettre de l'information. **(2)** L'**infodeck** — le terme est de Fowler — quand le contenu a une longue durée de vie et mérite un soin visuel. **(3)** Les **applications web interactives**, pour piloter la charge cognitive du lecteur. **(4)** L'**audio ou la vidéo enregistrée**, quand la voix compte mais pas l'interaction. **(5)** La **présentation live**, réservée aux cas où la présence synchrone sert à influencer et à traiter les objections en temps réel. Deux observations datent le texte de 2026 : les **harnais de codage** mettent la fabrication d'applications interactives à portée de non-développeurs, et un document linéaire *« reduces the probability of hallucinations »* quand un lecteur le fait résumer par un LLM. Même support que [[boeckeler-harness-engineering-coding-agents-2026-04-02]].

## Titre Article

Do you even need a presentation?

## Date

2026-09-08

## URL

https://martinfowler.com/articles/never-send-slides/need-presentation.html

## Keywords

présentation, slides, slideware, storytelling, document linéaire, écriture structurée, artefact autoportant, infodeck, slidedoc, Duarte, slideument, design de l'information, applications web interactives, charge cognitive, microcourse, harnais de codage, non-développeurs, durée de vie d'un artefact, vidéo enregistrée, builds et transitions, chapitrage, présentation live, présence synchrone, coût de coordination, communication asynchrone, async-first, Thoughtworks, Martin Fowler, Grammarly, Keynote, hallucination LLM

## Authors

Sumeet Gayathri Moghe (global head of culture and organisational design, Thoughtworks), publié sur martinfowler.com ; relecture éditoriale de Martin Fowler.

## Ton

**Profil** : article de conseil professionnel, premier volet d'une série pédagogique. Public : cadres et *knowledge workers* d'entreprise qui produisent des supports de communication interne. Anglais soigné, phrases courtes, aucun jargon technique — le seul terme d'art, *infodeck*, est défini et attribué.

**Style** : la structure **est** l'argument — le texte descend une échelle du plus léger au plus coûteux (document → infodeck → app web → enregistrement → live), et chaque palier s'ouvre par la condition qui le déclenche plutôt que par sa description. La démonstration passe par des artefacts montrés, pas décrits : la bibliothèque de diagrammes de son livre, un carnet de voyage mis en page par son fils, un nuage de mots filtrable, un microcours embarqué, ses propres vidéos. L'auteur chiffre ses exemples (**129 builds** en 8 minutes, **141** en 24) puis désamorce aussitôt la métrique — *« there's no formula for the right number of builds »*. Les contreparties sont posées à chaque étage : les apps web perdent le commentaire inline des wikis, les infodecks coûtent cher en compétence de design, dont la rareté explique que la plupart soient ratés.

**Position épistémique** : prescriptive et explicitement située — l'auteur écrit depuis l'*async-first* dont il a publié le manuel, et rappelle qu'il n'est pas ingénieur logiciel, ce qui borne son estimation de la durée de vie des applications qu'il fabrique. La section acknowledgments liste sept relecteurs, et déclare l'usage de Grammarly pour la relecture et de Claude pour vérifier la prise en compte des retours.

## Pense-betes

- **La définition, et son corollaire.** Une présentation est *« un acte de narration où un présentateur orchestre le récit, le rythme et l'émotion »* pour créer un sens que ni les visuels ni les documents n'atteignent seuls. Donc : les slides ne sont pas la présentation, et la présentation est un outil d'influence qu'on garde pour les moments où elle porte.
- **La règle par défaut** : dans la plupart des scénarios d'entreprise, on ne fait que transmettre de l'information — un document suffit. Le slideware utilisé comme format documentaire force à consommer l'information *« in fragmented, disconnected bursts »*, alors qu'une structure linéaire laisse le lecteur construire sa compréhension.
- **Ce que le linéaire force et que les slides autorisent.** Les decks laissent des choses non dites entre les slides ; en asynchrone, cela produit des malentendus et du contexte perdu. L'écriture linéaire oblige à faire le pont entre les sections — et ce caractère explicite **réduit la probabilité d'hallucination** si le lecteur passe le document à un LLM.
- **Les outils d'écriture comme un IDE** : Word, Hemingway ou Grammarly permettent de *codifier* un style et un niveau de lisibilité visé, comme un plugin d'IDE assiste un développeur.
- **L'encadré « slideware as a companion tool »** : faire les diagrammes dans Keynote puis les importer dans le document. Le slideware reste l'interface familière du dessin ; il n'a pas à devenir le format de livraison.
- **Infodeck** (terme de Martin Fowler) : mise en page dans une interface de slides pour du *light reading*, texte et visuels juxtaposés. Ce n'est **ni un slideument ni un support de présentation**. Duarte Design l'appelle *slidedoc* et en publie un catalogue de patterns.
- **Les trois conditions d'un infodeck réussi** : l'écriture d'abord (produite dans un outil d'écriture, pas dans le deck) ; la brièveté qui ne sacrifie pas la compréhension (*« I'd have written a shorter letter, but I didn't have the time »*) ; et surtout le design — la rareté du sens du design chez les *knowledge workers* est la raison pour laquelle la plupart des infodecks échouent, et le poste de coût principal est l'information designer.
- **Applications web interactives** : depuis un an, les harnais de codage mettent HTML/CSS/JS à portée de non-développeurs. L'interactivité sert à *déplacer la charge cognitive de l'audience vers l'artefact* — filtrer un nuage de mots, chunker un long article en microcours avec questions de réflexion.
- **Leur contrepartie, souvent oubliée** : wikis et documents collaboratifs ont le commentaire inline natif ; le rajouter à chaque app est un surcoût. Une app interactive mais *sans état* ne vaut guère mieux qu'un transfert d'information à sens unique. S'y ajoute la question de l'hébergement et de la durée de vie.
- **L'enregistrement avant le live.** Un monologue bien écrit, sans aucun visuel, suffit souvent (l'exemple donné est Ed Zitron). Enregistrer force à couper le gras ; l'audience choisit son moment, accélère, ralentit, réécoute ; sous-titres et chapitrage font le reste. Conclusion assumée : *« most presentations are better off as recordings »*.
- **Le rythme d'une vidéo n'est pas celui d'une salle** : à 30 images par seconde, personne n'attend des slides statiques — il faut enchaîner builds et transitions beaucoup plus vite qu'en présentiel. Ses repères : 129 builds sur 8 minutes en voix off (qu'il juge encore lent), 141 sur 24 minutes quand il est à l'image. Aucune formule, seulement le tempo que le récit demande.
- **Quand passer en live** : uniquement quand la présence synchrone est le but — influencer, traiter les objections en temps réel, pitcher un client, célébrer, fédérer. À réserver aux situations qui **méritent le coût de coordination**, et à préparer d'autant plus que le public ne peut ni vous accélérer ni vous ralentir.

## RésuméDe400mots

Sumeet Gayathri Moghe, global head of culture and organisational design chez Thoughtworks, ouvre sur martinfowler.com une série intitulée « Never Send The Slides » par un article qui pose la question préalable : avez-vous seulement besoin d'une présentation ? Il commence par séparer deux choses que l'usage confond, le fichier et l'acte. Une présentation, écrit-il, est un acte de narration où un présentateur orchestre le récit, le rythme et l'émotion pour créer un sens que ni les visuels ni les documents n'atteignent seuls. Le corollaire est net : les slides ne sont pas la présentation. Comme la présentation est un outil d'influence puissant, on en tire le maximum en la réservant aux moments qui la justifient.

Suit une échelle de cinq artefacts, résumée en fin d'article par un tableau. La règle par défaut est le document linéaire : dans la plupart des situations d'entreprise, il ne s'agit que de transmettre de l'information, et le slideware employé comme format documentaire impose une lecture fragmentée. Un document bien structuré — titres, paragraphes courts, listes, tableaux, diagrammes — laisse le lecteur bâtir sa compréhension, et son caractère explicite réduit le risque d'hallucination lorsqu'un LLM le résume. Les outils d'écriture permettent de codifier un style et une lisibilité visée, comme un plugin d'IDE assiste un développeur.

Deuxième palier, l'infodeck — le terme est de Martin Fowler : un document mis en page dans une interface de slides, pour de la lecture légère, ni slideument ni support de présentation. L'intérêt tient à l'accessibilité de l'outil pour qui ne maîtrise pas InDesign ; le coût réel est le design, dont la rareté explique que la plupart des infodecks échouent. Troisième palier, les applications web interactives : les harnais de codage apparus depuis un an les mettent à portée de non-développeurs, et l'interactivité sert à piloter la charge cognitive du lecteur. Leur revers est l'absence de commentaire inline, l'hébergement et une durée de vie incertaine.

Quatrième palier, l'enregistrement. Un monologue sans visuels suffit parfois ; l'enregistrement force la concision, laisse l'audience choisir son rythme, et gagne sous-titres et chapitrage. Moghe prévient que le tempo d'une vidéo n'est pas celui d'une salle — 129 builds en huit minutes, 141 en vingt-quatre — sans en faire une règle. Sa conclusion : la plupart des présentations gagneraient à être des enregistrements. Reste le live, à réserver aux moments où la présence synchrone sert à influencer et à traiter les objections, et qui méritent le coût de coordination qu'ils imposent à tout le monde.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Sumeet Gayathri Moghe | PERSONNE | travaille_chez | Thoughtworks | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Sumeet Gayathri Moghe | PERSONNE | publie | Never Send The Slides | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Sumeet Gayathri Moghe | PERSONNE | publie | The Async-First Playbook | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| Sumeet Gayathri Moghe | PERSONNE | affirme_que | "The slides are not the presentation" | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| Sumeet Gayathri Moghe | PERSONNE | affirme_que | "A presentation is an act of storytelling in which a presenter orchestrates narrative, timing, and emotion" | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Sumeet Gayathri Moghe | PERSONNE | affirme_que | "Most presentations are better off as recordings" | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| Sumeet Gayathri Moghe | PERSONNE | recommande | réserver la présentation live aux situations qui méritent le coût de coordination | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Martin Fowler | PERSONNE | a_créé | Infodeck | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| Document linéaire | CONCEPT | surpasse | Slideware | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| Document linéaire | CONCEPT | réduit | probabilité d'hallucination lors d'un résumé par LLM | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Slideware | TECHNOLOGIE | permet | mise en page accessible aux non-designers (calques, WYSIWYG) | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Infodeck | CONCEPT | s_applique_à | contenu à longue durée de vie méritant un soin visuel | AFFIRMATION | 0.91 | ATEMPOREL | déclaré_article |
| Slidedoc | CONCEPT | est_variante_de | Infodeck | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Duarte Design | ORGANISATION | publie | Slidedocs | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| Thoughtworks | ORGANISATION | utilise | Infodeck | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Applications web interactives | TECHNOLOGIE | réduit | Charge cognitive | CONCEPT | 0.89 | ATEMPOREL | déclaré_article |
| Harness | CONCEPT | permet | production d'applications simples par des non-développeurs | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Applications web interactives | TECHNOLOGIE | s_oppose_à | commentaire inline natif des wikis et documents collaboratifs | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| Vidéo enregistrée | TECHNOLOGIE | permet | consommation au rythme de l'audience (sous-titres, chapitrage, vitesse) | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Sumeet Gayathri Moghe | PERSONNE | mesure | 129 builds en 8 minutes de voix off, 141 en 24 minutes à l'image | MESURE | 0.9 | STATIQUE | déclaré_article |
| Présentation live | CONCEPT | s_applique_à | influence et traitement des objections en présence synchrone | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Grammarly | TECHNOLOGIE | améliore | lisibilité et style de l'écriture | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| Ed Zitron | PERSONNE | utilise | monologue vidéo sans visuels | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Martin Fowler | PERSONNE | référence | Never Send The Slides | DOCUMENT | 0.9 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Sumeet Gayathri Moghe | PERSONNE | rôle | Global head of culture and organisational design chez Thoughtworks ; ex-business analyst, product manager et consultant en transformation | AJOUT |
| Martin Fowler | PERSONNE | rôle | Éditeur du site hôte, auteur du terme « infodeck », relecture éditoriale de l'article | AJOUT |
| Ed Zitron | PERSONNE | rôle | Critique de la bulle des capex IA ; monologues vidéo sans visuels | AJOUT |
| Thoughtworks | ORGANISATION | pratique | Publie ses playbooks (cloud economics, responsible tech, data engineering) en infodecks | AJOUT |
| Duarte Design | ORGANISATION | production | Ebook « Slidedocs », catalogue de patterns de mise en page | AJOUT |
| Never Send The Slides | DOCUMENT | catégorie | Série d'articles sur martinfowler.com ; « Do you even need a presentation? » en est le premier volet | AJOUT |
| The Async-First Playbook | DOCUMENT | auteur | Livre de Sumeet Gayathri Moghe ; sa bibliothèque de diagrammes a été faite sous Keynote | AJOUT |
| Infodeck | CONCEPT | définition | Document mis en page dans une interface de slides, pour du « light reading » ; ni slideument ni support de présentation | AJOUT |
| Slidedoc | CONCEPT | origine | Nom donné par Duarte Design à l'infodeck | AJOUT |
| Document linéaire | CONCEPT | vertu | Force à faire le pont entre les sections ; artefact autoportant à faible contexte | AJOUT |
| Présentation live | CONCEPT | condition | Réservée à la présence synchrone : influence, objections en temps réel, pitch, célébration | AJOUT |
| Charge cognitive | CONCEPT | levier | Chunking, interactions exploratoires, questions de réflexion | AJOUT |
| Slideware | TECHNOLOGIE | catégorie | PowerPoint, Keynote, Canva, Google Slides — interface de mise en page ubiquitaire | AJOUT |
| Applications web interactives | TECHNOLOGIE | limite | Pas de commentaire inline natif ; hébergement et durée de vie incertains ; sans état, utilité réduite | AJOUT |
| Harness | CONCEPT | usage | Met la production de HTML/CSS/JS interactif à portée de non-développeurs | AJOUT |
| Grammarly | TECHNOLOGIE | catégorie | Outil d'aide à l'écriture ; codifie un style et un niveau de lisibilité visé | AJOUT |
