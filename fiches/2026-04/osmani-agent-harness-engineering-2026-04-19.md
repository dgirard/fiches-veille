# osmani-agent-harness-engineering-2026-04-19

## Veille
Synthèse par Addy Osmani (Google, Chrome/Cloud) du champ émergent du *harness engineering* : équation `agent = model + harness`, principe du *ratchet* ("chaque erreur devient une règle"), reframe HumanLayer "skill issue", preuves Terminal Bench (Top 30 → Top 5 par seul changement de harnais), architecture Claude Code en couches, vision Anthropic "harnesses don't shrink, they move" et Harness-as-a-Service (Claude Agent SDK, Codex SDK, OpenAI Agents SDK). Article-pivot qui consolide Trivedy, HumanLayer, Anthropic et Böckeler en doctrine.

## Titre Article
Agent Harness Engineering

## Date
2026-04-19

## URL
https://addyosmani.com/blog/agent-harness-engineering/

## Keywords
harness engineering, agent harness, Addy Osmani, Viv Trivedy, HumanLayer, Dex Horthy, Anthropic engineering, Birgitta Böckeler, agent = model + harness, ratchet principle, skill issue reframe, Terminal Bench, Claude Code architecture, Fareed Khan, Ralph Loop, planner evaluator split, AGENTS.md, hooks lifecycle, sandboxes, context rot, compaction, tool offloading, progressive disclosure, full context resets, model-harness training loop, Harness-as-a-Service, Claude Agent SDK, Codex SDK, OpenAI Agents SDK, just-in-time tool assembly

## Authors
Addy Osmani (Software Engineer at Google, Cloud + Gemini)

## Ton
**Profil** : Article-synthèse signé par un ingénieur logiciel reconnu (Addy Osmani, Google, ex-Chrome) sur son blog personnel. Registre tech-éditorial à forte densité conceptuelle, narration à la première personne ("I've watched this play out", "in my own workflows"). Public cible : ingénieurs senior et tech leads qui construisent ou opèrent des agents de codage en production, lecteurs de Trivedy/HumanLayer/Böckeler cherchant une pièce de consolidation. Autorité construite par la position Google et la pratique personnelle assumée.

**Style** : Article long format structuré en huit sections (équation pivot → "skill issue" → ratchet → 7 primitives du harnais → architecture en production → mouvement du harnais → loop d'entraînement → HaaS → ouvertures). Phrases nettes, métaphores ramassées (*"teaching someone to use a single kitchen gadget vs handing them a kitchen"* pour bash, *"pilot's checklist, not style guide"* pour AGENTS.md, *"GANs for prose"* pour le split planner/evaluator). Citation explicite et créditée de chaque source (Trivedy, Horthy/HumanLayer, Anthropic, Böckeler, Willison, Khan). Tonalité ferme et programmatique, sans hype. La force du document tient à sa **fonction agrégative** : Osmani ne propose pas un nouveau cadre, il rassemble en doctrine ce que les pionniers ont publié séparément. C'est la pièce qui transforme le harness engineering de discipline naissante en consensus partagé. Les chiffres-pivot circulent ("Top 30 → Top 5", *"60 lignes max dans AGENTS.md"*) et la phrase Anthropic *"harnesses don't shrink, they move"* devient l'aphorisme structurant du débat 2026.

## Pense-betes
- **Date et auteur** : 19 avril 2026, Addy Osmani (Google, Cloud + Gemini, ex-Chrome).
- **Équation pivot** (créditée à Viv Trivedy) : ***"Agent = Model + Harness. If you're not the model, you're the harness."*** Reformulation Osmani : *"a decent model with a great harness beats a great model with a bad harness"*.
- Crédits explicites :
  - **Viv Trivedy** : a créé le terme *harness engineering*, post "Anatomy of an Agent Harness" est la dérivation la plus claire.
  - **Dex Horthy / HumanLayer** : framing "skill issue" — la plupart des échecs d'agent sont des problèmes de config, pas de poids.
  - **Anthropic Engineering** : meilleur breakdown public sur le design de harnais long-running.
  - **Birgitta Böckeler** : bonne vue côté utilisateur.
- **Ratchet principle** : *"Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong."* On n'ajoute une contrainte qu'après une vraie défaillance. On ne la retire que quand un modèle plus capable l'a rendue redondante.
- **Skill issue reframe (HumanLayer)** : *"It's not a model problem. It's a configuration problem."* Le default *"wait for the next version"* est explicitement rejeté.
- **Terminal Bench data** (Trivedy/HumanLayer cité) : sur Terminal Bench 2.0, **Claude Opus 4.6 dans Claude Code score nettement plus bas que le même modèle dans un harnais custom**. L'équipe Trivedy a fait passer un coding agent de **Top 30 à Top 5 en ne changeant que le harnais**. Preuve empirique massive.
- Pattern *"working backwards from behaviour"* : *"behaviour we want (or want to fix) → harness design to help the model achieve this"*. Si tu ne peux pas nommer le comportement qu'un composant délivre, il ne devrait pas être là.
- **7 primitives du harnais** :
  1. **Filesystem & Git** : état durable, workspace partagé humains/agents, versioning gratuit.
  2. **Bash & code execution** : *"the difference between teaching someone to use a single kitchen gadget and handing them a kitchen."* Willison cité.
  3. **Sandboxes** : isolation, bons défauts (runtimes pré-installés, headless browser pour vérification).
  4. **Memory & search** : AGENTS.md rechargé à chaque tour + MCP/Context7 pour combler le cutoff.
  5. **Battling context rot** : 3 techniques — *compaction* (résumés intelligents), *tool-call offloading* (head/tail tokens, output complet sur disque), *skills with progressive disclosure* (révéler tools/instructions à la demande). Anthropic ajoute le *full context reset* avec hand-off file structuré.
  6. **Long-horizon execution** : Ralph Loop (hook qui ré-injecte le prompt original dans une fresh context window), planning avec plan file, **planner/generator/evaluator split** (Anthropic explicite : *"separating generation from evaluation outperforms self-evaluation"*), sprint contract (négocier la condition de "done" avant le code).
  7. **Hooks** : enforcement layer. Principe HumanLayer : ***"success is silent, failures are verbose"***. Block destructive bash, run typecheck après edit, require approval avant push main.
- **AGENTS.md** : *"flat markdown rulebook at the root of your repo... lands in the system prompt every turn."* HumanLayer garde le sien sous **60 lignes**. *"Pilot's checklist, not style guide. Earn each line."*
- **Tool economy** : *"Ten focused tools outperform fifty overlapping ones because the model can hold the menu in its head."* Sécurité MCP : tool descriptions = trusted text, MCP malveillant peut prompt-inject avant que tu tapes quoi que ce soit.
- **Architecture Claude Code en couches** (référence Fareed Khan) : input layer (UI, session manager, permission gate) → knowledge layer (skill registry, context compressor, task graph, memory store) → integration layer (MCP runtime) → execution layer (tool dispatch, streaming runtime, prompt cache) → output layer → observability layer → multi-agent layer (subagent spawning, mailboxes, FSM protocol, autonomous board, worktree isolator). Master agent loop au centre.
- **"Harnesses don't shrink, they move"** (Anthropic) : aphorisme structurant. Opus 4.6 a tué le mode d'échec *context-anxiety* de Sonnet 4.5 → toute la scaffolding "anxiety-mitigation" est désormais dead code. Mais le plafond a bougé : nouvelles tâches débloquées → nouvelles failure modes → nouveau scaffolding (memory policy multi-jours, coordination de 3 agents spécialisés, evaluators design-quality).
- **Citation Anthropic clé** : *"every component in a harness encodes an assumption about what the model can't do on its own."*
- **Model-harness training loop** : primitive découverte dans le harnais → standardisée dans le produit → utilisée pour post-training du modèle suivant → modèle suivant meilleur sur cette primitive. Cycle. Crée du *co-training* / overfitting : *"a genuinely general model wouldn't care whether you used apply_patch or str_replace, but co-training creates overfitting."* Explique pourquoi Opus 4.6 *"feels different inside Claude Code than inside someone else's harness"*.
- **Harness-as-a-Service (HaaS)** : framing Trivedy. Bascule de "build on LLM APIs (completion)" → "build on harness APIs (runtime)". Triade citée : **Claude Agent SDK, Codex SDK, OpenAI Agents SDK**. Quatre piliers de configuration : system prompt, tools, context, subagents. Aphorisme Trivedy : *"good agent building is an exercise in iteration. You can't do iterations if you don't have a v0.1."*
- **3 ouvertures pour la suite** :
  1. Multi-agent orchestration sur codebase partagée.
  2. Harnais auto-analytiques qui détectent et corrigent leurs propres failure modes.
  3. JIT tool/context assembly — *"harnesses stop being static config and start becoming something closer to a compiler."*
- Observation de fond : *"Look at the top coding agents side by side (Claude Code, Cursor, Codex, Aider, Cline) and they look more like each other than their underlying models do. The models are different. The harness patterns are converging."*
- Articulation dossier veille : pièce de **consolidation doctrinale** entre Trivedy (fondateur du terme, mars 2026), Böckeler (vue utilisateur, avril 2026), Seale (semantic agent, avril 2026). Osmani agrège et stabilise le vocabulaire commun.

## RésuméDe400mots
Addy Osmani (Google) publie le 19 avril 2026 un article qui consolide en doctrine ce que Viv Trivedy, HumanLayer, Anthropic et Birgitta Böckeler ont publié séparément depuis le début 2026 : le *harness engineering*. Sa thèse tient en une équation, créditée à Trivedy :

> *"Agent = Model + Harness. If you're not the model, you're the harness."*

Reformulée par Osmani : un modèle correct dans un excellent harnais bat un excellent modèle dans un mauvais harnais. La preuve empirique vient de Terminal Bench 2.0 : Claude Opus 4.6 dans Claude Code score nettement plus bas que le même modèle dans un harnais custom, et l'équipe Trivedy a fait passer un coding agent de **Top 30 à Top 5 en ne changeant que le harnais**.

Osmani articule trois principes méthodologiques. Le ***skill issue reframe*** (HumanLayer) : la plupart des échecs ne sont pas des limites du modèle mais des problèmes de configuration. Le ***ratchet principle*** : chaque ligne d'un AGENTS.md doit être traçable à un échec passé concret — *"add only when you've seen a real failure, remove only when a capable model has made them redundant"*. Le ***working backwards from behaviour*** : ne pas pré-construire l'infrastructure, dériver chaque composant du comportement attendu.

Suivent les sept primitives du harnais : filesystem et Git (état durable), bash et code execution (*"hand them a kitchen, not a single kitchen gadget"*), sandboxes (isolation et défauts), memory et search (AGENTS.md rechargé, MCP, Context7), battling context rot (compaction, tool-call offloading, skills à révélation progressive, full context resets Anthropic), long-horizon execution (Ralph Loop, planning, **planner/evaluator split** — *"GANs for prose"*), hooks (*"success is silent, failures are verbose"*).

Sur AGENTS.md, deux leçons : moins de 60 lignes (HumanLayer), *"pilot's checklist, not style guide"*. Sur les tools : *"ten focused tools outperform fifty overlapping ones"* — sécurité MCP comprise.

Osmani s'appuie ensuite sur le breakdown de Fareed Khan de l'architecture Claude Code en sept couches (input, knowledge, integration, execution, output, observability, multi-agent) pour montrer que chaque concept précédent a un home concret en production.

Vient la phrase Anthropic qui structure le débat : *"Harnesses don't shrink, they move."* Quand un modèle s'améliore, le scaffolding qui encodait ses limites disparaît, mais le plafond bouge et de nouveau scaffolding émerge. À cela s'ajoute le **model-harness training loop** : les primitives utiles deviennent standards, sont post-trainées dans le modèle suivant, créant du co-training et de l'overfitting (Opus 4.6 *"feels different inside Claude Code"*).

L'article ferme sur le *Harness-as-a-Service* (Claude Agent SDK, Codex SDK, OpenAI Agents SDK) et trois ouvertures : multi-agent sur codebase partagée, harnais auto-analytiques, JIT tool/context assembly *"closer to a compiler than to static config"*.

Pièce de consolidation qui stabilise le vocabulaire commun du champ et fait basculer le harness engineering du statut de discipline naissante à celui de consensus partagé.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Addy Osmani | PERSONNE | a_publié | Agent Harness Engineering | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Addy Osmani | PERSONNE | est_employé_par | Google | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Addy Osmani | PERSONNE | affirme_que | un bon harnais bat un meilleur modèle dans un mauvais harnais | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Viv Trivedy | PERSONNE | a_créé | terme harness engineering | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Viv Trivedy | PERSONNE | a_formulé | équation Agent = Model + Harness | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Harness engineering | METHODOLOGIE | est_basé_sur | ratchet principle | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Ratchet principle | CONCEPT | exige | traçabilité de chaque règle AGENTS.md à un échec passé | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| HumanLayer | ORGANISATION | recommande | reframe skill issue pour échecs d'agent | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Dex Horthy | PERSONNE | dirige | HumanLayer | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Terminal Bench 2.0 | EVENEMENT | démontre | Top 30 → Top 5 par changement de harnais seul | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Claude Opus 4.6 | TECHNOLOGIE | score_inférieur_dans | Claude Code vs harnais custom | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | harnesses don't shrink they move | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | recommande | planner generator evaluator split | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Ralph Loop | METHODOLOGIE | utilise | hook qui ré-injecte prompt dans fresh context window | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| AGENTS.md | TECHNOLOGIE | doit_rester | sous 60 lignes selon HumanLayer | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Hooks | CONCEPT | suivent | principe success is silent failures are verbose | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Fareed Khan | PERSONNE | a_documenté | architecture Claude Code en 7 couches | DOCUMENT | 0.92 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | est_organisé_en | 7 couches input knowledge integration execution output observability multi-agent | METHODOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Model-harness training loop | CONCEPT | crée | co-training et overfitting | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Harness-as-a-Service | CONCEPT | inclut | Claude Agent SDK, Codex SDK, OpenAI Agents SDK | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Harness engineering | METHODOLOGIE | converge | entre Claude Code Cursor Codex Aider Cline | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Birgitta Böckeler | PERSONNE | documente | harness engineering côté utilisateur | METHODOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Addy Osmani | PERSONNE | rôle | Software Engineer at Google (Cloud + Gemini, ex-Chrome) | MISE_A_JOUR |
| Agent Harness Engineering | DOCUMENT | format | Article de blog long format addyosmani.com | AJOUT |
| Harness engineering | METHODOLOGIE | définition | Discipline d'ingénierie du scaffolding entourant un modèle (prompts, tools, context, hooks, sandboxes, subagents, feedback loops, recovery paths) | MISE_A_JOUR |
| Ratchet principle | CONCEPT | définition | Chaque erreur d'agent devient une règle permanente. Toute ligne d'AGENTS.md traçable à un échec passé. | AJOUT |
| Skill issue reframe | CONCEPT | définition | Cadre HumanLayer : la plupart des échecs d'agent sont des problèmes de configuration, pas de poids du modèle | AJOUT |
| HumanLayer | ORGANISATION | secteur | Outillage agents IA / harness engineering | AJOUT |
| Dex Horthy | PERSONNE | rôle | Tracking pattern harness engineering, HumanLayer | AJOUT |
| Viv Trivedy | PERSONNE | rôle | Créateur du terme harness engineering, post Anatomy of an Agent Harness | MISE_A_JOUR |
| Terminal Bench 2.0 | EVENEMENT | rôle | Benchmark de référence — preuve empirique du gap harnais (Top 30 → Top 5) | AJOUT |
| Ralph Loop | METHODOLOGIE | définition | Hook qui intercepte la sortie du modèle et ré-injecte le prompt original dans une fresh context window pour exécution multi-session | AJOUT |
| Planner-Evaluator split | METHODOLOGIE | définition | Pattern Anthropic : générateur et évaluateur séparés en agents distincts (les agents skewent positif sur leur propre travail) | AJOUT |
| Sprint contract | METHODOLOGIE | définition | Generator et evaluator négocient la condition de "done" avant que le code soit écrit | AJOUT |
| Success is silent failures are verbose | CONCEPT | définition | Principe HumanLayer : un hook ne renvoie rien si le check passe, injecte l'erreur dans la loop si ça échoue | AJOUT |
| AGENTS.md | TECHNOLOGIE | guidelines | Pilot's checklist, pas style guide. <60 lignes (HumanLayer). Earn each line. | MISE_A_JOUR |
| Tool economy | CONCEPT | définition | 10 outils focalisés battent 50 outils chevauchants — le modèle peut tenir le menu en tête | AJOUT |
| Harnesses don't shrink they move | CONCEPT | définition | Aphorisme Anthropic : quand le modèle s'améliore, le scaffolding bouge plutôt qu'il ne disparaît | AJOUT |
| Model-harness training loop | CONCEPT | définition | Boucle de co-évolution : primitive harnais → produit → post-training modèle suivant → meilleur sur cette primitive. Crée du co-training et de l'overfitting. | AJOUT |
| Harness-as-a-Service (HaaS) | CONCEPT | définition | Bascule industrielle des LLM APIs (completion) vers les harness APIs (runtime). SDK fournissant loop, tools, context, hooks, sandbox par défaut. | AJOUT |
| Claude Agent SDK | TECHNOLOGIE | catégorie | Harness-as-a-Service Anthropic | AJOUT |
| Codex SDK | TECHNOLOGIE | catégorie | Harness-as-a-Service OpenAI | AJOUT |
| OpenAI Agents SDK | TECHNOLOGIE | catégorie | Harness-as-a-Service OpenAI | AJOUT |
| Fareed Khan | PERSONNE | rôle | Auteur du breakdown architecture Claude Code en 7 couches | AJOUT |
| JIT tool/context assembly | CONCEPT | définition | Vision future : harnais qui assemble dynamiquement tools et contexte juste-à-temps, plus proche d'un compilateur que d'une config statique | AJOUT |
