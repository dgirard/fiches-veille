---
themes: [qualite-securite, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-rea-evidence-sortie-agent-2026-10-15

## Veille

Article **SFEIR AI** publié sur sfeir.com le **15 octobre 2026** et mis à jour le **21 octobre** (~6 000 signes, cinq sources), dans la série consacrée à **REA** (morluto/rea). Il propose une méthode de relecture des sorties d'un agent de rétro-ingénierie, en partant d'un test public : la même sortie comptait **744 limitations explicites** et annonçait **zéro preload** là où l'application en chargeait deux. Trois apports. **(A)** La place de l'erreur : REA renvoie des faits outillés et localisés, l'agent les résume et les relie, et *« les erreurs de lecture naissent presque toujours à cette étape »*. **(B)** Une grille de revue en **trois états** — **vu** (pointe vers un fichier, un décalage, une chaîne vérifiable), **inféré** (déduit d'un motif ou d'un nom), **inconnu** (non résolu) — présentée comme la méthode du cabinet et non comme une fonction de REA ; règle : une affirmation inférée ne remonte jamais comme vue. Les inconnues sont décrites comme *« la partie de la sortie qui ne vous trompera pas »*. **(C)** Deux pièges illustrés : un comptage pris pour une preuve de complétude, et le code plausible pris pour le code exécuté (test d'**Aayush Tyagi** sur Obsidian, prédiction écrite avant l'analyse, 1,83 $). La sortie devient utile une fois convertie en **golden master**. Complète [[sfeir-rea-application-electron-2026-10-15]].

## Titre Article

Lire une sortie REA : preuves, pseudocode et hallucinations

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/rea-evidence-lire-sortie-agent/

## Keywords

REA, Reverse Engineer Anything, morluto/rea, sortie d'agent, preuves localisées, pseudocode, assembleur, hallucination, revue en trois états, vu, inféré, inconnu, limitations, inconnues, complétude, faux zéro, preload, minification, code plausible, prédiction testable, table de vérification, Obsidian, Slack, Electron, Ghidra, golden master, tests de non-régression, rétro-ingénierie par agents, AI Cyber

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article de méthode pour équipes sécurité et équipes de migration qui relisent les conclusions d'un agent de rétro-ingénierie. Français précis, ton de revue technique, FAQ finale.

**Style** : ouverture sur un cas chiffré qui oppose deux informations de nature différente (une limitation signalée, une erreur non signalée). La grille en trois états est définie en une phrase par état, suivie d'une règle unique. Les deux pièges sont chacun adossés à un test public nommé, avec citation en anglais de l'auteur (*« Finding plausible-looking scoring code and assuming it is the code that runs is the classic failure mode here »*).

**Position épistémique** : le texte distingue ce que dit le dépôt de REA (preuves et limitations jointes, avertissement sur des résultats possiblement faux) de ce qui relève de la méthode du cabinet. Il rapporte aussi l'incertitude des auteurs cités (Choudhary « suppose, sans l'avoir confirmé » la cause du faux zéro). La mise à jour du 21 octobre est datée et isolée.

## Pense-betes

- **Cas d'ouverture** (Choudhary, 11 octobre, REA 6.4.0, app de 100 Mo) : 744 limitations (dont 365 liées au budget de résultat) + 0 preload annoncé pour 2 réels.
- **Ce que promet REA** : chaque conclusion avec preuves, limitations et localisation ; DISCLAIMER : décompilation et analyse IA *« peuvent être incomplètes ou fausses »*.
- **Où naît l'erreur** : entre l'outil (faits outillés) et l'agent (résumé, liens, explication).
- **Trois états** (méthode SFEIR) :
  - **Vu** : fichier, décalage, fonction, chaîne vérifiables par grep ou décompilateur
  - **Inféré** : déduit d'un motif, d'un nom, d'une habitude de framework
  - **Inconnu** : chemin, nom minifié, appel dynamique non résolu
  - règle : un inféré ne remonte jamais comme un vu
- **Inconnues = partie fiable** : REA refuse de conclure à l'absence (« ne prouve pas l'absence de la fonctionnalité »). Slack 4.52.171 (Turland) : 43 004 inconnues et une découverte exacte en ~10 minutes.
- **Piège 1, comptage ≠ complétude** : 5 fenêtres et 2 contextBridge justes, 0 preload faux ; 0 contrôle d'expéditeur alors qu'un `checkSender(e)` existait. Un zéro se vérifie à la main.
- **Piège 2, code plausible ≠ code exécuté** : Tyagi (Obsidian 1.14.4, quick switcher) vérifie l'héritage de la classe minifiée ; prédiction écrite avant, 24 classements relevés à la main, ambiguïté d'un décalage d'une unité révélée ; 7 min 8 s, 1,83 $.
- **Vers la preuve** : règle vue → cas de test ; règle inférée → confirmation métier avant toute ligne de code ; golden master sur l'application d'origine.
- **Validation** : recouper par grep/décompilateur, écrire une prédiction, convertir en tests.
- **À relier** : [[sfeir-rea-limites-2026-10-15]], [[sfeir-windev-agents-rea-clean-room-2026-10-15]].

## RésuméDe400mots

L'article de SFEIR explique comment relire la sortie de REA, un outil qui fait piloter des décompilateurs et des analyseurs par un agent de code. Il part d'un test public mené le 11 octobre 2026 sur une application Electron de 100 Mo : la sortie comptait 744 limitations explicites et annonçait zéro script preload alors que le code en chargeait deux. La première information signale ce que l'outil n'a pas pu établir ; la seconde est une erreur non signalée. La relecture doit séparer ces deux cas.

D'après son dépôt, REA associe chaque conclusion à ses preuves, ses limitations et sa localisation dans l'artefact, et prévient que la décompilation et l'analyse assistée par IA peuvent être incomplètes ou fausses. L'article situe l'essentiel des erreurs entre l'outil et le lecteur : l'agent résume, relie et explique les faits renvoyés.

La méthode proposée, présentée comme celle du cabinet, classe chaque affirmation en trois états. Une affirmation vue pointe vers un fichier, un décalage ou une chaîne vérifiable. Une affirmation inférée est déduite d'un motif ou d'un nom, souvent juste mais jamais prouvée. Une affirmation inconnue correspond à un élément que l'outil n'a pas résolu. La règle : une inférence ne doit jamais apparaître dans un rapport comme un constat vu. Les inconnues sont décrites comme la partie la plus fiable, puisque l'outil refuse d'y conclure à l'absence ; l'analyse de Slack par Connor Turland en compte 43 004, à côté d'une découverte exacte.

Deux pièges sont détaillés. Le premier consiste à prendre un comptage pour une preuve de complétude : des comptages justes côtoient un zéro faux, causé selon l'auteur du test par un chemin construit à l'exécution. Le second consiste à croire que le code plausible est celui qui s'exécute : Aayush Tyagi, analysant le quick switcher d'Obsidian, a vérifié l'héritage d'une classe minifiée, écrit une prédiction testable avant l'analyse et confronté le résultat à 24 classements relevés à la main, pour un coût de 1,83 dollar.

L'article conclut qu'une sortie REA est une hypothèse documentée, qui devient utile lorsqu'elle est convertie en tests de non-régression par golden master : chaque règle vue devient un cas de test, chaque règle inférée doit être confirmée par le métier. La FAQ résume la validation : recouper avec grep ou le décompilateur, écrire une prédiction, puis tester sur l'application d'origine.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Lire une sortie REA : preuves, pseudocode et hallucinations | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | a_créé | revue en trois états (vu, inféré, inconnu) | METHODOLOGIE | 0.92 | STATIQUE | déclaré_article |
| revue en trois états (vu, inféré, inconnu) | METHODOLOGIE | s_applique_à | REA | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | ne jamais faire remonter une affirmation inférée comme une affirmation vue | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les erreurs de lecture naissent presque toujours dans l'interprétation par l'agent | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | affirme_que | la décompilation et l'analyse assistée par IA peuvent être incomplètes ou fausses | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Ishank Choudhary | PERSONNE | mesure | 744 limitations explicites et zéro preload annoncé pour deux réels | MESURE | 0.9 | STATIQUE | déclaré_article |
| Connor Turland | PERSONNE | mesure | 43 004 éléments inconnus sur Slack 4.52.171 | MESURE | 0.88 | STATIQUE | déclaré_article |
| Aayush Tyagi | PERSONNE | affirme_que | Finding plausible-looking scoring code and assuming it is the code that runs is the classic failure mode here | CITATION | 0.9 | STATIQUE | déclaré_article |
| Aayush Tyagi | PERSONNE | recommande | écrire une prédiction testable avant de lancer l'agent | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| Aayush Tyagi | PERSONNE | mesure | 7 min 8 s de travail actif pour 1,83 $ sur le quick switcher d'Obsidian | MESURE | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | vérifier à la main tout zéro dans un comptage REA | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| golden master | METHODOLOGIE | permet | transformer une sortie REA en tests de non-régression | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle, éditeur de sfeir.com | AJOUT |
| REA | TECHNOLOGIE | catégorie | outil open source de rétro-ingénierie par agents (morluto/rea) | AJOUT |
| revue en trois états (vu, inféré, inconnu) | METHODOLOGIE | règle | Une affirmation inférée ne remonte jamais comme vue ; un zéro se vérifie à la main | AJOUT |
| golden master | METHODOLOGIE | usage | Règle vue → cas de test ; règle inférée → confirmation métier | AJOUT |
| Ishank Choudhary | PERSONNE | support | Auteur d'un test public de REA sur HackerNoon (14 octobre 2026) | AJOUT |
| Connor Turland | PERSONNE | support | Cyrus ; analyse de Slack 4.52.171 avec REA (20 octobre 2026) | AJOUT |
| Aayush Tyagi | PERSONNE | support | Analytics Vidhya ; analyse d'Obsidian 1.14.4 avec REA (18 octobre 2026) | AJOUT |
