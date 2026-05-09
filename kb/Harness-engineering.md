# Harness engineering

> **Type** : METHODOLOGIE | 10 relations | 4 fiches sources

## Attributs

- **catégorie** : Pratique d'ingénierie pour construire la confiance dans les agents de codage
- **définition** : Couche déterministe de contrôle, garde-fous, structuration des informations injectées à l'IA et vérification du code produit
- **période_dominante** : 2026

## Relations (comme sujet)

### converge

- [[kb/_entites-mineures#entre-Claude-Code-Cursor-Codex-Aider-Cline\|entre Claude Code Cursor Codex Aider Cline]] (CONCEPT) — 0.92, ATEMPOREL
  - [[fiches/2026-04/osmani-agent-harness-engineering-2026-04-19\|Synthèse par Addy Osmani (Google, Chrome/Cloud) du champ émergent du *harness engineering* : équation `agent = model + harness`, principe du *ratchet* ("chaque erreur devient une règle"), reframe HumanLayer "skill issue", preuves Terminal Bench (Top 30 → Top 5 par seul changement de harnais), architecture Claude Code en couches, vision Anthropic "harnesses don't shrink, they move" et Harness-as-a-Service (Claude Agent SDK, Codex SDK, OpenAI Agents SDK). Article-pivot qui consolide Trivedy, HumanLayer, Anthropic et Böckeler en doctrine.]]

### est_basé_sur

- [[kb/_entites-mineures#ratchet-principle\|ratchet principle]] (CONCEPT) — 0.95, ATEMPOREL
  - [[fiches/2026-04/osmani-agent-harness-engineering-2026-04-19\|Synthèse par Addy Osmani (Google, Chrome/Cloud) du champ émergent du *harness engineering* : équation `agent = model + harness`, principe du *ratchet* ("chaque erreur devient une règle"), reframe HumanLayer "skill issue", preuves Terminal Bench (Top 30 → Top 5 par seul changement de harnais), architecture Claude Code en couches, vision Anthropic "harnesses don't shrink, they move" et Harness-as-a-Service (Claude Agent SDK, Codex SDK, OpenAI Agents SDK). Article-pivot qui consolide Trivedy, HumanLayer, Anthropic et Böckeler en doctrine.]]

### est_une_forme_de

- [[kb/_entites-mineures#Context-engineering\|Context engineering]] (METHODOLOGIE) — 0.95, ATEMPOREL
  - [[fiches/2026-04/boeckeler-harness-engineering-coding-agents-2026-04-02\|Harness engineering : modèle mental pour construire la confiance dans les agents de codage via guides feedforward et capteurs feedback]]

### repose_sur

- [[kb/_entites-mineures#Contraintes-architecturales\|Contraintes architecturales]] (CONCEPT) — 0.97, ATEMPOREL
  - [[fiches/2026-02/openai-harness-engineering-codex-agent-first-2026-02-13\|Harness engineering OpenAI : 1M lignes de code zéro écriture manuelle, Codex agents, ingénierie d'environnement agent-first]]
- [[kb/_entites-mineures#Ingénierie-de-contexte\|Ingénierie de contexte]] (CONCEPT) — 0.97, ATEMPOREL
  - [[fiches/2026-02/openai-harness-engineering-codex-agent-first-2026-02-13\|Harness engineering OpenAI : 1M lignes de code zéro écriture manuelle, Codex agents, ingénierie d'environnement agent-first]]
- [[kb/_entites-mineures#Garbage-collection\|Garbage collection]] (CONCEPT) — 0.95, ATEMPOREL
  - [[fiches/2026-02/openai-harness-engineering-codex-agent-first-2026-02-13\|Harness engineering OpenAI : 1M lignes de code zéro écriture manuelle, Codex agents, ingénierie d'environnement agent-first]]

### succède_à

- [[kb/_entites-mineures#Context-Engineering\|Context Engineering]] (METHODOLOGIE) — 0.92, STATIQUE
  - [[fiches/2026-05/bfmtv-tech-co-business-ia-developpeurs-disparaissent-2026-05-05\|Débat télévisé sur BFM Business (émission *Tech & Co Business*, segment "Le débat", 17 minutes) avec **Rémi Jacquet** (DG Cast Software France, fondateur en 2023 d'un think tank d'une centaine de DSI sur l'impact de l'IA générative sur le développement, partenariat Cigref / Epita) et **Didier Girard** (CTO et DG de **SFEIR**, ESN française d'environ 1 000 personnes). Thèses fortes : *"écrire du code est devenu un anti-pattern"* (Girard), l'IA produit du code de qualité supérieure à la plupart des ingénieurs et est *"2 à 10× plus efficace"* — c'est une réalité, mais le métier ne disparaît pas. Le développeur devient **chef d'orchestre / manager d'agents / juge de paix**, les sprints de 14 jours sont remplacés par des ***bolts*** d'une heure à une demi-journée, la **Pizza Team** (8-10 personnes) ne fonctionne plus à l'ère agentique, un nouveau métier émerge — le ***product engineer*** —, la durée de vie d'une compétence passe de **10 ans à 1 an**, et la consommation de **tokens** devient le *fuel* de la création de valeur (anecdote NVIDIA qui verserait des primes en tokens, métaphore du chauffeur de taxi qui ne consomme pas d'essence). SFEIR revendique *"1 000 personnes, capacité de production 10 000"*. Côté Cast : positionnement sur le ***harness engineering*** (déterministe vs IA probabiliste, contrôle et garde-fous), aligné sur la tribune Sylvain Duranton (BCG X) dans *Les Échos* selon laquelle *"un agent = un LLM + des harnesses"*. Pivot historique 2024 *prompt engineering* → 2025 *context engineering* → 2026 *harness engineering*. Avertissement clé : *"plus l'IA devient forte, plus on baisse la garde — plus il y a de risques"* (Jacquet). Rôle pivot des DRH dans la transformation, remise à plat complète du SDLC, recommandation aux juniors de bétonner les fondamentaux d'architecture logicielle (*"le code est la partition, il faut maîtriser la symphonie"*).]]

### utilise

- [[kb/_entites-mineures#Capteurs-feedback\|Capteurs feedback]] (CONCEPT) — 0.98, ATEMPOREL
  - [[fiches/2026-04/boeckeler-harness-engineering-coding-agents-2026-04-02\|Harness engineering : modèle mental pour construire la confiance dans les agents de codage via guides feedforward et capteurs feedback]]
- [[kb/_entites-mineures#Guides-feedforward\|Guides feedforward]] (CONCEPT) — 0.98, ATEMPOREL
  - [[fiches/2026-04/boeckeler-harness-engineering-coding-agents-2026-04-02\|Harness engineering : modèle mental pour construire la confiance dans les agents de codage via guides feedforward et capteurs feedback]]

## Relations (comme objet)

- [[kb/_entites-mineures#Cast-Software\|Cast Software]] **propose** → Harness engineering — 0.95

## Fiches sources

- [[fiches/2026-05/bfmtv-tech-co-business-ia-developpeurs-disparaissent-2026-05-05\|Débat télévisé sur BFM Business (émission *Tech & Co Business*, segment "Le débat", 17 minutes) avec **Rémi Jacquet** (DG Cast Software France, fondateur en 2023 d'un think tank d'une centaine de DSI sur l'impact de l'IA générative sur le développement, partenariat Cigref / Epita) et **Didier Girard** (CTO et DG de **SFEIR**, ESN française d'environ 1 000 personnes). Thèses fortes : *"écrire du code est devenu un anti-pattern"* (Girard), l'IA produit du code de qualité supérieure à la plupart des ingénieurs et est *"2 à 10× plus efficace"* — c'est une réalité, mais le métier ne disparaît pas. Le développeur devient **chef d'orchestre / manager d'agents / juge de paix**, les sprints de 14 jours sont remplacés par des ***bolts*** d'une heure à une demi-journée, la **Pizza Team** (8-10 personnes) ne fonctionne plus à l'ère agentique, un nouveau métier émerge — le ***product engineer*** —, la durée de vie d'une compétence passe de **10 ans à 1 an**, et la consommation de **tokens** devient le *fuel* de la création de valeur (anecdote NVIDIA qui verserait des primes en tokens, métaphore du chauffeur de taxi qui ne consomme pas d'essence). SFEIR revendique *"1 000 personnes, capacité de production 10 000"*. Côté Cast : positionnement sur le ***harness engineering*** (déterministe vs IA probabiliste, contrôle et garde-fous), aligné sur la tribune Sylvain Duranton (BCG X) dans *Les Échos* selon laquelle *"un agent = un LLM + des harnesses"*. Pivot historique 2024 *prompt engineering* → 2025 *context engineering* → 2026 *harness engineering*. Avertissement clé : *"plus l'IA devient forte, plus on baisse la garde — plus il y a de risques"* (Jacquet). Rôle pivot des DRH dans la transformation, remise à plat complète du SDLC, recommandation aux juniors de bétonner les fondamentaux d'architecture logicielle (*"le code est la partition, il faut maîtriser la symphonie"*).]]
- [[fiches/2026-04/boeckeler-harness-engineering-coding-agents-2026-04-02\|Harness engineering : modèle mental pour construire la confiance dans les agents de codage via guides feedforward et capteurs feedback]]
- [[fiches/2026-02/openai-harness-engineering-codex-agent-first-2026-02-13\|Harness engineering OpenAI : 1M lignes de code zéro écriture manuelle, Codex agents, ingénierie d'environnement agent-first]]
- [[fiches/2026-04/osmani-agent-harness-engineering-2026-04-19\|Synthèse par Addy Osmani (Google, Chrome/Cloud) du champ émergent du *harness engineering* : équation `agent = model + harness`, principe du *ratchet* ("chaque erreur devient une règle"), reframe HumanLayer "skill issue", preuves Terminal Bench (Top 30 → Top 5 par seul changement de harnais), architecture Claude Code en couches, vision Anthropic "harnesses don't shrink, they move" et Harness-as-a-Service (Claude Agent SDK, Codex SDK, OpenAI Agents SDK). Article-pivot qui consolide Trivedy, HumanLayer, Anthropic et Böckeler en doctrine.]]
