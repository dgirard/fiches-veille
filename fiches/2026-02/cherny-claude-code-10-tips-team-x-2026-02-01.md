# cherny-claude-code-10-tips-team-x-2026-02-01
## Veille
Conseils utilisation Claude Code par équipe Anthropic - 10 astuces productivité

## Titre Article
Claude Code Tips from the Claude Code Team

## Date
2026-02-01

## URL
https://x.com/bcherny/status/2017742741636321619?s=20

## Keywords
Claude Code, git worktrees, plan mode, CLAUDE.md, skills, slash commands, subagents, BigQuery, Ghostty, parallélisme, productivité développeur, MCP Slack, CI/CD

## Authors
Boris Cherny (créateur de Claude Code)

## Ton
**Profil** : Perspective d'initié (créateur du produit), registre informel et direct, niveau technique intermédiaire à avancé

**Description** : Boris Cherny adopte un ton de partage authentique entre pairs, présentant non pas sa propre façon d'utiliser Claude Code mais celle de son équipe. Le style est pragmatique, orienté astuces concrètes avec une structure numérotée claire. L'autorité vient directement de la source (l'équipe qui a construit l'outil), ce qui confère une légitimité rare. Le texte évite le jargon marketing pour privilégier des conseils actionnables. Le public cible est constitué de développeurs déjà utilisateurs de Claude Code cherchant à optimiser leur workflow.

## Pense-betes
- **Git worktrees = déblocage productivité majeur** : 3-5 worktrees en parallèle, chacun avec sa session Claude. Support natif dans Claude Desktop app par @amorriscode
- **Mode plan systématique** : Toujours commencer les tâches complexes en mode plan. Investir dans le plan permet un "1-shot" de l'implémentation
- **Double Claude pour plans** : Un Claude écrit le plan, un second le révise comme "staff engineer"
- **CLAUDE.md évolutif** : Après chaque correction, dire "Update your CLAUDE.md so you don't make that mistake again". Claude excelle à écrire ses propres règles
- **Skills et slash commands** : Si action répétée plus d'une fois par jour → skill. Exemples : /techdebt, sync Slack/GDrive/Asana/GitHub
- **Correction de bugs simplifiée** : Activer MCP Slack, coller thread de bug, dire "fix". Ou simplement "Go fix the failing CI tests"
- **Ghostty recommandé** : Rendering synchronisé, couleurs 24-bit, support unicode
- **Subagents pour calcul intensif** : Ajouter "use subagents" aux requêtes complexes pour plus de puissance de calcul
- **BigQuery via CLI** : L'équipe n'écrit plus de SQL depuis 6+ mois, tout passe par Claude + CLI bq
- **Dictée vocale** : Parler 3x plus vite que taper, prompts plus détaillés (fn x2 sur macOS)
- **Mode apprentissage** : Activer style "Explanatory" ou "Learning" dans /config pour comprendre le "pourquoi"

## RésuméDe400mots
Boris Cherny, créateur de Claude Code, partage dix conseils d'utilisation directement issus de l'équipe Claude Code chez Anthropic. Il souligne d'emblée qu'il n'existe pas de méthode unique et encourage l'expérimentation.

**Parallélisme via git worktrees** : Le conseil numéro un de l'équipe est d'utiliser 3 à 5 git worktrees simultanément, chacun exécutant sa propre session Claude. Cette approche constitue le plus grand gain de productivité identifié. Certains membres créent des alias shell (za, zb, zc) pour naviguer rapidement entre worktrees, et d'autres maintiennent un worktree dédié à l'analyse de logs et BigQuery.

**Mode plan systématique** : Pour toute tâche complexe, l'équipe recommande de commencer en mode plan et d'investir l'effort nécessaire pour que Claude puisse implémenter en une seule passe. Une pratique consiste à utiliser un Claude pour rédiger le plan, puis un second pour le réviser avec l'œil d'un "staff engineer". Dès qu'une implémentation déraille, revenir immédiatement en mode plan plutôt que de persister.

**CLAUDE.md comme mémoire évolutive** : Après chaque correction, demander à Claude de mettre à jour son fichier CLAUDE.md pour ne pas répéter l'erreur. Claude s'avère étonnamment efficace pour rédiger ses propres règles. Un ingénieur fait maintenir à Claude un répertoire de notes par tâche/projet, mis à jour après chaque PR.

**Skills et commandes personnalisées** : Toute action répétée plus d'une fois par jour mérite de devenir une skill ou commande slash. Exemples cités : /techdebt pour identifier le code dupliqué, une commande synchronisant 7 jours de Slack, GDrive, Asana et GitHub en un seul contexte, ou des agents façon analytics-engineer pour dbt.

**Correction de bugs autonome** : Activer le MCP Slack, coller un thread de bug et simplement dire "fix". Ou demander "Go fix the failing CI tests" sans micro-management. Claude gère également le troubleshooting via docker logs sur des systèmes distribués.

**Techniques de prompting avancées** : Demander à Claude de jouer le rôle de reviewer ("Grill me on these changes"), de prouver que le code fonctionne via diff entre branches, ou de reprendre une implémentation médiocre avec "implement the elegant solution".

**Environnement terminal optimisé** : L'équipe privilégie Ghostty pour son rendering synchronisé et support unicode. Utilisation de /statusline pour afficher le contexte et la branche git, tabs colorés par tâche, et dictée vocale (fn x2 sur macOS) pour des prompts 3x plus rapides.

**Subagents et analytics** : Ajouter "use subagents" aux requêtes complexes pour déléguer du calcul. L'équipe utilise Claude avec le CLI BigQuery (bq) pour toutes ses requêtes analytics, sans écrire de SQL depuis plus de six mois.

**Apprentissage continu** : Activer le style "Explanatory" ou "Learning" dans /config, générer des présentations HTML ou diagrammes ASCII pour comprendre le code, et créer une skill de répétition espacée pour consolider les apprentissages.
