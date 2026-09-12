# hooks

> **Type** : TECHNOLOGIE | 7 relations | 3 fiches sources

## Attributs

- **rôle** : Commandes déclenchées à des points fixes du cycle de vie de Claude Code, servant de portes dures indépendantes de la décision du modèle
- **usage** : check-file-size bloque les Read au-delà de 350 lignes (SHUNT_MIN_LINES) ; check-bash-read intercepte cat, head, tail, less, more ; lectures ciblées et commandes pipées exemptées

## Relations (comme sujet)

### améliore

- [[kb/Claude-Skills\|Claude Skills]] (TECHNOLOGIE) — 0.88, ATEMPOREL
  - [[fiches/2026-08/claxton-anthropic-ai-native-sdlc-playbook-2026-08-21\|The AI-Native SDLC playbook: How to transform your software development lifecycle with AI—stage by stage]]

### est_basé_sur

- [[kb/_entites-mineures#Success-is-silent-failures-are-verbose\|Success is silent failures are verbose]] (CONCEPT) — 0.95, ATEMPOREL
  - [[fiches/2026-04/osmani-agent-harness-engineering-2026-04-19\|Agent Harness Engineering]]

### fait_partie_de

- harness de l'agent (CONCEPT) — 0.94, ATEMPOREL
  - [[fiches/2026-07/lassiege-usine-logicielle-heure-ia-2026-07-28\|Mon usine logicielle à l'heure de l'IA]]

### permet

- « blocage des lectures au-delà de 350 lignes par défaut » (AFFIRMATION) — 0.93, ATEMPOREL
  - [[fiches/2026-09/mazmanov-portal-spotify-shunt-claude-code-tokens-2026-09-03\|Portal by Spotify cut my Claude Code token usage by 90%]]
- « portes dures s'exécutant à chaque fois quelle que soit la décision du modèle : lint bloquant, test avant commit, retrait des secrets » (AFFIRMATION) — 0.92, ATEMPOREL
  - [[fiches/2026-08/segner-anthropic-claude-code-guide-startups-2026-08-20\|The Claude Code guide for startups]]

### s_applique_à

- événements PreToolUse et PostToolUse (CONCEPT) — 0.93, ATEMPOREL
  - [[fiches/2026-02/maitriser-claude-code-formation-pedagogique-deep-research-2026-02\|Maîtriser Claude Code — Détail complet des 12 modules et ~60 leçons]]

## Relations (comme objet)

- [[kb/shunt\|shunt]] **utilise** → hooks — 0.95

## Fiches sources

- [[fiches/2026-08/claxton-anthropic-ai-native-sdlc-playbook-2026-08-21\|The AI-Native SDLC playbook: How to transform your software development lifecycle with AI—stage by stage]]
- [[fiches/2026-09/mazmanov-portal-spotify-shunt-claude-code-tokens-2026-09-03\|Portal by Spotify cut my Claude Code token usage by 90%]]
- [[fiches/2026-08/segner-anthropic-claude-code-guide-startups-2026-08-20\|The Claude Code guide for startups]]
