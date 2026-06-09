# subagents

> **Type** : TECHNOLOGIE | 12 relations | 2 fiches sources

## Attributs

- **définition** : Assistants IA spécialisés avec context window séparé
- **usage** : Délégation de calcul intensif, maintien de la fenêtre de contexte principale

## Relations (comme sujet)

### améliore

- [[kb/_entites-mineures#préservation-du-contexte\|préservation du contexte]] (CONCEPT) — 0.95, ATEMPOREL
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - Assistants IA spécialisés - Gestion du contexte - Délégation de tâches - Documentation Anthropic]]

### observé_dans

- [[kb/_entites-mineures#répertoire-.claude-agents\|répertoire .claude/agents/]] (TECHNOLOGIE) — 0.98, STATIQUE
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - Assistants IA spécialisés - Gestion du contexte - Délégation de tâches - Documentation Anthropic]]

### permet

- [[kb/_entites-mineures#Contexte-propre-isolé\|Contexte propre isolé]] (CONCEPT) — 0.93, ATEMPOREL
  - [[fiches/2026-04/thariq-claude-code-session-management-1m-context-2026-04-14\|Gestion de sessions Claude Code : fenêtre 1M tokens, compaction, rewind, subagents et pourriture de contexte]]
- [[kb/_entites-mineures#chaînage-de-workflows\|chaînage de workflows]] (CONCEPT) — 0.92, ATEMPOREL
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - Assistants IA spécialisés - Gestion du contexte - Délégation de tâches - Documentation Anthropic]]
- [[kb/_entites-mineures#parallélisation-des-workstreams\|parallélisation des workstreams]] (CONCEPT) — 0.88, ATEMPOREL
  - [[fiches/2026-05/salesforce-tallapragada-how-engineering-became-agentic-2026-05-27\|Billet de blog officiel **Salesforce News** (rubrique *Agentic Enterprise*, série *« Pioneering the Agentic Shift Within Salesforce Engineering »*), publié le **27 mai 2026** (6 min de lecture) par **Srinivas « Srini » Tallapragada**, *President and Chief Engineering and Customer Success Officer* de Salesforce. Suite directe d'un premier billet (*« How we got our engineers to use AI — without breaking everything »*) qui racontait le passage de **>90% d'adoption**. **Thèse-pivot** : Salesforce Engineering est passé d'un monde où l'IA était un *copilote* utile à un monde où des **outils agentiques pilotent le cycle de vie logiciel (SDLC) lui-même** — écriture de code, revue de PRs, génération de tests, mise à jour de doc, gestion des déploiements, coordination du travail jadis confié à des handoffs humains. **Décision-signal canonique** : standardisation org-wide sur **Claude Code** + ***« we removed all token limits »*** — *« remove every last piece of friction between our engineers and the tools that make them faster and more effective »*. **Résultat empirique majeur** (avril 2026 vs avril 2025) : work items complétés par développeur **+50,8%**, PRs mergées par développeur **+79%**, et surtout **Effective Output score** (mesure ML de la **valeur réelle du code livré**, pas le volume) **+151,3% en glissement annuel**. **Cas d'usage emblématique** : migration de **33 endpoints API** vers une architecture cloud-native, estimée **~231 person-days** (7 par API) en traditionnel, réalisée en **13 jours = 18× plus vite** — via un **framework rule-based en Claude** (fichiers markdown + reference implementations), feedback des PRs réinjecté en continu dans le rule set, **boucles LLM autonomes (build, fix, validate)** sans intervention manuelle, parallélisées sur environnements isolés → **5 PRs**, la plus grosse livrant **21 endpoints avec 100% de couverture de tests**. **Pas de tradeoff vitesse↔qualité** : via la plateforme **Engineering 360** (centralise les données d'ingénierie de centaines de systèmes), **les incidents totaux baissent de 5%** malgré la hausse des PRs (*« quality doesn't suffer from speed. It benefits from it »*), grâce à des **guardrails de sécurité et standards qualité encastrés structurellement** dans le workflow agentique (Trust = valeur n°1). **Refonte du SDLC** : une fois l'IA adoptée, les ingénieurs **détruisent et reconstruisent** les workflows (quels process supprimer ? quels handoffs inutiles ? où l'humain fait-il encore un travail qu'un agent peut posséder ?). **Nouveau craft d'ingénierie** : les **Claude Code skills** (capacités packagées/réutilisables encodant contexte d'équipe, conventions de nommage, patterns) deviennent un **artefact d'ingénierie** partagé et composable ; **AI Expert Suite** + **Salesforce Foundation Plugins** = bibliothèque curatée institutionnalisée de skills (benchmark interne : **précision et fiabilité en hausse, coût inutile réduit**) ; **subagents & agent teams** parallélisent les workstreams (*« They describe the outcome, and a set of coordinated agents figures out the steps »*). **Ce qui reste dur** : (1) **gestion du contexte** en sessions longues — la **qualité des fichiers CLAUDE.md** varie beaucoup et pèse fort sur la qualité de sortie ; (2) **sécurité agentique** = modèle fondamentalement différent (agents qui *agissent*, pas seulement *suggèrent* → blast radius accru) ; (3) **évolution des rôles** (comment les juniors deviennent seniors si l'IA absorbe le travail entry-level ? rôle du designer/PM ? l'unité d'exécution = scrum team → expérimentations d'unités à 1 ou 3 personnes). Conclusion : *« It changed what was economically possible »* ; ambition affichée = **« the most automated, agentic SDLC in the industry »**. Recoupe directement Gupta (*cost of a completed outcome*, marginal token utility), Greenwald/Sierra (outcome-based pricing), DORA (ROI / coût par feature) et le débat BFM/Girard (token = fuel de valeur, pas coût à couper).]]

### utilise

- [[kb/_entites-mineures#context-window-séparé\|context window séparé]] (CONCEPT) — 0.98, ATEMPOREL
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - Assistants IA spécialisés - Gestion du contexte - Délégation de tâches - Documentation Anthropic]]
- [[kb/_entites-mineures#fichiers-Markdown-YAML-frontmatter\|fichiers Markdown YAML frontmatter]] (TECHNOLOGIE) — 0.97, STATIQUE
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - Assistants IA spécialisés - Gestion du contexte - Délégation de tâches - Documentation Anthropic]]
- [[kb/_entites-mineures#MCP-Tools\|MCP Tools]] (TECHNOLOGIE) — 0.93, DYNAMIQUE
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - Assistants IA spécialisés - Gestion du contexte - Délégation de tâches - Documentation Anthropic]]
- [[kb/_entites-mineures#agentId\|agentId]] (CONCEPT) — 0.90, STATIQUE
  - [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - Assistants IA spécialisés - Gestion du contexte - Délégation de tâches - Documentation Anthropic]]

## Relations (comme objet)

- [[kb/Claude-Code\|Claude Code]] **utilise** → subagents — 0.99
- [[kb/Boris-Cherny\|Boris Cherny]] **utilise** → subagents — 0.95
- [[kb/Compound-Engineering\|compound engineering]] **utilise** → subagents — 0.95

## Fiches sources

- [[fiches/2026-02/cherny-claude-code-10-tips-team-x-2026-02-01\|Conseils utilisation Claude Code par équipe Anthropic - 10 astuces productivité]]
- [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - Assistants IA spécialisés - Gestion du contexte - Délégation de tâches - Documentation Anthropic]]
