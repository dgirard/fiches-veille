# Opus 4.7

> **Type** : TECHNOLOGIE | 2 relations | 3 fiches sources

## Attributs

- **capabilité** : Refactor 100k lignes, find zero days — mais jagged sur questions simples
- **reasoning_effort_défaut** : xhigh (après correction)
- **score_expert_pass1** : 48,6% (+-10,0%)

## Relations (comme sujet)

### utilise

- [[kb/_entites-mineures#1MM-context-window\|1MM context window]] (CONCEPT) — 0.97, STATIQUE
  - [[fiches/2026-05/shihipar-claude-code-html-unreasonable-effectiveness-markdown-2026-05-10\|Article-manifeste de **Thariq Shihipar** (Engineer & serial entrepreneur, équipe Claude Code chez Anthropic) qui annonce un **changement de format de sortie par défaut pour les agents** : remplacer **Markdown par HTML**. Thèse : Markdown a été le format dominant entre humains et agents (simple, portable, éditable, lisible) mais est devenu **un goulot d'étranglement** à mesure que les agents produisent des artefacts plus longs et plus riches (specs, plans, rapports, code review). Au-delà de ~100 lignes, plus personne ne lit un fichier Markdown. HTML résout six limites simultanément : **densité d'information** (tableaux, CSS, SVG, scripts, canvas, images), **clarté visuelle** (mise en page navigable, responsive mobile), **facilité de partage** (lien S3 directement ouvrable dans un navigateur), **interactivité bidirectionnelle** (sliders, knobs, boutons "copy as JSON/prompt" pour reboucler vers Claude Code), **ingestion contextuelle native** (Claude Code lit codebase + MCP Slack/Linear + git history + Chrome) et **plaisir** (l'auteur revendique explicitement *"it's joyful"*). Cinq usages canoniques détaillés : (1) **specs/plans/exploration** en grille comparative, (2) **PR review** avec diff annoté inline, (3) **design & prototypes** avec sliders d'animation, (4) **rapports/recherche/learning** (l'auteur a fait générer un explainer prompt caching depuis l'historique git), (5) **éditeurs jetables custom** (drag-and-drop de tickets Linear, éditeurs de feature flags, prompt-tuner side-by-side) qui produisent un export "copy as markdown/diff/JSON" reréinjectable. Anti-pattern explicite : *"I'm a little bit afraid that people will read this article and turn it into a /html skill"* — l'auteur **refuse la skill-ification prématurée**, recommande de prompter from scratch ("make a HTML file"). FAQ pragmatique : coût tokens absorbé par les 1 MM context de **Opus 4.7**, génération 2-4× plus longue, diffs HTML bruyants (downside réel), style maîtrisé via design system HTML de référence.]]

## Relations (comme objet)

- [[kb/GPT-5.5\|GPT-5.5]] **surpasse** → Opus 4.7 — 0.95

## Fiches sources

- [[fiches/2026-04/aisi-uk-gpt55-cyber-capabilities-evaluation-2026-04-30\|Evaluation cybersecurite offensive GPT-5.5 par UK AISI — 95 taches CTF, cyber range 32 etapes, jailbreak universel — Blog AISI]]
- [[fiches/2026-04/anthropic-claude-code-quality-postmortem-2026-04-23\|Post-mortem qualité Claude Code mars-avril 2026 — Trois incidents caching/reasoning/prompt — Blog Engineering Anthropic]]
- [[fiches/2026-04/karpathy-vibe-coding-agentic-engineering-software-3-0-2026-04-29\|Interview d'Andrej Karpathy (co-fondateur OpenAI, ex-Tesla Autopilot) qui passe de la *vibe coding* à l'*agentic engineering* : December 2025 comme bascule "never felt more behind as a programmer", taxonomie Software 1.0/2.0/3.0, exemple openclaw (script bash → texte à copier-coller dans l'agent) et MenuGen rendu obsolète par Nanobanana de Gemini, théorie de la *verifiability* expliquant pourquoi les LLMs sont *jagged* (math/code peakent, "marche jusqu'au lavage 50m" échoue), distinction *vibe coding* (raise the floor) vs *agentic engineering* (préserver le quality bar), métaphore "animaux vs fantômes", refonte du recrutement par projets agent-versus-agent, et formule clé : ***"You can outsource your thinking but you can't outsource your understanding."***]]
