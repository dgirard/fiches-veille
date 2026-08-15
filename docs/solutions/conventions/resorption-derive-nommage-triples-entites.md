---
title: Résorber une dérive de nommage Triples↔Entités sans la déplacer ailleurs
date: 2026-08-15
category: conventions
module: fiches
problem_type: convention
component: documentation
severity: high
applies_when:
  - "Le doctor signale des variantes de nommage entre les triples et la table Entités d'une même fiche"
  - "On corrige en lot un défaut du GrapheDeConnaissance réparti sur des dizaines ou des centaines de fiches"
  - "On hésite entre corriger les fiches et corriger le contrôle qui les signale"
  - "On envisage de déclarer une entité pour faire taire un signalement"
tags:
  - graphe-de-connaissance
  - ontologie-kg
  - entity-resolution
  - derive-nommage
  - doctor
  - correction-en-lot
---

# Résorber une dérive de nommage Triples↔Entités sans la déplacer ailleurs

## Contexte

Le contrôle `h. dérive nommage Triples↔Entités` du doctor
(`scripts/check_coherence.py:240`) signale un nom de triple qui est une
**variante** d'une entité déclarée dans la **même** fiche — les triples disent
`Uber` là où la table `### Entités` déclare `Uber Engineering`. Le build
dédupliquant par couple (nom, type), chaque variante scinde une entité en deux
pages `kb/` qui se partagent le savoir.

Le stock au démarrage : **646 variantes dans 250 fiches**. C'est un volume qui
interdit la correction ligne à ligne et qui, surtout, expose deux pièges que
l'on ne voit pas sur un cas isolé : une « correction » peut fabriquer de la
dérive ailleurs, et une partie des signalements n'en était pas.

## Guidance

### 1. Trois leviers, pas un seul

Le réflexe « renommer le triple vers l'entité déclarée » ne couvre qu'un cas sur
trois. Diagnostiquer avant de renommer :

| Situation | Levier | Exemple |
|---|---|---|
| Même référent, le triple porte un qualificatif | **Aligner** le libellé du triple sur l'entité déclarée ; la précision part en `Valeur` | `STS (demande de JWT)` → `STS (Security Token Service)` |
| Référent réellement distinct, simplement voisin de nom | **Déclarer** l'entité dans la table (elle devient un nom connu, donc exclue du contrôle) | `SPIFFE` face à `SPIFFE Verifiable IDs (SVID)` ; `revue de code humaine` face à `revue de code agentique` |
| La cellule porte **plusieurs** entités | **Éclater** le triple en autant de relations binaires | `Home Mixer + Thunder + Phoenix + Grox` → 4 triples |

Le troisième cas n'est pas une dérive de nommage mais un triple malformé que le
contrôle attrape par ricochet — un sujet ou un objet qui contient `+`, `,`,
` et ` ou `→` n'est pas une entité. Le corriger améliore le graphe bien au-delà
du signalement.

### 2. Le piège : déclarer un nom générique fabrique de la dérive

Le levier « déclarer » est sûr sur un nom propre, **dangereux sur un mot
générique**. Déclarer `IA`, `MCP`, `Markdown`, `token`, `SDLC` ou `Google` pour
faire taire un signalement transforme **toute phrase contenant ce mot** en
nouvelle dérive, puisque le contrôle compare au mot près.

Mesuré sur ce lot : déclarer `IA` dans trois fiches a créé **9 signalements
neufs** (`adoption IA`, `assistants IA`, `modèles IA`, `qualité code IA`,
`partenaire stratégique IA`…) ; déclarer `Agent` dans une fiche en a créé **2**
(`Multi-agent delegation`, `Video editor agent`).

Face à un nom générique, préférer dans cet ordre :

1. **Renommer les phrases** qui l'entourent vers des noms qui ne le contiennent
   plus — `qualité code IA` → `qualité du code généré`. C'est presque toujours
   un meilleur nom d'entité de toute façon.
2. **Renommer l'entité déclarée** dont le nom composé provoque la collision —
   `token economics` → `économie des jetons` libère `token`.
3. **Déclarer le générique** en dernier recours seulement, après avoir vérifié
   qu'aucune autre entité de la fiche ne contient ce mot.

### 3. Boucler : mesurer après chaque vague, jamais une seule fois

Corollaire direct du piège : le compteur ne décroît pas de façon monotone. Une
vague de corrections peut en ouvrir de nouvelles, y compris dans des fiches déjà
traitées. La boucle qui converge :

```
dump des paires signalées → décider en TSV → appliquer → re-dump → recommencer
```

Huit vagues ont été nécessaires pour aller de 646 à 0, dont la dernière ne
traitait **que** des dérives créées par les vagues précédentes.

### 4. Appliquer mécaniquement, décider éditorialement

Séparer le jugement de l'exécution. Le jugement se pose dans un TSV
`chemin<TAB>ancien_nom<TAB>nouveau_nom` ; l'application est un script qui
remplace **par égalité stricte de cellule** dans les tables Markdown, jamais en
sous-chaîne. Un remplacement en sous-chaîne sur `GLM` corromprait `GLM-5.2`,
`GLM Coding Plan` et la prose des attributs.

Après application : `lint_fiches.py` sur tout le corpus (un éclatement de triple
peut introduire un prédicat hors registre), puis re-dump.

### 5. Quand corriger le contrôle plutôt que les fiches

Corriger un contrôle pour faire disparaître son avertissement est en général
l'anti-pattern. Il y a une exception, et elle est étroite : **le contrôle
signale ce qu'une règle documentée prescrit**.

C'était le cas ici. L'ontologie impose de préfixer le DOCUMENT quand un article
et le concept qu'il introduit portent le même nom — `article Cognitive
Surrender` (DOCUMENT) face à `Cognitive Surrender` (CONCEPT),
`docs/reference/ontologie-kg.md:180`. Le contrôle comptait ces paires comme des
dérives : **76 faux positifs**, tous conformes à la règle.

L'exemption ajoutée (`scripts/check_coherence.py:237` et `:281`) : un nom de
triple typé `DOCUMENT` ou `EVENEMENT` dont **toutes** les entités déclarées
voisines portent un autre type applique la convention, il ne dérive pas.

Trois garde-fous qui distinguent l'exemption légitime du silence de complaisance :

- **L'exemption tombe si les deux côtés partagent le type** — deux DOCUMENT dont
  l'un est une variante de l'autre restent signalés.
- **Elle est testée dans les deux sens** (`test_document_homonyme_de_son_sujet_exempte`
  et `test_document_variante_d_un_document_signale`).
- **Elle est écrite dans la référence d'ontologie**, pas seulement dans le code —
  une règle de contrôle qui n'existe que dans son implémentation n'est pas une
  règle, c'est un comportement.

## Pourquoi c'est important

Une dérive de nommage ne casse rien : le lint passe, le build passe, le doctor
n'émet qu'un WARN. Elle dégrade silencieusement la seule chose que le graphe
sert à faire — retrouver tout ce que le corpus sait d'une entité. Deux pages
`kb/` à moitié remplies valent moins qu'une page complète, et rien ne le signale
au lecteur.

Le coût de correction est asymétrique dans le temps : chaque fiche ajoutée sans
discipline de nommage ajoute des variantes qu'il faudra arbitrer plus tard,
quand le contexte éditorial de la fiche aura disparu.

## Quand l'appliquer

- Le doctor sort `h. dérive nommage Triples↔Entités WARN` avec un stock non
  trivial.
- On s'apprête à déclarer une entité dont le nom tient en un mot courant.
- On corrige en lot un défaut réparti sur plus d'une dizaine de fiches, quelle
  que soit sa nature — la boucle mesure/décide/applique/re-mesure vaut au-delà
  de ce contrôle.

## Exemples

**Aligner (le cas majoritaire)** — la précision descend en `Valeur`, le triple
reprend le libellé déclaré :

```diff
- | Uber (Sr Staff Engineer) | ORGANISATION | ... |
+ | Uber Engineering | ORGANISATION | ... |
```

**Déclarer (référent distinct)** — `SPIFFE` est le standard, `SVID` le document
d'identité qu'il définit ; les fusionner effacerait la distinction :

```diff
+ | SPIFFE | TECHNOLOGIE | catégorie | Standard d'identité de charge de travail dont SPIRE est l'implémentation de référence et le SVID le document d'identité | AJOUT |
```

**Éclater (triple malformé)** :

```diff
- | Home Mixer + Thunder + Phoenix + Grox | TECHNOLOGIE | fait_partie_de | x-algorithm | ... |
+ | Home Mixer | TECHNOLOGIE | fait_partie_de | x-algorithm | ... |
+ | Thunder | TECHNOLOGIE | fait_partie_de | x-algorithm | ... |
+ | Phoenix | TECHNOLOGIE | fait_partie_de | x-algorithm | ... |
+ | Grox | TECHNOLOGIE | fait_partie_de | x-algorithm | ... |
```

**Contourner le générique plutôt que le déclarer** :

```diff
- | ... | qualité code IA | CONCEPT | ... |     ← déclarer « IA » ferait dériver toute la fiche
+ | ... | qualité du code généré | CONCEPT | ... |
```

## Related

- [[sigles-jamais-entites-graphe]] — la règle amont : un sigle nu n'est jamais un
  nom d'entité. Les deux se complètent — celle-ci traite la fragmentation
  intra-fiche, celle-là la conflation inter-fiches.
- [[alias-entites-et-bornage-kb]] — `scripts/entity_aliases.tsv` arbitre les
  variantes **entre** fiches (`FUSION`/`DISTINCT`) là où le contrôle (h) ne voit
  que l'intérieur d'une fiche.
- [[index-genere-catalogue-machine]] — après toute correction de fiches,
  régénérer index et KB avant de committer.
