# Knowledge Base — Context Engineering

> 34 fiches | Période : Mai 2025 — Février 2026 | Généré le 2026-03-02

## Vue d'ensemble

Cette KB thématique couvre le **Context Engineering** : l'ensemble des pratiques, architectures et outils permettant de fournir aux agents IA le contexte nécessaire pour travailler efficacement sur des codebases complexes. Le sujet englobe les spécifications, le prompt caching, les skills/subagents, MCP, les knowledge graphs, et les méthodologies de planification.

## Chronologie

### 2025 — Fondations

- **Mai 2025** — Tony Seale théorise le noyau ontologique : la philosophie (sémantique formalisée) guide l'IA
- **Juin 2025** — Netflix publie l'architecture UDA : knowledge graph RDF/SHACL comme socle sémantique
- **Juil. 2025** — Rod Johnson propose le framework DICE pour le domain understanding des LLM
- **Juil. 2025** — AWS lance Kiro, IDE agentique spec-driven
- **Juil. 2025** — Microsoft publie "MCP for Beginners"
- **Août 2025** — MCP-UI émerge (Goose/Block) : interfaces agentiques avec composants web
- **Sep. 2025** — Pragmatic Engineer détaille l'architecture de Claude Code
- **Sep. 2025** — Anthropic documente les subagents Claude Code
- **Sep. 2025** — Sam Schillace théorise les compounding teams
- **Oct. 2025** — Jesse Vincent publie la méthodologie agents de codage + système Superpowers/Skills
- **Oct. 2025** — Anthropic lance Agent Skills ; Simon Willison analyse Skills vs MCP
- **Oct. 2025** — Stanford publie ACE (Agentic Context Engineering)
- **Oct. 2025** — Liad Yosef (Monday.com) présente MCP-UI en conférence
- **Nov. 2025** — Kieran Klaassen publie "Stop Coding, Start Planning" + "Teach AI to Think Like a Senior Engineer"
- **Déc. 2025** — Dan Shipper & Kieran Klaassen publient "Compound Engineering" : boucle Plan-Work-Assess-Compound + plugin 12 subagents
- **Déc. 2025** — Google lance Conductor (context-driven development pour Gemini CLI)
- **Déc. 2025** — Foundation Capital théorise les Context Graphs comme nouvelle génération de systèmes de record

### 2026 — Maturité

- **Jan. 2026** — Boris Cherny révèle son workflow (5 agents parallèles, CLAUDE.md)
- **Jan. 2026** — Addy Osmani publie les 5 principes pour écrire des specs agents IA
- **Jan. 2026** — Jude Gao (Vercel) démontre que AGENTS.md surpasse les skills dans les évals
- **Fév. 2026** — Boris Cherny raconte la genèse de Claude Code + publie 10 conseils
- **Fév. 2026** — BMAD : méthode d'urbanisme pour l'IA agentique dans le SDLC
- **Fév. 2026** — @trq212 et Lance Martin publient les leçons prompt caching Claude Code
- **Fév. 2026** — Patrick Debois théorise le CDLC et le Context Flywheel
- **Fév. 2026** — Vasilopoulos publie l'évaluation empirique la plus détaillée : architecture 3 tiers, 283 sessions

## Fiches sources

### Core Context Engineering

- [[fiches/2026-02/vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24\|Infrastructure contexte codifié : architecture 3 tiers, mémoire persistante, 283 sessions, MCP]]
- [[fiches/2026-02/debois-tessl-context-development-lifecycle-ai-coding-agents-2026-02-19\|Context Development Lifecycle (CDLC) — cycle d'ingénierie du contexte pour agents de codage IA]]
- [[fiches/2026-02/debois-tessl-context-flywheel-ai-coding-teams-2026-02-26\|Volant d'inertie contextuel — avantage compétitif des équipes IA par le contexte cumulé]]
- [[fiches/2025-10/ace-agentic-context-engineering-stanford-2025-10-07\|Ingénierie de contexte agentique - Auto-amélioration LLM - Architecture réflexive - Stanford]]
- [[fiches/2025-07/context-engineering-domain-understanding-johnson-2025-07-23\|Context Engineering - Domain Understanding - DICE - Rod Johnson]]

### Prompt Caching & Context Windows

- [[fiches/2026-02/trq212-anthropic-claude-code-prompt-caching-lessons-2026-02\|Leçons prompt caching Claude Code : architecture cache, plan mode, compaction]]
- [[fiches/2026-02/lancemartin-anthropic-prompt-auto-caching-claude-2026-02\|Auto-caching prompts Claude : mécanisme technique, API cache_control, économies 90% tokens]]

### Context-Driven Platforms

- [[fiches/2025-12/gupta-garg-context-graphs-trillion-dollar-opportunity-2025-12-22\|Context Graphs Foundation Capital - nouvelle génération systèmes de record pour agents IA]]
- [[fiches/2025-12/google-conductor-context-driven-development-gemini-cli-2025-12-17\|Conductor Google - extension Gemini CLI développement piloté par le contexte]]
- [[fiches/2025-12/memodb-acontext-context-data-platform-agents-2025-12-11\|Acontext: Context Data Platform for Cloud-Native AI Agents]]

### Specs & Plans pour agents IA

- [[fiches/2026-01/osmani-how-write-good-spec-ai-agents-2026-01-13\|Addy Osmani - écrire specs pour agents IA, 5 principes, Plan Mode, PRD structuré]]
- [[fiches/2026-01/gao-vercel-agents-md-outperforms-skills-evals-2026-01-27\|AGENTS.md surpasse les skills dans les évaluations agents Vercel/Next.js]]
- [[fiches/2025-07/aws-kiro-specification-driven-agentic-ide-forbes-2025-07-15\|AWS Kiro - Agentic IDE - Specification-driven - Vibe coding vs Spec coding]]
- [[fiches/2026-02/martin-bmad-method-urbanisme-ia-agentique-sdlc-2026-02-04\|Méthode BMAD : cadre structuré pour intégrer l'IA agentique dans le SDLC]]

### Skills, Subagents & Agent Architecture

- [[fiches/2025-10/agent-skills-anthropic-2025-10-16\|Agent Skills d'Anthropic, compétences modulaires réutilisables, portabilité cross-product]]
- [[fiches/2025-10/claude-skills-bigger-than-mcp-willison-2025-10-16\|Claude Skills vs MCP - Simplicité élégante - Explosion cambrienne prédite]]
- [[fiches/2025-10/claude-skills-document-manipulation-willison-2025-10-10\|Système de compétences Claude - Manipulation documents - Simon Willison]]
- [[fiches/2025-10/superpowers-skills-coding-agents-vincent-2025-10-09\|Superpowers/Skills - Apprentissage continu agents IA]]
- [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - AI assistants spécialisés - Context management]]

### MCP (Model Context Protocol)

- [[fiches/2025-10/mcp-ui-conference-monday-liad-yosef-2025-10\|MCP-UI conférence détaillée, islands architecture, remote DOM, theming]]
- [[fiches/2025-08/mcp-ui-future-agentic-interfaces-goose-2025-08-25\|MCP-UI révolutionne interfaces agents IA, composants web interactifs]]
- [[fiches/2025-09/mcp-replaces-browser-logrocket-2025-09-15\|MCP remplace le navigateur - Interactions agents IA]]
- [[fiches/2025-07/mcp-for-beginners-microsoft-developer-youtube-2025-07-28\|MCP for Beginners - Model Context Protocol - Microsoft Developer]]

### Claude Code — Architecture & Workflow

- [[fiches/2025-09/how-claude-code-is-built-pragmatic-engineer-2025-09-15\|Construction de Claude Code - Architecture AI-first - Pragmatic Engineer]]
- [[fiches/2026-02/cherny-yc-lightcone-claude-code-origin-story-2026-02\|Boris Cherny raconte la genèse de Claude Code - Y Combinator Light Cone]]
- [[fiches/2026-02/cherny-claude-code-10-tips-team-x-2026-02-01\|Conseils utilisation Claude Code par équipe Anthropic - 10 astuces productivité]]
- [[fiches/2026-01/nunez-cherny-claude-code-workflow-venturebeat-2026-01-05\|Boris Cherny workflow 5 agents parallèles, Opus 4.5, CLAUDE.md]]

### Méthodologie & Planning

- [[fiches/2025-10/coding-agents-methodology-vincent-2025-10-05\|Méthodologie d'utilisation agents IA pour développement - Workflow multi-sessions]]
- [[fiches/2025-11/klaassen-stop-coding-start-planning-every-2025-11-06\|Planification vs Vibe Coding - Compounding Engineering - Three Fidelities]]
- [[fiches/2025-11/klaassen-teach-ai-think-senior-engineer-every-2025-11-07\|8 stratégies planification IA - Research agents parallèles - Codebase grounding]]

### Compound Engineering

- [[fiches/2025-12/shipper-klaassen-compound-engineering-every-agents-2025-12-11\|Compound Engineering : processus 4 étapes (Plan, Work, Assess, Compound) - Every]]

### Knowledge, Ontologie & Compounding

- [[fiches/2025-09/compounding-teams-schillace-2025-09-28\|Équipes à effet multiplicateur - Développement IA récursif - Productivité exponentielle]]
- [[fiches/2025-05/seale-philosophy-eats-ai-ontological-core-2025-05-30\|Philosophie mange l'IA : noyau ontologique entreprise, sémantique métier, knowledge graph]]
- [[fiches/2025-06/netflix-uda-unified-data-architecture-knowledge-graph-2025-06-12\|Architecture données unifiée Netflix, knowledge graph RDF/SHACL, modélisation domaine]]

## Entités clés

### Concepts fondamentaux

- [[kb/contexte\|Contexte]] — Le matériau premier du développement agentique
- [[kb/Context-Flywheel\|Context Flywheel]] — Volant d'inertie : le contexte documenté compose
- [[kb/Context-Development-Lifecycle\|Context Development Lifecycle]] — CDLC 4 phases (Debois)
- [[kb/_entites-mineures#noyau-ontologique\|Noyau ontologique]] — Sémantique métier formalisée en ontologie (Seale)
- [[kb/compounding-teams\|Compounding teams]] — Équipes à effet multiplicateur (Schillace)
- [[kb/CLAUDE.md\|CLAUDE.md]] — Fichier de contexte projet pour Claude Code
- [[kb/_entites-mineures#AGENTS.md\|AGENTS.md]] — Alternative/complément aux skills (Gao/Vercel)

### Technologies et protocoles

- [[kb/Claude-Code\|Claude Code]] — Agent CLI terminal-first, architecture de référence
- [[kb/Model-Context-Protocol\|Model Context Protocol (MCP)]] — Protocole de connexion outils-agents
- [[kb/MCP-UI\|MCP-UI]] — Extensions UI pour MCP (islands architecture, remote DOM)
- [[kb/Claude-Skills\|Claude Skills]] — Compétences modulaires réutilisables
- [[kb/subagents\|Subagents]] — Assistants IA spécialisés délégués
- [[kb/Plan-mode\|Plan mode]] — Mode planification structurée avant exécution
- [[kb/_entites-mineures#DPROD\|DPROD]] — Spécification ouverte pour data products sémantiques
- [[kb/_entites-mineures#Conductor\|Conductor]] — Context-driven development pour Gemini CLI
- [[kb/Kiro\|Kiro]] — IDE agentique spec-driven (AWS)

### Personnes clés

- [[kb/Boris-Cherny\|Boris Cherny]] — Créateur Claude Code, architecture et workflow
- [[kb/_entites-mineures#Patrick-Debois\|Patrick Debois]] — CDLC, Context Flywheel (Tessl)
- [[kb/_entites-mineures#Aristidis-Vasilopoulos\|Aristidis Vasilopoulos]] — Évaluation empirique contexte codifié 3 tiers
- [[kb/Jesse-Vincent\|Jesse Vincent]] — Méthodologie agents, Superpowers/Skills
- [[kb/Simon-Willison\|Simon Willison]] — Analyse Skills vs MCP, explosion cambrienne
- [[kb/Addy-Osmani\|Addy Osmani]] — 5 principes specs pour agents IA
- [[kb/_entites-mineures#Rod-Johnson\|Rod Johnson]] — Framework DICE, domain understanding
- [[kb/Kent-Beck\|Kent Beck]] — Vibe Coding vs TDD, augmented coding
- [[kb/_entites-mineures#Kieran-Klaassen\|Kieran Klaassen]] — Three Fidelities, compounding engineering
- [[kb/_entites-mineures#Sam-Schillace\|Sam Schillace]] — Compounding teams
- [[kb/_entites-mineures#Lance-Martin\|Lance Martin]] — Auto-caching, developer advocacy Anthropic
- [[kb/_entites-mineures#@trq212\|@trq212]] — Prompt caching lessons, équipe Claude Code

### Organisations

- [[kb/Anthropic\|Anthropic]] — Claude Code, Skills, MCP, subagents
- [[kb/Google\|Google]] — Conductor, Gemini CLI
- [[kb/_entites-mineures#Stanford-University\|Stanford]] — ACE framework
- [[kb/_entites-mineures#Tessl\|Tessl]] — CDLC, Context Flywheel (Patrick Debois)
- [[kb/_entites-mineures#Every\|Every]] — Compounding engineering (Klaassen)

## Architecture conceptuelle

### Les 3 couches du Context Engineering

```
┌─────────────────────────────────────────────────┐
│  LAYER 3 — Knowledge Base (Cold Memory)         │
│  Specs à la demande, knowledge graphs,          │
│  documentation subsystèmes (via MCP)            │
│  → Vasilopoulos Tier 3, Context Graphs,         │
│    Netflix UDA, Acontext                         │
├─────────────────────────────────────────────────┤
│  LAYER 2 — Agents spécialisés (Warm Memory)     │
│  Skills, subagents, agents domain experts       │
│  → Anthropic Skills, Superpowers, AGENTS.md,    │
│    Vasilopoulos Tier 2                          │
├─────────────────────────────────────────────────┤
│  LAYER 1 — Constitution (Hot Memory)            │
│  CLAUDE.md, conventions, patterns, routing      │
│  → Toujours chargé, Vasilopoulos Tier 1,       │
│    CLAUDE.md, Conductor                         │
└─────────────────────────────────────────────────┘
```

### Le Context Flywheel (Debois)

```
Documenter le contexte
  → Les agents produisent mieux
    → L'output enrichit le contexte
      → Le contexte compose et accélère
        → (boucle vertueuse)
```

### Spec-Driven vs Vibe Coding

| Approche | Contexte fourni | Résultat |
|----------|----------------|----------|
| Vibe Coding | Minimal, prompt ad-hoc | Prototypage rapide, dette technique |
| Spec-Driven | Spécifications structurées | Qualité, maintenabilité, reproductibilité |
| Codified Context | Constitution + agents + KB | Cohérence long terme, compounding |

### Principes clés extraits des fiches

1. **Une constitution basique améliore l'output dès le jour 1** (Vasilopoulos)
2. **Les explications répétées signalent le besoin de créer une spec** (Vasilopoulos)
3. **Les specs obsolètes sont le principal mode de défaillance** (Vasilopoulos)
4. **Le contexte documenté compose** : chaque sous-système accélère les features adjacentes (Debois, Vasilopoulos)
5. **AGENTS.md surpasse les skills** dans les évaluations agents (Gao/Vercel)
6. **Plans teach systems** — planifier enseigne au système, pas seulement au développeur (Klaassen)
7. **Le cache hit rate est la métrique la plus importante** pour un agent en production (@peakji/Manus)
8. **80% des prompts < 100 mots** quand le contexte est pré-chargé (Vasilopoulos)
