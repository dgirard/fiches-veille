---
title: Modéliser un document de fact-checking / méta-analyse comme une fiche
date: 2026-07-20
category: conventions
module: fiches
problem_type: convention
component: documentation
severity: low
applies_when:
  - "La source n'est pas un article primaire mais un fact-check, une revue de synthèse ou une méta-analyse de claims sur un sujet"
  - "Le contenu porte des verdicts gradués (confirmé / partiel / spéculatif / non sourçable / auto-déclaré) qu'il faut préserver"
  - "On doit distinguer un fait vérifié d'un chiffre auto-déclaré ou d'une intention annoncée dans le GrapheDeConnaissance"
tags:
  - fiche
  - graphe-de-connaissance
  - ontologie-kg
  - fact-checking
  - affirme_que
  - epistemique
---

# Modéliser un document de fact-checking / méta-analyse comme une fiche

## Context

Le format de fiche (10 sections gelées, cf. CLAUDE.md) et l'ontologie du graphe
(`docs/reference/ontologie-kg.md`) sont pensés pour l'analyse d'**un article
primaire** — une source qui *affirme* quelque chose. Rien n'y décrit le cas où la
source est elle-même **méta** : un fact-check, une « revue de la synthèse », une
vérification de claims sur un sujet (entreprise, levée de fonds, benchmark). Là,
la valeur du document n'est pas *ce qu'il rapporte* mais *le degré de confiance
qu'il attribue* à chaque affirmation — un régime épistémique gradué (CONFIRMÉ /
PARTIELLEMENT EXACT / NON CONFIRMÉ / NON SOURÇABLE / AUTO-DÉCLARÉ). Modéliser un
tel document comme s'il s'agissait d'un article primaire aplatit cette gradation
et fait entrer dans le graphe des chiffres auto-déclarés (ex. « 100 000
utilisateurs », « 1 M$ d'ARR ») comme s'ils étaient des faits établis. Le registre
de prédicats est **fermé** et ne contient ni `confirme`, ni `réfute`, ni
`vérifie` : il faut donc une convention de repli fidèle. (Première occurrence :
fiche `delos-intelligence-fact-check-levee-2026-07-20`.)

## Guidance

Traiter le document de fact-checking comme l'**article**, et porter la gradation
épistémique dans trois endroits :

1. **Sections texte** — `Titre Article` = le titre du fact-check ; `URL` = une
   ancre canonique (site du sujet ou source primaire dominante) faute d'URL unique
   pour une synthèse ; `Authors` = « Synthèse de veille (fact-checking) » + les
   sources primaires/presse mobilisées. Conserver les **verdicts gradués tels
   quels** dans `Ton` et `Pense-betes` (« CONFIRMÉ », « auto-déclaré », « intention
   annoncée, non bouclée ») — c'est là que vit la valeur du document.

2. **Une entité `DOCUMENT` pour la synthèse.** Créer `synthèse fact-check <Sujet>`
   (type `DOCUMENT`) et lui accrocher les **méta-claims** — ce que le fact-check
   dit du *statut de vérité* d'une affirmation — via `affirme_que` → objet
   `AFFIRMATION` :

   ```
   | synthèse fact-check Delos | DOCUMENT | affirme_que | la liste des business angels est confirmée mot pour mot par le communiqué de 20VC (pas une hallucination) | AFFIRMATION | 0.95 | STATIQUE | déclaré_article |
   | synthèse fact-check Delos | DOCUMENT | affirme_que | aucune Série A n'a été bouclée à ce jour, seulement annoncée comme intention visant mars 2026 | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
   | synthèse fact-check Delos | DOCUMENT | affirme_que | l'effectif de 50 personnes n'est pas sourçable ; chiffres attestés ~20 (avril 2025) puis ~40 (fin 2025) | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
   ```

3. **Distinguer trois régimes dans les triples :**
   - **Faits vérifiés sur le sujet** → triples directs normaux
     (`Delos Intelligence | utilise | Scaleway`, `TotalEnergies | utilise | Delos`).
   - **Chiffres/affirmations auto-déclarés** → jamais en triple direct ; les
     attribuer à leur émetteur via `affirme_que` → `AFFIRMATION`
     (`Pierre de la Grand'rive | affirme_que | 1 M$ d'ARR en quelques jours pour
     Workers (auto-déclaré, non audité, ≠ ARR total) | AFFIRMATION`).
   - **Méta-verdicts** (confirmé / non sourçable / spéculatif) → portés par
     l'entité `DOCUMENT` de la synthèse (point 2).

Une **intention annoncée** (levée visée, produit à venir) ne s'écrit jamais avec
`publie` / un prédicat de fait accompli : la garder en `affirme_que` →
`AFFIRMATION` attribué à la personne qui l'annonce.

## Why This Matters

- **Le graphe reste honnête.** Sans cette convention, `Delos | mesure | 100 000
  utilisateurs` et `Delos | mesure | 1 M$ ARR` entreraient comme des faits ; la
  requalification en `affirme_que`/`AFFIRMATION` attribuée à l'émetteur préserve le
  fait que ce sont des dires d'entreprise non audités. C'est exactement la
  distinction fait/opinion que les prédicats épistémiques (`affirme_que`, `prédit`,
  `mesure`, `recommande`) existent pour capturer (cf. ontologie-kg.md, types
  épistémiques `AFFIRMATION`/`MESURE`/`CITATION`).
- **Le registre fermé n'est pas contourné.** On n'invente pas `confirme`/`réfute` :
  `affirme_que` sur une entité `DOCUMENT` est le repli fidèle. L'entité `DOCUMENT`
  de la synthèse sert d'ancre pour tout ce qui est *jugement de véracité*, sans
  polluer le sujet lui-même.
- **La leçon anti-hallucination se documente.** Un fact-check confirme parfois une
  info plausible (ici les business angels, exacts au mot près). Porter ce verdict
  positif dans le graphe (`… est confirmée … pas une hallucination`) est aussi
  utile qu'une réfutation : le réflexe est *vérifier*, pas suspecter par défaut.

## When to Apply

- Source = fact-check, revue/vérification de synthèse, méta-analyse de claims sur
  une entité (startup, levée, produit, benchmark).
- Dès qu'un chiffre est **auto-déclaré** (communiqué d'entreprise, post X) ou
  qu'une opération est **annoncée mais non bouclée** : attribuer via `affirme_que`,
  ne pas l'établir comme fait.
- **Ne s'applique pas** à un article primaire ordinaire (même s'il cite des
  chiffres d'entreprise en passant) : la lourdeur de l'entité `DOCUMENT` méta ne se
  justifie que quand le *jugement de véracité* est le cœur du document.

## Examples

Fiche de référence : `fiches/2026-07/delos-intelligence-fact-check-levee-2026-07-20.md`.

**Avant (naïf, aplati) :**

```
| Delos Intelligence | ORGANISATION | mesure | 100 000 utilisateurs | MESURE | ... |
| Delos Intelligence | ORGANISATION | mesure | 1 M$ d'ARR | MESURE | ... |
| Delos Intelligence | ORGANISATION | publie | Série A de plusieurs dizaines de M€ | EVENEMENT | ... |
```

**Après (gradation préservée) :**

```
| Pierre de la Grand'rive | PERSONNE | affirme_que | 1 M$ d'ARR en quelques jours pour Workers (auto-déclaré, non audité, ≠ ARR total) | AFFIRMATION | 0.85 | ... |
| synthèse fact-check Delos | DOCUMENT | affirme_que | aucune Série A n'a été bouclée, seulement annoncée comme intention visant mars 2026 | AFFIRMATION | 0.9 | ... |
```

Entité d'ancrage des méta-verdicts :

```
| synthèse fact-check Delos | DOCUMENT | définition | Note confrontant une veille aux sources primaires (communiqué lead, site, registres) et à la presse ; gradue les verdicts (confirmé/partiel/spéculatif/non sourçable/auto-déclaré) | AJOUT |
```

## Related

- `docs/reference/ontologie-kg.md` — registre fermé des 30 prédicats et types
  épistémiques (`AFFIRMATION`/`MESURE`/`CITATION`) ; ce doc-ci en dérive une
  convention d'usage pour les sources *méta*.
- [[Fiche]] (CONCEPTS.md) — l'unité de base dont ce cas est une variante de
  source.
