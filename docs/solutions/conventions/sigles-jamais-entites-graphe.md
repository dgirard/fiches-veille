---
title: Ne jamais typer un sigle nu comme entité du GrapheDeConnaissance
date: 2026-08-02
category: conventions
module: fiches
problem_type: convention
component: documentation
severity: high
applies_when:
  - "Une entité du GrapheDeConnaissance porte un nom qui est un sigle (ACP, UCP, MCP, ACS, AP2…)"
  - "Plusieurs entités distinctes du corpus peuvent revendiquer le même sigle"
  - "Un sujet ou un objet de triple contient une conjonction ou une virgule (« X et Y », « A, B, C »)"
  - "On relit le GrapheDeConnaissance d'une fiche avant commit"
tags:
  - graphe-de-connaissance
  - ontologie-kg
  - entity-resolution
  - homonymie
  - sigles
  - knowledge-base-generation
  - entity-aliases
---

# Ne jamais typer un sigle nu comme entité du GrapheDeConnaissance

## Contexte

En mettant en fiche une note sur l'homonymie du sigle « ACP » (trois protocoles
sans rapport : **Agent Client Protocol** de Zed, **Agentic Commerce Protocol**
d'OpenAI/Stripe, **Agent Communication Protocol** d'IBM/BeeAI), une vérification
du corpus a montré que le piège décrit par la note était **déjà refermé sur le
dépôt** :

- le sigle nu `ACP` était typé comme entité, sujet de triples dans deux fiches ;
- une variante `Agentic Commerce Protocol (ACP)` coexistait dans une troisième —
  soit **trois noms pour un seul protocole** ;
- et surtout, `kb/Agentic-Commerce-Protocol.md` portait depuis février
  `Google | a_créé | Agentic Commerce Protocol` avec une **confiance de 0,99**,
  alors que ce protocole est d'OpenAI et Stripe et que celui de Google est UCP.

Le vecteur de l'erreur est instructif : le titre de l'article source disait
« les protocoles **ACP et UCP de Google** ». Le complément qualifiait UCP seul, il
a été appliqué aux deux. C'est la **proximité des sigles** qui a rendu la
mélecture possible — deux noms complets côte à côte ne se seraient pas confondus.

## Règle

**L'entité est le nom complet. Le sigle n'est jamais un nom d'entité.**

Trois corollaires, tous vérifiables au relecture d'un tableau de triples :

1. **Jamais de sigle nu** en sujet ou en objet — `| ACP |`, `| UCP |`, `| ACS |`.
2. **Jamais de variante parenthésée** — `Agentic Commerce Protocol (ACP)` est un
   *troisième* nom, pas une aide à la lecture. Le sigle vit dans la prose
   (`## Veille`, `## Keywords`, `## Pense-betes`), où il est légitime et utile ;
   il ne franchit pas la frontière du tableau.
3. **Jamais d'entité composée** — un nom qui contient une conjonction ou une
   virgule n'est pas un nom d'entité. `ACP et UCP` devient deux triples ;
   `MCP, Agent2Agent, REST API` en devient trois.

Quand un sigle mérite d'être conservé, il se déclare comme **attribut** de
l'entité canonique, pas comme entité :

```markdown
| Agent Client Protocol | TECHNOLOGIE | définition | Protocole ouvert reliant un client à un agent ; alias « ACP » (homonyme, à ne jamais employer seul) | AJOUT |
```

## Pourquoi c'est important

Le pipeline possède deux garde-fous d'entity resolution. **Aucun des deux
n'attrape une collision de sigle** — c'est le seul mode d'échec qui passe entre
les deux, silencieusement.

### Le suffixe de type ne peut rien

Les pages sont keyées par le couple `(nom, type)`
(`scripts/build_knowledge_base.py:88`), et un nom porté par plusieurs types
majeurs reçoit un suffixe déterministe (`Cursor-organisation` /
`Cursor-technologie`, cf. [[alias-entites-et-bornage-kb]]). Ce mécanisme résout
les homonymes **de types différents**.

Or Agent Client Protocol et Agentic Commerce Protocol sont **tous deux
`TECHNOLOGIE`**. Typés `ACP`, ils produisent la **même clé** — et fusionnent en
une seule page mêlant deux sujets sans aucun rapport. Le suffixe de type est
inopérant par construction : il discrimine sur le type, et le type est identique.

### Le détecteur de quasi-doublons ne peut rien non plus

`_quasi_key` normalise en minuscules, sans accents, séparateurs supprimés
(`re.sub(r"[\s\-_/]+", "", s)`, `scripts/build_knowledge_base.py:346`) puis
regroupe les noms **distincts** qui se ressemblent.

Sur les noms complets, il compare `agentclientprotocol` et
`agenticcommerceprotocol` : deux clés différentes, aucun signalement — et c'est
correct, ce sont bien deux entités. Mais si les deux sont typées `ACP`, il n'y a
plus **qu'une seule entité** dans le graphe : il n'y a rien à comparer, donc rien
à signaler. Le détecteur voit la **fragmentation** (un objet éclaté en plusieurs
noms) ; il est structurellement aveugle à la **conflation** (plusieurs objets
sous un seul nom).

### Les deux dégâts

- **Conflation** — deux sujets fusionnés en une page, sans erreur ni warning.
  Le build passe au vert. C'est le cas grave : le graphe affirme des choses
  fausses avec la confiance des triples d'origine.
- **Fragmentation** — `ACP` + `Agentic Commerce Protocol (ACP)` +
  `Agentic Commerce Protocol` = relations dispersées sur trois nœuds. Un `grep`
  sur le nom canonique en rate les deux tiers, et la page canonique paraît
  maigre alors que l'information existe.

`entity_aliases.tsv` est le garde-fou complémentaire pour les variantes qui
passeraient malgré tout — mais il ne sauve que la fragmentation. Sa directive
`FUSION` fusionne ; face à une conflation il faudrait **scinder**, ce qu'aucune
directive ne fait. D'où la règle en amont : le problème se prévient à l'écriture,
il ne se rattrape pas au build.

## Quand l'appliquer

- À l'écriture de la section `## GrapheDeConnaissance` d'une fiche.
- À la relecture avant commit, en balayant la colonne Sujet et la colonne Objet.
- Chaque fois qu'un sigle apparaît dans le titre de l'article source : c'est le
  signal qu'il va vouloir descendre dans le graphe.
- Sur un sigle déjà connu du corpus, vérifier qu'il ne désigne pas déjà autre
  chose : `grep -rn "| SIGLE |" fiches/`.

## Exemples

Avant — trois noms pour un protocole, une entité composée, un sigle nu :

```markdown
| OpenAI | ORGANISATION | a_créé | Agentic Commerce Protocol (ACP) | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| ACP | TECHNOLOGIE | mesure | commission de 4% par transaction | MESURE | 0.98 | DYNAMIQUE | déclaré_article |
| Amazon | ORGANISATION | s_oppose_à | ACP et UCP | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| UCP | TECHNOLOGIE | utilise | MCP, Agent2Agent, REST API | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
```

Après — un nom canonique par entité, conjonctions défaites :

```markdown
| OpenAI | ORGANISATION | a_créé | Agentic Commerce Protocol | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Agentic Commerce Protocol | TECHNOLOGIE | mesure | commission de 4% par transaction | MESURE | 0.98 | DYNAMIQUE | déclaré_article |
| Amazon | ORGANISATION | s_oppose_à | Agentic Commerce Protocol | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Amazon | ORGANISATION | s_oppose_à | Universal Commerce Protocol | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Universal Commerce Protocol | TECHNOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Universal Commerce Protocol | TECHNOLOGIE | utilise | Agent2Agent | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Universal Commerce Protocol | TECHNOLOGIE | utilise | REST API | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
```

Effet mesuré de la normalisation sur les trois fiches concernées, après
régénération : Universal Commerce Protocol passe de 15 à 22 relations, Agentic
Commerce Protocol de 8 à 11 (sur 5 fiches sources au lieu de 4), et Model Context
Protocol de 15 à 16 — l'usage de MCP par UCP, jusque-là noyé dans une entité
composée, rejoint enfin la page de l'entité majeure.

## Voir aussi

- [[alias-entites-et-bornage-kb]] — suffixe de type, table `entity_aliases.tsv`,
  rapport de quasi-doublons : les garde-fous que cette règle complète par l'amont.
- `docs/reference/ontologie-kg.md` — règles de désambiguïsation des types
  (ORGANISATION vs TECHNOLOGIE, versions de produits).
- `scripts/entity_aliases.tsv` — directives `FUSION` / `DISTINCT` pour les
  variantes résiduelles.
