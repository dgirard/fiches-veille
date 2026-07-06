---
themes: [agents-codage-ia-skills]
source: "The Batch (Andrew Ng)"
---
# ng-thebatch-359-3-product-development-loops-2026-06-26

## Veille

Lettre « Dear friends » d'Andrew Ng dans *The Batch* (DeepLearning.AI, n°359) sur le **loop engineering** appliqué au développement produit **0-to-1**. Ng partage ses **3 boucles clés** — boucle de codage agentique (~minutes), boucle de feedback développeur (~heures), boucle de feedback externe (~jours) — imbriquées par échelle de temps croissante, reliant *coding agent → product spec/evals → developer vision → external feedback*. Thèse centrale : les humains conservent un **avantage de contexte** (plutôt qu'un « goût ») qui rend le human-in-the-loop indispensable ; les ingénieurs endossent un rôle partiel de product management. Domaine : agents de codage, ingénierie produit, méthodologie agentique.

## Titre Article

3 Key Product Development Loops (The Batch, Issue 359 — « Dear friends » letter)

## Date

2026-06-26

## URL

https://www.deeplearning.ai/the-batch/issue-359

## Keywords

Loop engineering, développement produit, boucle de codage agentique, boucle de feedback développeur, boucle de feedback externe, evals, product spec, vision produit, avantage de contexte, human-in-the-loop, taste, product management, agents de codage, 0-to-1

## Authors

Andrew Ng

## Ton

**Profil** : lettre personnelle à la première personne (« Dear friends… Keep building! Andrew »), registre chaleureux et pédagogique, adressée à une communauté de builders. Niveau technique accessible, appuyé sur un schéma unique (3 boucles concentriques, échelles ~minutes / ~heures / ~jours).

**Style** : didactique et encourageant, illustré par une **anecdote personnelle** filée (l'app pour apprendre à taper au clavier construite le week-end pour sa fille — costumes de chats à débloquer, flux de connexion parent, design visuel changé plusieurs fois). Ng procède par définitions cadrées puis exemples vécus, avec une nuance conceptuelle assumée : il **préfère « avantage de contexte » à « taste »** car cela « donne un chemin plus clair pour aider les systèmes d'IA à s'améliorer ». Autorité : figure de référence de l'IA (fondateur DeepLearning.AI, Coursera, Google Brain), qui parle en praticien (« over the weekend, I was building… »). Public cible : ingénieurs et builders adoptant les agents de codage et grandissant vers un rôle produit. Ton prospectif (« I will write more about how to do this in future letters »).

## Pense-betes

- « **Loop engineering** » est devenu une *buzzphrase* virale après les mentions de **Boris Cherny** (créateur de Claude Code) et **Peter Steinberger** (créateur d'OpenClaw) ; les boucles sont désormais clés pour faire itérer les agents longtemps sur du logiciel.
- Ng décrit **3 boucles imbriquées** qui guident *comment* il construit **et** *quoi* construire. Nœuds enchaînés : `coding agent → product spec/evals → developer vision → external feedback`.
- **Boucle 1 — codage agentique (~minutes)** : `coding agent ↔ product spec/evals`. Donné une spec (+ evals optionnelles), l'agent écrit du code, teste, itère jusqu'à ce que ce soit sans bug et conforme à la spec. « Fermer la boucle » a décollé **fin de l'an dernier** → *game changer* (agents productifs plus longtemps sans intervention). Exemple : l'agent a travaillé **~1 heure**, utilisant un navigateur pour vérifier son travail plusieurs fois, sans intervention. Tourne toutes les quelques minutes. **Domaine d'invention actif.**
- **Boucle 2 — feedback développeur (~dizaines de minutes à heures)** : `product spec/evals ↔ developer vision`. Le développeur examine le produit et **oriente** l'agent. L'an dernier, les devs faisaient la **QA** manuellement (trouver les bugs) ; comme les agents testent mieux leur propre code, ce temps a **fortement baissé** → on se concentre sur des **décisions produit de haut niveau** (features clés, UI). Traduire la vision en spec reste du travail ; **clarifier/mettre à jour la spec** après implémentation ; **construire des evals** quand un problème revient.
- **Avantage de contexte humain** : les équipes AI-native utilisent l'IA pour façonner la direction produit (données d'usage, synthèse de feedback client écrit/oral, analyse concurrentielle). Mais **les humains en savent plus** sur les utilisateurs et le contexte. Beaucoup appellent ça « **taste** » ; Ng préfère « **context advantage** ». **Non automatisable** : tant que l'humain sait quelque chose que l'IA ignore, le **human-in-the-loop** est nécessaire pour injecter cette connaissance.
- **Boucle 3 — feedback externe (~jours)** : `developer vision ↔ external feedback`. Tactiques : demander à des amis, alpha testeurs, mise en prod avec **A/B testing**. **Lentes** (rarement < heures, parfois jours/semaines). Ces données informent la **vision**, qui pilote la **spec**, qui pilote l'**agent**.
- **Convergence des rôles** : avec des agents qui accélèrent le dev, **de plus en plus d'ingénieurs jouent un rôle partiel de product management**. Le plus dur : **façonner la vision produit** et **équilibrer** construire (combler l'écart vision→spec) et récolter du feedback pour faire évoluer la vision. *« It is important to do both! »*
- Miroir encourageant : les ingénieurs s'élargissent vers le produit, comme les **PM et designers font désormais plus d'ingénierie**.
- **Distinction éditoriale** vs les autres fiches loop engineering : Ng recadre les boucles au niveau **produit** (imbrication + rôle humain), là où Lushbinary détaille le **harness technique** (briques, /goal, worktrees) et Saboo l'applique au **PM**.

## RésuméDe400mots

Dans cette lettre de *The Batch* (n°359), Andrew Ng prend acte de la viralité du terme « **loop engineering** » — popularisé par Boris Cherny (créateur de Claude Code) et Peter Steinberger (créateur d'OpenClaw) — et partage les **trois boucles clés** qui structurent sa façon de construire des produits **0-to-1**, mais aussi de décider *quoi* construire. Le schéma les présente imbriquées, par échelle de temps croissante, reliant quatre nœuds : *coding agent → product spec/evals → developer vision → external feedback*.

La **boucle de codage agentique** (~minutes) part d'une spécification produit et, optionnellement, d'un jeu d'**evals** : l'agent écrit du code, le teste et itère jusqu'à ce qu'il soit sans bug et conforme. Ng rappelle que « fermer la boucle » a décollé fin 2025 et change la donne — son agent a pu travailler environ une heure sur une app d'apprentissage du clavier pour sa fille, vérifiant lui-même son travail dans un navigateur, sans intervention. C'est un domaine d'invention très actif.

La **boucle de feedback développeur** (~dizaines de minutes à heures) voit le développeur examiner le produit et orienter l'agent. Comme les agents testent désormais bien mieux leur propre code, le temps passé en QA manuelle a fortement chuté, libérant le développeur pour des **décisions produit de plus haut niveau** (features, UI, parcours utilisateur). Traduire une vision en spec — puis la clarifier après une première implémentation, et bâtir des evals quand un problème récurrent apparaît — reste un vrai travail.

Ng insiste sur l'**avantage de contexte humain** : même si les équipes AI-native automatisent la collecte de données d'usage, la synthèse du feedback client et l'analyse concurrentielle, les humains en savent plus sur les utilisateurs et le contexte d'opération. Beaucoup nomment cela « taste » ; Ng préfère « avantage de contexte », car cela indique un chemin plus clair pour améliorer l'IA. Tant que l'humain sait quelque chose que l'IA ignore, le **human-in-the-loop** demeure nécessaire pour injecter cette connaissance.

La **boucle de feedback externe** (~jours) rassemble amis, alpha testeurs et A/B testing en production — des tactiques lentes dont les données nourrissent la vision, laquelle pilote la spec, laquelle pilote l'agent.

Ng conclut que, les agents accélérant le développement, de plus en plus d'ingénieurs endossent un rôle **partiel de product management**. Le plus difficile est de façonner la vision et d'équilibrer construction et feedback utilisateur — « il faut faire les deux ». Il y voit un signe encourageant : les ingénieurs s'élargissent vers le produit, comme PM et designers font désormais plus d'ingénierie.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Andrew Ng | PERSONNE | recommande | 3 boucles clés de développement produit 0-to-1 | METHODOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Boris Cherny | PERSONNE | a_créé | Claude Code | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Peter Steinberger | PERSONNE | a_créé | OpenClaw | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Loop engineering | METHODOLOGIE | observé_dans | réseaux sociaux (buzzphrase virale) | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Boucle de codage agentique | METHODOLOGIE | utilise | product specification et evals | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Boucle de codage agentique | METHODOLOGIE | permet | agent codant/testant/itérant sans intervention (~1 h) | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Boucle de feedback développeur | METHODOLOGIE | s_applique_à | orientation de l'agent par le développeur (~heures) | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Coding agent | TECHNOLOGIE | réduit | temps de QA manuelle du développeur | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Boucle de feedback externe | METHODOLOGIE | permet | retours d'alpha testers et A/B testing (~jours) | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| External feedback | CONCEPT | affine | developer vision | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Andrew Ng | PERSONNE | affirme_que | "les humains ont un avantage de contexte sur l'IA (préférable à 'taste')" | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Human-in-the-loop | METHODOLOGIE | résout | injection de connaissance que l'IA n'a pas | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Andrew Ng | PERSONNE | affirme_que | "de plus en plus d'ingénieurs jouent un rôle partiel de product management" | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Andrew Ng | PERSONNE | recommande | équilibrer construction (vision→spec) et feedback utilisateur | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Boucle de codage agentique | METHODOLOGIE | fait_partie_de | 3 boucles de développement produit | METHODOLOGIE | 0.92 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Andrew Ng | PERSONNE | rôle | Fondateur DeepLearning.AI ; auteur de la lettre The Batch n°359 | AJOUT |
| The Batch | DOCUMENT | éditeur | DeepLearning.AI (newsletter, issue 359) | AJOUT |
| Loop engineering | METHODOLOGIE | statut | Buzzphrase virale (mentions Cherny / Steinberger) | AJOUT |
| Boucle de codage agentique | METHODOLOGIE | échelle | ~minutes ; coding agent ↔ product spec/evals | AJOUT |
| Boucle de feedback développeur | METHODOLOGIE | échelle | ~heures ; product spec/evals ↔ developer vision | AJOUT |
| Boucle de feedback externe | METHODOLOGIE | échelle | ~jours ; developer vision ↔ external feedback | AJOUT |
| Evals | CONCEPT | définition | Jeu de données pour mesurer la performance de l'agent | AJOUT |
| Avantage de contexte | CONCEPT | définition | Les humains en savent plus que l'IA sur les utilisateurs/le contexte (préféré à « taste ») | AJOUT |
| Human-in-the-loop | METHODOLOGIE | justification | Nécessaire tant que l'humain sait ce que l'IA ignore | AJOUT |
| Boris Cherny | PERSONNE | rôle | Créateur de Claude Code | AJOUT |
| Peter Steinberger | PERSONNE | rôle | Créateur d'OpenClaw | AJOUT |
| App d'apprentissage du clavier | TECHNOLOGIE | contexte | Exemple 0-to-1 construit par Ng le week-end (pour sa fille) | AJOUT |
