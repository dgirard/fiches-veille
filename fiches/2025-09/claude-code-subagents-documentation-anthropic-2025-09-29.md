# claude-code-subagents-documentation-anthropic-2025-09-29

## Veille
Subagents Claude Code - AI assistants spécialisés - Context management - Task delegation - Documentation Anthropic

## Titre Article
Subagents - Claude Docs

## Date
2025-09-29

## URL
https://docs.anthropic.com/en/docs/claude-code/sub-agents

## Keywords
Claude Code, subagents, AI assistants, task-specific workflows, context management, system prompts, tools, delegation, code reviewer, debugger, data scientist, AI models, configuration, best practices, YAML frontmatter, Markdown files, tool permissions, `/agents` command

## Authors
Anthropic (documentation officielle)

## Ton
**Profil:** Professionnel-Pédagogique | Instructionnelle | Éducative | Intermédiaire

Documentation adopte ton technical writing standard équilibrant completeness et accessibility. Structure systematic (Caractéristiques → Configuration → Exemples → Best Practices) guides progressive understanding. Terminologie technique précise (YAML frontmatter, context windows, tool permissions) assume developer audience. Code examples concrets (code reviewer, debugger, data scientist) ground abstract concepts. Langage prescriptif pour best practices ("should", "must", "avoid") provides clear guidance. Formatting soigné avec sections clairement délimitées facilite scanning. Pas de marketing fluff — pure instructional content. Typique developer documentation quality (Stripe, Anthropic docs style) priorisant clarity et practical utility.

## Pense-betes
- **Subagents = AI assistants spécialisés** avec purpose spécifique, context window séparé, outils configurables, system prompt custom
- **Bénéfices clés** : préservation contexte, expertise spécialisée, réutilisabilité, permissions outils flexibles
- **Gestion via `/agents`** ou fichiers directs (Markdown + YAML frontmatter)
- **Configuration** : `name`, `description`, `tools` (optionnel), `model` (optionnel)
- **Invocation** : automatique par Claude Code ou explicite par mention du nom
- **Localisation fichiers** : `.claude/agents/` (projet) ou `~/.claude/agents/` (utilisateur)
- **Exemples types** : Code reviewer (Read, Grep, Glob, Bash), Debugger (Read, Edit, Bash, Grep, Glob), Data scientist (Bash, Read, Write)
- **Best practices** : commencer avec agents Claude-generated, design focused, prompts détaillés, limiter accès outils, version control pour agents projet
- **Chaînage possible** : multiples subagents pour workflows complexes
- **Sélection dynamique** : Claude choisit subagent approprié selon tâche/contexte

## RésuméDe400mots

La documentation officielle Claude Code introduit les "subagents", des assistants IA spécialisés conçus pour améliorer les workflows task-specific et optimiser la gestion du contexte dans l'environnement de développement. Ces subagents sont des personnalités IA préconfigurées auxquelles Claude Code peut déléguer des tâches, chacune opérant avec un purpose distinct et une expertise domaine ciblée.

**Caractéristiques Fondamentales**

Chaque subagent possède quatre attributs essentiels : une fenêtre de contexte indépendante qui évite la pollution du contexte conversationnel principal, un ensemble d'outils configurables spécifiques à son domaine, et un system prompt personnalisé guidant son comportement. Cette isolation contextuelle permet une résolution de problèmes plus focalisée et efficace, les instructions fine-tuned améliorant les taux de succès sur tâches désignées.

**Avantages Structurels**

Les subagents offrent quatre bénéfices majeurs : **préservation du contexte** en maintenant la conversation principale focalisée sur objectifs high-level, **expertise spécialisée** via instructions détaillées pour domaines spécifiques améliorant performance, **réutilisabilité** cross-projects avec possibilité de partage team promouvant workflows consistants, et **permissions flexibles** avec contrôle granulaire d'accès outils par type de subagent pour sécurité renforcée.

**Création et Configuration**

La création s'initie via commande `/agents` dans Claude Code, permettant sélection entre subagents project-level ou user-level. Les utilisateurs définissent le purpose et accordent accès outils spécifiques. Les subagents sont stockés comme fichiers Markdown avec YAML frontmatter : `.claude/agents/` pour project-level, `~/.claude/agents/` pour user-level. Les champs de configuration incluent `name` (unique identifier), `description` (purpose description), `tools` (liste comma-separated optionnelle), et `model` (spécification optionnelle comme `sonnet`, `opus`, `haiku`, ou `inherit`).

**Exemples Pratiques et Patterns**

La documentation fournit trois exemples archétypaux : **Code reviewer** expert en qualité et sécurité code utilisant Read, Grep, Glob, Bash; **Debugger** spécialisé en root cause analysis avec Read, Edit, Bash, Grep, Glob; **Data scientist** expert SQL et BigQuery analysis utilisant Bash, Read, Write. Ces patterns illustrent comment limiter l'accès outils au strict nécessaire améliore sécurité et focus.

**Gestion et Invocation**

La commande `/agents` offre interface interactive pour viewing, creating, editing, deleting subagents et managing tool permissions. Alternative : gestion directe fichiers. Claude Code peut déléguer automatiquement tâches aux subagents basé sur task description, subagent configuration et contexte courant. Invocation explicite possible par mention du nom.

**Best Practices et Cas d'Usage Avancés**

Les recommandations clés incluent : démarrer avec agents Claude-generated pour calibration initiale, designer subagents focused avec responsabilités claires, écrire system prompts détaillés, limiter accès outils au strict minimum, utiliser version control pour subagents projet. Les usages avancés comprennent chaînage de multiples subagents pour workflows complexes et leverage de sélection dynamique où Claude choisit automatiquement le subagent approprié selon contexte. Cette architecture modulaire permet composition flexible de capacités spécialisées tout en maintenant séparation des préoccupations et clarté contextuelle.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Anthropic | ORGANISATION | publie | documentation subagents Claude Code | EVENEMENT | 0.99 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | supporte | subagents | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| subagents | CONCEPT | possèdent | context window séparé | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| subagents | CONCEPT | sont_configurés_via | fichiers Markdown YAML frontmatter | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | délègue_tâches_à | subagents | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| subagents | CONCEPT | améliore | préservation du contexte | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Plan subagent | TECHNOLOGIE | est_utilisé_par | Claude Code | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Plan subagent | TECHNOLOGIE | fonctionne_en | plan mode | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| subagents | CONCEPT | permettent | chaînage de workflows | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| subagents | CONCEPT | stockés_dans | .claude/agents/ | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| MCP Tools | TECHNOLOGIE | accessibles_par | subagents | CONCEPT | 0.93 | DYNAMIQUE | déclaré_article |
| subagents | CONCEPT | peuvent_être_repris_via | agentId | CONCEPT | 0.90 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI | AJOUT |
| subagents | CONCEPT | définition | Assistants IA spécialisés avec context window séparé | AJOUT |
| Plan subagent | TECHNOLOGIE | rôle | Sous-agent natif Claude Code pour le plan mode | AJOUT |
| plan mode | CONCEPT | définition | Mode non-exécution pour planification et recherche codebase | AJOUT |
| MCP Tools | TECHNOLOGIE | catégorie | Outils Model Context Protocol accessibles aux subagents | AJOUT |
| agentId | CONCEPT | rôle | Identifiant unique permettant reprise de session subagent | AJOUT |
