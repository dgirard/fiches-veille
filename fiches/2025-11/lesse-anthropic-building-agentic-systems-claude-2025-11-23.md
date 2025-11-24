# lesse-anthropic-building-agentic-systems-claude-2025-11-23
## Veille
Construction de systèmes agentiques puissants avec Claude - Architecture et patterns d'implémentation - Anthropic
## Titre Article
Building Powerful Agentic Systems with Claude
## Date
2025-11-23
## URL
https://www.youtube.com/live/cMSprbJ95jg?si=4HnxK8w1ELvSr4tz
## Keywords
agents IA, Claude, Anthropic, architecture agentique, APIs Claude, développement agents, orchestration, plateforme développeurs
## Authors
Katelyn Lesse
## Ton
**Profil** : Ingénieure senior chez Anthropic, perspective technique approfondie, registre expert, présentation structurée pour développeurs expérimentés

**Style** : Présentation technique précise et méthodique. Ton professionnel et didactique, utilisant des exemples concrets d'implémentation. Langage technique mais accessible, avec des métaphores liées à l'architecture logicielle. L'autorité vient de l'expérience directe sur la plateforme Claude. Public cible : développeurs et architectes logiciels construisant des systèmes agentiques complexes.
## Pense-betes
- **3 piliers pour maximiser Claude** : Harness capabilities, Manage context window, Give Claude a computer
- **Thinking as API feature** : Performance scale avec le temps de raisonnement, budget configurable en tokens
- **MCP (Model Context Protocol)** : Standard pour interaction avec systèmes externes (GitHub, Sentry)
- **Memory tool** : Système de fichiers côté client pour stocker/rappeler le contexte pertinent
- **Context editing** : Nettoyage automatique des résultats d'outils obsolètes (39% de gain de performance)
- **Code execution tool** : Environnement sandboxé sécurisé sur serveurs Anthropic
- **Agent Skills** : Dossiers de scripts/instructions avec expertise domaine (ex: design system)
- **Infrastructure challenges** : Orchestration containers, persistance sessions, sécurité à l'échelle
## RésuméDe400mots
Katelyn Lesse, responsable de l'ingénierie pour la plateforme développeurs Claude chez Anthropic, présente une approche en trois piliers pour maximiser la performance des systèmes agentiques avec Claude, utilisant Claude Code comme exemple concret d'implémentation.

Le premier pilier consiste à **exploiter les capacités de Claude** via des fonctionnalités API personnalisables. Claude a développé une capacité de "thinking" où sa performance s'améliore avec le temps de raisonnement alloué. L'API expose cette fonctionnalité avec un budget configurable en tokens, permettant aux développeurs de choisir entre réponses rapides et raisonnement approfondi. Le tool use fiable permet à Claude d'appeler des outils personnalisés, comme le fait Claude Code avec ses nombreux outils de manipulation de fichiers et d'exécution de tests.

Le deuxième pilier concerne la **gestion du contexte**. Obtenir le bon contexte au bon moment est critique pour les performances. Trois innovations majeures supportent cela : MCP (Model Context Protocol) permet l'interaction standardisée avec des systèmes externes comme GitHub ou Sentry ; le Memory tool offre un système de fichiers côté client où Claude stocke intelligemment des informations (patterns de codebase, préférences git) pour les rappeler quand nécessaire ; le Context Editing nettoie automatiquement les résultats d'outils obsolètes, générant un gain de performance de 39% dans les benchmarks internes.

Le troisième pilier, le plus audacieux, préconise de **"donner un ordinateur à Claude"**. Plutôt que de débattre sur la complexité des harnesses d'agents, Anthropic fournit l'infrastructure permettant à Claude d'écrire et exécuter du code de manière autonome. Le Code Execution Tool offre un environnement sandboxé sécurisé sur les serveurs Anthropic, gérant containers et orchestration. Cette approche a permis le lancement de Claude Code sur web et mobile, résolvant des défis complexes d'orchestration et de persistance de sessions.

Les **Agent Skills** enrichissent cette autonomie en fournissant de l'expertise domaine. Ce sont des dossiers de scripts et instructions que Claude peut invoquer selon le contexte, comme appliquer automatiquement un design system lors de la création de landing pages. Cette combinaison de Skills avec MCP crée un système où Claude accède aux outils, au contexte, et possède l'expertise pour les utiliser efficacement.

La vision future d'Anthropic continue d'évoluer autour de ces trois axes : exposer les nouvelles capacités de Claude via l'API, améliorer la gestion contextuelle avec des outils plus sophistiqués, et résoudre les défis d'infrastructure pour permettre une véritable autonomie agentique sécurisée à grande échelle.