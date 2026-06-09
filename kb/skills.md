# skills

> **Type** : TECHNOLOGIE | 10 relations | 1 fiches sources

## Attributs

- **catégorie** : Standard ouvert de packaging de connaissances agent

## Relations (comme sujet)

### améliore

- [[kb/_entites-mineures#la-précision-de-21%-à-plus-de-95%\|la précision de 21% à plus de 95%]] (CONCEPT) — 0.95, STATIQUE
  - [[fiches/2026-06/anthropic-self-service-data-analytics-claude-agentic-stack-2026-06-03\|REX d'ingénierie de l'équipe **Data Science & Data Engineering d'Anthropic** (Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry) publié le **3 juin 2026** sur le blog Anthropic (catégorie *Enterprise AI*, focus **Claude Code**). **Résultat-phare** : ***« 95 % des requêtes d'analytics métier sont automatisées par Claude, avec ~95 % de précision en agrégat »*** (jusqu'à **~99 %** sur certains domaines). **Problème central** : l'analytics n'est **pas** du code — *« there's often only a single correct answer using a single correct source »* — il faut **mapper une question utilisateur à des entités précises et à jour** du modèle de données. Trois **modes d'échec** : (1) **ambiguïté concept↔entité** (ex. *« active users »* : quelles actions ? exclure les fraudeurs ? quelle fenêtre ?) ; (2) **obsolescence** (assets et connaissance de l'agent deviennent *« subtly wrong »*) ; (3) **échec de retrieval** (*« 80 % des requêtes échouées avaient l'info présente dans le corpus »* mais introuvable). **Solution = « agentic analytics stack » en 4 couches** : (L1) **Data foundations** — dimensional modeling, **canonical datasets** *« single source-of-truth »*, métadonnées *« as a first-class product »*, intégrité par CI/CD ; (L2) **Sources of truth** par ordre de confiance décroissant — **semantic layer** (l'agent est *« structurally required (by skill instruction) to leverage the semantic layer first »*), graphe de lineage, **query corpus** (distillé en docs structurées, **pas** du retrieval brut), business context (knowledge graph : roadmaps, decision logs, org) ; (L3) **Skills** — le levier décisif : ***« without skills … didn't exceed 21 % … Adding skills gets these numbers consistently above 95 % »*** ; structure **par paires** (*Knowledge skill* = routeur vers ~30 fichiers de référence ; *Unbook skill* = workflow de l'analyste senior : clarifier → trouver les sources → exécuter → **revue adversariale**) ; maintenance **colocalisée** (*« a code-review hook flags any reporting-model change that doesn't touch a skill file »* → **~90 % des PR data incluent un changement de skill**) ; (L4) **Validation** — evals offline (seuil ~90 % pour lancer un agent, cible ~100 %), **ablation testing** (résultat négatif notable : grep brut sur des milliers de fichiers SQL → précision bouge *« less than a point »*), online (revue adversariale : **+6 % de précision, +32 % de tokens, +72 % de latence**), **provenance footers** (tier de source + fraîcheur + ownership), **active correction harvesting** (agents planifiés scannant les canaux pour drafter des fixes markdown). **Insight stratégique** : *« documentation generated, definitions owned by humans »* — laisser le LLM **définir** les métriques fut *« net-negative »*. **Démarrage minimal** : quelques canonical datasets + quelques dizaines d'evals + un *thin knowledge skill* captent *« most of the upside »*. Converge fortement avec [[shihipar-claude-code-lessons-building-skills-2026-06-03]] (skills = dossiers, Gotchas, hooks), la doctrine *systems around the model* de [[dropbox-okumura-beyond-code-generation-engineering-productivity-ai-agents-2026-05-28]], le **semantic layer / ontology** de [[talisman-modern-data-101-ontology-pipeline-refresh-2026-05-04]] et [[seale-semantic-agent-model-harness-ontology-data-2026-04-17]], le *context development lifecycle* de [[debois-tessl-context-development-lifecycle-ai-coding-agents-2026-02-19]] et l'UDA/knowledge graph de [[netflix-uda-unified-data-architecture-knowledge-graph-2025-06-12]].]]

### est_basé_sur

- [[kb/_entites-mineures#fichiers-SKILL-md\|fichiers SKILL.md]] (TECHNOLOGIE) — 0.95, STATIQUE
  - [[fiches/2025-10/superpowers-skills-coding-agents-vincent-2025-10-09\|Système de compétences pour agents IA - Superpowers/Skills - Apprentissage continu - Blog Fsck]]

### est_instance_de

- [[kb/_entites-mineures#prompts-copyables-réutilisables-(63-dans-New-Form)\|prompts copyables réutilisables (63 dans New Form)]] (CONCEPT) — 0.95, STATIQUE
  - [[fiches/2026-05/isenberg-meng-to-google-design-md-design-team-in-a-file-2026-05-06\|Podcast Greg Isenberg × Meng To (designer, fondateur Design+Code, créateur des produits Aura / New Form / Dream Cut) sur **`design.md`** — la convention open-source de Google, équivalente à `agents.md` / `skills.md` / `soul.md` mais **pour la design system** (typographie, couleurs, spacing, WebGL/Three.js animations, règles de reveal). Idée centrale : porter "l'**âme du design**" dans un fichier markdown qui se transmet à un agent (Claude Code, Codex, OpenClaude, Gemini, Stitch, Aura, V0, Lovable, Cursor) pour préserver la **cohérence cross-medium** (web, mobile, slides Replit, motion design Hyperframes/Remotion). Triade enseignée : **HTML = plat fini, design.md = recette, skills = ingrédients** (skills typo, lasers, skeuomorphic, 3D — 63 dans New Form). Diagnostic majeur : **design drift** sur les workflows one-shot (`v0`, Lovable, Framer) qui démarrent forts puis dérivent en générique. Méta-message : la *taste* est le seul **moat** restant — *"si une chose ressemble à une autre, sa valeur baisse de 10× à 100×"*. Workflow : **Reference → Design.md → Generate → Inspect → Systemize → Iterate (jusqu'à 1000+ prompts) → Remix → Expand → Export**. Critique des **purple gradients** ("you just run") = baseline générique post-vibe-coding. Meng To revendique avoir dépensé ~500 000 $ en tokens, fait 1000–10 000 itérations par produit, gère 4 produits en parallèle en solo.]]

### mesure

- « non-invocation dans 56% des cas d'évaluation » (MESURE) — 0.99, STATIQUE
  - [[fiches/2026-01/gao-vercel-agents-md-outperforms-skills-evals-2026-01-27\|AGENTS.md surpasse les skills dans les évaluations agents Vercel/Next.js]]
- « taux de réussite 79% (avec instructions explicites) » (MESURE) — 0.99, STATIQUE
  - [[fiches/2026-01/gao-vercel-agents-md-outperforms-skills-evals-2026-01-27\|AGENTS.md surpasse les skills dans les évaluations agents Vercel/Next.js]]

### permet

- [[kb/_entites-mineures#capacités-latentes-des-modèles\|capacités latentes des modèles]] (CONCEPT) — 0.90, ATEMPOREL
  - [[fiches/2025-11/rajasekaran-anthropic-frontend-design-skills-2025-11-12\|Anthropic - Design frontend avec Skills - Convergence distributionnelle - Typographie distinctive - React/Tailwind artifacts - Contexte dynamique à la demande - Patterns RPG/editorial]]

### s_inspire_de

- [[kb/_entites-mineures#livres-techniques\|livres techniques]] (CONCEPT) — 0.88, ATEMPOREL
  - [[fiches/2025-10/superpowers-skills-coding-agents-vincent-2025-10-09\|Système de compétences pour agents IA - Superpowers/Skills - Apprentissage continu - Blog Fsck]]

### surpasse

- [[kb/_entites-mineures#baseline-sans-documentation\|baseline sans documentation]] (CONCEPT) — 0.97, STATIQUE
  - [[fiches/2026-01/gao-vercel-agents-md-outperforms-skills-evals-2026-01-27\|AGENTS.md surpasse les skills dans les évaluations agents Vercel/Next.js]]

## Relations (comme objet)

- [[kb/AGENTS-md\|AGENTS.md]] **surpasse** → skills — 0.99
- [[kb/Superpowers\|Superpowers]] **utilise** → skills — 0.97

## Fiches sources

- [[fiches/2026-01/gao-vercel-agents-md-outperforms-skills-evals-2026-01-27\|AGENTS.md surpasse les skills dans les évaluations agents Vercel/Next.js]]
