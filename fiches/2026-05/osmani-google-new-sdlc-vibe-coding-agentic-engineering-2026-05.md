# osmani-google-new-sdlc-vibe-coding-agentic-engineering-2026-05

## Veille

Whitepaper Google (volet « Day 1 » d'une série, par Addy Osmani, Shubham Saboo et Sokratis Kartakis) qui cartographie la mutation du cycle de vie logiciel (SDLC) à l'ère des agents de codage. Thèse : le basculement fondamental n'est pas un nouveau langage mais le passage de l'écriture de code à l'**expression d'intention**. Le document pose un spectre allant du *vibe coding* (prompter et accepter) à l'*agentic engineering* (l'IA implémente sous contraintes, tests et boucles de feedback conçus par l'humain), avec le **context engineering** comme compétence centrale, le modèle de l'**usine logicielle** (le livrable du dev = le système qui produit le code), le **harness engineering** (Agent = Modèle + Harness) et une analyse économique CapEx/OpEx du coût total de possession.

## Titre Article

The New SDLC With Vibe Coding — From ad-hoc prompting to Agentic Engineering

## Date

2026-05

## URL

https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding

<!-- Republication par Addy Osmani sur son blog perso (« The New Software Lifecycle », 2026-06-16) : https://addyosmani.com/blog/new-sdlc-vibe-coding/ — même contenu que le whitepaper Google, conservé ici plutôt qu'en fiche distincte (anti-doublon). -->

## Keywords

nouveau SDLC, vibe coding, agentic engineering, ingénierie agentique, intention vs syntaxe, context engineering, ingénierie du contexte, contexte statique vs dynamique, Agent Skills, harness engineering, Agent = Modèle + Harness, usine logicielle, factory model, boucle de l'agent, evals, trajectory evaluation, conductor vs orchestrator, problème des 80 %, AGENTS.md, CLAUDE.md, GEMINI.md, MCP, A2A, Agents CLI, ADK, model routing, CapEx OpEx, coût total de possession, token economy, Google, Addy Osmani

## Authors

Addy Osmani, Shubham Saboo, Sokratis Kartakis (Google)

## Ton

Profil : whitepaper d'entreprise (Google), perspective « nous » d'auteurs-praticiens, registre didactique-stratégique en anglais, niveau technique élevé mais volontairement accessible (le document précise viser des ingénieurs, managers, architectes et leaders techniques familiers du dev moderne mais pas du ML). Le ton conjugue l'autorité de la marque Google, celle d'Addy Osmani (figure reconnue de l'ingénierie web, abondamment auto-citée dans les endnotes) et un effort pédagogique soutenu : chaque concept est introduit par une définition, illustré par une figure numérotée (9 figures) et ancré sur des données chiffrées et des benchmarks publics. Style structuré en mouvements (du syntaxe→intention, au spectre, au contexte, au nouveau SDLC, au harness, aux rôles, à la pratique, à l'économie, aux recommandations), métaphores filées et porteuses : le **directeur d'usine** qui conçoit la chaîne plutôt que d'assembler chaque pièce, le **moteur** (modèle) vs **la voiture, la route et le code de la route** (harness), le **chef d'orchestre vs l'orchestrateur**. Équilibre assumé entre promesse (gains 25-39 %) et nuance (étude METR : -19 %, « problème des 80 % »). Document de cadrage qui revendique des principes durables plutôt qu'un instantané périssable.

## Pense-betes

- **Thèse-pivot** : *« The most profound shift in software engineering isn't a new language, framework, or cloud service. It's the transition from writing code to expressing intent. »* L'interface du développeur passe de la **syntaxe** à l'**intention**.
- **Données de cadrage (2026)** : **85 %** des développeurs professionnels utilisent régulièrement des agents de codage, **51 %** quotidiennement, **41 %** du nouveau code est généré par IA.
- **Figure 1 — De l'autocomplétion à l'autonomie** : 5 générations qui se cumulent (Autocomplete ~2021 → Inline suggestions ~2022 → Chat-based generation ~2023 → Coding agents ~2024-25 → Autonomous agents ~2025-26), axe Syntaxe → Intention, *« more human effort »* → *« more machine autonomy »*.
- **L'agent = boucle** : perceive goal → plan → act (tools) → observe → iterate (auto-correction). Construit de **5 parties** (cf. whitepaper *Introduction to Agents*, nov. 2025) : modèle, outils, mémoire, orchestration, déploiement. *« The loop is the beating heart of every agent. »*
- **Vibe coding** : terme de Karpathy (févr. 2025, *« fully give in to the vibes »*) ; appliqué si largement qu'il a perdu son sens → début 2026 Karpathy introduit **agentic engineering** pour le bout discipliné du spectre.
- **Le spectre** (vibe coding ↔ structured AI-assisted ↔ agentic engineering) : *« the key differentiator is not whether you use AI. It's how much structure, verification, and human judgment surrounds the AI's output. »*
- **Vérification = le vrai différenciateur** : **Tests** vérifient le déterministe (entrée→sortie) ; **Evals** vérifient le non-déterministe (bonne trajectoire ? bons outils ? réponse au niveau de qualité ?), via datasets étiquetés, grilles de score, **LM judges**. *« Without both, the practice is always vibe coding, regardless of how sophisticated the prompts are. »*
- **Context engineering = la vraie compétence** : la qualité du code dépend moins de la finesse du prompt que de la qualité du **contexte**. **6 types** : Instructions, Knowledge, Memory, Examples, Tools, Guardrails. Arbitrage **contexte statique** (toujours chargé : AGENTS.md/CLAUDE.md/GEMINI.md — coûteux) vs **dynamique** (chargé à la demande : skills, RAG, résultats d'outils — efficient).
- **Agent Skills** = pattern le plus puissant pour le contexte dynamique (progressive disclosure : métadonnées au démarrage, instructions au match, références au besoin). Résout 4 problèmes : **context rot**, absence de mémoire procédurale, surcoût opérationnel multi-agents, portabilité cross-outils.
- **Le nouveau SDLC** : l'IA **compresse le cycle de façon inégale** — l'implémentation passe de semaines à heures, mais requirements/architecture/vérification restent au rythme humain. *« It is not a faster version of the old SDLC. It is a different workflow. »* Le dev glisse de *primary implementor* à *system designer & quality arbiter*.
- **Par phase** : Requirements (collapse requirements→prototype) ; **Design/architecture = la phase la plus obstinément humaine** (arbitrages de compromis) ; Implementation (gains **25-39 %**, mais étude **METR : devs expérimentés 19 % plus lents** sur certaines tâches à cause de la vérification) ; Testing (output eval + **trajectory evaluation**) ; Code review (IA en *first-pass reviewer*) ; Maintenance (la dette technique « trop risquée à toucher » devient refactorable).
- **Modèle de l'usine** : *« the developer's primary output is not code — it's the system that produces code »* (specs + agents + tests/quality gates + feedback loops + guardrails). Le dev conçoit la chaîne et le contrôle qualité, pas chaque pièce.
- **Harness Engineering** : *« Agent = Model + Harness »*. Le modèle ≈ **10 %**, le harness ≈ **90 %**. Contenu : instructions/rule files, tools/MCP, sandboxes, orchestration (sub-agents, routing, hand-offs), guardrails/hooks (code déterministe aux points du lifecycle), observability. *« This surrounding machinery is known as the Harness. »*
- **Preuves de l'effet harness** : sur **Terminal Bench 2.0**, une équipe a fait passer un agent **hors du Top 30 au Top 5 en ne changeant que le harness** (modèle inchangé) ; **LangChain : +13,7 points** en ne touchant que system prompt/outils/middleware. *« Most agent failures, examined honestly, are configuration failures. »*
- **Rôles du dev** : **Conductor** (temps réel, synchrone, in-IDE, contrôle au keystroke — Copilot/Gemini Code Assist/Cursor/Windsurf) vs **Orchestrator** (async, multi-agent, contrôle au niveau objectif — Jules/Cursor background/Claude Code). *« Not either/or — both, depending on the task. »*
- **Le problème des 80 %** : l'IA génère vite ~80 % du code ; les **20 %** restants (edge cases, gestion d'erreurs, intégration, correction subtile) exigent une connaissance contextuelle profonde. Les erreurs IA ont migré de fautes de syntaxe vers des **échecs conceptuels** (le code *« looks right »* et passe les tests basiques).
- **Agents en pratique — 3 lieux** : *in the editor* (Copilot, Cursor, Windsurf, JetBrains), *in the terminal* (Antigravity CLI, Claude Code, Codex CLI, Open Code, Cline), *in the background* (Jules, Cursor background, AlphaEvolve). **Vibe coding d'agents de prod** via **Google Agents CLI** (`agents-cli create/playground/eval/deploy`, lifecycle ADK), **MCP** (outils) + **A2A** (délégation inter-agents). Anthropic : équipes d'agents ayant construit un **compilateur C en Rust en 2 semaines**.
- **Économie (CapEx/OpEx)** : **vibe coding = low CapEx, high OpEx** (token burn, maintenance tax, security remediation) ; **agentic engineering = high CapEx, low OpEx** (investissement amont en specs/tests/contexte → coût marginal de livraison effondré). **Context engineering = levier financier** ; **intelligent model routing** (gros modèles pour requirements/archi, petits modèles pour tests/review/CI). Figure 9 : point de croisement où le vibe coding coûte **3-10× plus cher par feature**.
- **Conclusion — 3 principes durables** : (1) *« Structure scales, vibes don't »* ; (2) *« AI amplifies your engineering culture »* (force multiplier des forces ET des faiblesses) ; (3) *« The human role is evolving, not diminishing »*. Clôture : ***« Generation is solved. Verification, judgment, and direction are the new craft. »***
- **Série** : Day 1 (ce document) ; **Day 3** = *Context Engineering: Sessions, Skills & Memory* ; **Day 5** = *Spec-Driven Production Grade Development in the Age of Vibe Coding* (revue de code, guardrails, zero-trust).

## RésuméDe400mots

Ce whitepaper Google (premier volet d'une série, signé Addy Osmani, Shubham Saboo et Sokratis Kartakis, mai 2026) soutient que la transformation la plus profonde de l'ingénierie logicielle n'est pas technologique mais interfacielle : on passe de l'écriture de code à l'expression d'intention, en confiant à des systèmes intelligents la traduction de cette intention en logiciel fonctionnel. Données de cadrage : 85 % des développeurs professionnels utilisent régulièrement des agents de codage, 51 % quotidiennement, et 41 % du nouveau code est généré par IA.

Les auteurs refusent l'opposition binaire vibe coding / agentic engineering au profit d'un **spectre**. Le différenciateur n'est pas l'usage de l'IA mais la quantité de structure, de vérification et de jugement humain qui entoure sa production. Distinction clé : les **tests** vérifient le déterministe, les **evals** (datasets étiquetés, grilles, LM judges) vérifient le non-déterministe — sans les deux, on reste en vibe coding.

La compétence centrale devient le **context engineering** : la qualité dépend moins du prompt que du contexte fourni. Six types de contexte (instructions, knowledge, memory, examples, tools, guardrails) se répartissent entre contexte **statique** (toujours chargé, coûteux : AGENTS.md, CLAUDE.md, GEMINI.md) et **dynamique** (à la demande, efficient). Les **Agent Skills** sont le pattern phare du contexte dynamique par progressive disclosure.

Le SDLC est compressé de façon inégale : l'implémentation passe de semaines à heures, mais requirements, architecture et vérification restent au rythme humain. L'architecture demeure la phase la plus humaine (arbitrages de compromis). Côté implémentation, gains de 25-39 % mais nuance de l'étude METR (devs 19 % plus lents sur certaines tâches). Le fil conducteur est le **modèle de l'usine** : le livrable du développeur n'est plus le code mais le système qui le produit (specs, agents, quality gates, boucles de feedback, guardrails).

Au cœur de l'usine, l'équation **Agent = Modèle + Harness** : le modèle pèse ~10 %, le harness ~90 % (instructions, outils/MCP, sandboxes, orchestration, hooks, observabilité). Preuve : sur Terminal Bench 2.0, changer le seul harness fait passer un agent hors Top 30 au Top 5. *« Most agent failures are configuration failures. »*

Le développeur oscille entre **conductor** (temps réel, in-IDE) et **orchestrator** (async, multi-agents), confronté au **problème des 80 %**. Économiquement, le vibe coding (low CapEx/high OpEx) finit 3-10× plus cher par feature que l'agentic engineering (high CapEx/low OpEx) ; le context engineering et le model routing sont des leviers financiers. Conclusion : *« Generation is solved. Verification, judgment, and direction are the new craft. »*

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Google | ORGANISATION | publie | The New SDLC With Vibe Coding | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Addy Osmani | PERSONNE | a_créé | The New SDLC With Vibe Coding | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Addy Osmani | PERSONNE | travaille_chez | Google | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| The New SDLC With Vibe Coding | DOCUMENT | affirme_que | le basculement fondamental est le passage de l'écriture de code à l'expression d'intention | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| agentic engineering | METHODOLOGIE | est_variante_de | vibe coding | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| context engineering | METHODOLOGIE | améliore | qualité du code généré par IA | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Agent Skills | METHODOLOGIE | permet | gestion du contexte dynamique par progressive disclosure | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Agent Skills | METHODOLOGIE | réduit | context rot des prompts surchargés | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| harness | CONCEPT | permet | transformer un modèle brut en agent capable de finir une tâche | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| The New SDLC With Vibe Coding | DOCUMENT | affirme_que | la plupart des échecs d'agents sont des échecs de configuration du harness | AFFIRMATION | 0.91 | ATEMPOREL | déclaré_article |
| IA | TECHNOLOGIE | réduit | durée de la phase d'implémentation du SDLC | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| modèle de l'usine | METHODOLOGIE | affirme_que | le livrable du développeur n'est pas le code mais le système qui produit le code | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| evals | METHODOLOGIE | s_applique_à | vérification des comportements non déterministes des agents | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | a_créé | vibe coding | METHODOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Andrej Karpathy | PERSONNE | a_créé | agentic engineering | METHODOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Google Agents CLI | TECHNOLOGIE | utilise | lifecycle ADK pour construire des agents de production | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| intelligent model routing | METHODOLOGIE | réduit | coût opérationnel en tokens (OpEx) | CONCEPT | 0.89 | ATEMPOREL | déclaré_article |
| vibe coding | METHODOLOGIE | s_applique_à | prototypes, scripts et projets jetables | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| The New SDLC With Vibe Coding | DOCUMENT | affirme_que | Generation is solved. Verification, judgment, and direction are the new craft | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| The New SDLC With Vibe Coding | DOCUMENT | mesure | 41 % du nouveau code est généré par IA en 2026 | MESURE | 0.90 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| The New SDLC With Vibe Coding | DOCUMENT | nature | Whitepaper Google, série « Day 1 », mai 2026 | AJOUT |
| Addy Osmani | PERSONNE | rôle | Ingénieur Google, co-auteur principal | AJOUT |
| Shubham Saboo | PERSONNE | rôle | Co-auteur (Google) | AJOUT |
| Sokratis Kartakis | PERSONNE | rôle | Co-auteur (Google) | AJOUT |
| agentic engineering | METHODOLOGIE | définition | Bout discipliné du spectre : IA implémente sous specs, tests et boucles de feedback humains | AJOUT |
| vibe coding | METHODOLOGIE | définition | Prompter une IA et accepter le résultat avec vérification minimale | AJOUT |
| context engineering | METHODOLOGIE | définition | Fournir aux agents un contexte riche et structuré (6 types ; statique vs dynamique) | AJOUT |
| harness | CONCEPT | équation | Agent = Modèle + Harness ; modèle ~10 %, harness ~90 % | AJOUT |
| modèle de l'usine | METHODOLOGIE | métaphore | Le dev conçoit la chaîne de production du code, pas chaque pièce | AJOUT |
| problème des 80 % | CONCEPT | définition | L'IA génère ~80 % du code ; les 20 % restants exigent un contexte profond | AJOUT |
| conductor vs orchestrator | CONCEPT | définition | Deux modes du dev : temps réel in-IDE vs délégation async multi-agents | AJOUT |
| Google Agents CLI | TECHNOLOGIE | catégorie | Outil CLI bundlant des skills ADK (create/playground/eval/deploy) | AJOUT |
