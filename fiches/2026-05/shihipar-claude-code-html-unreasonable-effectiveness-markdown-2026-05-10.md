# shihipar-claude-code-html-unreasonable-effectiveness-markdown-2026-05-10

## Veille
Article-manifeste de **Thariq Shihipar** (Engineer & serial entrepreneur, équipe Claude Code chez Anthropic) qui annonce un **changement de format de sortie par défaut pour les agents** : remplacer **Markdown par HTML**. Thèse : Markdown a été le format dominant entre humains et agents (simple, portable, éditable, lisible) mais est devenu **un goulot d'étranglement** à mesure que les agents produisent des artefacts plus longs et plus riches (specs, plans, rapports, code review). Au-delà de ~100 lignes, plus personne ne lit un fichier Markdown. HTML résout six limites simultanément : **densité d'information** (tableaux, CSS, SVG, scripts, canvas, images), **clarté visuelle** (mise en page navigable, responsive mobile), **facilité de partage** (lien S3 directement ouvrable dans un navigateur), **interactivité bidirectionnelle** (sliders, knobs, boutons "copy as JSON/prompt" pour reboucler vers Claude Code), **ingestion contextuelle native** (Claude Code lit codebase + MCP Slack/Linear + git history + Chrome) et **plaisir** (l'auteur revendique explicitement *"it's joyful"*). Cinq usages canoniques détaillés : (1) **specs/plans/exploration** en grille comparative, (2) **PR review** avec diff annoté inline, (3) **design & prototypes** avec sliders d'animation, (4) **rapports/recherche/learning** (l'auteur a fait générer un explainer prompt caching depuis l'historique git), (5) **éditeurs jetables custom** (drag-and-drop de tickets Linear, éditeurs de feature flags, prompt-tuner side-by-side) qui produisent un export "copy as markdown/diff/JSON" reréinjectable. Anti-pattern explicite : *"I'm a little bit afraid that people will read this article and turn it into a /html skill"* — l'auteur **refuse la skill-ification prématurée**, recommande de prompter from scratch ("make a HTML file"). FAQ pragmatique : coût tokens absorbé par les 1 MM context de **Opus 4.7**, génération 2-4× plus longue, diffs HTML bruyants (downside réel), style maîtrisé via design system HTML de référence.

## Titre Article
Using Claude Code: The Unreasonable Effectiveness of HTML

## Date
2026-05-10

## URL
https://x.com/i/status/2052809885763747935

## Keywords
HTML, Markdown, format de sortie, Claude Code, artefacts agentiques, Thariq Shihipar, Anthropic, Opus 4.7, 1MM context, densité d'information, SVG, CSS, canvas, mise en page responsive, interactivité bidirectionnelle, copy as JSON, copy as prompt, ingestion contextuelle, MCP, Slack, Linear, git history, Chrome, specs, plans, exploration, code review, PR review, diff annoté, design system, prototypes, animations, sliders, rapports, recherche, explainer, éditeurs jetables, throwaway editor, feature flags, prompt tuning, joyful, anti-skill-ification, prompter from scratch, S3, partage, tokens efficiency, diff noisy, design drift, frontend design plugin, taste, design memory, html-effectiveness, gallery, playgrounds, two-way interaction, judgment, comprehension debt, in-the-loop, design system file, illustrations vs ASCII, color via unicode anti-pattern, mobile responsive, tabs, illustrations, custom UI throwaway

## Authors
Thariq Shihipar (Engineer & serial entrepreneur, équipe Claude Code chez Anthropic — site : thariqs.github.io/html-effectiveness ; X : @trq212)

## Ton
**Profil** : Article-manifeste personnel (~1500 mots) publié sur X / blog personnel, première personne assumée, registre praticien-évangéliste. Public cible : utilisateurs avancés de Claude Code, designers, PM, ingénieurs qui produisent specs/plans/rapports avec un agent. Niveau technique : intermédiaire — pas de code, beaucoup de pratique vécue (exemples concrets : son article sur prompt caching, ses PR au quotidien, ses brainstorms onboarding).

**Style** : **Pédagogique-démonstratif**. Ouverture en concession ("Markdown has become the dominant file format used by agents… *But* as agents have become more and more powerful, I have felt that markdown has become a restricting format"). Puis structure rhétorique classique : *why → how → use cases → FAQ → wrap*. Chaque section appuyée par un **exemple vécu** ("when writing this article, I asked Claude Code to read through my code folder…") plutôt que par une démonstration abstraite. Pré-empte les objections ("Isn't it less token efficient?", "How do I view the HTML file?", "What about version control?") sous forme FAQ honnête (concède le diff HTML bruyant comme *"one of the biggest downsides"*).

Position épistémique : **insider Anthropic Claude Code** qui formalise une pratique déjà adoptée par son équipe (*"I increasingly see this being used by others on the Claude Code team"*). Ton émotionnel : enthousiaste mais non-prosélyte. Phrases-signaux plantées pour viralité : *"the unreasonable effectiveness of HTML"* (clin d'œil Wigner-Karpathy), *"it's joyful"*, *"the chance of someone actually reading your spec is much much higher if it's in HTML"*, *"I'm a little bit afraid that people will read this article and turn it into a /html skill"*. Méta-mouvement remarquable : **anti-skill-ification explicite** — l'auteur, alors qu'il appartient à l'écosystème qui pousse les Claude Skills, refuse de canoniser sa pratique en skill. *"You don't need to do much to get Claude to do this. You can just ask it to 'make a HTML file' or 'make a HTML artifact'."*

Ton global : **doctrinal mais humble**. Conclusion en émotion ("I feel much more in the loop than ever before when using HTML. I hope you do too.") — ramène la question technique au problème vécu de la **perte de contrôle cognitif** face à des agents qui produisent des plans trop longs pour être lus (résonance forte avec *cognitive surrender* / *comprehension debt* d'Osmani).

## Pense-betes

- **Auteur** : Thariq Shihipar — Engineer & serial entrepreneur, **équipe Claude Code chez Anthropic**. X : @trq212. Site : thariqs.github.io/html-effectiveness (gallery d'exemples HTML générés par Claude Code, organisée par catégorie d'usage).
- **Date** : ~2026-05-10 (article récent, mentionne Opus 4.7 avec 1MM context, ID snowflake X ~ mai 2026). URL : `https://x.com/i/status/2052809885763747935`.
- **Thèse en une ligne** : *"I've started preferring HTML as an output format instead of Markdown"* — le format de sortie par défaut pour les artefacts agentiques doit basculer de Markdown vers HTML.
- **Pourquoi maintenant ?** : trois facteurs convergents :
  1. Les agents produisent des specs/plans plus longs et plus riches qu'avant.
  2. L'auteur (et son entourage) **n'édite plus manuellement** ces fichiers — il prompte Claude pour les éditer → l'avantage "Markdown éditable à la main" disparaît.
  3. **Opus 4.7 + 1MM context** absorbe sans douleur les tokens supplémentaires du HTML.
- **Les 6 raisons (why HTML)** :
  1. **Information density** — tableaux, CSS, SVG, scripts, canvas, images, positions absolues, données spatiales. *"Almost no set of information that Claude can read that you cannot fairly efficiently represent with HTML."*
  2. **Visual clarity & ease of reading** — tabs, illustrations, liens, mobile responsive. Au-delà de 100 lignes en Markdown, plus personne ne lit.
  3. **Ease of sharing** — upload S3 → lien direct. *"The chance of someone actually reading your spec is much much higher if it's in HTML."*
  4. **Two-way interaction** — sliders, knobs, boutons "copy as prompt" pour reboucler vers Claude Code.
  5. **Data ingestion** — Claude Code agrège codebase + MCP (Slack, Linear) + git history + Chrome → contexte plus large que ClaudeAI ou Claude Design.
  6. **It's joyful** — *"makes me feel more involved and invested in the creation, and that by itself is enough"*.
- **Anti-pattern Markdown observé** : le modèle, privé d'expressivité visuelle, fait des **diagrammes ASCII** ou **estime des couleurs avec des caractères Unicode** (l'article inclut un screenshot de Claude Code essayant de "montrer une couleur" en Unicode → signal absurde d'inadéquation du format).
- **Référence rhétorique** : *"The Unreasonable Effectiveness of HTML"* est un clin d'œil à *"The Unreasonable Effectiveness of Mathematics"* (Wigner, 1960) et à la lignée de titres "unreasonable effectiveness of X" en ML (Karpathy 2015 sur les RNN).
- **5 use cases canoniques détaillés** :
  1. **Specs, Planning & Exploration** — *"a web of HTML files"* : brainstorm 6 directions en grille comparative, expansion d'une option, mockups, code snippets, plan d'implémentation. Prompt-type : *"Generate 6 distinctly different approaches — vary layout, tone, and density — and lay them out as a single HTML file in a grid so I can compare them side by side."*
  2. **Code Review & Understanding** — attacher un explainer HTML à chaque PR. Diff rendu inline avec annotations marginales, code-coloring par sévérité. Prompt-type : *"Render the actual diff with inline margin annotations, color-code findings by severity."*
  3. **Design & Prototypes** — Claude Design est lui-même basé sur HTML. Prototyper animations avec sliders et bouton "copy parameters" pour exporter les valeurs réglées.
  4. **Reports, Research & Learning** — l'auteur a fait générer son article sur prompt caching en lisant l'historique git. Format long HTML, explainer interactif, slideshow.
  5. **Custom Editing Interfaces (throwaway editors)** — éditeur jetable single-file pour une donnée spécifique, finissant toujours par un **export** (copy as JSON/markdown/prompt) re-injectable dans Claude Code. Exemples : drag-and-drop de 30 tickets Linear en colonnes Now/Next/Later/Cut, éditeur de feature flags avec dépendances et warnings, prompt-tuner side-by-side avec compteur tokens. *"Not a product, or a reusable tool, but a single HTML file, purpose-built for this one piece of data."*
- **Anti-pattern majeur explicité** : *"I'm a little bit afraid that people will read this article and turn it into a /html skill or something. While there might be some value in that, I want to emphasize that you don't need to do much to get Claude to do this."* → **Anti-skill-ification** : la pratique est trop contextuelle pour être figée en skill ; prompter "make a HTML file" suffit.
- **FAQ honnête** (concessions explicites) :
  - **Token efficiency** : HTML utilise plus de tokens mais le 1MM context d'Opus 4.7 absorbe.
  - **Génération** : 2-4× plus lente que Markdown — *"but I've found the results are worth it"*.
  - **Version control** : *"this is honestly one of the biggest downsides of HTML, HTML diffs are noisy and hard to review compared to Markdown"* — downside non résolu, l'auteur l'assume.
  - **Style / éviter le moche** : utiliser le **frontend design plugin** ou créer un **design system HTML unique** en pointant Claude vers la codebase, puis le référencer pour les autres fichiers HTML générés.
- **Méta-thèse finale (in-the-loop)** : *"I had begun to fear that because I had stopped reading plans in depth I would simply have to leave Claude to make its choices. But I am happy to say instead that I feel more in the loop than ever before when using HTML."* → HTML comme **antidote au cognitive surrender** (Osmani) / **comprehension debt** : la lisibilité retrouvée permet de rester dans la boucle de décision.
- **Articulation avec la veille corpus** :
  - Convergence directe avec **Isenberg × Meng To `design.md`** (2026-05-06) : Meng dit explicitement *"HTML = finished dish, MD file = recipe, skills = ingredients"*. Shihipar valide la primauté HTML pour le **plat fini livré à l'humain**.
  - Réponse opérationnelle à **Osmani — Cognitive Surrender / Comprehension Debt** (2026-05-05) : Shihipar nomme exactement le même problème (*"I had stopped reading plans in depth"*) et propose HTML comme solution de "rester dans la boucle".
  - Tension avec **Lattice / Vincent / Karpathy "skills-maxi"** : Shihipar adopte la **posture inverse** sur la skill-ification ("don't turn this into a /html skill"). Compromis : skills pour les patterns stables, prompt nu pour les pratiques émergentes.
  - Confirmation **Opus 4.7 + 1MM context** comme **changement architectural** qui rend économiquement supportables des formats plus verbeux (HTML, design system, brainstorms étendus).
  - Lignée **Compounding engineering / Cherny** : HTML comme nouvelle couche de l'**output artefactuel** entre l'agent et l'humain, au même titre que les PR descriptions, les release notes, les commits messages.
- **Exemple méta** : pour rédiger cet article, l'auteur a demandé à Claude Code de lire son dossier de code, trouver tous les fichiers HTML générés, les grouper/catégoriser et produire un fichier HTML avec tous les diagrammes par type → les illustrations de l'article sont elles-mêmes le produit du pattern qu'il décrit.
- **Workflow découlant pour la pratique cabinet** :
  - Toute spec, plan ou rapport > 100 lignes → bascule HTML.
  - PR critiques → attacher un explainer HTML.
  - Onboarding de fichiers, explorations de design, reorderings → throwaway editor HTML avec export structuré.
  - Garder Markdown pour : commits messages, notes de fiches courtes, fichiers .md de config (CLAUDE.md, agents.md, etc.).

## RésuméDe400mots

**Thariq Shihipar** (équipe Claude Code chez Anthropic) publie un article-manifeste annonçant un changement de format de sortie par défaut pour les agents : remplacer **Markdown par HTML**. Le diagnostic : Markdown a régné comme format dominant entre humain et agent (simple, portable, éditable) mais est devenu **restrictif** à mesure que les agents produisent des artefacts plus longs et plus riches. Au-delà de ~100 lignes, plus personne ne lit un fichier Markdown — et comme l'auteur n'édite plus manuellement ses specs (il prompte Claude pour les éditer), l'avantage historique de Markdown disparaît.

**Six raisons** justifient le basculement vers HTML : (1) **densité d'information** — tableaux, CSS, SVG, scripts, canvas, images ; *"almost no set of information that Claude can read that you cannot represent with HTML"* ; (2) **clarté visuelle** — tabs, illustrations, responsive mobile ; (3) **partage** — upload S3 → lien direct, taux de lecture multiplié ; (4) **interactivité bidirectionnelle** — sliders, knobs, boutons "copy as prompt" pour reboucler ; (5) **ingestion contextuelle** native à Claude Code (codebase + MCP + git + Chrome) ; (6) **plaisir** — *"it's joyful"*.

L'auteur formalise **cinq usages canoniques** : (a) **specs/plans/exploration** en grille comparative ; (b) **PR review** avec diff annoté inline et code-coloring par sévérité ; (c) **design & prototypes** avec sliders d'animation ; (d) **rapports/recherche** (son explainer sur prompt caching généré depuis l'historique git) ; (e) **éditeurs jetables custom** — single-file HTML purpose-built pour une donnée (drag-and-drop de tickets Linear, éditeur de feature flags, prompt-tuner side-by-side) finissant toujours par un export "copy as JSON/markdown/prompt" re-injectable.

Anti-pattern explicite : **l'auteur refuse la skill-ification** de sa pratique. *"I'm a little bit afraid that people will read this article and turn it into a /html skill. You don't need to do much — just ask it to 'make a HTML file'."* La pratique est trop contextuelle pour être figée.

FAQ honnête : HTML coûte plus de tokens mais le **1MM context d'Opus 4.7** absorbe ; génération 2-4× plus lente ; **diffs HTML bruyants** = downside non résolu, assumé.

Méta-thèse finale : HTML comme **antidote au cognitive surrender**. *"I had begun to fear that because I had stopped reading plans in depth I would simply have to leave Claude to make its choices. But I feel more in the loop than ever before when using HTML."* La lisibilité retrouvée permet de rester décisionnaire face à des agents de plus en plus puissants.

L'article s'articule directement avec **Meng To `design.md`** (HTML = "finished dish") et avec **Osmani comprehension debt** dont il propose une réponse opérationnelle.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Thariq Shihipar | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Thariq Shihipar | PERSONNE | fait_partie_de | équipe Claude Code | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Thariq Shihipar | PERSONNE | recommande | HTML comme format de sortie par défaut | METHODOLOGIE | 0.98 | ATEMPOREL | déclaré_article |
| HTML | TECHNOLOGIE | remplace | Markdown pour artefacts agentiques longs | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Thariq Shihipar | PERSONNE | affirme_que | Markdown devient restrictif au-delà de ~100 lignes | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| HTML | TECHNOLOGIE | permet | densité d'information (tables, CSS, SVG, scripts, canvas) | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| HTML | TECHNOLOGIE | permet | interactivité bidirectionnelle (sliders, copy as prompt) | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| HTML | TECHNOLOGIE | améliore | taux de lecture des specs et rapports | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| HTML | TECHNOLOGIE | résout | cognitive surrender / comprehension debt (lisibilité retrouvée) | CONCEPT | 0.90 | ATEMPOREL | inféré |
| Claude Code | TECHNOLOGIE | utilise | codebase + MCP + git history + Chrome | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Opus 4.7 | TECHNOLOGIE | utilise | 1MM context window | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| 1MM context Opus 4.7 | CONCEPT | permet | absorption du coût tokens supplémentaire du HTML | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Throwaway HTML editor | METHODOLOGIE | utilise | export copy as JSON / markdown / prompt | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Thariq Shihipar | PERSONNE | s_oppose_à | skill-ification prématurée du pattern HTML | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Thariq Shihipar | PERSONNE | affirme_que | les diffs HTML sont bruyants et difficiles à reviewer (downside assumé) | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Génération HTML | METHODOLOGIE | mesure | 2-4× plus lente que Markdown | MESURE | 0.88 | ATEMPOREL | déclaré_article |
| Frontend design plugin | TECHNOLOGIE | permet | production de HTML stylé par Claude | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| Design system HTML unique | METHODOLOGIE | permet | cohérence stylistique cross-fichiers | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Article HTML effectiveness | DOCUMENT | converge_avec | design.md de Meng To (HTML = finished dish) | CONCEPT | 0.93 | ATEMPOREL | inféré |
| Article HTML effectiveness | DOCUMENT | résout | comprehension debt d'Osmani (réponse opérationnelle) | CONCEPT | 0.90 | ATEMPOREL | inféré |
| Claude Code | TECHNOLOGIE | permet | artefacts HTML pour specs, PR, rapports, éditeurs jetables | METHODOLOGIE | 0.96 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | emploie | Thariq Shihipar | PERSONNE | 0.97 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Thariq Shihipar | PERSONNE | rôle | Engineer & serial entrepreneur, équipe Claude Code chez Anthropic, X @trq212 | AJOUT |
| HTML (format de sortie agent) | METHODOLOGIE | catégorie | Format préféré pour artefacts agentiques riches (specs, plans, rapports, éditeurs) | AJOUT |
| Throwaway HTML editor | METHODOLOGIE | catégorie | Éditeur single-file purpose-built pour une donnée, finissant par export structuré | AJOUT |
| Anti-skill-ification | CONCEPT | catégorie | Refus de figer un pattern contextuel en skill prématurée | AJOUT |
| Cognitive surrender (réponse) | CONCEPT | catégorie | Pratique de rester dans la boucle décisionnelle via lisibilité HTML | AJOUT |
| html-effectiveness gallery | TECHNOLOGIE | catégorie | Site exemples de Shihipar (thariqs.github.io/html-effectiveness) | AJOUT |
| Diff HTML bruyant | CONCEPT | catégorie | Downside assumé du basculement Markdown → HTML | AJOUT |
| Design system HTML de référence | METHODOLOGIE | catégorie | Fichier HTML unique servant de blueprint stylistique inter-fichiers | AJOUT |
| Joyful artifact | CONCEPT | catégorie | Critère émotionnel-pragmatique de choix de format (engagement praticien) | AJOUT |
| Unreasonable effectiveness | CONCEPT | catégorie | Lignée rhétorique Wigner-Karpathy appliquée à HTML pour agents | AJOUT |
