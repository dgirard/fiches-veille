# Spécification : Construction de la Knowledge Base

> Document de référence pour le pipeline de construction de la Knowledge Base (KB) du projet de veille technologique.
> Dernière mise à jour : 2026-03-29 | Métriques de référence : 211 fiches, 1376 entités, 2630 triples.

---

## Table des matières

1. [Contrat d'interface (Input Format Contract)](#1-contrat-dinterface)
2. [Pipeline de traitement](#2-pipeline-de-traitement)
3. [Règles de déduplication](#3-règles-de-déduplication)
4. [Structure de sortie](#4-structure-de-sortie)
5. [Limitations connues et bugs](#5-limitations-connues-et-bugs)
6. [Paramètres et configuration](#6-paramètres-et-configuration)
7. [Scripts auxiliaires](#7-scripts-auxiliaires)

---

## 1. Contrat d'interface

Le script `scripts/build_knowledge_base.py` consomme les sections `## GrapheDeConnaissance` présentes dans chaque fiche de veille sous `fiches/`. Le format de ces sections est défini dans `CLAUDE.md`.

### En-têtes attendus — Triples (8 colonnes)

Le script accède aux colonnes par leur nom exact (avec accents). Toute variation orthographique provoque des valeurs vides.

```
| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
```

| Colonne | Accédée via | Type attendu | Notes |
|---------|------------|-------------|-------|
| Sujet | `triple.get("Sujet", "")` | Texte libre | Nom d'entité, langue d'origine |
| Type Sujet | `triple.get("Type Sujet", "")` | Enum (voir types ci-dessous) | |
| Prédicat | `triple.get("Prédicat", "")` | Verbe français court | **Sensible aux accents** — `Predicat` sans accent → vide |
| Objet | `triple.get("Objet", "")` | Texte libre | |
| Type Objet | `triple.get("Type Objet", "")` | Enum | |
| Confiance | `float(triple.get("Confiance", "0"))` | Float 0.0–1.0 | `ValueError` → 0.0 |
| Temporalité | `triple.get("Temporalité", "")` | STATIQUE / DYNAMIQUE / ATEMPOREL | **Sensible aux accents** |
| Source | `triple.get("Source", "")` | déclaré_article / inféré / généré_assistant | |

### En-têtes attendus — Entités (5 colonnes)

```
| Entité | Type | Attribut | Valeur | Action |
```

| Colonne | Accédée via | Type attendu | Notes |
|---------|------------|-------------|-------|
| Entité | `entity.get("Entité", "")` | Texte libre | Nom d'entité |
| Type | `entity.get("Type", "")` | Enum | |
| Attribut | `entity.get("Attribut", "")` | Texte libre | Clé d'attribut |
| Valeur | `entity.get("Valeur", "")` | Texte libre | Valeur de l'attribut |
| Action | `entity.get("Action", "")` | AJOUT / MISE_A_JOUR / INVALIDATION | **Ignorée par le script** |

### Types d'entités canoniques

Définis dans `CLAUDE.md`, hardcodés dans le script (lignes 401-402, 534-535, 728-729) :

| Type | Description |
|------|-------------|
| PERSONNE | Individu nommé |
| ORGANISATION | Entreprise, labo, institution |
| TECHNOLOGIE | Outil, framework, plateforme, langage |
| CONCEPT | Idée, principe, pattern |
| METHODOLOGIE | Approche, workflow, pratique |
| EVENEMENT | Publication, annonce, incident |
| LIEU | Localisation géographique |

**Extension observée** : le type `DOCUMENT` existe dans 3 fiches. Il n'est pas dans `CLAUDE.md` mais est géré par le script via un fallback `sorted()` qui l'ajoute en fin de liste.

### Valeurs de temporalité

| Valeur | Priorité (résolution de conflit) |
|--------|----------------------------------|
| DYNAMIQUE | 1 (plus haute) |
| STATIQUE | 2 |
| ATEMPOREL | 3 (plus basse) |

### Seuil de confiance

- **CLAUDE.md** prescrit un minimum de 0.70 à la création des fiches.
- **Le script** n'applique aucun filtrage de confiance. Tous les triples sont inclus dans la KB, y compris ceux à confiance 0.0.

### Sections markdown attendues

Le script cherche ces sections par regex sur le contenu de chaque fiche :

```
^## GrapheDeConnaissance\s*$     → Identifie le début de la section KG
^### Triples\s*$                 → Sous-section des triples
^### Entités\s*$                 → Sous-section des entités
```

Si `## GrapheDeConnaissance` est absent, la fiche est ignorée silencieusement (retourne listes vides).

---

## 2. Pipeline de traitement

Script : `scripts/build_knowledge_base.py` (770 lignes, zéro dépendance externe).

Exécution : `python3 scripts/build_knowledge_base.py` depuis la racine du projet.

### Étapes séquentielles

```
fiches/*.md
    │
    ▼
┌───────────────────────────────────────────────┐
│ 1. Découverte                                  │
│    fiches_dir.rglob("*.md")                   │
│    Scan récursif de fiches/                    │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ 2. Extraction par fiche                        │
│    extract_graphe_connaissance(filepath)       │
│    → regex ^## GrapheDeConnaissance            │
│    → regex ^### Triples / ^### Entités         │
│    → parse_markdown_table() sur chaque section │
│    Retourne: (triples[], entités[], fiche_id)  │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ 3. Métadonnées fiches                          │
│    build_fiche_metadata(fiches_dir)            │
│    → fiche_id → chemin relatif (sans .md)      │
│    → fiche_id → texte sous ## Veille           │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ 4. Déduplication entités                       │
│    deduplicate_entities(all_entities)          │
│    Clé: (name.strip().lower(), type.lower())  │
│    Merge: nom le + fréquent, attrs last-write  │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ 5. Déduplication triples                       │
│    deduplicate_triples(all_triples)           │
│    Clé: (sujet_norm, prédicat_norm, objet_norm)│
│    Merge: confiance max, temporalité max       │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ 6. Classification entités                      │
│    classify_entities(entities, triples, threshold=3) │
│    Majeure: ≥3 triples sujet OU ≥3 fiches     │
│    Mineure: tout le reste                      │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ 7. Génération fichiers                         │
│    → knowledge-base.md (dashboard)             │
│    → kb/{Entité}.md (pages majeures)           │
│    → kb/_index-*.md (index)                    │
│    → kb/_entites-mineures.md                   │
│    + Nettoyage fichiers .md obsolètes dans kb/ │
└───────────────────────────────────────────────┘
```

### Détail des fonctions

| Fonction | Entrée | Sortie | Rôle |
|----------|--------|--------|------|
| `normalize_name(name)` | str | str | `name.strip().lower()` |
| `parse_markdown_table(lines)` | list[str] | list[dict] | Parse tableau pipe-delimited, gère colonnes manquantes/excédentaires |
| `extract_graphe_connaissance(filepath)` | str (chemin) | (triples, entités, fiche_id) | Extraction regex + parsing |
| `build_fiche_metadata(fiches_dir)` | Path | (fiche_paths, fiche_veilles) | Chemin relatif + texte Veille |
| `deduplicate_entities(all_entities)` | list[(dict, str)] | list[dict] | Déduplication par nom+type |
| `deduplicate_triples(all_triples)` | list[(dict, str)] | list[dict] | Déduplication par SPO |
| `classify_entities(entities, triples, threshold)` | lists, int | (major_set, minor_set) | Classification majeure/mineure |
| `compute_incoming_triples(triples)` | list[dict] | dict[str, list] | Index triples entrants par objet |
| `entity_to_filename(name)` | str | str | Nom → nom de fichier (espaces→tirets, speciaux supprimés) |
| `entity_wikilink(name, major_set, entity_filenames)` | str, set, dict | str | Génère wikilink Obsidian |
| `fiche_wikilink(fiche_id, fiche_paths, fiche_veilles)` | str, dict, dict | str | Génère wikilink vers fiche |
| `generate_entity_page(...)` | entity, triples... | str | Contenu page entité majeure |
| `generate_minor_entities_page(...)` | entities, triples... | str | Page entités mineures |
| `generate_type_index(etype, ...)` | str, entities... | str | Index par type |
| `generate_alpha_index(entities, ...)` | entities... | str | Index alphabétique |
| `generate_dashboard(...)` | all stats... | str | Dashboard knowledge-base.md |
| `write_output_files(base_dir, files)` | Path, dict | None | Écriture + nettoyage obsolètes |

---

## 3. Règles de déduplication

### Déduplication des entités

**Clé de déduplication** : `(normalize_name(entité), normalize_name(type))`

Où `normalize_name = str.strip().lower()`

**Stratégie de merge** :

| Champ | Stratégie | Risque |
|-------|-----------|--------|
| Nom canonique | Forme la plus fréquente parmi les occurrences | Aucun |
| Type canonique | Forme la plus fréquente | Aucun |
| Attributs | Dictionnaire fusionné, **last-write-wins** par clé | Perte silencieuse si deux fiches définissent des valeurs différentes pour le même attribut |
| Fiches source | Union de tous les fiche_id | Aucun |
| Occurrences | Nombre total d'apparitions dans les fiches | Aucun |

**Exemple** :
- Fiche A : `Entité=Claude Code, Type=TECHNOLOGIE, Attribut=catégorie, Valeur=Agent CLI`
- Fiche B : `Entité=claude code, Type=Technologie, Attribut=catégorie, Valeur=Agent de codage`
- Résultat : `name=Claude Code` (plus fréquent), `type=TECHNOLOGIE`, `catégorie=Agent de codage` (dernière valeur)

### Déduplication des triples

**Clé de déduplication** : `(normalize_name(sujet), normalize_name(prédicat), normalize_name(objet))`

**Stratégie de merge** :

| Champ | Stratégie |
|-------|-----------|
| Confiance | Valeur maximale parmi les doublons |
| Temporalité | Priorité : DYNAMIQUE > STATIQUE > ATEMPOREL |
| Types (sujet/objet) | Proviennent de l'instance à plus haute confiance |
| Sources | Union de toutes les sources |
| Fiches | Union de tous les fiche_id |

### Ce que la normalisation attrape et manque

| Cas | Fusionné ? |
|-----|-----------|
| `Claude Code` / `claude code` | Oui |
| `IA générative` / `IA GÉNÉRATIVE` | Oui |
| `IA générative` / `intelligence artificielle` | Non — synonymes non gérés |
| `agent IA` / `agents IA` | Non — pas de stemming |
| `Google` / `Google Cloud` | Non — noms différents |

---

## 4. Structure de sortie

### Fichiers générés

```
veille/
├── knowledge-base.md                    # Dashboard principal
└── kb/
    ├── {Nom-Entité}.md                  # Pages entités majeures (~211 fichiers)
    ├── _index-entites.md                # Index alphabétique complet
    ├── _index-type-PERSONNE.md          # Index par type (un par type)
    ├── _index-type-ORGANISATION.md
    ├── _index-type-TECHNOLOGIE.md
    ├── _index-type-CONCEPT.md
    ├── _index-type-METHODOLOGIE.md
    ├── _index-type-EVENEMENT.md
    ├── _index-type-LIEU.md
    ├── _index-type-DOCUMENT.md          # Extension non-canonique
    └── _entites-mineures.md             # Toutes les entités mineures
```

### Convention de nommage des fichiers entités

Fonction `entity_to_filename(name)` :

1. Remplace les caractères `/\:*?"<>|` par des tirets
2. Remplace les espaces par des tirets
3. Collapse les tirets multiples en un seul
4. Supprime les tirets en début et fin

**Exemples** : `Claude Code` → `Claude-Code`, `AG2R LA MONDIALE` → `AG2R-LA-MONDIALE`

**Risque** : deux noms ne différant que par des caractères spéciaux produiraient le même fichier. Aucune détection de collision.

### Dashboard `knowledge-base.md`

Structure du fichier généré :

1. **En-tête** : compteurs (fiches, entités, triples) + date de génération
2. **Navigation** : wikilinks vers tous les index (alphabétique, par type, mineures)
3. **Entités les plus connectées** : tableau top 20, trié par nombre total de relations (sujet + objet)
4. **Statistiques** :
   - Top 15 prédicats les plus fréquents
   - Distribution par type d'entité (nombre + pourcentage)
   - Stats de déduplication (brutes → uniques)

### Pages entités majeures `kb/{Nom}.md`

Structure de chaque page :

1. **En-tête** : `# Nom` + type + nombre de relations + nombre de fiches
2. **Attributs** : liste des attributs fusionnés
3. **Relations comme sujet** : groupées par prédicat, triées par confiance décroissante, chaque triple avec ses fiches sources en wikilinks
4. **Relations comme objet** (entrantes) : triées par confiance décroissante
5. **Fiches sources** : liste de wikilinks vers les fiches d'origine

### Page entités mineures `kb/_entites-mineures.md`

- Groupées par type d'entité
- Chaque entité a une ancre Obsidian : `### Nom {#anchor}`
- Contenu compact : attributs, relations sortantes, relations entrantes, fiches

### Format des wikilinks

**Plateforme cible : Obsidian uniquement.**

Le pipe `|` est toujours échappé en `\|` pour éviter les conflits avec les tableaux markdown.

| Contexte | Format | Exemple |
|----------|--------|---------|
| Entité majeure | `[[kb/{filename}\|{name}]]` | `[[kb/Claude-Code\|Claude Code]]` |
| Entité mineure | `[[kb/_entites-mineures#{anchor}\|{name}]]` | `[[kb/_entites-mineures#vibe-coding\|Vibe coding]]` |
| Fiche source | `[[{chemin_relatif}\|{texte_veille}]]` | `[[fiches/2026-03/wardley-llms\|Paradoxe Jevons...]]` |
| Navigation | `[[kb/_index-entites\|Index alphabétique]]` | |

**Incompatibilité** : ces wikilinks ne s'affichent pas correctement sur GitHub ou MkDocs. C'est un choix délibéré — le KB est conçu pour être consulté dans Obsidian.

### Nettoyage automatique

`write_output_files()` supprime tout fichier `.md` dans `kb/` qui n'est pas dans l'ensemble des fichiers attendus de la génération courante. Cela gère le renommage ou la suppression d'entités entre deux builds.

---

## 5. Limitations connues et bugs

### Bug : 109 triples avec prédicat vide

**Impact** : 4.1% des triples ont un prédicat vide. Le dashboard affiche `**** : 109` comme deuxième "prédicat" le plus fréquent.

**Cause racine** : 5 fiches créées en mars 2026 utilisent des en-têtes de colonnes sans accents :
- `Predicat` au lieu de `Prédicat`
- `Temporalite` au lieu de `Temporalité`

Le script accède aux valeurs via `triple.get("Prédicat", "")` (avec accent). Quand l'en-tête réel n'a pas d'accent, la clé ne matche pas et une chaîne vide est retournée.

**Fiches affectées** (identifiées dans `fiches/2026-03/`) :
- `ensarguet-beyond-brain-speed-economics-computation-2026-03-11.md`
- 4 autres fiches du même mois avec des en-têtes non accentués

**Corrections possibles** :
1. Corriger les 5 fiches pour utiliser les en-têtes accentués (correction côté données)
2. Rendre le script tolérant aux deux variantes (correction côté code)

### Tableau récapitulatif des limitations

| # | Problème | Impact | Cause | Sévérité |
|---|----------|--------|-------|----------|
| 1 | Prédicats vides (109 triples) | Stats faussées, triples mal indexés | En-têtes sans accent dans 5 fiches | Haute |
| 2 | Normalisation naïve | Entités sémantiquement identiques non fusionnées | `strip().lower()` uniquement, pas de fuzzy matching | Moyenne |
| 3 | Pas de filtrage confiance | Triples basse confiance incluses dans la KB | Script n'implémente pas le seuil >= 0.70 de CLAUDE.md | Basse |
| 4 | Colonne Action ignorée | MISE_A_JOUR et INVALIDATION sans effet | Non implémentée dans le script | Basse |
| 5 | Type DOCUMENT non canonique | 3 entités hors vocabulaire CLAUDE.md | Fiches avec type ad hoc | Basse |
| 6 | Attributs last-write-wins | Perte silencieuse d'information en cas de conflit | Pas de multi-valeur ni détection de conflit | Moyenne |
| 7 | Pas de build incrémental | Rebuild complet à chaque exécution | Pas de cache ni détection de changement | Basse (rapide à 211 fiches) |
| 8 | Pas de rapport d'erreurs | Fiches malformées ignorées silencieusement | Aucun warning émis par le script | Moyenne |
| 9 | Collision de noms de fichiers | Écrasement potentiel de pages entités | `entity_to_filename()` ne détecte pas les collisions | Basse (non observé) |
| 10 | Pas d'atomicité d'écriture | Fichiers partiels si crash mid-write | Écriture séquentielle sans transaction | Basse |

---

## 6. Paramètres et configuration

Tous les paramètres sont hardcodés. Aucun argument CLI, fichier de configuration, ou variable d'environnement.

| Paramètre | Valeur | Emplacement dans le code | Description |
|-----------|--------|--------------------------|-------------|
| Seuil majeur/mineur | `3` | `classify_entities(threshold=3)` | Nombre minimum de triples comme sujet OU de fiches source |
| Top entités dashboard | `20` | `generate_dashboard()` — slice `[:20]` | Nombre d'entités dans le tableau "plus connectées" |
| Top prédicats stats | `15` | `generate_dashboard()` — slice `[:15]` | Nombre de prédicats dans les statistiques |
| Répertoire source | `../fiches/` | `main()` — `Path(__file__).parent.parent / "fiches"` | Relatif au script |
| Répertoire de sortie | `../` | `main()` — `Path(__file__).parent.parent` | Racine du projet |
| Liste des types ordonnés | 7 types CLAUDE.md | Hardcodé 3 fois (lignes 401, 534, 728) | Ordre d'affichage des types |

### Chemins relatifs

Le script calcule ses chemins à partir de `Path(__file__).parent.parent`, ce qui suppose :
- Le script est situé dans `scripts/build_knowledge_base.py`
- Le répertoire `fiches/` est au même niveau que `scripts/`
- Les fichiers de sortie (`knowledge-base.md`, `kb/`) sont écrits à la racine du projet

Le script ne fonctionne pas depuis un répertoire de travail différent sans modification.

---

## 7. Scripts auxiliaires

### `scripts/list_missing_kg.sh`

Identifie les fiches qui ont un fichier raw-data correspondant mais pas de section `## GrapheDeConnaissance`. Utile pour détecter les fiches à compléter.

**Sortie** : `YYYY-MM|nom_fichier` trié par date décroissante.

### `scripts/check_missing.py`

Compare les slugs présents dans `scripts/urls_to_fetch.txt` avec les noms de fichiers existants dans `fiches/` pour identifier les fiches non encore créées.

### `scripts/fetch_urls.py`

Extrait toutes les URLs des fiches existantes. Première étape du pipeline de téléchargement raw-data.

### `scripts/download_raw_data.py`

Télécharge le contenu des articles sources et le convertit en markdown dans `raw-data/`. Deuxième étape du pipeline.

### Pipeline complet

```
Création fiche (manuelle ou IA)
    │
    ├── Fiche écrite dans fiches/YYYY-MM/ avec ## GrapheDeConnaissance
    ├── Raw data sauvé dans raw-data/ (gitignored)
    │
    ▼
python3 scripts/build_knowledge_base.py
    │
    ├── knowledge-base.md (dashboard)
    └── kb/ (pages entités + index)
```

---

## Références

- **Script principal** : `scripts/build_knowledge_base.py`
- **Format d'entrée** : `CLAUDE.md` — section "GrapheDeConnaissance — Format détaillé"
- **Plan initial KB** : `docs/plans/2026-02-28-feat-knowledge-base-consolidee-graphe-connaissance-plan.md`
- **Solution backfill KG** : `docs/solutions/data-completeness/missing-knowledge-graph-sections.md`
- **Solution wikilinks** : `docs/solutions/integration-issues/obsidian-wikilinks-pipe-escaping.md`
