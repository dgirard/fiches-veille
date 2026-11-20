---
themes: [qualite-securite, architecture-construction]
source: SFEIR
---
# sfeir-electron-asar-secrets-2026-10-21

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **21 octobre 2026** (~1 100 mots, quatre sources : README et documentation des fuses de **REA**, tests de Connor Turland et d'Ishank Choudhary). Il s'adresse aux éditeurs d'applications **Electron**. **(1) Le format** : `app.asar` est *« une concaténation de fichiers avec un index, sans chiffrement »*, conçu pour le packaging, jamais pour protéger ; REA le lit sans lancer l'application. Sur **Slack 4.52.171**, Turland obtient en **52 secondes** **529** fichiers JS, **1 904** modules, **45** canaux IPC et **8** add-ons natifs (JSON de 158 Mo) ; Choudhary vérifie sur une application de 100 Mo que les comptages concordent avec un grep sur le source. **(2) Ce qui s'expose** : clés d'API, identifiants de télémétrie en écriture, URL internes, drapeaux de fonctionnalités, règles non revalidées par le serveur ; une clé publiée doit être tenue pour compromise. **(3) Correctifs** : jetons courts, validation serveur, scan de secrets bloquant dans la chaîne de build. **(4) Fuses Electron** (`EnableEmbeddedAsarIntegrityValidation`, `OnlyLoadAppFromAsar`) : ils compliquent la modification, *« Ils ne protègent pas la lecture »*. Fait partie de la série SFEIR d'octobre 2026 sur la rétro-ingénierie par agents.

## Titre Article

Applications Electron : secrets et logique métier exposés dans l'ASAR

## Date

2026-10-21

## URL

https://www.sfeir.com/articles/electron-asar-secrets/

## Keywords

Electron, ASAR, app.asar, packaging, secrets embarqués, clés d'API, télémétrie, drapeaux de fonctionnalités, logique métier côté client, canaux IPC, add-ons natifs, REA, rétro-ingénierie par agents, Slack, jetons courts, validation côté serveur, scan de secrets, chaîne de build, révocation, fuses Electron, EnableEmbeddedAsarIntegrityValidation, OnlyLoadAppFromAsar, intégrité, minification, obfuscation, AI Cyber

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

Note technique en français, destinée aux éditeurs et équipes de développement d'applications Electron. Le registre est direct et opératoire : définition du format, tests publics chiffrés, inventaire des éléments à risque, correctifs à intégrer à la chaîne de build. Les distinctions sont nettes et formulées en phrases brèves (« Ils ne protègent pas la lecture », « Une chaîne reste une chaîne »). Les chiffres sont attribués à leurs auteurs et sources. L'article distingue l'audit de sa propre application, où l'analyse statique suffit, de l'analyse d'un binaire tiers, qui exige un environnement isolé. FAQ courte et renvoi à l'offre AI Cyber de SFEIR et au hub du dossier en conclusion.

## Pense-betes

- **ASAR** : archive `app.asar` = concaténation de fichiers + index, **sans chiffrement** ; format de packaging lu par le runtime sans extraction, jamais conçu pour protéger.
- **REA sur Electron** : modules, imports, source maps, routes, canaux IPC, add-ons natifs, sans lancer l'application ni moteur de décompilation.
- **Test Turland (20 octobre 2026)** : Slack **4.52.171**, **52 s**, **529** fichiers JS, **1 904** modules, **45** canaux IPC, **8** add-ons natifs, JSON de **158 Mo**.
- **Test Choudhary** : application de **100 Mo** ; comptages structurels (fenêtres, API exposées au renderer, gestionnaires IPC) concordants avec un grep sur le source.
- **Éléments exposés** : clés d'API tierces, identifiants de télémétrie avec droits d'écriture, URL d'environnements internes, drapeaux révélant la feuille de route, règles de validation ou de calcul non refaites côté serveur.
- **Clé publiée = compromise** : les anciennes versions restent installées et téléchargeables ; seule réponse, la **révocation**.
- **Correctifs** : jeton court, limité, révocable remis par le serveur, qui appelle lui-même les services tiers ; droits, quotas, tarification, licences vérifiés côté serveur à chaque requête ; **scan de secrets bloquant** sur l'archive produite avant publication.
- **Fuses Electron** : `EnableEmbeddedAsarIntegrityValidation`, `OnlyLoadAppFromAsar` ; REA lit leur état sans modifier le binaire ; à activer contre la modification, sans effet sur la lecture. Chez Turland, 8 binaires natifs ne correspondaient pas à leur empreinte (re-signature par l'outil de packaging) ; relance avec `--integrity-policy record-and-continue`.
- **Audit** : sa propre application = statique suffisant ; binaire tiers d'origine inconnue = environnement isolé.

## RésuméDe400mots

L'article explique pourquoi le code d'une application Electron est lisible par quiconque l'installe, et ce qu'un éditeur doit en tirer. Une application Electron range son code dans un fichier app.asar, que l'article décrit comme une concaténation de fichiers accompagnée d'un index, sans chiffrement. Le format sert au packaging : il regroupe JavaScript, HTML, CSS et ressources en une archive que le runtime lit sans extraction. Il n'a jamais eu pour objet de protéger le contenu.

Le README de REA, outil de rétro-ingénierie piloté par un agent, range Electron parmi les cibles lisibles sans moteur de décompilation : modules, imports, source maps, routes, canaux IPC et add-ons natifs, sans lancer l'application. Le 20 octobre 2026, Connor Turland a ainsi cartographié Slack 4.52.171 en 52 secondes : 529 fichiers JavaScript, 1 904 modules, 45 canaux IPC et 8 add-ons natifs, consignés dans un JSON de 158 Mo. Le test d'Ishank Choudhary sur une application de 100 Mo montre que les comptages structurels concordent avec un grep sur le source.

L'article invite chaque éditeur à inventorier son propre build. Les éléments problématiques reviennent d'un projet à l'autre : clés d'API de services tiers, identifiants de télémétrie avec droits d'écriture, URL d'environnements internes, drapeaux de fonctionnalités révélant la feuille de route, règles de validation ou de calcul que le serveur ne refait pas. La minification n'y change rien. Une clé présente dans une version publiée doit être tenue pour compromise, même retirée ensuite, car les anciennes versions restent installées ; la seule réponse est la révocation.

Les correctifs proposés sont architecturaux : aucun secret durable dans le client, un jeton court, limité et révocable remis par le serveur, qui appelle lui-même les services tiers avec la vraie clé ; vérification côté serveur des règles à valeur économique ou de sécurité ; scan de secrets sur l'archive produite, bloquant la publication.

Electron propose des fuses, interrupteurs gravés dans le binaire, dont l'un active la validation d'intégrité de l'archive et l'autre impose de ne charger le code que depuis app.asar. REA lit leur état sans modifier le binaire. Ils compliquent la modification de l'application installée, mais ne protègent pas la lecture : une archive dont l'intégrité est vérifiée reste lisible octet par octet. Pour sa propre application, l'analyse statique suffit ; pour un binaire tiers inconnu, l'analyse se fait en environnement isolé, REA n'étant pas un sandbox.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Applications Electron : secrets et logique métier exposés dans l'ASAR | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| ASAR | TECHNOLOGIE | fait_partie_de | Electron | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | l'archive ASAR est une concaténation de fichiers avec index, sans chiffrement | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | Electron | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Connor Turland | PERSONNE | mesure | Slack 4.52.171 cartographié en 52 secondes : 529 fichiers JS, 1 904 modules, 45 canaux IPC, 8 add-ons natifs | MESURE | 0.92 | STATIQUE | déclaré_article |
| Ishank Choudhary | PERSONNE | mesure | comptages structurels de REA concordants avec un grep sur le source d'une application de 100 Mo | MESURE | 0.86 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | une clé présente dans une version publiée doit être tenue pour compromise | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | remplacer les secrets du client par des jetons courts émis par le serveur | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| scan de secrets | METHODOLOGIE | réduit | publication de secrets dans l'archive ASAR | CONCEPT | 0.84 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | ajouter un scan de secrets bloquant à la chaîne de build | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| fuses Electron | TECHNOLOGIE | fait_partie_de | Electron | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| fuses Electron | TECHNOLOGIE | réduit | modification de l'application installée | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la validation d'intégrité de l'ASAR ne protège pas la lecture | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | utilise | fuses Electron | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| obfuscation | CONCEPT | réduit | lisibilité du code pour un humain | CONCEPT | 0.75 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| ASAR | TECHNOLOGIE | définition | format d'archive de packaging d'Electron (app.asar), non chiffré | AJOUT |
| Electron | TECHNOLOGIE | catégorie | framework d'applications de bureau JavaScript | AJOUT |
| fuses Electron | TECHNOLOGIE | exemples | EnableEmbeddedAsarIntegrityValidation, OnlyLoadAppFromAsar | AJOUT |
| scan de secrets | METHODOLOGIE | rôle | détecter les motifs de secrets dans l'archive produite et bloquer la publication | AJOUT |
| Connor Turland | PERSONNE | apport | test de REA sur Slack 4.52.171 (20 octobre 2026) | AJOUT |
| REA | TECHNOLOGIE | catégorie | outil open source de rétro-ingénierie par agents (morluto/rea) | AJOUT |
