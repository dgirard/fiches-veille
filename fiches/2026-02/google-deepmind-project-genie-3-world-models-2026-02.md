# google-deepmind-project-genie-3-world-models-2026-02
## Veille
Project Genie - Modèles de monde interactifs temps réel Google DeepMind

## Titre Article
Project Genie: Interactive World Models with Genie 3

## Date
2026-02

## URL
https://www.youtube.com/watch?v=Ow0W3WlJxRY

## Keywords
World models, Project Genie, Genie 3, Google DeepMind, Google Labs, génération de mondes interactifs, temps réel, Nano Banana Pro, simulation, robotique, intelligence incarnée, Simmer, agents IA, médias interactifs, réalité virtuelle

## Authors
Logan Kilpatrick (Google DeepMind), Diego Schlomi (Google DeepMind), Jack (Google DeepMind)

## Ton
**Profil** : Conversation technique entre membres de l'équipe produit/recherche, registre accessible et enthousiaste, niveau technique modéré avec vulgarisation

**Description** : Format podcast "Release Notes" avec trois intervenants de Google DeepMind présentant Project Genie de manière conversationnelle. Le ton est celui d'une démonstration produit détendue, alternant entre explications techniques accessibles et moments de découverte spontanée lors des démos live. L'enthousiasme est palpable mais mesuré, avec une honnêteté sur les limitations actuelles du modèle. Les speakers adoptent une posture d'explorateurs partageant une technologie frontier, invitant le public à expérimenter plutôt qu'à consommer un produit fini. Le public cible est large : développeurs, créatifs, early adopters technophiles.

## Pense-betes
- **World model vs video model** : Un modèle vidéo génère une séquence fixe ; un world model génère frame par frame avec contrôle utilisateur en temps réel (gauche/droite/actions)
- **Project Genie = app grand public** : Équivalent de ce que Flow/ISK sont pour VO, lancé pour abonnés Google US Ultra
- **Pipeline créatif** : Nano Banana Pro génère d'abord une image "canvas", puis Genie 3 transforme cette image en monde explorable
- **Personnalisation clé** : Upload de photos personnelles (jouets, objets, espaces) pour les animer - différenciateur vs autres systèmes
- **Limite 60 secondes** : Compromis coût/serving, dynamisme diminue progressivement, "deux mondes d'une minute > un monde de deux minutes"
- **Physique implicite** : Le modèle apprend implicitement comment le monde évolue (balles qui roulent, eau qui éclabousse)
- **Problème plus difficile que vidéo** : Pas de liberté de modifier frames passées/futures, doit être cohérent avec passé ET action immédiate
- **Trajectoire Genie** : Genie 1 (papier recherche) → Genie 2 (déc 2024, 10s, basse résolution) → Genie 3 (août 2025 annonce, 1 min temps réel photoréaliste)
- **Cas d'usage Simmer** : Agent Gemini capable d'interagir dans mondes 3D, entraîné dans mondes Genie 3 pour tester généralisation
- **Roadmap évoquée** : Multijoueur (latence complexe), plus de contrôles/interactions, API développeur, surfaces au-delà de l'app
- **"Prompting is back"** : Le modèle n'est pas encore robuste au prompting, expérimentation requise - opportunité pour early adopters
- **Vision long terme** : "Copie de l'univers où on peut faire ce qu'on veut" - simulation indistinguable de la réalité comme north star

## RésuméDe400mots
Google DeepMind lance Project Genie, une application web permettant aux abonnés Google US Ultra de créer et explorer des mondes interactifs générés par le modèle Genie 3. Contrairement aux modèles vidéo classiques qui produisent des séquences fixes, un "world model" génère l'environnement frame par frame en temps réel, permettant à l'utilisateur de naviguer et interagir.

**Fonctionnement et pipeline créatif** : L'utilisateur commence par décrire son monde et son personnage. Nano Banana Pro génère d'abord une image "canvas" servant de point de départ visuel. En cliquant sur "Generate World", Genie 3 transforme cette image 2D en environnement 3D explorable. Le passage du 2D au 3D immersif constitue le "moment wow" identifié par les testeurs. L'application permet également d'uploader des photos personnelles - un jouet dinosaure photographié peut devenir un personnage contrôlable dans une reconstitution de la pièce.

**Défis techniques** : Genie 3 résout un problème plus complexe que la génération vidéo standard. Un modèle vidéo peut ajuster rétroactivement les frames pour assurer la cohérence ; Genie 3 doit générer en temps réel, cohérent avec le passé ET l'action immédiate de l'utilisateur, sans connaître les inputs futurs. La limite actuelle de 60 secondes résulte d'un compromis : le dynamisme du monde tend à diminuer progressivement, et les coûts de serving restent élevés.

**Évolution depuis Genie 1** : Genie 1 était un papier de recherche. Genie 2 (décembre 2024) offrait 10 secondes à basse résolution, sans temps réel. Genie 3 (annoncé août 2025, lancé maintenant) atteint une minute en temps réel avec qualité photoréaliste. L'équipe souligne qu'il y a un an, une minute de cohérence en temps réel semblait un objectif ambitieux ; aujourd'hui, les utilisateurs demandent plus.

**Applications envisagées** : Au-delà du divertissement, l'équipe explore l'éducation (expositions thérapeutiques personnalisées, comme un enfant explorant une pièce pleine d'araignées virtuelles) et l'intelligence incarnée. Le projet Simmer utilise déjà Genie 3 pour entraîner des agents IA capables d'accomplir des objectifs dans des mondes 3D arbitraires - étape vers l'AGI incarnée.

**Perspectives** : La roadmap inclut le multijoueur (complexe à cause de la latence), davantage de contrôles d'interaction, une API développeur, et l'expansion vers d'autres surfaces. L'équipe estime avoir atteint 50% de leur vision, avec un "headroom énorme" d'améliorations possibles. La vision ultime : une simulation indistinguable de la réalité, "une copie de l'univers où l'on peut faire ce qu'on veut".

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Google DeepMind | ORGANISATION | a_développé | Genie 3 | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Google DeepMind | ORGANISATION | a_lancé | Project Genie | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Project Genie | TECHNOLOGIE | est_basé_sur | Genie 3 | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Project Genie | TECHNOLOGIE | utilise | Nano Banana Pro | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Genie 3 | TECHNOLOGIE | améliore | Genie 2 | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Genie 2 | TECHNOLOGIE | a_été_publié | 2024-12 | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| Genie 3 | TECHNOLOGIE | est_basé_sur | modèles de monde interactifs | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Genie 3 | TECHNOLOGIE | diffère_de | modèles vidéo | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Simmer | TECHNOLOGIE | utilise | Genie 3 | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Simmer | TECHNOLOGIE | fait_partie_de | Google DeepMind | ORGANISATION | 0.90 | DYNAMIQUE | déclaré_article |
| Google Labs | ORGANISATION | collabore_avec | Google DeepMind | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Genie 3 | TECHNOLOGIE | cible | intelligence incarnée | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Logan Kilpatrick | PERSONNE | anime | Release Notes | EVENEMENT | 0.99 | STATIQUE | déclaré_article |
| modèles de monde interactifs | CONCEPT | permet | génération temps réel | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Genie 3 | TECHNOLOGIE | prédit | simulation indistinguable de la réalité | CONCEPT | 0.82 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Genie 3 | TECHNOLOGIE | catégorie | Modèle de monde interactif temps réel | AJOUT |
| Genie 3 | TECHNOLOGIE | capacité | Génération frame par frame, 1 minute, qualité photoréaliste | AJOUT |
| Project Genie | TECHNOLOGIE | audience | Abonnés Google US Ultra | AJOUT |
| Google DeepMind | ORGANISATION | secteur | Intelligence artificielle / Recherche | AJOUT |
| Google Labs | ORGANISATION | rôle | Partenaire produit et infrastructure | AJOUT |
| Nano Banana Pro | TECHNOLOGIE | rôle | Génération du canvas image initial | AJOUT |
| Simmer | TECHNOLOGIE | catégorie | Agent IA incarné dans mondes 3D (Gemini) | AJOUT |
| Genie 2 | TECHNOLOGIE | capacité | 10 secondes, basse résolution, non temps réel | AJOUT |
| Logan Kilpatrick | PERSONNE | rôle | Animateur Release Notes, Google DeepMind | AJOUT |
| intelligence incarnée | CONCEPT | description | IA opérant dans environnements physiques ou simulés | AJOUT |
| modèles de monde interactifs | CONCEPT | différence_clé | Cohérence temps réel sans modification des frames passées | AJOUT |
