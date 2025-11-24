# zhang-bloomberg-deploying-ai-engineering-2025-11-23
## Veille
Bloomberg - Enterprise AI Deployment - Platform Engineering - Paved Path - Uplift Agents

## Titre Article
What We Learned Deploying AI within Bloomberg’s Engineering Organization

## Date
2025-11-23

## URL
https://www.youtube.com/live/cMSprbJ95jg?si=4HnxK8w1ELvSr4tz&t=19560

## Keywords
Bloomberg, AI Deployment, Platform Engineering, Paved Path, Uplift Agents, Incident Response, Internal Developer Platform, Training, Adoption

## Authors
Lei Zhang (Head of Technology Infrastructure Engineering, Bloomberg)

## Ton
**Profil:** Infrastructure-Leader | Pragmatique | "Golden Path" | Éducatif

Lei Zhang a le ton d'un responsable d'infrastructure gérant une organisation massive (9000 ingénieurs). Il est calme, méthodique et focalisé sur la standardisation et l'efficacité à grande échelle. Il parle de "Paved Path" (voie pavée) et de principes directeurs ("make the right thing easy"). Son discours est celui de l'industrialisation de l'IA interne, loin de l'improvisation.

## Pense-betes
- **Échelle massive** : 9000 ingénieurs, un des plus gros réseaux privés, code base JavaScript énorme.
- **Au-delà du "Coding"** : L'IA ne sert pas qu'à écrire du code (greenfield), mais à la maintenance (brownfield).
    - **Uplift Agents** : Agents de migration et de maintenance (patchs automatiques, refactoring).
    - **Incident Response Agents** : L'IA est rapide et "non biaisée" pour scanner les logs, traces et configs lors d'une panne.
- **Le "Paved Path" (Golden Path)** : Pour éviter le chaos de 1000 équipes créant leurs propres outils IA, Bloomberg fournit une plateforme centralisée.
    - **AI Gateway** : Accès unifié aux modèles.
    - **MCP Hub** : Annuaire de serveurs MCP pour éviter la duplication (découverte d'outils).
    - **PaaS deployment** : Déploiement facile d'agents et outils internes.
- **Stratégies d'adoption** :
    - **Training** : Intégrer l'IA dans le "bootcamp" des nouveaux arrivants. Les juniors deviennent des agents du changement en ramenant ces pratiques dans leurs équipes.
    - **Guilds/Champions** : Communautés internes pour partager les "prompts" et pratiques.
    - **Visit Engineer** : Envoyer un ingénieur dans une autre équipe pour implémenter une solution (inner source).
- **Défis** : Augmentation du temps de merge et du nombre de PRs (goulot d'étranglement humain). Les leaders (managers) adoptent l'IA moins vite que les contributeurs individuels (IC).

## RésuméDe400mots
Lei Zhang, responsable de l'infrastructure technologique chez Bloomberg, détaille comment une organisation de 9 000 ingénieurs déploie l'IA de manière structurée et efficace. Avec une base de code massive et critique (marchés financiers), Bloomberg ne peut pas se permettre une adoption chaotique.

Zhang distingue l'IA pour le "coding" (écriture de nouvelles fonctionnalités) de l'IA pour le **"Software Engineering"** (maintenance, opération). Bloomberg met l'accent sur ce deuxième aspect, souvent négligé mais à fort ROI :
1.  **Uplift Agents** : Des agents dédiés aux migrations et aux correctifs de sécurité de masse, capables de proposer des patchs expliqués sur l'ensemble de la codebase.
2.  **Incident Response Agents** : En cas de panne, l'IA est utilisée pour scanner instantanément logs, télémétrie et configurations. Sa force est d'être "rapide et sans biais" (contrairement aux humains qui ont des préjugés sur la cause probable).

Pour gérer cette échelle, Bloomberg applique le principe du **"Paved Path" (la voie pavée)** : rendre la bonne méthode facile et la mauvaise difficile. Ils ont construit une plateforme centralisée offrant une passerelle IA (Gateway), un déploiement PaaS simplifié pour les outils internes, et surtout un **Hub MCP** (Model Context Protocol) pour partager les connecteurs et éviter que chaque équipe ne recrée les mêmes outils.

Sur le plan humain, Zhang note que l'adoption est plus forte chez les contributeurs individuels que chez les managers. Pour pallier cela, Bloomberg a intégré l'IA dans le cursus de formation des nouveaux arrivants. Ces "juniors" deviennent alors des vecteurs de changement, challengeant les seniors avec de nouvelles méthodes.

Zhang conclut en soulignant que l'IA change la **"fonction de coût"** de l'ingénierie : certaines tâches autrefois coûteuses (migrations, docs) deviennent bon marché, invitant à repenser les compromis habituels du développement logiciel.
