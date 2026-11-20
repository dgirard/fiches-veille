# REVIEW.md

> **Type** : DOCUMENT | 4 relations | 3 fiches sources

## Attributs

- **définition** : Fichier écrit par les code owners qui dit au relecteur IA ce qui compte dans leur partie du code
- **règle** : Lu depuis la branche de base, jamais depuis les changements de la PR
- **rôle** : Doctrine de revue : passes bugs/sécurité/conformité, définition de « Important », plafond de nits

## Relations (comme sujet)

### réduit

- modification par l'agent des règles qui le jugent (CONCEPT) — 0.86, ATEMPOREL
  - [[fiches/2026-11/sfeir-verification-code-agents-claude-code-2026-11-19\|Comment l'équipe Claude Code vérifie le code écrit par ses agents]]

### s_applique_à

- passes de revue bugs, sécurité et conformité au spec et au plan (CONCEPT) — 0.89, ATEMPOREL
  - [[fiches/2026-08/claxton-anthropic-ai-native-sdlc-playbook-2026-08-21\|The AI-Native SDLC playbook: How to transform your software development lifecycle with AI—stage by stage]]

## Relations (comme objet)

- [[kb/revue-de-code-agentique\|revue de code agentique]] **utilise** → REVIEW.md — 0.92
- [[kb/Claude-Code\|Claude Code]] **utilise** → REVIEW.md — 0.88

## Fiches sources

- [[fiches/2026-08/claxton-anthropic-ai-native-sdlc-playbook-2026-08-21\|The AI-Native SDLC playbook: How to transform your software development lifecycle with AI—stage by stage]]
- [[fiches/2026-10/osmani-lunt-wang-code-review-claude-code-2026-10-15\|How the Claude Code team does code review]]
- [[fiches/2026-11/sfeir-verification-code-agents-claude-code-2026-11-19\|Comment l'équipe Claude Code vérifie le code écrit par ses agents]]
