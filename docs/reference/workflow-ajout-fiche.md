# Ajouter une fiche à partir d'une URL — procédure de référence

Référence chargée à la demande, pendant de [`workflow-batch.md`](workflow-batch.md)
(qui traite la production en lot). Celle-ci traite **une URL, une fiche**.

`CLAUDE.md` porte les règles ; ce document porte **l'ordre des gestes** et les
pièges constatés en production. En cas de divergence, `CLAUDE.md` fait foi.

## 0. Avant de commencer — trois lectures

| À lire | Quand | Pourquoi |
|--------|-------|----------|
| `CLAUDE.md` § **Registre éditorial** | avant d'écrire `## Veille` | volumes cibles, registre proscrit |
| [`ontologie-kg.md`](ontologie-kg.md) | avant d'écrire `## GrapheDeConnaissance` | registre fermé des 30 prédicats, types, désambiguïsation |
| `scripts/themes.tsv` | avant d'écrire le frontmatter | seuls ces slugs sont acceptés par le lint |

## 1. Extraire l'article

```bash
curl -sL "$URL" | lynx -dump -stdin -nolist > raw-data/$ID.md
```

**Piège constaté** : les pages d'annonce des laboratoires de modèles sont souvent
des **SPA rendues en JavaScript**. `curl` renvoie alors un `<div id="root">` vide
ou un `HTTP 202` sans corps (cas rencontrés : Z.ai, DeepSeek Harness). Deux
recours, dans cet ordre :

1. lire le **bundle JS** (les valeurs de tableaux y figurent souvent en clair,
   donc sans risque d'erreur de transcription) ;
2. utiliser `WebFetch` ou le navigateur.

Consigner dans `## Authors` que la page n'est pas capturable par `curl | lynx` —
c'est une information d'archivage, et le nom du bundle est haché, donc instable.

`raw-data/` est **gitignoré** : on archive, on ne stage jamais.

## 2. Déterminer l'identifiant et la date

- **Identifiant** : `auteur-sujet-YYYY-MM-DD`, préfixe `skill-` pour une skill.
  **Unique globalement** — vérifier avant d'écrire :
  ```bash
  grep -c "^$ID	" catalogue.tsv    # doit renvoyer 0
  ```
  **Gelé après commit** : ne jamais le renommer ensuite (traçabilité `fiche_id`
  côté référentiel transverse).
- **Date** : celle de **publication de l'article**, pas celle du jour. Elle
  détermine le répertoire `fiches/YYYY-MM/`, et le lint vérifie la cohérence.
  Une fiche écrite en août sur un article de mai va dans `fiches/2026-05/`.

## 3. Écrire la fiche

Dix sections, dans l'ordre gelé, précédées du frontmatter (`themes`, `source`).

Le point d'attention n'est pas la structure — le lint la vérifie — mais le
**registre**. La fiche **restitue et situe ; elle ne plaide pas**.

`## Veille`, dans cet ordre : situer la source (auteur, fonction affichée,
support, date, volume) → restituer les apports en les étiquetant `(A)`/`(B)` →
citer le texte en *italique* → rapprocher du corpus en une phrase finale. Gras
sur les entités et les chiffres, jamais sur un jugement.

**Proscrit** — la dérive d'août 2026, que le lint bloque désormais :

- le procédé « le sujet annoncé est X, le vrai sujet est Y » et ses variantes ;
- le procès d'intention (inférer un intérêt commercial, une dissimulation) — on
  rapporte ce qui est écrit **et ce qui est absent**, on n'attribue pas de motif ;
- le tableau de citabilité des signatures d'un même éditeur, et le comptage
  « Nième texte de X en un mois » ;
- plus de **2 marqueurs** ⭐/⚠️, plus de **4 wikilinks** en `Pense-betes`, plus
  de **2** en `Veille`.

Une citation où **l'auteur de l'article** emploie lui-même une de ces formules
reste légitime : la norme porte sur la voix de la fiche, pas sur celle de la
source.

**Jamais de wikilink vers une fiche non encore committée.**

## 4. Gate Bronze

```bash
python3 scripts/lint_fiches.py fiches/YYYY-MM/$ID.md
```

Doit finir à 0 violation. Si le lint refuse, **corriger la fiche, pas le lint**.

## 5. Régénérer les artefacts

```bash
python3 scripts/build_index.py
python3 scripts/build_knowledge_base.py
python3 scripts/check_coherence.py     # doit finir exit 0
```

`index.md`, `catalogue.tsv`, `kb/` et `knowledge-base.md` sont des **fonctions
pures des fiches** : ne jamais les éditer à la main, ne jamais les merger en cas
de conflit — régénérer.

Si `check_coherence.py` signale des quasi-doublons d'entités, traiter via
`scripts/entity_aliases.tsv`.

## 6. Commit unique

Stager la fiche **et** les artefacts régénérés, plus `README.md` si les stats ont
bougé :

```bash
git add fiches/YYYY-MM/$ID.md catalogue.tsv index.md knowledge-base.md kb/ README.md
```

**Ne jamais stager** : `.DS_Store`, `.obsidian/`, `docs/` (hors `reference/` et
`solutions/`), `gold/`, `raw-data/`.

Message de commit — descriptif neutre, sans thèse :

```
fiche: Auteur — « Titre » (date), <ce que la source apporte>
```

## Contrôle final

```bash
python3 scripts/lint_fiches.py            # 392 fiches, 0 violation
python3 -m unittest discover -s scripts/tests -t scripts/tests -p "test_*.py"
```

## Anti-patterns

- Renommer l'identifiant ou déplacer la fiche à la main après commit (utiliser
  un script si la date de publication doit changer).
- Éditer un artefact généré.
- Committer la fiche sans les artefacts, ou l'inverse.
- Reprendre un chiffre de la source comme une donnée établie : `## Authors`
  doit dire qui mesure quoi, et `## Ton` ce que le texte permet de citer.
