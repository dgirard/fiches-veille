# Model Context Protocol

> **Type** : TECHNOLOGIE | 10 relations | 5 fiches sources

## Attributs

- **abréviation** : MCP — standard ouvert d'accès aux outils
- **catégorie** : Standard ouvert d'accès live aux outils/données (Anthropic, nov. 2024)
- **usage** : Interface langage naturel pour données de conformité

## Relations (comme sujet)

### est_instance_de

- [[kb/_entites-mineures#protocole-d'Agentic-Web\|protocole d'Agentic Web]] (CONCEPT) — 0.92, ATEMPOREL
  - [[fiches/2025-08/mit-nanda-genai-divide-95-percent-pilots-fail-legalio-2025-08-23\|Relais Legal.io de l'étude MIT NANDA "The GenAI Divide: State of AI in Business 2025" : 95% des pilotes IA en entreprise n'apportent aucun ROI mesurable malgré $30-40 Mds investis. Concept de "GenAI Divide", "shadow AI economy", quatre facteurs structurels d'échec, recommandation back-office et build-to-buy. Justification empirique du basculement RH-organisationnel.]]

### permet

- [[kb/_entites-mineures#AI-agents-sécurisés-et-scalables\|AI agents sécurisés et scalables]] (TECHNOLOGIE) — 0.95, ATEMPOREL
  - [[fiches/2025-07/mcp-for-beginners-microsoft-developer-youtube-2025-07-28\|MCP for Beginners - Model Context Protocol - Microsoft Developer - YouTube playlist - AI agents - Tutorial]]
- [[kb/_entites-mineures#accès-outils-cyberattaque\|accès outils cyberattaque]] (CONCEPT) — 0.92, STATIQUE
  - [[fiches/2025-11/anthropic-disrupting-ai-espionage-2025-11-13\|Première campagne cyber espionnage orchestrée par IA - Claude Code manipulé - Acteur État chinois - 30 cibles globales - 80-90% automatisé - Jailbreaking - Anthropic Threat Intelligence]]

### utilise

- [[kb/_entites-mineures#security-best-practices\|security best practices]] (CONCEPT) — 0.90, ATEMPOREL
  - [[fiches/2025-07/mcp-for-beginners-microsoft-developer-youtube-2025-07-28\|MCP for Beginners - Model Context Protocol - Microsoft Developer - YouTube playlist - AI agents - Tutorial]]

## Relations (comme objet)

- [[kb/MCP-UI\|MCP-UI]] **est_basé_sur** → Model Context Protocol — 0.98
- [[kb/MCP-for-Beginners\|MCP for Beginners]] **référence** → Model Context Protocol — 0.98
- [[kb/infrastructure-contexte-codifié\|infrastructure contexte codifié]] **utilise** → Model Context Protocol — 0.97
- [[kb/QMD\|QMD]] **utilise** → Model Context Protocol — 0.97
- [[kb/_entites-mineures#Phase-2-production\|Phase 2 production]] **est_basé_sur** → Model Context Protocol — 0.95
- [[kb/_entites-mineures#Vanta\|Vanta]] **utilise** → Model Context Protocol — 0.95

## Fiches sources

- [[fiches/2025-11/anthropic-disrupting-ai-espionage-2025-11-13\|Première campagne cyber espionnage orchestrée par IA - Claude Code manipulé - Acteur État chinois - 30 cibles globales - 80-90% automatisé - Jailbreaking - Anthropic Threat Intelligence]]
- [[fiches/2025-07/mcp-for-beginners-microsoft-developer-youtube-2025-07-28\|MCP for Beginners - Model Context Protocol - Microsoft Developer - YouTube playlist - AI agents - Tutorial]]
- [[fiches/2025-08/mcp-ui-future-agentic-interfaces-goose-2025-08-25\|MCP-UI révolutionne interfaces agents IA, composants web interactifs, sandboxed iframes, accessibilité, générative UI - Goose/Block]]
- [[fiches/2026-05/pillitteri-opus-4-8-seo-workflow-deux-phases-2026-05-29\|Article du blog de **Pasquale Pillitteri** (ingénieur informatique, Palermo) publié le **29 mai 2026** (version FR), 18 min de lecture, rubrique *Claude Code & Anthropic*. **Thèse-pivot** : *« Claude Opus 4.8 est le modèle SEO le plus puissant de 2026, mais presque tout le monde l'utilise mal »* — non pas un problème de modèle mais de **système**. La règle d'or : ***« la stratégie est un tableau blanc, la production est une chaîne de montage »*** — il faut **scinder le SEO en deux phases distinctes**, et les mélanger est *« le moyen le plus rapide de gaspiller un modèle qui coûte cinq dollars par million de tokens en entrée et vingt-cinq en sortie »*. **Contexte modèle** : Opus 4.8 publié le **28 mai 2026** (41 jours après Opus 4.7), contexte **1M tokens**, **GraphWalks Long-Context F1 à 1M : 40,3 % → 68,1 %**, **SWE-bench Verified 88,6 %**, **USAMO 2026 96,7 %** (+27,4 pts), **HLE avec tool 57,9 %**, prix inchangé **5 $/25 $** par M tokens, **Fast Mode 2,5× à 10 $/50 $**, quatre **effort levels** (Low, High, Extra, Max). **L'anti-pattern central** = *« la conversation géante »* / **dérive du contexte** : mélanger stratégie, keyword research, analyse concurrentielle et rédaction dans un seul chat produit une *« bouillie d'intentions contradictoires »* → le modèle glisse vers les **best practices génériques** (« optimisation holistique », « approche stratégique ») au lieu d'un contenu ancré aux données. **Phase 1 — Stratégie (tableau blanc, UI visuelle, one-off)** : dashboard / Google Sheet / canvas Claude.ai pour décider en voyant les données ensemble. **3 plays** : (a) **keyword research classifiée** (tableau volume / difficulté 0-100 / intention / potentiel business / priorité = volume÷difficulté×poids business) ; (b) **analyse concurrentielle visuelle** (matrice de couverture thématique, gaps) ; (c) **roadmap par phases** (quick wins M1-2 / moyen terme M3-6 / pillar pages M7-12). Mode **Extra/Max** justifié ici (*« une décision stratégique juste vaut mille pages bien écrites sur des mots-clés erronés »*). 3 artefacts fermés sauvegardés sur Notion/Drive. **Phase 2 — Production (chaîne de montage, Opus 4.8 + MCP)** : le modèle passe de stratège à **machine d'exécution** ; chaque décision **ancrée à des données live** via **Model Context Protocol**. **Stack MCP minimum** : **GSC MCP** (AminForou/mcp-gsc, 500+ étoiles), **Ahrefs MCP officiel** (98 étoiles), **GA4 MCP** ; repo `modelcontextprotocol/servers` = **86 440 étoiles**, **10 000+ serveurs actifs**, 97M téléchargements SDK/mois. Setup ~35 min, refresh mensuel ~20 min. **Loop hebdomadaire** : un prompt unique tire les données live, construit le brief (top 10 SERP + GSC + Ahrefs), dérive H2/H3, écrit, contrôle densité, suggère titres → **+45 % productivité**, draft en **6-12 min** (référence explicite au **content engineering de Ryan Law / Ahrefs**, 23 skills). Mention des **Dynamic Workflows** Anthropic (jusqu'à 1 000 subagents). **4 erreurs courantes** : (1) ne pas vérifier les chiffres (spot-check obligatoire, *trust & verify*) ; (2) remplacer complètement Semrush/Ahrefs (le MCP est une **couche par-dessus**, pas un substitut) ; (3) ignorer le **content gap paid-organic** (cas client education : **2 742 termes gaspillés / 351 opportunités** identifiés en 90 s) ; (4) utiliser Opus 4.8 là où **Haiku 4.5** suffit (meta descriptions, alt text). **Coût** : 1-3 $/article de 2 500 mots. **Sonnet 4.6** suffit pour la production récurrente, Opus 4.8 réservé à la stratégie. Article SEO-optimisé et auto-référentiel (l'auteur écrit sur le SEO un contenu lui-même conçu pour se positionner sur « Opus 4.8 SEO »). Convergence directe avec **Ryan Law/Ahrefs** (cité), **systems around the model** (Dropbox/Okumura), **skills-over-prompts** (Lattice), routage modèle Haiku/Sonnet/Opus (Gupta token-to-outcome).]]
- [[fiches/2025-07/powered-by-claude-anthropic-partners-2025-07-09\|Vitrine « Powered by Claude » : écosystème de partenaires Anthropic — intégrations IA et applications construites sur Claude (anthropic.com)]]
