---
themes: [architecture-construction, outils-plateformes, economie-marche]
source: "All Things Distributed (blog de Werner Vogels)"
---
# warfield-duckdb-changing-physics-analytics-2026-08-26

## Veille

Billet invité d'**Andy Warfield**, ingénieur du service **S3** chez **AWS**, publié le **26 août 2026** sur *All Things Distributed*, le blog de **Werner Vogels**, qui le présente en quelques lignes signées *« --W »* : **3 554 mots** annoncés par la page. Le texte sert de véhicule à l'annonce que **DuckLabs**, l'équipe derrière **DuckDB**, rejoint **AWS**. (A) La thèse : l'informatique système consiste à chercher le compromis élégant face à une « physique » mobile — les rapports entre vitesse mémoire, réseau et calcul — et cette physique a changé. Warfield chiffre l'écart : une **m1.xlarge** de 2007 offrait **15 Go de RAM**, **4 cœurs virtuels** et **~1 Gb/s** de réseau ; une **m8g.48xlarge** d'aujourd'hui environ **50×** plus de chacun des trois. La croissance des jeux de données, elle, suit une distribution dont les très grands volumes sont la queue. (B) La conséquence : le traitement distribué — **MapReduce**, les **RDD** de **Spark** — a été conçu sous la contrainte d'I/O du début des années 2000, et une grande part du travail qui lui était confié n'a plus besoin de quitter l'application. D'où le moteur embarqué en bibliothèque, dans l'espace d'adressage de l'application, dont **DuckDB** est l'exemple. Warfield y adosse l'article *Scalability! But at what COST?* (2015) et l'épigraphe de **Paul Barham** : *« You can have a second computer once you've shown you know how to use the first one. »* Il pose une réserve explicite : *« When a job genuinely needs a thousand machines, it needs a thousand machines. »* Le corpus tient déjà [[vogels-tech-predictions-2026-allthingsdistributed-2025-11-25]] du même blog et [[anthropic-self-service-data-analytics-claude-agentic-stack-2026-06-03]] sur l'analytique en libre-service.

## Titre Article

DuckDB and the changing physics of analytics

## Date

2026-08-26

## URL

https://www.allthingsdistributed.com/2026/08/duckdb-and-the-changing-physics-of-analytics.html

## Keywords

DuckDB, DuckLabs, acquisition AWS, moteur analytique embarqué, bibliothèque en processus, physique changeante des systèmes, COST paper, Paul Barham, MapReduce, Spark RDD, traitement distribué, MonetDB, X100, CWI, vectorisation, SQLite, S3 Tables, Apache Iceberg, extension Iceberg v2 v3, I/O asynchrone, saturation du NIC, AWS Lambda, ATTACH, CONNECT, WebAssembly, glibc du données structurées, DuckDB Foundation, licence MIT, m1.xlarge, m8g.48xlarge, efficacité par cœur, analytique continue

## Authors

Andy Warfield, ingénieur du service S3 chez AWS, en billet invité sur *All Things Distributed* ; introduction de Werner Vogels, CTO d'Amazon.

## Ton

Profil : billet technique long-form à la première personne, registre de récit d'ingénieur plutôt que de communiqué, niveau technique moyen-élevé, public cible développeurs et architectes de systèmes de données. La construction va du souvenir personnel à l'annonce : une anecdote de pub britannique où des amis physiciens raillent l'informatique — *« any discipline that needs to put science in its name probably isn't a science »* — sert à installer la thèse que cette absence de vérité immuable est justement l'intérêt du métier. Suivent trois exemples situés dans le temps (le projet **NOW** de Berkeley, le travail de l'auteur sur **Xen**, les travaux **MonetDB**/**X100** au CWI), la remarque que ces contraintes reviennent par cycles — les idées de virtualisation de Xen étaient posées sur mainframes IBM dans les années 60 —, puis l'application au traitement de données. Warfield qualifie sa lecture des systèmes distribués : *« I mean this much more as an observation than as a criticism of these systems, because they were building for their own physics. »* Les titres de section filent le proverbe du canard (*If it walks like a duck… / …and quacks like a duck / …it must be a duck*), et l'anecdote du canard domestique de Hannes, Wilbur, est donnée comme origine du nom. Sont citables tels quels : la formule *« the glibc of structured data »*, l'énoncé que *« "analytics" is becoming less of a separate activity that happens to data somewhere else, and more of something you do continuously as you build »*, l'objectif rapporté de Hannes Mühleisen — permettre à *« anyone to work with data confidently »* — et la phrase du papier SIGMOD sur l'absence de composant révolutionnaire dans DuckDB.

## Pense-betes

- **L'argument est un rapport, pas une valeur absolue** : ce qui a bougé, ce sont les rapports entre calcul, mémoire et réseau sur une seule machine. Repères donnés : m1.xlarge de 2007 (15 Go, 4 vCPU, ~1 Gb/s) contre m8g.48xlarge (~50× sur les trois axes) ; le MacBook Pro de l'auteur revendique 3 à 5× les cœurs et la RAM, ~40× la bande passante mémoire et plus de 100× celle d'I/O par rapport à la m1.xlarge. Un serveur d'aujourd'hui dépasse les clusters sur lesquels beaucoup ont fait tourner Hadoop et Spark.
- **La croissance des données est une distribution, pas une tendance uniforme.** Les plus grands jeux croissent exponentiellement, mais ce sont la queue ; beaucoup d'autres suivent des grandeurs humaines — taille d'une entreprise, nombre de clients, nombre de transactions bancaires par jour. C'est l'écart entre les deux qui alimente le retour d'intérêt pour les moteurs mono-hôte.
- **Le papier COST comme point d'appui** : *Scalability! But at what COST?* (McSherry, Isard, Murray, 2015) compare une implémentation mono-thread bien optimisée aux frameworks distribués sur les mêmes tâches — sur des traitements de graphe, le thread unique bat les systèmes distribués tournant sur **128 cœurs**, et il faut **512 cœurs** pour que le distribué repasse devant. Warfield souligne que les auteurs travaillaient eux-mêmes sur des systèmes distribués : l'objet est l'efficacité par cœur, pas le rejet de la distribution.
- **Ce que change la forme « bibliothèque »** : le moteur tourne dans l'espace d'adressage de l'application, sur les structures mémoire déjà présentes, et se soucie autant de son propre surcoût que des requêtes qu'il exécute. Il n'a pas à être dans le client — il devient une brique plaçable là où elle est utile dans la pile, jusqu'à compiler en **WebAssembly** et tourner dans un onglet (shell.duckdb.org). Filiation revendiquée : le papier de démonstration SIGMOD 2019 s'appuyait sur la popularité de **SQLite**, et les deux fondateurs viennent du laboratoire CWI qui a produit MonetDB et X100.
- **La chronologie AWS ↔ DuckLabs, telle que rapportée** : AWS devient client de DuckLabs et sponsorise l'extension **Iceberg** pendant les travaux sur **S3 Tables**, l'objectif étant d'élargir Iceberg hors du monde Spark ; l'extension couvre désormais les spécifications **v2 et v3** et a motivé l'**I/O asynchrone** attendu en version **2.0**, dont l'objectif de conception est de saturer le NIC en scannant des tables sur S3. Chiffre unique de l'article : plus de **800 000 téléchargements par semaine** pour l'extension. Autres pistes citées : **Lambda** comme primitive pour lancer des requêtes, et les commandes **ATTACH**/**CONNECT** vers les moteurs AWS.
- **Termes de l'opération** : DuckLabs rejoint AWS **en tant que filiale** ; le projet DuckDB reste open source sous la garde de la **DuckDB Foundation**, développé par l'équipe DuckLabs, sous licence **MIT** ; l'équipe reste à Amsterdam. Hannes Mühleisen et Mark Raasveldt s'en expliquent dans un billet distinct sur le blog DuckLabs, non repris ici. AWS déclare viser les développeurs *« and increasingly agents »*, et utiliser déjà DuckDB en interne pour des tableaux de bord, de l'outillage CLI, des accélérateurs côté serveur et des ponts entre systèmes.
- ⚠️ **Ce que le texte ne donne pas** : aucun montant ni structure financière de l'opération, aucune donnée de performance comparée sur DuckDB lui-même, et aucune indication de gouvernance chiffrée pour la Fondation (composition, droits, engagement de durée). Le seul repère quantifié du billet reste le volume de téléchargements de l'extension.
- **À relier** : [[netflix-uda-unified-data-architecture-knowledge-graph-2025-06-12]] sur la modélisation unique consommée par plusieurs moteurs, et [[clouded-judgement-121225-long-live]] sur le déplacement de la valeur vers les systèmes d'enregistrement.

## RésuméDe400mots

Andy Warfield, ingénieur du service S3 chez AWS, publie le 26 août 2026 un billet invité sur All Things Distributed, présenté par Werner Vogels. Il y explique pourquoi les moteurs analytiques embarqués comme DuckDB prennent de l'importance, et annonce que DuckLabs, l'équipe qui développe DuckDB, rejoint AWS.

Sa grille de lecture est celle d'une « physique » mobile. Là où les sciences physiques explorent des invariants, l'informatique système cherche le compromis élégant face à des rapports qui bougent : vitesse de la mémoire contre celle du réseau, richesse des abstractions contre puissance disponible. Il cite trois moments — le projet NOW de Berkeley, ses propres travaux sur Xen, les recherches MonetDB et X100 au CWI d'Amsterdam, où le goulot du traitement de requêtes s'était déplacé du disque vers le CPU — et note que ces contraintes reviennent par cycles.

Appliquée aux données, cette grille explique le traitement distribué. Le traitement est toujours plus simple et plus efficace sur une seule machine rapide, mais quand le disque ou la carte réseau d'un serveur ne suffisent plus à lire le volume voulu, on partitionne. C'était la contrainte du début des années 2000, celle qui a produit MapReduce puis les RDD de Spark. Warfield relève deux qualités de ces systèmes : ils ont beaucoup innové sur l'ergonomie développeur, et ils ont assumé un coût fixe de planification et de distribution en pariant sur le débit obtenu par ajout de machines plutôt que sur l'efficacité unitaire.

Or les rapports ont changé. Une instance actuelle offre environ cinquante fois la mémoire, les cœurs et la bande passante réseau de la plus grosse instance EC2 de 2007, tandis que la croissance des jeux de données suit une distribution dont les cas extrêmes sont la queue. Le papier Scalability! But at what COST? de 2015 avait déjà montré qu'une implémentation mono-thread soignée pouvait battre des frameworks distribués sur cent vingt-huit cœurs.

DuckDB, lancé en 2018 par Hannes Mühleisen et Mark Raasveldt, applique cette logique : un moteur analytique en bibliothèque, tournant dans l'espace d'adressage de l'application, sur le modèle de diffusion de SQLite. AWS en est devenu client puis sponsor de l'extension Iceberg, dans le sillage de S3 Tables ; l'extension supporte Iceberg v2 et v3 et dépasse 800 000 téléchargements par semaine.

Warfield ne présente pas l'embarqué comme un remplacement : quand un traitement exige mille machines, il les exige. Ce qui change, écrit-il, c'est qu'une grande part du travail sur données n'avait jamais besoin d'un cluster. DuckLabs rejoint AWS comme filiale, le projet restant open source sous licence MIT et sous la garde de la DuckDB Foundation.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Andy Warfield | PERSONNE | a_créé | DuckDB and the changing physics of analytics | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Werner Vogels | PERSONNE | publie | DuckDB and the changing physics of analytics | DOCUMENT | 0.93 | STATIQUE | déclaré_article |
| Andy Warfield | PERSONNE | travaille_chez | AWS | ORGANISATION | 0.96 | DYNAMIQUE | déclaré_article |
| AWS | ORGANISATION | collabore_avec | DuckLabs | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| DuckLabs | ORGANISATION | fait_partie_de | AWS | ORGANISATION | 0.96 | STATIQUE | déclaré_article |
| Hannes Mühleisen | PERSONNE | a_créé | DuckDB | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Mark Raasveldt | PERSONNE | a_créé | DuckDB | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| DuckDB | TECHNOLOGIE | est_instance_de | moteur analytique embarqué | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| DuckDB | TECHNOLOGIE | s_inspire_de | SQLite | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| DuckDB | TECHNOLOGIE | est_basé_sur | MonetDB | TECHNOLOGIE | 0.87 | STATIQUE | inféré |
| DuckDB Foundation | ORGANISATION | permet | maintien de DuckDB en open source sous licence MIT après l'entrée de DuckLabs chez AWS | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |
| Andy Warfield | PERSONNE | affirme_que | les rapports entre calcul, mémoire et réseau sur une seule machine ne sont plus les contraintes qu'ils étaient | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| m8g.48xlarge | TECHNOLOGIE | mesure | environ 50× la mémoire, les cœurs et la bande passante réseau d'une m1.xlarge de 2007 (15 Go, 4 vCPU, ~1 Gb/s) | MESURE | 0.93 | STATIQUE | déclaré_article |
| Andy Warfield | PERSONNE | affirme_que | la croissance des jeux de données suit une distribution dont les très grands volumes sont la queue, beaucoup d'autres suivant des grandeurs humaines | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| MapReduce | TECHNOLOGIE | résout | contrainte de bande passante d'I/O des grands jeux de données du début des années 2000 | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| Spark | TECHNOLOGIE | utilise | Resilient Distributed Datasets | CONCEPT | 0.94 | STATIQUE | déclaré_article |
| Scalability! But at what COST? | DOCUMENT | mesure | une implémentation mono-thread optimisée bat des systèmes de graphe distribués sur 128 cœurs, le distribué ne repassant devant qu'à 512 cœurs | MESURE | 0.93 | STATIQUE | déclaré_article |
| Paul Barham | PERSONNE | affirme_que | « You can have a second computer once you've shown you know how to use the first one » | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| moteur analytique embarqué | CONCEPT | réduit | surcoût de planification, d'expédition de tâches et d'aller-retour réseau du traitement distribué | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Andy Warfield | PERSONNE | affirme_que | l'embarqué ne remplace pas le distribué : un travail qui exige mille machines les exige toujours | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| extension Iceberg de DuckDB | TECHNOLOGIE | mesure | plus de 800 000 téléchargements par semaine | MESURE | 0.92 | DYNAMIQUE | déclaré_article |
| extension Iceberg de DuckDB | TECHNOLOGIE | utilise | Apache Iceberg | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| DuckDB | TECHNOLOGIE | s_applique_à | S3 Tables | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| S3 Tables | TECHNOLOGIE | fait_partie_de | S3 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| I/O asynchrone | CONCEPT | permet | saturer le NIC lors du scan de tables stockées sur S3, attendu en DuckDB 2.0 | AFFIRMATION | 0.90 | DYNAMIQUE | déclaré_article |
| DuckDB | TECHNOLOGIE | s_applique_à | WebAssembly | TECHNOLOGIE | 0.91 | DYNAMIQUE | déclaré_article |
| Andy Warfield | PERSONNE | affirme_que | DuckDB est « the glibc of structured data » : une dépendance sobre et ubiquitaire à laquelle beaucoup de logiciels se lient sans y penser | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| Andy Warfield | PERSONNE | prédit | l'analytique cesse d'être une activité séparée pour devenir quelque chose que l'on fait en continu pendant qu'on construit | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| AWS | ORGANISATION | utilise | DuckDB en interne pour des tableaux de bord, de l'outillage CLI, des accélérateurs côté serveur et des ponts entre systèmes | AFFIRMATION | 0.89 | DYNAMIQUE | déclaré_article |
| Xen | TECHNOLOGIE | s_inspire_de | virtualisation des mainframes IBM des années 60 | CONCEPT | 0.88 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Andy Warfield | PERSONNE | rôle | Ingénieur du service S3 chez AWS, ancien contributeur au projet Xen, auteur du billet invité | AJOUT |
| Werner Vogels | PERSONNE | rôle | CTO d'Amazon, éditeur d'All Things Distributed ; signe l'introduction du billet | MISE_A_JOUR |
| Hannes Mühleisen | PERSONNE | rôle | Co-créateur de DuckDB, ancien chercheur au CWI ; formule l'objectif « allowing anyone to work with data confidently » | AJOUT |
| Mark Raasveldt | PERSONNE | rôle | Co-créateur de DuckDB, ancien chercheur au CWI | AJOUT |
| DuckDB | TECHNOLOGIE | catégorie | Moteur analytique SQL embarqué en bibliothèque, lancé en 2018, présenté au SIGMOD 2019, licence MIT, compilable en WebAssembly | AJOUT |
| DuckLabs | ORGANISATION | statut | Équipe de développement de DuckDB, rejoint AWS comme filiale, reste basée à Amsterdam | AJOUT |
| DuckDB Foundation | ORGANISATION | rôle | Structure gardienne du projet open source DuckDB, maintenue après l'entrée de DuckLabs chez AWS | AJOUT |
| moteur analytique embarqué | CONCEPT | définition | Moteur tournant en bibliothèque dans l'espace d'adressage de l'application, sur ses structures mémoire, sans service externe à l'autre bout d'un câble | AJOUT |
| Scalability! But at what COST? | DOCUMENT | référence | Papier de 2015 de Frank McSherry, Michael Isard et Derek Murray sur l'efficacité par cœur, dont l'épigraphe est attribuée à Paul Barham | AJOUT |
| AWS | ORGANISATION | rôle | Acquéreur de DuckLabs, client puis sponsor de l'extension Iceberg ; utilise DuckDB en interne et vise les développeurs « and increasingly agents » | AJOUT |
| S3 | TECHNOLOGIE | contexte | Service de stockage objet d'AWS, étendu par S3 Files, S3 Tables et S3 Vectors, dont l'équipe a observé l'embarquement de DuckDB chez ses clients | AJOUT |
| S3 Tables | TECHNOLOGIE | rôle | Primitive de stockage tabulaire de S3 bâtie sur Iceberg, motivée par les clients Spark adoptant Iceberg | AJOUT |
| extension Iceberg de DuckDB | TECHNOLOGIE | maturité | Implémentation des spécifications Iceberg v2 et v3, sponsorisée par AWS, plus de 800 000 téléchargements hebdomadaires | AJOUT |
| Apache Iceberg | TECHNOLOGIE | rôle | Format de table ouvert dont l'article vise l'élargissement hors du monde Spark | AJOUT |
| MonetDB | TECHNOLOGIE | apport | Travaux du CWI ayant déplacé l'exécution de requêtes vers des lots de valeurs tenant en cache, le goulot étant passé du disque au CPU | AJOUT |
| Spark | TECHNOLOGIE | apport | Chaînage d'opérateurs à évaluation paresseuse et dataframes, décomposés par un planificateur en tâches distribuées | AJOUT |
| MapReduce | TECHNOLOGIE | apport | Motif fonctionnel forçant les développeurs à exprimer le parallélisme explicitement ; l'auteur note qu'il s'agit plutôt de map/group-by-and-aggregate | AJOUT |
| Xen | TECHNOLOGIE | contexte | Hyperviseur issu des travaux doctoraux de l'auteur, tirant parti de l'abondance de CPU, mémoire et réseau sur un serveur unique | AJOUT |
| AWS Lambda | TECHNOLOGIE | rôle | Explorée comme primitive adaptée au lancement rapide de requêtes DuckDB | AJOUT |
