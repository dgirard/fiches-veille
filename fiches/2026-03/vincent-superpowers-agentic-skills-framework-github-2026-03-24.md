# vincent-superpowers-agentic-skills-framework-github-2026-03-24
## Veille
Framework de compétences agentiques pour agents de codage IA - Superpowers - 94k stars - Méthodologie développement structuré - GitHub

## Titre Article
Superpowers: An agentic skills framework & software development methodology that works

## Date
2026-03-24

## URL
https://github.com/obra/superpowers

## Keywords
framework agentique, compétences IA, agents de codage, méthodologie développement, TDD, sous-agents, Claude Code, Cursor, Codex, Gemini CLI, OpenCode, marketplace Anthropic, workflow structuré, brainstorming, planification, git worktrees, Prime Radiant, open source, plugins, développement piloté par les tests

## Authors
Jesse Vincent (obra), Prime Radiant

## Ton
Profil : perspective de mainteneur open source et architecte de méthodologie, registre technique-prescriptif, niveau avancé. Le README du dépôt adopte un ton à la fois pratique et opinioné, présentant Superpowers comme une réponse structurée au problème des agents IA indisciplinés. La métaphore centrale — traiter l'agent IA comme un « ingénieur junior enthousiaste mais sans goût, sans jugement et allergique aux tests » — ancre le projet dans une philosophie pragmatique de l'encadrement. Le style est celui d'une documentation technique de qualité, ponctuée de convictions fortes sur le TDD, YAGNI et DRY. L'autorité de Vincent (créateur de Request Tracker, Perl 5, K-9 Mail/Thunderbird Android, Keyboardio) renforce la crédibilité. Public cible : développeurs utilisant des agents de codage IA cherchant à structurer et fiabiliser leurs workflows.

## Pense-betes
- Superpowers est décrit comme « an agentic skills framework & software development methodology that works »
- Créé par Jesse Vincent (obra) et l'équipe de Prime Radiant
- Plus de 94 000 stars GitHub en mars 2026, l'un des projets open source à la croissance la plus rapide de l'année (~2 000 stars/jour)
- Inclus dans le marketplace officiel Anthropic depuis janvier 2026
- Fonctionne avec Claude Code, Cursor (via plugin marketplace), Codex, OpenCode et Gemini CLI
- Workflow en 7 phases : Brainstorm → Design → Plan → Implement (TDD) → Review → Finish → Cleanup
- Phase Brainstorm : questionnement socratique avant toute écriture de code, exploration d'alternatives, validation du design par morceaux digestes
- Phase Plan : tâches de 2-5 minutes avec chemins de fichiers exacts, code complet et étapes de vérification
- Subagent-Driven Development : un sous-agent frais par tâche avec revue en deux étapes (conformité au spec puis qualité du code)
- TDD strict RED-GREEN-REFACTOR : écrire le test, le voir échouer, écrire le code minimal, le voir passer, committer
- Règle radicale : si du code existe sans tests, l'agent est instruit de le supprimer
- Philosophie clé : imposer une méthodologie rigoureuse à un modèle existant produit de meilleurs résultats que laisser un modèle supérieur travailler sans contraintes
- Vincent a découvert que les principes de persuasion de Cialdini fonctionnent sur les LLMs comme sur les humains — les skills utilisent l'autorité, l'engagement, la preuve sociale et la rareté
- v2.0 : architecture séparée avec skills dans un dépôt dédié (obra/superpowers-skills)
- L'agent peut travailler de manière autonome pendant plusieurs heures sans dévier du plan
- Fiche existante connexe : superpowers-skills-coding-agents-vincent-2025-10-09.md (couvre le blog post original d'octobre 2025)
- Background de Jesse Vincent : créateur de Request Tracker (RT), gestionnaire de Perl 5 (2005-2008), cofondateur de Keyboardio, K-9 Mail (devenu Thunderbird pour Android)

## RésuméDe400mots
Superpowers est un framework open source de compétences agentiques créé par Jesse Vincent (obra) et l'équipe de Prime Radiant, qui impose une méthodologie de développement structurée aux agents de codage IA. Avec plus de 94 000 stars sur GitHub en mars 2026 et une inclusion dans le marketplace officiel d'Anthropic, le projet est devenu l'un des frameworks les plus populaires pour encadrer le travail des agents IA.

Le principe fondateur de Superpowers repose sur une métaphore pragmatique : traiter l'agent IA comme un ingénieur junior puissant mais indiscipliné, et lui imposer les garde-fous méthodologiques qui transforment les juniors en seniors. Plutôt que de chercher un modèle plus intelligent, le framework démontre qu'une méthodologie rigoureuse appliquée à un modèle existant produit de meilleurs résultats qu'un modèle supérieur travaillant sans contraintes.

Le workflow s'articule en sept phases. Le brainstorming emploie un questionnement socratique pour affiner les idées avant toute écriture de code, explorant les alternatives et présentant le design en sections validables. La planification découpe le travail en tâches de deux à cinq minutes, chacune spécifiant les chemins de fichiers exacts, le code complet et les étapes de vérification. L'implémentation suit un TDD strict selon le cycle RED-GREEN-REFACTOR : écrire un test qui échoue, le voir échouer, écrire le code minimal pour le faire passer, puis committer. La règle est radicale — si du code existe sans test accompagnant, l'agent est instruit de le supprimer.

L'innovation du « Subagent-Driven Development » permet de dispatcher un sous-agent frais par tâche avec une revue en deux étapes — conformité au cahier des charges, puis qualité du code. Cette architecture permet à l'agent de travailler de manière autonome pendant plusieurs heures sans dévier du plan initial.

Un aspect fascinant du projet est l'application des principes de persuasion de Cialdini à la conception des skills. Vincent a découvert que l'autorité, l'engagement, la preuve sociale et la rareté fonctionnent sur les LLMs comme sur les humains, améliorant significativement la fiabilité de l'agent.

Superpowers supporte désormais de multiples plateformes : Claude Code (via le marketplace Anthropic), Cursor (via plugin), Codex, OpenCode et Gemini CLI. La version 2.0 a introduit une séparation architecturale majeure avec les skills hébergées dans un dépôt dédié.

Le succès fulgurant du projet — près de 2 000 nouvelles stars par jour — témoigne d'une demande massive de la communauté développeur pour des outils qui structurent et disciplinent les agents de codage IA, au-delà de la simple capacité des modèles sous-jacents.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Jesse Vincent | PERSONNE | a_créé | Superpowers | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Prime Radiant | ORGANISATION | développe | Superpowers | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | impose | workflow structuré en 7 phases | METHODOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | applique | TDD RED-GREEN-REFACTOR | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | utilise | Subagent-Driven Development | METHODOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | fait_partie_de | marketplace Anthropic | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | supporte | Claude Code, Cursor, Codex, OpenCode, Gemini CLI | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Jesse Vincent | PERSONNE | affirme_que | méthodologie rigoureuse surpasse modèle supérieur sans contraintes | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Jesse Vincent | PERSONNE | applique | principes de persuasion Cialdini aux skills | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | a_atteint | 94 000+ stars GitHub | EVENEMENT | 0.95 | DYNAMIQUE | déclaré_article |
| Jesse Vincent | PERSONNE | a_créé | Request Tracker (RT) | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Jesse Vincent | PERSONNE | a_cofondé | Keyboardio | ORGANISATION | 0.95 | STATIQUE | déclaré_article |
| K-9 Mail | TECHNOLOGIE | est_devenu | Thunderbird pour Android | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Superpowers | TECHNOLOGIE | catégorie | Framework de compétences agentiques pour agents de codage IA | MISE_A_JOUR |
| Superpowers | TECHNOLOGIE | stars | 94 000+ (mars 2026) | MISE_A_JOUR |
| Superpowers | TECHNOLOGIE | version | v2.0 (architecture séparée skills/plugin) | MISE_A_JOUR |
| Jesse Vincent | PERSONNE | rôle | Créateur de Superpowers, fondateur Prime Radiant | MISE_A_JOUR |
| Prime Radiant | ORGANISATION | secteur | Outils de développement IA | AJOUT |
| Subagent-Driven Development | METHODOLOGIE | description | Dispatch d'un sous-agent par tâche avec revue en deux étapes | AJOUT |
| Marketplace Anthropic | TECHNOLOGIE | catégorie | Plateforme de distribution de plugins Claude Code | AJOUT |
| Principes de persuasion Cialdini | CONCEPT | application | Conception de skills pour améliorer fiabilité des agents IA | MISE_A_JOUR |
