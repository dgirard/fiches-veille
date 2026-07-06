---
title: Bornage de la KB — alias courts, homonymes multi-types et collisions de fichiers
date: 2026-07-06
category: architecture
tags:
  - knowledge-base-generation
  - wikilinks
  - entity-resolution
  - case-insensitive-filesystem
  - token-efficiency
component: scripts/build_knowledge_base.py
severity: high
problem_type: architecture_pattern
applies_when:
  - Une KB Obsidian générée grossit plus vite que le nombre de fiches
  - Des entités homonymes de types différents entrent en collision de fichiers
  - Un fichier kb/ généré heurte un fichier réservé du dépôt (CLAUDE.md, README.md)
symptoms:
  - "kb/Léon-XIV.md : 163 Ko pour 1 fiche source"
  - "kb/ croît en O(longueur Veille × triples), pas en O(fiches)"
  - "kb/Claude.md injecté comme instructions projet sur FS insensible à la casse"
  - "20 collisions de noms de fichiers case-insensitive (Cursor ORG vs TECH…)"
root_cause: >
  Alias de wikilink = paragraphe ## Veille entier (jusqu'à 6000 chars), répété à
  chaque triple ; et pages d'entités keyées par nom seul, écrasement silencieux
  des homonymes multi-types sur un système de fichiers insensible à la casse.
---

# Bornage et assainissement de la KB

## Problème

Le build KB utilisait le paragraphe `## Veille` entier comme alias de chaque
wikilink de fiche → poids en **O(longueur Veille × nombre de triples)**
(`kb/Léon-XIV.md` = 163 Ko pour 1 fiche). Les pages d'entités étaient keyées par
**nom seul** : deux entités homonymes de types différents (Cursor ORGANISATION
vs TECHNOLOGIE — désambiguïsation légitime de l'ontologie) produisaient le même
nom de fichier et s'écrasaient. Sur APFS insensible à la casse, `kb/Claude.md`
heurtait `CLAUDE.md` et était chargé comme instructions projet.

## Solution

- **Alias de wikilink = `Titre Article`** sanitisé (`|`, `[`, `]`, retours → `-`,
  préserve le grep-invariant `\|`) et **tronqué à 120 caractères**. Supprime
  l'amplification. `kb/Léon-XIV.md` : 163 Ko → 9,5 Ko ; `kb/` total : 6,9 Mo → 3,3 Mo.
- **Index de pages keyé par (nom, type)** ; `entity_wikilink` reçoit le type du
  triple pour cibler la bonne page. Les homonymes multi-types reçoivent un
  **suffixe de type** déterministe (`Cursor-organisation`, `Cursor-technologie`) —
  aucune fusion, aucun jugement, aucune donnée perdue.
- **Noms réservés** (`claude`, `readme`, `index`, `catalogue`, `knowledge-base`,
  `gemini`, `agents`) suffixés `-entite` → `kb/Claude.md` éliminé.
- **Table `entity_aliases.tsv`** (directives `FUSION` pour vrais synonymes,
  `DISTINCT` pour override de suffixe) + **erreur bloquante** sur toute collision
  résiduelle (message proposant les deux issues). Rapport de **quasi-doublons**
  imprimé à chaque build (jamais fusionnés automatiquement — arbitrage humain).
- **Manifest** (sha256 de chemin + Titre + section KG) dans `knowledge-base.md`
  → `doctor` détecte un kb/ périmé même après une simple édition de titre.

## Prévention

- La logique d'alias/lien reste **centralisée** dans `fiche_alias`,
  `entity_wikilink`, `fiche_wikilink` — ne jamais dupliquer (régression du grep
  `\|`, cf. [[obsidian-wikilinks-pipe-escaping]]).
- Ne pas résoudre une collision en fusionnant à l'aveugle deux homonymes : le
  suffixe de type est automatique ; `FUSION` est réservé aux vrais synonymes.
- Traiter le rapport de quasi-doublons à chaque lot (sinon fragmentation du
  graphe). Voir aussi [[index-genere-catalogue-machine]].
