# Plan mode

> **Type** : METHODOLOGIE | 7 relations | 6 fiches sources

## Attributs

- **activation** : Shift+Tab dans Claude Code
- **description** : Conserve tous les outils + system message au lieu de swapper les outils
- **définition** : Mode non-exécution pour planification et recherche codebase
- **effet** : Double ou triple le taux de succès sur tâches complexes
- **usage** : Planification préalable avant implémentation complexe

## Relations (comme sujet)

### améliore

- [[kb/_entites-mineures#qualité-implémentation\|qualité implémentation]] (CONCEPT) — 0.90, ATEMPOREL
  - [[fiches/2026-02/cherny-claude-code-10-tips-team-x-2026-02-01\|Conseils utilisation Claude Code par équipe Anthropic - 10 astuces productivité]]

### permet

- [[kb/_entites-mineures#stabilité-du-cache\|stabilité du cache]] (CONCEPT) — 0.96, ATEMPOREL
  - [[fiches/2026-02/trq212-anthropic-claude-code-prompt-caching-lessons-2026-02\|Leçons prompt caching Claude Code : architecture cache, plan mode, compaction, optimisation coûts et latence]]
- [[kb/_entites-mineures#exploration-read-only-avant-code\|exploration read-only avant code]] (CONCEPT) — 0.93, ATEMPOREL
  - [[fiches/2026-01/osmani-how-write-good-spec-ai-agents-2026-01-13\|Addy Osmani - écrire specs pour agents IA, 5 principes, Plan Mode, PRD structuré, modularité]]

### utilise

- [[kb/_entites-mineures#EnterPlanMode-ExitPlanMode-comme-outils\|EnterPlanMode/ExitPlanMode comme outils]] (TECHNOLOGIE) — 0.95, STATIQUE
  - [[fiches/2026-02/trq212-anthropic-claude-code-prompt-caching-lessons-2026-02\|Leçons prompt caching Claude Code : architecture cache, plan mode, compaction, optimisation coûts et latence]]

## Relations (comme objet)

- [[kb/_entites-mineures#Plan-subagent\|Plan subagent]] **s_applique_à** → Plan mode — 0.97
- [[kb/Boris-Cherny\|Boris Cherny]] **recommande** → Plan mode — 0.96
- [[kb/Boris-Cherny\|Boris Cherny]] **a_créé** → Plan mode — 0.95

## Fiches sources

- [[fiches/2026-02/cherny-claude-code-10-tips-team-x-2026-02-01\|Conseils utilisation Claude Code par équipe Anthropic - 10 astuces productivité]]
- [[fiches/2026-02/cherny-yc-lightcone-claude-code-origin-story-2026-02\|Boris Cherny raconte la genèse de Claude Code, philosophie produit et conseils fondateurs - Y Combinator Light Cone]]
- [[fiches/2025-09/claude-code-subagents-documentation-anthropic-2025-09-29\|Subagents Claude Code - Assistants IA spécialisés - Gestion du contexte - Délégation de tâches - Documentation Anthropic]]
- [[fiches/2026-01/osmani-how-write-good-spec-ai-agents-2026-01-13\|Addy Osmani - écrire specs pour agents IA, 5 principes, Plan Mode, PRD structuré, modularité]]
- [[fiches/2026-02/trq212-anthropic-claude-code-prompt-caching-lessons-2026-02\|Leçons prompt caching Claude Code : architecture cache, plan mode, compaction, optimisation coûts et latence]]
- [[fiches/2025-10/wu-cherny-use-claude-code-builders-every-2025-10-29\|Cat Wu et Boris Cherny (Anthropic) expliquent comment utiliser Claude Code comme ses créateurs : antfooding, plan mode, subagents, hooks et extensibilité — podcast AI & I d'Every]]
