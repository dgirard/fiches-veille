---
title: "Candidats Pont V — fiches veille à promouvoir vers le référentiel transverse"
status: active
date: 2026-04-30
plan_reference: ATransverse/docs/plans/2026-04-29-001-feat-pipeline-capitalisation-v3.1-plan.md
---

# Candidats Pont V — promotion vers Transverse

> Fichier consolidé des fiches candidates à promotion vers `ATransverse/00-raw/from-pont-v/`. Lu par le Lab transverse en revue mensuelle (cf. plan v3 § 14.5 et `ATransverse/docs/governance-drafts/lab-charter.md`).

## Format d'une entrée

```yaml
- fiche_id: <slug-de-la-fiche>             # ex. osmani-agent-harness-engineering-2026-04-19
  fiche_path: fiches/YYYY-MM/<slug>.md
  proposed_class: Concept | Pattern | Framework | BenchmarkDatapoint
  proposed_capability: capability/<slug>   # ex. capability/software-factory
  proposed_label: ""                       # nom transverse de l'asset à créer
  status: pending | under-review | promoted | rejected
  marked_by: <consultant>
  marked_date: YYYY-MM-DD
  notes: ""                                # justification ou observations cabinet
  lab_session: <date de la session Lab qui a tranché>
  lab_decision_rationale: ""               # pour les promoted/rejected
  resulting_asset_id: <id transverse>      # pour les promoted
```

## Workflow

1. **Marquer un candidat** :
   - Soit dans le frontmatter de la fiche elle-même (cf. `CLAUDE.md` section frontmatter de promotion).
   - Soit en ajoutant une entrée ci-dessous (recommandé pour le suivi consolidé).
2. **Le Lab transverse** parcourt ce fichier en revue mensuelle.
3. **Décision Lab** : promote (création de l'asset transverse) / clarification_needed / reject.
4. **Mise à jour du status** par le Lab après la session.

## Candidats

*(Aucun candidat enregistré. Premier candidat à venir lors de la première session Lab après bootstrap.)*

## Anti-patterns

- **Marquer 50 fiches d'un coup** : le Lab ne peut absorber que ~5-10 candidats Pont V par session. Privilégier les fiches qui correspondent à un pattern observé en plusieurs missions (effet compound veille × mission) ou à une nouveauté stratégique pour le cabinet.
- **Marquer une fiche pour "intérêt futur"** : sans `proposed_class` et `proposed_label`, la fiche reste marquée indéfiniment sans avancée. Marquer = engager une décision dans les 3 sessions Lab suivantes.
- **Promouvoir sans synthèse autoportante** : un asset transverse Concept/Pattern/Framework doit pouvoir être lu sans la fiche source. Si l'asset proposé dépend trop fortement de la fiche pour être compris, il n'est pas mûr — laisser en `pending`.
