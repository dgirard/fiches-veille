---
themes: [agents-codage-ia-skills, transformation-adoption, strategie-frameworks]
source: "LinkedIn"
---
# meppiel-getting-started-agentic-sdlc-enterprise-2026-10-01

## Veille

Post LinkedIn de **Daniel Meppiel** (travaille avec des équipes d'ingénierie d'entreprise chez **Microsoft** et **GitHub**), daté du **1er octobre 2026**, accompagné d'une infographie (~350 mots). Il propose un cadre de décision à quatre points d'entrée pour démarrer un **SDLC agentique** à l'échelle de l'entreprise, le bon point de départ dépendant de ce qui fonctionne déjà, de ce qui manque et de la capacité de l'organisation à assumer la maintenance.

**(1)** Activer la base native : **Copilot Code Review**, **Coding Agent** et **Enterprise Managed Plugins**. **(2)** Développer ses pratiques avec **HVE Core** (Research → Plan → Implement → Review). **(3)** Traiter les skills comme du logiciel avec **APM**, le gestionnaire de paquets d'agents (sources contrôlées, versions épinglées, audit des dépendances). **(4)** Gouverner un catalogue : propriétaires, approbation, cycle de vie, avec le registre de plugins de **Microsoft Copilot** (prise en charge de GitHub Copilot annoncée comme prévue). Meppiel cite : *« Keep what works. Add what you can maintain. »*

Rapproche le packaging de skills de [[google-agent-plugins-packaging-skills-mcp-2026-08-06]].

## Titre Article

Getting started with Agentic SDLC at enterprise scale (post LinkedIn et infographie)

## Date

2026-10-01

## URL

https://www.linkedin.com/posts/danielmeppiel_in-my-work-at-microsoft-and-github-with-enterprise-share-7511397522762883073-6Mhi/

## Keywords

Agentic SDLC, SDLC agentique, skills, gestionnaire de paquets d'agents, APM, HVE Core, Copilot Code Review, Coding Agent, Enterprise Managed Plugins, registre de plugins, catalogue gouverné, golden path, chaîne d'approvisionnement, versions épinglées, Software Factory, GitHub Copilot, Microsoft

## Authors

Daniel Meppiel — travaille avec des équipes d'ingénierie d'entreprise chez Microsoft et GitHub ; post LinkedIn.

## Ton

Profil : retour d'expérience de praticien, formulé en cadre de décision numéroté et en impératifs courts, destiné aux responsables d'ingénierie et d'architecture en entreprise. Le texte s'ouvre sur sa position (« in my work at Microsoft and GitHub with enterprise engineering teams ») et pose une règle de choix : on part de l'écart que l'on a et de ce que les ressources permettent de traiter. L'ordre des quatre étapes va du moins coûteux (activer l'existant) au plus structurant (gouverner un catalogue). Les produits cités sont ceux de Microsoft et GitHub, ce que le contexte d'énonciation rend lisible. Le post appuie son raisonnement sur une affirmation de principe, que les skills portent l'expertise propre à une organisation qu'aucun modèle de pointe ne peut deviner, et se clôt sur trois injonctions brèves.

## Pense-betes

- **Le cadre n'est pas une séquence obligatoire** : quatre points d'entrée, à choisir selon ce qui fonctionne déjà, ce qui manque et la capacité de l'organisation à porter la maintenance. L'infographie conclut : *« Start where your organization is today. Build on the earlier foundations as you scale. »*
- **Étape 1, base native** : Copilot Code Review (revues activées de façon centralisée sur les dépôts), Coding Agent et Enterprise Managed Plugins (plugins approuvés et skills partagés déployés sans installation individuelle sur les clients pris en charge). Peu ou pas d'ingénierie sur mesure.
- **Étape 2, pratiques** : HVE Core est présenté comme une boîte à outils open source de Microsoft, évolutive, de pratiques, d'agents et de skills, à étudier et adapter plutôt qu'à réinventer. Boucle affichée : Research → Plan → Implement → Review.
- **Étape 3, skills comme logiciel** : quand les skills prolifèrent entre équipes, utiliser des paquets logiciels plutôt que des fichiers copiés. APM (open source) permet de créer, valider et composer des paquets, contrôler les sources, épingler les versions et auditer les dépendances.
- **Étape 4, catalogue gouverné** : propriétaires, approbation, mises à jour et retrait pour les skills et plugins partagés ; définition d'un « golden path » du SDLC agentique. Le registre de plugins de Microsoft Copilot sert à publier et gouverner des plugins pour Microsoft 365 ; la prise en charge de GitHub Copilot est indiquée comme prévue.
- **Pourquoi des skills** : instructions et ressources réutilisables qui capturent l'expertise d'ingénierie et d'organisation ; l'auteur écrit qu'aucun modèle de pointe ne peut déduire sa façon propre de travailler « unless you want to break the bank each time ».
- ⚠️ **Portée** : post de positionnement sans donnée chiffrée ni cas client ; il ne dit pas combien d'équipes ont suivi ce parcours. L'auteur relie le tout aux « Agentic Software Factories » à l'échelle de l'entreprise.

## RésuméDe400mots

Daniel Meppiel, qui accompagne des équipes d'ingénierie d'entreprise chez Microsoft et GitHub, publie le 1er octobre 2026 un cadre de décision pour démarrer un SDLC agentique. Il distingue quatre points d'entrée, le bon dépendant de ce qui fonctionne déjà, de ce qui manque et de la capacité de l'organisation à porter le sujet. L'objectif est de construire la capacité de fond tout en livrant vite un retour sur investissement.

Premier point : activer la base native. Copilot Code Review, Coding Agent et Enterprise Managed Plugins apportent des capacités partagées à toute l'entreprise avec peu ou pas d'ingénierie sur mesure. L'infographie précise que les revues s'activent de façon centralisée sur les dépôts et que les plugins approuvés et skills partagés se déploient sans installation individuelle sur les clients pris en charge.

Deuxième point : développer ses pratiques. HVE Core, boîte à outils open source de Microsoft, propose des pratiques d'ingénierie, des agents et des skills, avec une boucle Research, Plan, Implement, Review. Il s'agit de s'en inspirer et de l'adapter plutôt que d'inventer chaque flux depuis zéro.

Troisième point : traiter les skills comme du logiciel. À mesure que l'expertise de SDLC assisté par IA se diffuse et que les skills prolifèrent, l'auteur recommande des paquets plutôt que des fichiers copiés, avec rigueur dans la rédaction, l'empaquetage, les versions et la chaîne d'approvisionnement. APM, gestionnaire de paquets d'agents open source, permet de créer, valider et composer des paquets, de contrôler les sources, d'épingler les versions et d'auditer les dépendances.

Quatrième point : gouverner un catalogue. Les skills et plugins partagés reçoivent des propriétaires, des règles d'approbation et de cycle de vie, jusqu'au retrait, et l'organisation définit son « golden path ». Le registre de plugins de Microsoft Copilot, qui publie et gouverne des plugins pour Microsoft 365, en est une option ; la prise en charge de GitHub Copilot est indiquée comme prévue.

Les skills sont présentés comme brique centrale : instructions et ressources réutilisables qui encodent l'expertise d'ingénierie et d'organisation. Aucun modèle de pointe ne peut déduire cette façon de travailler, sauf à y mettre un budget considérable à chaque fois. Meppiel y voit une part de la fondation des « Agentic Software Factories » à l'échelle de l'entreprise, et de tout agent au-delà du SDLC. Sa règle de conduite tient en trois phrases : partir de l'écart que l'on a et de ce que ses ressources permettent de traiter, garder ce qui fonctionne, ajouter ce que l'on peut maintenir.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Daniel Meppiel | PERSONNE | travaille_chez | Microsoft | ORGANISATION | 0.90 | DYNAMIQUE | déclaré_article |
| Daniel Meppiel | PERSONNE | recommande | démarrer l'Agentic SDLC par l'écart existant et la capacité de maintenance de l'organisation | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Agentic SDLC | METHODOLOGIE | utilise | Copilot Code Review | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Agentic SDLC | METHODOLOGIE | utilise | Enterprise Managed Plugins | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Copilot Code Review | TECHNOLOGIE | fait_partie_de | GitHub Copilot | TECHNOLOGIE | 0.88 | STATIQUE | inféré |
| Microsoft | ORGANISATION | publie | HVE Core | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Microsoft | ORGANISATION | publie | APM | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| HVE Core | TECHNOLOGIE | permet | pratiques, agents et skills de SDLC à adapter | AFFIRMATION | 0.90 | DYNAMIQUE | déclaré_article |
| APM | TECHNOLOGIE | permet | contrôle des sources, versions épinglées et audit des dépendances de skills | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| APM | TECHNOLOGIE | résout | fichiers copiés entre équipes | CONCEPT | 0.85 | ATEMPOREL | inféré |
| Microsoft Copilot plugin registry | TECHNOLOGIE | permet | publication et gouvernance de plugins pour Microsoft 365 | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Daniel Meppiel | PERSONNE | affirme_que | aucun modèle de pointe ne peut deviner la façon de travailler d'une organisation | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Daniel Meppiel | PERSONNE | affirme_que | les skills sont la fondation des Software Factories agentiques à l'échelle de l'entreprise | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| Software Factory | METHODOLOGIE | utilise | skills | TECHNOLOGIE | 0.80 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Daniel Meppiel | PERSONNE | rôle | Accompagne des équipes d'ingénierie d'entreprise chez Microsoft et GitHub | AJOUT |
| Microsoft | ORGANISATION | secteur | Logiciel / IA | AJOUT |
| Agentic SDLC | METHODOLOGIE | définition | Cycle de vie logiciel où des agents prennent en charge des étapes, démarré selon quatre points d'entrée | AJOUT |
| Copilot Code Review | TECHNOLOGIE | catégorie | Revue de code native de GitHub Copilot, activable de façon centralisée | AJOUT |
| Enterprise Managed Plugins | TECHNOLOGIE | catégorie | Déploiement centralisé de plugins approuvés et de skills partagés | AJOUT |
| HVE Core | TECHNOLOGIE | catégorie | Boîte à outils open source Microsoft de pratiques, agents et skills (Research, Plan, Implement, Review) | AJOUT |
| APM | TECHNOLOGIE | catégorie | Gestionnaire de paquets d'agents open source (Microsoft) | AJOUT |
| Microsoft Copilot plugin registry | TECHNOLOGIE | statut | Registre de plugins pour Microsoft 365 ; prise en charge de GitHub Copilot prévue | AJOUT |
| GitHub Copilot | TECHNOLOGIE | catégorie | Assistant de codage de GitHub | AJOUT |
| skills | TECHNOLOGIE | définition | Instructions et ressources réutilisables qui encodent l'expertise d'une organisation pour les agents | AJOUT |
| Software Factory | METHODOLOGIE | statut | Cible évoquée par l'auteur à l'échelle de l'entreprise | AJOUT |
