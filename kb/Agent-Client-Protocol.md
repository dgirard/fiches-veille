# Agent Client Protocol

> **Type** : TECHNOLOGIE | 24 relations | 3 fiches sources

## Attributs

- **définition** : Protocole ouvert reliant un client (éditeur) à un agent de codage ; JSON-RPC 2.0 sur stdio, Apache-2.0, introduit par Zed en août 2025 — le « LSP des agents ». Alias « ACP » (homonyme, à ne jamais employer seul)
- **gouvernance** : Site liant Zed Industries et JetBrains au même niveau, avec ACP Registry, RFDs, Community, Publications, Updates et Brand ; bibliothèques Kotlin, Java, Python, Rust, TypeScript
- **rôle** : Protocole d'interopérabilité client↔agent accepté par Buzz : tout agent qui le parle peut travailler dans le workspace, aux côtés de Claude Code, Codex et goose
- **spécification** : Deux modes de transport : agents locaux en JSON-RPC sur stdio, agents distants en HTTP ou WebSocket (support en cours) ; réutilise les représentations JSON de MCP ; Markdown par défaut ; versions v1 (Latest) et v2 (Draft)

## Relations (comme sujet)

### affirme_que

- « le support complet des agents distants est encore un travail en cours » (AFFIRMATION) — 0.93, DYNAMIQUE
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]

### converge_avec

- [[kb/Model-Context-Protocol\|Model Context Protocol]] (TECHNOLOGIE) — 0.90, ATEMPOREL
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]

### est_basé_sur

- « les représentations JSON de Model Context Protocol » (AFFIRMATION) — 0.93, ATEMPOREL
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]

### permet

- « de standardiser la communication entre éditeurs de code et agents de codage » (AFFIRMATION) — 0.98, ATEMPOREL
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]
- « de relier un client à un agent, en découplant l'éditeur de l'agent » (AFFIRMATION) — 0.96, ATEMPOREL
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
- « de changer d'agent ou de fournisseur sans changer d'éditeur » (AFFIRMATION) — 0.94, ATEMPOREL
  - [[fiches/2026-05/dethlefsen-zed-anthropic-subscription-changes-2026-05-14\|What Anthropic's New Claude Billing Means for Zed Users]]
- « l'affichage de diffs et autres éléments d'UX propres au codage agentique » (AFFIRMATION) — 0.90, ATEMPOREL
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]

### publie

- « une spécification versionnée v1 (Latest) et v2 (Draft) » (AFFIRMATION) — 0.90, DYNAMIQUE
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]

### réduit

- « l'integration overhead, la compatibilité limitée et le verrouillage développeur » (AFFIRMATION) — 0.94, ATEMPOREL
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]
- « le nombre d'intégrations de N×M à N+M » (AFFIRMATION) — 0.94, ATEMPOREL
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]

### résout

- « le couplage étroit entre agents de codage et éditeurs » (AFFIRMATION) — 0.95, ATEMPOREL
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]

### s_inspire_de

- [[kb/_entites-mineures#Language-Server-Protocol\|Language Server Protocol]] (TECHNOLOGIE) — 0.96, ATEMPOREL
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]

### utilise

- JSON-RPC sur stdio (TECHNOLOGIE) — 0.95, ATEMPOREL
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]
- JSON-RPC 2.0 sur stdio (TECHNOLOGIE) — 0.94, ATEMPOREL
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
- Markdown (TECHNOLOGIE) — 0.92, ATEMPOREL
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]
- HTTP ou WebSocket pour les agents distants (TECHNOLOGIE) — 0.90, DYNAMIQUE
  - [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]

## Relations (comme objet)

- [[kb/Zed\|Zed]] **utilise** → Agent Client Protocol — 0.96
- [[kb/Zed\|Zed]] **a_créé** → Agent Client Protocol — 0.95
- [[kb/Buzz\|Buzz]] **utilise** → Agent Client Protocol — 0.95
- [[kb/_entites-mineures#buzz-acp\|buzz-acp]] **utilise** → Agent Client Protocol — 0.95
- JetBrains **utilise** → Agent Client Protocol — 0.92
- Zed Industries **a_créé** → Agent Client Protocol — 0.90
- [[kb/_entites-mineures#ACP-Registry\|ACP Registry]] **fait_partie_de** → Agent Client Protocol — 0.88
- Nous Research **utilise** → Agent Client Protocol — 0.88

## Fiches sources

- [[fiches/2026-08/agentclientprotocol-introduction-2026-08-02\|Agent Client Protocol — Introduction]]
- [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
- [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
