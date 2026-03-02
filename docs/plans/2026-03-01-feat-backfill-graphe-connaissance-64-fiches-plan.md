---
title: "feat: Garantir GrapheDeConnaissance sur toute nouvelle fiche"
type: feat
date: 2026-03-01
---

# Garantir GrapheDeConnaissance sur toute nouvelle fiche

## Overview

Quand une nouvelle fiche est créée (via Claude Code ou manuellement), la section `## GrapheDeConnaissance` doit **toujours** être générée. Actuellement, CLAUDE.md liste la section comme obligatoire mais rien ne l'impose techniquement. Objectif : ajouter une validation automatique.

## Solution

### 1. Script de validation `scripts/validate_fiches.py`

Script qui vérifie que toutes les fiches dans `fiches/` possèdent une section `## GrapheDeConnaissance` correctement formatée.

**Vérifications :**
- Présence de `## GrapheDeConnaissance`
- Sous-section `### Triples` avec tableau 8 colonnes
- Sous-section `### Entités` avec tableau 5 colonnes
- Au moins 3 triples par fiche
- Confiance >= 0.70 sur tous les triples
- Types d'entités dans l'ensemble autorisé

**Usage :**
```bash
# Valider toutes les fiches
python3 scripts/validate_fiches.py

# Valider une fiche spécifique
python3 scripts/validate_fiches.py fiches/2026-03/nouvelle-fiche-2026-03-01.md

# Mode strict : exit code non-zero si erreurs (pour CI/hooks)
python3 scripts/validate_fiches.py --strict
```

**Output :**
```
Validating 192 fiches...
  OK: 128 fiches avec GrapheDeConnaissance valide
  MISSING: 64 fiches sans GrapheDeConnaissance
  ERRORS: 0 fiches avec section malformée

Fiches sans GrapheDeConnaissance:
  fiches/2024-06/exemple-ancien.md
  fiches/2025-11/exemple-youtube.md
  ...
```

### 2. Hook git pre-commit (optionnel)

Script shell qui lance la validation sur les fiches modifiées/ajoutées dans le commit :

```bash
# .claude/hooks/pre-commit ou git hook
# Vérifie que les fiches ajoutées/modifiées ont GrapheDeConnaissance
changed_fiches=$(git diff --cached --name-only --diff-filter=AM | grep '^fiches/.*\.md$')
if [ -n "$changed_fiches" ]; then
  python3 scripts/validate_fiches.py --strict $changed_fiches
fi
```

### 3. Rebuild KB à la demande

La régénération de la knowledge base Obsidian reste **manuelle** (coûteuse en temps) :

```bash
python3 scripts/build_knowledge_base.py
```

Le script de validation **ne déclenche pas** le rebuild. L'utilisateur le lance quand il le souhaite.

## Acceptance Criteria

- [ ] `scripts/validate_fiches.py` créé et fonctionnel
- [ ] Accepte un chemin de fiche en argument ou valide tout le répertoire `fiches/`
- [ ] Détecte : section manquante, colonnes incorrectes, confiance < 0.70, types invalides
- [ ] Mode `--strict` avec exit code 1 si erreurs (pour intégration CI/hooks)
- [ ] Affiche un résumé clair (OK / MISSING / ERRORS)

## Hors scope

- Backfill des 64 fiches existantes sans GrapheDeConnaissance
- Génération automatique de la section (reste manuelle via Claude)
- Hook git pre-commit (optionnel, peut être ajouté après)
