# MCP

> **Type** : TECHNOLOGIE | 17 relations | 11 fiches sources

## Attributs

- **categorie** : Protocole exposition services pour agents
- **catégorie** : Model Context Protocol
- **date_lancement** : Novembre 2024
- **forme_longue** : Model Context Protocol
- **limite** : Interactions semi-typées perdant de la fidélité par rapport aux domain objects
- **nature** : protocole ouvert
- **nom complet** : Model Context Protocol
- **objectif** : accès structuré aux outils/données/API pour agents IA

## Relations (comme sujet)

### est_instance_de

- [[kb/_entites-mineures#protocole-ouvert\|protocole ouvert]] (CONCEPT) — 0.97, STATIQUE
  - [[fiches/2025-09/mcp-replaces-browser-logrocket-2025-09-15\|MCP remplace le navigateur - Interactions agents IA - Développeurs frontend - LogRocket Blog]]

### permet

- [[kb/_entites-mineures#accès-structuré-des-agents-IA-aux-outils-et-données\|accès structuré des agents IA aux outils et données]] (CONCEPT) — 0.98, ATEMPOREL
  - [[fiches/2025-09/mcp-replaces-browser-logrocket-2025-09-15\|MCP remplace le navigateur - Interactions agents IA - Développeurs frontend - LogRocket Blog]]
- [[kb/_entites-mineures#connexion-à-outils-externes\|connexion à outils externes]] (CONCEPT) — 0.95, DYNAMIQUE
  - [[fiches/2026-02/maitriser-claude-code-formation-pedagogique-deep-research-2026-02\|Formation complète Claude Code : 12 modules pédagogiques coding agentique - Deep Research]]
- [[kb/_entites-mineures#interaction-standardisée-avec-systèmes-externes\|interaction standardisée avec systèmes externes]] (CONCEPT) — 0.95, DYNAMIQUE
  - [[fiches/2025-11/lesse-anthropic-building-agentic-systems-claude-2025-11-23\|Construction de systèmes agentiques puissants avec Claude - Architecture et patterns d'implémentation - Anthropic]]
- [[kb/_entites-mineures#connexion-de-Claude-à-GSC-Ahrefs-GA4\|connexion de Claude à GSC / Ahrefs / GA4]] (CONCEPT) — 0.94, DYNAMIQUE
  - [[fiches/2026-05/pillitteri-opus-4-8-seo-workflow-deux-phases-2026-05-29\|Article du blog de **Pasquale Pillitteri** (ingénieur informatique, Palermo) publié le **29 mai 2026** (version FR), 18 min de lecture, rubrique *Claude Code & Anthropic*. **Thèse-pivot** : *« Claude Opus 4.8 est le modèle SEO le plus puissant de 2026, mais presque tout le monde l'utilise mal »* — non pas un problème de modèle mais de **système**. La règle d'or : ***« la stratégie est un tableau blanc, la production est une chaîne de montage »*** — il faut **scinder le SEO en deux phases distinctes**, et les mélanger est *« le moyen le plus rapide de gaspiller un modèle qui coûte cinq dollars par million de tokens en entrée et vingt-cinq en sortie »*. **Contexte modèle** : Opus 4.8 publié le **28 mai 2026** (41 jours après Opus 4.7), contexte **1M tokens**, **GraphWalks Long-Context F1 à 1M : 40,3 % → 68,1 %**, **SWE-bench Verified 88,6 %**, **USAMO 2026 96,7 %** (+27,4 pts), **HLE avec tool 57,9 %**, prix inchangé **5 $/25 $** par M tokens, **Fast Mode 2,5× à 10 $/50 $**, quatre **effort levels** (Low, High, Extra, Max). **L'anti-pattern central** = *« la conversation géante »* / **dérive du contexte** : mélanger stratégie, keyword research, analyse concurrentielle et rédaction dans un seul chat produit une *« bouillie d'intentions contradictoires »* → le modèle glisse vers les **best practices génériques** (« optimisation holistique », « approche stratégique ») au lieu d'un contenu ancré aux données. **Phase 1 — Stratégie (tableau blanc, UI visuelle, one-off)** : dashboard / Google Sheet / canvas Claude.ai pour décider en voyant les données ensemble. **3 plays** : (a) **keyword research classifiée** (tableau volume / difficulté 0-100 / intention / potentiel business / priorité = volume÷difficulté×poids business) ; (b) **analyse concurrentielle visuelle** (matrice de couverture thématique, gaps) ; (c) **roadmap par phases** (quick wins M1-2 / moyen terme M3-6 / pillar pages M7-12). Mode **Extra/Max** justifié ici (*« une décision stratégique juste vaut mille pages bien écrites sur des mots-clés erronés »*). 3 artefacts fermés sauvegardés sur Notion/Drive. **Phase 2 — Production (chaîne de montage, Opus 4.8 + MCP)** : le modèle passe de stratège à **machine d'exécution** ; chaque décision **ancrée à des données live** via **Model Context Protocol**. **Stack MCP minimum** : **GSC MCP** (AminForou/mcp-gsc, 500+ étoiles), **Ahrefs MCP officiel** (98 étoiles), **GA4 MCP** ; repo `modelcontextprotocol/servers` = **86 440 étoiles**, **10 000+ serveurs actifs**, 97M téléchargements SDK/mois. Setup ~35 min, refresh mensuel ~20 min. **Loop hebdomadaire** : un prompt unique tire les données live, construit le brief (top 10 SERP + GSC + Ahrefs), dérive H2/H3, écrit, contrôle densité, suggère titres → **+45 % productivité**, draft en **6-12 min** (référence explicite au **content engineering de Ryan Law / Ahrefs**, 23 skills). Mention des **Dynamic Workflows** Anthropic (jusqu'à 1 000 subagents). **4 erreurs courantes** : (1) ne pas vérifier les chiffres (spot-check obligatoire, *trust & verify*) ; (2) remplacer complètement Semrush/Ahrefs (le MCP est une **couche par-dessus**, pas un substitut) ; (3) ignorer le **content gap paid-organic** (cas client education : **2 742 termes gaspillés / 351 opportunités** identifiés en 90 s) ; (4) utiliser Opus 4.8 là où **Haiku 4.5** suffit (meta descriptions, alt text). **Coût** : 1-3 $/article de 2 500 mots. **Sonnet 4.6** suffit pour la production récurrente, Opus 4.8 réservé à la stratégie. Article SEO-optimisé et auto-référentiel (l'auteur écrit sur le SEO un contenu lui-même conçu pour se positionner sur « Opus 4.8 SEO »). Convergence directe avec **Ryan Law/Ahrefs** (cité), **systems around the model** (Dropbox/Okumura), **skills-over-prompts** (Lattice), routage modèle Haiku/Sonnet/Opus (Gupta token-to-outcome).]]
- [[kb/_entites-mineures#exposition-services-aux-agents\|exposition services aux agents]] (CONCEPT) — 0.88, ATEMPOREL
  - [[fiches/2026-03/levie-building-trillions-agents-software-2026-03-07\|Construire pour des trillions d'agents : logiciel API-first, infrastructure agentique, nouveau paradigme logiciel - X/Twitter]]
- [[kb/_entites-mineures#intégration-Gemini-CLI\|intégration Gemini CLI]] (TECHNOLOGIE) — 0.85, DYNAMIQUE
  - [[fiches/2025-06/gemini-cli-claude-code-hybrid-workflow-reddit-2025-06-23\|Gemini CLI + Claude Code - Workflow hybride - Large codebase analysis - Context window - Reddit ChatGPTCoding]]

### remplace

- [[kb/_entites-mineures#navigateur-web\|navigateur web]] (TECHNOLOGIE) — 0.85, DYNAMIQUE
  - [[fiches/2025-09/mcp-replaces-browser-logrocket-2025-09-15\|MCP remplace le navigateur - Interactions agents IA - Développeurs frontend - LogRocket Blog]]

### réduit

- [[kb/_entites-mineures#besoin-de-parsing-HTML\|besoin de parsing HTML]] (CONCEPT) — 0.92, ATEMPOREL
  - [[fiches/2025-09/mcp-replaces-browser-logrocket-2025-09-15\|MCP remplace le navigateur - Interactions agents IA - Développeurs frontend - LogRocket Blog]]

### s_applique_à

- [[kb/_entites-mineures#Semrush-et-Ahrefs-(couche-par-dessus,-pas-substitut)\|Semrush et Ahrefs (couche par-dessus, pas substitut)]] (TECHNOLOGIE) — 0.90, ATEMPOREL
  - [[fiches/2026-05/pillitteri-opus-4-8-seo-workflow-deux-phases-2026-05-29\|Article du blog de **Pasquale Pillitteri** (ingénieur informatique, Palermo) publié le **29 mai 2026** (version FR), 18 min de lecture, rubrique *Claude Code & Anthropic*. **Thèse-pivot** : *« Claude Opus 4.8 est le modèle SEO le plus puissant de 2026, mais presque tout le monde l'utilise mal »* — non pas un problème de modèle mais de **système**. La règle d'or : ***« la stratégie est un tableau blanc, la production est une chaîne de montage »*** — il faut **scinder le SEO en deux phases distinctes**, et les mélanger est *« le moyen le plus rapide de gaspiller un modèle qui coûte cinq dollars par million de tokens en entrée et vingt-cinq en sortie »*. **Contexte modèle** : Opus 4.8 publié le **28 mai 2026** (41 jours après Opus 4.7), contexte **1M tokens**, **GraphWalks Long-Context F1 à 1M : 40,3 % → 68,1 %**, **SWE-bench Verified 88,6 %**, **USAMO 2026 96,7 %** (+27,4 pts), **HLE avec tool 57,9 %**, prix inchangé **5 $/25 $** par M tokens, **Fast Mode 2,5× à 10 $/50 $**, quatre **effort levels** (Low, High, Extra, Max). **L'anti-pattern central** = *« la conversation géante »* / **dérive du contexte** : mélanger stratégie, keyword research, analyse concurrentielle et rédaction dans un seul chat produit une *« bouillie d'intentions contradictoires »* → le modèle glisse vers les **best practices génériques** (« optimisation holistique », « approche stratégique ») au lieu d'un contenu ancré aux données. **Phase 1 — Stratégie (tableau blanc, UI visuelle, one-off)** : dashboard / Google Sheet / canvas Claude.ai pour décider en voyant les données ensemble. **3 plays** : (a) **keyword research classifiée** (tableau volume / difficulté 0-100 / intention / potentiel business / priorité = volume÷difficulté×poids business) ; (b) **analyse concurrentielle visuelle** (matrice de couverture thématique, gaps) ; (c) **roadmap par phases** (quick wins M1-2 / moyen terme M3-6 / pillar pages M7-12). Mode **Extra/Max** justifié ici (*« une décision stratégique juste vaut mille pages bien écrites sur des mots-clés erronés »*). 3 artefacts fermés sauvegardés sur Notion/Drive. **Phase 2 — Production (chaîne de montage, Opus 4.8 + MCP)** : le modèle passe de stratège à **machine d'exécution** ; chaque décision **ancrée à des données live** via **Model Context Protocol**. **Stack MCP minimum** : **GSC MCP** (AminForou/mcp-gsc, 500+ étoiles), **Ahrefs MCP officiel** (98 étoiles), **GA4 MCP** ; repo `modelcontextprotocol/servers` = **86 440 étoiles**, **10 000+ serveurs actifs**, 97M téléchargements SDK/mois. Setup ~35 min, refresh mensuel ~20 min. **Loop hebdomadaire** : un prompt unique tire les données live, construit le brief (top 10 SERP + GSC + Ahrefs), dérive H2/H3, écrit, contrôle densité, suggère titres → **+45 % productivité**, draft en **6-12 min** (référence explicite au **content engineering de Ryan Law / Ahrefs**, 23 skills). Mention des **Dynamic Workflows** Anthropic (jusqu'à 1 000 subagents). **4 erreurs courantes** : (1) ne pas vérifier les chiffres (spot-check obligatoire, *trust & verify*) ; (2) remplacer complètement Semrush/Ahrefs (le MCP est une **couche par-dessus**, pas un substitut) ; (3) ignorer le **content gap paid-organic** (cas client education : **2 742 termes gaspillés / 351 opportunités** identifiés en 90 s) ; (4) utiliser Opus 4.8 là où **Haiku 4.5** suffit (meta descriptions, alt text). **Coût** : 1-3 $/article de 2 500 mots. **Sonnet 4.6** suffit pour la production récurrente, Opus 4.8 réservé à la stratégie. Article SEO-optimisé et auto-référentiel (l'auteur écrit sur le SEO un contenu lui-même conçu pour se positionner sur « Opus 4.8 SEO »). Convergence directe avec **Ryan Law/Ahrefs** (cité), **systems around the model** (Dropbox/Okumura), **skills-over-prompts** (Lattice), routage modèle Haiku/Sonnet/Opus (Gupta token-to-outcome).]]

### s_oppose_à

- [[kb/DICE\|DICE]] (METHODOLOGIE) — 0.75, ATEMPOREL
  - [[fiches/2025-07/context-engineering-domain-understanding-johnson-2025-07-23\|Context Engineering - Domain Understanding - DICE - Rod Johnson - LLM - Domain Model - Embabel]]

### utilise

- [[kb/_entites-mineures#sécurité-renforcée\|sécurité renforcée]] (CONCEPT) — 0.93, ATEMPOREL
  - [[fiches/2025-09/mcp-replaces-browser-logrocket-2025-09-15\|MCP remplace le navigateur - Interactions agents IA - Développeurs frontend - LogRocket Blog]]

## Relations (comme objet)

- [[kb/_entites-mineures#fuites-de-données\|fuites de données]] **observé_dans** → MCP — 0.93
- [[kb/Claude-Skills\|Claude Skills]] **s_oppose_à** → MCP — 0.90
- [[kb/Shopify\|Shopify]] **utilise** → MCP — 0.90
- [[kb/_entites-mineures#overhead-de-tokens-excessif\|overhead de tokens excessif]] **observé_dans** → MCP — 0.88
- [[kb/Agent-Skills\|Agent Skills]] **converge_avec** → MCP — 0.85

## Fiches sources

- [[fiches/2025-11/chen-fioca-openai-future-proof-coding-agents-2025-11-23\|Construire des agents de codage pérennes face aux cycles de modèles : architecture Harness, Codex SDK et Computer Use terminal — retour d'expérience OpenAI]]
- [[fiches/2025-10/claude-skills-bigger-than-mcp-willison-2025-10-16\|Claude Skills vs MCP - Simplicité élégante - Explosion cambrienne prédite - Simon Willison]]
- [[fiches/2025-07/context-engineering-domain-understanding-johnson-2025-07-23\|Context Engineering - Domain Understanding - DICE - Rod Johnson - LLM - Domain Model - Embabel]]
- [[fiches/2025-06/gemini-cli-claude-code-hybrid-workflow-reddit-2025-06-23\|Gemini CLI + Claude Code - Workflow hybride - Large codebase analysis - Context window - Reddit ChatGPTCoding]]
- [[fiches/2025-12/google-deepmind-interactions-api-gemini-agents-2025-12-11\|API Interactions Google DeepMind - interface unifiée modèles et agents Gemini]]
- [[fiches/2025-11/lesse-anthropic-building-agentic-systems-claude-2025-11-23\|Construction de systèmes agentiques puissants avec Claude - Architecture et patterns d'implémentation - Anthropic]]
- [[fiches/2026-03/levie-building-trillions-agents-software-2026-03-07\|Construire pour des trillions d'agents : logiciel API-first, infrastructure agentique, nouveau paradigme logiciel - X/Twitter]]
- [[fiches/2026-02/maitriser-claude-code-formation-pedagogique-deep-research-2026-02\|Formation complète Claude Code : 12 modules pédagogiques coding agentique - Deep Research]]
- [[fiches/2026-02/martinho-allen-cloudflare-markdown-for-agents-2026-02-12\|Cloudflare — conversion HTML vers Markdown en temps réel pour agents IA via négociation de contenu HTTP]]
- [[fiches/2025-09/mcp-replaces-browser-logrocket-2025-09-15\|MCP remplace le navigateur - Interactions agents IA - Développeurs frontend - LogRocket Blog]]
- [[fiches/2025-09/vibe-coding-hot-summer-redmonk-2025-09-08\|Vibe Coding - Été 2025 - Développement intuitif assisté IA - Sécurité et coûts - RedMonk]]
