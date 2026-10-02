---
themes: [recherche-education, outils-plateformes]
source: "surya.website"
---
# narreddi-training-ai-paint-with-code-2026-03-01

## Veille

Étude de cas de **Surya Narreddi** (avec **Cameron Franz** et **Alex Wang**) sur son site personnel, datée de **mars 2026** (jour non précisé ; ~1 500 mots), intitulée *Training AI to Paint with Code*. Les auteurs entraînent un modèle de langage (**Qwen 3.5 35B**) par apprentissage par renforcement (**GRPO**) à produire des peintures à l'aquarelle sous forme de code JavaScript **p5.brush**, le code étant l'artefact éditable. La question de fond : comment faire du RL quand la récompense, esthétique, n'est pas vérifiable.

**(1) La boucle** : prompt, code, rendu PNG (Puppeteer en bac à sable), juge, récompense, mise à jour GRPO. **(2) Échec de la première grille** : neuf signaux, plateau à **0,65** de récompense, cinq juges corrélés entre **0,85 et 0,95**, signal de longueur saturé dès l'étape 30. **(3) Correctif** : quatre composantes (portillon de compilation 0,05, longueur 0,05, **HPSv3** 0,30, juge par paires 0,60) ; le même modèle atteint l'ancien plateau trois fois plus vite et le code passe de **13 500 à moins de 2 000 jetons**. **(4) Pool de références** : 581 images, issues de 1 664 générations notées à la main (117 « love »). **(5) Prompt système** : évolué avec **GEPA** (200 itérations) ; une liste fermée de huit méthodes remplace 400 lignes de documentation d'API qui provoquaient des hallucinations.

Réserve des auteurs : « I don't think this is a better way to make images », et un rapport technique complet est annoncé pour juin 2026. Voir sur le même sujet des juges comme signaux de récompense : [[almeida-system-one-models-jev-2026-09-15]] (récompenses calibrées).

## Titre Article

Training AI to Paint with Code (RLing Qwen to paint with code)

## Date

2026-03-01

## URL

https://surya.website/rling-qwen-to-paint-with-code

## Keywords

apprentissage par renforcement, GRPO, fonction de récompense, juge par paires, récompense subjective, tâches créatives, Qwen, p5.brush, aquarelle, génération par code, HPSv3, GEPA, optimisation de prompt, pool de références, hallucination d'API, plateau de récompense, signaux corrélés, RLHF, Puppeteer, design de récompense

## Authors

Surya Narreddi — designer et développeur, auteur du projet (site personnel) ; collaborateurs Cameron Franz (infrastructure d'entraînement) et Alex Wang.

## Ton

Récit de projet à la première personne, à mi-chemin entre mémoire de design et notes de recherche. Le texte avance par échec puis diagnostic : le plateau, la lecture des sous-récompenses « en isolation », la correction. Les choix sont expliqués de façon concrète, sans jargon inutile, et les limites sont posées sans détour (images du pool toutes générées par des modèles, étape RLHF « que nous n'avons pas atteinte », méthode plus lente que la génération d'images classique). La conclusion défend l'intention : participer à la création au-delà du prompt, en agissant sur le modèle et sur l'artefact.

## Pense-betes

- **Le problème** : une image générée par un modèle ne s'édite qu'en reprompant ; générer du **code** rend l'artefact modifiable finement. Le RL exige une récompense, et l'esthétique n'est ni juste ni fausse.
- **Diagnostic de la première grille** : cinq signaux (reconnaissabilité, esthétique, technique, profondeur, adhérence au prompt) corrélés à 0,85-0,95 « mesuraient la même chose cinq fois » ; la longueur, environ un tiers de la récompense, ne donnait plus de gradient après l'étape 30 ; le seul signal à vraie variance, HPSv3, pesait 0,10.
- **Deux correctifs** : jugement **par paires** (le juge compare le rendu à deux références ; la récompense est la proportion de victoires) à la place d'un score de 0 à 10 compressé près de zéro ; **pool de références** notées à la main.
- **Pool** : 581 références (117 « love », 266 « okay », 198 de complément pour les couleurs peu couvertes), toutes produites par des modèles (AutoResearch avec Opus 4.6, GPT-5.4 et Gemini 3.1 Pro ; lot sur Gemini 3.1 Pro), faute d'exemples humains pour cet outil de niche.
- **Prompt système via GEPA** : 400 lignes de référence d'API faisaient inventer des méthodes ; la version à huit méthodes autorisées, sans documentation ni exemples, a donné pour la première fois trois générations sur trois exploitables.
- ⚠️ **Limites** : la proposition d'entraîner un petit modèle de récompense sur les notes (RLHF au sens propre) n'est pas réalisée ; une dernière passe d'entraînement est annoncée, avec rapport technique en juin 2026.

## RésuméDe400mots

**Surya Narreddi**, avec **Cameron Franz** et **Alex Wang**, décrit en **mars 2026** un projet d'entraînement d'un modèle de langage à peindre avec du code. Le point de départ est un constat : avec un modèle d'images, la seule façon de participer est le prompt, et l'image ne s'édite pas directement. Ici, le modèle écrit un programme **p5.brush** en JavaScript qui rend une aquarelle ; le code est l'artefact, modifiable plus finement qu'un prompt. La question de fond est de faire de l'apprentissage par renforcement sur des tâches créatives : le RL fonctionne quand la récompense est vérifiable, ce que l'esthétique n'est pas.

La boucle est répétée des milliers de fois. Le modèle (**Qwen 3.5 35B**) reçoit un prompt, par exemple un hibiscus pêche à l'aquarelle, écrit le sketch complet ; celui-ci est rendu en PNG dans un environnement Puppeteer isolé ; un modèle juge compare le rendu à deux références tirées d'un pool noté à la main ; le jugement devient une récompense ; **GRPO** met à jour le modèle.

La première grille comptait neuf signaux : portillon de compilation, usage de p5.brush, rampe de longueur autour de 3 000 jetons, HPSv3 (modèle de préférence humaine), adhérence au prompt jugée par GPT-5.4 et Gemini, et quatre juges de qualité. Le modèle a plafonné à 0,65, toutes les sorties étant des fleurs plates de style clip-art. L'examen isolé des sous-récompenses a montré que cinq juges étaient corrélés entre 0,85 et 0,95, que la longueur (un tiers du total) était saturée à l'étape 30 et que HPSv3, seul signal variable, ne pesait que 0,10.

Le correctif : un jugement **par paires** (le juge choisit la meilleure aquarelle entre le rendu et deux références ; la récompense est la fraction de comparaisons gagnées), plus étalé qu'un score absolu compressé, et un **pool de références** de 581 images, issu de 1 664 générations notées « love », « okay » ou « nope » (117 « love »). La grille passe à quatre composantes : portillon de compilation et d'usage du pinceau (0,05), longueur (0,05), HPSv3 (0,30), juge par paires (0,60). Avec le même modèle et les mêmes données, l'ancien plateau est atteint trois fois plus vite, la progression continue et le code passe de 13 500 à moins de 2 000 jetons. Toutes les images du pool sont des sorties de modèles, faute d'exemples humains.

Le prompt système a aussi été retravaillé avec **GEPA** : une référence d'API de 400 lignes faisait inventer des méthodes inexistantes ; après 200 itérations contre un juge à sept exemples, la meilleure version est une liste fermée de huit méthodes, sans documentation. L'auteur en tire que de longues références dans un prompt favorisent l'hallucination et qu'une liste courte et tranchée contraint mieux.

En conclusion, l'auteur écrit que le RL subjectif oblige à rédiger la récompense à la main : trop spécifique, le modèle copie les exemples ; trop lâche, il n'apprend rien. Il ne présente pas la méthode comme meilleure pour produire des images, plutôt comme un moyen d'agir sur le prompt, le modèle et l'artefact. Une dernière passe et un rapport technique sont annoncés pour juin 2026.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-----------|-----------|-----------|-------------|--------|
| Surya Narreddi | PERSONNE | publie | article Training AI to Paint with Code | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Surya Narreddi | PERSONNE | collabore_avec | Cameron Franz | PERSONNE | 0.95 | STATIQUE | déclaré_article |
| projet Paint with Code | METHODOLOGIE | utilise | Qwen 3.5 35B | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| projet Paint with Code | METHODOLOGIE | utilise | GRPO | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| projet Paint with Code | METHODOLOGIE | utilise | p5.brush | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| jugement par paires | METHODOLOGIE | résout | plateau de récompense | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| jugement par paires | METHODOLOGIE | améliore | grille de récompense | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| jugement par paires | METHODOLOGIE | utilise | pool de références | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| grille de récompense | CONCEPT | mesure | plateau à 0,65 avec neuf signaux, juges corrélés à 0,85-0,95 | MESURE | 0.95 | STATIQUE | déclaré_article |
| grille de récompense | CONCEPT | mesure | code réduit de 13 500 à moins de 2 000 jetons | MESURE | 0.93 | STATIQUE | déclaré_article |
| GEPA | TECHNOLOGIE | réduit | hallucination d'API | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| Surya Narreddi | PERSONNE | affirme_que | une documentation d'API longue dans le prompt système favorise l'hallucination | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Surya Narreddi | PERSONNE | affirme_que | le RL sur tâches créatives est un problème de design de la récompense | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| projet Paint with Code | METHODOLOGIE | s_oppose_à | RLVR | METHODOLOGIE | 0.75 | ATEMPOREL | inféré |
| HPSv3 | TECHNOLOGIE | fait_partie_de | grille de récompense | CONCEPT | 0.93 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Surya Narreddi | PERSONNE | rôle | Designer et développeur, auteur du projet | AJOUT |
| Cameron Franz | PERSONNE | rôle | Collaborateur, infrastructure d'entraînement | AJOUT |
| article Training AI to Paint with Code | DOCUMENT | date | 2026-03 | AJOUT |
| projet Paint with Code | METHODOLOGIE | définition | Entraînement par RL d'un LLM à générer des peintures sous forme de code | AJOUT |
| Qwen 3.5 35B | TECHNOLOGIE | usage | Modèle de base entraîné | AJOUT |
| GRPO | METHODOLOGIE | définition | Algorithme de RL utilisé pour les mises à jour | AJOUT |
| p5.brush | TECHNOLOGIE | catégorie | Bibliothèque JavaScript de pinceaux pour p5 | AJOUT |
| HPSv3 | TECHNOLOGIE | catégorie | Modèle de préférence humaine, poids 0,30 | AJOUT |
| GEPA | TECHNOLOGIE | catégorie | Bibliothèque d'optimisation de prompt par évolution | AJOUT |
| jugement par paires | METHODOLOGIE | définition | Récompense = fraction de comparaisons gagnées contre des références | AJOUT |
| grille de récompense | CONCEPT | définition | Ensemble pondéré de signaux ; version finale à quatre composantes | AJOUT |
| pool de références | CONCEPT | définition | 581 images, dont 117 de niveau « love » notées à la main | AJOUT |
| plateau de récompense | CONCEPT | définition | Stagnation à 0,65 sous la première grille | AJOUT |
| hallucination d'API | CONCEPT | définition | Invention de méthodes inexistantes à partir d'une longue référence | AJOUT |
| RLVR | METHODOLOGIE | définition | RL à récompenses vérifiables, opposé au cas esthétique | AJOUT |
