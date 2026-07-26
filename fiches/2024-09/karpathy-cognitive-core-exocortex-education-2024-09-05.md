---
themes: [recherche-education, architecture-construction, philosophie-societe]
source: "No Priors Ep. 80 (Sarah Guo & Elad Gil)"
---
# karpathy-cognitive-core-exocortex-education-2024-09-05

## Veille
Dernier segment de l'épisode 80 de *No Priors* (sept. 2024) où Andrej Karpathy, fraîchement sorti d'OpenAI pour fonder Eureka Labs, tient **un seul argument appliqué deux fois** : la capacité de calcul (machine ou humaine) ne doit pas être dépensée en mémorisation. Côté machine, c'est la thèse du ***cognitive core*** — les modèles « gaspillent une tonne de capacité à retenir des hashes SHA » parce que le dataset internet est « 0,001 % cognition et 99,99 % information » ; extrait ce noyau qui *pense* et sait appeler des outils, **un milliard de paramètres suffit, peut-être moins**, la distillation marchant « étonnamment bien ». Côté humain, c'est la réponse finale sur ce qu'il faut faire étudier aux enfants : maths, physique, CS — ***« symbol manipulation heavy tasks, not memory heavy tasks »***, ~80 % du temps de la période critique. Entre les deux : l'architecture qui en découle (pas un modèle mais un **essaim / « companies of LLMs »** hiérarchique, CEO = gros modèle cloud, workers = modèles open source bon marché, escalade automatique selon la difficulté ; l'exocortex tourne en local), et la doctrine produit d'Eureka (l'enseignant passe **du front end au back end**, l'IA devient l'interface de l'étudiant — « AI TA »), avec l'avertissement qui date le mieux : ***« the demo is near but the product is far »***. Reposté sur X le 24 juil. 2026 sous un cadrage « ce qu'il faut enseigner avant l'AGI » (1 751 likes), ce qui en fait un **point de contrôle rétrospectif** : la prédiction du cognitive core a presque deux ans.

## Titre Article
No Priors Ep. 80 — With Andrej Karpathy from OpenAI and Tesla (segment final : cognitive core, swarm of LLMs, Eureka & éducation)

## Date
2024-09-05

## URL
https://www.youtube.com/watch?v=hM_h0UA7upI

<!-- Repost X de l'extrait (16 min 46 s) qui a relancé la circulation du segment le 2026-07-24, sous le cadrage « A father asked Karpathy what to teach his 8-year-old before AGI » (1 751 likes, 208 RT) : https://x.com/expemillyweb3/status/2080691057906323907 — brut et transcription diarisée dans raw-data/karpathy-cognitive-core-exocortex-education-2024-09-05.md -->

## Keywords
Andrej Karpathy, No Priors, Sarah Guo, Elad Gil, cognitive core, noyau cognitif, un milliard de paramètres, distillation, small language model, modèles minuscules, dataset non curé, SHA hashes, 0.001% cognition, tool use, appel d'outils, exocortex, edge device, inférence locale, coût d'inférence, companies of LLMs, swarm, essaim de modèles, écosystème biologique, spécialisation, hiérarchie d'entreprise, escalade automatique, CEO cloud model, workers open source, cost functions, Eureka Labs, CS231n, Stanford, teacher back end, AI front end, AI TA, scaling d'un enseignant, 8 milliards de personnes, traduction low hanging fruit, adaptativité au background, analogies pédagogiques, demo is near product is far, effet 2 sigma, Bloom, tutorat un-à-un, The Diamond Age, Young Lady's Illustrated Primer, team human, empower not displace, lineage, gatekeeping, H-index, effet de cluster, Bay Area, culture comme variable dominante, Slovaquie, University of Toronto, entrepreneuriat, learning is hard, gym pour le cerveau, pre-AGI education, post-AGI education entertainment, cours undergrad, retour à l'école, apprentissage tout au long de la vie, math physique CS, symbol manipulation, memory heavy tasks, 80% du curriculum, période critique

## Authors
Andrej Karpathy (invité — membre fondateur d'OpenAI, ex-directeur IA de Tesla Autopilot, fondateur d'Eureka Labs) ; Sarah Guo & Elad Gil (hôtes du podcast No Priors)

## Ton
**Profil** : podcast VC-tech en format conversation à trois, registre détendu et spéculatif. Karpathy parle en oral hésitant (« uh », « I think », « we'll see »), les deux hôtes — investisseurs (Conviction, solo GP) — jouent le rôle de relanceurs cultivés : ils apportent la référence académique (l'effet 2 sigma de Bloom, la littérature des années 80), la référence littéraire (*The Diamond Age*), l'analogie sportive (les Jeux Olympiques « il y a un mois »), et poussent Karpathy vers la formalisation qu'il refuse poliment (« is there a mathematical representation of that ? » → « maybe, maybe… »). Public : fondateurs, investisseurs, ingénieurs IA.

**Style** : pensée à voix haute, par estimations rondes assumées comme provisoires (« I think even a billion. Billion suffices » ; « I think even one billion is too much, I don't know »). Karpathy avance en **ratios frappants** plutôt qu'en chiffres sourcés — 0,001 % / 99,99 %, 80 % du curriculum — qui sont des figures rhétoriques, pas des mesures. Il enchaîne systématiquement une thèse technique et sa transposition sociale (le modèle qui ne doit pas mémoriser → l'enfant qui ne doit pas mémoriser ; l'entreprise comme architecture de parallélisation → les LLMs organisés en entreprise). Deux registres cohabitent : **ingénieur prudent** sur les capacités présentes (« the demo is near but the product is far », « I don't think the models are good enough to create a good course ») et **prescripteur assumé** sur les valeurs (« there's a correct answer in my mind », « team human »). L'humilité est réelle mais bornée : sur l'éducation, il tranche. Aphorismes plantés : *« the cognitive core »*, *« companies of LLMs »*, *« the demo is near but the product is far »*, *« learning is like going to the gym but for the brain »*, *« symbol manipulation, not memory »*. Position épistémique : **optimiste outillé, pessimiste sur les institutions** — l'éducation est déjà accessible, ce qui bloque, c'est la culture d'appartenance.

## Pense-betes
- **Provenance et datation** — la fiche est datée du **2024-09-05** (publication de l'épisode No Priors n° 80), pas du repost X du 2026-07-24 qui a relancé sa circulation. C'est ce décalage qui donne sa valeur à la fiche : les prédictions y sont **testables avec ~2 ans de recul**. Le repost (@expemillyweb3, 1 751 likes / 208 RT) recadre l'extrait en « un père demande quoi enseigner à son enfant de 8 ans avant l'AGI » — **reformulation inexacte** : la question est posée par un hôte, sans âge mentionné.
- **Attribution des voix** : la transcription diarisée distingue trois locuteurs mais le mapping Locuteur 2 / Locuteur 3 ↔ Sarah Guo / Elad Gil **n'est pas établi**. Les propos d'hôtes sont donc attribués au podcast, pas nommément, dans le graphe.
- **Cognitive core — l'argument en trois temps** :
  1. *Constat* : « current models are wasting a ton of capacity remembering stuff that doesn't matter. Like they remember SHA hashes » — cause désignée par un hôte et validée par Karpathy : **le dataset n'est pas curé**.
  2. *Ratio* : « The internet is like 0.001% cognition and like 99.99% of like information » — la partie utile au *thinking* est infime.
  3. *Cible* : « we just need to get to the cognitive core… it's just this thing that thinks, and if it needs to look up information, it knows how to use different tools ». Taille : **« I think even a billion. Billion suffices »**, puis surenchère : « I think even one billion is too much ».
- **Pourquoi c'est possible : la distillation.** « Distillation works like surprisingly well… you get a really big model or a huge amount of compute supervising a very small model… you can stuff a lot of capability into a very small model. » C'est **le seul mécanisme** invoqué — pas d'architecture nouvelle, pas de données nouvelles.
- **Question laissée ouverte (intéressante)** : un hôte demande s'il existe une **formulation mathématique / théorie de l'information** de la capacité cognitive rapportée à la taille du modèle. Karpathy n'a pas de réponse — il répond par le ratio internet. À suivre comme angle mort : on prédit une taille sans savoir la calculer.
- **Conséquences immédiates tirées par les hôtes** : bascule edge vs cloud, effondrement du **coût brut d'inférence**, et surtout — *« at less than a billion parameters, I have my exocortex on a local device as well »*.
- **Mais pas un modèle unique — « companies of LLMs »** (le passage le plus architectural) :
  - Motif : on veut de la **parallélisation**, pas un processus séquentiel. « Companies to some extent are also kind of like parallelization of work », et la hiérarchie existe parce que c'est une façon de faire le *traitement et les réductions d'information* dans une organisation.
  - Forme : « models of different capabilities specialized to various unique domains, maybe there's a programmer… a program manager… working in parallel and coming together and **orchestrating computation on your behalf** ».
  - Métaphore corrigée en direct : pas un modèle, **un essaim** — « your exocortex is like a swarm of these » ; un hôte propose « écosystème biologique avec rôles et niches », plus **l'escalade automatique vers d'autres parties de l'essaim selon la difficulté et la spécialisation**.
  - Économie : « maybe the CEO is like a really brilliant cloud model, but **the workers can be a lot cheaper, maybe even open source models** » + « my cost functions are different from your cost functions ».
  - ⚠️ À lire aujourd'hui comme une **description anticipée du multi-agent** (orchestrateur + sous-agents spécialisés, routage par difficulté, modèles bon marché en exécution) formulée avant que le pattern ne soit outillé.
- **Pourquoi il quitte OpenAI pour l'éducation** : « most of it is to kind of like replace or displace people… I'm always more interested in anything that **empowers** people. I'm kind of on a high-level like **team human**. » Et la question directrice : *how far can a person go if they have the perfect tutor for all the subjects* — les riches ont des tuteurs et vont loin, l'IA peut approcher voire dépasser ça.
- **Effet 2 sigma de Bloom** — apporté par les hôtes (« one standard deviation… » / « Two, Bloom! »), avec la référence à *The Diamond Age* de Neal Stephenson et son *Young Lady's Illustrated Primer*. ⚠️ Repère de vigilance : la mesure de terrain la plus proche dans le corpus (Banque mondiale, Nigeria) donne **0,31 SD**, pas 2 SD — l'écart entre l'idéal cité en podcast et le mesuré est d'un ordre de grandeur.
- **Doctrine produit Eureka (le point le plus actionnable)** — inversion des rôles :
  - « At the current AI capability, **I don't think the models are good enough to create a good course**. But they are good to become the **front end to the student** and interpret the course to them. »
  - « The teacher is not the front end anymore, the teacher is **on the back end designing materials and the course**, and the AI is the front end and it can speak all the different languages. » → assumé comme un **« AI TA »**.
  - Problème posé : un enseignant ne scale pas à « maybe like 8 billion people on Earth », multilingues, de niveaux différents. Karpathy a déjà enseigné **CS231n à Stanford** (premier cours de deep learning).
  - Méta-règle de conception : viser le **sweet spot des capacités du jour** — « a lot of companies don't quite understand intuitively where the capabilities [are] today, and they end up building things too ahead of what's available, or maybe not ambitious enough ».
- **Gradient de difficulté annoncé** : *low hanging fruit* = **traduction/localisation à la volée** (les modèles y sont déjà bons) ; plus dur mais « pas trop loin » = **adaptation au background** de l'apprenant, en particulier faire des **analogies vers les disciplines qu'il connaît déjà** (« extremely powerful in education »). Réserve : *« the easy version is a prompt away… but I mean something that actually works, not something you can demo »*.
- **Formule à retenir** : ***« the demo is near but the product is far »*** — l'énoncé le plus réutilisable de l'extrait, et le plus vérifié depuis.
- **Lineage et culture** : Karpathy refuse le monde où la filiation de labo compte (« gatekeeping by some finite scarce resource ») et espère que l'IA « détruise cette structure ». Mais il concède que le **cluster** apporte deux choses distinctes : (1) éducation/apprentissage — *« yours is the easier one »*, largement disponible aujourd'hui ; (2) **culture** — ce que le milieu met sur un piédestal (le **H-index** en académie), qui est selon lui **la variable dominante**. Exemple autobiographique : University of Toronto, où « il ne t'occurre même pas que tu devrais créer une entreprise », la conversation portant sur les stages et une liste fermée d'employeurs.
- **Apprendre ≠ se divertir** : « learning is like going to the gym but for the brain » — effort, mais plaisir et *payoff*. Séquence prédictive nette : **société pré-AGI** → on apprend pour des raisons pratiques (emploi, ascension économique) ; **société post-AGI** → « education is entertainment to a much larger extent », avec l'espoir que la salle de sport mentale devienne un objet de statut social.
- **Public d'Eureka** : cours de **niveau undergrad technique**, « le cours où aller si tu veux apprendre l'IA », mais tout âge — parce que « we have this **antiquated concept of education** where you go through school and then you graduate and go to work », qui casse dans une société qui se renouvelle vite (retours à l'école fréquents). Timeline annoncée : espérée fin 2024, « probablement début d'année prochaine », avec l'aveu « I do have a lot of distractions that are piling up ».
- **La réponse finale (celle qui a fait le repost)** — « There's a correct answer in my mind : **math, physics, CS** ». Justification : meilleur **socle de compétences de pensée**, utile pré-AGI et nécessaire post-AGI (« you still want **empowered humans** who can function in any arbitrary capacity »). Cadrage temporel : la **période critique** où l'on dispose de temps et d'attention doit aller aux **« symbol manipulation heavy tasks and workloads, not memory heavy tasks »**. Nuance systématiquement coupée dans les reprises : « I would of course put in a bunch of other stuff as well… it's actually beautiful to have a large diversity of things, **but I do think 80% of it should be something like this** ».
- **La symétrie qui structure tout l'extrait** : le reproche fait aux modèles (dépenser de la capacité en mémorisation faute de dataset curé) et le conseil éducatif (ne pas dépenser la période critique en tâches de mémoire) sont **le même argument**. Le corollaire est énoncé par un hôte en clôture : *« we're not efficient memorizers compared to our tools »*.
- **Articulation dossier veille** :
  - **Karpathy sur Karpathy, 19 mois plus tard** : [[karpathy-vibe-coding-agentic-engineering-software-3-0-2026-04-29]] prolonge exactement la même ligne — le *cognitive core* de 2024 devient « you can outsource your thinking but you can't outsource your understanding », et les *companies of LLMs* deviennent l'*agentic engineering* (coordonner des agents spiky). Les deux fiches se lisent en paire.
  - **Vérification de la thèse petits modèles / open weights** : [[sfeir-kimi-k3-moonshot-frontier-open-weights-2026-07-16]] et [[deanwball-open-weights-decelerationnistes-kimi-2026-07-17]] pour les *workers open source bon marché* ; [[sfeir-zml-llmd-docker-llm-inference-souveraine-2026-07-09]] pour l'inférence locale/souveraine qui donne corps à l'*exocortex sur device*.
  - **Éducation** : [[worldbank-chalkboards-chatbots-genai-education-nigeria-2025-12]] fournit le contrepoint chiffré au 2-sigma de Bloom (0,31 SD, 48 $/élève) ; [[connelly-nyt-ai-companies-eating-higher-education-2026-02-12]] montre le versant institutionnel (les labos mangent l'enseignement supérieur) là où Karpathy pariait sur le contournement ; [[youtube-educational-content-ai-tutorials-explosion-2025-10-01]] documente la démocratisation par le contenu ; [[maitriser-claude-code-formation-pedagogique-deep-research-2026-02]] est une application directe du pattern « enseignant en back-end, IA en front-end ».
  - **Emploi / motivation d'apprendre** : [[sfeir-ia-emploi-risque-decrochage-2026-07-23]] met sous tension la séquence « pré-AGI on apprend pour l'emploi » en montrant le décrochage quand ce motif s'affaisse.
  - **Multi-agent** : la description de l'essaim hiérarchique anticipe les patterns documentés dans [[williams-adlc-5-three-dials-parallel-agents-2026-06-12]] (parallélisme d'agents) et [[akhouri-adhd-ideation-divergente-parallele-2026-07-20]] (idéation divergente parallèle).

## RésuméDe400mots

Dans le segment final de l'épisode 80 de *No Priors* (5 septembre 2024), Andrej Karpathy — membre fondateur d'OpenAI, ex-Autopilot Tesla, alors tout juste lancé dans Eureka Labs — développe une thèse et sa transposition pédagogique.

**La thèse : le *cognitive core*.** Les modèles actuels « gaspillent une tonne de capacité à mémoriser des choses sans importance » — des hashes SHA, des trivia — parce que le dataset d'entraînement n'est pas curé. Or « l'internet, c'est 0,001 % de cognition et 99,99 % d'information ». Il faut donc extraire le noyau : *« cette chose qui pense, et qui, si elle a besoin d'une information, sait utiliser des outils »*. Sa taille ? **Un milliard de paramètres suffit**, et probablement moins. Le seul mécanisme invoqué est la **distillation**, qui « marche étonnamment bien » : un très gros modèle supervise un très petit et y comprime beaucoup de capacité. Un hôte demande s'il existe une formalisation mathématique de la capacité cognitive rapportée à la taille — Karpathy n'en a pas.

**L'architecture qui suit.** Ce ne sera pas un modèle unique : on veut de la parallélisation, et les entreprises sont précisément des machines à paralléliser le travail, avec une hiérarchie qui sert à réduire l'information. D'où des **« companies of LLMs »** : des modèles de capacités différentes spécialisés par domaine (un programmeur, un chef de projet) qui orchestrent du calcul pour vous. La bonne métaphore est **l'essaim** — un écosystème avec des niches, une escalade automatique selon la difficulté, un « CEO » qui serait un gros modèle cloud et des « workers » bien moins chers, éventuellement open source. L'exocortex tient alors sur un appareil local.

**La transposition : Eureka.** Karpathy quitte un secteur qui cherche surtout à « remplacer les gens » ; il se dit *team human*. Sa question : jusqu'où irait quelqu'un doté du tuteur parfait ? Comme les modèles ne savent pas encore concevoir un bon cours, il inverse les rôles — **l'enseignant passe en back-end** (curriculum, matériel) et **l'IA devient le front-end de l'étudiant**, capable de parler toutes les langues : un « AI TA ». La traduction est le fruit à portée de main ; l'adaptation au background de l'apprenant vient ensuite. Avertissement : *« the demo is near but the product is far »*.

**La conclusion.** Ce qui bloque n'est plus l'accès au savoir mais la culture d'appartenance (le H-index, les clusters). Apprendre reste dur — « une salle de sport pour le cerveau » ; utile avant l'AGI, divertissement de statut après. Et pour les enfants : maths, physique, CS, ~80 % du temps — **manipulation de symboles, pas mémorisation**. Le même argument que pour les modèles.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Andrej Karpathy | PERSONNE | observé_dans | No Priors Ep. 80 | EVENEMENT | 0.99 | STATIQUE | déclaré_article |
| Andrej Karpathy | PERSONNE | affirme_que | les modèles actuels gaspillent une part majeure de leur capacité à mémoriser des informations sans valeur cognitive, faute de dataset curé | AFFIRMATION | 0.97 | STATIQUE | déclaré_article |
| Andrej Karpathy | PERSONNE | affirme_que | "The internet is like 0.001% cognition and like 99.99% of information" | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | prédit | "I think even a billion. Billion suffices" (taille visée du cognitive core) | CITATION | 0.96 | STATIQUE | déclaré_article |
| Cognitive core | CONCEPT | est_basé_sur | distillation | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Distillation | METHODOLOGIE | permet | compression d'une large capacité dans un très petit modèle | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Cognitive core | CONCEPT | utilise | appel d'outils externes pour la recherche d'information | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Cognitive core | CONCEPT | permet | exocortex exécuté sur un appareil local | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | prédit | l'IA prendra la forme de "companies of LLMs" — un essaim hiérarchique de modèles spécialisés orchestrant du calcul | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Companies of LLMs | CONCEPT | s_inspire_de | hiérarchie d'entreprise comme machine de parallélisation et de réduction de l'information | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| Companies of LLMs | CONCEPT | utilise | modèles open source bon marché comme workers, gros modèle cloud comme CEO | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | a_créé | Eureka Labs | ORGANISATION | 0.93 | STATIQUE | déclaré_article |
| Andrej Karpathy | PERSONNE | recommande | l'enseignant conçoit le cours en back-end et l'IA devient le front-end de l'étudiant ("AI TA") | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | affirme_que | les modèles ne sont pas assez bons pour créer un bon cours, mais assez bons pour l'interpréter à l'étudiant | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |
| IA | TECHNOLOGIE | permet | scaling d'un bon enseignant vers 8 milliards de personnes multilingues | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | affirme_que | "the demo is near but the product is far" | CITATION | 0.97 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | s_oppose_à | lineage académique comme gatekeeping par une ressource rare | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | affirme_que | la culture d'une communauté (ce qu'elle met sur un piédestal) pèse plus que l'accès à l'éducation, déjà largement disponible | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | prédit | "in a post-AGI society education is entertainment to a much larger extent" | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | recommande | maths, physique et CS pour ~80 % de la période critique : tâches de manipulation de symboles, pas de mémorisation | AFFIRMATION | 0.97 | ATEMPOREL | déclaré_article |
| No Priors Ep. 80 | EVENEMENT | référence | Effet 2 sigma de Bloom | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| No Priors Ep. 80 | EVENEMENT | référence | The Diamond Age | DOCUMENT | 0.88 | STATIQUE | déclaré_article |
| Andrej Karpathy | PERSONNE | a_créé | CS231n | DOCUMENT | 0.94 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Andrej Karpathy | PERSONNE | projet | Fondateur d'Eureka Labs après son départ d'OpenAI — posture revendiquée "team human" (empower plutôt que displace) | AJOUT |
| Cognitive core | CONCEPT | définition | Noyau de raisonnement d'un LLM une fois retirée la connaissance encyclopédique ; il pense et appelle des outils — Karpathy l'estime à ~1 milliard de paramètres, voire moins | AJOUT |
| Distillation | METHODOLOGIE | mécanisme | Un très gros modèle (ou beaucoup de compute) supervise un très petit modèle ; "works surprisingly well" — seul mécanisme invoqué pour justifier le cognitive core | AJOUT |
| Companies of LLMs | CONCEPT | définition | Essaim hiérarchique de modèles spécialisés (programmeur, chef de projet), escalade automatique selon la difficulté, CEO = modèle cloud, workers = modèles open source bon marché | AJOUT |
| Exocortex | CONCEPT | définition | Extension cognitive personnelle exécutée en local, rendue possible sous le milliard de paramètres ; forme d'essaim plutôt que de modèle unique | AJOUT |
| Eureka Labs | ORGANISATION | catégorie | École AI-native de Karpathy ; premier cours de niveau undergrad technique, public de tout âge, timeline annoncée fin 2024 → début 2025 | AJOUT |
| AI TA | METHODOLOGIE | fonctionnement | Inversion des rôles : enseignant en back-end (curriculum, matériel), IA en front-end de l'étudiant (multilingue, interprétation du cours) | AJOUT |
| Effet 2 sigma de Bloom | CONCEPT | définition | Littérature des années 80 : le tutorat un-à-un apporterait ~2 écarts-types de gain vs classe standard — cité par les hôtes comme horizon de l'IA éducative | AJOUT |
| No Priors Ep. 80 | EVENEMENT | date | 2024-09-05, podcast No Priors, hôtes Sarah Guo & Elad Gil, invité Andrej Karpathy | AJOUT |
| CS231n | DOCUMENT | catégorie | Premier cours de deep learning à Stanford, enseigné par Karpathy — référence de son expérience pédagogique | AJOUT |
| The Diamond Age | DOCUMENT | catégorie | Roman de Neal Stephenson, référence au Young Lady's Illustrated Primer comme archétype du tuteur personnel | AJOUT |
| Sarah Guo | PERSONNE | rôle | Investisseuse (Conviction), co-hôte du podcast No Priors | AJOUT |
| Elad Gil | PERSONNE | rôle | Investisseur, co-hôte du podcast No Priors | AJOUT |
