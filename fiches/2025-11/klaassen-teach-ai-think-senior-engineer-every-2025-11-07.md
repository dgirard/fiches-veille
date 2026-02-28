# klaassen-teach-ai-think-senior-engineer-every-2025-11-07

## Veille
8 stratégies planification IA - Research agents parallèles - Codebase grounding - Git history - Vibe prototyping - Style agents - Compounding engineering - Every Source Code - Kieran Klaassen

## Titre Article
Teach Your AI to Think Like a Senior Engineer

## Date
2025-11-07

## URL
https://every.to/source-code/teach-your-ai-think-like-a-senior-engineer

## Keywords
planning strategies, research agents, parallel operations, Cora email bankruptcy, reproduce and document, best practices grounding, codebase grounding, libraries grounding, git history, vibe prototyping, synthesis with options, style review agents, compounding engineering, institutional memory, CLAUDE.md, docs knowledge base, AppSignal logs, RubyLLM gem, EmailClassifier, event tracking, specialized reviewers

## Authors
Kieran Klaassen (General Manager, Cora)

## Ton
**Profil:** Practitioner-Tutorial-Advanced | Première personne praticien | Prescriptive-Systematic | Expert

Klaassen adopte experienced practitioner voice sharing concrete tactical playbook suite article précédent philosophical. Structure 8-strategy framework (reproduce → best practices → codebase → libraries → git → vibe → synthesize → review) demonstrates systematic thinking typical senior engineer. Langage hands-on engineer (AppSignal logs, RubyLLM gem, helper methods, denormalizing, pull requests) grounded in Cora production examples creates credibility. Tone prescriptive-confident ("You can avoid building the wrong thing, too") reflects mastery. Direct GitHub links et open-sourced planning system shows commitment open knowledge sharing. Emphasis "how to make this compound" after each strategy reinforces central thesis knowledge accumulation. Typique Every Source Code advanced tutorials (Klaassen, Dan Shipper technical pieces) visant practitioner audience ready implement immediately vs conceptual understanding.

## Pense-bêtes
- **Suite article précédent** : Stop Coding and Start Planning (2025-11-06)
- **Core thesis** : parallel research operations teach AI how you think faster than sequential human planning
- **8 planning strategies** selon fidelity levels (One: quick fixes, Two: clear scope, Three: uncertain requirements)

**Strategy 1: Reproduce and document**
- Fidelity: One & Two, bug fixes
- Agent job: step-by-step reproduction guide
- Example Cora: 19 users stuck email bankruptcy, AppSignal logs revealed rate limit errors swallowed, silent failures
- Compound: updated @kieran-rails-reviewer checklist "background jobs calling external APIs - handle rate limits?"

**Strategy 2: Ground in best practices**
- Fidelity: All, especially unfamiliar patterns
- Agent: @agent-best-practices-researcher
- Use cases: technical architecture, copywriting, pricing research, upgrade paths
- Example: gem upgrade 2 versions behind, found official guide + 3 blog posts with edge cases, 3min saved hours debugging
- Compound: save findings to docs/*.md (pay-gem-upgrades.md, pricing-research.md), agent checks docs first before web

**Strategy 3: Ground in your codebase**
- Fidelity: Anything duplicating existing functionality
- Agent job: search existing code for related implementations
- Example: event tracking feature, agent found forgotten existing tracking system with helper methods
- Compound: created @event-tracking-expert agent distilling all tracking patterns, runs automatically on features needing tracking

**Strategy 4: Ground in your libraries**
- Fidelity: Fast-moving or poorly documented libraries
- Agent job: analyze source code to understand capabilities
- Example: RubyLLM gem updates constantly, docs lag, agent read source found v1.9 streaming support undocumented
- Compound: knowledge auto-updates every dependency update, never stale information

**Strategy 5: Study git history**
- Fidelity: Refactors, continuing work, understanding "why"
- Agent job: research past decisions and context
- Example: EmailClassifier v1 vs v2, agent found 3-month-old PR showing v2 upgrade attempted, broke edge cases, deliberately rolled back
- Compound: institutional memory preserved searchable, new team members inherit reasoning

**Strategy 6: Vibe prototype for clarity**
- Fidelity: Three, UX uncertainty, exploratory
- Agent job: quickly build throwaway versions to interact with
- Example: Brief interface redesign, 5 prototypes 5min each, user feedback "archive button top-left - muscle memory from Gmail"
- Compound: vibe coding turns uncertainty into concrete specifications, user reactions documented

**Strategy 7: Synthesize with options**
- Fidelity: End research phase before implementation
- Agent job: present 2-3 solution paths with honest pros/cons
- Example: Gmail inbox sync, 3 options (bolt onto existing/real-time/mirror caching), tradeoffs (fast messy/clean slow/work upfront best long-term)
- Compound: choice reveals preferences ("I prefer widely supported over cutting-edge"), codified for future similar decisions

**Strategy 8: Review with style agents**
- Fidelity: Final planning step before implementation
- Agent job: catch misalignments with coding style and architecture
- Three review agents:
  - Simplification: flags over-engineering
  - Security: checks vulnerabilities
  - Kieran-style: personal preferences (simple queries vs complex joins, denormalizing)
- Compound: agents accumulate taste over time, every "I don't like this" makes system smarter

**Getting started practical guide** :
- Pick Fidelity Two feature (multi-file, clear scope)
- 15-20min research: best practices (web), patterns (codebase), library capabilities (docs/source)
- AI synthesize: problem (1 sentence), 2-3 approaches (pros/cons), existing patterns match, edge cases/security
- Review reactions: capture "too complex" or "better way" - write down WHY
- Ship feature, compare implementation vs plan, note divergences
- Codify 1 learning: add to CLAUDE.md ("When X, check Y" or "Prefer A over B because C")
- Create specialized agents: Event Tracking Expert, Security Checker
- Repeat: next week reference notes, second plan better than first

**Open-sourced** : Every's GitHub marketplace, /plan slash command + research agents ready to use

## RésuméDe400mots

Kieran Klaassen présente les 8 stratégies concrètes transformant la philosophie de planification en systèmes opérationnels pour enseigner à l'IA comment penser comme un senior engineer. Suite de son article précédent sur l'importance de planning vs vibe coding, ce guide tactique détaille comment exécuter parallel research operations plus rapides que planification humaine séquentielle.

**Framework des 8 stratégies**

**1. Reproduce and document** : Avant de fixer bugs, reproduire et documenter. Exemple Cora email bankruptcy : 19 users bloqués, agent loop AppSignal logs → rate limit errors swallowed silently. Saved from guessing. Compounding : updated @kieran-rails-reviewer checklist permanent.

**2. Ground in best practices** : @agent-best-practices-researcher cherche web comment autres ont résolu. Use cases : architecture, copywriting, pricing, upgrades. Gem upgrade 2 versions behind : 3min research found official guide + 3 blog posts edge cases, prevented hours debugging. Compounding : save findings docs/*.md, agent checks local docs first.

**3. Ground in codebase** : Chercher patterns existants avant recréer. Event tracking feature : agent found forgotten existing system avec helper methods. Prevented building second incompatible system. Compounding : @event-tracking-expert agent distills all patterns, runs automatically.

**4. Ground in libraries** : Fast-moving libs mal documentées, read source code. RubyLLM gem : agent discovered v1.9 streaming support undocumented mais présent dans test suite. Compounding : auto-updates à chaque dependency update.

**5. Study git history** : Comprendre "why" past decisions. EmailClassifier upgrade : agent found 3-month-old PR showing v2 attempted, broke edge cases (inbox→archive, archive→inbox inverted), deliberately rolled back detailed reasoning. 5min search prevented reintroducing debugged bug. Compounding : institutional memory preserved searchable.

**6. Vibe prototype for clarity** : Fidelity Three, UX uncertain. Brief interface : 5 prototypes 5min each, user feedback concrete ("archive button top-left - Gmail muscle memory"). Prototypes deleted, knowledge into plan. Compounding : uncertainty → concrete specifications documented.

**7. Synthesize with options** : Combine all research into 2-3 approaches avec honest tradeoffs. Gmail sync : Option A (bolt existing - fast messy), B (real-time - clean slow), C (mirror cache - work upfront best long-term). Agent research, human judgment. Compounding : choices reveal preferences codified ("prefer widely supported over cutting-edge").

**8. Review with style agents** : 3 specialized reviewers final pass. Simplification agent (flags over-engineering), Security agent (vulnerabilities), Kieran-style agent (personal preferences: simple queries vs complex joins, denormalizing). Compounding : accumulate taste over time.

**Cas email bankruptcy révélateur** : Initially thought easy ("bulk archive 53k emails - how hard?"). Research agent 20min revealed reality check : Gmail rate limits kill at 2k, system timeouts, long user wait. Simple feature became 3-day architectural challenge. Planning saved from building wrong thing entirely.

**Practical implementation** : Pick Fidelity Two feature → 15-20min research (best practices web + codebase patterns + library capabilities) → AI synthesize plan (problem/approaches/patterns/edge cases) → review reactions capture WHY → ship → compare implementation vs plan → codify 1 learning CLAUDE.md → create specialized agents → repeat next week.

**Open-source contribution** : Klaassen open-sourced planning system Every's GitHub marketplace avec /plan slash command et research agents prêts à utiliser. Philosophy : don't build from scratch, adapt existing proven systems.

Chaque stratégie includes "How to make this compound" demonstrating central thesis : parallel research operations teach AI institutional knowledge accumulating faster than human sequential planning.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Kieran Klaassen | PERSONNE | a_créé | Compounding Engineering | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Kieran Klaassen | PERSONNE | gère | Cora | TECHNOLOGIE | 0.98 | DYNAMIQUE | déclaré_article |
| Kieran Klaassen | PERSONNE | publie_dans | Every | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Compounding Engineering | METHODOLOGIE | est_basé_sur | opérations de recherche parallèles | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| opérations de recherche parallèles | CONCEPT | remplace | planification séquentielle humaine | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | est_utilisé_par | Kieran Klaassen | PERSONNE | 0.97 | DYNAMIQUE | déclaré_article |
| Cora | TECHNOLOGIE | utilise | Gmail API | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Gmail API | TECHNOLOGIE | impose | limite de débit à 2000 emails | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| AppSignal | TECHNOLOGIE | permet | diagnostic logs production | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| RubyLLM | TECHNOLOGIE | est_utilisé_par | Cora | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| CLAUDE.md | TECHNOLOGIE | codifie | préférences architecturales | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| mémoire institutionnelle | CONCEPT | est_préservée_par | git history | TECHNOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| vibe coding | METHODOLOGIE | transforme | incertitudes UX en spécifications | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Every | ORGANISATION | héberge | planning system open-source | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Kieran Klaassen | PERSONNE | rôle | General Manager de Cora | AJOUT |
| Every | ORGANISATION | secteur | Media / Outils IA | AJOUT |
| Cora | TECHNOLOGIE | catégorie | Produit email géré par Every | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI | AJOUT |
| AppSignal | TECHNOLOGIE | catégorie | Système de tracking d'erreurs production | AJOUT |
| RubyLLM | TECHNOLOGIE | catégorie | Gem Ruby pour appels API LLM | AJOUT |
| Gmail API | TECHNOLOGIE | contrainte | Rate limit 2000 emails par batch | AJOUT |
| Compounding Engineering | METHODOLOGIE | principe | Chaque feature améliore le système pour la suivante | AJOUT |
| opérations de recherche parallèles | CONCEPT | avantage | Plus rapide que planification séquentielle humaine | AJOUT |
| mémoire institutionnelle | CONCEPT | mécanisme | Git history + agents spécialisés + docs/*.md | AJOUT |
| CLAUDE.md | TECHNOLOGIE | usage | Codifier préférences et règles de l'ingénieur | AJOUT |
| vibe coding | METHODOLOGIE | usage | Prototypage rapide jetable pour clarifier les exigences | AJOUT |
