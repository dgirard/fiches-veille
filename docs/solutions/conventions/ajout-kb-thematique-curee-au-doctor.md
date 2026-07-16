---
title: Ajouter une KB thématique curée (kb-*.md) et l'enregistrer au doctor
date: 2026-07-16
category: conventions
module: kb-thematiques-curees
problem_type: convention
component: tooling
severity: medium
applies_when:
  - "On crée un nouveau kb-*.md thématique curé à la main (souveraineté, context-engineering…)"
  - "On veut que check_coherence.py signale le retard de ce fichier quand de nouvelles fiches arrivent"
  - "Un thème est trop large pour servir de périmètre de suivi sans générer de faux retards"
tags:
  - knowledge-base
  - check-coherence
  - doctor
  - kb-thematique
  - curated-vs-generated
  - staleness-tracking
---

# Ajouter une KB thématique curée (kb-*.md) et l'enregistrer au doctor

## Context

Les `kb-*.md` à la racine (`kb-context-engineering.md`, `kb-commerce-agentique.md`,
`kb-skills.md`, et désormais `kb-souverainete.md`) sont des **KB thématiques
curées à la main** — à ne pas confondre avec le répertoire `kb/` (pages d'entités
**générées** par `build_knowledge_base.py`). Elles sont versionnées (étage Silver)
mais **écrites, pas dérivées**. Rien ne les régénère : leur seul garde-fou de
fraîcheur est le **check (d)** de `scripts/check_coherence.py` (« KB thématiques à
jour »), qui n'existe que si le fichier est **déclaré** dans la table
`KB_THEMATIQUES`. Un `kb-*.md` créé sans cet enregistrement est un artefact
orphelin : il vieillit en silence, sans jamais qu'un `doctor` ne réclame sa mise
à jour.

## Guidance

Créer une KB thématique curée = **deux écritures** (le fichier + son inscription
au doctor), pas une seule.

1. **Écrire `kb-<slug>.md`** à la racine, en calquant la structure d'une KB
   existante (`kb-commerce-agentique.md` est le meilleur modèle) : titre `#`, puis
   une **ligne d'en-tête** `> N fiches | Période : … | Généré le YYYY-MM-DD`, puis
   Vue d'ensemble → Chronologie → Fiches sources → Entités clés → Concepts
   structurants. Les wikilinks pointent vers `[[fiches/AAAA-MM/id\|Titre]]` et
   `[[kb/Entité\|libellé]]` (pages majeures) ou `[[kb/_entites-mineures#Ancre\|…]]`
   (entités mineures). Vérifier les cibles avant d'écrire (les ancres mineures
   existent sous la forme `{#Nom-Avec-Tirets}`).

2. **Enregistrer le périmètre** dans `KB_THEMATIQUES` (`scripts/check_coherence.py`) :

   ```python
   "kb-souverainete.md": {
       "themes": set(),                    # ← vide, cf. « Why this matters »
       "keywords": ["souverain", "cloud act", "secnumcloud", "extraterritorial",
                    "cloud de confiance", "réversibilité", "scaleway"],
   },
   ```

3. **Vérifier** : la suite complète (`python3 -m unittest discover -s scripts/tests
   -t scripts/tests -p "test_*.py"`) reste verte, et `check_coherence.py` finit
   **exit 0** *sans* lister le nouveau fichier en retard.

Aucune régénération d'`index.md` / `catalogue.tsv` / `kb/` n'est requise : une KB
curée n'ajoute **pas** de fiche, donc les fonctions pures des fiches sont
inchangées. Commit : le `kb-*.md` **et** `scripts/check_coherence.py` (les deux
sont versionnés — Silver + tooling ; ce ne sont pas des générés, on peut les
stager sans réserve).

## Why This Matters

Deux pièges non évidents, tous deux dans le mécanisme du check (d) :

- **La date de l'en-tête pilote le retard.** Le check lit les **8 premières
  lignes**, en extrait la **première date ISO** comme « date de génération », puis
  compte les fiches publiées **strictement après** (`date > since`) qui matchent le
  périmètre. Mettre `Généré le` = date de la fiche la plus récente incluse (ou la
  date du jour) → **zéro retard immédiat**. Une date trop ancienne dans l'en-tête
  fait clignoter le doctor dès la création.

- **`themes` large = faux retards en cascade.** Le périmètre matche une fiche si
  `themes ∩ fiche.themes` **ou** n'importe quel `keyword` apparaît dans
  titre+veille+keywords. Un slug de thème large (`politique-regulation`) capturerait
  des dizaines de fiches sans rapport avec la souveraineté cloud/IA, générant des
  retards permanents et non actionnables. Préférer **`themes: set()` + mots-clés
  discriminants** : le suivi reste précis, et les WARN futurs sont de vrais signaux
  (« une fiche souveraineté est arrivée, enrichis la KB »).

Sans l'étape 2, la KB est invisible du doctor : elle ne bénéficie d'aucun filet de
fraîcheur alors que c'est précisément la seule chose qui la protège (elle n'est
jamais régénérée).

## When to Apply

- À chaque création d'un `kb-*.md` thématique curé.
- Quand on hésite entre `themes` (slug) et `keywords` comme périmètre : choisir
  `keywords` seuls dès que le thème est plus large que le sujet réel de la KB.
- Ne s'applique **pas** aux pages `kb/*.md` (générées — ne jamais éditer à la main)
  ni à `knowledge-base.md` (dashboard généré).

## Examples

**Faux retard évité (choix du périmètre)** — au 2026-07-16, `kb-souverainete.md`
couvre 9 fiches et n'apparaît pas dans le check (d) :

```
d. KB thématiques à jour  WARN  kb-context-engineering.md: 20 depuis 2026-06-09 ;
                                kb-commerce-agentique.md: 5 depuis 2026-06-09 ;
                                kb-skills.md: 6 depuis 2026-06-16
                                # kb-souverainete.md : absent = à jour ✓
```

Si l'on avait déclaré `"themes": {"politique-regulation"}`, la KB serait apparue
en retard dès sa naissance (toute fiche politique-regulation postérieure au
2026-07-16 comptant, y compris les non-souveraines).

**Mécanisme du check (extrait `check_coherence.py`)** :

```python
since = m.group(1)                 # 1re date ISO des 8 premières lignes de kb-*.md
for r in records:
    if r["date"] <= since:         # fiches ≤ date d'en-tête : ignorées
        continue
    hay = (r["titre"] + " " + r["veille_courte"] + " " + " ".join(r["keywords"])).lower()
    if perim["themes"] & set(r["themes"]) or any(k in hay for k in kws):
        n += 1                     # n > 0 ⇒ WARN « retard »
```

## Related

- [[index-genere-catalogue-machine]] — le doctor et son manifest côté artefacts
  **générés** (index/catalogue/kb) ; ce doc-ci couvre le versant **curé**.
- [[alias-entites-et-bornage-kb]] — distinction `kb/` (généré) vs `kb-*.md` (curé),
  et wikilinks/ancres d'entités utilisés par les KB thématiques.
