# Knowledge Base — Context Engineering

> 90 fiches | Période : Mai 2025 — Août 2026 | Généré le 2026-08-15

## Vue d'ensemble

Cette KB thématique couvre le **Context Engineering** : l'ensemble des pratiques, architectures et outils permettant de fournir aux agents IA le contexte nécessaire pour travailler efficacement sur des codebases complexes. Le sujet englobe les spécifications, le prompt caching, les skills/subagents, MCP, les knowledge graphs, et les méthodologies de planification.

Le printemps 2026 voit émerger deux sous-thèmes majeurs : le **harness engineering** (équation `agent = modèle + harnais` — Trivedy, Böckeler, Osmani, OpenAI/Codex), qui déplace l'ingénierie du prompt vers l'environnement complet de l'agent, et le **contexte en fichiers** (design.md, doctrine PROJ-AI, formats de sortie HTML vs Markdown), qui généralise le pattern CLAUDE.md/AGENTS.md à la design system, à la gouvernance projet et aux artefacts de revue.

**L'été 2026 fait passer le sujet du contexte au cycle.** Le contexte bien fourni
ne suffit plus à qualifier une pratique : ce qui distingue les corpus sérieux de
juin-août, c'est qu'ils décrivent un **cycle instrumenté** avec des étapes
nommées, des gates entre elles et des compteurs dessus. Quatre déplacements :

1. **Le goulot n'a jamais été la génération, c'est la vérification.** La
   formule est de SFEIR (« la génération est une bouche large, la vérification
   un col étroit ») ; Anthropic la documente en chiffres (Claude écrit ~80 % du
   code fusionné, et c'est l'étape **Test** qui a dû être reconstruite, pas le
   *coding*) ; Williams en fait le principe d'architecture de l'**ADLC**
   (« replace trust with structure, and structure with measurement »).
2. **La revue de code devient adversariale, et sort des gates humains.** Charter
   des agents pour **réfuter**, en fenêtres de contexte séparées, et n'agir que
   sur des findings reproduits par un test rouge (Williams, « Prosecution, Not
   Code Review ») ; ne jamais laisser l'auteur du code écrire les tests qui le
   valident — *« vous avez construit un miroir, pas un anneau »* (SFEIR). Le
   mode d'échec le mieux documenté de la période est celui de Dumortier : un
   vérificateur en **monde clos certifie ce qu'il ignore**, d'où l'interdiction
   du « pass » nu et l'obligation de déclarer sa propre couverture.
3. **Le contexte se durcit en exécutable.** Lassiège : *« Ce qui compte doit
   être exécutable. Une consigne est suivie "la plupart du temps"… Un hook ou un
   test est suivi tout le temps. »* Même logique dans le *tool-locking* de
   hyperresearch (un patcheur verrouillé à `[Read, Edit]` **ne peut
   physiquement pas** réécrire), dans le principe du cliquet (« toute échappée
   devient une contrainte ») et dans l'AST déterministe de graphify.
4. **Le coût devient une dimension de conception, pas une conséquence.** Le
   *Token Manifesto* (« You don't have a prompt problem. You have a
   context-window problem ») ; les benchmarks Block, qui montrent qu'au-delà
   d'un seuil *« payer plus cesse d'aider, puis commence à nuire »* et qu'entre
   les six meilleurs runs **5,5× d'écart de prix pour 8,9 pts** fait du choix
   « une décision de budget, pas de qualité » ; et le principe ADLC selon lequel
   un cycle sain voit son **coût par changement fusionné baisser à chaque run**
   (« flat cost is failure »).

**Deux résultats négatifs, rares et précieux**, publiés par des acteurs sans
intérêt à le faire : sur des tâches courtes, **aucune composition d'équipe
d'agents ne bat l'agent solo** à prix égal (Block, Terminal-Bench 2.1) — le
gain n'apparaît qu'à horizon long ; et le run le plus cher n'est pas le
meilleur (Opus 5 *xhigh* : 140,63 $ pour 75,0 %, sous six runs moins chers,
par sur-raisonnement et timeouts).

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
- **Fév. 2026** — Kieran Klaassen publie le guide définitif du Compound Engineering : boucle 7 étapes, plugin 40+ agents
- **Fév. 2026** — OpenAI révèle le harness engineering de Codex : 1M lignes de code sans écriture manuelle, ingénierie d'environnement agent-first
- **Fév. 2026** — @trq212 et Lance Martin publient les leçons prompt caching Claude Code
- **Fév. 2026** — Patrick Debois théorise le CDLC et le Context Flywheel
- **Fév. 2026** — Vasilopoulos publie l'évaluation empirique la plus détaillée : architecture 3 tiers, 283 sessions

### 2026 — Outillage mémoire

- **Mars 2026** — Artem Zhutov démontre QMD (Tobias Lütke) + skill /recall : moteur de recherche local BM25/sémantique/hybride remplace grep pour mémoire persistante agents

### 2026 — Harness engineering & contexte en fichiers (mars — juin)

- **Mars 2026** — Trivedy (LangChain) formalise l'anatomie du harnais : Agent = Modèle + Harnais
- **Mars 2026** — Mornati expérimente BMAD en 1 jour : le développeur devient superviseur d'agents
- **Mars 2026** — Compound Engineering v2.60 durcit le pipeline plan→work→review (scoring de confiance, revue obligatoire)
- **Avr. 2026** — Birgitta Böckeler (Thoughtworks) théorise le harness engineering : guides feedforward, capteurs feedback
- **Avr. 2026** — Jesse Vincent publie le framework Superpowers sur GitHub : skills agentiques + méthodologie TDD
- **Avr. 2026** — Thariq Shihipar documente la gestion de sessions Claude Code : fenêtre 1M tokens, compaction, rewind, pourriture de contexte
- **Avr. 2026** — Tony Seale pose la symétrie (modèle + harnais) ↔ (ontologie + données) : l'ontologie comme seul actif non-commodité
- **Avr. 2026** — Addy Osmani consolide la doctrine du harness engineering : principe du ratchet ("chaque erreur devient une règle"), Harness-as-a-Service
- **Avr. 2026** — Anthropic publie le post-mortem qualité Claude Code : trois incidents caching/reasoning/prompt
- **Avr. 2026** — Ryan Law (Ahrefs) industrialise le content engineering : ~23 skills orchestrées, drafts en 6-12 minutes
- **Mai 2026** — Jessica Talisman rafraîchit l'Ontology Pipeline : gouvernance continue + partenariat IA (augment vs replace)
- **Mai 2026** — Lattice formalise les skills composables Atoms/Molecules/Refiners : "living context over static config"
- **Mai 2026** — Antoine Habert (WEnvision) formalise PROJ-AI : un repo, un agent, une doctrine markdown
- **Mai 2026** — Google design.md : "l'âme du design" dans un fichier transmissible aux agents (Meng To × Isenberg)
- **Mai 2026** — Shihipar propose HTML comme format de sortie par défaut des agents, à la place de Markdown
- **Mai 2026** — Thoughtworks lance AI/works : Super Spec et plateforme de développement agentique spec-driven
- **Mai 2026** — Jaya Gupta (Token Budget Wars) : les decision traces capturées pour le FinOps deviennent un context graph
- **Juin 2026** — Shihipar capitalise les leçons skills d'Anthropic : taxonomie 9 catégories, "le file system entier est du context engineering"

### 2026 — Le cycle agentique (juin — août)

- **12 juin 2026** — **Chris Williams** publie la série **ADLC** en sept volets :
  le SDLC humain défend contre des modes de défaillance humains, absents des
  LLM ⇒ erreur de catégorie. Huit phases (P0 Triage → P7 Distill), gates
  déterministes entre chacune, **exactement deux moments humains** (approbation
  de spec, acceptation comportementale), tests comme spécification, revue
  reconfigurée en *prosecution*, trois cadrans pour paralléliser sans merge
  hell, et une phase Distill qui fait **baisser le coût à chaque run**.
- **16 juin 2026** — Skill **grill-with-docs** (Matt Pocock) : interview
  adversariale d'un plan d'archi contre le vocabulaire métier, capture inline
  dans `CONTEXT.md` + ADR.
- **21-26 juin 2026** — Le **loop engineering** se formalise côté produit :
  Shubham Saboo (« la prochaine compétence n'est pas le prompt engineering »,
  boucle à 5 parties dont la *condition d'arrêt*) puis **Andrew Ng** (trois
  boucles imbriquées par échelle de temps : codage ~minutes, feedback
  développeur ~heures, feedback externe ~jours).
- **2 juil. 2026** — Kieran Klaassen documente le **Compounding Knowledge
  Lifecycle** : anatomie d'une *learning* (`docs/solutions/`), carte mémoire
  durable/éphémère, récupération **grep-first**, trois contre-forces pour que
  la mémoire ne mente pas.
- **3 juil. 2026** — **Field Guide to Fable** (Shihipar) : « la carte n'est pas
  le territoire » — la qualité du travail est plafonnée par la capacité à
  clarifier les **inconnues** ; quatre quadrants et une boîte à outils ordonnée
  avant / pendant / après l'implémentation. Willison relaie le corollaire :
  **laisser le modèle exercer son jugement** et déléguer les petites tâches à
  des modèles moins puissants qu'il choisit lui-même.
- **8 juil. 2026** — **Réécriture de Bun de Zig vers Rust en 11 jours** pilotée
  par Claude (Jarred Sumner) : portage mécanique validé par une suite de tests
  **écrite en TypeScript, donc indépendante du langage** (60 624 tests, 0
  supprimé), ~50 dynamic workflows, jusqu'à **64 Claude en parallèle**, 6 502
  commits, ~165 000 $ de tokens. Méthode : **revue adversariale à contexte
  séparé** et « corriger le processus qui génère le code, pas le code ».
- **15-17 juil. 2026** — Le rôle bouge : l'architecte passe d'**Oracle** à
  **amplificateur d'intelligence** (SFEIR/Hohpe, DDD comme garde-fou) ; Boris
  Cherny publie les **Steps of AI Adoption** (5 étapes, ~1 → ~1 000 agents ;
  « consommer plus de tokens ne fait pas monter d'un cran — il faut casser le
  prochain goulot ET bâtir le prochain jeu de garde-fous ») ; Cherny & Cat Wu
  posent la fusion produit/ingénierie, que les commentaires reformulent :
  **livrer devient bon marché**, la valeur se déplace vers le jugement.
- **17 juil. 2026** — **The Token Manifesto** (Martignole) : pastiche du
  Manifeste Agile où l'unité de valeur est le **token**. « You don't have a
  prompt problem. You have a context-window problem. »
- **20 juil. 2026** — Skill **ADHD** (Akhouri) : idéation divergente parallèle —
  N agents isolés sous frames cognitifs distordus puis un critique séparé ;
  correctif **architectural**, pas un prompt, à la convergence prématurée.
- **21-26 juil. 2026** — **Anthropic publie son SDLC AI-native sécurisé**
  (Jason Clinton) : Claude écrit ~80 % du code fusionné, trois menaces
  cadrantes, un principe par étape, l'étape **Test** identifiée comme le goulot
  et reconstruite (16 % → 54 % de PR commentées), agents IR **sans droit de
  déployer**, routage SIEM de chaque action d'agent. Relecture SFEIR : sans
  cycle nommé, ni gains, ni ancrage sécurité, ni politique FinOps token, ni
  rien à mesurer.
- **22 juil. 2026** — **SDLC vs PDLC** (SFEIR) : cycles emboîtés, pas
  concurrents. L'IA comprimant le SDLC, le goulot remonte vers la **discovery**
  ; un SDLC augmenté devient **norme de marché, pas différenciateur**.
- **28 juil. 2026** — **Usine logicielle solo** (Hugo Lassiège) : code « quasi
  100 % généré », six couches outillées répondant à trois questions — que sait
  l'agent, que sait-il faire de façon déterministe, **qu'est-ce qui l'arrête
  quand il se trompe**. Rare section « À améliorer » : impossible de mesurer
  l'obsolescence d'une règle.
- **30 juil. 2026** — **L'anneau de contraintes** (SFEIR d'après Osmani) : la
  qualité a changé d'adresse — elle se lit dans l'anneau autour de l'agent, pas
  dans le code. Review **instrumente**, Ship **décide** ; piège nommé de la
  **validation circulaire**.
- **2-6 août 2026** — La couche protocolaire se range : la spécification
  **Agent Client Protocol** s'affiche (v1/v2, Zed *et* JetBrains, registry,
  RFDs) ; Didier Girard démêle les **trois ACP** et pose « on n'indexe jamais un
  sigle seul » ; **Agent Plugins 1.0.0** normalise l'**emballage** des skills et
  serveurs MCP (« The core problem isn't the components. It's the manifest »),
  avec Google rejoignant Amazon, Cursor, Microsoft, OpenAI et Vercel comme Core
  Maintainer — **sans Anthropic**, alors que les deux briques empaquetées sont
  d'origine Anthropic.
- **3-6 août 2026** — Deux skills structurantes : **hyperresearch** (Gibbs) —
  routeur mince + 20 skills chargées fraîches, *« patch, never regenerate »*,
  tool-locking, gates de citation ; et **graphify** (Shamsi) — codebase → graphe
  interrogeable par **AST tree-sitter déterministe**, chaque arête étiquetée
  `EXTRACTED`/`INFERRED`, **pas d'index vectoriel**, « LLM credits : 0 ».
- **3 août 2026** — **Notion as Code** (alpha) : l'infra-as-code appliquée à
  l'espace documentaire — script idempotent sans identifiants, table de
  correspondance `resourceId → RecordPointer`, SDK explicitement écrit pour
  *« you or your coding agent »*.
- **6 août 2026** — **Benchmarks Buzz** (Block) : douze compositions d'équipes
  testées ; **aucune ne bat le solo** sur tâches courtes, +12,4 pts sur horizon
  long. Taxonomie QuickBee / WorkerBee / SmartBee, escalade **vers un
  coordinateur, pas vers l'humain** — *« the human stops being middleware »*.
- **12 août 2026** — **Le vérificateur qui certifie son ignorance** (Dumortier) :
  quatre couches (Vérité, Production, Vérification, Distribution) ; un
  fact-checker rend un « pass » sur une affirmation que ses sources ne
  couvraient pas. Correctif : **interdire le « pass » nu**, obliger le
  vérificateur à déclarer sa propre couverture — *« "je ne peux pas vérifier
  ceci" est un résultat de première classe »*.
- **12 août 2026** — **Desktop vs web** (rapport interne) : mêmes modèles des
  deux côtés, le gain est **de friction, pas de puissance** — et l'app desktop
  devient *« un runtime d'agents avec accès à la machine »*, ce qui déplace la
  frontière de confiance. Sept chiffres largement repris sont **non
  confirmés** : la fragilité des sources est ici l'information.

## Fiches sources

### ADLC — le cycle refondé sur les modes de défaillance des modèles (Williams, juin 2026)

- [[fiches/2026-06/williams-adlc-1-models-arent-human-2026-06-12\|1. Stop Running the SDLC on Models That Aren't Human — 8 modes de défaillance (F1-F8), 5 propriétés exploitables (E1-E5)]]
- [[fiches/2026-06/williams-adlc-2-two-human-gates-2026-06-12\|2. Two Human Gates and Everything Between Is Machine-Checked — 8 phases P0→P7, coûts « en haltère »]]
- [[fiches/2026-06/williams-adlc-3-tests-are-the-spec-2026-06-12\|3. Tests Are the Spec — rail discipline, gel au niveau de l'outil, mutation testing plutôt que couverture]]
- [[fiches/2026-06/williams-adlc-4-prosecution-not-code-review-2026-06-12\|4. Prosecution, Not Code Review — reviewers mono-lentille à contextes frais, findings vérifiés par test rouge]]
- [[fiches/2026-06/williams-adlc-5-three-dials-parallel-agents-2026-06-12\|5. Three Dials — coût / temps mural / précision ; « control flow is code; judgment is models »]]
- [[fiches/2026-06/williams-adlc-6-lifecycle-gets-cheaper-2026-06-12\|6. The Lifecycle That Gets Cheaper Every Run — phase Distill, lesson foundry, « flat cost is failure »]]
- [[fiches/2026-06/williams-adlc-7-built-with-the-lifecycle-2026-06-12\|7. The ADLC Toolkit — doctrine « frontier-free », cinq substitutions, generator-verifier gap]]

### SDLC augmenté, revue adversariale & gouvernance

- [[fiches/2026-07/clinton-anthropic-secure-ai-native-sdlc-2026-07-21\|How Anthropic secures its AI-native SDLC (Clinton) : ~80 % du code écrit par Claude, un principe par étape, SIEM sur les actions d'agents]]
- [[fiches/2026-07/sfeir-anthropic-sdlc-ai-native-securise-2026-07-26\|Le cycle redevient le socle (SFEIR) : sans SDLC, ni gains, ni ancrage sécurité, ni FinOps token, ni mesure]]
- [[fiches/2026-07/sfeir-code-review-anneau-contraintes-2026-07-30\|L'anneau de contraintes autour des agents : Review instrumente, Ship décide ; validation circulaire et cliquet]]
- [[fiches/2026-07/sfeir-sdlc-pdlc-articulation-2026-07-22\|SDLC vs PDLC : cycles emboîtés, goulot déplacé vers la discovery, spécifications exécutables]]
- [[fiches/2026-07/sfeir-architecte-ere-ia-2026-07-15\|Le rôle de l'architecte à l'ère de l'IA : d'Oracle à amplificateur d'intelligence, DDD comme garde-fou]]
- [[fiches/2026-08/dumortier-marketing-ai-os-verification-2026-08-12\|Le vérificateur en monde clos certifie ce qu'il ignore : interdire le « pass » nu, déclarer sa couverture]]

### Usines logicielles & boucles

- [[fiches/2026-07/lassiege-usine-logicielle-heure-ia-2026-07-28\|Mon usine logicielle à l'heure de l'IA (Lassiège) : six couches, « ce qui compte doit être exécutable »]]
- [[fiches/2026-07/sumner-bun-rewrite-rust-claude-2026-07-08\|Rewriting Bun in Rust : 11 jours, 64 Claude en parallèle, tests indépendants du langage comme oracle]]
- [[fiches/2026-06/saboo-loop-engineering-product-managers-2026-06-21\|Loop Engineering for Product Managers : boucle à 5 parties, artefacts durables, dérive silencieuse]]
- [[fiches/2026-06/ng-thebatch-359-3-product-development-loops-2026-06-26\|3 Key Product Development Loops (Ng) : trois boucles imbriquées, avantage de contexte des humains]]
- [[fiches/2026-08/patel-block-buzz-teams-tokens-benchmarks-2026-08-06\|Efficient Tokens & Effective Teams in Buzz : aucune équipe ne bat le solo à horizon court, taxonomie QuickBee/WorkerBee/SmartBee]]
- [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz! — workspace humains+agents à canaux, chaque participant est une paire de clés Nostr]]

### Adoption, rôles & économie des tokens

- [[fiches/2026-07/cherny-steps-ai-adoption-2026-07-16\|Steps of AI Adoption (Cherny) : 5 étapes 0→4, goulot + garde-fous à casser pour monter d'un cran]]
- [[fiches/2026-07/cherny-wu-reflecting-year-claude-code-2026-07-17\|Reflecting on a year of Claude Code : produit et ingénierie fusionnent — parce que livrer devient bon marché]]
- [[fiches/2026-07/martignole-token-manifesto-2026-07-17\|The Token Manifesto : « You don't have a prompt problem. You have a context-window problem. »]]

### Protocoles & empaquetage (ACP, Agent Plugins)

- [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction : « ce que LSP a fait pour les langages », local stdio et distant HTTP/WebSocket]]
- [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport — « on n'indexe jamais un sigle seul »]]
- [[fiches/2026-08/google-agent-plugins-packaging-skills-mcp-2026-08-06\|Agent Plugins 1.0.0 : « The core problem isn't the components. It's the manifest », et ce que la v1 exclut]]

### Skills — harnais de recherche, graphe de code, idéation

- [[fiches/2026-08/skill-gibbs-hyperresearch-2026-08-03\|hyperresearch : routeur mince, skills chargées fraîches, « patch, never regenerate », tool-locking, gates de citation]]
- [[fiches/2026-08/skill-shamsi-graphify-2026-08-06\|graphify : AST tree-sitter déterministe, arêtes EXTRACTED/INFERRED, pas d'index vectoriel]]
- [[fiches/2026-08/graphify-net-annuaire-ia-coding-2026-08-06\|graphify.net : vitrine et annuaire — et un site officiel factuellement décalé de son propre dépôt]]
- [[fiches/2026-07/akhouri-adhd-ideation-divergente-parallele-2026-07-20\|ADHD — idéation divergente parallèle : correctif architectural à la convergence prématurée]]
- [[fiches/2026-06/skill-pocock-grill-with-docs-2026-06\|grill-with-docs : interview adversariale du plan contre le modèle de domaine, CONTEXT.md + ADR inline]]

### Contexte, inconnues & jugement du modèle

- [[fiches/2026-07/thariq-field-guide-fable-finding-unknowns-2026-07-03\|A Field Guide to Fable : « la carte n'est pas le territoire », quatre quadrants d'inconnues, outils avant/pendant/après]]
- [[fiches/2026-07/willison-fable-judgement-delegation-subagents-2026-07-03\|Fable's judgement : laisser le modèle juger, lui faire choisir le modèle moins puissant à qui déléguer]]
- [[fiches/2026-07/klaassen-thinkroom-compounding-knowledge-lifecycle-2026-07-02\|The Compounding Knowledge Lifecycle : anatomie d'une learning, mémoire durable vs éphémère, récupération grep-first]]
- [[fiches/2026-08/notion-as-code-2026-08-03\|Notion as Code : infra-as-code documentaire, script idempotent, SDK écrit pour « you or your coding agent »]]
- [[fiches/2026-08/chatgpt-claude-desktop-vs-web-deep-research-2026-08-12\|Desktop vs web : gain de friction et non de puissance, runtime d'agents, sept chiffres non confirmés]]

### Core Context Engineering

- [[fiches/2026-02/vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24\|Infrastructure contexte codifié : architecture 3 tiers, mémoire persistante, 283 sessions, MCP]]
- [[fiches/2026-02/debois-tessl-context-development-lifecycle-ai-coding-agents-2026-02-19\|Context Development Lifecycle (CDLC) — cycle d'ingénierie du contexte pour agents de codage IA]]
- [[fiches/2026-02/debois-tessl-context-flywheel-ai-coding-teams-2026-02-26\|Volant d'inertie contextuel — avantage compétitif des équipes IA par le contexte cumulé]]
- [[fiches/2025-10/ace-agentic-context-engineering-stanford-2025-10-07\|Ingénierie de contexte agentique - Auto-amélioration LLM - Architecture réflexive - Stanford]]
- [[fiches/2025-07/context-engineering-domain-understanding-johnson-2025-07-23\|Context Engineering - Domain Understanding - DICE - Rod Johnson]]

### Harness Engineering

- [[fiches/2026-04/osmani-agent-harness-engineering-2026-04-19\|Harness engineering consolidé (Osmani) : agent = model + harness, ratchet, Terminal Bench, Harness-as-a-Service]]
- [[fiches/2026-04/boeckeler-harness-engineering-coding-agents-2026-04-02\|Harness engineering (Böckeler/Thoughtworks) : confiance via guides feedforward et capteurs feedback]]
- [[fiches/2026-03/trivedy-langchain-anatomy-agent-harness-2026-03-10\|Anatomie d'un harnais d'agent (LangChain) : composants fondamentaux, évolution des harnais]]
- [[fiches/2026-02/openai-harness-engineering-codex-agent-first-2026-02-13\|Harness engineering OpenAI/Codex : 1M lignes de code zéro écriture manuelle, environnement agent-first]]

### Prompt Caching & Context Windows

- [[fiches/2026-02/trq212-anthropic-claude-code-prompt-caching-lessons-2026-02\|Leçons prompt caching Claude Code : architecture cache, plan mode, compaction]]
- [[fiches/2026-02/lancemartin-anthropic-prompt-auto-caching-claude-2026-02\|Auto-caching prompts Claude : mécanisme technique, API cache_control, économies 90% tokens]]
- [[fiches/2026-04/thariq-claude-code-session-management-1m-context-2026-04-14\|Gestion de sessions Claude Code : fenêtre 1M tokens, compaction, rewind, subagents, pourriture de contexte]]
- [[fiches/2026-04/anthropic-claude-code-quality-postmortem-2026-04-23\|Post-mortem qualité Claude Code : trois incidents caching/reasoning/prompt (mars-avril 2026)]]

### Context-Driven Platforms

- [[fiches/2025-12/gupta-garg-context-graphs-trillion-dollar-opportunity-2025-12-22\|Context Graphs Foundation Capital - nouvelle génération systèmes de record pour agents IA]]
- [[fiches/2025-12/google-conductor-context-driven-development-gemini-cli-2025-12-17\|Conductor Google - extension Gemini CLI développement piloté par le contexte]]
- [[fiches/2025-12/memodb-acontext-context-data-platform-agents-2025-12-11\|Acontext: Context Data Platform for Cloud-Native AI Agents]]
- [[fiches/2026-05/gupta-token-budget-wars-marginal-token-utility-2026-05-28\|Token Budget Wars : token-to-outcome attribution, decision traces, "measurement becomes memory" → context graph]]

### Mémoire & Recherche locale

- [[fiches/2026-03/zhutov-qmd-grep-dead-claude-code-memory-recall-2026-03-01\|QMD + skill /recall : moteur recherche local BM25/sémantique, mémoire persistante agents, remplacement grep]]

### Specs & Plans pour agents IA

- [[fiches/2026-01/osmani-how-write-good-spec-ai-agents-2026-01-13\|Addy Osmani - écrire specs pour agents IA, 5 principes, Plan Mode, PRD structuré]]
- [[fiches/2026-01/gao-vercel-agents-md-outperforms-skills-evals-2026-01-27\|AGENTS.md surpasse les skills dans les évaluations agents Vercel/Next.js]]
- [[fiches/2025-07/aws-kiro-specification-driven-agentic-ide-forbes-2025-07-15\|AWS Kiro - Agentic IDE - Specification-driven - Vibe coding vs Spec coding]]
- [[fiches/2026-02/martin-bmad-method-urbanisme-ia-agentique-sdlc-2026-02-04\|Méthode BMAD : cadre structuré pour intégrer l'IA agentique dans le SDLC]]
- [[fiches/2026-05/thoughtworks-aiworks-agentic-development-platform-2026-05-12\|AI/works Thoughtworks : Super Spec dynamique, plateforme de développement agentique spec-driven sur tout le SDLC]]

### Doctrine & Design en fichiers (contexte en fichiers)

- [[fiches/2026-05/habert-wenvision-proj-ai-repo-agent-ide-doctrine-2026-05-05\|PROJ-AI (Habert/WEnvision) : repo + agent + doctrine markdown, cycle DPEV, "le projet EST le livrable"]]
- [[fiches/2026-05/isenberg-meng-to-google-design-md-design-team-in-a-file-2026-05-06\|design.md (Google/Meng To) : l'âme du design dans un fichier, anti design-drift, taste comme moat]]
- [[fiches/2026-05/shihipar-claude-code-html-unreasonable-effectiveness-markdown-2026-05-10\|HTML remplace Markdown comme format de sortie agents : densité, interactivité bidirectionnelle, éditeurs jetables]]

### Skills, Subagents & Agent Architecture

- [[fiches/2025-10/agent-skills-anthropic-2025-10-16\|Agent Skills d'Anthropic, compétences modulaires réutilisables, portabilité cross-product]]
- [[fiches/2025-10/claude-skills-bigger-than-mcp-willison-2025-10-16\|Claude Skills vs MCP - Simplicité élégante - Explosion cambrienne prédite]]
- [[fiches/2025-10/claude-skills-document-manipulation-willison-2025-10-10\|Système de compétences Claude - Manipulation documents - Simon Willison]]
- [[fiches/2025-10/superpowers-skills-coding-agents-vincent-2025-10-09\|Superpowers/Skills - Apprentissage continu agents IA]]
- [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - AI assistants spécialisés - Context management]]
- [[fiches/2026-04/vincent-superpowers-agentic-skills-framework-github-2026-04-02\|Superpowers (GitHub) : framework de skills agentiques + méthodologie TDD pour agents de codage]]
- [[fiches/2026-05/techygarg-lattice-composable-ai-skills-atoms-molecules-refiners-2026-05-05\|Lattice : skills composables Atoms/Molecules/Refiners, "skills over prompts", living context]]
- [[fiches/2026-06/shihipar-claude-code-lessons-building-skills-2026-06-03\|Leçons skills Anthropic : taxonomie 9 catégories, gotchas, progressive disclosure, "le file system est du context engineering"]]
- [[fiches/2026-04/law-ahrefs-content-engineering-claude-code-2026-04-28\|Content engineering Ahrefs : ~23 skills orchestrées par un skill blog-pipeline, drafts en 6-12 min, MCP Ahrefs]]

### MCP (Model Context Protocol)

- [[fiches/2025-10/mcp-ui-conference-monday-liad-yosef-2025-10-18\|MCP-UI conférence détaillée, islands architecture, remote DOM, theming]]
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
- [[fiches/2026-03/mornati-developer-coding-agents-bmad-experiment-2026-03-14\|Expérimentation BMAD en 1 jour : le développeur devient superviseur d'agents]]

### Compound Engineering

- [[fiches/2025-12/shipper-klaassen-compound-engineering-every-agents-2025-12-11\|Compound Engineering : processus 4 étapes (Plan, Work, Assess, Compound) - Every]]
- [[fiches/2026-02/klaassen-compound-engineering-definitive-guide-every-2026-02-09\|Guide définitif Compound Engineering : boucle 7 étapes, plugin 40+ agents, échelle d'adoption 5 stades, règle 50/50]]
- [[fiches/2026-03/chow-compound-engineering-v260-review-pipeline-2026-03-31\|Compound Engineering v2.60 : revue de code obligatoire avec scoring de confiance, pipeline plan→work→review durci]]

### Knowledge, Ontologie & Compounding

- [[fiches/2025-09/compounding-teams-schillace-2025-09-28\|Équipes à effet multiplicateur - Développement IA récursif - Productivité exponentielle]]
- [[fiches/2025-05/seale-philosophy-eats-ai-ontological-core-2025-05-30\|Philosophie mange l'IA : noyau ontologique entreprise, sémantique métier, knowledge graph]]
- [[fiches/2025-06/netflix-uda-unified-data-architecture-knowledge-graph-2025-06-12\|Architecture données unifiée Netflix, knowledge graph RDF/SHACL, modélisation domaine]]
- [[fiches/2026-04/seale-semantic-agent-model-harness-ontology-data-2026-04-17\|Agent sémantique (Seale) : symétrie (modèle + harnais) ↔ (ontologie + données), l'ontologie seul actif non-commodité]]
- [[fiches/2026-05/talisman-modern-data-101-ontology-pipeline-refresh-2026-05-04\|Ontology Pipeline rafraîchi (Talisman) : gouvernance continue, partenariat IA augment vs replace, SKOS/OWL/RDF]]

## Entités clés

### Concepts fondamentaux

- [[kb/context-engineering\|Context engineering]] — Le matériau premier du développement agentique
- [[kb/Context-Flywheel\|Context Flywheel]] — Volant d'inertie : le contexte documenté compose
- [[kb/_entites-mineures#Context-Development-Lifecycle\|Context Development Lifecycle]] — CDLC 4 phases (Debois)
- [[kb/_entites-mineures#noyau-ontologique\|Noyau ontologique]] — Sémantique métier formalisée en ontologie (Seale)
- [[kb/compounding-teams\|Compounding teams]] — Équipes à effet multiplicateur (Schillace)
- [[kb/CLAUDE-md-technologie\|CLAUDE.md]] — Fichier de contexte projet pour Claude Code
- [[kb/AGENTS-md\|AGENTS.md]] — Alternative/complément aux skills (Gao/Vercel)
- [[kb/ADLC\|ADLC]] — Agentic Development Lifecycle : 8 phases, gates déterministes, deux portes humaines (Williams)
- [[kb/_entites-mineures#prosecution\|Prosecution]] — Revue reconfigurée en réfutation adversariale, gate de sortie à deux passes sèches
- [[kb/_entites-mineures#phase-Distill\|Phase Distill]] — P7 : simplification post-merge + *lesson foundry* ; la leçon payée une fois passe du probabiliste au déterministe
- [[kb/Loop-Engineering\|Loop Engineering]] — Concevoir un système qui s'améliore à chaque exécution plutôt que le prompt parfait (Saboo, Ng)
- [[kb/Steps-of-AI-Adoption\|Steps of AI Adoption]] — 5 étapes d'adoption (~1 → ~1 000 agents), goulot + garde-fous par palier (Cherny)
- [[kb/Context-Rot\|Context Rot]] — Pourriture de contexte en session longue

### Technologies et protocoles

- [[kb/Claude-Code\|Claude Code]] — Agent CLI terminal-first, architecture de référence
- [[kb/Model-Context-Protocol\|Model Context Protocol (MCP)]] — Protocole de connexion outils-agents
- [[kb/MCP-UI\|MCP-UI]] — Extensions UI pour MCP (islands architecture, remote DOM)
- [[kb/Claude-Skills\|Claude Skills]] — Compétences modulaires réutilisables
- [[kb/subagents-technologie\|Subagents]] — Assistants IA spécialisés délégués
- [[kb/Plan-mode\|Plan mode]] — Mode planification structurée avant exécution
- [[kb/_entites-mineures#DPROD\|DPROD]] — Spécification ouverte pour data products sémantiques
- [[kb/Conductor\|Conductor]] — Context-driven development pour Gemini CLI
- [[kb/Kiro\|Kiro]] — IDE agentique spec-driven (AWS)
- [[kb/QMD\|QMD]] — Moteur de recherche local markdown BM25/sémantique/hybride (Tobias Lütke)
- [[kb/Agent-Client-Protocol\|Agent Client Protocol]] — Éditeur ↔ agent de codage, « ce que LSP a fait pour les langages » ; s'empile avec MCP, ne le concurrence pas
- [[kb/Agent-Plugins\|Agent Plugins]] — Format d'empaquetage ouvert (skills + serveurs MCP) : « un plugin est un répertoire », composants à échec indépendant
- [[kb/graphify\|graphify]] — Codebase → graphe interrogeable, AST tree-sitter déterministe, arêtes `EXTRACTED`/`INFERRED`, zéro crédit LLM
- [[kb/hyperresearch\|hyperresearch]] — Harnais de deep research : routeur mince, skills chargées fraîches, tool-locking, gates de citation
- [[kb/Notion-as-Code\|Notion as Code]] — Infra-as-code documentaire : script idempotent, découplé de l'espace de travail
- [[kb/Buzz\|Buzz]] — Workspace humains+agents de Block sur Nostr ; harnais ACP agnostique d'agents (Goose, Claude Code, Codex)

### Personnes clés

- [[kb/Boris-Cherny\|Boris Cherny]] — Créateur Claude Code ; Steps of AI Adoption, « il n'écrit plus de prompts, il écrit des boucles »
- [[kb/Chris-Williams\|Chris Williams]] — Série ADLC : « replace trust with structure, and structure with measurement »
- [[kb/Jason-Clinton\|Jason Clinton]] — Deputy CISO Anthropic ; SDLC AI-native sécurisé, « surveiller des boucles » plutôt que des bugs
- [[kb/Thariq-Shihipar\|Thariq Shihipar]] — Leçons skills, gestion de sessions, Field Guide to Fable (les inconnues)
- [[kb/Cat-Wu\|Cat Wu]] — Head of Product Claude Code ; fusion des rôles produit/ingénierie
- [[kb/Jarred-Sumner\|Jarred Sumner]] — Créateur de [[kb/Bun\|Bun]] ; réécriture Zig → Rust en 11 jours pilotée par Claude
- [[kb/Hugo-Lassiège\|Hugo Lassiège]] — Usine logicielle solo ; « ce qui compte doit être exécutable »
- [[kb/Shubham-Saboo\|Shubham Saboo]] — Loop Engineering pour PM
- [[kb/Andrew-Ng\|Andrew Ng]] — Trois boucles de développement produit ; avantage de contexte des humains
- [[kb/Guillaume-Dumortier\|Guillaume Dumortier]] — Le vérificateur en monde clos ; « la génération est gratuite, la confiance est le produit »
- [[kb/Patrick-Debois\|Patrick Debois]] — CDLC, Context Flywheel (Tessl)
- [[kb/_entites-mineures#Aristidis-Vasilopoulos\|Aristidis Vasilopoulos]] — Évaluation empirique contexte codifié 3 tiers
- [[kb/Jesse-Vincent\|Jesse Vincent]] — Méthodologie agents, Superpowers/Skills
- [[kb/Simon-Willison\|Simon Willison]] — Analyse Skills vs MCP, explosion cambrienne
- [[kb/Addy-Osmani\|Addy Osmani]] — 5 principes specs pour agents IA
- [[kb/Rod-Johnson\|Rod Johnson]] — Framework DICE, domain understanding
- [[kb/Kent-Beck\|Kent Beck]] — Vibe Coding vs TDD, augmented coding
- [[kb/Kieran-Klaassen\|Kieran Klaassen]] — Three Fidelities, compounding engineering, Compounding Knowledge Lifecycle
- [[kb/Sam-Schillace\|Sam Schillace]] — Compounding teams
- [[kb/_entites-mineures#Lance-Martin\|Lance Martin]] — Auto-caching, developer advocacy Anthropic
- [[kb/_entites-mineures#@trq212\|@trq212]] — Prompt caching lessons, équipe Claude Code
- [[kb/_entites-mineures#Tobias-Lütke\|Tobias Lütke]] — CEO Shopify, créateur QMD
- [[kb/_entites-mineures#Artem-Zhutov\|Artem Zhutov]] — Créateur skill /recall, lab Claude Code × Obsidian

### Organisations

- [[kb/Anthropic\|Anthropic]] — Claude Code, Skills, MCP, subagents ; SDLC AI-native sécurisé (~80 % du code écrit par Claude)
- [[kb/Google\|Google]] — Conductor, Gemini CLI ; Core Maintainer d'Agent Plugins 1.0.0
- [[kb/Stanford-University\|Stanford]] — ACE framework
- [[kb/_entites-mineures#Tessl\|Tessl]] — CDLC, Context Flywheel (Patrick Debois)
- [[kb/Every\|Every]] — Compounding engineering (Klaassen)
- [[kb/Shopify\|Shopify]] — QMD, moteur de recherche local (Tobias Lütke)
- [[kb/Block\|Block]] — Buzz, Goose ; benchmarks de composition d'équipes d'agents (Terminal-Bench, LHTB)
- [[kb/_entites-mineures#Graphify-Labs\|Graphify Labs]] — graphify (Safi Shamsi, Y Combinator S26)

## Architecture conceptuelle

### Les 3 couches du Context Engineering

```
┌─────────────────────────────────────────────────┐
│  LAYER 3 — Knowledge Base (Cold Memory)         │
│  Specs à la demande, knowledge graphs,          │
│  documentation subsystèmes (via MCP)            │
│  → Vasilopoulos Tier 3, Context Graphs,         │
│    Netflix UDA, Acontext, QMD                    │
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

### L'anneau de contraintes (Osmani / SFEIR, juil. 2026)

La qualité ne se lit plus dans le code — les agents en produisent plus que
personne ne peut relire — mais dans **ce que le système refuse de laisser
passer**. Sept dimensions (correction, sécurité, performance, accessibilité,
maintenabilité, **efficience économique**, **compréhensibilité**) reliées par la
règle de **back-pressure** : *on ne confie à une boucle que l'autonomie qu'on
sait vérifier à faible coût et de façon fiable, pas un pouce de plus.*

```
        ┌──── correction ──── sécurité ────┐
   compréhensibilité                  performance
        │         [ AGENT ]                │
   efficience éco.                  accessibilité
        └────────  maintenabilité  ────────┘
              back-pressure ↑ autonomie
```

Deux corollaires d'architecture de cycle :

- **Review instrumente, Ship décide.** Review est délibérément **hors des gates
  humains** : y placer l'attention humaine — ressource finie — reviendrait à
  « bâtir un pipeline dont le débit maximal est le nombre de diffs qu'un senior
  peut lire avant la fin de la journée ». Review livre un **faisceau de preuves
  opposable** ; Ship décide sur les preuves, pas sur le diff intégral.
- **Le cliquet** : toute échappée devient une contrainte — un défaut qui a
  franchi l'anneau se referme *dans l'anneau* (test, règle de lint, rubrique,
  garde-fou de harnais). Même mécanique que le *lesson foundry* de l'ADLC et le
  *ratchet* d'Osmani : « le seul actif de la chaîne qui s'apprécie pendant que
  les modèles se déprécient ».

### Les modes d'échec de la vérification (le catalogue de l'été 2026)

| Mode d'échec | Ce qui se passe | Contre-mesure documentée |
|---|---|---|
| **Validation circulaire** | L'agent qui écrit le code écrit les tests qui le valident | Gates indépendants, **fenêtres de contexte séparées** ; « déterministe + agentique », jamais l'un à la place de l'autre |
| **Certification de l'ignorance** | Le vérificateur rend un *pass* parce que ses sources ne parlent pas du sujet — « il n'a pas seulement raté l'erreur, il l'a certifiée » | **Interdire le « pass » nu** : tout rapport se termine par sa propre couverture ; « je ne peux pas vérifier ceci » est un résultat de première classe |
| **Incohérence inter-actifs** | Deux livrables individuellement corrects se contredisent | Un contrôle qui lit **les actifs les uns contre les autres**, pas seulement contre la couche de vérité |
| **Métrique Goodhart-able** | Le % de couverture est optimisé à vitesse machine | **Mutation testing** ; audits adversariaux (« un test échoue-t-il si on supprime la feature ? ») |
| **Périmètre en prompt** | La frontière de sécurité repose sur une consigne | « Un périmètre qui repose sur une consigne dans un prompt n'est pas un périmètre » ; identités *single-purpose* à permissions minimales |
| **Procédure évincée** | Dans un pipeline long, l'étape tardive est compactée et sautée silencieusement | **Routeur mince** + skills chargées fraîches ; **tool-locking** (`[Read, Edit]`) plutôt que consigne |

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
9. **Grep ne passe pas à l'échelle** pour les agents IA — la recherche sémantique transforme un vault passif en mémoire active (Zhutov/QMD)
10. **"Tools change. Your context stays."** — le contexte survit aux changements d'outils (Zhutov)
11. **Agent = Modèle + Harnais** — la performance vient autant du harnais que du modèle (Trivedy, Osmani, OpenAI/Codex)
12. **Chaque erreur devient une règle** (principe du ratchet) — le harnais encode les leçons et ne régresse pas (Osmani)
13. **Le file system entier est du context engineering** — progressive disclosure via l'arborescence, gotchas = contenu au plus fort signal (Shihipar)
14. **L'ontologie est le seul actif non-commodité** — modèles et harnais se commoditisent, pas la sémantique métier (Seale, Talisman)
15. **Le goulot n'a jamais été la génération, c'est la vérification** — « la génération est une bouche large, la vérification un col étroit ; accélérer la bouche épaissit le tas au col » (SFEIR, Anthropic/Amdahl)
16. **Ce qui compte doit être exécutable** — une consigne est suivie « la plupart du temps », un hook ou un test l'est tout le temps (Lassiège) ; corollaire outillé : le *tool-locking* rend un comportement **mécaniquement impossible** au lieu de le déconseiller (Gibbs)
17. **Chaque phase doit se rattacher à un mode de défaillance qu'elle défend ou à une propriété qu'elle exploite** — sinon c'est du rituel humain plaqué sur des modèles (Williams, ADLC)
18. **Un handoff LLM→LLM sans checkpoint déterministe multiplie les taux d'erreur** — d'où les gates entre phases et exactement deux portes humaines (Williams)
19. **Un vérificateur est un système en monde clos** — il ne peut parler que de ce qu'on lui a donné, donc il lui est interdit de rendre un « pass » nu (Dumortier)
20. **« Control flow is code; judgment is models »** — des scripts déterministes orchestrent, les modèles ne fournissent que le jugement (Williams)
21. **Sur tâches courtes, plus d'agents n'achète que le coût de tout expliquer deux fois** — le gain d'équipe n'apparaît qu'à horizon long (Block, Terminal-Bench 2.1 vs LHTB)
22. **Payer plus cesse d'aider, puis commence à nuire** — sur-raisonnement et timeouts ; à qualité équivalente, choisir est « une décision de budget, pas de qualité » (Block)
23. **Sur un modèle bon marché, les tokens de raisonnement sont la meilleure affaire disponible** — et un SmartBee en effort *medium* suffit à la plupart des tâches (Block)
24. **Faire escalader les agents vers un coordinateur, pas vers l'humain** — « the human stops being middleware and goes back to being the last reviewer » (Block)
25. **Le cycle doit devenir moins cher à chaque run** — « flat cost is failure » ; l'unité de compte est le *coût par changement fusionné et vérifié* (Williams)
26. **La qualité est plafonnée par la capacité à clarifier les inconnues du modèle** — « la carte n'est pas le territoire » (Shihipar)
27. **Le manifeste, pas les composants** — skills et serveurs MCP sont portables ; la boîte dans laquelle on les met ne l'était pas (Agent Plugins 1.0.0)
28. **On n'indexe jamais un sigle seul** — l'entité est le nom complet, le sigle n'est qu'un alias, et trois entités peuvent le porter (Girard)
