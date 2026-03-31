---
title: "feat: Specification document for knowledge base construction"
type: feat
date: 2026-03-29
---

# feat: Specification document for knowledge base construction

## Overview

Creer un fichier de specifications documentant la construction de la knowledge base (KB) du projet de veille. Ce document servira de reference pour les mainteneurs du script `build_knowledge_base.py`, les contributeurs futurs, et les agents IA qui generent les fiches.

## Problem Statement / Motivation

Le pipeline de construction de la KB est implemente dans un script Python de 770 lignes (`scripts/build_knowledge_base.py`) sans documentation technique formelle. Les regles de deduplication, le format de sortie, le contrat d'interface avec CLAUDE.md, et les limitations connues ne sont documentes nulle part de maniere consolidee. Cela rend le script opaque pour les nouveaux contributeurs et fragile face aux changements de format.

Un bug concret illustre le probleme : 5 fiches de mars 2026 utilisent des en-tetes sans accents ("Predicat" au lieu de "Predicat") causant 109 triples avec predicats vides dans la KB, sans aucun avertissement.

## Proposed Solution

Creer un fichier `docs/specs/knowledge-base-construction.md` structuree en 7 sections couvrant l'ensemble du pipeline.

## Structure du document de specifications

### Section 1 : Contrat d'interface (Input Format Contract)

Le coeur de la spec. Definir explicitement les en-tetes attendus par le script :

**Triples — 8 colonnes exactes :**
```
| Sujet | Type Sujet | Predicat | Objet | Type Objet | Confiance | Temporalite | Source |
```

**Entites — 5 colonnes exactes :**
```
| Entite | Type | Attribut | Valeur | Action |
```

**Types d'entites canoniques** (depuis CLAUDE.md) : PERSONNE, ORGANISATION, TECHNOLOGIE, CONCEPT, METHODOLOGIE, EVENEMENT, LIEU

- Documenter que DOCUMENT existe dans 3 fiches comme extension non-canonique
- Documenter que la colonne Action (AJOUT, MISE_A_JOUR, INVALIDATION) est definie dans CLAUDE.md mais ignoree par le script
- Documenter le seuil de confiance : CLAUDE.md prescrit >= 0.70, le script n'applique aucun filtrage

### Section 2 : Pipeline de traitement

Walkthrough etape par etape avec noms de fonctions :

1. **Decouverte** : `fiches_dir.rglob("*.md")` — scan recursif de `fiches/`
2. **Extraction** : `extract_graphe_connaissance()` — regex `^## GrapheDeConnaissance\s*$`
3. **Parsing** : `parse_markdown_table()` — tables pipe-delimited en listes de dicts
4. **Metadonnees** : `build_fiche_metadata()` — chemin relatif + texte `## Veille`
5. **Deduplication entites** : `deduplicate_entities()` — cle = `(name.strip().lower(), type.strip().lower())`
6. **Deduplication triples** : `deduplicate_triples()` — cle = `(sujet_norm, predicat_norm, objet_norm)`
7. **Classification** : `classify_entities()` — majeure si >= 3 triples sujet OU >= 3 fiches source
8. **Generation** : dashboard + pages entites + index + nettoyage fichiers obsoletes

### Section 3 : Regles de deduplication

**Entites :**
- Cle : `(normalize_name(entity), normalize_name(type))` ou `normalize_name = str.strip().lower()`
- Nom canonique : forme la plus frequente parmi les occurrences
- Attributs : last-write-wins par cle d'attribut (perte silencieuse si conflit)
- Accumulation des fiches source

**Triples :**
- Cle : `(sujet_norm, predicat_norm, objet_norm)`
- Confiance : valeur max parmi les doublons
- Temporalite : `DYNAMIQUE > STATIQUE > ATEMPOREL`
- Types d'entites : proviennent de l'instance a plus haute confiance

**Limitations connues :**
- Pas de fuzzy matching ("IA generative" vs "intelligence artificielle" restent separes)
- Collision d'entites possibles (deux entites differentes avec meme nom+type fusionnees silencieusement)
- Collision de noms de fichiers possibles (`entity_to_filename()` ne detecte pas les collisions)

### Section 4 : Structure de sortie

**Dashboard** : `knowledge-base.md`
- Compteurs (fiches, entites, triples)
- Liens de navigation vers les index
- Top 20 entites les plus connectees
- Top 15 predicats, distribution par type, stats de deduplication

**Repertoire `kb/`** :
- Pages entites majeures : `kb/{Nom-Entite}.md` (convention : espaces → tirets, caracteres speciaux supprimes)
- `kb/_index-entites.md` — index alphabetique
- `kb/_index-type-{TYPE}.md` — un par type d'entite
- `kb/_entites-mineures.md` — toutes les entites mineures avec ancres `{#anchor}`
- Nettoyage automatique des fichiers `.md` obsoletes dans `kb/`

**Format wikilinks (Obsidian-only)** :
- Entites majeures : `[[kb/Nom-Entite\|Nom Entite]]`
- Entites mineures : `[[kb/_entites-mineures#anchor\|Nom]]`
- Fiches : `[[fiches/YYYY-MM/id\|texte veille]]`
- Le pipe est echappe `\|` pour compatibilite avec les tableaux markdown Obsidian
- Non compatible GitHub/MkDocs

### Section 5 : Limitations connues et bugs

| Probleme | Impact | Cause | Piste de correction |
|----------|--------|-------|---------------------|
| 109 triples avec predicat vide | 4.1% des triples, stats faussees | 5 fiches mars 2026 avec "Predicat" sans accent vs script attendant "Predicat" | Corriger les 5 fiches OU accepter les deux variantes dans le script |
| Normalisation naive | Entites semantiquement identiques non fusionnees | `strip().lower()` uniquement | Ajouter fuzzy matching ou synonymes |
| Pas de filtrage confiance | Triples basse confiance incluses | Script n'applique pas seuil CLAUDE.md | Ajouter filtre >= 0.70 |
| Colonne Action ignoree | MISE_A_JOUR et INVALIDATION sans effet | Non implementee dans le script | Implementer ou retirer de CLAUDE.md |
| Type DOCUMENT non-canonique | 3 entites hors vocabulaire CLAUDE.md | Fiches avec type ad hoc | Formaliser ou corriger |
| Attributs last-write-wins | Perte silencieuse d'information | Pas de multi-valeur ni detection conflit | Ajouter detection ou multi-valeur |
| Pas de build incremental | Rebuild complet a chaque execution | Pas de cache/change detection | Acceptable a 211 fiches |
| Pas de rapport d'erreurs | Fiches malformees ignorees silencieusement | Aucun warning emis | Ajouter rapport de parsing |

### Section 6 : Parametres et configuration

| Parametre | Valeur | Emplacement |
|-----------|--------|-------------|
| Seuil majeur/mineur | 3 (triples sujet OU fiches) | `classify_entities()` |
| Top entites dashboard | 20 | `generate_dashboard()` |
| Top predicats stats | 15 | `generate_dashboard()` |
| Repertoire source | `../fiches/` relatif au script | `main()` |
| Repertoire sortie | `../` relatif au script | `main()` |

Aucun argument CLI, aucun fichier de config, aucune variable d'environnement.

### Section 7 : Scripts auxiliaires

- `scripts/list_missing_kg.sh` — Identifie les fiches sans `## GrapheDeConnaissance`
- `scripts/check_missing.py` — Compare slugs URL vs fiches existantes
- `scripts/fetch_urls.py` + `scripts/download_raw_data.py` — Pipeline amont raw-data

## Acceptance Criteria

- [x] Fichier `docs/specs/knowledge-base-construction.md` cree avec les 7 sections
- [x] Contrat d'interface explicite : en-tetes exacts attendus, types canoniques
- [x] Pipeline documente etape par etape avec noms de fonctions
- [x] Regles de deduplication documentees (cle, normalisation, strategie de merge)
- [x] Structure de sortie complete (dashboard, kb/, conventions de nommage)
- [x] Toutes les limitations connues listees avec cause et piste de correction
- [x] Bug des 109 predicats vides documente avec root cause precise
- [x] Metriques actuelles incluses (211 fiches, 1376 entites, 2630 triples)

## Dependencies & Risks

- **Dependance** : lecture complete de `scripts/build_knowledge_base.py` (770 lignes)
- **Risque faible** : les metriques citees dans la spec deviendront obsoletes a chaque rebuild — mentionner la date de reference
- **Pas de risque technique** : tache de documentation pure, aucun code modifie

## References & Research

### Internal References
- Script principal : `scripts/build_knowledge_base.py`
- Format d'entree : `CLAUDE.md` section "GrapheDeConnaissance — Format detaille"
- Plan initial KB : `docs/plans/2026-02-28-feat-knowledge-base-consolidee-graphe-connaissance-plan.md`
- Solution backfill KG : `docs/solutions/data-completeness/missing-knowledge-graph-sections.md`
- Solution wikilinks : `docs/solutions/integration-issues/obsidian-wikilinks-pipe-escaping.md`
- Script auxiliaire : `scripts/list_missing_kg.sh`
