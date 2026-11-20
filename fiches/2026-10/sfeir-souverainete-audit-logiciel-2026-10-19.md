---
themes: [politique-regulation, qualite-securite]
source: SFEIR
---
# sfeir-souverainete-audit-logiciel-2026-10-19

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **19 octobre 2026** (~1 200 mots, trois sources tirées du dépôt **REA**, encadré « ceci n'est pas un conseil juridique »). Destiné aux acheteurs publics, opérateurs d'importance vitale et administrations, il traite l'audit du comportement d'un logiciel extra-européen sans son code source. **(A) Enjeu** : lois extraterritoriales (le **CLOUD Act** de 2018 en exemple), serveurs destinataires, télémétrie, mises à jour, accès distant. **(B) Apport de l'agent** : REA cartographie le comportement observable (binaire natif via Ghidra, Hopper ou IDA ; JavaScript/Electron ; APK ; sites web) ; le statique dit ce que le logiciel *peut* faire, la capture réseau en environnement isolé ce qu'il *fait*. **(C) Ne pas créer la fuite en auditant** : selon la FAQ de REA, les résultats d'outils partent chez le fournisseur du modèle ; pour un logiciel sensible, un modèle local (exemple d'**Aikido** en réseau coupé sur quatre H200). **(D) Limites** : l'audit *« vérifie ; il ne garantit pas »*. **(E) Cadre** : le III de l'article **L122-6-1 CPI** autorise l'observation ; la décompilation relève de l'interopérabilité ou de l'arrêt Top System. Rejoint [[sfeir-rapport-kill-switch-souverainete-2026-07-24]] sur la souveraineté.

## Titre Article

Souveraineté : auditer le comportement d'un logiciel extra-européen

## Date

2026-10-19

## URL

https://www.sfeir.com/articles/souverainete-audit-logiciel/

## Keywords

souveraineté numérique, logiciel extra-européen, audit de comportement, lois extraterritoriales, CLOUD Act, RGPD, opérateur d'importance vitale, OIV, acheteur public, marché public, télémétrie, mises à jour automatiques, REA, rétro-ingénierie par agents, capture réseau, analyse statique, modèle local, open weights, air gap, Aikido, article L122-6-1, observation, décompilation, interopérabilité, Top System, AI Cyber

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

Article de cadrage en français, à destination des décideurs publics et des responsables sécurité d'organisations sensibles. Le texte part d'une nuance tirée de la FAQ de REA (« Does REA upload my app? ») et la déploie en enjeu de souveraineté. Le registre est mesuré : chaque capacité est assortie de sa limite (« Elle vérifie ; elle ne garantit pas »), la décompilation est encadrée par le droit et renvoyée au juriste, et une section entière décrit ce que l'analyse ne couvre pas (traitement des données côté serveur de l'éditeur, accès, hébergement, exposition juridique). Les références sont courtes et proviennent du dépôt REA ; le cadre légal est cité par article et alinéa. FAQ finale et renvoi à l'offre AI Cyber de SFEIR (modèles exécutés chez le client ou chez un hébergeur souverain).

## Pense-betes

- **Enjeu** : un logiciel édité hors d'Europe peut relever de lois extraterritoriales (**CLOUD Act**, 2018) ; questions opérationnelles : serveurs destinataires, télémétrie, canaux de mise à jour, accès distant ; poids dans la décision d'achat d'un OIV, d'une administration, d'un acheteur public.
- **Ce que REA cartographie** : natif via Ghidra, Hopper, IDA (chaînes, symboles, références) ; JavaScript/Electron (modules, routes, canaux IPC) ; Android (manifeste, classes décompilées) ; site web (structure, scripts, observations réseau). Recherche : domaines contactés, télémétrie, bibliothèques embarquées, mises à jour automatiques.
- **Statique vs dynamique** : le statique montre ce que le logiciel *peut* faire ; la capture réseau en environnement isolé montre ce qu'il *fait*. Chaque constat est localisé dans le fichier.
- **Ne pas créer la fuite** : REA analyse localement, mais l'agent envoie les résultats d'outils (pseudocode, chaînes, extraits) au fournisseur du modèle → **modèle exécuté chez soi** pour un logiciel sensible. Exemple : Aikido Security, septembre 2026, modèle de sécurité open weights en réseau coupé sur **quatre GPU H200**.
- **Confinement du binaire** : REA n'est pas un bac à sable ; l'analyse s'exécute avec les permissions de l'utilisateur.
- **Limites** : rien sur ce que l'éditeur fait des données sur ses serveurs ni sur qui y accède ; ne remplace ni clause de localisation, ni hébergement qualifié, ni évaluation juridique. DISCLAIMER de REA : l'analyse assistée par IA *« may be incomplete or incorrect »*.
- **Cadre juridique** : III de l'article **L122-6-1 CPI** (non écartable par contrat) = observer, étudier, tester lors d'une utilisation autorisée ; décompilation limitée à l'interopérabilité (IV) ou à la correction d'erreurs (Top System) → audit fondé d'abord sur l'observation ; décompiler pour auditer demande en principe l'accord de l'éditeur (clause d'audit négociée au marché).

## RésuméDe400mots

L'article s'adresse aux acheteurs publics, aux opérateurs d'importance vitale et aux administrations qui veulent savoir ce qu'un logiciel édité hors d'Europe fait de leurs données. Il part de la FAQ de REA, outil de rétro-ingénierie par agents très suivi en octobre 2026 : l'outil analyse les cibles localement, mais l'agent reçoit les résultats d'outils, et le fournisseur du modèle applique sa propre politique de données. Toute la difficulté d'un audit de souveraineté est là : comprendre un programme sans créer soi-même une nouvelle fuite.

L'enjeu tient aux lois à portée extraterritoriale, le CLOUD Act américain de 2018 étant l'exemple le plus cité. Au-delà du RGPD, les questions deviennent opérationnelles : vers quels serveurs partent les données, quels canaux de télémétrie et de mise à jour existent, un accès distant est-il possible.

Sans code source, un agent équipé de REA cartographie le comportement observable : pour un binaire natif, il pilote Ghidra, Hopper ou IDA ; pour une application JavaScript ou Electron, il relève modules, routes et canaux IPC ; pour Android, le manifeste et les classes ; pour un site, la structure, les scripts et le réseau. On y cherche domaines contactés, télémétrie, bibliothèques embarquées et mécanismes de mise à jour. Le statique montre ce que le logiciel peut faire ; une capture réseau en environnement isolé montre ce qu'il fait.

Pour ne pas créer la fuite en auditant, l'article recommande un modèle exécuté chez soi dès que le logiciel ou le code est sensible, en citant l'exemple d'Aikido Security, qui a fait tourner un modèle de sécurité open weights en réseau coupé sur quatre GPU H200. Le binaire analysé doit lui aussi être confiné, REA n'étant pas un bac à sable.

Les limites sont assumées : l'analyse ne dit rien du traitement des données sur les serveurs de l'éditeur ni des accès, et ne remplace ni clause contractuelle de localisation, ni hébergement qualifié, ni évaluation juridique. Elle vérifie sans garantir.

Pour l'acheteur public, l'audit nourrit l'analyse du besoin et les vérifications préalables. Le III de l'article L122-6-1 du Code de la propriété intellectuelle, non écartable par contrat, autorise l'utilisateur légitime à observer, étudier et tester le logiciel ; la décompilation n'est prévue que pour l'interopérabilité ou, selon l'arrêt Top System, la correction d'erreurs. Un audit de souveraineté s'appuie donc d'abord sur l'observation, et une décompilation demande en principe l'accord de l'éditeur, par exemple via une clause d'audit négociée.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Souveraineté : auditer le comportement d'un logiciel extra-européen | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| audit de comportement logiciel | METHODOLOGIE | s_applique_à | souveraineté numérique | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| audit de comportement logiciel | METHODOLOGIE | utilise | REA | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| audit de comportement logiciel | METHODOLOGIE | utilise | capture réseau | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Cloud Act | CONCEPT | s_applique_à | logiciel extra-européen | CONCEPT | 0.82 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | l'analyse statique montre ce que le logiciel peut faire, la capture réseau ce qu'il fait | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | avec un modèle hébergé, les résultats d'outils partent chez le fournisseur du modèle | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | auditer un logiciel sensible avec un modèle exécuté chez soi | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Aikido Security | ORGANISATION | mesure | modèle de sécurité open weights en réseau coupé sur quatre GPU H200 | MESURE | 0.82 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | l'audit vérifie le comportement, il ne garantit pas la souveraineté | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | permet | observation et étude du fonctionnement par l'utilisateur légitime | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| arrêt Top System | DOCUMENT | affine | article L122-6-1 du CPI | DOCUMENT | 0.8 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | négocier une clause d'audit au marché pour décompiler | AFFIRMATION | 0.82 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| audit de comportement logiciel | METHODOLOGIE | définition | cartographie statique + capture réseau d'une exécution autorisée en environnement isolé | AJOUT |
| REA | TECHNOLOGIE | catégorie | outil open source de rétro-ingénierie par agents (morluto/rea) | AJOUT |
| Cloud Act | CONCEPT | portée | loi américaine extraterritoriale de 2018 | AJOUT |
| article L122-6-1 du CPI | DOCUMENT | contenu | exceptions au droit d'auteur logiciel : observation (III, non écartable), interopérabilité (IV) | AJOUT |
| Aikido Security | ORGANISATION | apport | modèle de sécurité open weights déployé en air gap (septembre 2026) | AJOUT |
| capture réseau | METHODOLOGIE | rôle | observer le trafic sortant réel d'une exécution autorisée | AJOUT |
