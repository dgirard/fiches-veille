---
title: Index et statistiques générés + catalogue machine pour la récupération grep-first
date: 2026-07-06
category: architecture
tags:
  - index-generation
  - catalogue
  - token-efficiency
  - grep-first
  - frontmatter
  - determinisme
component: scripts/build_index.py
severity: high
problem_type: architecture_pattern
applies_when:
  - On maintient un index markdown à la main qui grossit avec le corpus
  - Le coût en tokens de mise à jour d'un index ou de recherche devient limitant
  - Une IA doit produire des fiches et retrouver de l'information à moindre coût
symptoms:
  - "index.md rédigé à la main : chaque fiche décrite 2 fois (datée + thématique)"
  - "ligne « Principaux auteurs » de 5663 caractères ré-émise à chaque incrément"
  - "index.md ~49K tokens : illisible en un appel, ~150K projetés à 1000 fiches"
root_cause: >
  Métadonnées éditoriales (thèmes, source, stats) stockées uniquement dans un
  index markdown rédigé, donc non dérivables et coûteuses à maintenir par une IA.
---

# Index généré + catalogue machine (scalabilité 327 → 1000 fiches)

## Problème

`index.md` était rédigé à la main : double description de chaque fiche (entrée
datée 2-4K chars + entrée thématique), statistiques agrégées sur une ligne unique
de 5 663 caractères, ~49K tokens au total. Chaque ajout de fiche coûtait 8-15K
tokens hors rédaction de la fiche ; à 1000 fiches l'index devenait inéditable.

## Investigation

Les métadonnées éditoriales (thèmes, source) n'existaient que dans la prose de
l'index — non dérivables des 10 sections d'une fiche. Il fallait donc les
**colocaliser dans la fiche** (frontmatter) pour rendre l'index dérivable.

## Solution

- **Frontmatter éditorial** (`themes` = slugs de `scripts/themes.tsv`, `source`),
  validé par un registre fermé dans le lint. Migration one-shot extrayant thèmes
  et source de l'`index.md` historique (`migrate_editorial_frontmatter.py`).
- **`build_index.py`** génère de façon **déterministe** (regénération identique
  octet pour octet) : `index.md` (vue humaine : mois + thématiques + stats en
  liste), `catalogue.tsv` (vue machine, 1 ligne/fiche, 9 colonnes + manifest),
  et le bloc stats de `README.md` entre marqueurs. Aucune prose produite par IA.
- **Récupération grep-first** : `catalogue.tsv` est le point d'entrée. Coût mesuré
  **~197 tokens/candidate** (grep d'une ligne) vs ~49K tokens (lecture d'index.md).
- **Manifest de fraîcheur** (sha256 de tous les champs consommés) + `doctor`
  (`check_coherence.py`) : détecte un catalogue/KB périmé, exit ≠ 0 bloquant.

## Résultats mesurés (2026-07-06, 327 fiches)

| Métrique | Avant | Après |
|----------|-------|-------|
| Coût d'ajout (hors fiche) | ~8-15K tokens | frontmatter ~60 octets + scripts |
| Identification d'une fiche | ~49K tokens (index.md) | ~197 tokens/candidate (catalogue) |
| CLAUDE.md / session | ~6600 tokens | ~1864 tokens |
| Rappel (5 requêtes réelles) | — | 5/5 |

## Prévention

- Ne **jamais** éditer `index.md`, `catalogue.tsv`, `kb/`, `knowledge-base.md` à
  la main — ce sont des fonctions pures des fiches. Régénérer, ne jamais merger.
- Toute métadonnée éditoriale nouvelle passe par une **clé de frontmatter du
  registre fermé** (lint), jamais par de la prose dans un artefact généré.
- Garder les générateurs **déterministes** (champs dérivés = troncatures
  mécaniques) pour des diffs git propres. Voir aussi
  [[missing-knowledge-graph-sections]] et [[alias-entites-et-bornage-kb]].
