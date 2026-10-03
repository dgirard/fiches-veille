---
themes: [agents-codage-ia-skills, transformation-adoption, strategie-frameworks, architecture-construction]
source: "YouTube"
---
# reyes-factory-building-machine-software-2026-09-22

## Veille

Conférence de **Eno Reyes** (cofondateur et CTO de **Factory**, dont les agents « droids » sont décrits en introduction comme utilisés par des centaines de milliers de développeurs et des entreprises telles que **Nvidia** et **MongoDB**, juste après une **série C de 150 millions de dollars**), publiée le **22 septembre 2026** sur la chaîne de **FirstMark Capital** (vidéo de 25 min 51 s, transcription d'environ 5 300 mots). Il présente la « software factory » comme une boucle de rétroaction pilotée par des agents, et le rôle des humains comme celui de stewards de cette usine.

**(A)** Le cycle de développement est une boucle : des signaux (demandes clients, bugs, télémétrie, concurrents) sont triés, transformés en plan, codés, validés, déployés et monitorés, ce qui produit de nouveaux signaux. **(B)** Trois principes : agnostique au modèle, souverain sur son déploiement et ses traces, couvrant tout le SDLC avec un **même agent sur toutes les surfaces**. **(C)** Le goulot n'est plus le modèle mais le **harnais**, puis l'**état de préparation de l'organisation** (*agent readiness*, **150+ signaux** chez Factory). **(D)** Les humains construisent *« the machine that builds the machine »* et cherchent leur *« Google metric »*, lien entre une métrique d'ingénierie et un résultat d'affaires.

Le propos s'appuie sur les produits de Factory (Droid, routeur de modèles, Agent Readiness, Missions) sans chiffre de résultat client. Rapproche la boucle agentique de bout en bout de [[mollick-agency-and-agents-twilight-factory-2026-08-31]].

## Titre Article

Building the Machine That Builds the Software | Eno Reyes, Co-Founder & CTO of Factory

## Date

2026-09-22

## URL

https://www.youtube.com/watch?v=NLsiZtleLe4

## Keywords

software factory, usine logicielle, Factory, Droid, agents de codage, boucle de rétroaction, SDLC, indépendance vis-à-vis du modèle, routeur de modèles, souveraineté, air gap, traces, gouvernance, identité d'agent, audit, harnais, agent readiness, validation déterministe, garde-fous, Google metric, allocation d'inférence, Missions, rôle des développeurs

## Authors

Eno Reyes — cofondateur et CTO de Factory ; conférence vidéo (FirstMark Capital).

## Ton

Profil : exposé de dirigeant technique d'un éditeur d'agents de codage, adressé à des responsables d'ingénierie et de DSI de grandes entreprises, en registre oral et démonstratif. Il commence par une rétrospective (2023 : autocomplétion « de lignes en paragraphes, fichiers, dépôts »), puis déroule des questions que posent les organisations (coûts de tokens, ROI, dépendance à un modèle, rôle des développeurs) avant de proposer son cadre. Les positions sont énoncées comme des principes (« you should… ») et illustrées par des pratiques internes de Factory. L'orateur présente certains choix comme ses propres opinions (« our take would be »), notamment sur l'identité des agents, et reconnaît les compromis : la souveraineté totale demande beaucoup d'effort et n'est pas adaptée à toute organisation.

## Pense-betes

- **Du codage à la boucle** : l'ère « coding agent » garde le modèle mental « j'appuie, j'obtiens le code ». Reyes constate que les développeurs passent la plupart de leur temps hors du code : revue (au sens large, pas seulement la pull request), tests manuels et QA, débogage, planification.
- **Boucle de signaux** : signaux (clients, bugs, télémétrie, concurrents) → tri par des humains (PM, EM) → plan → code → validation (test, QA, sécurité) → déploiement → monitoring → nouveaux signaux. La question n'est pas la faisabilité mais la **mesure, l'analytique et la gouvernance** : *« the problem is not technical. The problem is organizational »*.
- **Principe 1, agnostique au modèle** : un DSI n'a pas à parier sur un seul modèle ; la dépendance expose aux prix du fournisseur. Factory décrit un routeur qui alloue le modèle par tâche et par rôle (ex. chefs de produit et développeurs n'accèdent pas au même éventail), pour arbitrer coût et qualité de façon centralisée.
- **Principe 2, souveraineté** : déploiement au choix, du SaaS à l'air gap (« dans un sous-marin »). Les données les plus précieuses sont les **traces** : pour corriger une mauvaise priorisation, il faut savoir pourquoi l'usine l'a décidée. Reyes nuance : il s'agit d'une flexibilité à posséder, pas forcément à exercer.
- **Principe 3, tout le SDLC, un seul agent** : revue de code, sécurité continue, QA en boîte noire (web, CLI, API), documentation synchronisée, réponse aux incidents, déploiement progressif. Un agent unique évite de multiplier routeurs, politiques de coût et exports de traces. Construire en interne un agent CLI est jugé faisable ; le multi-surface (SDK, sandboxes) l'est beaucoup moins.
- **Gouvernance** : identité d'agent hiérarchique (organisation, équipe, projet, utilisateur, machine) ; héritage de l'identité de l'utilisateur pour l'activité synchrone, compte de service pour la revue de code en sandbox. Contrôles : listes d'autorisation, classification de risque, plafonds de dépense, et audit permettant de remonter en **une requête** de l'accès à une table jusqu'à la personne, au prompt et aux traces de raisonnement. L'indexation du code dans un cloud tiers est jugée non indispensable.
- **Goulot déplacé** : *« it hasn't been the LLM for a little bit »* ; le harnais devient bon, le nouveau frein est l'organisation (outils accessibles aux agents, validation déterministe : lint, tests, typage, conventions de fichiers imposées au commit).
- **Humains et métrique** : les humains passent de la construction du logiciel à celle de l'usine, en code classique et non en spécifications en langage naturel. Chaque entreprise doit trouver sa « Google metric » pour rendre l'allocation de tokens pilotable par le ROI (exemple : Missions, objectif de latence de 50 ms avec 2 milliards de tokens alloués).
- ⚠️ **Portée** : conférence d'un éditeur qui décrit ses propres produits ; aucune donnée mesurée sur des clients n'est donnée, et la session de questions n'a pas eu lieu faute de temps. Les chiffres cités (150+ signaux, 140 personnes à San Francisco, série C) sont déclaratifs.

## RésuméDe400mots

Eno Reyes, cofondateur et CTO de Factory, présente comment bâtir une « software factory », c'est-à-dire une organisation où des agents prennent en charge la boucle complète de développement logiciel. Il part d'une rétrospective : en 2023, on imaginait l'IA de code progresser de l'autocomplétion de lignes vers celle de fichiers, puis de dépôts. Les agents de codage sont arrivés, mais la plupart des usages restent « je demande, j'obtiens ». Selon lui, cette ère s'essouffle : les organisations posent maintenant des questions sur les dépassements de coûts, le retour sur investissement, la dépendance à un modèle et le rôle des développeurs, qui consacrent peu de temps au seul codage.

Il décrit le développement comme une boucle de rétroaction. Des signaux venus des clients, des bugs, de la télémétrie ou des concurrents sont triés, puis transformés en plan, en code, en validation et en déploiement, lequel produit de nouveaux signaux. Chaque étape peut être confiée à des agents. Pour Reyes, les vraies difficultés sont la mesure, l'analytique et la gouvernance : le problème est organisationnel plutôt que technique.

Trois principes structurent son cadre. D'abord l'indépendance vis-à-vis du modèle : un responsable informatique ne doit pas se lier à un seul fournisseur, ni subir ses prix. Un routeur de modèles permet d'allouer le calcul par tâche et par rôle. Ensuite la souveraineté : choisir son déploiement, du SaaS à l'air gap, et rester maître des traces, car corriger une mauvaise décision de l'usine suppose de comprendre pourquoi elle a été prise. Enfin la couverture de tout le cycle de vie, avec le même agent sur toutes les surfaces, afin d'éviter la dispersion des politiques, des routeurs et des exports de traces.

La gouvernance reste difficile : identité des agents (héritée de l'utilisateur pour l'interactif, compte de service pour la revue en sandbox), contrôle des modèles, listes d'autorisation, classification des risques, plafonds de dépense, et audit capable de remonter, en une requête, de l'accès à une table jusqu'à la personne, au prompt et aux traces. Il juge l'indexation du code dans un cloud inutile.

Le goulot, dit-il, n'est plus le modèle ni désormais le harnais, mais la préparation de l'organisation : outils utilisables par les agents et validation déterministe (lint, tests, typage, conventions). Factory propose un produit d'*agent readiness* mesurant plus de 150 signaux.

Les humains deviennent les stewards de l'usine : ils observent les dérives, corrigent le système et empêchent durablement les erreurs, en code plutôt qu'en spécifications. Reyes conclut que les entreprises devront trouver leur « Google metric », lien entre un indicateur d'ingénierie et un résultat d'affaires, pour allouer l'inférence selon le ROI, par exemple en confiant un objectif de performance à un agent avec un budget de tokens.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Eno Reyes | PERSONNE | travaille_chez | Factory | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Eno Reyes | PERSONNE | a_créé | Factory | ORGANISATION | 0.90 | STATIQUE | déclaré_article |
| Factory | ORGANISATION | publie | Droid | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Factory | ORGANISATION | publie | Agent Readiness | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Factory | ORGANISATION | publie | Missions | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Factory | ORGANISATION | mesure | série C de 150 millions de dollars | MESURE | 0.88 | STATIQUE | déclaré_article |
| Eno Reyes | PERSONNE | recommande | construire la software factory indépendante du modèle | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Eno Reyes | PERSONNE | recommande | rester souverain sur le déploiement et les traces de la software factory | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Eno Reyes | PERSONNE | recommande | un même agent sur toutes les surfaces du SDLC | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Eno Reyes | PERSONNE | affirme_que | le goulot est désormais l'état de préparation de l'organisation plutôt que le modèle | AFFIRMATION | 0.90 | DYNAMIQUE | déclaré_article |
| Eno Reyes | PERSONNE | affirme_que | le problème de la software factory est organisationnel et non technique | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Software factory | METHODOLOGIE | utilise | boucle de rétroaction | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Droid | TECHNOLOGIE | utilise | routeur de modèles | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| routeur de modèles | TECHNOLOGIE | réduit | dépendance à un fournisseur de modèle | CONCEPT | 0.85 | ATEMPOREL | inféré |
| Agent Readiness | TECHNOLOGIE | mesure | plus de 150 signaux de la base de code | MESURE | 0.90 | DYNAMIQUE | déclaré_article |
| validation déterministe | CONCEPT | améliore | fiabilité des agents | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Eno Reyes | PERSONNE | prédit | les meilleures entreprises seront celles qui trouvent leur Google metric | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| Google metric | CONCEPT | permet | allocation d'inférence guidée par le ROI | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| Missions | TECHNOLOGIE | s_applique_à | objectifs de performance de long terme | CONCEPT | 0.82 | DYNAMIQUE | déclaré_article |
| Eno Reyes | PERSONNE | affirme_que | les humains deviennent les stewards de l'usine logicielle | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Eno Reyes | PERSONNE | rôle | Cofondateur et CTO de Factory | AJOUT |
| Factory | ORGANISATION | secteur | Agents de codage autonomes ; série C de 150 millions de dollars | AJOUT |
| Droid | TECHNOLOGIE | catégorie | Agent de codage de Factory, multi-surface (terminal, revue, sandbox) | AJOUT |
| Agent Readiness | TECHNOLOGIE | catégorie | Produit Factory évaluant la préparation d'une base de code aux agents (150+ signaux) | AJOUT |
| Missions | TECHNOLOGIE | catégorie | Produit Factory d'objectifs de long terme avec budget de tokens alloué | AJOUT |
| Software factory | METHODOLOGIE | définition | Boucle de développement logiciel de bout en bout pilotée par des agents, humains en stewards | AJOUT |
| boucle de rétroaction | CONCEPT | définition | Signaux, tri, plan, code, validation, déploiement, monitoring, nouveaux signaux | AJOUT |
| routeur de modèles | TECHNOLOGIE | catégorie | Allocation du modèle par tâche et par rôle pour arbitrer coût et qualité | AJOUT |
| validation déterministe | CONCEPT | définition | Lint, tests, typage et conventions imposées comme boucles de rétroaction des agents | AJOUT |
| Google metric | CONCEPT | définition | Lien entre une métrique d'ingénierie et un résultat d'affaires mesurable | AJOUT |
