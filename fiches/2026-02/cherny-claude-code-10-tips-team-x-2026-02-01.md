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

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Boris Cherny | PERSONNE | a_créé | Claude Code | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Boris Cherny | PERSONNE | publie | conseils équipe Claude Code | CONCEPT | 0.98 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | développe | Claude Code | TECHNOLOGIE | 0.99 | DYNAMIQUE | inféré |
| Claude Code | TECHNOLOGIE | supporte | git worktrees | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| amorriscode | PERSONNE | a_intégré | git worktrees | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Claude Desktop app | TECHNOLOGIE | intègre | git worktrees | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Boris Cherny | PERSONNE | recommande | Plan mode | METHODOLOGIE | 0.96 | ATEMPOREL | déclaré_article |
| Plan mode | METHODOLOGIE | améliore | qualité implémentation | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| CLAUDE.md | TECHNOLOGIE | sert_de | mémoire évolutive agent | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | supporte | slash commands | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | s_intègre_avec | Slack MCP | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | s_intègre_avec | BigQuery | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | supporte | subagents | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Ghostty | TECHNOLOGIE | est_recommandé_par | équipe Claude Code | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |
| Opus 4.5 | TECHNOLOGIE | est_utilisé_pour | validation permissions subagents | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Boris Cherny | PERSONNE | rôle | Créateur de Claude Code, Anthropic | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
| amorriscode | PERSONNE | rôle | Membre équipe Claude Code, auteur du support natif worktrees | AJOUT |
| Claude Desktop app | TECHNOLOGIE | catégorie | Application bureau Claude, support natif git worktrees | AJOUT |
| git worktrees | TECHNOLOGIE | usage | Parallélisme de sessions Claude, gain de productivité majeur | AJOUT |
| Plan mode | METHODOLOGIE | usage | Planification préalable avant implémentation complexe | AJOUT |
| CLAUDE.md | TECHNOLOGIE | usage | Fichier de règles évolutif, mémoire persistante de l'agent | AJOUT |
| slash commands | TECHNOLOGIE | usage | Automatisation de tâches récurrentes dans Claude Code | AJOUT |
| Slack MCP | TECHNOLOGIE | catégorie | Intégration MCP pour correction de bugs depuis threads Slack | AJOUT |
| BigQuery | TECHNOLOGIE | usage | Requêtes analytics via CLI bq, remplace SQL manuel | AJOUT |
| subagents | CONCEPT | usage | Délégation de calcul intensif, maintien de la fenêtre de contexte principale | AJOUT |
| Ghostty | TECHNOLOGIE | catégorie | Emulateur de terminal, rendering synchronisé, 24-bit couleur | AJOUT |
| Opus 4.5 | TECHNOLOGIE | usage | Modèle Claude dédié à la validation des permissions via hook | AJOUT |
