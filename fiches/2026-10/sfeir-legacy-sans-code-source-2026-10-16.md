---
themes: [architecture-construction, qualite-securite, transformation-adoption]
source: SFEIR
---
# sfeir-legacy-sans-code-source-2026-10-16

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **16 octobre 2026** (mis à jour le 23 octobre, ~6 500 signes, quatre sources notées). Il pose la question d'une DSI qui porte une application critique dont le **code source est perdu** : peut-on comprendre le binaire assez bien pour le réécrire ? Point d'entrée : **REA**, serveur MCP créé le **14 avril 2026** par le compte **morluto**, à **369 860 étoiles** au 23 octobre. Quatre apports. **(1)** Le point de départ réaliste : un exécutable, une base et des utilisateurs ; l'objectif n'est pas de ressusciter le code mais de **rétro-documenter** les règles métier. **(2)** Ce que les agents changent : REA orchestre **Ghidra**, Hopper ou IDA et rend pseudocode, assembleur et preuves ; *« le coût de la première lecture d'un binaire s'effondre »*, mais la couverture reste partielle (zéro preload annoncé pour deux réels). **(3)** Une méthode en quatre temps reprise du cluster WinDev, où seule la première étape change : rétro-documenter depuis binaire, écrans et données ; faire relire par les utilisateurs ; faire de l'ancien binaire l'oracle d'un **golden master** ; réécrire brique par brique. **(4)** Confinement (*« This is not a sandbox »*) et trois régimes du droit européen (observation, correction d'erreurs, interopérabilité, article **L122-6-1**). Article pivot qui relie la série REA et la série migration WinDev de SFEIR.

## Titre Article

Applications legacy sans code source : comprendre avant de réécrire

## Date

2026-10-16

## URL

https://www.sfeir.com/articles/legacy-sans-code-source/

## Keywords

legacy, code source perdu, application sans code source, rétro-documentation, rétro-ingénierie, REA, Reverse Engineer Anything, MCP, Ghidra, Hopper, IDA, décompilation, pseudocode, .NET, Electron, golden master, oracle de test, réécriture brique par brique, modernisation legacy, WinDev, Visual Basic 6, Delphi, PowerBuilder, confinement, sandbox, droit européen, L122-6-1, interopérabilité, arrêt Top System, Software Factory

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé individuellement, publié sur sfeir.com.

## Ton

Profil : article de cadrage d'une ESN, registre posé et pragmatique, en français, adressé à la deuxième personne aux DSI qui portent une application critique sans source. Le texte s'ouvre sur un fait daté et chiffré (création du dépôt REA, nombre d'étoiles) puis ramène immédiatement les attentes à un objectif « plus modeste et plus utile » : documenter le comportement, pas retrouver le code. Il alterne ce qui change (le coût de la première lecture) et ce qui ne change pas (couverture partielle, validation par les utilisateurs, preuve par golden master), avec un exemple chiffré de faux zéro. L'article fonctionne comme une page pivot : il renvoie à de nombreux articles de la série pour chaque stack (VB6, Delphi, PowerBuilder, WinDev) et chaque sujet (confinement, droit). La partie juridique est précise (articles, directive, arrêt) mais se termine par un renvoi au juriste. La FAQ répond sans promesse (« rarement », « aucune automatique »). Clôture sur la rétro-documentation comme premier livrable de la Software Factory SFEIR.

## Pense-betes

- **REA** : serveur MCP créé le **14 avril 2026** par le compte GitHub **morluto** ; **369 860 étoiles** au 23 octobre 2026.
- **Point de départ** : exécutable + base de données + utilisateurs qui connaissent le comportement. Un compilateur jette noms, commentaires et une bonne part de la structure → on ne ressuscite pas le source.
- **Objectif** : rétro-documenter les règles métier assez précisément pour une réimplémentation sur stack moderne, puis **prouver** l'équivalence de comportement.
- **Avant les agents** : expert du désassemblage, semaines de lecture, budget rarement accordé pour une application « qui marche » → parcs vieillis en l'état.
- **Ce que REA change** : il ne décompile pas lui-même, il **orchestre** Hopper, Ghidra ou IDA (natif) et lit sans exécuter les applications .NET et JavaScript/Electron ; pseudocode, assembleur, chaînes, symboles, références, avec preuves et limites. Première lecture : de jours de spécialiste à une session d'agent supervisée.
- **Ce qui ne change pas** : couverture partielle (REA 6.4.0, 11 octobre : zéro preload annoncé, deux réels) → garder visibles les inconnues déclarées.
- **Méthode en quatre temps** (cluster WinDev, seule l'étape 1 change sans source) : (1) rétro-documenter depuis exécutable, écrans, données ; (2) relecture par les utilisateurs ; (3) l'ancien binaire comme **oracle** du golden master ; (4) réécriture brique par brique validée contre l'oracle.
- **Confinement** : SECURITY.md de REA — *« This is not a sandbox »* ; application interne connue → analyse statique sur poste acceptable ; origine incertaine → VM ou conteneur jetable.
- **Trois régimes juridiques** (UE / CPI) : observation et test pendant une utilisation autorisée (III de L122-6-1, sans décompiler) ; correction d'erreurs par l'acquéreur légitime (article 5 de la directive, arrêt Top System, I) ; interopérabilité sous trois conditions (IV). Vérifier la cession écrite des droits d'un prestataire.
- **FAQ** : source rarement retrouvable (p-code VB et PowerBuilder conservent davantage) ; première lecture en heures, l'essentiel du temps va à la validation et au golden master ; il faut en interne au moins une personne capable de vérifier l'agent.

## RésuméDe400mots

L'article de SFEIR s'adresse aux directions informatiques qui exploitent une application critique dont le code source est perdu, incomplet ou illisible. Il part de l'apparition de REA (Reverse Engineer Anything), un serveur MCP créé en avril 2026 qui donne à un agent de code les outils d'un rétro-ingénieur et dont le dépôt dépassait 369 000 étoiles six mois plus tard. La question devient concrète : peut-on comprendre ce binaire assez bien pour le réécrire ?

Le point de départ réaliste est un exécutable, une base de données et des utilisateurs qui connaissent le comportement de l'application. Le code d'origine ne sera pas reconstitué, un compilateur ayant supprimé noms, commentaires et une partie de la structure. L'objectif est de rétro-documenter les règles métier assez précisément pour les réimplémenter sur une stack moderne, puis de prouver que la nouvelle application se comporte comme l'ancienne. Ce travail existait avant les agents mais coûtait des semaines d'expertise, ce qui a laissé la plupart des parcs vieillir en l'état.

Les agents changent le coût de la première lecture. REA ne décompile pas lui-même : il orchestre Ghidra, Hopper ou IDA pour le code natif, lit les applications .NET ou Electron sans les exécuter, et rend pseudocode, assembleur, chaînes et références avec les preuves et limites de chaque conclusion. Ce qui demandait des jours tient dans une session supervisée. La couverture reste partielle : sur une application Electron, REA a annoncé zéro script preload alors qu'il y en avait deux. Les inconnues déclarées doivent rester visibles dans la documentation.

La méthode reprend celle de la série SFEIR sur la migration WinDev, où seule la première étape change en l'absence de source : rétro-documenter depuis le binaire, les écrans et les données, faire relire par les utilisateurs, capturer les sorties de l'ancienne application pour en faire l'oracle d'un golden master, puis réécrire brique par brique contre cet oracle. Des pages dédiées traitent VB6, Delphi, PowerBuilder, WinDev et les formats de données propriétaires.

L'article aborde enfin le confinement et le droit. REA n'isole rien, sa politique de sécurité l'écrit ; un exécutable d'origine incertaine s'ouvre dans une machine virtuelle. Le droit européen distingue trois régimes : l'observation pendant une utilisation autorisée, la correction d'erreurs par l'acquéreur légitime, et la décompilation à fin d'interopérabilité sous conditions. Il faut aussi vérifier la cession des droits d'un prestataire. La FAQ précise qu'aucune complétude n'est garantie et qu'une personne capable de vérifier l'agent reste indispensable.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Applications legacy sans code source | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| morluto | PERSONNE | a_créé | REA | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | mesure | 369 860 étoiles GitHub au 23 octobre 2026 | MESURE | 0.88 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | réduit | coût de la première lecture d'un binaire | CONCEPT | 0.86 | DYNAMIQUE | déclaré_article |
| rétro-documentation | METHODOLOGIE | s_applique_à | applications legacy sans code source | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| rétro-documentation | METHODOLOGIE | utilise | REA | TECHNOLOGIE | 0.86 | DYNAMIQUE | déclaré_article |
| rétro-documentation | METHODOLOGIE | utilise | golden master | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | sans source, l'objectif est de rétro-documenter les règles métier, pas de ressusciter le code | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | faire de l'ancien binaire l'oracle du golden master et réécrire brique par brique | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SECURITY.md de REA | DOCUMENT | affirme_que | This is not a sandbox | CITATION | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | ouvrir tout exécutable d'origine incertaine dans une machine virtuelle ou un conteneur jetable | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| article L122-6-1 | DOCUMENT | s_applique_à | décompilation | CONCEPT | 0.86 | DYNAMIQUE | déclaré_article |
| Applications legacy sans code source | DOCUMENT | référence | Ishank Choudhary | PERSONNE | 0.82 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| REA | TECHNOLOGIE | catégorie | Serveur MCP de rétro-ingénierie orchestrant Ghidra, Hopper, IDA ; dépôt morluto/rea créé le 14 avril 2026 | AJOUT |
| morluto | PERSONNE | rôle | Compte GitHub créateur du dépôt REA | AJOUT |
| rétro-documentation | METHODOLOGIE | définition | Reconstituer les règles métier d'un existant (code ou binaire) en spécification vérifiable | AJOUT |
| golden master | METHODOLOGIE | rôle | Sorties de l'application d'origine servant d'oracle aux tests de la réécriture | AJOUT |
| article L122-6-1 | DOCUMENT | contenu | Code de la propriété intellectuelle : observation (III), correction d'erreurs (I), interopérabilité (IV) | AJOUT |
| SECURITY.md de REA | DOCUMENT | contenu | Politique de sécurité de REA, section « Security boundary » | AJOUT |
