---
themes: [agents-codage-ia-skills]
source: "Anthropic"
---
# claude-code-subagents-documentation-anthropic-2025-09-29

## Veille
Subagents Claude Code - Assistants IA spécialisés - Gestion du contexte - Délégation de tâches - Documentation Anthropic

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
**Profil:** Professionnel-pédagogique | Instructionnel | Éducatif | Intermédiaire

La documentation adopte un ton de rédaction technique standard, équilibrant exhaustivité et accessibilité. La structure systématique (Caractéristiques → Configuration → Exemples → Bonnes pratiques) guide une compréhension progressive. La terminologie technique précise (frontmatter YAML, fenêtres de contexte, permissions d'outils) suppose un public de développeurs. Les exemples de code concrets (relecteur de code, débogueur, data scientist) ancrent les concepts abstraits. Le langage prescriptif pour les bonnes pratiques fournit des consignes claires. La mise en forme soignée, avec des sections clairement délimitées, facilite la lecture en diagonale. Aucun discours marketing — contenu purement instructionnel. Qualité typique de la documentation développeur (style Stripe, docs Anthropic) privilégiant clarté et utilité pratique.

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
| Anthropic | ORGANISATION | publie | documentation subagents Claude Code | DOCUMENT | 0.99 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | subagents | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| subagents | TECHNOLOGIE | utilise | context window séparé | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| subagents | TECHNOLOGIE | utilise | fichiers Markdown YAML frontmatter | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | permet | délégation de tâches aux subagents | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| subagents | TECHNOLOGIE | améliore | préservation du contexte | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | Plan subagent | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Plan subagent | TECHNOLOGIE | s_applique_à | plan mode | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| subagents | TECHNOLOGIE | permet | chaînage de workflows | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| subagents | TECHNOLOGIE | observé_dans | répertoire .claude/agents/ | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| subagents | TECHNOLOGIE | utilise | MCP Tools | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| subagents | TECHNOLOGIE | utilise | agentId | CONCEPT | 0.90 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI | AJOUT |
| subagents | TECHNOLOGIE | définition | Assistants IA spécialisés avec context window séparé | AJOUT |
| Plan subagent | TECHNOLOGIE | rôle | Sous-agent natif Claude Code pour le plan mode | AJOUT |
| plan mode | METHODOLOGIE | définition | Mode non-exécution pour planification et recherche codebase | AJOUT |
| MCP Tools | TECHNOLOGIE | catégorie | Outils Model Context Protocol accessibles aux subagents | AJOUT |
| agentId | CONCEPT | rôle | Identifiant unique permettant reprise de session subagent | AJOUT |
