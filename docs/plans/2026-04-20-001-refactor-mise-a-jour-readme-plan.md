---
title: 'refactor: Mise à jour du README'
type: refactor
status: active
date: 2026-04-20
---

# refactor: Mise à jour du README

## Overview

Le fichier `README.md` du dépôt de veille est désynchronisé avec l'état actuel du projet. Plusieurs informations factuelles (période couverte, nombre de fiches, statistiques knowledge base, liste des auteurs, arborescence) ne reflètent plus la réalité depuis l'ajout de fiches en avril 2026 et la reconstruction de la KB. Ce plan liste les corrections ponctuelles à apporter pour remettre le README en phase avec `index.md` et la structure actuelle du dépôt.

## Problem Frame

Le README est la porte d'entrée du dépôt (affiché par défaut sur GitHub). Il comporte aujourd'hui :

- Une période couverte qui s'arrête en **Mars 2026** alors que des fiches de **Avril 2026** existent
- Un total de **214 fiches** alors que `index.md` (source de vérité) en comptabilise **212**
- Des statistiques KB (`1376 entités, 2630 triples`) générées le **2026-03-27**, potentiellement obsolètes après l'ajout de nouvelles fiches en avril
- Une arborescence `fiches/` qui liste `2026-01/ à 2026-03/` sans mentionner `2026-04/`
- Une liste d'auteurs principaux avec OpenAI à **3 articles** (actuel : 4) et sans Tony Seale ni Martin Fowler qui atteignent 2 articles
- Une description erronée d'Alistair Gray ("Knowledge graphs, IA") qui doit refléter ses articles Stripe Minions

Le README doit redevenir un snapshot fidèle de l'état du dépôt.

## Requirements Trace

- R1. La période couverte doit inclure Avril 2026
- R2. Le nombre total de fiches doit correspondre à la valeur déclarée dans `index.md`
- R3. Les compteurs de la knowledge base doivent être à jour ou explicitement datés
- R4. L'arborescence doit refléter les répertoires de fiches actuellement présents
- R5. La liste des auteurs principaux doit refléter les compteurs actuels
- R6. La date de dernière mise à jour doit être actualisée

## Scope Boundaries

**Inclus :**
- Correction des chiffres et dates du README
- Mise à jour de l'arborescence et de la liste d'auteurs
- Option de reconstruire la knowledge base en amont pour obtenir des compteurs à jour

**Exclus (non-goals) :**
- Restructuration du README (ajout/suppression de sections majeures)
- Traduction ou réécriture éditoriale
- Modification du contenu des fiches ou de `index.md`
- Évolution des scripts ou du format de fiche
- Création d'un historique de changelog

## Context & Research

### Relevant Code and Patterns

- `README.md` — fichier cible, structuré en sections déjà stables
- `index.md` lignes 520-524 — bloc **Statistiques** qui sert de source de vérité pour `Total d'articles` et liste d'auteurs
- `knowledge-base.md` ligne 3 — ligne d'en-tête KB datée (`211 fiches | 1376 entités | 2630 triples | Généré le 2026-03-27`)
- `scripts/build_knowledge_base.py` — script à relancer si on veut actualiser les compteurs KB
- `CLAUDE.md` — convention : les fiches sont en français, organisées par mois de publication

### Institutional Learnings

- `index.md` est la source de vérité pour le compte de fiches et la liste des auteurs (le README reflète, n'invente pas)
- Les fiches datées `YYYY-MM` sans jour (ex : `2026-03`, `2025-12`) sont comptées dans le total mais peuvent faire varier le compte fichier vs compte logique (219 fichiers `.md` vs 212 entrées logiques)
- Rebuild KB coûte peu : `python3 scripts/build_knowledge_base.py` lit les sections `GrapheDeConnaissance` de toutes les fiches et régénère `kb/` + `knowledge-base.md`

## Key Technical Decisions

- **Source de vérité** : `index.md` (bloc Statistiques ligne 520+) pour le total d'articles et la liste des auteurs. En cas de divergence avec le comptage filesystem, `index.md` gagne.
- **Rebuild KB avant mise à jour README** : pour éviter de réécrire des compteurs KB qui seront immédiatement obsolètes, on relance `scripts/build_knowledge_base.py` avant de recopier les nouveaux chiffres dans le README.
- **Pas de reformatage** : on conserve la structure actuelle du README. Seules les valeurs factuelles changent.
- **Date de mise à jour** : on utilise la date du jour (2026-04-20) au format `Mois AAAA` pour cohérence avec l'existant.

## Open Questions

### Resolved During Planning

- **Quelle est la source de vérité entre `index.md` (212) et le filesystem (219) ?** `index.md` — les fichiers peuvent contenir des fiches groupées au niveau mois ou des auxiliaires. Le README doit reporter la valeur d'`index.md`.
- **Faut-il régénérer la KB avant la mise à jour README ?** Oui — l'en-tête `knowledge-base.md` date du 2026-03-27 et ne reflète pas les fiches d'avril ; relancer le script prend quelques secondes.

### Deferred to Implementation

- **Compteurs KB exacts après rebuild** : valeurs non connues avant exécution de `build_knowledge_base.py`. L'implémenteur lit `knowledge-base.md` après rebuild et recopie `N fiches | N entités | N triples`.
- **Compteur exact par auteur** : la liste actuelle de `index.md` ligne 524 agrège les principaux mais l'ordre/libellé peut être révisé. L'implémenteur s'appuie sur cette ligne comme référence.

## Implementation Units

- [ ] **Unit 1: Rebuild knowledge base**

**Goal:** Régénérer les index KB et `knowledge-base.md` pour obtenir des compteurs entités/triples à jour incluant les fiches d'avril 2026.

**Requirements:** R3

**Dependencies:** Aucune

**Files:**
- Modify: `knowledge-base.md` (régénéré)
- Modify: `kb/*.md` (régénéré)

**Approach:**
- Exécuter `python3 scripts/build_knowledge_base.py` depuis la racine du dépôt
- Lire l'en-tête de `knowledge-base.md` pour noter les nouveaux compteurs (fiches, entités, triples, date de génération)

**Test scenarios:**
- Test expectation: none — étape de génération, pas d'implémentation comportementale. Vérification uniquement : l'en-tête de `knowledge-base.md` porte la date du jour et `N fiches` ≥ 212.

**Verification:**
- `knowledge-base.md` ligne 3 mentionne la date d'aujourd'hui et un nombre de fiches cohérent avec `index.md`
- Les compteurs entités/triples sont disponibles pour l'unité 2

---

- [ ] **Unit 2: Actualiser les blocs statistiques du README**

**Goal:** Mettre à jour les deux blocs statistiques du README avec les nouvelles valeurs (période, fiches, KB).

**Requirements:** R1, R2, R3

**Dependencies:** Unit 1

**Files:**
- Modify: `README.md` (lignes 9-11 bloc en-tête, lignes 160-167 bloc Statistiques actuelles, ligne 119-125 section Knowledge Base, ligne 182 date de mise à jour)

**Approach:**
- Remplacer `Période couverte : Janvier 2019 - Mars 2026` → `Janvier 2019 - Avril 2026` (deux occurrences, lignes 9 et 163)
- Remplacer `Total d'articles : 214 fiches` → valeur d'`index.md` ligne 522 (actuellement 212)
- Remplacer les compteurs KB de la ligne 11 et lignes 121-122 par les valeurs post-rebuild de l'unité 1
- Remplacer `214 fiches analysées` ligne 162 par la nouvelle valeur
- Remplacer `Dernière mise à jour : Avril 2026` ligne 182 par `Avril 2026` (inchangé si toujours valide, sinon ajuster)

**Patterns to follow:**
- Format existant des lignes `**Clé** : Valeur`

**Test scenarios:**
- Test expectation: none — mise à jour documentaire, pas de comportement. Vérification : les trois compteurs (fiches, entités, triples) sont identiques entre README, `index.md`, et `knowledge-base.md`.

**Verification:**
- Recherche textuelle dans le README : aucune occurrence de `Mars 2026` comme fin de période
- Le nombre total de fiches est cohérent entre README, `index.md`, et `knowledge-base.md`
- Les compteurs KB du README correspondent à l'en-tête de `knowledge-base.md`

---

- [ ] **Unit 3: Actualiser l'arborescence et la liste d'auteurs**

**Goal:** Refléter dans le README l'existence du répertoire `fiches/2026-04/` et synchroniser la liste d'auteurs principaux avec `index.md`.

**Requirements:** R4, R5

**Dependencies:** Aucune (peut être fait en parallèle de Unit 2)

**Files:**
- Modify: `README.md` (ligne 23 arborescence, lignes 107-115 liste d'auteurs)

**Approach:**
- Arborescence ligne 23 : remplacer `└── 2026-01/ à 2026-03/` par `└── 2026-01/ à 2026-04/`
- Liste d'auteurs (lignes 107-115) : synchroniser avec la liste agrégée d'`index.md` ligne 524
  - Corriger OpenAI : `3 articles` → `4 articles`
  - Ajouter Martin Fowler (2 articles) — blog martinfowler.com, Thoughtworks
  - Ajouter Tony Seale (2 articles) — The Knowledge Graph Guy (ontologie, agent sémantique)
  - Vérifier la description d'Alistair Gray : il a publié les deux articles Stripe Minions, pas Knowledge Graphs. Remplacer la description par `Ingénierie agents, Stripe Minions`
- Conserver l'ordre actuel (par compteur décroissant)

**Patterns to follow:**
- Format `- **Nom** (N articles) - Thématique courte`
- Ne pas lister tous les auteurs à 1 article, se limiter aux auteurs à ≥ 2 articles et aux organisations majeures

**Test scenarios:**
- Test expectation: none — mise à jour documentaire. Vérification : chaque auteur listé dans le README est présent dans `index.md` ligne 524 avec le même compteur.

**Verification:**
- Le répertoire `fiches/2026-04/` apparaît dans l'arborescence
- Les compteurs des auteurs listés dans le README correspondent à ceux d'`index.md`
- Aucun auteur à 2+ articles présent dans `index.md` ne manque dans la section README si sa contribution est structurante

---

- [ ] **Unit 4: Relecture finale et diff**

**Goal:** Valider la cohérence globale du README après les corrections.

**Requirements:** R1, R2, R3, R4, R5, R6

**Dependencies:** Unit 2, Unit 3

**Files:**
- Modify: `README.md` (aucune modification attendue, lecture de validation)

**Approach:**
- Relire le README de bout en bout
- Vérifier qu'il n'y a plus d'incohérence entre les trois sources : `README.md`, `index.md`, `knowledge-base.md`
- Grep sur `2026` pour confirmer qu'aucune référence à `Mars 2026` ne subsiste comme borne de période
- Vérifier que les liens internes (`index.md`, `knowledge-base.md`, `CLAUDE.md`, `SYNTHESE-JUILLET-OCTOBRE-2025.md`) pointent encore vers des fichiers existants

**Test scenarios:**
- Test expectation: none — pas de comportement, vérification d'intégrité documentaire.

**Verification:**
- Diff git du README ne contient que les changements prévus (pas de modification accidentelle de sections hors scope)
- Tous les liens du README résolvent vers des fichiers existants du dépôt

## System-Wide Impact

- **Interaction graph:** Le README est une surface de lecture (GitHub, agents IA qui clonent le dépôt). Aucun script, aucune fiche ne parse le README, donc pas de ripple effect.
- **Unchanged invariants:** Format des fiches, structure `fiches/YYYY-MM/`, format du knowledge graph, scripts, `index.md`, `CLAUDE.md` — rien de tout cela ne change.

## Risks & Dependencies

| Risque | Mitigation |
|--------|------------|
| Rebuild KB modifie des fichiers `kb/*.md` déjà commités et produit un diff large | Accepté — c'est l'usage normal du script et le dépôt versionne déjà `kb/`. Si besoin, commit séparé pour le rebuild. |
| Le compteur `212` d'`index.md` est lui-même obsolète | Vérification croisée avec le filesystem (219 fichiers vs 212 entrées logiques). `index.md` reste la source de vérité éditoriale ; si l'écart est jugé trop grand, recalibrer `index.md` sort du scope de ce plan. |
| Nouvelle fiche ajoutée entre le rebuild KB et le commit README | Peu probable sur la durée de l'opération (< 10 min). Si cela arrive, refaire rapidement Unit 1 + Unit 2. |

## Documentation / Operational Notes

- Aucun impact opérationnel. Le README n'est ni déployé ni consommé par un pipeline.
- Commit conseillé : message unique de type `docs: actualiser README (période avril 2026, KB rebuild, auteurs)` regroupant la régénération KB + les modifications README.

## Sources & References

- `README.md` — fichier cible
- `index.md` (lignes 9-11, 520-524) — source de vérité éditoriale
- `knowledge-base.md` (ligne 3) — source des compteurs KB
- `scripts/build_knowledge_base.py` — script de régénération KB
- `CLAUDE.md` — conventions du dépôt
