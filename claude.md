# Structure d'analyse d'article pour la veille

Dépôt de veille technologique **100 % fichiers** (pas de serveur), manipulé
surtout par une IA. Architecture médaillon : `raw-data/` (Raw) → `fiches/`
(Bronze) → `kb/` + `knowledge-base.md` + `catalogue.tsv` + `index.md` (Silver,
générés) → `gold/` (livrables). Tout est optimisé pour un coût en tokens bas
(production, mise à jour des index, récupération).

## Organisation des fichiers

```
veille/
├── index.md                    # Index HUMAIN généré (dates, thématiques, stats) — NE PAS ÉDITER
├── catalogue.tsv               # Index MACHINE généré (1 ligne/fiche) — point d'entrée grep-first
├── knowledge-base.md           # Dashboard KB généré (+ ligne manifest)
├── kb/                         # Pages entités générées (wikilinks Obsidian)
├── kb-*.md                     # KB thématiques curées à la main (context-engineering, …)
├── CONCEPTS.md                 # Vocabulaire de domaine partagé (fiche, médaillon, doctor, KB curée vs générée)
├── fiches/YYYY-MM/*.md         # Bronze : fiches par mois de PUBLICATION
├── scripts/                    # Outils stdlib Python + tests
├── docs/reference/             # Références versionnées (ontologie-kg, workflow-batch)
├── docs/solutions/             # Solutions documentées de problèmes passés (bugs, conventions, patterns), par catégorie + frontmatter YAML (module, tags, problem_type) — pertinent avant d'implémenter/déboguer
├── raw-data/                   # Contenu brut (gitignoré)
└── gold/                       # Livrables générés (gitignoré)
```

## Format standardisé d'une fiche

Dix sections, **dans cet ordre** (gelé) :

```
# [Identifiant Technique]
## Veille   ## Titre Article   ## Date   ## URL   ## Keywords
## Authors  ## Ton   ## Pense-betes   ## RésuméDe400mots   ## GrapheDeConnaissance
```

- **Identifiant** : `auteur-sujet-YYYY-MM-DD` (préfixe `skill-` pour une skill).
  **Unique globalement** (le lint le vérifie), **gelé après commit**.
- **Date** (ISO `YYYY-MM-DD`) : fait foi et détermine le répertoire
  `fiches/YYYY-MM/` (le lint vérifie la cohérence Date ↔ répertoire).
- **GrapheDeConnaissance** : triples (8 colonnes) + entités (5 colonnes).
  ⚠️ **Avant de créer, linter ou modifier une fiche, lire
  [`docs/reference/ontologie-kg.md`](docs/reference/ontologie-kg.md)** — registre
  fermé des 30 prédicats, types d'entités/épistémiques, désambiguïsation, format
  des fiches de skill. Le lint valide le mécanique ; la référence porte la
  sémantique.

**Langue** : tout en français (résumés, pense-bêtes, ton, keywords, types et
prédicats du graphe). Restent en langue d'origine : Titre Article, URL, noms
d'auteurs, noms d'entités.

## Frontmatter éditorial (registre fermé)

Chaque fiche porte un frontmatter YAML validé par le lint. **Clés autorisées
uniquement** (toute autre clé = erreur) :

| Groupe | Clés |
|--------|------|
| Éditorial | `themes` (liste de slugs de `scripts/themes.tsv`), `source` (nom court) |
| Promotion cabinet | `cabinet_promotion_candidate`, `proposed_class`, `proposed_capability`, `notes` |
| Skill | `fiche_type`, `skill_source`, `skill_author` |

`themes` : uniquement des slugs présents dans `scripts/themes.tsv` (ajouter un
thème = ajouter une ligne à ce fichier). Grammaire frontmatter supportée :
scalaires (quotes retirées), listes flow `[a, b]`, listes bloc `- a`, booléens.
Toute autre construction (map imbriquée, `|` multiligne) est rejetée par le lint.

## Workflow d'ajout d'une fiche

1. Extraire l'article ; sauver le brut dans `raw-data/id.md`.
2. Créer `fiches/YYYY-MM/id.md` : 10 sections + frontmatter (`themes`, `source`).
3. `python3 scripts/lint_fiches.py fiches/YYYY-MM/id.md` (gate Bronze).
4. Régénérer les artefacts :
   `python3 scripts/build_index.py` puis `python3 scripts/build_knowledge_base.py`.
5. `python3 scripts/check_coherence.py` (doit finir exit 0 ; traiter le rapport
   de quasi-doublons via `scripts/entity_aliases.tsv` si besoin).
6. **Commit unique** : la fiche + `index.md` + `catalogue.tsv` + `kb/` +
   `knowledge-base.md` (+ `README.md` si stats changées). **Jamais de lien
   pendant** (fiche non committée référencée par un artefact).

**Ne jamais stager** : `.DS_Store`, `.obsidian/`, `docs/` (sauf
`docs/reference/`), `gold/`, `raw-data/`.

## Workflow de récupération (grep-first)

1. `python3 scripts/check_coherence.py --catalogue-only` — si `STALE`, régénérer
   d'abord.
2. Grep `catalogue.tsv` (colonnes : id, date, titre, auteurs, source, themes,
   keywords, veille_courte, flags) et/ou `kb/_index-*.md`. Corpus **bilingue** :
   toujours `grep -i`, essayer variante accentuée ET désaccentuée, terme FR ET EN.
3. Lire les fiches ciblées (`fiches/…`) ou les pages `kb/Entité.md`.

## Workflow d'édition / production en lot

- **Édition** : l'identifiant et le chemin d'une fiche sont **gelés après
  commit** (traçabilité `fiche_id`). Le contenu est éditable → **re-run des
  générateurs** (index + KB) après édition. Changer la date de publication =
  déplacer la fiche via script, jamais à la main.
- **Lot** (agents parallèles, 8-12 fiches) : voir
  [`docs/reference/workflow-batch.md`](docs/reference/workflow-batch.md). Règle
  cardinale : **les artefacts générés ne se mergent jamais — en cas de conflit
  git, on régénère.**

## Gestion des données brutes (raw-data)

Pour chaque fiche, archiver le brut de l'URL dans `raw-data/id.md`
(`curl -sL URL | lynx -dump -stdin -nolist > raw-data/id.md`, ou
`scripts/download_raw_data.py`). Répertoire **gitignoré** (~100-500 Ko/article,
absent d'un clone frais — doctor ne bloque jamais dessus).

## Frontmatter de promotion cabinet (v3)

Une fiche candidate à promotion vers le référentiel transverse (ATransverse)
porte `cabinet_promotion_candidate: true` + `proposed_class`
(`Concept | Pattern | Framework | BenchmarkDatapoint`) + `proposed_capability`
+ `notes`. Optionnel. **Anti-pattern** : modifier l'identifiant après marquage
(casse la traçabilité `fiche_id` côté transverse).

⚠️ Le skip du frontmatter dans le parsing (`scripts/fiche_lib.py`, consommé par
lint et build) est **à ne pas régresser** — tests
`scripts/tests/test_frontmatter_compat.py` + `test_fiche_lib.py`.

## Architecture médaillon

Le médaillon est **logique** : aucun répertoire n'est renommé (ATransverse3
consomme ce dépôt en lisant `fiches/` par chemin ; il ne parse pas le format
d'`index.md`).

| Étage | Répertoire(s) | Versionné | Gate |
|-------|---------------|-----------|------|
| Raw | `raw-data/` | Non | — |
| Bronze | `fiches/` | Oui | `scripts/lint_fiches.py` (bloquant) |
| Silver | `kb/`, `knowledge-base.md`, `catalogue.tsv`, `index.md`, `kb-*.md` | Oui | `build_index.py` + `build_knowledge_base.py` ; `check_coherence.py` (doctor) |
| Gold | `gold/` | Non | checklist prompts `gold/prompts/` |

**Exception documentée** : `docs/reference/` est **versionné** (contrairement aux
autres sous-dossiers `docs/`, gitignorés) — il héberge les références chargées à
la demande. Ne pas y committer de livrable ni de contenu NDA.

### Anti-patterns

- Éditer `index.md`, `catalogue.tsv`, `kb/` ou `knowledge-base.md` à la main :
  ce sont des artefacts générés (fonction pure des fiches).
- Renommer les répertoires-étages (`raw-data/`, `fiches/`, `kb/`).
- Committer un livrable dans `docs/` (`gold/` est la seule destination).
- Versionner `gold/` (dépôt public ; HTML inlinent le design system exclu).

### Tests

Suite complète : `python3 -m unittest discover -s scripts/tests -t scripts/tests -p "test_*.py"`
(à conserver verte).
