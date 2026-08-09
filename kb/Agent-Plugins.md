# Agent Plugins

> **Type** : TECHNOLOGIE | 16 relations | 1 fiches sources

## Attributs

- **définition** : Spécification ouverte et vendor-neutral (v1.0.0) empaquetant Agent Skills et serveurs MCP dans un répertoire portable : plugin.json réduit à $schema et name, skills/ au format Agent Skills, mcp.json avec type explicite par entrée, et un espace d'extension en domaine inversé par client
- **gouvernance** : Publiée par un TSC de Core Maintainers issus d'Amazon, Cursor, Microsoft, OpenAI et Vercel ; Google rejoint le groupe le 6 août 2026, représenté par Kevin Hou. Anthropic, à l'origine d'Agent Skills et de MCP, ne figure pas dans la liste des mainteneurs citée
- **limites** : La v1 ne définit ni installation, ni protocole de distribution, ni modèle de permissions, ni exigence de bac à sable, ni vérification de confiance ou de provenance, ni expérience utilisateur : ces responsabilités reviennent au client

## Relations (comme sujet)

### permet

- « d'empaqueter des Agent Skills et des serveurs MCP dans un plugin portable d'un client à l'autre » (AFFIRMATION) — 0.97, ATEMPOREL
  - [[fiches/2026-08/google-agent-plugins-packaging-skills-mcp-2026-08-06\|Agent Plugins package your skills, tools, and more]]
- « l'échec indépendant des composants : un serveur mcp.json qui ne démarre pas n'emporte pas les skills du plugin » (AFFIRMATION) — 0.95, ATEMPOREL
  - [[fiches/2026-08/google-agent-plugins-packaging-skills-mcp-2026-08-06\|Agent Plugins package your skills, tools, and more]]

### réduit

- « la surface de divergence entre implémentations, en supprimant les chemins de découverte configurables et les ordres de précédence » (AFFIRMATION) — 0.91, ATEMPOREL
  - [[fiches/2026-08/google-agent-plugins-packaging-skills-mcp-2026-08-06\|Agent Plugins package your skills, tools, and more]]

### résout

- « la duplication et la dérive des packages forkés pour chaque client » (AFFIRMATION) — 0.94, ATEMPOREL
  - [[fiches/2026-08/google-agent-plugins-packaging-skills-mcp-2026-08-06\|Agent Plugins package your skills, tools, and more]]

### s_oppose_à

- « la prise en charge de l'installation, de la distribution, des permissions, du bac à sable, de la vérification de provenance et de l'expérience utilisateur » (AFFIRMATION) — 0.96, DYNAMIQUE
  - [[fiches/2026-08/google-agent-plugins-packaging-skills-mcp-2026-08-06\|Agent Plugins package your skills, tools, and more]]

### utilise

- [[kb/Agent-Skills\|Agent Skills]] (TECHNOLOGIE) — 0.96, ATEMPOREL
  - [[fiches/2026-08/google-agent-plugins-packaging-skills-mcp-2026-08-06\|Agent Plugins package your skills, tools, and more]]
- [[kb/Model-Context-Protocol\|Model Context Protocol]] (TECHNOLOGIE) — 0.96, ATEMPOREL
  - [[fiches/2026-08/google-agent-plugins-packaging-skills-mcp-2026-08-06\|Agent Plugins package your skills, tools, and more]]
- « un répertoire à emplacements fixes plutôt qu'un manifeste expressif : plugin.json ne peut ni relocaliser ni déclarer les composants en ligne » (AFFIRMATION) — 0.95, ATEMPOREL
  - [[fiches/2026-08/google-agent-plugins-packaging-skills-mcp-2026-08-06\|Agent Plugins package your skills, tools, and more]]

## Relations (comme objet)

- [[kb/Google\|Google]] **collabore_avec** → Agent Plugins — 0.97
- [[kb/_entites-mineures#Agents-CLI\|Agents CLI]] **utilise** → Agent Plugins — 0.95
- [[kb/_entites-mineures#Data-Agent-Kit\|Data Agent Kit]] **utilise** → Agent Plugins — 0.95
- [[kb/Amazon\|Amazon]] **publie** → Agent Plugins — 0.90
- [[kb/Cursor-organisation\|Cursor]] **publie** → Agent Plugins — 0.90
- [[kb/Microsoft\|Microsoft]] **publie** → Agent Plugins — 0.90
- [[kb/OpenAI\|OpenAI]] **publie** → Agent Plugins — 0.90
- [[kb/Vercel\|Vercel]] **publie** → Agent Plugins — 0.90

## Fiches sources

- [[fiches/2026-08/google-agent-plugins-packaging-skills-mcp-2026-08-06\|Agent Plugins package your skills, tools, and more]]
