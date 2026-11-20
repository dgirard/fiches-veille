---
themes: [qualite-securite, strategie-frameworks, politique-regulation]
source: SFEIR
---
# sfeir-editeurs-logiciel-lisible-agents-2026-10-21

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **21 octobre 2026** (~1 150 mots, cinq sources : README de **REA**, test de Connor Turland sur Slack, article L122-6-1 du CPI, arrêt SAS Institute de la CJUE, test d'Ishank Choudhary ; encadré « ceci n'est pas un conseil juridique »). Il s'adresse aux éditeurs de logiciels. Point de départ chiffré : le **20 octobre 2026**, **Connor Turland** a cartographié le client de bureau de **Slack** avec REA en **52 secondes** (**529** fichiers JavaScript, **1 904** modules, **45** canaux IPC, **8** add-ons natifs). **(1) Ce qu'un agent voit** : Electron, .NET, APK, natif. **(2) Ce qu'on ne peut plus cacher** : secrets embarqués, logique métier côté client, carte des appels réseau ; minification et compilation *« gênent peu les outils d'un agent »*. **(3) Où déplacer la valeur** : traiter le client comme public, jetons courts, validation côté serveur ; les actifs difficiles à copier sont les données, les utilisateurs, l'infrastructure, le support. **(4) Ce que le droit protège** : en France, certaines clauses anti-rétro-ingénierie sont nulles (L122-6-1) ; la CJUE (2012) exclut du droit d'auteur la fonctionnalité, le langage et le format de fichiers. Fait partie de la série SFEIR d'octobre 2026 sur la rétro-ingénierie par agents.

## Titre Article

Votre logiciel est lisible par n'importe quel agent : guide pour éditeurs

## Date

2026-10-21

## URL

https://www.sfeir.com/articles/editeurs-logiciel-lisible-agents/

## Keywords

éditeur de logiciel, rétro-ingénierie par agents, REA, Slack, Electron, .NET, APK, secrets côté client, clés d'API, jetons courts, logique métier côté serveur, client public, canaux IPC, minification, obfuscation, valeur côté serveur, avantage concurrentiel, licence logicielle, clause anti-rétro-ingénierie, article L122-6-1, CJUE SAS Institute, droit d'auteur, interopérabilité, clean-room, AI Cyber

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

Guide en français adressé directement aux éditeurs (« Si vous éditez un logiciel, partez de ce chiffre »). Le registre est prescriptif et concret : un chiffre d'ouverture tiré d'un test public, trois catégories d'exposition, des consignes d'architecture (client public, jetons courts, validation serveur), puis un volet juridique encadré par un avertissement explicite. Le texte reste mesuré sur les protections : l'obfuscation est gardée *« comme ralentisseur, sans en faire votre défense principale »*, la licence protège *« partiellement »*. Les références juridiques sont précises (article, arrêt, date). L'article recommande à l'éditeur de tester lui-même son produit avec ces outils et se clôt sur l'offre AI Cyber de SFEIR et un renvoi au hub du dossier.

## Pense-betes

- **Chiffre d'ouverture** : Connor Turland, 20 octobre 2026, client de bureau Slack cartographié par REA en **52 s** : **529** fichiers JS, **1 904** modules, **45** canaux IPC, **8** add-ons natifs ; logique d'un contrôle de notifications comprise en une dizaine de minutes.
- **Ce que REA renvoie** : Electron (modules, imports, source maps, routes, IPC, add-ons natifs, sans lancer l'app) ; .NET (métadonnées, CIL, dépendances natives) ; APK (manifeste, classes, méthodes) ; natif via Ghidra, Hopper, IDA (pseudocode, chaînes, symboles, appels). Le README assume l'usage : voir une fonctionnalité, demander comment elle marche, en construire une version.
- **Trois expositions** : **secrets embarqués** (clés, jetons, identifiants tiers) ; **logique métier côté client** (calculs, contrôles de droits, activation de fonctionnalités) ; **carte des appels réseau** (endpoints, formats, en-têtes).
- **Minification et obfuscation** : ralentissent un humain, gênent peu un agent ; test de Choudhary : l'analyseur de REA garde l'expression réelle d'un libellé de canal dans du JS minifié.
- **Déplacer la valeur** : client = public ; aucun secret durable ; jetons courts, émis à l'exécution, révocables ; droits, quotas, licences, calculs tarifés revalidés côté serveur ; logique différenciante derrière une API.
- **Actifs difficiles à copier** : données, utilisateurs, infrastructure, distribution, support, rythme de livraison, historique d'incidents.
- **Droit français** : L122-6-1 CPI rend nulles les clauses contraires à la copie de sauvegarde, à l'observation lors d'une utilisation autorisée et à la décompilation pour interopérabilité.
- **CJUE, 2 mai 2012, SAS Institute (C-406/10)** : fonctionnalité, langage et format de fichiers non protégés par le droit d'auteur ; réimplémenter un comportement ≠ recopier le code.

## RésuméDe400mots

L'article s'adresse aux éditeurs de logiciels et part d'un test public : le 20 octobre 2026, Connor Turland a cartographié le client de bureau de Slack avec REA, un outil de rétro-ingénierie piloté par un agent, en 52 secondes, obtenant 529 fichiers JavaScript, 1 904 modules, 45 canaux IPC et 8 add-ons natifs. Pour SFEIR, tout ce qu'un éditeur installe sur le poste de ses clients se lit désormais en une minute par quiconque dispose d'un agent de code.

Le README de REA décrit ce que l'outil renvoie : pour une application Electron, modules, imports, source maps, routes, canaux IPC et add-ons natifs, sans la lancer ; pour une assembly .NET, métadonnées et instructions CIL ; pour une APK, manifeste et classes ; pour un binaire natif, pseudocode et symboles via Ghidra, Hopper ou IDA. Turland dit avoir compris la logique d'un contrôle de notifications de Slack en une dizaine de minutes, et le README assume l'usage consistant à comprendre une fonctionnalité pour en construire une version.

Trois catégories passent ainsi du difficile à trouver au lisible en une session : les secrets embarqués, la logique métier exécutée côté client et la carte des appels réseau. Minification, empaquetage et compilation native ralentissent un humain mais gênent peu un agent, comme l'illustre un test sur du JavaScript minifié.

L'article recommande de traiter le client comme public : aucun secret durable dans le binaire, des jetons courts émis à l'exécution et révocables, une validation des droits, quotas, licences et calculs tarifés refaite côté serveur, et la logique différenciante placée derrière une API contrôlée. Les actifs qui se copient mal sont ailleurs : données, utilisateurs, infrastructure, distribution, qualité du support, rythme de livraison et historique d'incidents. L'éditeur est invité à tester lui-même son build avec ces outils, en tenant compte des licences des composants tiers embarqués.

Le volet juridique, assorti d'un avertissement, rappelle qu'en France l'article L122-6-1 du Code de la propriété intellectuelle rend nulles les clauses contraires à la copie de sauvegarde, à l'observation du fonctionnement lors d'une utilisation autorisée et à la décompilation nécessaire à l'interopérabilité. Le code et les assets restent protégés, mais la CJUE a jugé en 2012, dans l'affaire SAS Institute, que la fonctionnalité d'un programme, son langage et le format de ses fichiers ne relèvent pas du droit d'auteur. La FAQ conclut : garder l'obfuscation comme ralentisseur, tenir tout secret présent dans l'application pour exposé, et faire relire ses licences.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Votre logiciel est lisible par n'importe quel agent | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Connor Turland | PERSONNE | utilise | REA | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Connor Turland | PERSONNE | mesure | client Slack cartographié en 52 secondes : 529 fichiers JS, 1 904 modules, 45 canaux IPC, 8 add-ons natifs | MESURE | 0.92 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | Slack | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | Electron | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | minification, empaquetage et compilation native gênent peu les outils d'un agent | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | traiter le client comme public et ne livrer aucun secret durable dans le binaire | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| jetons courts révocables | CONCEPT | remplace | secrets embarqués côté client | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | revalider droits, quotas, licences et calculs tarifés côté serveur | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | données, utilisateurs, infrastructure, support et rythme de livraison se copient mal | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | affirme_que | les clauses contraires à l'observation et à la décompilation pour interopérabilité sont nulles | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| arrêt SAS Institute | DOCUMENT | affirme_que | la fonctionnalité, le langage et le format de fichiers d'un programme ne sont pas protégés par le droit d'auteur | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| CJUE | ORGANISATION | publie | arrêt SAS Institute | DOCUMENT | 0.92 | STATIQUE | déclaré_article |
| obfuscation | CONCEPT | réduit | lisibilité du code pour un humain | CONCEPT | 0.78 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | tester soi-même ce qu'un agent lit de son propre build | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| REA | TECHNOLOGIE | catégorie | outil open source de rétro-ingénierie par agents (morluto/rea) | AJOUT |
| Connor Turland | PERSONNE | apport | test de REA sur Slack (atcyrus.com, 20 octobre 2026) | AJOUT |
| Slack | TECHNOLOGIE | version testée | client de bureau Electron | AJOUT |
| jetons courts révocables | CONCEPT | définition | jetons émis à l'exécution par le serveur, limités et révocables, à la place des clés embarquées | AJOUT |
| arrêt SAS Institute | DOCUMENT | référence | CJUE, 2 mai 2012, C-406/10 | AJOUT |
| article L122-6-1 du CPI | DOCUMENT | contenu | exceptions d'ordre public : sauvegarde, observation, décompilation pour interopérabilité | AJOUT |
