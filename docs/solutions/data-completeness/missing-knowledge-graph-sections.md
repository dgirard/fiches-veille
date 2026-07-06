---
title: "Ajout GrapheDeConnaissance manquant sur 60 fiches et reconstruction knowledge-base"
date: 2026-03-27
last_updated: 2026-06-16
category: data-completeness
tags:
  - knowledge-graph
  - fiches-veille
  - graphe-de-connaissance
  - knowledge-base
  - batch-update
  - parallel-agents
component: fiches/GrapheDeConnaissance + knowledge-base.md + kb/
severity: medium
symptoms:
  - 60 fiches sur ~207 ne contenaient pas de section "## GrapheDeConnaissance"
  - knowledge-base.md périmé (132 fiches indexées au 2026-03-02 vs 207+ fiches existantes)
  - Couverture du knowledge graph incomplète (1012 entités, 1695 triples seulement)
root_cause: Les 60 fiches avaient été créées avant l'introduction systématique de la section GrapheDeConnaissance dans le workflow, ou avaient été ajoutées sans cette section obligatoire
---

# Ajout GrapheDeConnaissance manquant sur 60 fiches et reconstruction knowledge-base

## Description du problème

Sur les ~207 fiches de veille du projet, 60 ne disposaient pas de la section `## GrapheDeConnaissance` (avec sous-sections `### Triples` et `### Entités`) pourtant requise par le format standardisé défini dans CLAUDE.md. Le fichier `knowledge-base.md`, généré par `scripts/build_knowledge_base.py`, était en conséquence périmé et incomplet : il ne référençait que 132 fiches avec 1012 entités et 1695 triples. Après identification des 60 fiches manquantes, ajout des sections KG à chacune d'entre elles via 6 agents parallèles, et reconstruction complète de la base de connaissances, le projet atteint désormais 211 fiches indexées, 1376 entités et 2630 triples.

## Root Cause

60 out of 207 fiches de veille in the `fiches/` directory were missing their `## GrapheDeConnaissance` section. This section is mandatory per the project's CLAUDE.md specification and is required by `scripts/build_knowledge_base.py` to generate the unified knowledge base (`knowledge-base.md` and `kb/` directory). The missing sections meant only 132 fiches were integrated into the knowledge graph, leaving it incomplete.

Causes de l'accumulation :
- Certaines fiches ont été créées avant la standardisation du format KG
- Certains workflows de création de fiches n'incluaient pas systématiquement la section
- Aucune validation automatisée pour vérifier la présence des sections requises
- Le script de build traitait silencieusement ce qui existait, sans signaler les absences

## Solution Steps

### 1. Identification des fichiers manquants

Comparaison de l'ensemble des fichiers `.md` sous `fiches/` (via Glob) avec ceux contenant `## GrapheDeConnaissance` (via Grep) pour identifier les 60 fichiers sans la section.

```bash
# Fichiers AVEC GrapheDeConnaissance
grep -rl "## GrapheDeConnaissance" fiches/  # → 147 fichiers

# Tous les fichiers .md
find fiches/ -name "*.md"                   # → 207 fichiers

# Différence = 60 fichiers à compléter
```

### 2. Traitement par lots parallèles

Les 60 fichiers ont été répartis en 6 lots de ~10 fichiers chacun, traités par 6 agents parallèles pour maximiser le débit :

| Lot | Fichiers | Période couverte |
|-----|----------|-----------------|
| 1 | 6 | 2024-06 à 2025-10 |
| 2 | 10 | 2025-11 (batch 1) |
| 3 | 10 | 2025-11 (batch 2) |
| 4 | 12 | 2025-11 (batch 3) |
| 5 | 13 | 2025-12 |
| 6 | 13 | 2026-01 + 2026-02 |

### 3. Génération du KG par fiche

Chaque agent a, pour chaque fichier de son lot :
1. Lu le contenu de la fiche pour comprendre le sujet de l'article
2. Généré une section `## GrapheDeConnaissance` avec :
   - `### Triples` — tableau 8 colonnes (Sujet, Type Sujet, Prédicat, Objet, Type Objet, Confiance, Temporalité, Source)
   - `### Entités` — tableau 5 colonnes (Entité, Type, Attribut, Valeur, Action)
3. Ajouté la section en fin de fiche via l'outil Edit
4. Respecté les règles CLAUDE.md : prédicats en français, confiance >= 0.70, 5-15 triples, types d'entités standards

Exemple de section ajoutée :

```markdown
## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Ethan Mollick | PERSONNE | affirme_que | IA transforme enseignement | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Wharton | ORGANISATION | utilise | outils IA en cours | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Ethan Mollick | PERSONNE | rôle | Professeur Wharton | AJOUT |
| Wharton | ORGANISATION | secteur | Éducation / Business School | AJOUT |
```

### 4. Reconstruction de la knowledge base

```bash
python3 scripts/build_knowledge_base.py
```

### 5. Vérification

| Métrique | Avant | Après |
|----------|-------|-------|
| Fiches intégrées | 132 | 211 |
| Entités uniques | 1012 | 1376 |
| Triples uniques | 1695 | 2630 |
| Entités majeures (pages kb/) | ~150 | 227 |
| Fichiers dans kb/ | 151 | 221 |

## Prevention Strategies

### 1. Validation à la création (Shift Left)

**Pre-commit hook :** Ajouter un hook git qui scanne tout fichier nouveau ou modifié sous `fiches/` et rejette les commits où une fiche ne contient pas les 10 sections requises (dont `## GrapheDeConnaissance`, `### Triples`, `### Entités`).

**Script de validation :** vérifier la présence des 10 en-têtes de section `##`, le tableau Triples (8 colonnes), le tableau Entités (5 colonnes) et un minimum de triples par fiche.

> **Mise à jour 2026-06-16** : ce garde-fou « shift-left » a depuis été **implémenté** sous la forme du **gate Bronze** `scripts/lint_fiches.py` (validation ontologie v2, bloquante — cf. CLAUDE.md « Architecture médaillon »), avec tests de régression `scripts/tests/test_lint_fiches.py` et `scripts/tests/test_frontmatter_compat.py`. ⚠️ Attention : ce gate valide le **Bronze** (`fiches/`) uniquement — il **ne contrôle pas la fraîcheur du Silver** (`kb/`, `knowledge-base.md`). La dérive décrite ci-dessous reste donc possible même avec un Bronze vert.

### 2. Détection précoce de la dérive

- Modifier `build_knowledge_base.py` pour émettre un avertissement clair avec la liste des fiches incomplètes au lieu de les ignorer silencieusement
- Ajouter un rapport de complétude :
  ```
  Total fiches: 211
  Complètes: 211
  Manquant GrapheDeConnaissance: 0
  ```

### 3. Maintien de la fraîcheur du KB

- Reconstruire après chaque ajout de fiches en lot
- Détecter la péremption en comparant les timestamps des fiches vs. le KB
- Objectif : KB reconstruit dans les 24h suivant tout ajout de fiche

#### Discipline « commit-together » Bronze + Silver (mise à jour 2026-06-16)

Le Silver (`kb/`, `knowledge-base.md`, `kb-*.md`) est un **artefact dérivé** : il doit être **régénéré et committé dans le même commit** que la modification Bronze qui le motive. Après tout ajout/édition d'une fiche :

1. `python3 scripts/lint_fiches.py` — gate Bronze, attendre « 0 violation ».
2. `python3 scripts/build_knowledge_base.py` — régénérer le Silver ; vérifier que le compteur bouge (ex. « Fiches avec GrapheDeConnaissance : 303 → 304 »).
3. `git status` — **confirmer qu'aucune fiche référencée par `index.md` ou le KB n'est laissée non trackée (`??`)**. Les nouvelles fiches ne se stagent pas toutes seules.
4. **Un seul commit** portant l'ensemble : la/les fiche(s) sous `fiches/` **+** `index.md` **+** `kb/` **+** `knowledge-base.md` **+** `kb-*.md` (périmètre de commit du projet ; jamais `docs/`, `.DS_Store`, `.obsidian/`).

**Deux modes de défaillance silencieux confirmés** :

- **Dérive du Silver** : ajouter une fiche sans relancer le build → le KG publié représente un corpus plus ancien et plus petit que les fiches, sans aucune erreur (le gate Bronze passe, le build n'est jamais invoqué).
- **Liens pendants** : committer `index.md` + `kb/` (qui référencent une fiche) alors que la fiche elle-même est restée `??` non trackée → publication de wikilinks/liens relatifs cassés sur GitHub. **Stager la fiche dans le même commit.**

**Heuristique de détection de péremption** : le Silver est suspect dès que (a) un changement sous `fiches/` est stagé sans changement correspondant sous `kb/`, ou (b) la mtime de la fiche la plus récente est postérieure à celle du KB (`ls -la kb/ knowledge-base.md` vs. dernier fichier de `fiches/`).

> **Mise à jour 2026-07-06 — détection automatisée (doctor)** : la détection
> heuristique manuelle ci-dessus est désormais **automatisée et bloquante** par
> `scripts/check_coherence.py` (« doctor »). Chaque générateur embarque un
> **manifest** (sha256 des champs consommés — `catalogue.tsv` en ligne 1,
> `knowledge-base.md` en commentaire) ; doctor recalcule et compare, retournant
> `STALE` (exit ≠ 0) si le Silver ou le catalogue ne reflète plus `fiches/`. La
> bijection catalogue ↔ fiches y détecte aussi les liens pendants. Lancer
> `python3 scripts/check_coherence.py` avant tout commit ; `--catalogue-only`
> avant toute lecture grep-first. La spec « validation automatisée et bloquante,
> pas indicative » est donc satisfaite côté Silver aussi. Voir
> [[index-genere-catalogue-machine]] et [[alias-entites-et-bornage-kb]].

> **Récurrence documentée (2026-06-16)** — deuxième occurrence du problème, cette fois en régime nominal (et non plus backfill) : les fichiers `kb/` étaient figés au « Jun 10 11:51 » alors que **9 fiches** avaient été ajoutées depuis (7 volets Williams ADLC + Nadella + Goodhart) ; les entités `Chris-Williams`, `Satya-Nadella`, `Charles-Goodhart`, `Marilyn-Strathern`, `ADLC` étaient absentes jusqu'au rebuild. De plus, les 7 fiches ADLC étaient **non trackées** dans git bien qu'`index.md` et le KB régénéré y renvoyaient déjà. La leçon : ce n'est pas qu'un risque de backfill ponctuel — la dérive se produit à **chaque** ajout unitaire si le rebuild + commit groupé n'est pas systématique.

## Best Practices pour les backfills parallèles

1. **Dimensionnement des lots** : 8-12 fiches par agent parallèle
2. **Idempotence** : vérifier l'absence de la section avant d'ajouter
3. **Exemplaires de référence** : fournir 2-3 fiches modèles dans le prompt agent
4. **Accès au contenu source** : les agents doivent lire la fiche complète pour générer des triples pertinents
5. **Audit post-backfill** : vérifier manuellement 10-15% des fiches traitées

## Monitoring

| Vérification | Fréquence | Méthode | Action |
|-------------|-----------|---------|--------|
| Nouvelle fiche complète | Chaque commit | Pre-commit hook | Bloquer le commit |
| Toutes fiches valides | Chaque push | Script validation | Avertissement |
| KB à jour | Avant chaque build | Comparaison timestamps | Rebuild |
| Qualité des triples | Mensuel | Revue manuelle de 5 fiches | Ajuster les prompts |

**Leçon principale** : la validation doit être automatisée et bloquante, pas indicative. La spécification CLAUDE.md était correcte et complète — le problème était l'absence d'enforcement.

## Cross-References

- **Format KG** : `CLAUDE.md` section "GrapheDeConnaissance — Format détaillé"
- **Architecture médaillon** (Bronze/Silver/Gold + table des gates) : `CLAUDE.md` section "Architecture médaillon (2026-06-11)"
- **Gate Bronze** : `scripts/lint_fiches.py` + tests `scripts/tests/test_lint_fiches.py`, `scripts/tests/test_frontmatter_compat.py`
- **Script de build (promotion Silver)** : `scripts/build_knowledge_base.py`
- **Plan initial du format KG** : `plans/2026-02-19-feat-knowledge-graph-section-fiches-plan.md`
- **Plan consolidation KB** : `docs/plans/2026-02-28-feat-knowledge-base-consolidee-graphe-connaissance-plan.md`
- **Plan backfill 123 fiches** : `docs/plans/2026-02-28-feat-ajout-graphe-connaissance-fiches-existantes-plan.md`
- **Plan validation** : `docs/plans/2026-03-01-feat-backfill-graphe-connaissance-64-fiches-plan.md`
- **Solution liée** : `docs/solutions/integration-issues/obsidian-wikilinks-pipe-escaping.md`
