# how-claude-code-is-built-pragmatic-engineer-2025-09-15
## Veille
Construction de Claude Code - Architecture AI-first - Product engineering - Pragmatic Engineer
## Titre Article
HOW CLAUDE CODE IS BUILT
## Date
2025-09-15
## URL
https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built
## Keywords
Claude Code, Anthropic, IA, ingénierie logicielle, développement, agents IA, terminal UX, prototypage rapide, tech stack, TypeScript, React, Ink, Yoga, Bun, sécurité, permissions, productivité, futur du développement, Gergely Orosz, Boris Cherny, Sid Bidasaria, Cat Wu
## Authors
Gergely Orosz (auteur de l'article), Boris Cherny, Sid Bidasaria, Cat Wu (équipe fondatrice de Claude Code)

## Ton
**Profil:** Conversationnel-Professionnel | Journalistique interview-based | Éducative-Analytique | Intermédiaire-Expert

Orosz adopte style longform tech journalism combinant narrative storytelling et technical deep-dive. Structure chronologique genèse → architecture → impact révèle product development journey. Multiple voix (Cherny, Bidasaria, Wu) créent richesse perspective. Details revealing (90% self-written code, 50% adoption 5 days) ground ambitious claims. Langage technique assumed (TypeScript, React/Ink, Yoga, Bun) vise developer audience. Admissions franches (permission system challenges, dogfooding extreme) show authenticity. Typique Pragmatic Engineer feature stories combinant access insider avec critical analysis visant engineering leaders et practitioners.

## Pense-betes
- Claude Code génère 500M$ de revenus annuels
- Prototype initial (sept 2024) : identifier la musique écoutée
- Percée : accès au système de fichiers et bash
- 50% des ingénieurs Anthropic l'utilisent quotidiennement 5 jours après le test interne
- Environ 90% du code de Claude Code est écrit par Claude Code lui-même
- Tech stack "sur distribution" : TypeScript, React/Ink, Yoga, Bun
- 60-100 versions internes par jour, 1 version externe quotidienne
- 20 prototypes d'UI en 2 jours pour la fonctionnalité "liste de tâches"
- Augmentation de 67% des pull requests chez Anthropic
- Système de permissions granulaire pour actions irréversibles
- Frontend React : partie la plus complexe avec canvas éditable géant
- Tool Use : permet à l'IA d'utiliser des outils (lire fichiers, lister répertoires)
## RésuméDe400mots
L'article de Gergely Orosz offre un aperçu rare du développement de Claude Code, l'outil de développement basé sur l'IA d'Anthropic qui a rapidement généré plus de 500 millions de dollars de revenus annuels. À travers des entretiens avec les ingénieurs fondateurs Boris Cherny et Sid Bidasaria, ainsi que la cheffe de produit Cat Wu, l'article explore la genèse, l'architecture et l'approche d'ingénierie "AI-first" de cet outil révolutionnaire.

Claude Code a débuté en septembre 2024 comme un prototype simple de Boris Cherny, capable initialement de seulement identifier la musique écoutée. La percée décisive est survenue en lui donnant accès au système de fichiers et aux commandes bash, lui permettant d'explorer les bases de code et de répondre à des questions en lisant et en suivant les imports de fichiers de manière autonome. Cette découverte a révélé un "surplus de produit" : la capacité du modèle existait déjà, mais aucun produit ne l'exploitait pleinement.

Le prototype a rapidement gagné en popularité chez Anthropic, avec 50% des ingénieurs l'utilisant quotidiennement cinq jours seulement après une version de test interne en novembre 2024. Malgré un débat interne sur le maintien de l'outil comme avantage concurrentiel, Anthropic a décidé de le lancer publiquement pour approfondir sa compréhension de la sécurité et des capacités des modèles. L'équipe, initialement composée de Boris seul, a atteint une dizaine d'ingénieurs en juillet, travaillant avec une grande autonomie et un accent sur le prototypage rapide.

L'utilité de Claude Code s'est étendue au-delà des développeurs, les data scientists l'adoptant également pour les requêtes et les visualisations. L'outil a contribué à une augmentation de 67% du nombre de pull requests chez Anthropic, malgré un doublement des effectifs d'ingénierie, démontrant un gain de productivité substantiel.

La pile technologique de Claude Code est "sur distribution" pour le modèle Claude, utilisant des technologies que le modèle maîtrise déjà : TypeScript, React avec Ink pour l'interface utilisateur du terminal, Yoga pour la mise en page et Bun pour la construction et le packaging. Fait remarquable, environ 90% du code de Claude Code est écrit par Claude Code lui-même, illustrant une approche "dogfooding" poussée à l'extrême.

L'architecture privilégie la simplicité, agissant comme une interface légère qui expose des outils et des hooks d'interface utilisateur au modèle Claude, lequel effectue la majeure partie du travail complexe. L'équipe affine constamment le système, supprimant souvent du code et simplifiant les prompts avec les nouvelles versions de modèles.

Un aspect crucial est le système de permissions, conçu pour empêcher l'IA d'apporter des modifications irréversibles sans le consentement de l'utilisateur. Il offre un contrôle granulaire, permettant aux utilisateurs d'accorder des permissions une fois, pour les sessions futures, ou de les refuser, avec des options de configuration à plusieurs niveaux.

Le processus de développement se caractérise par une vitesse extrême. L'équipe publie 60 à 100 versions internes par jour et une version externe quotidienne. Le prototypage est exceptionnellement rapide : Boris Cherny a développé environ 20 prototypes d'interface utilisateur pour une fonctionnalité de "liste de tâches" en seulement deux jours, itérant rapidement en fonction des prompts et des retours.

Cette itération rapide, rendue possible par les agents IA, accélère considérablement la conception et l'implémentation de nouvelles fonctionnalités, modifiant fondamentalement le rythme du prototypage. Claude Code introduit également des fonctionnalités innovantes d'expérience utilisateur pour le terminal, tirant parti de la nature interactive des terminaux alimentés par les LLM.
