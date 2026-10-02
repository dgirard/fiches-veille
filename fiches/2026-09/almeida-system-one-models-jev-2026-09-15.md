---
themes: [produits-services, outils-plateformes, architecture-construction]
source: "TypeSafe AI"
---
# almeida-system-one-models-jev-2026-09-15

## Veille

Annonce de **Diogo Almeida**, fondateur de **TypeSafe AI** (ancien d'OpenAI, où il a participé aux méthodes d'entraînement à suivre des instructions), publiée le **15 septembre 2026** sur le blog de l'entreprise (~2 500 mots). Le texte présente une nouvelle classe de modèles, les **System One Models**, et leur premier modèle, **Jev**, en accès anticipé.

**(1) Le principe.** Jev ne génère pas de texte : il reçoit un état non structuré et renvoie des décisions typées avec des probabilités calibrées, en une requête parallèle. **(2) L'entraînement.** Une méthode propre, **RLCD** (*Reinforcement Learning for Calibrated Decisions*), et une nouvelle architecture. **(3) Les chiffres déclarés.** Entrée à **0,042 $/MTok**, sortie gratuite, latence de bout en bout de **70 à 500 ms**, soit 40 à 200 fois plus rapide que les LLM de frontière sur les requêtes de ce type ; **193,6× plus rapide et 444,6× moins cher** sur les évaluations de workflow. **(4) Les limites énoncées** : chiffres LLM issus d'OpenRouter, évaluations écrites par l'équipe, référence moyennée sur deux modèles d'OpenAI et d'Anthropic, cardinalité maximale de 255 choix.

Le texte affirme : « Think of Jev as a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out. » Il a suscité la réponse de Cloudflare avec Clef : [[chen-reneau-flansburg-clef-decision-models-2026-10-01]].

## Titre Article

Introducing System One Models & Jev

## Date

2026-09-15

## URL

https://typesafe.ai/blog/introducing-system-one-models-and-jev

## Keywords

System One, modèle de décision, Jev, TypeSafe AI, RLCD, sortie typée, probabilités calibrées, échantillonnage parallèle, appel de fonction, workflow, évaluation de workflow, hallucination, latence, coût par appel, Kahneman, Jevons, classification, automatisation, Pareto

## Authors

Diogo Almeida — fondateur de TypeSafe AI, ancien chercheur chez OpenAI (billet du blog d'entreprise).

## Ton

Annonce de lancement à la première personne, enthousiaste et assumée (« beyond excited »), mais construite autour de la preuve : une section « Evidence » distingue les affirmations vérifiables (vitesse, coût, absence d'erreurs de type) des plus audacieuses, et chaque démonstration est suivie d'un encadré « Nuance » listant ses biais (requêtes simplifiées, évaluations écrites par l'équipe, référence favorable à OpenAI et Anthropic, chiffres OpenRouter). L'humour des démonstrations (Doom, Wikiracing) côtoie un tableau comparatif sec entre LLM et System One. L'argument central est posé en question : « Models have been superhuman at chat for years, so where is all the automation? »

## Pense-betes

- **Définition** : un System One Model produit des **valeurs typées** dont la structure est fixée à l'avance ; il ne peut donc pas commettre d'erreur de type. Le nom vient de la distinction de Kahneman (système 1 rapide / système 2 lent) ; « Jev » vient de William Stanley Jevons (chaque baisse du coût de l'intelligence ouvre de nouveaux usages).
- **Comparaison déclarée avec les LLM** : optimisation par RLHF/RLVR contre RLCD ; sortie en chaînes de caractères contre valeurs typées avec probabilités ; échantillonnage séquentiel contre parallèle ; sortie facturée environ 5× l'entrée contre sortie gratuite.
- **Cas d'usage visés** : « smart if-statements » (classer, router, noter, extraire, brancher), traitement de grands volumes, applications temps réel, vérification (garde-fous, détection de jailbreaks sur les sorties de LLM). Écartés : conversation, coding agents, preuves.
- **Évaluation de workflow** : un graphe de calcul supposé correct, des probabilités de référence tirées des plus gros modèles (moyenne de GPT-6 Astra et Fable 5.1), même workflow pour tous. Jev occupe la frontière de Pareto sur près de deux ordres de grandeur ; quatre workflows publiés.
- **Mise en garde de l'article** : l'absence d'erreurs de type est garantie par construction (« 0 % » non empirique) ; la soutenabilité du prix n'est pas démontrable à ce stade.
- **Démos** : agent jouant à Doom (environ 10 requêtes par seconde, ~7 $/heure) sur état structuré, pas sur images ; Wikiracing, avec un système en deux étapes au-delà de 255 choix.

## RésuméDe400mots

**Diogo Almeida**, fondateur de **TypeSafe AI**, annonce le **15 septembre 2026** la première **System One Model**, nommée **Jev**, disponible en accès anticipé. Sa question de départ : alors que les modèles sont surhumains en conversation depuis des années, où est l'automatisation ? Son diagnostic est que les LLM, optimisés pour la préférence humaine (RLHF) ou pour des récompenses vérifiables (RLVR), produisent des chaînes de caractères ; pour qu'un logiciel les exploite, il faut les analyser et les valider, avec le risque permanent qu'ils sortent du cadre.

TypeSafe propose une pile entièrement tournée vers l'automatisation : une nouvelle architecture de modèle, un échantillonneur parallèle et une méthode d'entraînement, **RLCD** (apprentissage par renforcement pour des décisions calibrées), qui optimise des réponses accompagnées de probabilités honnêtes. Jev prend en entrée des données non structurées, de préférence un état de programme, et renvoie des valeurs **typées**, dont la forme est définie à l'avance, avec des probabilités et des scores de confiance. Il renonce à la génération de texte, ce qui, selon l'auteur, l'empêche d'halluciner et d'erreur de type. Il se décrit comme un appel de fonction d'intelligence de frontière.

Les chiffres annoncés : entrée à 0,042 $ par million de jetons, sortie gratuite, latence de 70 à 500 ms contre 3 à 329 secondes pour les modèles de frontière, soit un facteur 40 à 200 sur des requêtes de type System One. L'échantillonnage est parallèle : toutes les sorties sont produites en une requête.

L'article sépare les affirmations vérifiables (vitesse, coût, absence d'erreurs de type) des plus audacieuses. Il présente une démonstration côte à côte avec GPT-5.6 Terra, dont le seul désaccord porte sur un niveau de risque de départ jugé réellement ambigu, puis des **évaluations de workflow** : on suppose un graphe de calcul correct et on compare les probabilités de chaque modèle à la moyenne de GPT-6 Astra et Fable 5.1. Jev domine la frontière de Pareto sur presque deux ordres de grandeur ; l'accueil de l'entreprise cite **193,6× plus rapide et 444,6× moins cher**, que l'auteur situe dans la fourchette haute des gains réels. Chaque démonstration est suivie de réserves : chiffres LLM issus d'OpenRouter, workflows écrits par l'équipe, référence favorable aux modèles d'OpenAI et d'Anthropic.

Les cas d'usage : décisions floues intégrées au code (classer, router, noter, extraire), traitement massif de données, applications temps réel, vérification des sorties de LLM. Deux démonstrations, Doom et Wikiracing, illustrent la vitesse et l'absence d'hallucination dans les choix à forte cardinalité (jusqu'à 255 options).

Le nom renvoie à Kahneman (système 1) et à Jevons : chaque baisse d'un ordre de grandeur du coût de l'intelligence ouvrirait autant d'usages nouveaux. TypeSafe ouvre l'accès anticipé et demande aux développeurs quelles décisions ils veulent automatiser.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-----------|-----------|-----------|-------------|--------|
| Diogo Almeida | PERSONNE | travaille_chez | TypeSafe AI | ORGANISATION | 0.96 | DYNAMIQUE | déclaré_article |
| Diogo Almeida | PERSONNE | publie | article Introducing System One Models & Jev | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| TypeSafe AI | ORGANISATION | publie | Jev | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Jev | TECHNOLOGIE | est_instance_de | System One Models | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| System One Models | CONCEPT | s_inspire_de | Thinking, Fast and Slow | DOCUMENT | 0.90 | STATIQUE | déclaré_article |
| Jev | TECHNOLOGIE | utilise | RLCD | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Jev | TECHNOLOGIE | utilise | échantillonnage parallèle | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Jev | TECHNOLOGIE | résout | hallucination | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| Jev | TECHNOLOGIE | permet | décisions typées à probabilités calibrées | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Jev | TECHNOLOGIE | surpasse | LLM de frontière | TECHNOLOGIE | 0.80 | STATIQUE | déclaré_article |
| Jev | TECHNOLOGIE | mesure | 193,6× plus rapide et 444,6× moins cher sur les évaluations de workflow | MESURE | 0.90 | STATIQUE | déclaré_article |
| Jev | TECHNOLOGIE | mesure | latence de 70 à 500 ms, 0,042 $/MTok en entrée | MESURE | 0.93 | DYNAMIQUE | déclaré_article |
| évaluation de workflow | METHODOLOGIE | est_basé_sur | moyenne de GPT-6 Astra et Fable 5.1 | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Jev | TECHNOLOGIE | s_applique_à | smart if-statements | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Jev | TECHNOLOGIE | concurrence | LLM de frontière | TECHNOLOGIE | 0.80 | STATIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Diogo Almeida | PERSONNE | rôle | Fondateur de TypeSafe AI, ancien d'OpenAI | AJOUT |
| TypeSafe AI | ORGANISATION | secteur | Modèles de décision pour l'automatisation | AJOUT |
| Jev | TECHNOLOGIE | catégorie | Premier System One Model, accès anticipé, cardinalité max 255 | AJOUT |
| System One Models | CONCEPT | définition | Modèles produisant des décisions typées et probabilistes, sans génération de texte | AJOUT |
| RLCD | METHODOLOGIE | définition | Reinforcement Learning for Calibrated Decisions, entraînement vers des probabilités calibrées | AJOUT |
| échantillonnage parallèle | CONCEPT | définition | Toutes les sorties produites en une seule requête, sans génération jeton par jeton | AJOUT |
| évaluation de workflow | METHODOLOGIE | définition | Même graphe de calcul pour tous les modèles, comparé à des probabilités de référence | AJOUT |
| LLM de frontière | TECHNOLOGIE | usage | Référence de comparaison (latence, coût, hallucination) | AJOUT |
| article Introducing System One Models & Jev | DOCUMENT | date | 2026-09-15 | AJOUT |
| Thinking, Fast and Slow | DOCUMENT | auteur | Daniel Kahneman, source du nom System One | AJOUT |
