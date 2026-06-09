# klaassen-compound-engineering-definitive-guide-every-2026-02-09

## Veille
Manuel de référence du compound engineering : boucle agentique en 7 étapes (Ideate→Brainstorm→Plan→Work→Review→Polish→Compound), plugin 40+ agents, échelle d'adoption 5 stades, règle 50/50 — Kieran Klaassen (Cora / Every) - Every Source Code

## Titre Article
Compound Engineering: The Definitive Guide

## Date
2026-02-09

## URL
https://every.to/source-code/compound-engineering-the-definitive-guide

## Keywords
compound engineering, philosophie AI-native, boucle 7 étapes, complexité inversée, Claude Code, plugin open source, subagents, code review multi-agents, agent-native, règle 50/50, plans are the new code, échelle adoption 5 stades, leçons apprises, docs/solutions, CLAUDE.md, harness, vibe coding, /lfg, Cora, Every

## Authors
Kieran Klaassen (avec Claude & GPT crédités co-auteurs du guide complet)

## Ton
**Profil** : Perspective de praticien-fondateur (GM produit), registre de manifeste-handbook doctrinal, niveau intermédiaire à avancé

**Description** : Kieran Klaassen écrit en mode « manuel de référence » — le texte se présente explicitement comme *The Definitive Guide* et ambitionne de figer le vocabulaire, la philosophie et l'outillage d'un mouvement déjà diffusé par plusieurs articles antérieurs d'Every. Le ton est assuré, presque doctrinal : il pose une définition canonique (*« each unit of engineering work should make subsequent units easier—not harder »*) puis l'oppose frontalement au destin habituel des codebases qui se dégradent (*« after 10 years, teams spend more time fighting their system than building »*). L'autorité repose sur la preuve par l'usage — Cora et les cinq produits d'Every tenus par des équipes d'une seule personne. La rhétorique procède par renversements de croyances (*« beliefs to unlearn »* / *« beliefs to adopt »*), par maximes percutantes (*« Plans are the new code »*, *« Ship more value. Type less code. »*, *« Taste belongs in systems, not in review. »*) et par un dispositif pédagogique très structuré (échelle d'adoption, checklists, exemples de code). Le public cible : développeurs et leaders techniques voulant passer d'un usage ponctuel de l'IA à une ingénierie agentique systématisée.

## Pense-betes
- **Définition canonique** : Le compound engineering est l'approche où *chaque unité de travail d'ingénierie rend les suivantes plus faciles, pas plus difficiles*. Inversion de la trajectoire de complexité : les corrections de bugs éliminent des catégories entières de bugs futurs, les patterns deviennent des outils, le codebase devient plus facile avec le temps.
- **Boucle principale en 7 étapes** : **Ideate → Brainstorm → Plan → Work → Review → Polish → Compound → (Repeat)**. Trois phases : décision humaine (quoi construire ?), exécution agent (plan/code/test/PR), jugement humain (output suffisant ? le système a-t-il appris ?).
  1. **Ideate** (`/ce-ideate`) : ambiguïté → options produit priorisées (scoring confiance/impact/complexité).
  2. **Brainstorm** (`/ce-brainstorm`) : idée floue → requirements concrets, sauvés dans `docs/brainstorms/`.
  3. **Plan** (`/ce-plan`) : 3 agents de recherche parallèles (repo, framework-docs, best-practices) + spec-flow-analyzer → plan structuré dans `docs/plans/`.
  4. **Work** (`/ce-work`) : isolation (git worktree), exécution pas-à-pas, validations, PR.
  5. **Review** (`/ce-code-review`) : reviewers spécialisés en parallèle, findings priorisés **P1/P2/P3**.
  6. **Polish** (`/ce-polish-beta`) : clic réel dans l'app, ce qui « feels wrong » (vitesse, anim, copy, empty states).
  7. **Compound** (`/ce-compound`) : « l'étape critique » — capturer la solution dans `docs/solutions/` avec frontmatter YAML, mettre à jour CLAUDE.md, créer des agents. *« Would the system catch this automatically next time? »*
- **Le plugin** (`EveryInc/compound-engineering-plugin`) : **40+ agents spécialisés**, **30+ slash commands**, **35+ skills**. Review = ~23 reviewers (always-on : correctness, testing, maintainability, project-standards, agent-native, learnings ; conditionnels : security, performance, API contract, migrations, reliability, adversarial ; stack-specific : Rails, Python, TypeScript, Swift/iOS, frontend-races). Installable sur Claude Code, Cursor, Codex (+ Copilot, Factory Droid, Gemini, etc.).
- **Arborescence projet** : `CLAUDE.md`/`AGENTS.md` (fichier le plus important, lu chaque session) + `.compound-engineering/config.local.yaml` + `docs/brainstorms/`, `docs/plans/`, `docs/solutions/` (catégorisé : performance-issues, security-issues, architecture-patterns, conventions…).
- **`/lfg`** : développement autonome idée→PR mergée (Plan → Work → review+autofix → tests browser → commit/push/PR).
- **Règle 50/50 (révision du 80/20)** : 50% du temps à construire des features, 50% à améliorer le système (agents de review, doc de patterns, générateurs de tests). ROI : 1h à créer un agent de review économise 10h sur l'année — *les améliorations système composent, les features non*.
- **8 croyances à désapprendre** : le code doit être écrit à la main / chaque ligne revue manuellement / la solution vient de l'ingénieur / le code est l'artefact principal / les premiers jets doivent être bons (*« first attempts have a 95% garbage rate »*) / le code est expression de soi (*« the code is not really yours »*) / plus on tape plus on apprend (*« understanding matters more than muscle memory »*) / pensée ingénierie ≠ pensée produit.
- **8 croyances à adopter** : extraire son *taste* dans le système ; règle 50/50 ; faire confiance au process + filets de sécurité ; **environnement agent-native** (*« if a developer can see or do something, the agent should too »*) ; parallélisation (nouveau bottleneck = compute, plus l'attention humaine) ; *« Plans are the new code »* ; *« engineers are product people now »* ; laisser les agents tourner pendant l'absence.
- **Échelle d'adoption en 5 stades** : 0 manuel → 1 chat-assistance → 2 agentique avec review ligne-à-ligne (la plupart plafonnent ici) → **3 plan-first, review au niveau PR (transition clé : le compound engineering commence ici)** → 4 idée→PR (1 machine) → 5 exécution cloud parallèle (multi-features, multi-devices).
- **Agent-native — 4 niveaux** : (1) dev de base (fichiers, tests, commits) ; (2) full local (browser, logs, PR) ; (3) visibilité prod (logs read-only, error tracking) ; (4) intégration complète (tickets, déploiement) → débloque le stade 5.
- **Skip permissions** : `alias cc='claude --dangerously-skip-permissions'` ; nom volontairement effrayant ; filets = git reset, tests, review PR, worktrees. Gain 5-10× en flow. Jamais en prod ni en apprentissage.
- **3 questions sans tooling** : *« What was the hardest decision? »* / *« What alternatives did you reject and why? »* / *« What are you least confident about? »*
- **Best practices détaillées** : *baby app* jetable pour itérer le design ; figma-design-sync + design-iterator ; codifier le *taste* design/copy dans des skills ; recherche utilisateur structurée (personas, frontmatter) lisible par l'IA ; extraction de patterns d'usage (heavy/struggle/workaround/abandonment) ; copy = UX (codifier la voix) ; product marketing automatisé (release notes + screenshots Playwright depuis le plan).
- **Lien fort veille** : texte de consolidation de la philosophie diffusée par [[shipper-klaassen-compound-engineering-every-agents-2025-12-11]], [[klaassen-stop-coding-start-planning-every-2025-11-06]], [[klaassen-teach-ai-think-senior-engineer-every-2025-11-07]] ; v260 review pipeline [[chow-compound-engineering-v260-review-pipeline-2026-03-31]] ; niveau 5 « Workflows / harness » de [[taylor-entis-every-eight-levels-ai-adoption-2026-06-02]].

## RésuméDe400mots
Kieran Klaassen signe avec *Compound Engineering: The Definitive Guide* le manuel de référence d'une philosophie d'ingénierie AI-native qu'Every promeut depuis fin 2025. La thèse est économique : l'IA transforme l'économie du développement, au point qu'Every fait tourner ses **cinq produits** (Cora, Spiral, Sparkle, Monologue, Proof) avec des **équipes d'une seule personne** — un ingénieur peut « ship like five ».

La **définition canonique** : *chaque unité de travail d'ingénierie devrait rendre les suivantes plus faciles, pas plus difficiles*. En ingénierie traditionnelle, chaque feature injecte de la complexité ; après dix ans, on combat son système plus qu'on ne construit. Le compound engineering inverse cette pente : les corrections de bugs éliminent des catégories entières de bugs futurs, les patterns deviennent des outils, le codebase devient *plus facile* avec le temps.

Le cœur opérationnel est une **boucle en sept étapes** : **Ideate → Brainstorm → Plan → Work → Review → Polish → Compound**, articulée en trois phases (décision humaine, exécution agent, jugement humain). Le **Plan** orchestre trois agents de recherche parallèles puis un spec-flow-analyzer ; le **Review** déploie des reviewers spécialisés (always-on, conditionnels, stack-specific) produisant des findings priorisés P1/P2/P3 ; le **Compound** — « l'étape critique » — capture chaque solution dans `docs/solutions/` avec frontmatter YAML et met à jour `CLAUDE.md`, transformant la connaissance en actif réutilisable et redistribué.

Tout ceci est outillé par un **plugin open source** (`EveryInc/compound-engineering-plugin`) : 40+ agents, 30+ slash commands, 35+ skills, installable sur Claude Code, Cursor, Codex. La commande `/lfg` automatise idée→PR mergée.

Le guide procède ensuite par renversement de croyances : **huit à désapprendre** (le code écrit à la main, la review ligne-à-ligne, le code comme expression de soi — *« first attempts have a 95% garbage rate »*) et **huit à adopter** (extraire son *taste* dans le système, la **règle 50/50** — moitié features, moitié amélioration du système —, l'environnement **agent-native** : *« if a developer can see or do something, the agent should too »*, la parallélisation, *« Plans are the new code »*).

L'adoption suit une **échelle de cinq stades**, de l'écriture manuelle (0) à l'exécution cloud parallèle (5), le compound engineering commençant au **stade 3** (plan-first, review au niveau PR). Klaassen détaille enfin des best practices : *baby app* design jetable, skip permissions, codification du *taste* (design, copy), recherche utilisateur structurée, extraction de patterns d'usage, marketing produit automatisé. Maximes-marqueurs : *« Taste belongs in systems, not in review »*, *« Ship more value. Type less code »*, *« Assign outcomes, not tasks »*.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Kieran Klaassen | PERSONNE | publie | Compound Engineering: The Definitive Guide | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| compound engineering | METHODOLOGIE | affirme_que | chaque unité de travail rend la suivante plus facile | AFFIRMATION | 0.98 | ATEMPOREL | déclaré_article |
| compound engineering | METHODOLOGIE | est_basé_sur | boucle 7 étapes Ideate-Brainstorm-Plan-Work-Review-Polish-Compound | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| étape Compound | CONCEPT | permet | capitalisation des leçons apprises en docs/solutions réutilisables | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| compound engineering | METHODOLOGIE | recommande | règle 50/50 (features / amélioration système) | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| compound engineering | METHODOLOGIE | recommande | environnement agent-native | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Every | ORGANISATION | publie | plugin compound-engineering (40+ agents) | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| plugin compound-engineering | TECHNOLOGIE | permet | review multi-agents P1/P2/P3 | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| plugin compound-engineering | TECHNOLOGIE | s_applique_à | Claude Code, Cursor, Codex | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Every | ORGANISATION | mesure | 5 produits opérés par des équipes d'une personne | MESURE | 0.95 | DYNAMIQUE | déclaré_article |
| Kieran Klaassen | PERSONNE | dirige | Cora | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| compound engineering | METHODOLOGIE | affirme_que | « Plans are the new code » | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| Kieran Klaassen | PERSONNE | affirme_que | l'adoption du compound engineering commence au stade 3 (plan-first, review niveau PR) | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Kieran Klaassen | PERSONNE | affirme_que | first attempts ont 95% de déchet | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| /lfg | TECHNOLOGIE | permet | développement idée vers PR mergée | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| compound engineering | METHODOLOGIE | catégorie | Philosophie d'ingénierie AI-native (travail cumulatif) | AJOUT |
| compound engineering | METHODOLOGIE | boucle | Ideate→Brainstorm→Plan→Work→Review→Polish→Compound | MISE_A_JOUR |
| compound engineering | METHODOLOGIE | principe_clé | règle 50/50, agent-native, Plans are the new code | AJOUT |
| Compound Engineering: The Definitive Guide | DOCUMENT | type | Handbook de référence (Every Source Code + guide complet) | AJOUT |
| Kieran Klaassen | PERSONNE | rôle | General Manager Cora, Every | MISE_A_JOUR |
| plugin compound-engineering | TECHNOLOGIE | attribut | 40+ agents, 30+ slash commands, 35+ skills, open source | MISE_A_JOUR |
| Every | ORGANISATION | produits | Cora, Spiral, Sparkle, Monologue, Proof (équipes d'une personne) | MISE_A_JOUR |
| échelle d'adoption | CONCEPT | stades | 0 manuel → 5 cloud parallèle (CE débute au stade 3) | AJOUT |
| Cora | TECHNOLOGIE | catégorie | Assistant email / chief of staff IA, produit Every | AJOUT |
