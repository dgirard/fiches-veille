# ADLC

> **Type** : METHODOLOGIE | 5 relations | 1 fiches sources

## Attributs

- **définition** : Agentic Development Lifecycle — cycle conçu autour des propriétés et défaillances des modèles
- **principe** : Chaque phase trace à un mode de défaillance défendu ou une propriété exploitée

## Relations (comme sujet)

### affirme_que

- « chaque phase doit tracer à un mode de défaillance défendu ou une propriété exploitée » (AFFIRMATION) — 0.95, ATEMPOREL
  - [[fiches/2026-06/williams-adlc-1-models-arent-human-2026-06-12\|Chris Williams (@voodootikigod) ouvre sa série ADLC en soutenant que faire tourner le SDLC humain sur des modèles est une erreur de catégorie : le cycle classique a été conçu pour contrer des modes de défaillance humains (ego, fatigue, oubli) absents chez les LLM. Il catalogue huit modes de défaillance porteurs (F1-F8) et cinq propriétés exploitables (E1-E5), et pose le principe fondateur : chaque phase d'un cycle agentique doit se rattacher à un mode de défaillance qu'elle défend ou à une propriété qu'elle exploite.]]
- « « replace trust with structure, and structure with measurement » » (CITATION) — 0.94, ATEMPOREL
  - [[fiches/2026-06/williams-adlc-7-built-with-the-lifecycle-2026-06-12\|Septième et dernier volet ADLC : Williams présente un toolkit open-source de dix-huit outils construit *avec* le cycle lui-même (boucle build-prosecute-fix, agents parallèles, core `@adlc/core` gelé puis fan-out — « pinned means merged »). Le cœur doctrinal est « frontier-free » : atteindre les cibles de précision avec des modèles mid-tier (Opus/Sonnet/Haiku-class) plutôt que frontier, via cinq substitutions (search remplace insight, décomposition remplace horizon, banking remplace présence, mesure remplace métacognition, le generator-verifier gap fait tourner le moteur), l'humain restant le tier « frontier » sur les deux portes de spec. Fil rouge de la série : « replace trust with structure, and structure with measurement. »]]

### fait_partie_de

- [[kb/_entites-mineures#cycle-agentique-en-huit-phases\|cycle agentique en huit phases]] (METHODOLOGIE) — 0.95, ATEMPOREL
  - [[fiches/2026-06/williams-adlc-2-two-human-gates-2026-06-12\|Deuxième volet de la série ADLC de Chris Williams : il déroule le cycle qui découle de la « première loi » — huit phases (P0 Triage → P7 Distill), un gate déterministe entre chaque paire, et exactement deux moments humains obligatoires (approbation de la spec en P1, acceptation comportementale en P6). Principe clé : un handoff LLM→LLM sans checkpoint déterministe multiplie les taux d'erreur ; et une distribution des coûts « en haltère » (lourde aux deux bouts, légère au milieu) qui inverse l'économie agile.]]

### s_oppose_à

- [[kb/SDLC\|SDLC]] (METHODOLOGIE) — 0.92, ATEMPOREL
  - [[fiches/2026-06/williams-adlc-1-models-arent-human-2026-06-12\|Chris Williams (@voodootikigod) ouvre sa série ADLC en soutenant que faire tourner le SDLC humain sur des modèles est une erreur de catégorie : le cycle classique a été conçu pour contrer des modes de défaillance humains (ego, fatigue, oubli) absents chez les LLM. Il catalogue huit modes de défaillance porteurs (F1-F8) et cinq propriétés exploitables (E1-E5), et pose le principe fondateur : chaque phase d'un cycle agentique doit se rattacher à un mode de défaillance qu'elle défend ou à une propriété qu'elle exploite.]]
- [[kb/_entites-mineures#revue-humaine-de-diff-complet-au-delà-de-500-lignes\|revue humaine de diff complet au-delà de 500 lignes]] (CONCEPT) — 0.90, ATEMPOREL
  - [[fiches/2026-06/williams-adlc-2-two-human-gates-2026-06-12\|Deuxième volet de la série ADLC de Chris Williams : il déroule le cycle qui découle de la « première loi » — huit phases (P0 Triage → P7 Distill), un gate déterministe entre chaque paire, et exactement deux moments humains obligatoires (approbation de la spec en P1, acceptation comportementale en P6). Principe clé : un handoff LLM→LLM sans checkpoint déterministe multiplie les taux d'erreur ; et une distribution des coûts « en haltère » (lourde aux deux bouts, légère au milieu) qui inverse l'économie agile.]]

## Fiches sources

- [[fiches/2026-06/williams-adlc-1-models-arent-human-2026-06-12\|Chris Williams (@voodootikigod) ouvre sa série ADLC en soutenant que faire tourner le SDLC humain sur des modèles est une erreur de catégorie : le cycle classique a été conçu pour contrer des modes de défaillance humains (ego, fatigue, oubli) absents chez les LLM. Il catalogue huit modes de défaillance porteurs (F1-F8) et cinq propriétés exploitables (E1-E5), et pose le principe fondateur : chaque phase d'un cycle agentique doit se rattacher à un mode de défaillance qu'elle défend ou à une propriété qu'elle exploite.]]
