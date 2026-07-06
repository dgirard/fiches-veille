# Workflow de production en lot — référence

> Ajout de fiches par agents parallèles (8-12 fiches/lot). Playbook éprouvé
> (learning `docs/solutions/data-completeness/missing-knowledge-graph-sections.md`).

## Principe

Les artefacts générés (`index.md`, `catalogue.tsv`, `kb/`, `knowledge-base.md`)
**ne se mergent jamais** — en cas de conflit git, on **régénère**. Un lot ne
touche donc que les sources ; l'orchestrateur seul régénère et committe.

## Rôles

**Agents de lot** (parallèles) — ne touchent QUE :
- `fiches/YYYY-MM/id.md` (fiche complète : 10 sections + frontmatter éditorial) ;
- `raw-data/id.md` (contenu brut, gitignoré).

Chaque agent lint sa propre fiche localement :
`python3 scripts/lint_fiches.py fiches/YYYY-MM/id.md`.
Il ne régénère pas les artefacts, ne stage pas, ne committe pas.

**Orchestrateur** (séquentiel, après le lot) :
1. `python3 scripts/lint_fiches.py` (corpus complet — unicité des ids, etc.) ;
2. `python3 scripts/build_index.py` (catalogue + index + README) ;
3. `python3 scripts/build_knowledge_base.py` (kb/ + dashboard) ;
4. Traiter le **rapport de quasi-doublons** imprimé par le build (arbitrer via
   `scripts/entity_aliases.tsv` : `FUSION` pour un vrai synonyme, sinon laisser) ;
5. `python3 scripts/check_coherence.py` (doit finir exit 0) ;
6. **Un seul commit** : fiches + `index.md` + `catalogue.tsv` + `kb/` +
   `knowledge-base.md` (+ `README.md` si stats changées). Jamais `docs/`,
   `.DS_Store`, `.obsidian/`.

## Bonnes pratiques (lot de masse / backfill)

- **Lots de 8-12 fiches** par agent ; au-delà, la qualité se dégrade.
- **Idempotence** : vérifier qu'une fiche n'existe pas déjà avant de l'écrire.
- **2-3 fiches modèles** dans le prompt de l'agent (exemples de référence).
- **Lire le contenu source complet** (raw-data) avant de rédiger le KG.
- **Audit manuel de 10-15 %** des fiches produites après chaque lot.
- **Traiter le rapport de quasi-doublons à chaque lot** — la fragmentation du
  graphe croît sinon linéairement avec le volume.

## Résolution de conflit sur artefacts générés

Un `git merge`/`rebase` qui entre en conflit sur `kb/**`, `index.md`,
`catalogue.tsv` ou `knowledge-base.md` : **ne pas résoudre à la main**. Prendre
une version au hasard (`git checkout --theirs`/`--ours`), puis **re-régénérer**
les trois scripts et re-committer. Le contenu généré est une fonction pure des
fiches.
