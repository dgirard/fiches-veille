---
title: "feat: Consolider les GrapheDeConnaissance en une Knowledge Base unifiée"
type: feat
date: 2026-02-28
---

# Consolider les GrapheDeConnaissance en une Knowledge Base Markdown unifiée

## Overview

Les 128 fiches de veille contiennent chacune une section `## GrapheDeConnaissance` avec des triples (relations) et des entités. L'objectif est de consolider ces 1 660 triples et 1 337 entités en un **fichier Markdown unique**, dédupliqué et structuré, consultable dans Obsidian.

## Problem Statement

Les données du graphe de connaissance sont dispersées dans 128 fichiers individuels. Il est impossible de :
- Voir toutes les relations d'une entité (ex: tout ce qui concerne "Anthropic" à travers 23 fiches)
- Détecter les contradictions ou évolutions entre fiches
- Naviguer le graphe de connaissance comme un tout cohérent

## Proposed Solution

### Script Python d'extraction et consolidation

Un script Python (`scripts/build_knowledge_base.py`) qui :

1. **Parse** toutes les fiches contenant `## GrapheDeConnaissance`
2. **Extrait** les tableaux Triples et Entités de chaque fiche
3. **Normalise** les noms d'entités (ex: "Anthropic" vs "anthropic")
4. **Déduplique** les entités identiques, en fusionnant leurs attributs
5. **Déduplique** les triples redondants (même sujet-prédicat-objet), en conservant la confiance la plus haute
6. **Enrichit** chaque entité/triple avec la source (identifiant de la fiche d'origine)
7. **Génère** un fichier Markdown structuré : `knowledge-base.md`

### Structure du fichier de sortie `knowledge-base.md`

```markdown
# Knowledge Base — Veille Technologique

> Consolidation automatique de 128 fiches | Généré le YYYY-MM-DD
> X entités uniques | Y triples uniques

## Table des matières

- [Entités par type](#entités-par-type)
- [Index des entités](#index-des-entités)
- [Triples consolidés](#triples-consolidés)
- [Statistiques](#statistiques)

## Entités par type

### PERSONNE (N entités)

| Entité | Attributs (fusionnés) | Fiches sources |
|--------|----------------------|----------------|
| Ethan Mollick | rôle: Professeur Wharton; distinction: TIME 100 AI | fiche1, fiche2, ... |

### ORGANISATION (N entités)
### TECHNOLOGIE (N entités)
### CONCEPT (N entités)
### METHODOLOGIE (N entités)
### EVENEMENT (N entités)
### LIEU (N entités)

## Index des entités

Index alphabétique avec liens internes vers la section de chaque entité.

## Triples consolidés

### Par sujet (groupés par entité sujet)

#### Anthropic

| Prédicat | Objet | Type Objet | Confiance max | Temporalité | Sources | Fiches |
|----------|-------|-----------|---------------|-------------|---------|--------|
| emploie | Boris Cherny | PERSONNE | 0.97 | DYNAMIQUE | déclaré_article | fiche1, fiche2 |

#### Claude Code
...

## Statistiques

- Total entités uniques : X
- Total triples uniques : Y
- Entités les plus connectées : ...
- Prédicats les plus fréquents : ...
```

### Règles de déduplication

#### Entités
- **Clé d'identité** : nom normalisé (lowercase, trim) + type
- **Fusion d'attributs** : si même entité avec attributs différents → concaténer les attributs uniques
- **Conflits de type** : si même nom mais types différents → conserver les deux entrées séparées
- **Traçabilité** : chaque entité porte la liste des fiches sources

#### Triples
- **Clé d'identité** : (sujet normalisé, prédicat normalisé, objet normalisé)
- **Confiance** : conserver la confiance maximale parmi les doublons
- **Temporalité** : si conflit (STATIQUE vs DYNAMIQUE) → conserver DYNAMIQUE (le plus récent prime)
- **Source** : concaténer les sources de toutes les occurrences
- **Traçabilité** : chaque triple porte la liste des fiches sources

## Technical Approach

### Architecture

```
scripts/build_knowledge_base.py
├── parse_fiche(filepath) → (triples[], entités[])
├── normalize_entity_name(name) → str
├── deduplicate_entities(all_entities[]) → unique_entities[]
├── deduplicate_triples(all_triples[]) → unique_triples[]
├── generate_markdown(entities, triples) → str
└── main() → knowledge-base.md
```

### Parsing des tableaux Markdown

Le script doit :
1. Identifier la section `## GrapheDeConnaissance` dans chaque fiche
2. Identifier les sous-sections `### Triples` et `### Entités`
3. Parser les lignes de tableau (lignes commençant par `|`, en ignorant les en-têtes et séparateurs `|---|`)
4. Extraire les valeurs de chaque colonne

### Dépendances

- Python 3 standard (pas de bibliothèque externe requise)
- Regex pour le parsing des tableaux markdown

## Acceptance Criteria

- [x] Le script parse correctement les 128 fiches
- [x] Toutes les entités sont extraites et dédupliquées
- [x] Tous les triples sont extraits et dédupliqués
- [x] Le fichier `knowledge-base.md` est généré avec la structure décrite
- [x] Chaque entité/triple est traçable vers sa/ses fiche(s) source(s)
- [x] Le fichier est lisible dans Obsidian
- [x] Les statistiques de consolidation sont affichées (avant/après déduplication)

## Dependencies & Risks

**Risques :**
- **Variabilité du parsing** : les tableaux Markdown peuvent avoir des variations de formatage (espaces, pipes manquants)
- **Normalisation des noms** : "Claude Code" vs "claude code" vs "Claude code" — besoin d'une normalisation robuste
- **Taille du fichier** : ~1 000+ entités et triples pourrait produire un fichier volumineux (mais acceptable en Markdown)

**Mitigations :**
- Parser robuste avec gestion des cas limites
- Normalisation case-insensitive avec conservation du nom original le plus fréquent
- Sections repliables dans le Markdown si besoin

## References

- Format GrapheDeConnaissance défini dans CLAUDE.md
- 128 fiches source dans `fiches/`
- Analyse de volume : 1 660 triples, 1 337 entités, score confiance moyen 0.939
