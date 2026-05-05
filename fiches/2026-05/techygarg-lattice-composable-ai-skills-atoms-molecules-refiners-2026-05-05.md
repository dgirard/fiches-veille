# techygarg-lattice-composable-ai-skills-atoms-molecules-refiners-2026-05-05

## Veille
Repo GitHub `techygarg/lattice` qui formalise un framework de **skills composables** pour installer une *engineering discipline* dans les assistants IA de code (Claude Code, Cursor). Architecture trois-tiers distinctive : **Atoms** (guardrails mono-principe : clean code, DDD, sécurité, test quality, design-first), **Molecules** (workflows multi-étapes composant les atoms : design, implement, refactor, fix, review), **Refiners** (interviews guidées produisant des standards projet-spécifiques qui customisent le comportement des atoms). Pipeline opérationnel `lattice-init` → `design-blueprint` → `code-forge` → `review`, avec `refactor-safely` et `bug-fix` en écarts. Trois principes pivots : *"Skills over prompts"*, *"Composability over monoliths"*, ***"Living context over static config"*** — le dossier `.lattice/` grossit smartement à chaque cycle de feature. MIT, shell pur, 18 stars / 52 commits, série d'articles sur martinfowler.com expliquant cinq *collaboration patterns*. Convergence forte avec Vincent *Superpowers* (2026-04-02), Habert *PROJ-AI* (2026-05-05), Wescale *Usine Logicielle Augmentée* (2026-05-03), et — convergence doctrinale la plus haute sans lignage déclaré — **Compound Engineering** d'Every (Shipper/Klaassen 2025-12-11) : pipelines isomorphes (lattice-init→design-blueprint→code-forge→review ↔ ce:brainstorm→ce:plan→ce:work→ce:review), living context layer (`.lattice/` ↔ `docs/plans/+solutions/+brainstorms/`), design-first commun, review obligatoire en sortie. La doctrine 2026 du *coding agent harness* converge sur un vocabulaire stable, sans influence directe.

## Titre Article
Lattice — Composable AI skills that teach assistants structured thinking (design-first, context-aware, architecture-guided)

## Date
2026-05-05

## URL
https://github.com/techygarg/lattice

## Keywords
lattice, techygarg, composable AI skills, engineering discipline, AI coding assistant framework, Claude Code plugin, Cursor compatible, three-tier architecture, atoms guardrails, molecules workflows, refiners interview-driven, lattice-init, design-blueprint, code-forge, review, refactor-safely, bug-fix, .lattice folder, living context layer, skills over prompts, composability over monoliths, living context over static config, design-first methodology, five-level progressive design, DDD secure coding test quality, project-specific standards, versioned skill files, team-owned skills, single-purpose skills, multi-step workflows, martinfowler.com five collaboration patterns, MIT license, shell installation, marketplace plugin

## Authors
techygarg (auteur GitHub, identité réelle non précisée dans le README ; auteur d'une série d'articles publiée sur martinfowler.com).

## Ton
**Profil** : Repository GitHub d'un framework opinion-driven de skills pour coding agents, avec un README dense et structuré qui sert à la fois de pitch produit, de documentation d'architecture et de manifeste philosophique. L'auteur (techygarg) ne se présente pas par credentials institutionnels mais par la qualité du framework et par la publication d'une série d'articles sur **martinfowler.com** — réseau qui inclut Böckeler (*Harness engineering for coding agent users*, 2026-04-02) et Fowler lui-même (*Thoughtworks Retreat*, 2026-02-13). Public cible : tech leads et engineering managers qui veulent installer des standards inviolables dans leurs équipes utilisant Claude Code/Cursor, plus la communauté open-source de plugins Claude Code.

**Style** : Voix manifeste-prescriptive, registre tech-éditorial à forte densité conceptuelle. Trois choix éditoriaux marquants :

1. **Diagnostic court et brutal** : *"AI coding assistants jump straight to code, silently make design decisions, forget constraints mid-conversation, and produce output nobody reviewed against real standards."* Quatre verbes, quatre dysfonctionnements canoniques. Pas de hype, pas de promesse — un constat.

2. **Triade conceptuelle** : *Atoms / Molecules / Refiners* est un emprunt assumé à la chimie organique appliqué à l'ingénierie logicielle. C'est mémorisable, ça scale (mono-principe → workflow → customisation), et ça pose une grammaire de composition. Vocabulaire structurant.

3. **Trois principes-aphorismes** : *"Skills over prompts"*, *"Composability over monoliths"*, *"Living context over static config"*. Format Strunk & White du manifeste tech — chaque principe est une opposition binaire qui prend position.

**Métaphores travaillées** : *"living context layer"* pour le dossier `.lattice/` qui *"grows smarter across feature cycles"* (la mémoire-projet qui se compose), *"engineering discipline installed into any AI coding assistant"* (l'ingénierie comme *posture* à imposer à l'assistant). Pas d'émotion forcée, pas d'urgence factice, mais une autorité structurée par la cohérence du framework.

**Autorité** : construite par (a) la rigueur architecturale (three-tier explicite, pipeline nominatif), (b) la publication associée sur martinfowler.com (network anglo-saxon thoughtworks-fluent), (c) l'opérationnalité immédiate (plugin Claude Code installable + script local), (d) la licence MIT et le code shell pur (transparence et adoption sans friction). Petit projet (18 stars / 52 commits) mais positionnement adulte — c'est de la doctrine packagée, pas un side-project hâtif.

## Pense-betes
- **Source** : repo GitHub `techygarg/lattice` (https://github.com/techygarg/lattice). MIT license, **18 stars / 0 forks / 52 commits** (snapshot mai 2026), code 100% shell.
- **Date d'ajout au dossier veille** : 2026-05-05 (URL apportée par mobile-share). Le repo lui-même n'expose pas de date claire dans le README extrait — projet en cours, jeune, mais doctrinalement abouti.
- **Auteur** : `techygarg` — identité réelle non documentée dans le README ; signe une série d'articles sur **martinfowler.com** expliquant cinq *collaboration patterns* sous-jacents.
- **Tagline** : *"Install engineering discipline into any AI coding assistant"* / *"Composable AI skills that teach assistants structured thinking — design-first, context-aware, and architecture-guided."*
- **Diagnostic d'ouverture** : *"AI coding assistants jump straight to code, silently make design decisions, forget constraints mid-conversation, and produce output nobody reviewed against real standards."* — quatre dysfonctionnements canoniques de l'agent en 2026.
- **Trois principes pivots** :
  1. **Skills over prompts** — fichiers skill versionnés et team-owned dans le repo > prompts personnels sur machines individuelles.
  2. **Composability over monoliths** — skills mono-purpose combinables > documents d'instructions exhaustifs.
  3. **Living context over static config** — le dossier `.lattice/` *"grows smarter across feature cycles"* (mémoire qui se compose au fil des features livrées).
- **Architecture trois-tiers (originalité conceptuelle clé)** :
  | Tier | Fonction | Couvre |
  |------|----------|--------|
  | **Atoms** | Guardrails mono-principe | Clean code, architecture, DDD, secure coding, test quality, design-first approach |
  | **Molecules** | Workflows multi-étapes composant les atoms | Design, implement, refactor, fix, review |
  | **Refiners** | Interviews guidées produisant standards projet-spécifiques | Customisent le comportement des atoms pour un team / un repo |
- **Pipeline canonique** : `lattice-init` → `design-blueprint` → `code-forge` → `review` (séquence principale, design-first), avec `refactor-safely` et `bug-fix` en écarts pour le travail structural et défensif.
- **Cinq commandes / skills principales** :
  - `/lattice-init` — project scanning + configuration initiale
  - `/design-blueprint` — **five-level progressive design approach** (design avant code)
  - `/code-forge` — implémentation appliquant les quality standards
  - `/review` — auditing des changes + persistance d'insights dans le `.lattice/`
  - `/refactor-safely` — refonte structurale guidée
  - `/bug-fix` — workflow defect-driven
- **Living context layer (`.lattice/`)** : dossier qui accumule **project standards, décisions, review insights** au fil des features. C'est l'équivalent du `DOCTRINE/` + `DR/` de Habert PROJ-AI, ou du `CLAUDE.md`/`AGENTS.md` enrichi de patterns appris.
- **Installation** :
  - **Plugin Claude Code** : `/plugins marketplace add techygarg/lattice` → `/plugins install lattice` → `/reload-plugins`. Compatible Cursor.
  - **Local** : `git clone https://github.com/techygarg/lattice.git` puis `./tools/install.sh /absolute/path/to/your/skills/folder`.
- **Documentation associée** : Origin Story, How It Works, Practical Guide, Configuration Reference, Framework Intelligence, Collaborative Judgment + série d'articles sur **martinfowler.com** sur les **cinq collaboration patterns** sous-jacents (réseau Böckeler/Fowler/Thoughtworks).
- **Articulation dossier veille (forte densité de convergence)** :
  - **Famille immédiate (skills frameworks pour coding agents 2026)** :
    - **Vincent *Superpowers*** (2026-04-02) : framework Skills agentiques avec SKILL.md, TDD strict, brainstorming. Lattice = même catégorie, mais pousse plus loin la **composition formelle** (atoms→molecules→refiners) et le **design-first** explicite.
    - **Anthropic *Skills*** (2025-10-16, Willison 2025-10-16) : annonce officielle des Skills Claude. Lattice est une mise en œuvre opinionated de cette primitive.
    - **Karpathy *Skills pour Claude Code*** (2026-01-27) : 4 principes anti-bloat. Lattice converge sur la simplicité et l'anti-monolithisme (*"composability over monoliths"*).
    - **Curran *Skills-Based Plugin Architecture*** (2026-04-16) : Intercom, marketplace privé 153 contributeurs / 267 skills. Lattice = équivalent open-source individuel d'un marketplace de skills, mais avec **architecture imposée** (Atoms/Molecules/Refiners).
    - **Habert WEnvision PROJ-AI*** (2026-05-05) : repo+agent+doctrine, six zones. Lattice partage la même thèse *living context > static config* mais s'oriente **production logicielle** plutôt que **conduite de projet**.
    - **Wescale Usine Logicielle Augmentée** (2026-05-03) : 6 lignes de fabrication, gouvernance injectée. Lattice = équivalent open-source qu'on installe en plugin Claude Code, là où Wescale est une méthodologie accompagnée par cabinet.
    - **Compound Engineering — Every** (Shipper/Klaassen 2025-12-11, Chow 2026-03-31, plugin GitHub Every 2025-12-10, Shipper *AI-native company* 2025-11-23) : **convergence doctrinale la plus forte** du corpus avec Lattice — sans lignage déclaré dans aucun sens.
      - **Pipelines isomorphes** : Lattice `lattice-init → design-blueprint → code-forge → review` ↔ CE `ce:brainstorm → ce:plan → ce:work → ce:review` (+ `compound` boucle).
      - **Living context layer** : Lattice `.lattice/` ↔ CE `docs/plans/`, `docs/solutions/`, `docs/brainstorms/` (mêmes artefacts vivants qui se composent au fil des features).
      - **Trois principes Lattice ↔ trois choix doctrinaux CE** : *Skills over prompts* ↔ slash-commands versionnés ; *Composability over monoliths* ↔ subagents spécialisés (12 reviewers ce:review) ; *Living context over static config* ↔ docs/plans comme living documents.
      - **Design-first commun** : `/design-blueprint` 5 niveaux ↔ Klaassen *Stop Coding and Start Planning* (2025-11-06) *three fidelities*.
      - **Review en sortie de pipeline** : Lattice `/review` ↔ CE `ce:review` (12 reviewers, scoring confiance, fixer queue).
      - **Distinctions** : (1) Lattice impose une **typologie formelle** (Atoms/Molecules/Refiners) absente de CE qui est plus *flat* ; (2) CE est porté par une **organisation media** (Every) qui en fait un produit éditorial vendable, Lattice est open-source individuel ; (3) **Maturité asymétrique** : CE en v2.60.0 avec marketplace plugin et adoption documentée hebdomadairement (Every Source Code), Lattice à 18 stars / 52 commits ; (4) **Networks éditoriaux distincts** — martinfowler.com/Thoughtworks (Lattice) vs Every (CE).
      - **Lecture** : les deux frameworks sont des **convergences indépendantes** sur les primitives qui s'imposent en 2026 pour discipliner les coding agents. La similarité de surface (slash-commands, pipeline 4 étapes, living docs, review obligatoire) est le **vocabulaire stable** qui émerge — pas une influence directe.
  - **Famille théorique (harness engineering)** :
    - **Trivedy *Anatomy of an Agent Harness*** (2026-03-10) : Agent = Modèle + Harnais, 7 primitives. Lattice = harnais opérationnel concret qui implémente plusieurs primitives.
    - **Osmani *Agent Harness Engineering*** (2026-04-19) : équation et 7 primitives consolidées, *AGENTS.md "pilot's checklist"*. Lattice s'inscrit dans cette doctrine.
    - **Böckeler *Harness engineering for coding agent users*** (2026-04-02, martinfowler.com) : feedforward guides, feedback sensors. **Même réseau éditorial** que Lattice (martinfowler.com).
    - **Seale *Semantic Agent: (Model+Harness) + (Ontology+Data)*** (2026-04-17) : étend l'équation harnais avec ontologie. Lattice = volet opérationnel design-first + composition.
  - **Famille design-first / specs** :
    - **Osmani *How to write a good spec for AI agents*** (2026-01-13) : 5 principes specs, Plan Mode. Lattice fait du design-first un *level 0* obligatoire.
    - **Klaassen *Stop Coding and Start Planning*** (2025-11-06) : compounding engineering, three fidelities. Lattice converge.
  - **Lien martinfowler.com** : Lattice s'inscrit dans le réseau qui inclut **Böckeler** (avril 2026), **Fowler** (*Thoughtworks Retreat*, 2026-02-13). C'est un réseau anglo-saxon Thoughtworks-fluent qui pose le vocabulaire de référence du *coding agent discipline* en 2026.
- **Limites à signaler** :
  - **Petit repo** (18 stars / 52 commits) — pas encore de validation par adoption massive comme Superpowers (130k+ stars).
  - **Code 100% shell** — installation simple mais lock-in opérationnel sur l'environnement Claude Code/Cursor.
  - **Documentation dense mais récente** — la maturité réelle des Atoms/Molecules/Refiners reste à éprouver en mission.
  - **Auteur peu identifié institutionnellement** — autorité construite par le framework lui-même + lien martinfowler.com, mais pas de credentials publics évidents.
- **À mobiliser pour** : architecture d'un dossier `.skills/` interne pour équipe Claude Code ; comparaison side-by-side avec Vincent *Superpowers* et Habert *PROJ-AI* dans une présentation dirigeants ; référence dans un dossier *harness engineering* français qui comparerait les approches FR (PROJ-AI, Wescale) vs anglo-saxonnes (Lattice, Superpowers).

## RésuméDe400mots

`techygarg/lattice` est un framework open-source MIT de skills composables conçu pour *"installer une engineering discipline dans n'importe quel assistant IA de code"* (Claude Code, Cursor). Le repo expose un diagnostic concis : *"les assistants IA sautent directement au code, prennent silencieusement des décisions de design, oublient les contraintes en cours de conversation, et produisent du code que personne ne review contre des standards réels."*

Lattice répond par trois principes-aphorismes : **Skills over prompts** (fichiers versionnés team-owned > prompts personnels), **Composability over monoliths** (skills mono-purpose composables > documents exhaustifs), **Living context over static config** (le dossier `.lattice/` *"grows smarter across feature cycles"*).

L'originalité conceptuelle réside dans l'**architecture trois-tiers** :
- **Atoms** : guardrails mono-principe couvrant clean code, architecture, DDD, secure coding, test quality, design-first.
- **Molecules** : workflows multi-étapes composant les atoms — design, implement, refactor, fix, review.
- **Refiners** : interviews guidées produisant des standards projet-spécifiques qui customisent le comportement des atoms pour un team donné.

Le pipeline canonique séquence `lattice-init` → `design-blueprint` → `code-forge` → `review`, avec `refactor-safely` et `bug-fix` en écarts. La commande `/design-blueprint` impose un *five-level progressive design approach* — design-first comme convention non négociable. Le dossier `.lattice/` accumule *project standards, décisions, review insights* en mémoire vive du projet.

Installation soit via plugin Claude Code (`/plugins marketplace add techygarg/lattice`) compatible Cursor, soit via clone + script shell `install.sh`. Documentation dense (Origin Story, How It Works, Practical Guide, Configuration Reference, Framework Intelligence, Collaborative Judgment) prolongée par une **série d'articles sur martinfowler.com** sur cinq *collaboration patterns* — même réseau éditorial que **Böckeler** (*Harness engineering for coding agent users*, 2026-04-02) et **Fowler** (*Thoughtworks Retreat*, 2026-02-13).

Lattice s'inscrit dans la **convergence doctrinale 2026** des skills frameworks pour coding agents, aux côtés de Vincent *Superpowers* (2026-04-02), Anthropic *Skills* (2025-10-16), Curran *Skills-Based Plugin Architecture* (Intercom 2026-04-16), Habert *PROJ-AI* (WEnvision 2026-05-05), Wescale *Usine Logicielle Augmentée* (2026-05-03) et — convergence la plus forte du corpus sans lignage déclaré — **Compound Engineering** (Every, Shipper/Klaassen 2025-12-11) : pipelines isomorphes (`lattice-init → design-blueprint → code-forge → review` ↔ `ce:brainstorm → ce:plan → ce:work → ce:review`), living context layer (`.lattice/` ↔ `docs/plans/+solutions/+brainstorms/`), trois principes Lattice cartographiables sur trois choix doctrinaux CE. Comparé à Vincent (130k+ stars, mature), Lattice (18 stars) propose une **architecture plus formelle** (atoms/molecules/refiners) et un **design-first explicite** comme niveau zéro.

Limites : repo encore jeune, validation d'adoption massive non établie, auteur peu documenté institutionnellement, code 100% shell. Mais positionnement adulte : c'est de la doctrine packagée et installable en plugin, pas un prototype hâtif. Pièce utile pour qui veut comparer des architectures de skills entre approches FR (PROJ-AI, Wescale) et anglo-saxonnes (Lattice, Superpowers).

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| techygarg | PERSONNE | a_créé | Lattice | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Lattice | TECHNOLOGIE | est | framework de skills composables | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Lattice | TECHNOLOGIE | s_installe_dans | Claude Code et Cursor | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Lattice | TECHNOLOGIE | est_structuré_en | trois tiers (Atoms / Molecules / Refiners) | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Atoms | CONCEPT | sont | guardrails mono-principe | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Molecules | CONCEPT | composent | atoms en workflows multi-étapes | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Refiners | CONCEPT | customisent | comportement des atoms via interviews guidées | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Pipeline canonique Lattice | METHODOLOGIE | séquence | lattice-init → design-blueprint → code-forge → review | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| .lattice folder | TECHNOLOGIE | est | living context layer projet | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| techygarg | PERSONNE | publie | série d'articles sur martinfowler.com | EVENEMENT | 0.93 | DYNAMIQUE | déclaré_article |
| Lattice | TECHNOLOGIE | impose | design-first progressive approach (5 niveaux) | METHODOLOGIE | 0.94 | ATEMPOREL | déclaré_article |
| Lattice | TECHNOLOGIE | affirme_que | "Skills over prompts" | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Lattice | TECHNOLOGIE | affirme_que | "Composability over monoliths" | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Lattice | TECHNOLOGIE | affirme_que | "Living context over static config" | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Lattice | TECHNOLOGIE | est_publié_sous | licence MIT | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Lattice | TECHNOLOGIE | est_dans | famille des skills frameworks 2026 | CONCEPT | 0.94 | DYNAMIQUE | inféré |
| Lattice | TECHNOLOGIE | converge_avec | Superpowers (Vincent) | TECHNOLOGIE | 0.92 | ATEMPOREL | inféré |
| Lattice | TECHNOLOGIE | converge_avec | PROJ-AI (Habert WEnvision) | METHODOLOGIE | 0.91 | ATEMPOREL | inféré |
| Lattice | TECHNOLOGIE | converge_avec | Compound Engineering (Every) | METHODOLOGIE | 0.93 | ATEMPOREL | inféré |
| Lattice pipeline | METHODOLOGIE | est_isomorphe_à | pipeline ce:brainstorm → ce:plan → ce:work → ce:review | METHODOLOGIE | 0.91 | ATEMPOREL | inféré |
| .lattice folder | TECHNOLOGIE | est_isomorphe_à | docs/plans + docs/solutions + docs/brainstorms (CE) | TECHNOLOGIE | 0.90 | ATEMPOREL | inféré |
| Lattice | TECHNOLOGIE | s_inscrit_dans | réseau éditorial martinfowler.com | ORGANISATION | 0.89 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| techygarg | PERSONNE | rôle | Auteur GitHub du framework Lattice + série d'articles martinfowler.com sur cinq collaboration patterns | AJOUT |
| Lattice | TECHNOLOGIE | catégorie | Framework open-source MIT de skills composables pour coding agents Claude Code/Cursor | AJOUT |
| Architecture trois-tiers Lattice | CONCEPT | description | Atoms (guardrails mono-principe) → Molecules (workflows multi-étapes composant atoms) → Refiners (interviews guidées customisant atoms par projet) | AJOUT |
| Atoms (Lattice) | CONCEPT | exemples | Clean code, architecture, DDD, secure coding, test quality, design-first approach | AJOUT |
| Molecules (Lattice) | CONCEPT | exemples | Design, implement, refactor, fix, review — workflows multi-étapes | AJOUT |
| Refiners (Lattice) | CONCEPT | rôle | Interviews guidées produisant standards projet-spécifiques qui customisent le comportement des atoms | AJOUT |
| Pipeline Lattice | METHODOLOGIE | séquence | lattice-init → design-blueprint → code-forge → review (+ refactor-safely, bug-fix en écarts) | AJOUT |
| /design-blueprint (Lattice) | METHODOLOGIE | description | Five-level progressive design approach — design-first comme convention non négociable | AJOUT |
| .lattice folder | TECHNOLOGIE | description | Living context layer qui accumule project standards, décisions, review insights au fil des feature cycles | AJOUT |
| Trois principes Lattice | CONCEPT | détail | (1) Skills over prompts, (2) Composability over monoliths, (3) Living context over static config | AJOUT |
| Cinq collaboration patterns (Lattice) | CONCEPT | source | Série d'articles martinfowler.com par techygarg expliquant les patterns sous-jacents au framework | AJOUT |
| Diagnostic Lattice | CONCEPT | citation | "AI coding assistants jump straight to code, silently make design decisions, forget constraints mid-conversation, and produce output nobody reviewed against real standards." | AJOUT |
| Famille skills frameworks 2026 | CONCEPT | composants | Lattice (techygarg), Superpowers (Vincent), Skills (Anthropic), PROJ-AI (Habert WEnvision), Skills-Based Plugin Architecture (Curran/Intercom), Usine Logicielle Augmentée (Wescale), Compound Engineering (Every / Shipper / Klaassen) | MISE_A_JOUR |
| Convergence Lattice ↔ Compound Engineering | CONCEPT | description | Pipelines isomorphes (lattice-init→design-blueprint→code-forge→review ↔ ce:brainstorm→ce:plan→ce:work→ce:review), living context layer (.lattice/ ↔ docs/plans+solutions+brainstorms), 3 principes Lattice ↔ 3 choix doctrinaux CE, design-first commun. Sans lignage déclaré dans aucun sens — convergence indépendante sur le vocabulaire stable 2026. | AJOUT |
