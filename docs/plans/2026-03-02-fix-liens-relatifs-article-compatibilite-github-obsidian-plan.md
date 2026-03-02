---
title: "fix: Liens relatifs article 404 sur GitHub — compatibilité GitHub/Obsidian"
type: fix
date: 2026-03-02
---

# fix: Liens relatifs article 404 sur GitHub — compatibilité GitHub/Obsidian

## Overview

Les liens dans `docs/articles/context-engineering/article.md` retournent des 404 sur GitHub. Le problème est un bug de profondeur relative : les liens utilisent `../fiches/...` alors que l'article est 3 niveaux sous la racine du repo.

## Diagnostic

### Le bug

L'article est situé à `docs/articles/context-engineering/article.md`. Les liens utilisent `../fiches/2026-02/filename.md`.

```
Chemin résolu par GitHub :
  docs/articles/context-engineering/../fiches/...
  = docs/articles/fiches/...     ← N'EXISTE PAS → 404
```

Le `../` ne remonte qu'un niveau (vers `docs/articles/`), mais `fiches/` est à la racine du repo, soit 3 niveaux au-dessus. Le chemin correct serait `../../../fiches/...`.

### Pourquoi ça "marche" dans Obsidian

Obsidian utilise par défaut un mode de résolution par **plus court chemin** (shortest path matching). Quand il rencontre `../fiches/2026-02/filename.md`, il ignore le chemin relatif incorrect et résout par recherche du nom de fichier dans tout le vault. C'est un comportement spécifique à Obsidian — GitHub résout le chemin strictement.

### Deux systèmes de liens dans le repo

| Contexte | Format | GitHub | Obsidian |
|----------|--------|--------|----------|
| `index.md` | `[text](fiches/YYYY-MM/file.md)` | Fonctionne | Fonctionne |
| `kb/*.md`, `kb-*.md` | `[[fiches/path\|texte]]` (wikilinks) | Ne rend pas (texte brut) | Fonctionne |
| `docs/articles/...` | `[text](../fiches/...)` (profondeur fausse) | 404 | Fonctionne (fallback filename) |

## Solution proposée

### Approche retenue : corriger la profondeur relative

Remplacer `../fiches/` par `../../../fiches/` dans les 4 fichiers du dossier article. C'est le format standard markdown avec chemin relatif correct + extension `.md`, qui fonctionne sur **les deux plateformes**.

```markdown
# Avant (cassé sur GitHub)
[texte](../fiches/2026-02/filename.md)

# Après (fonctionne partout)
[texte](../../../fiches/2026-02/filename.md)
```

### Pourquoi cette approche

| Approche | GitHub | Obsidian | Effort | Retenue |
|----------|--------|----------|--------|---------|
| Corriger `../` → `../../../` | Fonctionne | Fonctionne | Faible | **Oui** |
| Convertir en wikilinks `[[...]]` | Ne rend pas | Fonctionne | Moyen | Non |
| Liens absolus GitHub (`/fiches/...`) | Fonctionne | Ne fonctionne pas | Faible | Non |

Le format `[text](../../../fiches/YYYY-MM/file.md)` est le seul qui fonctionne nativement sur GitHub ET Obsidian sans plugin.

## Fichiers à modifier

1. `docs/articles/context-engineering/article.md` — tous les liens `../fiches/` → `../../../fiches/`
2. `docs/articles/context-engineering/presentation-15-slides.md` — idem si liens présents
3. `docs/articles/context-engineering/presentation-20-slides.md` — idem si liens présents
4. `docs/articles/context-engineering/plan-presentation.md` — idem si liens présents

## Acceptance Criteria

- [ ] Tous les liens `../fiches/` remplacés par `../../../fiches/` dans les 4 fichiers
- [ ] Les liens fonctionnent sur GitHub (pas de 404)
- [ ] Les liens fonctionnent dans Obsidian (navigation correcte)
- [ ] Aucune autre modification de contenu

## Recommandation pour le futur

Documenter dans CLAUDE.md la convention de liens pour les fichiers sous `docs/articles/` :

> Les liens dans les articles sous `docs/articles/` doivent utiliser le format markdown standard avec le chemin relatif correct vers la racine : `[texte](../../../fiches/YYYY-MM/identifiant.md)`.

Optionnel : configurer Obsidian pour générer des liens relatifs corrects (Settings > Files and Links > New link format > "Relative path to file" + Use Wikilinks > OFF pour les fichiers articles).
