# nunez-cherny-claude-code-workflow-venturebeat-2026-01-05

## Veille
Boris Cherny créateur Claude Code - workflow 5 agents parallèles, Opus 4.5, CLAUDE.md

## Titre Article
The creator of Claude Code just revealed his workflow, and developers are losing their minds

## Date
2026-01-05

## URL
https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are

## Keywords
Claude Code, Boris Cherny, Anthropic, workflow, agents parallèles, Opus 4.5, CLAUDE.md, subagents, slash commands, vérification, productivité développeur

## Authors
Michael Nuñez

## Ton
Profil : Article tech journalistique, registre enthousiaste et analytique, perspective actualité virale.
Style : Ton captivant avec ouverture dramatique ("Silicon Valley doesn't just listen — it takes notes"). Structure en sections thématiques claires. Métaphore gaming récurrente (Starcraft, "fleet commander", "real-time strategy game"). Citations multiples de réactions Twitter pour amplifier l'impact. Vocabulaire accessible avec explications techniques intégrées. Public cible : développeurs, tech leaders, early adopters IA.

## Pense-betes
- **Source** : Thread X de Boris Cherny (créateur et head of Claude Code chez Anthropic)
- **5 agents en parallèle** : onglets numérotés 1-5 dans iTerm2 avec notifications système
- **5-10 Claudes supplémentaires** sur claude.ai avec commande "teleport" pour transfert web→terminal
- **Modèle exclusif** : Opus 4.5 avec thinking - "plus lent mais moins de corrections = plus rapide au final"
- **CLAUDE.md** : fichier unique dans le repo git pour corriger les erreurs récurrentes de l'IA
- **Slash commands** : /commit-push-pr utilisé des dizaines de fois par jour
- **Subagents spécialisés** : code-simplifier (architecture), verify-app (tests e2e)
- **Boucle de vérification** : Claude teste via extension Chrome, ouvre navigateur, itère jusqu'à fonctionnel
- **Amélioration qualité** : 2-3x grâce à la vérification automatique
- **Métaphore** : passer de "taper du code" à "commander des unités autonomes" (comme Starcraft)
- **Citation clé** : "AI as a workforce, not an assistant"
- **Contexte** : Claude Code aurait atteint 1B$ ARR

## RésuméDe400mots
Michael Nuñez rapporte sur VentureBeat l'impact viral d'un thread X de Boris Cherny, créateur et responsable de Claude Code chez Anthropic, détaillant son workflow de développement. La communauté des développeurs qualifie ces révélations de moment charnière pour Anthropic.

Le workflow de Cherny repose sur l'exécution de cinq agents Claude en parallèle dans son terminal. Il numérote ses onglets iTerm2 de 1 à 5 et utilise les notifications système pour savoir quand un agent nécessite une intervention. Pendant qu'un agent exécute une suite de tests, un autre refactorise un module legacy, un troisième rédige de la documentation. Il lance également 5 à 10 sessions Claude supplémentaires sur claude.ai, avec une commande "teleport" pour transférer les sessions entre le web et sa machine locale.

Contrairement à l'obsession de l'industrie pour la latence, Cherny utilise exclusivement Opus 4.5, le modèle le plus lourd et lent d'Anthropic. Sa justification : bien que plus lent, ce modèle nécessite moins de corrections et excelle en utilisation d'outils, le rendant finalement plus rapide qu'un modèle léger. Le goulot d'étranglement n'est pas la vitesse de génération mais le temps humain passé à corriger les erreurs de l'IA.

Pour résoudre le problème d'amnésie des LLM entre sessions, l'équipe maintient un fichier unique CLAUDE.md dans leur repository git. Chaque fois que Claude commet une erreur, elle est documentée dans ce fichier pour éviter sa répétition. Cette pratique transforme le codebase en organisme auto-correctif où chaque erreur devient une règle permanente.

Cherny utilise des slash commands - raccourcis personnalisés versionnés dans le repository - pour automatiser les tâches répétitives. Sa commande /commit-push-pr, utilisée des dizaines de fois par jour, gère automatiquement le versioning. Il déploie également des subagents spécialisés : un code-simplifier pour nettoyer l'architecture et un verify-app pour les tests end-to-end.

La boucle de vérification constitue l'innovation clé. Claude teste chaque modification via l'extension Chrome, ouvre un navigateur, teste l'interface et itère jusqu'à ce que le code fonctionne et l'UX soit satisfaisante. Cette vérification automatique améliore la qualité finale de 2-3x.

L'article conclut sur un changement de paradigme : l'IA n'est plus un assistant d'autocomplétion mais un "système d'exploitation pour le travail lui-même". Les développeurs qui adoptent cette vision ne seront pas juste plus productifs - ils joueront à un jeu entièrement différent.
