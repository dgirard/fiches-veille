---
themes: [produits-services, economie-marche, strategie-frameworks]
source: "X"
---
# sarver-personal-ai-should-actually-be-personal-2026-09-29

## Veille

Long fil publié sur X le **29 septembre 2026** par **Ryan Sarver** (@rsarver), intitulé *« Personal AI Should Actually Be Personal »* ; environ **1 700 mots**, 91,5 k vues à la collecte. Point de départ : **Amazon** a bloqué **Muse** (**Meta**) de son site de vente, et les utilisateurs ont perdu l'accès à leur agent d'achat, *« a side effect of a dispute I had no say in »*. **(A)** Définition : une IA personnelle doit être **possédée** (open source, données en stockage contrôlé, portabilité), n'avoir **un seul mandant**, offrir un contrat lisible et des arbitrages inspectables, tourner où l'on choisit, et être agréable. **(B)** Constat sur l'existant : Muse inscrit par défaut à l'entraînement, **Instinct** avec une licence *« perpétuelle et irrévocable »* ; écart de coût estimé à **3 à 7 k$ par utilisateur et par an** contre 20 $ par mois. **(C)** Un renversement : la pile possédée peut être meilleure, car l'utilisateur lui donne *« every corner of your life »*. **(D)** Une pile en cinq couches (clients, harness et connecteurs, mémoire, modèles à deux niveaux, machine) et un appel à créer une version productisée d'**OpenClaw**. Répond à **Brad Gerstner** sur la confiance ; prolonge le corpus sur les agents d'achat et la mémoire en markdown.

## Titre Article

Personal AI Should Actually Be Personal

## Date

2026-09-29

## URL

https://x.com/rsarver/status/2104928906650304618

## Keywords

IA personnelle, personal AI, agent personnel, double mandant, principal unique, propriété des données, OpenClaw, Hermes, Muse, Meta, Instinct, Amazon, blocage d'agents, guerre de plateformes, entraînement sur données utilisateur, steering, orientation silencieuse, mémoire en markdown, LLM wiki, GBrain, modèles open-weights, routage de modèles, coût par utilisateur, machine louée, souveraineté des données, modèle d'affaires, produit grand public

## Authors

Ryan Sarver (@rsarver), auteur du fil sur X ; fonction non indiquée dans le texte.

## Ton

**Profil** : billet d'opinion d'un utilisateur intensif d'OpenClaw, qui se dit client des entreprises citées et écrit pour trouver un porteur de projet (*« if you're building it, I'd love to hear from you »*).

**Style** : plaidoyer structuré en définition, cas, pile technique, appel. Formules courtes (*« If you don't pay for the product, you are the product »*, *« OpenClaw feels like Linux. We need Apple experience »*), comparaisons avec la recherche web et le Linux/Apple.

**Position épistémique** : thèse assumée, chiffres rapportés de tiers ou d'usage personnel (3 à 7 k$ par an entendu d'Anish, 2 $ contre 46 $ par mois d'une décomposition non citée, 10 $ par mois la machine). L'auteur précise que Muse et Instinct sont de bons produits et que leurs conditions sont publiques ; l'inférence sur l'équilibre économique de Meta est posée comme question.

## Pense-betes

- **Déclencheur** : blocage de Muse par Amazon la semaine précédente, avec un message évoquant l'accès par un agent non autorisé. L'utilisateur, client des deux, n'est pas consulté.
- **Deux mandants** : un agent hébergé par une plateforme sert l'utilisateur et l'entreprise qui l'a construit, et la seconde est prioritaire. D'où le critère d'un **mandant unique**.
- **Cinq critères du « personnel »** : possédé, un seul mandant, contrat connu (modèle d'affaires, données, inspection de ce qu'il a pesé), lieu d'exécution libre et réversible, agréable à utiliser.
- ⭐ **Steering plus grave que dans la recherche** : avec dix liens, l'utilisateur choisit activement ; avec un agent, il délègue et veut le résultat, donc l'orientation passe **en silence** par un algorithme opaque. Exigence : préférences intégrées et décisions inspectables.
- **Économie** : coût de 3 à 7 k$ par utilisateur et par an contre 20 $ par mois ; question posée sur le remboursement de la subvention par une activité publicitaire.
- **Renversement de l'avantage données** : d'ordinaire l'acteur qui détient le plus de données a le meilleur produit ; ici la propriété permet l'accès le plus complet, et la mémoire **compose** dans le temps.
- **Pile en cinq couches** : clients (Muse et Instinct en avance) ; harness et connecteurs (OpenClaw, Hermes) avec approbations et journal ; mémoire lisible et exportable (LLM wiki de Karpathy, GBrain de Garry Tan) ; modèles à deux niveaux (open-weights par défaut, frontier appelé délibérément, ~2 $ par mois contre ~46 $) ; machine personnelle ou louée (~10 $ par mois).
- **Constat sur OpenClaw** : fondation solide (présidée par Dave Morin), mais trop de réglages pour le grand public ; il faut une version qui fait les choix, les garde réversibles et ajoute des surfaces mobile, bureau, messagerie.
- **Modèle de revenus voulu** : l'argent ne vient que de l'utilisateur ; paiement de mises à jour, logiciel acheté, machine et appels de modèle vendus par des acteurs dont c'est le seul métier.
- ⚠️ **Lacunes** : pas de description du routage entre modèles (dit *« mostly hand-built »*) ; chiffres de coût non sourcés ; aucun porteur de projet identifié.

## RésuméDe400mots

Dans ce fil du 29 septembre 2026, Ryan Sarver soutient que ce que l'on appelle aujourd'hui IA personnelle ne l'est pas. Il part d'un incident : Amazon a bloqué Muse, l'assistant de Meta, de son site de vente, affichant un message qui qualifie l'accès d'agent non autorisé. Les utilisateurs, clients des deux entreprises, ont perdu un usage central des agents, l'achat, à cause d'un différend auquel ils n'ont pas participé. Il y voit le début de guerres de plateformes où le consommateur sera pris entre deux feux.

Son argument central tient au double mandant. Un agent hébergé par une plateforme travaille pour l'utilisateur et pour l'entreprise qui l'a construit, et l'on sait laquelle prime. Il cite les conditions de Muse, où l'entraînement sur les conversations est activé par défaut, et celles d'Instinct, qui accordent une licence perpétuelle et irrévocable couvrant captures d'écran et frappes. Il ne dit pas que ces acteurs trichent : ils annoncent ce qu'ils font. Mais une IA personnelle est « maximaliste » en information, et c'est précisément celle qu'on devrait le moins confier à un tiers.

Il définit cinq exigences : posséder l'agent (open source, données sous contrôle, portabilité), n'avoir qu'un seul mandant, connaître le contrat et pouvoir inspecter les arbitrages, choisir où l'agent tourne, et avoir un produit agréable. L'orientation silencieuse lui paraît plus grave qu'en recherche : on délègue le choix et l'on ne voit plus les alternatives. Il rapporte que les assistants coûteraient 3 à 7 k$ par utilisateur et par an, contre 20 $ par mois facturés, et s'interroge sur la façon dont un acteur publicitaire récupérerait cette subvention.

Son paradoxe est que la propriété peut produire le meilleur produit : l'utilisateur donne tout à ce qu'il possède, la mémoire s'accumule, et l'accès le plus complet fait la qualité. Mais OpenClaw ressemble à Linux ; il faut une expérience à la Apple.

Il décrit la pile en cinq couches : des clients soignés ; un harness avec connecteurs, approbations et journal ; une mémoire lisible en markdown, à la manière du LLM wiki de Karpathy ou de GBrain ; deux niveaux de modèles, un open-weights par défaut (environ 2 $ par mois contre 46 $) et un frontier appelé à la demande ; et une machine personnelle ou louée (environ 10 $ par mois).

Il appelle à construire une version productisée d'OpenClaw, dont les revenus viennent uniquement de l'utilisateur, qui peut partir avec tout.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Ryan Sarver | PERSONNE | publie | article Personal AI Should Actually Be Personal | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Amazon | ORGANISATION | s_oppose_à | Muse | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Meta | ORGANISATION | a_créé | Muse | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| article Personal AI Should Actually Be Personal | DOCUMENT | affirme_que | un agent hébergé par une plateforme a deux mandants et le second prime, donc l'IA dite personnelle ne l'est pas | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| article Personal AI Should Actually Be Personal | DOCUMENT | recommande | IA personnelle possédée, à mandant unique, à contrat lisible, exécutée où l'utilisateur choisit | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Muse | TECHNOLOGIE | observé_dans | entraînement sur les conversations activé par défaut | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| Instinct | TECHNOLOGIE | observé_dans | licence perpétuelle et irrévocable couvrant captures d'écran et frappes, y compris pour l'entraînement | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| agent personnel | CONCEPT | mesure | coût de 3 à 7 k$ par utilisateur et par an contre 20 $ par mois facturés | MESURE | 0.8 | DYNAMIQUE | déclaré_article |
| article Personal AI Should Actually Be Personal | DOCUMENT | affirme_que | l'orientation silencieuse d'un agent est plus grave que celle d'un moteur de recherche, car l'utilisateur délègue le choix | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| article Personal AI Should Actually Be Personal | DOCUMENT | s_oppose_à | Brad Gerstner | PERSONNE | 0.8 | STATIQUE | déclaré_article |
| OpenClaw | TECHNOLOGIE | est_basé_sur | pile de l'IA personnelle | CONCEPT | 0.75 | DYNAMIQUE | inféré |
| Muse | TECHNOLOGIE | s_inspire_de | OpenClaw | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Hermes | TECHNOLOGIE | concurrence | OpenClaw | TECHNOLOGIE | 0.7 | DYNAMIQUE | inféré |
| LLM wiki | METHODOLOGIE | est_instance_de | mémoire en markdown lisible et modifiable | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | a_créé | LLM wiki | METHODOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Garry Tan | PERSONNE | a_créé | GBrain | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| routage à deux niveaux de modèles | METHODOLOGIE | réduit | le coût mensuel à environ 2 $ par utilisateur contre environ 46 $ par défaut | MESURE | 0.78 | STATIQUE | déclaré_article |
| Dave Morin | PERSONNE | dirige | fondation OpenClaw | ORGANISATION | 0.85 | DYNAMIQUE | déclaré_article |
| article Personal AI Should Actually Be Personal | DOCUMENT | affirme_que | "OpenClaw feels like Linux. We need Apple experience." | CITATION | 0.93 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Ryan Sarver | PERSONNE | rôle | Utilisateur intensif d'OpenClaw, auteur du fil ; fonction non précisée | AJOUT |
| Amazon | ORGANISATION | secteur | Commerce en ligne ; a bloqué Muse | AJOUT |
| Meta | ORGANISATION | secteur | Éditeur de Muse | AJOUT |
| Muse | TECHNOLOGIE | catégorie | Assistant personnel de Meta, entraînement activé par défaut | AJOUT |
| Instinct | TECHNOLOGIE | catégorie | Assistant personnel à licence perpétuelle sur les données | AJOUT |
| OpenClaw | TECHNOLOGIE | catégorie | Agent personnel open source, jugé difficile d'accès au grand public | AJOUT |
| Hermes | TECHNOLOGIE | catégorie | Harness d'agent cité avec OpenClaw | AJOUT |
| GBrain | TECHNOLOGIE | catégorie | Mémoire markdown pour agents de Garry Tan | AJOUT |
| LLM wiki | METHODOLOGIE | définition | Le modèle compile les informations en fichiers markdown éditables | AJOUT |
| agent personnel | CONCEPT | définition | Agent agissant pour un seul mandant, possédé par l'utilisateur | AJOUT |
| pile de l'IA personnelle | CONCEPT | définition | Clients, harness, mémoire, modèles, machine | AJOUT |
| routage à deux niveaux de modèles | METHODOLOGIE | définition | Open-weights par défaut, frontier appelé à la demande | AJOUT |
| fondation OpenClaw | ORGANISATION | secteur | Fondation présidée par Dave Morin | AJOUT |
| Brad Gerstner | PERSONNE | rôle | Interlocuteur cité (@altcap) | AJOUT |
| Andrej Karpathy | PERSONNE | rôle | Auteur du LLM wiki | AJOUT |
| Garry Tan | PERSONNE | rôle | Auteur de GBrain | AJOUT |
| Dave Morin | PERSONNE | rôle | Président de la fondation OpenClaw | AJOUT |
| article Personal AI Should Actually Be Personal | DOCUMENT | forme | Fil X du 29 septembre 2026 | AJOUT |
