# Context Rot

> **Type** : CONCEPT | 5 relations | 3 fiches sources

## Attributs

- **définition** : Dégradation de performance quand le contexte grandit, attention diluée sur trop de tokens
- **nature** : Dégradation du jugement à mesure que la fenêtre de contexte se remplit

## Relations (comme sujet)

### réduit

- [[kb/_entites-mineures#Performance-du-modèle\|Performance du modèle]] (CONCEPT) — 0.95, ATEMPOREL
  - [[fiches/2026-04/thariq-claude-code-session-management-1m-context-2026-04-14\|Gestion de sessions Claude Code : fenêtre 1M tokens, compaction, rewind, subagents et pourriture de contexte]]
- [[kb/_entites-mineures#Performance-de-l'agent\|Performance de l'agent]] (CONCEPT) — 0.92, ATEMPOREL
  - [[fiches/2026-03/trivedy-langchain-anatomy-agent-harness-2026-03-10\|Anatomie d'un harnais d'agent : Agent = Modèle + Harnais, composants fondamentaux et évolution des harnais LangChain]]
- [[kb/_entites-mineures#qualité-du-jugement-à-mesure-que-le-contexte-se-remplit\|qualité du jugement à mesure que le contexte se remplit]] (CONCEPT) — 0.92, DYNAMIQUE
  - [[fiches/2026-06/williams-adlc-1-models-arent-human-2026-06-12\|Chris Williams (@voodootikigod) ouvre sa série ADLC en soutenant que faire tourner le SDLC humain sur des modèles est une erreur de catégorie : le cycle classique a été conçu pour contrer des modes de défaillance humains (ego, fatigue, oubli) absents chez les LLM. Il catalogue huit modes de défaillance porteurs (F1-F8) et cinq propriétés exploitables (E1-E5), et pose le principe fondateur : chaque phase d'un cycle agentique doit se rattacher à un mode de défaillance qu'elle défend ou à une propriété qu'elle exploite.]]

## Relations (comme objet)

- [[kb/_entites-mineures#phase-Decompose\|phase Decompose]] **réduit** → Context Rot — 0.90
- [[kb/Compaction\|Compaction]] **résout** → Context Rot — 0.90

## Fiches sources

- [[fiches/2026-04/thariq-claude-code-session-management-1m-context-2026-04-14\|Gestion de sessions Claude Code : fenêtre 1M tokens, compaction, rewind, subagents et pourriture de contexte]]
- [[fiches/2026-03/trivedy-langchain-anatomy-agent-harness-2026-03-10\|Anatomie d'un harnais d'agent : Agent = Modèle + Harnais, composants fondamentaux et évolution des harnais LangChain]]
- [[fiches/2026-06/williams-adlc-1-models-arent-human-2026-06-12\|Chris Williams (@voodootikigod) ouvre sa série ADLC en soutenant que faire tourner le SDLC humain sur des modèles est une erreur de catégorie : le cycle classique a été conçu pour contrer des modes de défaillance humains (ego, fatigue, oubli) absents chez les LLM. Il catalogue huit modes de défaillance porteurs (F1-F8) et cinq propriétés exploitables (E1-E5), et pose le principe fondateur : chaque phase d'un cycle agentique doit se rattacher à un mode de défaillance qu'elle défend ou à une propriété qu'elle exploite.]]
