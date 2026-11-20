---
themes: [outils-plateformes, architecture-construction]
source: SFEIR
---
# sfeir-rea-dotnet-2026-10-17

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **17 octobre 2026** (~900 mots, quatre sources, toutes issues du dépôt `morluto/rea`), fiche technique du cluster SFEIR sur la rétro-ingénierie par agents. Point de départ : dans le tableau des cibles de **REA**, la ligne « .NET assemblies » ne demande rien d'autre que *« None (static only) »*. Trois apports. **(A)** Ce que REA lit : métadonnées, instructions **CIL**, dépendances natives déclarées et comparaisons de builds, par un parseur PE/CLI maison ; aucune assembly n'est chargée, *« le CLR ne démarre jamais »*. **(B)** Ce qu'il ne fait pas : pas d'émission de **C#**, pas d'extraction des exécutables single-file, pas de décodage IL2CPP ; **NativeAOT** relève de l'analyse native, avec un parseur limité aux cibles x64 et métadonnées RTR 9.1 (.NET 8), les corps de méthode passant par **Ghidra**. **(C)** L'usage visé : un patrimoine **.NET Framework** dont le dépôt ne correspond plus aux binaires en production — cartographier dépendances et appels natifs, comparer deux livraisons, alimenter une rétro-documentation. L'article borne l'intérêt : *« Sur trois assemblies, un décompilateur .NET ouvert à la main suffit »* ; REA sert sur un parc mixte. Recoupe la fiche SFEIR sur les limites de REA.

## Titre Article

Analyser des assemblies .NET avec REA

## Date

2026-10-17

## URL

https://www.sfeir.com/articles/rea-dotnet/

## Keywords

REA, .NET, .NET Framework, assembly, CIL, métadonnées, PE/CLI, CLR, analyse statique, dépendances natives, comparaison de builds, NativeAOT, ReadyToRun, single-file, IL2CPP, Unity, Ghidra, décompilateur, C#, rétro-documentation, legacy sans code source, serveur MCP, décompilation, interopérabilité, arrêt Top System, golden master, Software Factory

## Authors

SFEIR AI (voix éditoriale du cabinet), article non signé individuellement — sfeir.com, site éditorial de SFEIR.

## Ton

Profil : fiche technique d'une ESN, en français, registre d'évaluation d'outil adressé aux DSI et équipes de modernisation qui portent un parc .NET ancien. Le texte part d'une citation du README et annonce qu'elle « mérite d'être lue de près ». La construction est symétrique : ce que l'outil lit, ce qu'il ne fait pas, ce que cela apporte, comment lire la sortie. Chaque capacité et chaque limite sont attribuées à la documentation du projet. Le ton est mesuré : il relativise la nouveauté (la lisibilité du CIL est « connue depuis vingt ans ») et situe le seuil d'utilité de l'outil. La distinction entre fait du binaire et intention déduite par l'agent est posée explicitement. FAQ en réponses courtes ; conclusion sur l'offre Software Factory.

## Pense-betes

- **Exigence REA pour .NET** : *« None (static only) »* — aucun moteur à installer, aucun runtime.
- **Sorties** : métadonnées, instructions **CIL**, dépendances natives déclarées, **comparaison de builds** ; parseur PE/CLI propre, aucune assembly chargée ni exécutée → utile pour une assembly de fournisseur inconnu.
- **Valeur** : la lisibilité du CIL (types, méthodes, signatures, références) est ancienne ; l'apport est de la **parcourir à l'échelle d'un parc** avec des résultats structurés interrogeables par l'agent.
- **Angles morts documentés** : pas de **C#** reconstruit ; pas d'extraction des **single-file** ; pas d'inférence NativeAOT depuis un PE ordinaire ; **IL2CPP** confié à un outil séparé (métadonnées Unity).
- **NativeAOT** : parseur en lecture seule pour **x64 PE + RTR 9.1 (.NET 8)** ; autres versions partielles ou non prises en charge ; corps de méthode via **Ghidra**.
- **Cas d'usage type** : application .NET Framework de ~15 ans, prestataire parti, dépôt désynchronisé de la production → dépendances entre assemblies, bibliothèques natives appelées, écarts entre livraisons (correctif livré sans commit).
- **Seuil** : 3 assemblies → décompilateur manuel ; parc mixte (.NET + natif + JavaScript) → un seul serveur MCP.
- **Lecture** : noms et appels = faits du binaire ; intention métier = hypothèse de l'agent → transformer les règles déduites en **tests de non-régression** avant réécriture.
- **Droit** : observer/tester ≠ décompiler ; décompilation = interopérabilité, correction d'erreurs (arrêt **Top System**) ou autorisation de l'éditeur.

## RésuméDe400mots

Cet article de SFEIR, publié le 17 octobre 2026, examine ce que l'outil de rétro-ingénierie REA permet sur des assemblies .NET. Il part d'une ligne du tableau des cibles de l'outil : pour les assemblies .NET, aucune exigence, l'analyse étant purement statique. L'article s'adresse aux DSI qui portent des dizaines d'applications .NET Framework dont plus personne ne maîtrise le code source.

Selon sa documentation, REA renvoie pour une assembly .NET ses métadonnées, ses instructions CIL, ses dépendances natives déclarées et des comparaisons entre builds. Il décode le format PE/CLI avec son propre parseur, sans charger ni exécuter l'assembly : le runtime .NET ne démarre jamais, ce qui compte quand le binaire provient d'un fournisseur inconnu. Le CIL conserve beaucoup d'information après compilation ; la nouveauté n'est pas cette lisibilité, connue depuis longtemps, mais la possibilité de la parcourir à l'échelle d'un parc avec des résultats structurés.

L'article détaille aussi les limites. REA ne reconstruit pas de C# ; il ne traite pas le contenu des exécutables single-file, ne décode pas IL2CPP et ne reconnaît pas NativeAOT dans un exécutable natif ordinaire. Pour NativeAOT, un parseur couvre les cibles x64 avec les métadonnées de .NET 8, et l'analyse des méthodes passe par Ghidra. La documentation du projet rappelle que toute décompilation assistée par IA peut être incomplète ou fausse.

Le cas d'usage type est une application métier écrite il y a une quinzaine d'années, maintenue par un prestataire parti, dont le dépôt ne correspond plus aux binaires en production. REA aide à savoir quelles assemblies dépendent de quoi, quelles bibliothèques natives sont appelées et ce qui a changé entre deux livraisons. Ces éléments alimentent une rétro-documentation, première étape d'une modernisation. L'outil devient intéressant sur un parc mixte, où la même session passe du .NET au natif ou au JavaScript ; sur quelques assemblies, un décompilateur classique suffit.

Une sortie REA reste une hypothèse documentée : noms de méthodes et appels sont des faits, l'intention métier déduite par l'agent ne l'est pas. L'article recommande de transformer les règles déduites en tests de non-régression avant toute réécriture, et rappelle que la décompilation est juridiquement encadrée, permise pour l'interopérabilité, la correction d'erreurs ou avec l'autorisation de l'éditeur.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Analyser des assemblies .NET avec REA | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | .NET | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | permet | analyse statique des métadonnées et du CIL sans exécution | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | permet | comparaison de builds | CONCEPT | 0.86 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | REA ne reconstruit pas de C# à partir d'une assembly .NET | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.86 | DYNAMIQUE | déclaré_article |
| NativeAOT | TECHNOLOGIE | fait_partie_de | .NET | TECHNOLOGIE | 0.85 | ATEMPOREL | inféré |
| SFEIR | ORGANISATION | affirme_que | le parseur NativeAOT de REA se limite aux cibles x64 avec métadonnées RTR 9.1 (.NET 8) | AFFIRMATION | 0.82 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | permet | rétro-documentation | METHODOLOGIE | 0.86 | ATEMPOREL | déclaré_article |
| rétro-documentation | METHODOLOGIE | s_applique_à | .NET Framework | TECHNOLOGIE | 0.84 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | sur trois assemblies un décompilateur .NET manuel suffit ; REA sert sur un parc mixte | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | transformer les règles déduites par l'agent en tests de non-régression avant réécriture | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | a_créé | Software Factory | METHODOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| Software Factory | METHODOLOGIE | utilise | golden master | METHODOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| REA | TECHNOLOGIE | couverture .NET | Métadonnées, CIL, dépendances natives, comparaison de builds ; pas de C#, pas de single-file | AJOUT |
| .NET | TECHNOLOGIE | catégorie | Plateforme de développement Microsoft (code managé CIL) | AJOUT |
| NativeAOT | TECHNOLOGIE | catégorie | Compilation anticipée de .NET en code natif | AJOUT |
| rétro-documentation | METHODOLOGIE | définition | Reconstitution de la documentation d'une application à partir de ses binaires | AJOUT |
| Software Factory | METHODOLOGIE | catégorie | Offre SFEIR de réécriture d'applications legacy sous tests de non-régression | AJOUT |
