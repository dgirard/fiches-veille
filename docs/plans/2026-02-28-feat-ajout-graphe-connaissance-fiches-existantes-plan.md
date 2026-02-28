---
title: "feat: Ajouter GrapheDeConnaissance aux 123 fiches existantes ayant un raw-data"
type: feat
date: 2026-02-28
---

# Ajouter ## GrapheDeConnaissance aux 123 fiches existantes

## Overview

123 fiches de veille disposent d'un fichier raw-data correspondant mais n'ont pas encore de section `## GrapheDeConnaissance`. Cette section (définie dans CLAUDE.md) contient deux sous-sections — `### Triples` et `### Entités` — qui extraient les entités et relations clés sous forme de knowledge graph structuré.

## Périmètre

### Fiches à traiter (123) — par mois

| Mois       | Nombre | Exemples                                       |
|------------|--------|-------------------------------------------------|
| 2025-10    | 30     | a16z-trillion, ace-stanford, agent-skills...    |
| 2025-11    | 16     | anand-wu-hbr, anthropic-espionage, caseau...    |
| 2025-07    | 16     | aws-kiro, gartner-hype, gemini-flash-lite...    |
| 2025-09    | 14     | anthropic-economic, claude-subagents, dora...   |
| 2026-02    | 12     | andreessen-coding, anthropic-trends, carlini... |
| 2025-08    | 9      | a16z-one-prompt, block-goose, luc-julia...      |
| 2025-06    | 6      | augmented-coding-beck, gemini-cli-hybrid...     |
| 2025-04    | 3      | ai-workflow-wardley, gemini-cli-tos, stanford...|
| 2026-01    | 2      | forrestchang-karpathy, gao-vercel-agents-md     |
| 2025-12    | 2      | clouded-judgement, worldbank-chalkboards         |
| 2025-05    | 2      | mollick-making-ai-work, linear-ai-first         |
| 2024-10    | 2      | kent-beck-vibe-coding, lightrag-hkuds           |
| 2024-04    | 2      | ethan-mollick-ai-adoption, raschka-ml           |
| 2025-03    | 1      | google-ai-mode-search                           |
| 2025-02    | 1      | graphite-aeo-seo                                |
| 2025-01    | 1      | lee-robinson-personal-software                  |
| 2024-07    | 1      | mollick-confronting-impossible-futures           |
| 2023-10    | 1      | workweave-loom-ai                               |
| 2023-07    | 1      | metr-study-autonomous-replication               |
| 2023-06    | 1      | mollick-setting-time-fire                        |

### Fiches déjà complètes (5) — à ne pas toucher

- `debois-tessl-context-flywheel-ai-coding-teams-2026-02-26.md`
- `debois-tessl-context-development-lifecycle-ai-coding-agents-2026-02-19.md`
- `lancemartin-anthropic-prompt-auto-caching-claude-2026-02.md`
- `trq212-anthropic-claude-code-prompt-caching-lessons-2026-02.md`
- `cherny-yc-lightcone-claude-code-origin-story-2026-02.md`

### Raw-data orphelins (2) — nommage différent, à ignorer pour l'instant

- `anthropic-political-even-handedness-2025-11-13.md` → fiche nommée `anthropic-measuring-political-bias-claude-2025-11-13.md`
- `rippletide-agent-reliability-enterprise-ai-2025-11.md` → fiche nommée `rippletide-agent-reliability-enterprise-architecture-2025-10-29.md`

## Proposed Solution

### Approche : traitement par lots parallèles via subagents

Pour chaque fiche à traiter, un subagent autonome :

1. **Lit le raw-data** (`raw-data/{identifiant}.md`) pour avoir le contenu source complet
2. **Lit la fiche existante** (`fiches/{mois}/{identifiant}.md`) pour comprendre le contexte déjà analysé (résumé, pense-bêtes, keywords)
3. **Génère la section `## GrapheDeConnaissance`** en respectant strictement le format CLAUDE.md :
   - `### Triples` : tableau 8 colonnes (Sujet, Type Sujet, Prédicat, Objet, Type Objet, Confiance, Temporalité, Source)
   - `### Entités` : tableau 5 colonnes (Entité, Type, Attribut, Valeur, Action)
   - 5-15 triples par fiche, seuil confiance ≥ 0.70
   - Prédicats en français, noms d'entités en langue d'origine
   - Types d'entités : PERSONNE, ORGANISATION, TECHNOLOGIE, CONCEPT, METHODOLOGIE, EVENEMENT, LIEU
4. **Ajoute la section** à la fin de la fiche existante (après `## RésuméDe400mots`)

### Stratégie de parallélisation

Traiter par **lots de 5 fiches en parallèle** (5 subagents simultanés), en procédant mois par mois dans l'ordre chronologique inverse (plus récent d'abord).

**Ordre des lots :**

1. **2026-02** (12 fiches → 3 lots)
2. **2026-01** (2 fiches → 1 lot)
3. **2025-12** (2 fiches → 1 lot)
4. **2025-11** (16 fiches → 4 lots)
5. **2025-10** (30 fiches → 6 lots)
6. **2025-09** (14 fiches → 3 lots)
7. **2025-08** (9 fiches → 2 lots)
8. **2025-07** (16 fiches → 4 lots)
9. **2025-06** (6 fiches → 2 lots)
10. **2025-05 et avant** (8 fiches → 2 lots)

**Total : ~28 lots séquentiels de 5 agents parallèles chacun**

### Prompt type pour chaque subagent

```
Lis le fichier raw-data/{identifiant}.md et la fiche fiches/{mois}/{identifiant}.md.
Génère une section ## GrapheDeConnaissance conforme au format CLAUDE.md et ajoute-la
à la fin de la fiche. Respecte : 5-15 triples, confiance ≥ 0.70, prédicats en français,
types d'entités standards, tout en français sauf noms d'entités et titres.
```

## Acceptance Criteria

- [x] Les 123 fiches identifiées contiennent une section `## GrapheDeConnaissance`
- [x] Chaque section contient `### Triples` (tableau 8 colonnes) et `### Entités` (tableau 5 colonnes)
- [x] 5 à 15 triples par fiche, confiance ≥ 0.70
- [x] Prédicats en français sous forme verbale courte
- [x] Types d'entités conformes (PERSONNE, ORGANISATION, TECHNOLOGIE, CONCEPT, METHODOLOGIE, EVENEMENT, LIEU)
- [x] Types temporels conformes (STATIQUE, DYNAMIQUE, ATEMPOREL)
- [x] Types source conformes (déclaré_article, inféré, généré_assistant)
- [x] Actions entités conformes (AJOUT, MISE_A_JOUR, INVALIDATION)
- [x] Noms d'entités en langue d'origine, tout le reste en français
- [x] Aucune fiche existante corrompue (pas de contenu supprimé)
- [x] Les 5 fiches déjà complètes ne sont pas modifiées

## Dependencies & Risks

**Risques :**
- **Volume** : 123 fiches × ~15 triples = traitement lourd, risque de timeout ou d'incohérence en fin de session
- **Qualité variable des raw-data** : certains fichiers bruts peuvent être incomplets (sites ayant bloqué le scraping)
- **Cohérence inter-fiches** : les mêmes entités (Anthropic, Claude Code, Ethan Mollick...) doivent être nommées de manière cohérente d'une fiche à l'autre

**Mitigations :**
- Traitement par lots avec vérification intermédiaire
- Script de validation post-traitement pour vérifier la présence des sections
- Nommage d'entités guidé par les conventions existantes dans les 5 fiches déjà complètes

## Vérification post-traitement

```bash
# Vérifier que toutes les fiches avec raw-data ont le GrapheDeConnaissance
for raw in raw-data/*.md; do
  base=$(basename "$raw")
  fiche=$(find fiches -name "$base" 2>/dev/null | head -1)
  if [ -n "$fiche" ] && ! grep -q "## GrapheDeConnaissance" "$fiche"; then
    echo "MANQUANT: $fiche"
  fi
done
```
