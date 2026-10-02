---
themes: [produits-services, outils-plateformes, agents-codage-ia-skills]
source: "Cloudflare Blog"
---
# chen-reneau-flansburg-clef-decision-models-2026-10-01

## Veille

Billet de **Michelle Chen, Alex Reneau et Kevin Flansburg**, publié le **1er octobre 2026** sur le blog de **Cloudflare** (~10 minutes de lecture, semaine « AI Birthday »). Cloudflare y publie **Clef** et **Clef-flash**, ses premiers modèles entraînés en interne, hébergés sur **Workers AI** et diffusés en open source (Apache 2.0, Hugging Face), ainsi qu'un service de fine-tuning par apprentissage par renforcement.

**(1) Positionnement.** Réponse explicite au modèle **Jev** de TypeSafe : API compatible, mêmes sorties typées. **(2) Différences déclarées** : encodeur de vision (Jev ne traite que du texte), contexte de **64k** contre 32k. **(3) Résultats** sur le *Jev Decision Index* : Clef en tête ; sur les évaluations de workflow de TypeSafe, il bat Jev dans 3 cas sur 4. Latence médiane **209 ms** (Clef) et **38,8 ms** (Clef-flash) contre 524 ms pour Jev. **(4) Architecture** : Qwen gelé, passe de préremplissage, notation parallèle des choix du schéma. **(5) Service RL** : AI Gateway, Workers AI, Containers et un nouveau *Trainer*.

Les auteurs notent que les modèles de décision se distinguent des LLM, non déterministes, par des sorties bornées, rapides et cohérentes. Voir l'annonce de départ : [[almeida-system-one-models-jev-2026-09-15]].

## Titre Article

Introducing Clef: our open-source decision models, and new RL fine-tuning platform

## Date

2026-10-01

## URL

https://blog.cloudflare.com/clef-decision-models/

## Keywords

Clef, Clef-flash, modèle de décision, Cloudflare, Workers AI, Jev, Jev Decision Index, open source, Apache 2.0, fine-tuning, apprentissage par renforcement, RLCD, Qwen, DiffusionGemma, logprobs, calibration, latence, classification, AI Gateway, agent cloud

## Authors

Michelle Chen, Alex Reneau, Kevin Flansburg — équipe Workers AI / plateforme IA, blog Cloudflare.

## Ton

Billet de lancement produit d'une équipe d'ingénierie, sur un ton positif et technique. L'entrée en matière situe Clef par rapport au « buzz » autour de Jev, puis alterne exemples concrets (classement de domaines par la Threat Intelligence, tri de tickets de support), tableaux de benchmarks et détails d'entraînement (adaptateurs de rang 256, perte de Brier). Le nom est expliqué par une analogie musicale (la clé de portée qui fixe le domaine des notes ; « CF » pour Cloudflare). Le texte parle au futur de la plateforme : le service de fine-tuning démarre avec des ingénieurs déployés (FDE), la version libre-service viendra plus tard, et Cloudflare cherche des clients partenaires de conception.

## Pense-betes

- **Définition posée par l'article** : un modèle de décision renvoie des réponses typées avec probabilités ; le code route, escalade ou renvoie à un humain. Cadre : agents qui collectent le contexte, décident et agissent, avec un humain seulement si nécessaire.
- **Cas interne** : classement de domaines par l'équipe Threat Intelligence avec Browser Run : **2,2 s** pour récupérer, rendre et classer, contre 4,7 s pour gpt-oss-120b, qui ne renvoyait que deux catégories.
- **Résultats sélectionnés** (Clef / Clef-flash / Jev) : BFCL 98,47 / 98,76 / 95,75 ; BANKING77 94,20 / 90,93 / 79,74 ; When2Call 72,37 / 65,58 / 80,97 ; BRIGHT 45,91 / 39,26 / 47,52. Sur les workflows de TypeSafe : facturation 64,7 contre 61,8, agent trace observability 68,5 contre 71,6.
- **Entraînement** : base Qwen gelée (Qwen3.8-27B pour Clef, Qwen3.5-9B pour Clef-flash), tête de routage et adaptateurs de rang 256, entropie croisée à lissage d'étiquettes plus perte de Brier, puis **RLCD** avec crédit partiel aux choix ordinaux voisins. L'approche initiale adaptait DiffusionGemma en exposant les logprobs.
- **Service RL** : AI Gateway (jeu de données à partir du trafic), Workers AI (rollouts), Containers (bac à sable de notation), *Trainer* (nouveau), Workers AI avec modèle apporté (Cog, hérité de Replicate). Données clients non lues ni stockées, sauf fine-tuning.
- ⚠️ **Réserves visibles dans les tableaux** : Clef-flash tombe à 66,77 sur CLINC150+OOS et Jev reste devant sur When2Call, BRIGHT et PhishNChips (DiffusionGemma Jev à 85,35) ; Laya est plus rapide mais nettement moins précis.

## RésuméDe400mots

Le **1er octobre 2026**, **Michelle Chen, Alex Reneau et Kevin Flansburg** annoncent sur le blog de **Cloudflare** deux modèles de décision, **Clef** et **Clef-flash**, hébergés sur **Workers AI** et publiés sur Hugging Face sous licence Apache 2.0, ainsi qu'un produit de fine-tuning par apprentissage par renforcement. Le billet part du « buzz » autour du modèle **Jev** de TypeSafe : un modèle de décision produit à bas coût, vite et de façon cohérente des sorties structurées bornées, à insérer dans un workflow quand une décision est requise, par opposition aux LLM, largement non déterministes mais ouverts.

Un modèle de décision reçoit un état, par exemple un message de support, et répond à des questions typées (urgence, équipe, gravité) avec des probabilités, que le code utilise pour router, escalader ou déléguer à un humain. Chez Cloudflare, Clef classe des domaines pour la Threat Intelligence : 2,2 secondes pour récupérer, rendre et classer un site, contre 4,7 secondes pour gpt-oss-120b, qui ne renvoyait que deux catégories.

Clef se distingue de Jev par un **encodeur de vision**, donc la classification d'images, et un contexte de **64k** contre 32k. L'API est compatible avec celle de Jev, ce qui rend le remplacement simple. Sur le *Jev Decision Index*, Clef est en tête ; les tableaux montrent des avantages nets (BFCL 98,47, BANKING77 94,20, CLINC150+OOS 97,43) et des cas où Jev ou une variante restent devant (When2Call, BRIGHT, PhishNChips). Sur les évaluations de workflow de TypeSafe, Clef bat Jev sur trois des quatre. Latence médiane : 209,3 ms pour Clef, 38,8 ms pour Clef-flash, 524,1 ms pour Jev ; l'hébergement sur le réseau de GPU en périphérie réduit la latence réseau. Clef peut ainsi se placer sur le chemin critique d'un agent, avant un LLM chargé d'agir.

L'entraînement : le projet est parti d'une adaptation de DiffusionGemma exposant les logprobs, appuyée sur les travaux de Matt Mastracci. Clef utilise Qwen3.8-27B gelé (Clef-flash : Qwen3.5-9B) pour une passe de préremplissage seule, puis note en parallèle les choix valides du schéma, sans génération de texte. Une tête de routage à deux étapes d'attention et des adaptateurs de rang 256 sont entraînés avec une entropie croisée à lissage d'étiquettes et une perte de Brier pour la calibration, puis avec **RLCD**, qui accorde un crédit partiel aux choix ordinaux adjacents.

Le service de fine-tuning s'adresse d'abord aux clients accompagnés par des ingénieurs déployés, puis en libre-service. Il s'appuie sur AI Gateway (jeu de données), Workers AI (rollouts), Containers (bac à sable de notation), un nouveau *Trainer* (mise à jour des poids) et le déploiement de modèles apportés. Cloudflare y voit un moyen de spécialiser Clef (modération, tri de support, bots) avec ses quinze ans de données labellisées, et d'incarner son « agent cloud ».

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-----------|-----------|-----------|-------------|--------|
| Michelle Chen | PERSONNE | travaille_chez | Cloudflare | ORGANISATION | 0.90 | DYNAMIQUE | inféré |
| Cloudflare | ORGANISATION | publie | Clef | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Cloudflare | ORGANISATION | publie | Clef-flash | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Clef-flash | TECHNOLOGIE | est_variante_de | Clef | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | est_instance_de | modèle de décision | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | converge_avec | Jev | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | surpasse | Jev | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | est_basé_sur | Qwen | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | utilise | RLCD | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | s_inspire_de | DiffusionGemma | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | mesure | latence médiane de 209,3 ms (Clef-flash : 38,8 ms) contre 524,1 ms pour Jev | MESURE | 0.95 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | mesure | 2,2 s pour classer un domaine contre 4,7 s pour gpt-oss-120b | MESURE | 0.95 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | utilise | Workers AI | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| service de fine-tuning RL | TECHNOLOGIE | utilise | AI Gateway | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| service de fine-tuning RL | TECHNOLOGIE | utilise | Cloudflare Containers | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Cloudflare | ORGANISATION | publie | service de fine-tuning RL | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Cloudflare | ORGANISATION | affirme_que | Clef a le potentiel de changer la façon d'utiliser les agents | AFFIRMATION | 0.80 | ATEMPOREL | déclaré_article |
| Jev | TECHNOLOGIE | permet | décisions typées à probabilités calibrées | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Michelle Chen | PERSONNE | rôle | Co-autrice, équipe Workers AI de Cloudflare | AJOUT |
| Cloudflare | ORGANISATION | secteur | Réseau, sécurité, plateforme IA (agent cloud) | AJOUT |
| Clef | TECHNOLOGIE | catégorie | Modèle de décision open source (Apache 2.0), contexte 64k, encodeur de vision | AJOUT |
| Clef-flash | TECHNOLOGIE | catégorie | Variante rapide de Clef pour décisions critiques en latence | AJOUT |
| Jev | TECHNOLOGIE | catégorie | Modèle de décision de TypeSafe AI, texte seul, contexte 32k | AJOUT |
| modèle de décision | CONCEPT | définition | Modèle renvoyant des sorties typées bornées avec probabilités, destiné à être inséré dans un workflow | AJOUT |
| RLCD | METHODOLOGIE | définition | Reinforcement Learning for Calibrated Decisions, avec crédit partiel aux choix ordinaux adjacents | AJOUT |
| Qwen | TECHNOLOGIE | usage | Modèle de base gelé (27B pour Clef, 9B pour Clef-flash) | AJOUT |
| DiffusionGemma | TECHNOLOGIE | usage | Base de l'approche initiale par logprobs | AJOUT |
| Workers AI | TECHNOLOGIE | usage | Hébergement des modèles sur les GPU en périphérie | AJOUT |
| AI Gateway | TECHNOLOGIE | usage | Capture du trafic IA pour constituer un jeu de données | AJOUT |
| Cloudflare Containers | TECHNOLOGIE | usage | Bac à sable de notation et de rejeu des actions | AJOUT |
| service de fine-tuning RL | TECHNOLOGIE | statut | Accompagné par ingénieurs déployés, libre-service à venir | AJOUT |
