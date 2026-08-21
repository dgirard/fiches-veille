# Concepts

Shared domain vocabulary for this project — entities, named processes, and status concepts with project-specific meaning. Seeded with core domain vocabulary, then accretes as ce-compound and ce-compound-refresh process learnings; direct edits are fine. Glossary only, not a spec or catch-all.

## Pipeline médaillon

### Fiche
L'unité atomique de la veille : l'analyse d'**un** article, en dix sections gelées et dans un ordre fixe, portant un identifiant unique global et une date de publication qui fait foi. La date détermine le mois de classement et est gelée après le premier commit ; le contenu reste éditable, mais l'identifiant et le chemin ne bougent plus (traçabilité).

### Médaillon
Le modèle d'étages **logique** (aucun répertoire n'est renommé) qui structure le dépôt : Raw (brut non versionné) → Bronze (les fiches, sous gate de lint) → Silver (artefacts dérivés : catalogue, index, KB) → Gold (livrables). « Logique » : un consommateur externe lit les fiches par chemin, pas via le format des artefacts.

### Catalogue
La vue **machine** du corpus, une ligne par fiche, point d'entrée de la récupération *grep-first* — on grep le catalogue avant de lire une fiche. Généré : fonction pure des fiches, jamais édité à la main.

### KB générée
Les pages d'entités produites automatiquement à partir des graphes de connaissance de toutes les fiches (une page par [[Entité]], wikilinks Obsidian). Artefact Silver dérivé : régénéré, jamais édité ni mergé à la main.
*À ne pas confondre avec :* [[KB thématique curée]].

### KB thématique curée
Un dossier de synthèse **écrit à la main** sur un thème transverse (chronologie, fiches sources, entités, concepts). Versionné mais non dérivé : rien ne le régénère. Comme il n'a aucun gate de régénération, son seul filet de fraîcheur est le retard signalé par le [[Doctor]] — ce qui n'existe que si la KB est déclarée à celui-ci.
*À ne pas confondre avec :* [[KB générée]].

### Doctor
Le contrôle de cohérence exécuté avant tout commit ou toute lecture du corpus : il vérifie que les artefacts générés sont frais (via manifests), que la bijection catalogue↔fiches tient, et signale les KB thématiques curées en **retard**. Une incohérence bloquante sort en code ≠ 0 ; les avertissements (retards, quasi-doublons, brut manquant) ne bloquent pas.

### Retard (doctor)
État d'une [[KB thématique curée]] pour laquelle des fiches entrant dans son périmètre déclaré ont été publiées après sa date d'en-tête — signal, non bloquant, qu'il faut la ré-enrichir à la main.

## Graphe de connaissance

### Entité
Le nœud du graphe : une chose nommée (personne, organisation, technologie, concept…) qui reçoit une page dans la [[KB générée]] — sa propre page si elle est assez citée, sinon une section d'une page collective (voir [[Entité mineure]]). Une entité est identifiée par le **couple nom + type**, jamais par le nom seul — deux homonymes de types différents restent donc distincts et sont séparés automatiquement.

Son nom canonique est le **nom complet développé** ; un sigle n'est jamais un nom d'entité, seulement un alias porté en attribut. La raison est asymétrique : deux entités de **même type** qui partageraient un sigle fusionneraient silencieusement en une seule page, et c'est la seule collision qu'aucun contrôle automatique ne rattrape.

### Entité mineure
Une [[Entité]] trop peu citée pour justifier sa propre page : elle est regroupée avec ses semblables dans une page collective de la [[KB générée]], où elle occupe une ancre plutôt qu'un fichier. Le partage est automatique et se rejoue à chaque build — une entité franchit le seuil dans un sens ou dans l'autre au fil des fiches ajoutées.

« Assez citée » se mesure de deux façons, dont une seule suffit : être sujet d'assez de triples, ou apparaître dans assez de fiches distinctes. Une entité peut donc être majeure en n'étant citée que par une seule fiche, si celle-ci l'assertait abondamment. Conséquence pour la récupération : lister les pages de la KB ne voit que les entités majeures, alors que l'index alphabétique des entités les couvre toutes — c'est lui, et non la liste des fichiers, qui répond à « cette entité existe-t-elle ? ».

### Triple
L'assertion élémentaire du graphe, reliant un sujet à un objet par un prédicat issu d'un **registre fermé** — on choisit le prédicat le plus proche, on n'en invente jamais. Chaque triple porte aussi sa confiance, sa temporalité et sa **source épistémique** (énoncé par l'article, inféré, ou ajouté par l'assistant), ce qui permet de lire un fait rapporté autrement qu'une déduction.

Un objet qui n'est pas une [[Entité]] mais une proposition, un chiffre ou un verbatim se type comme tel et n'entre jamais dans la table des entités.

### Quasi-doublon
Deux noms d'[[Entité]] assez proches pour désigner probablement la même chose (casse, accents, séparateurs), observés **à l'échelle du corpus**. Ils sont **signalés à chaque build, jamais fusionnés automatiquement** : l'arbitrage est humain, parce qu'une fusion à l'aveugle détruit une désambiguïsation légitime.

Le rapport ne voit que la **fragmentation** — un même objet éclaté sur plusieurs noms. Il est structurellement aveugle à la **conflation** — plusieurs objets sous un seul nom —, qui ne produit qu'une entité et donc rien à comparer.
*À ne pas confondre avec :* [[Dérive de nommage]], qui est la même fragmentation observée **à l'intérieur d'une seule fiche**.

### Dérive de nommage
Un [[Triple]] qui désigne une [[Entité]] par une variante du nom sous lequel la **même fiche** la déclare — un qualificatif ajouté, une parenthèse, un pluriel. La déduplication traitant les deux libellés comme deux entités, le savoir de la fiche se scinde entre deux pages sans que rien ne le signale au lecteur.

Trois issues, et une seule est un renommage : **aligner** le triple sur le nom déclaré quand le référent est le même (la précision descend en attribut) ; **déclarer** l'entité quand le référent est réellement distinct d'un voisin de nom ; **éclater** le triple quand la cellule portait plusieurs entités à la fois — auquel cas ce n'était pas une dérive mais un triple malformé. Déclarer est sûr sur un nom propre et piégeux sur un mot courant : un générique déclaré fait dériver toute phrase qui le contient, si bien que le stock ne décroît qu'en mesurant après chaque vague de corrections. Enfin, un DOCUMENT ou un EVENEMENT porte normalement le nom de ce dont il parle : ce recouvrement-là applique la règle de désambiguïsation et n'est pas une dérive, sauf si les deux côtés portent le même type.
