---
themes: [qualite-securite, agents-codage-ia-skills, outils-plateformes]
source: SFEIR
---
# sfeir-rea-application-electron-2026-10-15

## Veille

Article **SFEIR AI** publié sur sfeir.com le **15 octobre 2026** et mis à jour le **21 octobre** (~6 000 signes, cinq sources), dans la série consacrée à **REA** (morluto/rea), outil de rétro-ingénierie piloté par agent. Il examine la cible où REA obtient ses meilleurs résultats : les applications **Electron**, dont le code voyage en JavaScript dans l'archive `app.asar`. Trois apports. **(A)** Le mécanisme : REA lit les fichiers sans lancer l'application, avec seulement Node.js et npm, et renvoie modules, imports, source maps, **canaux IPC**, add-ons natifs et état des **fuses** Electron ; Ghidra, Hopper ou IDA ne servent que pour les add-ons `.node`. **(B)** Trois tests publics : **Ishank Choudhary** (REA 6.4.0, application de 100 Mo, **52,2 s**, comptages conformes à grep mais **zéro preload** annoncé au lieu de deux, sans limitation signalée parmi 744), **Javier Cañete Arroyo** (Hyper 3.4.1, 253 Mo de preuves), **Connor Turland** (Slack 4.52.171, 45 canaux IPC, **43 004** inconnues). **(C)** Trois angles morts récurrents : noms minifiés, chemins construits à l'exécution, code servi par un serveur. Pour un éditeur, la structure et la logique client d'une application Electron sont *« lisibles par n'importe quel agent en moins d'une minute »*. Suite de [[sfeir-rea-trois-schemas-architecture-usage-2026-10-12]].

## Titre Article

Ce qu'une analyse REA révèle d'une application Electron

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/rea-application-electron/

## Keywords

REA, Reverse Engineer Anything, morluto/rea, Electron, app.asar, analyse statique JavaScript, Node.js, npm, canaux IPC, preload, contextBridge, BrowserWindow, add-ons natifs, .node, fuses Electron, intégrité de l'archive, Ghidra, Hopper, IDA, source maps, minification, inconnues, limitations, Slack, Hyper, PI-Desktop, rétro-ingénierie par agents, sécurité applicative, secrets dans l'ASAR, AI Cyber

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article technique de sécurité applicative, destiné aux éditeurs d'applications Electron et aux équipes sécurité. Français précis, chiffres de tests publics, FAQ courte.

**Style** : le texte s'organise autour des tests tiers, rapportés « comptage par comptage » (fenêtres, contextBridge, gestionnaires IPC) avec leurs écarts. Une section datée « Mise à jour du 21 octobre » ajoute deux applications réelles sans réécrire la partie initiale. Les angles morts sont regroupés en trois familles, puis traduits en conséquences pour l'éditeur.

**Position épistémique** : les chiffres sont attribués à leur auteur et à la version de REA utilisée (6.4.0, 6.7.0). Le texte souligne qu'aucune des 744 limitations ne signalait les preloads manquants, et qu'un zéro se vérifie à la main. Le cadre juridique est rappelé (n'analyser qu'un logiciel qu'on est autorisé à examiner) avec renvoi à l'article clean-room du même site.

## Pense-betes

- **Pourquoi Electron** : code en JavaScript dans `app.asar` (concaténation + index) → pas de décompilateur ; REA n'exige que Node.js et npm.
- **Ce que REA renvoie** : modules, imports, source maps, routes, canaux IPC, add-ons natifs ; lecture des **fuses** (EnableEmbeddedAsarIntegrityValidation, OnlyLoadAppFromAsar) sans lancer, modifier ni réseau.
- **Test Choudhary (11 octobre, REA 6.4.0, PI-Desktop v0.16.1)** : 100 Mo, 52,2 s, 421 fichiers JS, 3 114 427 nœuds AST, 59,2 Mo de résultats. Conformes à grep : 5 fenêtres, 2 contextBridge, IPC 4/6/5. Écarts : **0 preload au lieu de 2** (chemin construit par un helper), d'où 0 membre exposé ; contrôle d'expéditeur caché non vu ; 744 limitations, aucune sur les preloads.
- **Hyper 3.4.1 (Cañete Arroyo, REA 6.7.0)** : app.asar 14 Mo, 2 236 fichiers, 18 canaux IPC, 6 add-ons natifs, 253 Mo de preuves.
- **Slack 4.52.171 (Turland)** : 52 s au second passage, JSON 158 Mo, 529 fichiers JS, 1 904 modules, 45 canaux IPC, 8 add-ons, **43 004 inconnues** ; logique d'un contrôle de notifications comprise en une dizaine de minutes. Huit `.node` hors empreinte → re-signature suggérée par REA.
- **Angles morts** : noms minifiés, chemins dynamiques, code chargé depuis un serveur (jamais visible).
- **Volume** : 59 à 253 Mo de preuves débordent toute fenêtre de contexte → interroger REA par questions étroites.
- **Pour un éditeur** : structure, IPC et logique client lisibles en moins d'une minute ; retirer secrets et logique de valeur de l'archive.
- **Usage** : audit de sa propre application en statique ; binaire tiers inconnu en environnement isolé.
- **À relier** : [[sfeir-rea-evidence-sortie-agent-2026-10-15]], [[sfeir-rea-limites-2026-10-15]].

## RésuméDe400mots

L'article de SFEIR décrit ce que l'outil de rétro-ingénierie REA reconstruit d'une application Electron, la cible sur laquelle il obtient ses meilleurs résultats. Publié le 15 octobre 2026, il a été complété le 21 octobre par deux tests supplémentaires.

Une application Electron transporte tout son code en JavaScript dans une archive app.asar présente sur le disque de l'utilisateur. REA la lit sans lancer l'application, avec seulement Node.js et npm, et en extrait modules, imports, source maps, routes, canaux de communication inter-processus (IPC) et relations avec les add-ons natifs. Il lit aussi l'état des fuses, ces options gravées dans le binaire qui contrôlent par exemple la vérification d'intégrité de l'archive. Un décompilateur comme Ghidra, Hopper ou IDA n'intervient que pour examiner un add-on natif compilé.

Le premier test public, mené le 11 octobre par Ishank Choudhary avec REA 6.4.0 sur une application de 100 Mo, a pris 52,2 secondes. Les comptages de fenêtres, d'API contextBridge et de gestionnaires IPC concordent avec un grep sur le source. Mais REA a annoncé zéro script preload alors que l'application en charge deux, via un chemin construit à l'exécution ; ce zéro a vidé le comptage des membres exposés au renderer. Parmi les 744 limitations explicites de la sortie, aucune ne signalait ce manque.

La mise à jour ajoute deux applications réelles. Hyper 3.4.1, analysée par Javier Cañete Arroyo avec REA 6.7.0, a produit 253 Mo de preuves. Slack 4.52.171, analysée par Connor Turland, a révélé 45 canaux IPC et 8 add-ons natifs, avec 43 004 éléments marqués inconnus ; Turland dit avoir compris un contrôle de notifications en une dizaine de minutes, après avoir contourné un problème d'intégrité de l'archive.

Trois familles d'éléments échappent à l'analyse statique dans tous les tests : les noms minifiés, les chemins construits à l'exécution et le code chargé depuis un serveur. Le volume des preuves impose en outre d'interroger l'outil par questions ciblées.

Pour un éditeur, l'article conclut que la structure, les canaux IPC et la logique côté client d'une application Electron sont lisibles par un agent en moins d'une minute, secrets embarqués compris. Il recommande l'analyse statique pour auditer sa propre application, un environnement isolé pour tout binaire tiers, et rappelle que l'analyse doit porter sur un logiciel qu'on est autorisé à examiner.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Ce qu'une analyse REA révèle d'une application Electron | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | Electron | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Node.js | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | permet | reconstruction des canaux IPC et des add-ons natifs sans exécuter l'application | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Ishank Choudhary | PERSONNE | mesure | 52,2 s d'analyse pour une application Electron de 100 Mo avec REA 6.4.0 | MESURE | 0.9 | STATIQUE | déclaré_article |
| Ishank Choudhary | PERSONNE | mesure | zéro preload annoncé par REA pour deux chargés, sans limitation signalée | MESURE | 0.9 | STATIQUE | déclaré_article |
| Connor Turland | PERSONNE | mesure | 43 004 éléments inconnus et 45 canaux IPC sur Slack 4.52.171 | MESURE | 0.88 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | observé_dans | Slack | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | observé_dans | Hyper | TECHNOLOGIE | 0.82 | STATIQUE | déclaré_article |
| Javier Cañete Arroyo | PERSONNE | mesure | 253 Mo de preuves pour Hyper 3.4.1 avec REA 6.7.0 | MESURE | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | noms minifiés, chemins construits à l'exécution et code servi à distance échappent à l'analyse statique | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la structure et la logique client d'une application Electron sont lisibles par un agent en moins d'une minute | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | vérifier à la main tout zéro dans un comptage REA | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | retirer secrets et logique de valeur de l'archive app.asar | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle, éditeur de sfeir.com | AJOUT |
| REA | TECHNOLOGIE | catégorie | outil open source de rétro-ingénierie par agents (morluto/rea) | AJOUT |
| Electron | TECHNOLOGIE | propriété | Code JavaScript livré dans app.asar, lisible sans décompilateur | AJOUT |
| Ishank Choudhary | PERSONNE | support | Auteur d'un test public de REA sur HackerNoon (14 octobre 2026) | AJOUT |
| Connor Turland | PERSONNE | support | Cyrus ; analyse de Slack 4.52.171 avec REA (20 octobre 2026) | AJOUT |
| Javier Cañete Arroyo | PERSONNE | support | Jacar Systems ; analyse de Hyper 3.4.1 avec REA (19 octobre 2026) | AJOUT |
| Slack | TECHNOLOGIE | résultat REA | 529 fichiers JS, 1 904 modules, 45 canaux IPC, 8 add-ons natifs | AJOUT |
