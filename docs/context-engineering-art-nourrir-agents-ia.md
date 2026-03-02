# Context Engineering — L'art de nourrir les agents IA

> De mai 2025 à février 2026, une discipline nouvelle s'est cristallisée : le context engineering. Retour sur ses fondations, son architecture et les principes qui redéfinissent le métier de développeur.

## Le paradoxe du prompt vide

Aristidis Vasilopoulos a observé un chiffre contre-intuitif au terme de [283 sessions avec des agents de codage IA](../fiches/2026-02/vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24.md) : **80 % des prompts font moins de 100 mots**. Pas parce que les développeurs sont paresseux. Parce que tout le travail a été fait en amont. Le contexte est déjà là — chargé, structuré, prêt à être consommé par l'agent.

La plupart des développeurs font l'inverse. Ils rédigent de longs prompts ad-hoc, répètent les mêmes instructions, décrivent à chaque session l'architecture de leur projet. Ils font du prompt engineering artisanal quand le vrai levier se trouve ailleurs : dans tout ce qui arrive *avant* le prompt.

C'est précisément ce que le context engineering adresse.

## Qu'est-ce que le Context Engineering ?

Le context engineering est l'ensemble des pratiques, architectures et outils qui permettent de fournir aux agents IA le contexte nécessaire pour travailler efficacement sur des codebases complexes. Il ne s'agit plus de formuler la bonne question — il s'agit de construire le système qui rend n'importe quelle question productive.

La distinction avec le prompt engineering est fondamentale. Le prompt engineering optimise une interaction. Le context engineering optimise l'environnement dans lequel toutes les interactions se déroulent. On passe de l'artisanat du prompt à l'ingénierie du système de contexte.

Rod Johnson (créateur de Spring Framework) a proposé dès juillet 2025 le [framework DICE](../fiches/2025-07/context-engineering-domain-understanding-johnson-2025-07-23.md) pour formaliser cette idée : le *domain understanding* — la compréhension structurée du domaine métier — constitue la fondation sur laquelle l'agent peut raisonner. Sans cette fondation, même le modèle le plus puissant produit du code générique qui ignore les conventions, les contraintes et l'histoire du projet.

## Les trois couches du contexte

L'une des contributions les plus structurantes vient de [Vasilopoulos](../fiches/2026-02/vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24.md), qui a identifié empiriquement une architecture à trois niveaux. Chaque couche correspond à un type de mémoire et à une fréquence d'accès différente.

### Layer 1 — Constitution (Hot Memory)

C'est le contexte toujours chargé. Le fichier `CLAUDE.md` (ou `AGENTS.md`) qui définit les conventions du projet, les patterns architecturaux, les règles de nommage, le style de code. Ce contexte est injecté à chaque interaction sans que le développeur ait à le redemander.

Boris Cherny, créateur de Claude Code chez Anthropic, a montré que ce fichier unique [transforme la productivité dès le premier jour](../fiches/2026-02/cherny-yc-lightcone-claude-code-origin-story-2026-02.md). Google a suivi la même logique avec [Conductor pour Gemini CLI](../fiches/2025-12/google-conductor-context-driven-development-gemini-cli-2025-12-17.md) : un fichier de contexte projet qui pilote le comportement de l'agent.

Le principe est simple : **une constitution basique améliore l'output immédiatement**. Pas besoin d'un système élaboré pour commencer.

### Layer 2 — Agents spécialisés (Warm Memory)

Ce sont les skills, subagents et agents experts invoqués à la demande. Anthropic a lancé les [Agent Skills](../fiches/2025-10/agent-skills-anthropic-2025-10-16.md) en octobre 2025 — des compétences modulaires et réutilisables qu'un agent peut mobiliser selon le contexte. Jesse Vincent a théorisé le [système Superpowers/Skills](../fiches/2025-10/superpowers-skills-coding-agents-vincent-2025-10-09.md) : des capacités que l'agent acquiert progressivement.

Jude Gao (Vercel) a démontré un résultat surprenant : dans les évaluations agents, [un simple fichier `AGENTS.md` bien rédigé surpasse des skills complexes](../fiches/2026-01/gao-vercel-agents-md-outperforms-skills-evals-2026-01-27.md). La clarté des instructions l'emporte sur la sophistication technique.

Les [subagents de Claude Code](../fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29.md) illustrent cette couche : des assistants spécialisés (exploration de code, exécution de tests, revue de sécurité) délégués par l'agent principal, chacun avec son propre contexte ciblé.

### Layer 3 — Knowledge Base (Cold Memory)

C'est le savoir de fond : spécifications détaillées, knowledge graphs, documentation des sous-systèmes. Ce contexte est tiré à la demande, typiquement via MCP (Model Context Protocol), le protocole standard de connexion entre outils et agents publié par Anthropic.

Netflix a montré la voie dès juin 2025 avec son [architecture UDA](../fiches/2025-06/netflix-uda-unified-data-architecture-knowledge-graph-2025-06-12.md) (Unified Data Architecture) : un knowledge graph en RDF/SHACL qui sert de socle sémantique à l'ensemble de la plateforme. Foundation Capital a théorisé les [Context Graphs](../fiches/2025-12/gupta-garg-context-graphs-trillion-dollar-opportunity-2025-12-22.md) comme la nouvelle génération de systèmes de record — une opportunité qu'ils qualifient de "trillion-dollar".

L'idée est que la connaissance structurée du domaine (ontologies, graphes de relations, specs formalisées) constitue un capital qui s'apprécie avec le temps.

## Le Context Flywheel — quand le contexte compose

Patrick Debois (Tessl), connu pour avoir inventé le terme DevOps, a identifié un mécanisme fondamental qu'il nomme le [*Context Flywheel*](../fiches/2026-02/debois-tessl-context-flywheel-ai-coding-teams-2026-02-26.md) — le volant d'inertie contextuel :

1. **Documenter le contexte** (conventions, décisions, patterns)
2. **Les agents produisent mieux** grâce à ce contexte
3. **L'output enrichit le contexte** (nouvelles specs, leçons apprises)
4. **Le contexte compose et accélère** — chaque itération rend la suivante plus efficace

C'est une boucle vertueuse. Debois a formalisé le [CDLC (Context Development Lifecycle)](../fiches/2026-02/debois-tessl-context-development-lifecycle-ai-coding-agents-2026-02-19.md) en quatre phases pour structurer ce cycle. L'idée centrale : le contexte documenté n'est pas un coût, c'est un investissement qui compose.

Sam Schillace (Microsoft) a décrit le même phénomène sous l'angle des équipes : les [*compounding teams*](../fiches/2025-09/compounding-teams-schillace-2025-09-28.md) sont celles qui capitalisent systématiquement sur leur contexte accumulé. L'effet multiplicateur ne vient pas de développeurs plus rapides, mais d'un contexte partagé plus riche.

Dan Shipper et Kieran Klaassen (Every) ont traduit ces principes en méthodologie opérationnelle avec le [Compound Engineering](../fiches/2025-12/shipper-klaassen-compound-engineering-every-agents-2025-12-11.md) : un processus en quatre étapes — **Plan, Work, Assess, Compound** — où la dernière étape (Compound) consiste explicitement à extraire et documenter les apprentissages pour enrichir le contexte. Ce n'est pas optionnel : c'est la quatrième étape du workflow, aussi importante que les trois premières.

## Spec-Driven vs Vibe Coding : le spectre des pratiques

Trois approches coexistent aujourd'hui, et elles se distinguent par la quantité et la structure du contexte fourni à l'agent.

Le **Vibe Coding** — terme popularisé par Andrej Karpathy — consiste à prompter l'agent avec des instructions minimales et ad-hoc. C'est efficace pour le prototypage rapide, mais génère une dette technique importante. Le contexte est éphémère : il disparaît à chaque nouvelle session.

Le **Spec-Driven Development** structure le contexte sous forme de spécifications. [AWS Kiro](../fiches/2025-07/aws-kiro-specification-driven-agentic-ide-forbes-2025-07-15.md), lancé en juillet 2025, incarne cette approche avec un IDE agentique entièrement piloté par les specs. [Addy Osmani](../fiches/2026-01/osmani-how-write-good-spec-ai-agents-2026-01-13.md) (Google) a publié cinq principes pour écrire des spécifications efficaces pour agents IA, insistant sur la clarté, la testabilité et la décomposition.

Le **Codified Context** va plus loin : il combine constitution (CLAUDE.md), agents spécialisés (skills/subagents) et knowledge base pour créer un environnement de contexte permanent et évolutif. C'est l'approche qui permet la cohérence à long terme et le compounding.

Kieran Klaassen a formulé le principe de manière lapidaire : [**"Stop Coding, Start Planning"**](../fiches/2025-11/klaassen-stop-coding-start-planning-every-2025-11-06.md). Planifier ne sert pas seulement le développeur — planifier enseigne au *système*. Un plan bien structuré est du contexte que l'agent peut consommer, mémoriser et réutiliser.

## Les outils et protocoles du Context Engineering

### CLAUDE.md et AGENTS.md

Le fichier de constitution projet est devenu la brique élémentaire. `CLAUDE.md` définit les conventions pour Claude Code. `AGENTS.md` fait de même pour d'autres agents. Ces fichiers sont simples — du markdown — mais leur impact est disproportionné. Ils transforment un agent générique en agent spécialiste du projet.

### MCP (Model Context Protocol)

Publié par Anthropic, MCP standardise la connexion entre agents et outils externes. Il permet à un agent d'interroger des bases de données, des API, des systèmes de fichiers de manière uniforme. Microsoft a publié ["MCP for Beginners"](../fiches/2025-07/mcp-for-beginners-microsoft-developer-youtube-2025-07-28.md) en juillet 2025, signe que le protocole s'impose comme standard de facto.

[MCP-UI](../fiches/2025-08/mcp-ui-future-agentic-interfaces-goose-2025-08-25.md) (porté par Goose/Block, puis [Monday.com](../fiches/2025-10/mcp-ui-conference-monday-liad-yosef-2025-10.md)) étend le concept au visuel : les agents peuvent générer des composants d'interface web via une architecture en îlots (*islands*) et un DOM distant. Le contexte ne circule plus seulement sous forme de texte — il devient interactif.

### Skills et Subagents

Les [Skills d'Anthropic](../fiches/2025-10/agent-skills-anthropic-2025-10-16.md) sont des compétences modulaires qu'un agent peut acquérir et réutiliser. [Simon Willison](../fiches/2025-10/claude-skills-bigger-than-mcp-willison-2025-10-16.md) les a comparés à MCP et a prédit une "explosion cambrienne" de skills spécialisés. Les [subagents de Claude Code](../fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29.md) poussent la logique plus loin : l'agent principal délègue des tâches à des agents spécialisés (exploration, tests, revue de code), chacun opérant dans un contexte dédié.

Boris Cherny a décrit [son workflow personnel](../fiches/2026-01/nunez-cherny-claude-code-workflow-venturebeat-2026-01-05.md) : cinq agents parallèles, chacun avec sa spécialité, orchestrés via CLAUDE.md. C'est le context engineering appliqué au quotidien.

### Knowledge Graphs

Le contexte sémantique — relations entre entités, ontologies métier, graphes de connaissances — représente la forme la plus riche de contexte. Tony Seale a théorisé le ["noyau ontologique"](../fiches/2025-05/seale-philosophy-eats-ai-ontological-core-2025-05-30.md) dès mai 2025 : la philosophie (la sémantique formalisée) guide l'IA mieux que n'importe quel prompt. Netflix l'a démontré avec son [architecture UDA](../fiches/2025-06/netflix-uda-unified-data-architecture-knowledge-graph-2025-06-12.md), Foundation Capital l'a [chiffré comme opportunité de marché](../fiches/2025-12/gupta-garg-context-graphs-trillion-dollar-opportunity-2025-12-22.md).

## Ce que 283 sessions nous apprennent

L'[étude de Vasilopoulos](../fiches/2026-02/vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24.md) est la plus détaillée à ce jour sur l'impact du contexte codifié. Ses conclusions méritent d'être listées :

1. **Une constitution basique améliore l'output dès le jour 1.** Pas besoin de perfection pour commencer.
2. **Les explications répétées signalent le besoin de créer une spec.** Si vous expliquez la même chose deux fois, c'est un signal : documentez-le.
3. **Les specs obsolètes sont le principal mode de défaillance.** Un contexte périmé est pire que pas de contexte du tout.
4. **Le contexte documenté compose.** Chaque sous-système documenté accélère les features adjacentes.
5. **Le cache hit rate est la métrique clé.** En production, la capacité de l'agent à réutiliser du contexte déjà chargé détermine la performance et le coût. L'équipe de Claude Code a montré que le [prompt caching réduit les coûts de 90 %](../fiches/2026-02/lancemartin-anthropic-prompt-auto-caching-claude-2026-02.md).

Ces principes convergent vers une même conclusion : le contexte est un actif, pas une dépense.

## L'ingénieur de demain est un ingénieur du contexte

En moins d'un an — de mai 2025 à février 2026 — le context engineering est passé de concept émergent à discipline structurée. Il possède désormais ses architectures (3 couches), ses protocoles (MCP), ses méthodologies (CDLC, Compound Engineering), ses outils (CLAUDE.md, Skills, subagents) et ses métriques (cache hit rate, taux de réutilisation des specs).

Le métier de développeur évolue. Il ne s'agit plus seulement d'écrire du code — il s'agit de structurer le contexte pour que les agents écrivent le bon code. L'expertise se déplace : de la syntaxe vers la sémantique, du prompt vers le système, de l'interaction vers l'architecture.

Le point de départ est accessible à tous : créer un fichier `CLAUDE.md` à la racine de son projet, y décrire les conventions, observer les patterns, documenter les décisions. Puis laisser le volant d'inertie faire son travail.

---

*Article basé sur l'analyse de 34 fiches de veille couvrant la période mai 2025 — février 2026.*

## Références

| # | Fiche | Auteur | Date |
|---|-------|--------|------|
| 1 | [Infrastructure contexte codifié : architecture 3 tiers, 283 sessions](../fiches/2026-02/vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24.md) | Vasilopoulos | 2026-02 |
| 2 | [Context Engineering — DICE Framework](../fiches/2025-07/context-engineering-domain-understanding-johnson-2025-07-23.md) | Rod Johnson | 2025-07 |
| 3 | [Genèse de Claude Code](../fiches/2026-02/cherny-yc-lightcone-claude-code-origin-story-2026-02.md) | Boris Cherny | 2026-02 |
| 4 | [Conductor — context-driven development Gemini CLI](../fiches/2025-12/google-conductor-context-driven-development-gemini-cli-2025-12-17.md) | Google | 2025-12 |
| 5 | [Agent Skills Anthropic](../fiches/2025-10/agent-skills-anthropic-2025-10-16.md) | Anthropic | 2025-10 |
| 6 | [Superpowers/Skills — apprentissage continu agents](../fiches/2025-10/superpowers-skills-coding-agents-vincent-2025-10-09.md) | Jesse Vincent | 2025-10 |
| 7 | [AGENTS.md surpasse les skills dans les évals](../fiches/2026-01/gao-vercel-agents-md-outperforms-skills-evals-2026-01-27.md) | Jude Gao / Vercel | 2026-01 |
| 8 | [Subagents Claude Code](../fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29.md) | Anthropic | 2025-09 |
| 9 | [Architecture données unifiée Netflix — knowledge graph](../fiches/2025-06/netflix-uda-unified-data-architecture-knowledge-graph-2025-06-12.md) | Netflix | 2025-06 |
| 10 | [Context Graphs — trillion-dollar opportunity](../fiches/2025-12/gupta-garg-context-graphs-trillion-dollar-opportunity-2025-12-22.md) | Foundation Capital | 2025-12 |
| 11 | [Context Flywheel — avantage compétitif par le contexte](../fiches/2026-02/debois-tessl-context-flywheel-ai-coding-teams-2026-02-26.md) | Patrick Debois | 2026-02 |
| 12 | [Context Development Lifecycle (CDLC)](../fiches/2026-02/debois-tessl-context-development-lifecycle-ai-coding-agents-2026-02-19.md) | Patrick Debois | 2026-02 |
| 13 | [Compounding teams — effet multiplicateur](../fiches/2025-09/compounding-teams-schillace-2025-09-28.md) | Sam Schillace | 2025-09 |
| 14 | [Compound Engineering — Plan, Work, Assess, Compound](../fiches/2025-12/shipper-klaassen-compound-engineering-every-agents-2025-12-11.md) | Shipper & Klaassen | 2025-12 |
| 15 | [AWS Kiro — IDE agentique spec-driven](../fiches/2025-07/aws-kiro-specification-driven-agentic-ide-forbes-2025-07-15.md) | AWS | 2025-07 |
| 16 | [5 principes pour écrire des specs agents IA](../fiches/2026-01/osmani-how-write-good-spec-ai-agents-2026-01-13.md) | Addy Osmani | 2026-01 |
| 17 | [Stop Coding, Start Planning](../fiches/2025-11/klaassen-stop-coding-start-planning-every-2025-11-06.md) | Kieran Klaassen | 2025-11 |
| 18 | [MCP for Beginners](../fiches/2025-07/mcp-for-beginners-microsoft-developer-youtube-2025-07-28.md) | Microsoft | 2025-07 |
| 19 | [MCP-UI — interfaces agentiques](../fiches/2025-08/mcp-ui-future-agentic-interfaces-goose-2025-08-25.md) | Goose / Block | 2025-08 |
| 20 | [MCP-UI conférence Monday.com](../fiches/2025-10/mcp-ui-conference-monday-liad-yosef-2025-10.md) | Liad Yosef | 2025-10 |
| 21 | [Claude Skills vs MCP — explosion cambrienne](../fiches/2025-10/claude-skills-bigger-than-mcp-willison-2025-10-16.md) | Simon Willison | 2025-10 |
| 22 | [Workflow 5 agents parallèles Claude Code](../fiches/2026-01/nunez-cherny-claude-code-workflow-venturebeat-2026-01-05.md) | Boris Cherny | 2026-01 |
| 23 | [Noyau ontologique — la philosophie mange l'IA](../fiches/2025-05/seale-philosophy-eats-ai-ontological-core-2025-05-30.md) | Tony Seale | 2025-05 |
| 24 | [Auto-caching prompts Claude — économies 90 %](../fiches/2026-02/lancemartin-anthropic-prompt-auto-caching-claude-2026-02.md) | Lance Martin | 2026-02 |
