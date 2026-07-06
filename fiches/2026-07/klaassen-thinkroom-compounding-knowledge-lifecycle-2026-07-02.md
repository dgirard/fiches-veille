---
themes: [agents-codage-ia-skills]
source: "Thinkroom (Kieran Klaassen)"
---
# klaassen-thinkroom-compounding-knowledge-lifecycle-2026-07-02

## Veille

Guide agent (Thinkroom, plateforme de Kieran Klaassen) documentant le **Compounding Knowledge Lifecycle** du compound-engineering-plugin (Every) : comment une leçon apprise une fois « continue de payer » — capturée, stockée, retrouvée et maintenue vraie. Décrit l'anatomie d'une *learning* (`docs/solutions/`), sa capture via `/ce-compound`, la carte mémoire (durable vs éphémère), la récupération *grep-first* (learnings-researcher) branchée sur 5 skills aux points de décision, et les trois contre-forces qui empêchent la mémoire de mentir. Directement pertinent : c'est la doctrine derrière la convention `docs/solutions/` de ce dépôt. Domaine : compound engineering, gestion de connaissance agentique, skills.

## Titre Article

The Compounding Knowledge Lifecycle — Agent Guide

## Date

2026-07-02

## URL

https://thinkroom.kieranklaassen.com/d/Yxr8tfwAVV

## Keywords

Compound engineering, compounding knowledge lifecycle, learning, solution doc, docs/solutions, /ce-compound, learnings-researcher, pattern doc, mémoire durable vs éphémère, grep-first, frontmatter, present evidence wins, coherence neighborhood, /ce-compound-refresh, retrait des classes de défaillance, CONCEPTS.md, repo-profile cache

## Authors

Kieran Klaassen (Thinkroom / Every — compound-engineering-plugin) ; document « Agent Guide » généré (byline « Claude Code / Anthropic »)

## Ton

**Profil** : guide technique de référence à visée agentique (« Agent Guide »), à la troisième personne, registre analytique et dense, structuré en 8 sections numérotées + glossaire. Niveau technique élevé, adressé autant à des agents qu'à des ingénieurs praticiens du compound engineering.

**Style** : explicatif et systématique, chaque section décrivant une phase du cycle (premise → capture → stockage → détection → refresh → boucle complète → pourquoi ça compose). Recours constant aux **tableaux** (rôles de chaque champ de frontmatter, consommateurs de la mémoire, modes de défaillance esquivés) et à des **descriptions de diagrammes**. **Métaphore filée financière** assumée et « méritée » : *learning = principal*, *retrieval qui change une décision = interest payment*, *pattern doc = reinvestment*, le corpus (35 docs) = *balance sheet*. Formules-doctrine : *« knowledge you'd mourn goes in git; knowledge you can re-derive goes in /tmp »*, *« present evidence wins »*, *« a confidently wrong memory is worse than none »*, *« not that documents accumulate, but that failure classes get retired »*, *« no empty hands »*. Autorité par l'auto-démonstration : le guide se prend lui-même comme corpus vivant (census de 35 learnings, feature `/ce-explain` livrée « hier », incident #714 réel). **Public cible** : concepteurs de systèmes agentiques et de skills, praticiens du compound engineering.

## Pense-betes

- **Le pari du compound engineering** : *« each unit of work should make the next unit easier »*. Le **code** améliore le *produit*, pas le *process* ; ce qui **compose**, c'est la **connaissance** — chaque problème résolu, concept nommé, convention documentés sous une forme **retrouvable au moment exact où le travail futur en a besoin**.
- **Le vrai verrou = la récupération**, pas l'écriture. Les postmortems « pourrissent dans les wikis parce que personne ne les relit ». Ce système **ferme la boucle** en rendant la récupération **automatique** dans 5 skills, pas une discipline volontaire.
- **Une *learning* (solution doc)** = 1 fichier markdown = 1 problème résolu, sous `docs/solutions/<category>/`. **Tout le frontmatter sert la *recherche*, pas le récit** : `title` (cible grep n°1), `tags` (surface de synonymes — on grep `tags:.*(menu|routing|handoff)` sans ouvrir un fichier), `module`/`component` (« est-ce ma zone ? »), `problem_type` (l'aiguillage), `applies_when` (test d'auto-sélection en 3 lignes), `severity` (classement quand plusieurs matchent), `date` (signal d'obsolescence).
- **`problem_type` = 2 pistes** : **bug-track** (ce qui a cassé : `runtime_error`, `test_failure`, `performance_issue`, `security_issue`…) et **knowledge-track** (ce qui a été *décidé/découvert* : `architecture_pattern`, `design_pattern`, `tooling_decision`, `convention`, `workflow_issue`, `best_practice`…). *« Un système qui ne retient que les bugs oublie l'essentiel de ce qu'une équipe apprend. »* Census vivant : **35 learnings, 6 catégories, skill-design en tête (20)**.
- **Pattern doc** = un cran au-dessus : généralisé à partir de *plusieurs* learnings → **plus de levier, plus de risque si périmé**. Aucun promu ici encore (`docs/solutions/patterns/critical-patterns.md` = slot en attente).
- **Capture = `/ce-compound`**, discipline cœur = le **timing** : documenter **tant que le contexte est frais** (même session que le fix, quand les tentatives ratées et le « ah, VOILÀ pourquoi » sont encore là). Une semaine après → dégénère en résumé.
- **Mécanique** : fan-out de subagents (**context analyzer** = catégorie/nom/frontmatter, **solution extractor** = corps en prose problem/investigation/solution/prevention, **related-docs finder** = anti-doublon) ; **l'orchestrateur seul écrit UN doc**, les subagents ne touchent jamais aux fichiers trackés. Autres portes d'entrée : `/ce-debug` (offre un compound après root-cause), `/ce-pov` (« compound it » → `tooling_decision` en headless), **lightweight mode** (petites leçons, skip anti-doublon).
- **« La vie d'une learning »** (exemple canonique) : issue **#714** (l'agent s'arrête après le menu) → root cause (routing par-option dans un fichier de référence non chargé) → fix + `/ce-compound` → learning `post-menu-routing-belongs-inline.md` → **test de régression** + **doctrine dans AGENTS.md** (« Inline the Trigger, Not the Content »). **Un incident, 4 artefacts durables.** *« Compounding » = les classes de défaillance sont retirées*, pas juste des docs qui s'accumulent.
- **Carte mémoire, axe = durabilité.** **DURABLE (git)** : `docs/solutions/` (les 35 learnings), `CONCEPTS.md` (vocabulaire/glossaire, jamais des specs), `STRATEGY.md` (direction/tracks), `docs/plans/` + `brainstorms/` (le **WHY**). **ÉPHÉMÈRE (dérivé)** : **repo-profile cache** (dérivé 1×/commit, partagé par 9 skills, jamais source de vérité — le supprimer ne perd rien). Règle : *knowledge you'd mourn → git ; re-derivable → /tmp*. Les **plans ne sont jamais édités après exécution** → ils expliquent encore le *pourquoi* des mois plus tard.
- **Détection : rien ne pousse la connaissance vers toi** (pas de digest, pas de « lis le wiki »). **5 skills la tirent** au moment de décider, via un protocole partagé **learnings-researcher**, **grep-first** (la mémoire est conçue pour être *cherchée* sans être *lue*). Entonnoir : 35 docs → greps parallèles de frontmatter → poignée de candidats (frontmatter ~30 lignes) → full-read des gagnants → **5 findings distillés** dans le contexte de l'appelant.
- **Consommateurs** : `/ce-plan` (learnings → contraintes & KTDs), `/ce-brainstorm` (cadre le scope), **`/ce-code-review`** (reviewer always-on : verdict **followed / violated** contre le diff réel — *« la dent la plus tranchante » ; une violation = un finding avec `file:line`, pas une suggestion*), `/ce-ideate` (élague les impasses passées), `/ce-debug` (fait remonter les root-causes connues).
- **2 règles de confiance** : (1) **Present evidence wins** — si une learning contredit le code actuel, on **signale le conflit** au lieu de l'échouer (une mémoire *confiante et fausse* est pire que rien) ; (2) **Date is signal** — chaque learning porte sa date pour peser si le monde a bougé.
- **Refresh — « une mémoire qui ne fait que croître finit par mentir ».** 3 contre-forces à tempos différents : **read time** (present evidence wins, gratuit) ; **write time** (à l'ajout/édition d'une entrée `CONCEPTS.md`, inspecter son **coherence neighborhood** — les termes frères référencés — et corriger la dérive *pour laquelle on a des preuves* ; borné, jamais un audit complet sur intuition) ; **on demand** (`/ce-compound-refresh`, balayage délibéré, **PAS un follow-up par défaut**, ne tourne que s'il y a une raison, prend un **scope hint** — `/ce-compound-refresh payments` — car un refresh full-corpus n'est presque jamais la bonne dépense).
- **La boucle complète via `/ce-explain`** (skill livrée « hier », tout est réellement arrivé) : brainstorm tire le repo-profile du cache ; planning fait remonter **5 learnings** (3 *must-apply* : inline menu routing [héritage de #714], `$ARGUMENTS` portability, `SKILL_DIR` anchor) ; implémentation crée son **test de régression miroir** ; review audite le diff contre **8 learnings** (tous suivis) et **rejette le fix proposé par un reviewer** qui aurait réintroduit le mode de défaillance d'origine (*« la mémoire n'a pas seulement informé le travail, elle l'a défendu »*) ; vocabulaire composé (*Explainer*, *Check-in* → `CONCEPTS.md`) ; résidu → **issue #1057** → future **learning #36**. *« No step required anyone to remember to consult the memory. »*
- **Pourquoi ça compose (métaphore financière)** : learning = **principal**, chaque retrieval qui change une décision = **interest payment**, pattern doc = **reinvestment**. Modes de défaillance esquivés : wiki rot, guidance périmée qui tue le neuf, accumulation non curée, mémoire invisible, décroissance, silos (un seul `docs/solutions/` sert 9 skills).
- **Lien direct avec ce dépôt** : la convention `docs/solutions/` (frontmatter `module`/`tags`/`problem_type`) documentée dans le `CLAUDE.md du repo veille` est exactement ce système ; les skills `compound-engineering:*` (`ce-compound`, `ce-plan`, `ce-code-review`, `ce-compound-refresh`…) sont installées ici. **Candidat naturel à promotion transverse cabinet** (pattern de capitalisation).

## RésuméDe400mots

Ce guide agent de Thinkroom (plateforme de Kieran Klaassen) décrit le **Compounding Knowledge Lifecycle** du compound-engineering-plugin : le mécanisme par lequel « une leçon apprise une fois continue de payer ». Le pari fondateur du compound engineering : *chaque unité de travail doit rendre la suivante plus facile*. Or le code améliore le produit, pas le process ; ce qui **compose**, c'est la **connaissance**, à condition d'être documentée sous une forme **retrouvable au moment exact du besoin**. Le vrai verrou n'est donc pas l'écriture (les postmortems « pourrissent dans les wikis ») mais la **récupération**, ici rendue **automatique** dans cinq skills plutôt que laissée à la discipline.

L'unité est la **learning** : un fichier markdown, un problème résolu, sous `docs/solutions/<category>/`, dont **tout le frontmatter sert la recherche** (`title`, `tags`, `module`, `problem_type`, `applies_when`, `severity`, `date`). Le `problem_type` sépare **bug-track** (ce qui a cassé) et **knowledge-track** (ce qui a été décidé/découvert) — car « un système qui ne retient que les bugs oublie l'essentiel ». Corpus vivant : 35 learnings, skill-design en tête. Au-dessus, le **pattern doc** généralise plusieurs learnings (plus de levier, plus de risque si périmé).

La **capture** se fait via `/ce-compound`, dont la discipline est le **timing** (documenter tant que le contexte est frais), avec un fan-out de subagents (analyzer, extractor, anti-doublon) pendant que l'orchestrateur seul écrit un unique doc. L'exemple canonique — l'incident #714 devenant fix + learning + test + doctrine — montre que « compounding » signifie **retirer des classes de défaillance**, pas empiler des documents.

La **carte mémoire** oppose le durable (git : `docs/solutions/`, `CONCEPTS.md`, `STRATEGY.md`, plans/brainstorms = le WHY) à l'éphémère (repo-profile cache re-dérivable). La **détection** ne pousse rien : cinq skills **tirent** au moment de décider via le **learnings-researcher** grep-first (35 docs → greps de frontmatter → candidats → full-read → 5 findings). Le `/ce-code-review` est « la dent la plus tranchante » : une violation devient un finding `file:line`. Deux règles de confiance protègent : **present evidence wins** et **date is signal**.

Enfin, le **refresh** empêche la mémoire de mentir via trois contre-forces (read time, write time via *coherence neighborhood*, on-demand `/ce-compound-refresh` scopé). La boucle est illustrée de bout en bout par la livraison de `/ce-explain`. Métaphore financière : learning = principal, retrieval = intérêt, pattern doc = réinvestissement — un système où le travail neuf « arrive immunisé contre les erreurs passées ».

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Compound engineering | METHODOLOGIE | affirme_que | "chaque unité de travail doit rendre la suivante plus facile" | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Compounding Knowledge Lifecycle | METHODOLOGIE | est_basé_sur | docs/solutions/ (mémoire qui compose) | DOCUMENT | 0.94 | ATEMPOREL | déclaré_article |
| Learning | DOCUMENT | fait_partie_de | docs/solutions/ | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Learning | DOCUMENT | est_basé_sur | frontmatter conçu pour la recherche (grep-first) | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| /ce-compound | TECHNOLOGIE | permet | capture d'une learning tant que le contexte est frais | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| /ce-compound | TECHNOLOGIE | utilise | subagents (context analyzer, solution extractor, related-docs finder) | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| learnings-researcher | METHODOLOGIE | permet | récupération grep-first aux points de décision (5 skills) | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| /ce-code-review | TECHNOLOGIE | utilise | learnings pour un verdict followed/violated contre le diff | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| /ce-plan | TECHNOLOGIE | utilise | learnings comme contraintes et KTDs | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Pattern doc | DOCUMENT | est_basé_sur | plusieurs learnings généralisées | DOCUMENT | 0.9 | ATEMPOREL | déclaré_article |
| repo-profile cache | TECHNOLOGIE | est_instance_de | connaissance éphémère re-dérivable | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Compounding Knowledge Lifecycle | METHODOLOGIE | recommande | "present evidence wins" (signaler le conflit si le code contredit) | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| /ce-compound-refresh | TECHNOLOGIE | résout | obsolescence de la mémoire (balayage scopé, non par défaut) | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Compounding Knowledge Lifecycle | METHODOLOGIE | affirme_que | "compounding = retirer des classes de défaillance, pas empiler des docs" | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Compounding Knowledge Lifecycle | METHODOLOGIE | résout | wiki rot (postmortems non relus) | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Kieran Klaassen | PERSONNE | a_créé | Thinkroom | TECHNOLOGIE | 0.85 | STATIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Compounding Knowledge Lifecycle | METHODOLOGIE | définition | Cycle capture→stockage→récupération→refresh rendant la connaissance composable | AJOUT |
| Compound engineering | METHODOLOGIE | principe | Chaque unité de travail rend la suivante plus facile (via la connaissance) | AJOUT |
| Learning | DOCUMENT | définition | 1 markdown = 1 problème résolu sous docs/solutions/<category>/, frontmatter orienté recherche | AJOUT |
| Pattern doc | DOCUMENT | définition | Guidance généralisée depuis plusieurs learnings (plus de levier, plus de risque si périmé) | AJOUT |
| docs/solutions/ | DOCUMENT | census | 35 learnings, 6 catégories, skill-design en tête (20) | AJOUT |
| /ce-compound | TECHNOLOGIE | rôle | Capture d'une learning tant que le contexte est frais (fan-out de subagents) | AJOUT |
| /ce-compound-refresh | TECHNOLOGIE | rôle | Balayage d'obsolescence délibéré et scopé (jamais par défaut) | AJOUT |
| learnings-researcher | METHODOLOGIE | rôle | Protocole de récupération grep-first partagé par 5 skills | AJOUT |
| /ce-code-review | TECHNOLOGIE | rôle | Reviewer always-on : verdict followed/violated (violation = finding file:line) | AJOUT |
| CONCEPTS.md | DOCUMENT | rôle | Vocabulaire partagé (glossaire, jamais des specs) | AJOUT |
| repo-profile cache | TECHNOLOGIE | nature | Connaissance éphémère dérivée 1×/commit, partagée par 9 skills | AJOUT |
| Coherence neighborhood | CONCEPT | définition | Termes frères d'un concept, inspectés/réparés au write time contre la dérive sémantique | AJOUT |
| Present evidence wins | CONCEPT | règle | Si le code contredit une learning, signaler le conflit (ne pas l'écho) | AJOUT |
| Kieran Klaassen | PERSONNE | rôle | Créateur de Thinkroom (Every / compound-engineering-plugin) | AJOUT |
| Thinkroom | TECHNOLOGIE | catégorie | Plateforme collaborative hébergeant l'agent guide | AJOUT |
| Incident #714 | EVENEMENT | résultat | Fix + learning + test de régression + doctrine AGENTS.md (classe de défaillance retirée) | AJOUT |
