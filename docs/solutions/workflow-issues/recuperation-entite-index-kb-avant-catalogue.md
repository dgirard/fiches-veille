---
title: Question sur une entité — grep kb/_index-entites.md avant catalogue.tsv
date: 2026-08-21
category: workflow-issues
module: récupération (catalogue.tsv + kb/)
problem_type: workflow_issue
component: development_workflow
severity: medium
applies_when:
  - "On cherche « y a-t-il une fiche sur X ? » où X est un nom d'entité (produit, personne, organisation)"
  - "Le terme cherché est court (3-5 caractères) et risque d'être un sous-mot d'autre chose"
  - "On veut le coût en tokens le plus bas possible avant de lire une fiche"
tags:
  - grep-first
  - recuperation
  - token-efficiency
  - kb-generee
  - catalogue
  - desambiguisation
---

# Question sur une entité — grep `kb/_index-entites.md` avant `catalogue.tsv`

## Contexte

Le workflow de récupération documenté dans `CLAUDE.md` est *grep-first sur
`catalogue.tsv`*. C'est le bon défaut pour une recherche **thématique** (« que
dit le corpus sur le coût d'inférence ? »), mais c'est le mauvais premier
barreau pour une question **d'entité** (« y a-t-il une fiche sur Berd ? »), et
ce pour deux raisons mesurables.

**Le coût.** Une ligne de `catalogue.tsv` fait en moyenne **931 octets** et
jusqu'à **5 175** (colonnes `auteurs` et `keywords` volumineuses). Un grep qui
ramène la ligne entière paie ce prix par candidat, y compris pour les faux
positifs. Sur une requête volontairement élargie (`ber[dt]`) : **17 lignes,
24 614 octets** — pour une réponse qui tient en un identifiant.

**Le bruit.** `grep -i` fait du sous-mot, pas du mot. Sur ce corpus bilingue et
riche en noms propres, un token de 4 lettres percute :

- `berd` ⊂ **cy·berd·éfenseurs** (fiche `anthropic-claude-fable-5-mythos-5-2026-06-09`)
- `bert` ⊂ **Bert·rand**, **Al·bert**, et l'entité réelle **BERT**

Rien dans la ligne ramenée ne dit *où* le terme a frappé — il faut lire pour
trancher, donc payer encore.

## Guidance

Pour une question d'entité, monter l'échelle par coût croissant et s'arrêter au
premier barreau qui répond :

**1. `kb/_index-entites.md`** — l'index alphabétique généré des **3 192**
entités du graphe (majeures *et* mineures). Une ligne par entité, avec son type
et son nombre de fiches :

```bash
grep -i "berd" kb/_index-entites.md
# - [[kb/Berd\|Berd]] (TECHNOLOGIE, 1 fiches)   → 1 ligne, 44 octets
```

C'est la réponse définitive au « existe-t-il une entité X ? », **typée** (donc
auto-désambiguïsante : `TECHNOLOGIE` écarte d'emblée un homonyme personne), pour
560× moins d'octets que le grep catalogue élargi. Ne jamais `cat` ce fichier :
266 Ko.

**2. `kb/Entité.md`** — si l'entité a sa page (513 pages sur 3 192 entités ; les
autres sont regroupées dans `kb/_entites-mineures.md`, **1,2 Mo**, à ne jamais
lire en entier). La page liste les fiches qui citent l'entité.

**3. `catalogue.tsv`, mais tronqué** — quand il faut passer au niveau fiche,
borner la largeur avec `cut` :

```bash
grep -i "berd" catalogue.tsv | cut -f1,2,3   # id, date, titre
# 2 lignes, 212 octets   (au lieu de 1 900 sans cut)
```

Les 9 colonnes sont `id date titre auteurs source themes keywords veille_courte
flags` ; `-f1,2,3` suffit à choisir un candidat, `-f1,2,3,8` ajoute la veille
courte quand le titre ne tranche pas.

**4. Lire la fiche** (`fiches/YYYY-MM/id.md`) — seulement une fois le candidat
choisi.

## Pourquoi ça compte

L'architecture du dépôt est explicitement optimisée pour un coût en tokens bas,
et la fiche [[index-genere-catalogue-machine]] chiffre la récupération
grep-first à **~197 tokens/candidate**. Ce chiffre suppose une ligne de taille
moyenne et un grep précis ; il ne tient pas pour une requête d'entité courte,
où le ratio réel observé est de l'ordre de 6 000 tokens pour une réponse de
44 octets. L'échelle ci-dessus restaure la propriété visée sans changer
l'architecture : elle exploite le fait que `build_knowledge_base.py` produit
déjà un **index d'entités**, c'est-à-dire précisément l'index inversé que le
catalogue n'est pas.

Le second effet est la **précision**. Le catalogue est un index plein texte sur
des champs longs ; l'index d'entités est un index sur des noms normalisés,
adossé au registre de types du graphe. Sur un corpus bilingue où
`CLAUDE.md` impose déjà d'essayer variante accentuée *et* désaccentuée, terme FR
*et* EN, réduire la surface de collision au nom d'entité est ce qui évite de
multiplier les passes.

## Quand l'appliquer

- **Oui** : la requête est un nom propre — produit, modèle, personne,
  organisation, technologie. C'est le cas d'usage direct de l'index d'entités.
- **Oui** : la requête fait moins de ~6 caractères, quel que soit son type — le
  risque de sous-mot domine.
- **Non** : la requête est thématique ou conceptuelle (« souveraineté »,
  « J-Curve », « coût d'inférence »). Là, `catalogue.tsv` reste le bon premier
  barreau : les colonnes `themes`, `keywords` et `veille_courte` sont faites pour
  ça, et l'index d'entités ne contient que des noms.
- **Préalable inchangé** : `python3 scripts/check_coherence.py --catalogue-only`
  avant toute lecture du corpus. Un `kb/` périmé ment exactement comme un
  catalogue périmé — et le doctor couvre les deux.

## Exemples

Avant — la question « y a-t-il une fiche sur Berd ? » traitée en attaquant le
catalogue, avec un motif élargi par prudence orthographique :

```bash
grep -i -E "ber[dt]" catalogue.tsv        # 17 lignes, 24 614 octets
```

Résultat : 16 des 17 lignes sont hors sujet (Bertrand, cyberdéfenseurs, Ellis
Jr., une mention réelle de BERT), et les colonnes `auteurs` et `keywords` pèsent
l'essentiel du volume ramené.

Après — même question, même incertitude orthographique :

```bash
grep -i -E "ber[dt]" kb/_index-entites.md        # 8 lignes, 585 octets
# - [[kb/Antoine-Habert\|Antoine Habert]] (PERSONNE, 2 fiches)
# - [[kb/Berd\|Berd]] (TECHNOLOGIE, 1 fiches)
# - [[kb/_entites-mineures#BERT-en-C\|BERT en C]] (TECHNOLOGIE, 1 fiches)
# - [[kb/_entites-mineures#Robert-Cialdini\|Robert Cialdini]] (PERSONNE, 1 fiches)
# …
grep -i "berd" catalogue.tsv | cut -f1,2,3       # 2 lignes, 212 octets
# block-berd-caractere-agents-open-source-2026-08-18  2026-08-18  Designing AI with character…
```

Le motif élargi produit du bruit ici aussi (Ha·bert·, Ro·bert·) — mais à
~73 octets la ligne au lieu de ~1 450, et **typée** : le tri est immédiat, et
`Berd` (TECHNOLOGIE) se distingue de `BERT en C` (TECHNOLOGIE, entité mineure)
avant toute lecture. Le passage au catalogue se fait ensuite avec un motif sûr
et une largeur bornée.

## Piège d'outillage

Le `grep` de ce poste est **ugrep 7.5.0**, pas le grep BSD de macOS : `-P`
(PCRE) y fonctionne. Ne pas en faire une hypothèse dans un script partagé — pour
un motif ancré sur une colonne, préférer `awk -F'\t'`, portable partout :

```bash
awk -F'\t' 'tolower($1) ~ /berd/ {print $1"\t"$3}' catalogue.tsv
```

## Related

- [[index-genere-catalogue-machine]] — l'architecture index généré + catalogue
  machine, et le chiffrage d'origine de la récupération grep-first.
- [[alias-entites-et-bornage-kb]] — normalisation des noms d'entités et bornage
  de la KB générée, qui conditionnent la fiabilité de l'index d'entités.
