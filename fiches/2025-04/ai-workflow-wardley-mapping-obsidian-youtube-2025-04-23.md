# ai-workflow-wardley-mapping-obsidian-youtube-2025-04-23

## Veille
Workflow IA pour générer Wardley Maps, LLM prompts capabilities, Obsidian graph, NetworkX clustering, bootstrap stratégique - Tutoriel vidéo

## Titre Article
AI Workflow for Creating Wardley Maps (Video Tutorial)

## Date
2025-04-23

## URL
https://www.youtube.com/watch?v=uU1fSE0piXM

## Keywords
Wardley Mapping automation, LLM prompts, capability decomposition, OpenAI API, Obsidian canvas, NetworkX clustering, value chain y-axis, graph relationships, strategic bootstrap, JSON output, capability relationships, proximity categorization, operational excellence

## Authors
Auteur vidéo (Product Manager ERP/Business Intelligence)

## Ton
**Profil :** Tutoriel praticien | Première personne, pédagogue | Registre pédagogique-démonstratif | Niveau technique intermédiaire à expert

Le praticien PM/BI adopte une voix de tutoriel YouTube combinant démonstration pratique et explication conceptuelle. Langage technique accessible (prompts LLM, canvas Obsidian, clustering NetworkX) qui guide le spectateur à travers le workflow. Le format vidéo permet la démonstration visuelle d'un processus d'automatisation complexe. Ton de praticien enthousiaste partageant un workflow découvert, plutôt que d'expert faisant autorité. Structure de tutoriel classique (problème → solution → mise en œuvre) qui facilite l'apprentissage. Typique des chaînes YouTube de praticiens partageant workflows personnels et découvertes, visant des pairs curieux d'automatiser leurs outils de réflexion stratégique.

## Pense-betes
- **Objectif** : utiliser l'IA pour amorcer (bootstrapper) une Wardley Map et obtenir rapidement un bon point de départ
- **Stack d'outils** : OpenAI API + Obsidian + Python NetworkX + frontend maison
- **Prompt 1 - Capacités** : « I'm product manager for [product]. Frame capabilities as 'the ability to [blank]'. Break down using 'is a function of the ability to'. Return JSON. »
- **Exemple de capacité** : « buy lunch for team » → décomposé en planifier des repas équilibrés, sourcer des ingrédients de qualité, préparer efficacement les repas, s'adapter aux préférences/allergies
- **Intégration Obsidian** : capacités déposées dans Obsidian, relations automatiquement liées (parent → sous-capacités)
- **Axe Y Wardley** : plus haut = plus proche du client, plus bas = abstrait/invisible pour le client
- **Prompt 2 - Positionnement sur l'axe Y** : catégoriser les capacités selon leur proximité avec différents rôles (leaders excellence opérationnelle → COO → program managers stratégiques → coachs/designers → ingénieurs opérations/IT → ingénieurs plateforme/data → couches infrastructure/utilitaires)
- **Toujours demander la justification** : « assigner un niveau + donner la justification » permet le réglage fin et de « rentrer dans le raisonnement du LLM »
- **Prompt 3 - Relations** : « identifier les relations significatives : capacités fonctionnellement similaires OU habilitantes. Retourner du JSON avec paire (deux IDs liés) + type (similar/enables) + explication claire »
- **Balayage aléatoire** : insérer les capacités au hasard, analyse stricte, comme « scanner un tableau et tracer des lignes entre éléments similaires »
- **Exemple de relation** : « analyze data insights » ↔ « trend analysis » = similaires (toutes deux centrées sur l'analyse de données pour en tirer des enseignements)
- **Clustering NetworkX** : bibliothèque Python d'analyse de graphes sociaux, identifie les clusters au sein de chaque niveau
- **Canvas final** : capacités organisées par niveau (axe Y) + cluster (approximation de l'axe X), avec la fonction de regroupement d'Obsidian
- **Navigation dans la chaîne de valeur** : exemple « un leader veut de la priorisation » → descendre la pile → identifier les différents éléments impliqués
- **Le bootstrap n'est pas la fin** : « ce n'est que le début, il faut maintenant passer du temps à apprendre le domaine en profondeur »

## RésuméDe400mots

**Objectif et contexte méthodologique**

Tutoriel vidéo démontrant un workflow pratique utilisant l'IA (LLM) pour amorcer la création d'une Wardley Map. L'auteur, product manager dans le domaine ERP/Business Intelligence, cherche à explorer un espace produit et à obtenir rapidement un bon point de départ plutôt que de partir d'une feuille blanche. L'approche reconnaît que le Wardley Mapping manuel est long et complexe, et propose une automatisation partielle pour accélérer la phase initiale d'exploration stratégique.

**Architecture technique : stack et outils**

Le workflow repose sur **quatre composants** : **(1) l'API OpenAI** pour générer capacités et relations via des prompts structurés ; **(2) Obsidian** comme outil de gestion des connaissances exploitant son graphe de relations natif ; **(3) Python avec la bibliothèque NetworkX** pour l'analyse de clustering de type graphe social ; **(4) un frontend maison** (optionnel) pour faciliter la saisie des prompts et capacités. L'intégration fluide permet de passer les sorties JSON du LLM directement dans Obsidian, puis de les exporter vers Python pour analyse avancée, puis de réimporter les données enrichies dans le canvas Obsidian.

**Trois prompts séquentiels structurés**

**Prompt 1 - Décomposition des capacités** : format strict « I'm product manager for [product] in [space]. Frame capabilities as 'the ability to [blank]'. Break down capabilities using '... is a function of the ability to...' Return results in JSON. » Exemple concret : « buy lunch for team » (capacité de premier niveau) décomposée automatiquement en sous-capacités : planifier des repas équilibrés, sourcer des ingrédients de qualité, préparer efficacement les repas, s'adapter aux préférences/allergies. La décomposition crée des **relations hiérarchiques parent → enfant** automatiquement liées dans le graphe Obsidian.

**Prompt 2 - Positionnement sur l'axe Y** : les Wardley Maps utilisent un axe Y représentant la proximité au client (haut = visible pour le client, bas = infrastructure abstraite/invisible). Le prompt catégorise les capacités selon leur proximité avec différents rôles d'une chaîne de valeur orientée excellence opérationnelle : **(niveau 1)** leaders excellence opérationnelle, COO, program managers stratégiques ; **(niveau 2)** coachs, designers ; **(niveau 3)** ingénieurs opérations/IT ; **(niveau 4)** ingénieurs plateforme et data ; **(niveau 5)** couches infrastructure/utilitaires. Point crucial : **toujours demander la justification** avec l'assignation du niveau. Cela permet de « rentrer dans le raisonnement du LLM » et facilite un réglage itératif. L'auteur souligne que ce prompt a nécessité un réglage en coulisses pour son domaine spécifique.

**Prompt 3 - Relations entre capacités** : « Étant donné une liste de capacités (chacune avec ID, nom, description), identifier les relations significatives. Soit fonctionnellement similaires, SOIT habilitantes. Être très précis. Retourner du JSON avec : paire (deux IDs de capacités liées), type (similar/enables), raison (explication claire). » Stratégie : **insérer les capacités au hasard**, analyse stricte, comme scanner un tableau et tracer des lignes entre éléments similaires. Exemple de sortie : « analyze data insights » ↔ « trend analysis » = similaires (toutes deux centrées sur l'analyse de données) ; « analyze data insights » habilite « actionable intelligence » (dérive de l'intelligence des motifs de données). Cela enrichit les relations au-delà de la simple hiérarchie parent-enfant.

**Clustering NetworkX et canvas final**

Après la création des capacités, des relations hiérarchiques, des relations de similarité/habilitation et des niveaux sur l'axe Y, le workflow utilise la **bibliothèque Python NetworkX** (standard de l'analyse de graphes sociaux) pour **identifier des clusters au sein de chaque niveau**. L'analyse de la densité des connexions, comme dans un réseau social, assigne des IDs de cluster. Résultat : chaque capacité possède **(1) un niveau sur l'axe Y** (proximité client), **(2) un ID de cluster** (regroupement logique au sein du niveau), **(3) des liens parent-enfant**, **(4) des liens de similarité/habilitation avec justifications**.

Les données enrichies sont importées dans le **canvas Obsidian** où les capacités sont visualisées. L'auteur utilise la **fonction de regroupement** d'Obsidian pour la lisibilité. Le clustering NetworkX produit parfois des regroupements sensés (exemple : « entrées horodatées, pistes d'audit des actions clés, préservation des données historiques » regroupées ensemble).

**Navigation dans la chaîne de valeur et philosophie du bootstrap**

Le canvas permet la **navigation dans la chaîne de valeur** : exemple « un leader veut de la priorisation » (haut de la carte) → descendre la pile niveau par niveau → identifier les différents éléments impliqués dans la priorisation. Démonstration concrète de la façon dont un besoin de haut niveau se décompose en capacités progressivement plus abstraites/infrastructurelles.

**Leçon clé** : l'auteur insiste : « ce n'est que le début, juste pour amorcer ». La sortie de l'IA n'est pas la carte finale mais un **point de départ accéléré**. L'intention : « passer ensuite beaucoup de temps à apprendre le domaine en profondeur ». L'IA réduit la friction initiale de la page blanche et permet au product manager de commencer immédiatement l'itération et le raffinement avec une structure de base solide, plutôt que des semaines de cartographie manuelle.

**Implications méthodologiques**

Le workflow démontre une **augmentation pragmatique par l'IA** : ni stratégie entièrement automatisée (impossible vu la nuance et le contexte), ni entièrement manuelle (trop lente). L'approche hybride exploite les forces du LLM (reconnaissance de motifs, décomposition logique, identification de relations) tout en reconnaissant que l'expertise humaine reste indispensable pour la validation, le réglage des prompts (via les justifications) et l'apprentissage approfondi du domaine après le bootstrap. Les justifications systématiques créent une **boucle de rétroaction** permettant au praticien de comprendre le raisonnement du LLM, d'ajuster les prompts itérativement et d'améliorer la qualité des sorties.

**Transférabilité au-delà du Wardley Mapping**

Bien que centrées sur les Wardley Maps, les techniques sont généralisables : décomposition de capacités, catégorisation par proximité, identification de relations et analyse de clustering s'appliquent à d'autres frameworks stratégiques nécessitant une pensée structurée sur les chaînes de valeur, les dépendances et les couches d'abstraction. La stack Obsidian + NetworkX + API LLM est particulièrement puissante pour les travailleurs du savoir explorant des domaines complexes.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| workflow IA Wardley | METHODOLOGIE | utilise | OpenAI API | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| workflow IA Wardley | METHODOLOGIE | utilise | Obsidian | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| workflow IA Wardley | METHODOLOGIE | utilise | NetworkX | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| NetworkX | TECHNOLOGIE | permet | clustering de graphe de capacités | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Obsidian | TECHNOLOGIE | permet | visualisation des relations parent-enfant de capacités | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Wardley Map | METHODOLOGIE | utilise | axe Y basé sur proximité client | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| LLM | TECHNOLOGIE | améliore | bootstrapping de cartographie stratégique | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| décomposition de capacités | METHODOLOGIE | permet | hiérarchie parent-enfant en JSON | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| rationale de prompt | CONCEPT | améliore | qualité des outputs LLM | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| workflow IA Wardley | METHODOLOGIE | s_applique_à | product managers ERP/BI | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| workflow IA Wardley | METHODOLOGIE | catégorie | Workflow d'automatisation de cartographie stratégique | AJOUT |
| Wardley Map | METHODOLOGIE | catégorie | Framework de cartographie de chaîne de valeur stratégique | AJOUT |
| OpenAI API | TECHNOLOGIE | usage | Génération de capacités et relations via prompts | AJOUT |
| Obsidian | TECHNOLOGIE | catégorie | Outil de gestion des connaissances avec graphe natif | AJOUT |
| NetworkX | TECHNOLOGIE | catégorie | Bibliothèque Python d'analyse de graphes et réseaux sociaux | AJOUT |
| décomposition de capacités | METHODOLOGIE | format_sortie | JSON hiérarchique parent-enfant | AJOUT |
| axe Y Wardley | CONCEPT | définition | Proximité client : haut = visible, bas = infrastructure | AJOUT |
