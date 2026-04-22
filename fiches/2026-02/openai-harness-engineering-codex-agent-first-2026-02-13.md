# openai-harness-engineering-codex-agent-first-2026-02-13

## Veille

Harness engineering OpenAI : 1M lignes de code zéro écriture manuelle, Codex agents, ingénierie d'environnement agent-first

## Titre Article

Harness engineering: leveraging Codex in an agent-first world

## Date

2026-02-13

## URL

https://openai.com/index/harness-engineering/

## Keywords

harness engineering, Codex, agents de codage, zéro code manuel, ingénierie de contexte, contraintes architecturales, garbage collection, linters custom, tests structurels, couches de dépendances, documentation structurée, boucles de feedback, agent-first, CI/CD, pull requests automatisées

## Authors

OpenAI

## Ton

**Profil** : Perspective d'ingénierie interne, registre technique élevé, ton de retour d'expérience factuel. Publication d'équipe d'ingénierie OpenAI.

**Description** : Le ton est celui d'un rapport d'ingénierie interne, factuel et ambitieux. L'article adopte une posture de "show, don't tell" en présentant les résultats d'une expérimentation interne radicale (zéro code écrit manuellement) avec des chiffres concrets. Le style est direct, orienté pratique, avec une structure qui progresse de "ce qui a cassé" vers "ce qui a fonctionné" et "ce qui s'est composé". L'article assume un public de développeurs et d'architectes logiciels familiers avec les agents de codage, les pipelines CI/CD et les pratiques d'ingénierie à grande échelle. Le message central est provocateur : le travail de l'ingénieur n'est plus d'écrire du code mais de concevoir des environnements pour les agents.

## Pense-betes

- **Expérimentation radicale** : une équipe de 3 ingénieurs (puis 7) a produit environ 1 million de lignes de code en 5 mois sans jamais écrire une seule ligne manuellement, uniquement via Codex agents. Environ 1500 PRs fusionnées, soit ~3.5 PRs par ingénieur par jour
- **Philosophie "no manually-written code"** : principe fondateur de l'équipe, les humains ne contribuent jamais directement au code. L'ingénierie se concentre sur les systèmes, l'échafaudage et l'effet de levier
- **Définition du harnais** : l'environnement complet d'échafaudage, contraintes et boucles de feedback qui entoure un agent IA (structure du repo, config CI, règles de formatage, gestionnaire de paquets, frameworks, instructions projet, intégration d'outils, linters)
- **Trois piliers** : (1) Ingénierie de contexte, (2) Contraintes architecturales, (3) Gestion de l'entropie (garbage collection)
- **Ingénierie de contexte** : documentation structurée dans le repo avec maps du système, plans d'exécution, spécifications de design. Les décisions d'architecture de Slack doivent être encodées en artefacts versionnés dans le repo. "Du point de vue de l'agent, ce qui n'est pas en contexte n'existe pas"
- **Contraintes architecturales** : modèle en couches strict avec direction de dépendances validée : Types → Config → Repo → Service → Runtime → UI. Application mécanique via linters custom (générés par Codex) et tests structurels dans la CI
- **Linters intelligents** : les messages d'erreur des linters sont conçus pour injecter des instructions de correction directement dans le contexte de l'agent, pas simplement bloquer le code
- **Garbage collection** : tâches Codex récurrentes en arrière-plan qui identifient les déviations par rapport aux "principes dorés", mettent à jour les grades de qualité, et ouvrent des PRs de refactoring pour auto-merge
- **Shift fondamental du rôle** : l'ingénieur passe de l'écriture de code à la conception d'environnements, la spécification d'intention, et la construction de boucles de feedback
- **Citation de Martin Fowler** : qualifie le harness engineering de "cadrage précieux" pour le développement assisté par IA
- **Le goulot d'étranglement** : la performance des agents dépend souvent plus de la conception de l'environnement que de l'intelligence du modèle

## RésuméDe400mots

OpenAI publie un retour d'expérience sur une méthodologie interne baptisée "harness engineering" appliquée au développement agent-first avec Codex. En cinq mois, une équipe de trois ingénieurs (élargie ensuite à sept) a produit un produit bêta interne contenant environ un million de lignes de code, avec zéro ligne écrite manuellement. Les agents Codex ont ouvert, évalué et fusionné environ 1500 pull requests, soit en moyenne 3,5 PRs par ingénieur par jour.

Le harnais (harness) est défini comme l'environnement complet d'échafaudage, de contraintes et de boucles de feedback qui entoure un agent IA : structure du dépôt, configuration CI, règles de formatage, frameworks applicatifs, instructions de projet, intégration d'outils externes et linters. Le premier commit dans un dépôt vide a été généré par Codex CLI avec GPT-5, guidé par des templates.

L'approche repose sur **trois piliers**. L'**ingénierie de contexte** s'appuie sur une documentation structurée dans le dépôt, organisée en répertoires contenant des cartes du système, des plans d'exécution et des spécifications de design. Les décisions d'architecture prises dans Slack doivent être encodées en artefacts versionnés et accessibles dans le repo, car du point de vue de l'agent, ce qui n'est pas en contexte n'existe pas.

Les **contraintes architecturales** sont appliquées mécaniquement via un modèle strict de couches de dépendances (Types → Config → Repo → Service → Runtime → UI), des linters custom générés par Codex, et des tests structurels de type ArchUnit exécutés dans la CI. Les messages d'erreur des linters sont conçus pour injecter des instructions de correction directement dans le contexte de l'agent, transformant les contraintes en guidage actif.

La **gestion de l'entropie** (garbage collection) consiste en des tâches Codex récurrentes qui scannent le code à la recherche de déviations par rapport aux principes établis, mettent à jour des grades de qualité, et ouvrent des PRs de refactoring auto-mergées.

L'article affirme un shift fondamental du rôle de l'ingénieur : celui-ci ne code plus mais conçoit des environnements, spécifie des intentions et construit des boucles de feedback pour les agents. Le plus grand défi identifié porte sur la conception de ces environnements, boucles de feedback et systèmes de contrôle. Le goulot d'étranglement de la performance des agents réside souvent dans la conception de l'environnement plutôt que dans l'intelligence du modèle. Martin Fowler a qualifié cette approche de "cadrage précieux" pour le développement assisté par IA.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| OpenAI | ORGANISATION | a_publié | Harness engineering: leveraging Codex in an agent-first world | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | a_produit | 1 million de lignes de code sans écriture manuelle | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| Codex | TECHNOLOGIE | a_généré | 1500 pull requests en 5 mois | EVENEMENT | 0.93 | STATIQUE | déclaré_article |
| Harness engineering | METHODOLOGIE | repose_sur | Ingénierie de contexte | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Harness engineering | METHODOLOGIE | repose_sur | Contraintes architecturales | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Harness engineering | METHODOLOGIE | repose_sur | Garbage collection | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Contraintes architecturales | CONCEPT | applique | Couches de dépendances Types→Config→Repo→Service→Runtime→UI | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Linters custom | TECHNOLOGIE | injecte | Instructions de correction dans contexte agent | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Garbage collection | CONCEPT | ouvre | PRs de refactoring auto-mergées | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Martin Fowler | PERSONNE | affirme_que | Harness engineering est un cadrage précieux | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| Codex | TECHNOLOGIE | utilise | GPT-5 | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Rôle de l'ingénieur | CONCEPT | se_transforme_en | Conception d'environnements pour agents | CONCEPT | 0.92 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| OpenAI | ORGANISATION | secteur | IA / Recherche | MISE_A_JOUR |
| Codex | TECHNOLOGIE | catégorie | Agent de codage autonome OpenAI | AJOUT |
| GPT-5 | TECHNOLOGIE | catégorie | Modèle de langage OpenAI | AJOUT |
| Harness engineering | METHODOLOGIE | catégorie | Méthodologie de développement agent-first | MISE_A_JOUR |
| Garbage collection (code) | CONCEPT | définition | Tâches récurrentes de scan et correction automatique de déviations | AJOUT |
| Martin Fowler | PERSONNE | rôle | Auteur et penseur du génie logiciel | MISE_A_JOUR |
| Tests structurels | TECHNOLOGIE | catégorie | Tests de type ArchUnit validant les contraintes architecturales | AJOUT |
