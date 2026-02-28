---
title: Obsidian wikilinks with aliases broken by unescaped pipe characters in markdown tables
date: 2026-02-28
category: integration-issues
tags:
  - obsidian
  - wikilinks
  - markdown-rendering
  - knowledge-base-generation
  - python-script
component: scripts/build_knowledge_base.py
severity: high
symptoms:
  - Wikilinks avec aliases (ex `[[kb/Claude-Code|Claude Code]]`) non cliquables dans Obsidian
  - Liens dans le tableau "Entites les plus connectees" du dashboard rendus cassés
  - Liens dans les listes a puces echouent a parser correctement
  - Caractère pipe `|` mal interprete comme separateur de colonne markdown
root_cause: Caractère pipe dans les wikilinks non échappe comme `\|`, causant le parser Obsidian a le traiter comme syntaxe de tableau au lieu de separateur d'alias wikilink
resolution_time: 15 minutes
---

# Obsidian wikilinks non cliquables — pipe non échappé

## Symptômes

- Les wikilinks avec alias `[[kb/Claude-Code|Claude Code]]` s'affichent en texte brut dans Obsidian au lieu de liens cliquables
- Le tableau du dashboard "Entités les plus connectées" éclate les wikilinks en colonnes supplémentaires
- Les liens de navigation dans les listes à puces ne fonctionnent pas non plus

## Investigation

1. **Identification du symptôme** : Les wikilinks avec alias `[[path|display text]]` apparaissent en texte brut au lieu de liens cliquables
2. **Analyse du scope** : Le problème touche les cellules de tableaux markdown ET les listes à puces dans les fichiers générés
3. **Découverte du conflit de parser** : Le caractère `|` a un double usage — délimiteur de colonne markdown ET séparateur d'alias wikilink Obsidian
4. **Test du comportement Obsidian** : Confirmé qu'Obsidian priorise la syntaxe de tableau sur la syntaxe wikilink pour les pipes non échappés

## Cause racine

Le caractère `|` dans les alias de wikilinks crée une ambiguïté quand il est placé dans des cellules de tableau markdown.

Le parser Obsidian traite les délimiteurs de tableau **avant** de résoudre la syntaxe wikilink. Quand il rencontre :
```
| [[kb/entity|display name]] |
```
Il interprète les deux pipes comme séparateurs de tableau, découpant le wikilink en morceaux :
- `[[kb/entity` — reconnu comme wikilink incomplet
- `display name` — traité comme contenu de cellule
- `]]` — crochets orphelins

## Solution

Échapper le pipe comme `\|` dans **toutes** les fonctions de génération de wikilinks du script Python.

### 1. Fonction `entity_wikilink()`
```python
# Avant
return f"[[kb/{filename}|{name}]]"

# Après
return f"[[kb/{filename}\\|{name}]]"
```

### 2. Fonction `fiche_wikilink()`
```python
# Avant
return f"[[{path}|{alias}]]"

# Après
return f"[[{path}\\|{alias}]]"
```

### 3. Liens de navigation hardcodés dans `generate_dashboard()`
```python
# Avant
"- [[kb/_index-entites|Index alphabétique]]"
"- [[kb/_index-type-PERSONNE|PERSONNE]] (156)"

# Après
"- [[kb/_index-entites\\|Index alphabétique]]"
"- [[kb/_index-type-PERSONNE\\|PERSONNE]] (156)"
```

### Note Python

Dans les f-strings Python, `\\|` produit la chaîne littérale `\|` dans le fichier de sortie. C'est la séquence d'échappement standard d'Obsidian pour les pipes dans les wikilinks.

## Vérification

1. Lancer `python3 scripts/build_knowledge_base.py`
2. Vérifier que les wikilinks contiennent `\|` : `grep -c '\\\\|' knowledge-base.md`
3. Ouvrir dans Obsidian — tous les liens doivent être cliquables (bleus/soulignés)
4. Cliquer un lien dans le tableau du dashboard — doit ouvrir la page entité
5. Cliquer un lien de navigation — doit ouvrir l'index correspondant

## Prévention

### Règles

- **Toujours** échapper le pipe comme `\|` dans les wikilinks Obsidian générés par du code, quel que soit le contexte (tableau ou liste)
- Centraliser la génération de wikilinks dans des fonctions dédiées (`entity_wikilink()`, `fiche_wikilink()`) pour éviter les oublis
- Ne pas appliquer un double échappement — vérifier que `\|` n'est pas ré-échappé en `\\|`

### Test automatisé suggéré

```bash
# Vérifie qu'aucun wikilink non échappé n'existe dans les fichiers générés
# Un pipe non échappé dans un wikilink = [[...| sans backslash avant
grep -Pn '\[\[[^\]]*(?<!\\)\|' knowledge-base.md kb/*.md && echo "FAIL: pipes non échappés" || echo "OK"
```

### Autres pièges Obsidian à surveiller

- `#` dans les ancres d'entités mineures : doit correspondre exactement au heading
- Caractères spéciaux dans les noms de fichiers (`/`, `:`, `*`, `?`) — nettoyés par `entity_to_filename()`
- Les alias très longs peuvent être tronqués dans certaines vues Obsidian

## Fichiers modifiés

- `scripts/build_knowledge_base.py` — fonctions `entity_wikilink()`, `fiche_wikilink()`, `generate_dashboard()`

## Références

- [Obsidian Wiki - Internal links](https://help.obsidian.md/Linking+notes+and+files/Internal+links)
- Plans associés : `docs/plans/2026-02-28-feat-knowledge-base-consolidee-graphe-connaissance-plan.md`
