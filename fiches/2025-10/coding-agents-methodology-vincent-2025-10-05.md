# coding-agents-methodology-vincent-2025-10-05
## Veille
Méthodologie d'utilisation agents IA pour développement - Workflow multi-sessions - Blog Fsck
## Titre Article
How I'm using coding agents in September, 2025
## Date
2025-10-05
## URL
https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/
## Keywords
Coding Agents, AI-Assisted Development, Claude, Workflow Methodology, Git Worktrees, Code Review, Multi-Session Approach, Software Development, Test-Driven Development
## Authors
Jesse Vincent

## Ton
**Profil:** Conversationnel-Professionnel | Première personne narrative | Éducative-Opinion | Intermédiaire-Expert

Vincent partage workflow personnel avec humour technique ("Our robot buddies are quite credulous", "Sometimes it tries to start writing code before I can stop it"). Ton praticien expérimenté documentant méthodologie éprouvée ("point-in-time writeup of a flow that's been pretty effective for me") avec admissions franches sur limites IA. Assume familiarité développement (git worktrees, TDD, code review). Typique blogs perso développeurs seniors partageant sagesse terrain sans prétention théorique.

## Pense-betes
- Utilisation de git worktrees pour isoler les tâches
- Approche multi-sessions avec différents "rôles" IA (architecte/implémenteur)
- Prompts de brainstorming encourageant conception incrémentale
- Techniques de role-playing pour rendre l'IA plus critique
- Découpage du travail en petites tâches gérables
- Commits fréquents et approche TDD (Test-Driven Development)
- Utilisation de CodeRabbit pour les code reviews
- Outil custom : coderabbit-review-helper
- Processus de revue entre sessions pour challenger les suggestions IA
- Instructions strictes pour empêcher l'IA de dévier des plans
## RésuméDe400mots
Jesse Vincent présente une méthodologie structurée et évolutive pour travailler efficacement avec les agents de codage IA, principalement Claude. Son approche se distingue par une organisation rigoureuse du workflow de développement qui combine planification, implémentation et revue de code dans un processus itératif sophistiqué.

Le fondement de sa méthodologie repose sur l'utilisation de git worktrees pour isoler différentes tâches de projet, permettant de travailler sur plusieurs branches simultanément sans interférence. Cette approche technique crée un environnement propice à l'expérimentation tout en maintenant la stabilité du code principal.

L'élément central de son workflow est une approche multi-sessions qui attribue des "rôles" distincts aux différentes instances de Claude. Une session "architecte" se concentre sur la conception et la planification détaillée, tandis qu'une session "implémenteur" se charge de l'écriture du code. Cette séparation des préoccupations permet une plus grande clarté dans le processus de développement et évite que l'IA ne soit tiraillée entre des objectifs contradictoires.

Vincent a développé des prompts de brainstorming spécifiques qui encouragent une conception incrémentale plutôt que des solutions monolithiques. Ces prompts guident l'IA vers des architectures modulaires et testables, alignées avec les meilleures pratiques du développement logiciel moderne. Il utilise également des techniques de role-playing pour rendre l'IA plus critique et discernante, l'encourageant à remettre en question les hypothèses et à identifier les pièges potentiels.

Un aspect crucial de sa méthodologie est le découpage systématique du travail en petites tâches gérables. Plutôt que de demander à l'IA de résoudre des problèmes complexes d'un seul coup, Vincent préconise une approche itérative avec des objectifs clairement définis pour chaque étape. Cette granularité permet un meilleur contrôle du processus et facilite l'identification précoce des problèmes.

L'auteur insiste sur l'importance des commits fréquents et d'une approche TDD (Test-Driven Development). Chaque modification doit être accompagnée de tests appropriés, créant une suite de régression qui protège contre les régressions futures. Cette discipline, appliquée rigoureusement avec l'aide de l'IA, améliore significativement la qualité du code produit.

Le processus intègre également CodeRabbit, un outil de revue de code automatisé, complété par un helper personnalisé (coderabbit-review-helper) que Vincent a développé pour optimiser le workflow de revue. Ce processus de revue entre sessions permet de challenger les suggestions de l'IA et d'assurer que le code respecte les standards de qualité établis.

Vincent met en place des instructions strictes pour empêcher l'IA de dévier des plans établis lors de la phase d'architecture. Cette contrainte force une réflexion plus approfondie pendant la planification et évite les solutions de facilité ou les raccourcis qui pourraient compromettre la qualité du design.

En conclusion, la méthodologie de Jesse Vincent démontre qu'une utilisation efficace des agents de codage IA nécessite une orchestration réfléchie, des processus clairs et une supervision active. Son approche transforme l'IA d'un simple outil d'autocomplétion en un véritable partenaire de développement, tout en maintenant le contrôle humain sur les décisions architecturales critiques.
