# subagents

> **Type** : CONCEPT | 14 relations | 4 fiches sources

## Attributs

- **définition** : Agents délégués avec leur propre fenêtre de contexte propre
- **usage** : Délégation de calcul intensif, maintien de la fenêtre de contexte principale

## Relations (comme sujet)

### améliore

- [[kb/_entites-mineures#préservation-du-contexte\|préservation du contexte]] (CONCEPT) — 0.95, ATEMPOREL
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - AI assistants spécialisés - Context management - Task delegation - Documentation Anthropic]]

### offre

- [[kb/_entites-mineures#Contexte-propre-isolé\|Contexte propre isolé]] (CONCEPT) — 0.93, ATEMPOREL
  - [[fiches/2026-04/thariq-claude-code-session-management-1m-context-2026-04-14\|Gestion de sessions Claude Code : fenêtre 1M tokens, compaction, rewind, subagents et pourriture de contexte]]

### parallélisent

- [[kb/_entites-mineures#workstreams\|workstreams]] (CONCEPT) — 0.88, ATEMPOREL
  - [[fiches/2026-05/salesforce-tallapragada-how-engineering-became-agentic-2026-05-27\|Billet de blog officiel **Salesforce News** (rubrique *Agentic Enterprise*, série *« Pioneering the Agentic Shift Within Salesforce Engineering »*), publié le **27 mai 2026** (6 min de lecture) par **Srinivas « Srini » Tallapragada**, *President and Chief Engineering and Customer Success Officer* de Salesforce. Suite directe d'un premier billet (*« How we got our engineers to use AI — without breaking everything »*) qui racontait le passage de **>90% d'adoption**. **Thèse-pivot** : Salesforce Engineering est passé d'un monde où l'IA était un *copilote* utile à un monde où des **outils agentiques pilotent le cycle de vie logiciel (SDLC) lui-même** — écriture de code, revue de PRs, génération de tests, mise à jour de doc, gestion des déploiements, coordination du travail jadis confié à des handoffs humains. **Décision-signal canonique** : standardisation org-wide sur **Claude Code** + ***« we removed all token limits »*** — *« remove every last piece of friction between our engineers and the tools that make them faster and more effective »*. **Résultat empirique majeur** (avril 2026 vs avril 2025) : work items complétés par développeur **+50,8%**, PRs mergées par développeur **+79%**, et surtout **Effective Output score** (mesure ML de la **valeur réelle du code livré**, pas le volume) **+151,3% en glissement annuel**. **Cas d'usage emblématique** : migration de **33 endpoints API** vers une architecture cloud-native, estimée **~231 person-days** (7 par API) en traditionnel, réalisée en **13 jours = 18× plus vite** — via un **framework rule-based en Claude** (fichiers markdown + reference implementations), feedback des PRs réinjecté en continu dans le rule set, **boucles LLM autonomes (build, fix, validate)** sans intervention manuelle, parallélisées sur environnements isolés → **5 PRs**, la plus grosse livrant **21 endpoints avec 100% de couverture de tests**. **Pas de tradeoff vitesse↔qualité** : via la plateforme **Engineering 360** (centralise les données d'ingénierie de centaines de systèmes), **les incidents totaux baissent de 5%** malgré la hausse des PRs (*« quality doesn't suffer from speed. It benefits from it »*), grâce à des **guardrails de sécurité et standards qualité encastrés structurellement** dans le workflow agentique (Trust = valeur n°1). **Refonte du SDLC** : une fois l'IA adoptée, les ingénieurs **détruisent et reconstruisent** les workflows (quels process supprimer ? quels handoffs inutiles ? où l'humain fait-il encore un travail qu'un agent peut posséder ?). **Nouveau craft d'ingénierie** : les **Claude Code skills** (capacités packagées/réutilisables encodant contexte d'équipe, conventions de nommage, patterns) deviennent un **artefact d'ingénierie** partagé et composable ; **AI Expert Suite** + **Salesforce Foundation Plugins** = bibliothèque curatée institutionnalisée de skills (benchmark interne : **précision et fiabilité en hausse, coût inutile réduit**) ; **subagents & agent teams** parallélisent les workstreams (*« They describe the outcome, and a set of coordinated agents figures out the steps »*). **Ce qui reste dur** : (1) **gestion du contexte** en sessions longues — la **qualité des fichiers CLAUDE.md** varie beaucoup et pèse fort sur la qualité de sortie ; (2) **sécurité agentique** = modèle fondamentalement différent (agents qui *agissent*, pas seulement *suggèrent* → blast radius accru) ; (3) **évolution des rôles** (comment les juniors deviennent seniors si l'IA absorbe le travail entry-level ? rôle du designer/PM ? l'unité d'exécution = scrum team → expérimentations d'unités à 1 ou 3 personnes). Conclusion : *« It changed what was economically possible »* ; ambition affichée = **« the most automated, agentic SDLC in the industry »**. Recoupe directement Gupta (*cost of a completed outcome*, marginal token utility), Greenwald/Sierra (outcome-based pricing), DORA (ROI / coût par feature) et le débat BFM/Girard (token = fuel de valeur, pas coût à couper).]]

### permettent

- [[kb/_entites-mineures#chaînage-de-workflows\|chaînage de workflows]] (CONCEPT) — 0.92, ATEMPOREL
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - AI assistants spécialisés - Context management - Task delegation - Documentation Anthropic]]

### peuvent_être_repris_via

- [[kb/_entites-mineures#agentId\|agentId]] (CONCEPT) — 0.90, STATIQUE
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - AI assistants spécialisés - Context management - Task delegation - Documentation Anthropic]]

### possèdent

- [[kb/_entites-mineures#context-window-séparé\|context window séparé]] (CONCEPT) — 0.98, ATEMPOREL
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - AI assistants spécialisés - Context management - Task delegation - Documentation Anthropic]]

### sont_configurés_via

- [[kb/_entites-mineures#fichiers-Markdown-YAML-frontmatter\|fichiers Markdown YAML frontmatter]] (TECHNOLOGIE) — 0.97, STATIQUE
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - AI assistants spécialisés - Context management - Task delegation - Documentation Anthropic]]

### spécialisent

- [[kb/_entites-mineures#code-simplifier,-verify-app\|code-simplifier, verify-app]] (METHODOLOGIE) — 0.90, DYNAMIQUE
  - [[fiches/2026-01/nunez-cherny-claude-code-workflow-venturebeat-2026-01-05\|Boris Cherny créateur Claude Code - workflow 5 agents parallèles, Opus 4.5, CLAUDE.md]]

### stockés_dans

- [[kb/_entites-mineures#.claude-agents\|.claude/agents/]] (TECHNOLOGIE) — 0.98, STATIQUE
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - AI assistants spécialisés - Context management - Task delegation - Documentation Anthropic]]

## Relations (comme objet)

- [[kb/Claude-Code\|Claude Code]] **supporte** → subagents — 0.99
- [[kb/Claude-Code\|Claude Code]] **délègue_tâches_à** → subagents — 0.98
- [[kb/Boris-Cherny\|Boris Cherny]] **utilise** → subagents — 0.95
- [[kb/Compound-Engineering\|compound engineering]] **utilise** → subagents — 0.95
- [[kb/_entites-mineures#MCP-Tools\|MCP Tools]] **accessibles_par** → subagents — 0.93

## Fiches sources

- [[fiches/2026-02/cherny-claude-code-10-tips-team-x-2026-02-01\|Conseils utilisation Claude Code par équipe Anthropic - 10 astuces productivité]]
- [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - AI assistants spécialisés - Context management - Task delegation - Documentation Anthropic]]
- [[fiches/2026-04/thariq-claude-code-session-management-1m-context-2026-04-14\|Gestion de sessions Claude Code : fenêtre 1M tokens, compaction, rewind, subagents et pourriture de contexte]]
- [[fiches/2025-10/wu-cherny-use-claude-code-builders-every-2025-10-29\|Claude Code - Cat Wu & Boris Cherny - Antfooding - Plan Mode - Subagents - Slash Commands - Stop Hooks - Settings.json - Dangerous Mode - AI & I Podcast - Every]]
