# rohit4verse-2026-ai-engineer-roadmap-5-projects-2026-04

## Veille
Thread X manifeste de Rohit (@rohit4verse) qui pose la *2026 AI engineer roadmap* : 150k$ d'écart entre prompt engineer et systems architect, fin des *generic wrappers* "sherlocked by big tech", et 5 projets de portfolio classés par niveau de complexité (mobile SLM offline, self-improving coding agent, *Cursor for video editors* multimodal, personal life OS agent privacy-first, autonomous enterprise workflow agent). Chaque projet décrit ses *key architectural decisions* (lazy loading, sliding window, sandboxing, scene detection, knowledge graph personnel, event-driven multi-agent, audit trail, RBAC, observability). Slogan structurant : *"the replaceable: building wrappers / the unfireable: shipping autonomous systems"*. Tonalité injonctive et virale typique X 2026.

## Titre Article
the 2026 ai engineer roadmap

## Date
2026-04-29

## URL
https://x.com/rohit4verse/status/2009663737469542875

## Keywords
2026 AI engineer roadmap, Rohit, rohit4verse, X thread, AI portfolio, prompt engineer vs systems architect, 150k salary gap, generic wrappers, sherlocked by big tech, production-grade projects, edge AI, small language models, SLM mobile, lazy loading, sliding window, semantic chunking, dynamic quantization, 4-bit 8-bit quantization, battery optimization, offline-first sync, self-improving coding agent, agentic loops, plan-execute-test-reflect, sandboxing, memory hierarchy, reflection mechanism, learning from mistakes, code safety, multimodal AI, Cursor for video editors, vision audio model, intent translation, scene detection, edit decision list, incremental preview, undo redo with reasoning, Shotcut fork, personal life OS agent, deep context, personal knowledge graph, proactive monitoring, value alignment, privacy architecture, predictive planning, decision support, memory consolidation, transparent reasoning, autonomous enterprise workflow agent, event-driven architecture, workflow orchestration, multi-agent delegation, self-healing, audit trail, RBAC, observability, human-in-the-loop, workflow learning, cost management, build in public, unfireable

## Authors
Rohit (@rohit4verse) — créateur de contenu IA sur X, vulgarisateur d'architecture et roadmaps de carrière en ingénierie IA.

## Ton
**Profil** : Thread X (ex-Twitter) au format manifeste-injonctif, registre pédagogique-motivationnel typique des *AI builders* sur X en 2026. Voix à la deuxième personne du singulier ("you must build deep", "don't be most people", "build it this weekend"), tutoiement direct du lecteur. Niveau technique intermédiaire à avancé : suffisamment de jargon (quantization, sliding window, RAG, multi-agent, RBAC, observability) pour signaler la compétence, sans rentrer dans le code. Public cible : développeurs early-mid career qui veulent passer à l'ingénierie IA, candidats à la transition de carrière 2026, audience X intéressée par les roadmaps.

**Style** : Phrases courtes, lowercase typographiquement assumé (esthétique X 2026), refus des majuscules de phrase pour donner un ton conversationnel. Construction par couches : hook viral (*"tutorial hell is a comfortable grave for your career"*), thèse économique (gap 150k$), structure en 5 niveaux gamifiés (beginner → master), aphorismes mémorisables (*"a chatbot waits for a prompt. an agent waits for a goal. the difference is the loop"*, *"the multimodal frontier — text is the past, vision and video are the present"*, *"the era of deep context — an agent that forgets is useless; an agent that knows your life is a partner"*, *"this is the final boss of ai engineering, the portfolio closer"*). Métaphores RPG (*"final boss"*, *"the unfireable"*) et langue de marché (*"sherlocked by big tech"*, référence Apple qui absorbe les features tierces). Closing call-to-action en mode *growth hacking* (*"reply with which project you are starting. i read every response"*) avec promesse d'amplification (*"build in public. tag me when you ship i will amplify it"*).

**Autorité** : construite par la posture (prescription architecturale détaillée), pas par les credentials. Le thread se positionne comme un *blueprint* utilisable directement, ce qui est la promesse classique de l'écosystème *build-in-public* sur X. Tonalité darwinienne assumée : *"the choice is simple: become the architect companies are desperate to hire or become obsolete."* L'éthos est celui du senior IA engineer qui parle aux juniors avec urgence économique. Cette voix s'inscrit dans une lignée 2025-2026 d'auteurs X qui transforment l'inquiétude *AI replacing jobs* en injonction à *shipper du système* — elle complète et rejoint Karpathy (*never felt more behind*), Andreessen (*orchestrating bots*), Sierra (*AI-native engineer*) en version vulgarisée et opérationnelle.

## Pense-betes
- **Date estimée** : avril 2026 (URL X sans date explicite, partagé par l'utilisateur le 2026-04-30).
- **Auteur** : Rohit (@rohit4verse) — créateur de contenu IA sur X, format thread roadmap. Pas de credentials institutionnels mentionnés ; autorité par la pratique et la viralité.
- **Thèse économique centrale** : *"in 2026 the gap between a prompt engineer and a systems architect is 150k."* Roadmap = 5 projets pour franchir le gap.
- **Thèse marché** : *"stop building generic wrappers. the market is flooded with thin layers over gpt. these are not businesses. they are features waiting to be sherlocked by big tech."* Réf. au verbe *to sherlock* (Apple absorbant fonctionnalités d'apps tierces dans le système).
- **Aphorisme structurant agentic** : *"a chatbot waits for a prompt. an agent waits for a goal. the difference is the loop."*
- **Les 5 projets de portfolio** :

### Projet 1 — AI powered mobile app with SLM (beginner)
- **Prouve** : edge AI + resource optimization
- **Décisions architecturales clés** :
  - **Model management** : lazy loading on-demand, unload sous pression mémoire, preload pendant idle.
  - **Context window** : sliding window + semantic chunking, embedding similarity pour décider ce qui reste.
  - **Quantization strategy** : dynamique selon device (4-bit < 2020, 8-bit récents), détection RAM.
  - **Battery optimization** : batch inference, throttle low battery, defer si pas en charge.
  - **Offline-first sync** : encryption locale, sync conditionnel, conflict resolution local-first.
- **Pourquoi ce niveau** : prouve qu'on gère contraintes ressources et edge AI, pas juste API calls.

### Projet 2 — Self-improving coding agent (intermediate)
- **Prouve** : agentic loops + production debugging
- **Décisions architecturales clés** :
  - **Execution loop** : plan → execute → test → reflect avec max iterations, state persisté, circuit breaker.
  - **Sandboxing** : env isolé par tâche, limites CPU/mémoire/temps, FS restreint au project dir.
  - **Memory hierarchy** : short-term (5 dernières iters), long-term (patterns indexés par problem type), failure memory (signatures d'erreur + solutions).
  - **Reflection mechanism** : extract error pattern + root cause, vector similarity vs past failures, hypothesis generation.
  - **Learning from mistakes** : store full context, retrieve similar failures avant tentative, *"avoid repeating the same mistake twice"*.
  - **Code safety** : static analysis pré-exécution, approval explicite pour FS/network.

### Projet 3 — Cursor but for video editors (advanced)
- **Prouve** : multimodal AI + complex tool integration
- **Punch-line** : *"the multimodal frontier — text is the past, vision and video are the present."*
- **Décisions architecturales clés** :
  - **Multimodal understanding** : vision (composition/lighting/subject) + audio (dialogue/musique/ambient), combinaison narrative.
  - **Intent translation** : *"cinematic"* → params concrets (slow pacing 80%, LUT desat, gaussian blur, dramatic music cues).
  - **Scene detection** : frame diff + embedding similarity pour boundaries + story beats.
  - **Edit decision list** : plan complet pré-exécution, validation narrative.
  - **Incremental preview** : ne pas re-render tout, cache segments inchangés.
  - **Feedback incorporation** : "too dark" → analyse histogram → corrections ciblées + apprentissage préférences.
  - **Undo/redo with reasoning** : chaque edit stocke le *pourquoi*, user peut demander "why did you cut here?".
- **Tip explicite** : *"fork an open-source editor like Shotcut."*

### Projet 4 — Personal life OS agent (expert)
- **Prouve** : deep context + privacy-first architecture
- **Punch-line** : *"the era of deep context — the biggest hurdle for ai is memory. an agent that forgets is useless; an agent that knows your life is a partner."*
- **Décisions architecturales clés** :
  - **Continuous context building** : ingest calendar/finance/health/comms temps réel, knowledge graph personnel.
  - **Proactive monitoring** : background thread toutes les 6h, anomalies (meeting density ↑ vs sleep quality ↓).
  - **Value alignment** : priorités explicites (family > work, health > income), recommandations validées contre.
  - **Privacy architecture** : encryption at rest avec clés user-controlled, pas de data sortante sans permission, offline-capable pour sensible.
  - **Predictive planning** : *"based on your q4 pattern, you'll be overcommitted in march."*
  - **Decision support** : analyse multi-dimensionnelle (financier/temps/values/conflicts), reasoning + conclusion.
  - **Memory consolidation** : process nocturne, compression préservant meaning, decay sauf reinforcement.
  - **Transparent reasoning** : *"why i'm recommending this"* avec citations data points, drill-in chain.

### Projet 5 — Autonomous enterprise workflow agent (master)
- **Prouve** : production-grade orchestration
- **Punch-line** : *"this is the final boss of ai engineering, the portfolio closer. an agent that runs a business."*
- **Décisions architecturales clés** :
  - **Event-driven architecture** : listen Slack/Jira/email/monitoring, pattern recognition → workflow templates.
  - **Workflow orchestration** : steps + dépendances, parallélisme où possible, durable state long-running.
  - **Multi-agent delegation** : orchestrator + communication + data + analysis + documentation agents.
  - **Self-healing** : retry vs escalation, exponential backoff, circuit breaker.
  - **Audit trail** : log immuable (what/why/who/outcome), queryable compliance.
  - **RBAC** : permissions de l'invocateur, approval humain pour sensible, scope strict.
  - **Observability** : trace LLM calls (inputs/outputs/latency), metrics success/time/cost, alerts.
  - **Human-in-the-loop** : plan proposé avant exécution critique, escalation si low confidence.
  - **Workflow learning** : evaluation post-completion, patterns successful stockés, templates updatés.
  - **Cost management** : token usage par workflow, budget limits, prompt optimization.
- *"this proves you are ready for a $150k+ salary tier."*

- **Slogan-pivot** : *"the replaceable: building wrappers. the unfireable: shipping autonomous systems."*
- **Closing brutal** : *"build it this weekend. the market rewards shipping, not studying."* + *"document everything: your architecture decisions, your failures and recoveries, your self correction loops, your production deployment."* + *"build in public. tag me when you ship i will amplify it."*
- **PS d'engagement** : *"reply with which project you are starting. i read every response."*

- **Articulation dossier veille** :
  - Vulgarisation et opérationnalisation des thèses portées par Karpathy (*From Vibe Coding to Agentic Engineering*, 2026-04-29) — bascule prompt → systèmes autonomes.
  - Reprend la **distinction** vibe coding / agentic engineering (Karpathy 2026-04-29) en version "carrière" : wrappers (replaceable) vs systèmes (unfireable).
  - Prolonge **Andreessen** (*orchestrating 10 bots*, 2026-02) côté ingénieur individuel.
  - Le projet 4 (*personal life OS agent*) corrobore Karpathy LLM Knowledge Bases + memodb-io *Acontext* (2025-12-11) sur context data platforms.
  - Le projet 5 (*autonomous enterprise workflow agent*) recoupe McKinsey *Reshaping Software Delivery with Agents* (2025-11-23), Stripe Minions (2026-02), StrongDM Software Factory (2026-02-06).
  - **Limites** à signaler dans la lecture : c'est un **thread de growth-hacker / influenceur X**, pas une étude. La densité d'aphorismes performatifs (*"unfireable"*, *"final boss"*) trahit l'intention virale. À utiliser comme **inventaire de patterns architecturaux** mainstream à connaître, pas comme référence académique. Cohérence néanmoins solide avec le consensus 2026 sur agentic systems.

## RésuméDe400mots

Rohit (@rohit4verse) publie sur X un thread-manifeste qui se présente comme *"the 2026 AI engineer roadmap"*. La thèse centrale est économique : en 2026, l'écart de salaire entre un *prompt engineer* (qui assemble des wrappers GPT) et un *systems architect* (qui livre des systèmes autonomes en production) atteint 150k$. Le marché serait saturé de couches fines au-dessus de GPT — *"features waiting to be sherlocked by big tech"*. Pour devenir indispensable, il faut construire profond : orchestration, mémoire, inférence locale.

Le thread propose un blueprint en 5 projets de portfolio classés par complexité, avec pour chacun les décisions architecturales clés.

**Projet 1 — AI mobile app avec SLM (beginner)** : app offline-first avec petits modèles. Prouve la maîtrise edge AI : lazy loading models, sliding window + semantic chunking, dynamic quantization (4-bit anciens devices, 8-bit récents), battery optimization, offline-first sync chiffré.

**Projet 2 — Self-improving coding agent (intermediate)** : agent autonome qui code, teste, apprend de ses échecs. *"A chatbot waits for a prompt. An agent waits for a goal. The difference is the loop."* Boucle plan-execute-test-reflect, sandboxing, memory hierarchy (short-term / long-term / failure memory), reflection mechanism par vector similarity, code safety par static analysis.

**Projet 3 — Cursor but for video editors (advanced)** : *"text is the past, vision and video are the present."* Fork d'éditeur open-source (Shotcut suggéré), agent multimodal qui comprend l'intent ("make this cinematic"), traduit en paramètres concrets (LUT, gaussian blur, dramatic cues), détecte les scènes, génère un edit decision list, propose un undo avec reasoning.

**Projet 4 — Personal life OS agent (expert)** : *"an agent that forgets is useless; an agent that knows your life is a partner."* Knowledge graph personnel construit en continu (calendar, finance, health), proactive monitoring (anomalies détectées toutes les 6h), value alignment explicite, privacy architecture (encryption at rest, offline-capable), predictive planning, transparent reasoning avec citations data points.

**Projet 5 — Autonomous enterprise workflow agent (master)** : *"the final boss of ai engineering."* Agent qui pilote des workflows business end-to-end. Event-driven (Slack/Jira), multi-agent delegation, self-healing avec circuit breaker, audit trail immuable, RBAC, observability complète, human-in-the-loop, workflow learning post-completion, cost management.

Le thread se conclut sur un slogan darwinien : *"the replaceable: building wrappers. the unfireable: shipping autonomous systems."* Appel à shipper le weekend, documenter en public, tag l'auteur pour amplification. Format growth-hacker assumé. À lire comme **inventaire architectural** des patterns 2026 (edge AI, agentic loops, multimodal, deep context, multi-agent orchestration), pas comme étude. La densité d'aphorismes — *"sherlocked"*, *"unfireable"*, *"final boss"* — trahit l'intention virale, mais le contenu technique recoupe le consensus 2026 (Karpathy, Sierra, Stripe Minions, Anthropic).

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Rohit | PERSONNE | publie | 2026 AI engineer roadmap | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Rohit | PERSONNE | affirme_que | gap prompt engineer vs systems architect = 150k$ | CONCEPT | 0.98 | STATIQUE | déclaré_article |
| Generic wrappers | CONCEPT | sont_menacés_par | big tech sherlocking | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| Agent | TECHNOLOGIE | est_défini_par | the loop | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| AI mobile app SLM | METHODOLOGIE | prouve | edge AI + resource optimization | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Self-improving coding agent | METHODOLOGIE | prouve | agentic loops + production debugging | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Video editor agent | METHODOLOGIE | prouve | multimodal AI + tool integration | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Personal life OS agent | METHODOLOGIE | prouve | deep context + privacy-first | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Enterprise workflow agent | METHODOLOGIE | prouve | production-grade orchestration | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Shotcut | TECHNOLOGIE | est_recommandé_pour | fork éditeur vidéo open-source | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| Sliding window + semantic chunking | METHODOLOGIE | gère | context window mobile SLM | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Dynamic quantization | METHODOLOGIE | adapte | modèle au device (4-bit/8-bit) | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Plan-execute-test-reflect | METHODOLOGIE | structure | agentic loop | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Memory hierarchy | METHODOLOGIE | combine | short-term + long-term + failure memory | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Personal knowledge graph | TECHNOLOGIE | structure | deep context personnel | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Event-driven architecture | METHODOLOGIE | déclenche | enterprise workflow | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Multi-agent delegation | METHODOLOGIE | décompose | orchestrator + spécialistes | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Audit trail immuable | METHODOLOGIE | garantit | compliance + debugging | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Rohit | PERSONNE | recommande | build in public + tag pour amplification | METHODOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Shipping autonomous systems | METHODOLOGIE | rend | engineer unfireable | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Building wrappers | METHODOLOGIE | rend | engineer replaceable | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Rohit (@rohit4verse) | PERSONNE | rôle | Créateur de contenu IA sur X, auteur de la 2026 AI engineer roadmap | AJOUT |
| 2026 AI engineer roadmap | CONCEPT | définition | Blueprint en 5 projets pour passer de prompt engineer à systems architect (gap 150k$) | AJOUT |
| Generic wrappers (anti-pattern) | CONCEPT | définition | Couches fines au-dessus de GPT, sans moat, vulnérables au sherlocking par big tech | AJOUT |
| Agentic loop | CONCEPT | définition | Plan → execute → test → reflect avec max iterations, state persisté, circuit breaker | AJOUT |
| AI mobile app SLM | METHODOLOGIE | niveau | Beginner — edge AI + resource optimization (lazy loading, quantization, battery, offline-first) | AJOUT |
| Self-improving coding agent | METHODOLOGIE | niveau | Intermediate — agentic loops + memory hierarchy + reflection mechanism + sandboxing | AJOUT |
| Cursor for video editors | METHODOLOGIE | niveau | Advanced — multimodal AI (vision + audio), intent translation, scene detection, EDL, undo with reasoning | AJOUT |
| Personal life OS agent | METHODOLOGIE | niveau | Expert — deep context, knowledge graph personnel, proactive monitoring, value alignment, privacy architecture, transparent reasoning | AJOUT |
| Autonomous enterprise workflow agent | METHODOLOGIE | niveau | Master — event-driven, multi-agent delegation, self-healing, audit trail, RBAC, observability, HITL, workflow learning, cost management | AJOUT |
| Shotcut | TECHNOLOGIE | catégorie | Éditeur vidéo open-source recommandé comme fork pour le projet 3 | AJOUT |
| Sherlocking | CONCEPT | définition | Pratique des grandes plateformes (orig. Apple) absorbant les fonctionnalités d'apps tierces | AJOUT |
| Replaceable vs Unfireable | CONCEPT | définition | Slogan : building wrappers (replaceable) vs shipping autonomous systems (unfireable) | AJOUT |
