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
Les pages d'entités produites automatiquement à partir des graphes de connaissance de toutes les fiches (une page par entité, wikilinks Obsidian). Artefact Silver dérivé : régénéré, jamais édité ni mergé à la main.
*À ne pas confondre avec :* [[KB thématique curée]].

### KB thématique curée
Un dossier de synthèse **écrit à la main** sur un thème transverse (chronologie, fiches sources, entités, concepts). Versionné mais non dérivé : rien ne le régénère. Comme il n'a aucun gate de régénération, son seul filet de fraîcheur est le retard signalé par le [[Doctor]] — ce qui n'existe que si la KB est déclarée à celui-ci.
*À ne pas confondre avec :* [[KB générée]].

### Doctor
Le contrôle de cohérence exécuté avant tout commit ou toute lecture du corpus : il vérifie que les artefacts générés sont frais (via manifests), que la bijection catalogue↔fiches tient, et signale les KB thématiques curées en **retard**. Une incohérence bloquante sort en code ≠ 0 ; les avertissements (retards, quasi-doublons, brut manquant) ne bloquent pas.

### Retard (doctor)
État d'une [[KB thématique curée]] pour laquelle des fiches entrant dans son périmètre déclaré ont été publiées après sa date d'en-tête — signal, non bloquant, qu'il faut la ré-enrichir à la main.
