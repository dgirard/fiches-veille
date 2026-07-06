---
fiche_type: skill
skill_source: github.com/mattpocock/skills
skill_author: Matt Pocock
themes: [agents-codage-ia-skills]
source: "GitHub (Matt Pocock, mattpocock/skills)"
---
# skill-pocock-grill-with-docs-2026-06

## Veille

Fiche de **Skill** (et non d'article) : `grill-with-docs` de Matt Pocock est une technique d'interview structurée qui « cuisine » (*grill*) un plan d'architecture en le confrontant méthodiquement au vocabulaire métier du projet (glossaire `CONTEXT.md`) et aux décisions déjà documentées (ADR). Plutôt que de foncer dans l'implémentation, elle challenge les hypothèses une par une via un dialogue question/réponse, nettoie la terminologie, vérifie la cohérence avec le code réel, et capture les décisions au fil de l'eau dans les bons artefacts. Skill de conception en amont, d'inspiration Domain-Driven Design.

## Titre Article

grill-with-docs — « Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise »

## Date

2026-06-16

## URL

https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md

## Keywords

skill, grilling, interview adversariale, conception en amont, Domain-Driven Design, DDD, vocabulaire métier, glossaire, CONTEXT.md, ADR, Architecture Decision Record, bounded context, CONTEXT-MAP.md, terminologie canonique, précision du langage, vérification par les preuves, création paresseuse de fichiers, discipline documentaire, dérive de terminologie

## Authors

Matt Pocock

## Ton

Profil : skill exécutable (fichier `SKILL.md` d'instructions pour agent), voix **impérative et socratique-adversariale** (« Interview me relentlessly about every aspect of this plan »), registre technique élevé, public cible développeurs et architectes pratiquant la conception amont. Le « ton » est ici le **registre opérationnel** que la skill impose à l'agent : questionnement séquentiel (une question à la fois, on attend la réponse avant d'avancer), exigence de précision lexicale (signaler immédiatement les conflits de terminologie), posture de preuve (croiser l'affirmation avec le code réel et faire remonter les contradictions), et sobriété documentaire (capturer au fil de l'eau, créer les fichiers à la demande). Métaphore filée culinaire — *grilling*, « cuisiner » le plan pour le mettre à l'épreuve. L'autorité vient de la méthode (DDD) et de la rigueur du protocole, pas d'un argument d'auteur.

## Pense-betes

- **Nature** : skill de **conception en amont** (DDD-flavored) — avant d'écrire du code, forcer une conversation rigoureuse qui ① nettoie le vocabulaire, ② vérifie la cohérence avec le code existant, ③ documente les décisions au bon endroit et au bon niveau de granularité.
- **But anti-dérive** : prévenir les **dérives de terminologie** et les **hypothèses non vérifiées** qui coûtent cher plus tard.
- **Deux artefacts cibles** : `CONTEXT.md` (glossaire du domaine) et les **ADR** (`docs/adr/`, décisions d'architecture).
- **Critère ADR strict** : un ADR n'est créé que si les **3** conditions tiennent — décision (1) difficile à revenir en arrière, (2) surprenante sans contexte, (3) issue d'un **vrai arbitrage** avec alternatives considérées.
- **`CONTEXT.md` = glossaire métier UNIQUEMENT** — *« should be totally devoid of implementation details »* (pas de specs, pas de notes de brouillon).
- **Création paresseuse** : *« Create files lazily — only when you have something to write »* (`CONTEXT.md` au premier terme résolu ; `docs/adr/` au premier ADR nécessaire).
- **Multi-domaines** : un repo à plusieurs *bounded contexts* utilise un `CONTEXT-MAP.md` qui pointe vers le `CONTEXT.md` (et `docs/adr/`) de chaque contexte.
- **Explore avant de demander** : si une question peut être tranchée en lisant le code, l'agent explore au lieu de te la poser — il ne te fait pas perdre de temps.
- **Pourquoi c'est une fiche de skill et pas d'article** : la valeur est dans le **fonctionnement réutilisable** (déclencheur, mécanisme, artefacts, anti-patterns), pas dans une opinion datée — voir le bloc Skill ci-dessous.

## RésuméDe400mots

`grill-with-docs`, signée Matt Pocock, est une **skill** (instructions exécutables pour un agent de codage) qui transforme la phase de conception en une session d'interview rigoureuse. Son principe : quand on conçoit une fonctionnalité, le plan repose sur des hypothèses et des dépendances de design ; plutôt que de foncer dans l'implémentation, la skill « cuisine » (*grill*) le plan en le confrontant, hypothèse par hypothèse, au vocabulaire métier du projet et aux décisions déjà prises. À mesure que les décisions se cristallisent, elles sont capturées dans deux types de documents : `CONTEXT.md`, un **glossaire du domaine** (le vocabulaire métier), et les **ADR** (*Architecture Decision Records*, dans `docs/adr/`), pour les décisions d'architecture importantes.

Le fonctionnement repose sur quatre principes. **(1) Approche par interview** : les questions sont posées séquentiellement, une à la fois, et l'agent attend la réponse avant d'avancer ; si une question peut être résolue en explorant le code, il explore au lieu de demander. **(2) Précision du langage** — le cœur de la skill : signaler immédiatement les conflits de terminologie avec le glossaire existant, proposer un terme canonique quand l'utilisateur emploie un mot vague (ex. « account »), et tester les relations métier avec des scénarios concrets de cas limites. **(3) Basé sur les preuves** : croiser le comportement annoncé avec le code réel et faire remonter les contradictions. **(4) Discipline documentaire** : `CONTEXT.md` est mis à jour au fil de l'eau (pas en lot à la fin) ; un ADR n'est créé que si la décision est difficile à inverser, surprenante sans contexte, et issue d'un vrai arbitrage.

Côté règles structurelles : `CONTEXT.md` ne contient **que** le glossaire métier (aucun détail d'implémentation, spec ou brouillon) ; un repo à plusieurs domaines (*bounded contexts* au sens DDD) utilise un `CONTEXT-MAP.md` qui pointe vers le `CONTEXT.md` de chaque contexte ; les fichiers sont créés **à la demande** (création paresseuse).

En résumé, c'est une skill de conception en amont, d'inspiration Domain-Driven Design, qui force avant le code une conversation rigoureuse pour ① nettoyer le vocabulaire, ② vérifier la cohérence avec l'existant, et ③ documenter les décisions au bon endroit et au bon niveau de granularité — afin d'éviter les dérives de terminologie et les hypothèses non vérifiées qui deviennent coûteuses plus tard.

## Commentaire

*Explication pédagogique de la skill (vulgarisation « comment ça marche ») — complément des sections structurées ci-dessous.*

**En une phrase.** C'est une technique d'interview structurée pour « cuisiner » (*grill*) un plan d'architecture : on le met à l'épreuve méthodiquement en le confrontant au vocabulaire métier du projet et aux décisions déjà documentées.

**L'idée centrale.** Quand tu conçois une fonctionnalité, ton plan repose sur des hypothèses et des dépendances de design. Cette skill te fait challenger ces hypothèses **une par une**, via un dialogue question/réponse, plutôt que de foncer dans l'implémentation. À mesure que les décisions se cristallisent, elles sont capturées dans deux types de documents :

- `CONTEXT.md` → un **glossaire du domaine** (le vocabulaire métier) ;
- **ADR** (*Architecture Decision Records*, dans `docs/adr/`) → les **décisions d'architecture** importantes.

**Les 4 principes de fonctionnement.**

1. **Approche par interview** — questions posées séquentiellement, on attend ta réponse avant d'avancer ; si une question peut être résolue en explorant le code, l'agent explore au lieu de demander (il ne te fait pas perdre ton temps).
2. **Précision du langage** (le cœur du truc) — signale immédiatement les conflits de terminologie avec le glossaire existant ; propose un terme canonique quand tu emploies un mot vague ; teste les relations métier avec des scénarios concrets de cas limites (*edge cases*).
3. **Basé sur les preuves** — croise le comportement annoncé avec le code réel ; fait remonter les contradictions entre ce qui est affirmé et ce qui est effectivement implémenté.
4. **Discipline documentaire** — `CONTEXT.md` est mis à jour au fil de l'eau (pas en lot à la fin) ; un ADR n'est créé que si la décision remplit **3 critères** : coût de revirement significatif, justification non évidente qui nécessite du contexte, et vrais arbitrages avec des alternatives considérées.

**Règles structurelles.**

- `CONTEXT.md` = glossaire métier **uniquement** (pas de détails d'implémentation, ni de specs, ni de notes de brouillon).
- Pour un repo avec plusieurs domaines (*bounded contexts* au sens DDD), un `CONTEXT-MAP.md` organise la doc par contexte.
- Les fichiers sont créés **à la demande** : `CONTEXT.md` au premier terme résolu, `docs/adr/` au premier ADR nécessaire.

**En résumé.** C'est essentiellement une skill de **conception en amont** (DDD-flavored) : avant d'écrire du code, on force une conversation rigoureuse qui ① nettoie le vocabulaire, ② vérifie la cohérence avec le code existant, et ③ documente les décisions au bon endroit et au bon niveau de granularité. L'objectif est d'éviter les **dérives de terminologie** et les **hypothèses non vérifiées** qui coûtent cher plus tard.

## Lecture commentée du SKILL.md

*Annotation quasi ligne-à-ligne du source : extraits verbatim du `SKILL.md` + glose. Utile pour comprendre comment la skill est construite, pas seulement ce qu'elle fait.*

### Frontmatter

- **`name`** : l'identifiant de la skill. C'est ce que tu taperais (`/grill-with-docs`) pour l'invoquer.
- **`description`** : sert à deux choses — résumer ce que fait la skill **et** indiquer quand l'agent doit la déclencher (« Use when… »). La dernière phrase est la **condition d'activation** : quand tu veux stress-tester un plan contre le langage et les décisions documentées de ton projet.

### Bloc `<what-to-do>` — le cœur comportemental

> *« Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer. »*

- **« Interview me relentlessly »** : l'agent doit te questionner sans relâche, pas valider gentiment. Posture **adversariale assumée**.
- **« design tree / one-by-one »** : on traite l'arbre de décisions branche par branche, en résolvant les dépendances entre choix dans l'ordre (un choix peut en contraindre un autre).
- **« provide your recommended answer »** : crucial — à chaque question, l'agent ne se contente pas de demander, il **propose sa propre réponse recommandée**. Ça t'évite la page blanche et donne quelque chose à valider/réfuter.

> *« Ask the questions one at a time, waiting for feedback on each question before continuing. »*

- **Une question à la fois.** Pas de questionnaire massif : un vrai dialogue séquentiel, on attend ta réponse avant la suivante (chaque réponse peut changer les questions suivantes).

> *« If a question can be answered by exploring the codebase, explore the codebase instead. »*

- **Explorer plutôt que demander.** Si la réponse est dans le code, l'agent va la chercher lui-même au lieu de te déranger.

### Bloc `<supporting-info>` — la doc de support

**Domain awareness → structure de fichiers.** Cas standard (un seul contexte) : un `CONTEXT.md` à la racine (le glossaire) + des ADR numérotés dans `docs/adr/` (`0001-…`, `0002-…` — convention ADR classique, séquence chronologique immuable). Si un `CONTEXT-MAP.md` existe à la racine, le repo a **plusieurs contextes** (vocabulaire DDD) : chaque *bounded context* (ex. `src/ordering/`, `src/billing/`) a son propre glossaire et ses propres ADR — car le même mot peut signifier des choses différentes selon le contexte — les ADR globaux restant au niveau racine.

> *« Create files lazily — only when you have something to write. »*

- **Création paresseuse.** Pas de fichiers vides « au cas où » : `CONTEXT.md` naît à la résolution du premier terme, `docs/adr/` au premier ADR réellement nécessaire.

**Challenge against the glossary** — *« Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it? »* → conflit de terminologie = **alerte immédiate** ; c'est le mécanisme anti-dérive du vocabulaire.

**Sharpen fuzzy language** — *« You're saying 'account' — do you mean the Customer or the User? Those are different things. »* → désambiguïsation des termes fourre-tout par un **terme canonique** précis (Customer vs User = deux concepts souvent confondus).

**Discuss concrete scenarios** — *« Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts. »* → test par **cas limites** inventés (« et si on annule une commande déjà à moitié expédiée ? ») qui font sortir les définitions floues au grand jour.

**Cross-reference with code** — *« Your code cancels entire Orders, but you just said partial cancellation is possible — which is right? »* → **confrontation parole vs code**, pilier *evidence-based*.

**Update CONTEXT.md inline** — *« When a term is resolved, update `CONTEXT.md` right there. Don't batch these up. »* (format délégué à `CONTEXT-FORMAT.md`) → documentation **au fil de l'eau**, jamais en lot. Et : *« `CONTEXT.md` should be totally devoid of implementation details. … It is a glossary and nothing else. »* → **frontière stricte** : glossaire pur, pas de specs ni de brouillon.

**Offer ADRs sparingly** — *« Only offer to create an ADR when all three are true: 1. Hard to reverse 2. Surprising without context 3. The result of a real trade-off. If any of the three is missing, skip the ADR. »* (format délégué à `ADR-FORMAT.md`) → les trois conditions sont **cumulatives** ; si une seule manque, pas d'ADR. C'est le garde-fou contre la noyade documentaire.

### Ce qu'il faut retenir sur la **conception** de la skill

Au-delà du contenu, deux choix de design intéressants :

1. **Balises XML sémantiques** (`<what-to-do>`, `<supporting-info>`) — séparent l'**instruction impérative** (le comportement à adopter) de l'**information de référence** (comment faire). Pattern de prompting efficace pour Claude.
2. **Modularisation par fichiers annexes** — les formats détaillés (`CONTEXT-FORMAT.md`, `ADR-FORMAT.md`) sont sortis du `SKILL.md` principal, qui reste un **document d'orchestration concis** ; les détails sont chargés au besoin (progressive disclosure).

## Déclencheur

- **Quand l'activer** : lorsqu'on veut **éprouver un plan** (architecture, conception d'une fonctionnalité) contre le langage du projet et ses décisions documentées, *avant* d'implémenter. Texte d'origine : *« Apply this when a user wants to stress-test a plan against their project's language and documented decisions. »*
- **Entrées attendues** : un plan ou une intention de conception à challenger ; l'accès au codebase (la skill explore le code pour répondre aux questions factuelles) ; le cas échéant, un `CONTEXT.md` / `docs/adr/` déjà existants à confronter.
- **Sortie** : un plan durci par le dialogue + des artefacts de documentation (`CONTEXT.md`, ADR) mis à jour au fil de la session.

## Fonctionnement

La skill opère par **questionnement relentless** : *« Interview me relentlessly about every aspect of this plan until we reach a shared understanding. »* Les questions avancent **une à une**, en attendant le retour avant de continuer ; quand c'est possible, l'agent **explore le codebase** plutôt que de poser une question dont la réponse est dans le code.

**Quatre principes de fonctionnement :**

1. **Approche par interview** — séquentielle, interactive ; pas de questions dont la réponse est trouvable dans le code (l'agent va chercher).
2. **Précision du langage** (le cœur) — signaler immédiatement les conflits de terminologie avec le glossaire `CONTEXT.md` (avec exemples précis) ; proposer un **terme canonique** face à un vocabulaire surchargé (ex. « account ») ; éprouver les relations métier via des **scénarios de cas limites** inventés.
3. **Basé sur les preuves** — vérifier les affirmations contre l'implémentation réelle ; faire remonter les contradictions entre ce qui est annoncé et ce qui est effectif.
4. **Discipline documentaire** — mettre à jour `CONTEXT.md` **inline** (au fil de l'eau, pas en lot) ; ne créer un ADR que sous conditions strictes (voir Anti-patterns).

## Artefacts

Structure de repo type :

```
/
├── CONTEXT.md      # glossaire du domaine (vocabulaire métier UNIQUEMENT, zéro détail d'implémentation)
├── docs/adr/       # Architecture Decision Records
└── src/
```

- **`CONTEXT.md`** — glossaire métier ; créé **au premier terme résolu** ; *« totally devoid of implementation details »*.
- **`docs/adr/`** — un fichier par décision d'architecture importante ; créé **au premier ADR nécessaire**.
- **`CONTEXT-MAP.md`** (repos multi-domaines) — pointe vers le `CONTEXT.md` et `docs/adr/` de chaque *bounded context* (DDD).
- **Règle de création** : *« Create files lazily — only when you have something to write. »*

## Anti-patterns

- **Créer un ADR pour tout** : un ADR n'est justifié que si les **3** critères tiennent simultanément — (1) **difficile à inverser** (coût réel de changer de cap plus tard), (2) **surprenant sans contexte** (un lecteur futur questionnerait la décision), (3) **résultat d'un vrai arbitrage** (des alternatives existaient et ont été pesées). Une décision triviale ou réversible ne devient pas un ADR.
- **Polluer `CONTEXT.md`** avec des détails d'implémentation, des specs ou des notes de brouillon : il doit rester un **glossaire métier pur**.
- **Documenter en lot à la fin** : la capture doit être **inline**, sinon les décisions se perdent.
- **Créer les fichiers en avance** (`CONTEXT.md`/`docs/adr/` vides « au cas où ») : violation de la création paresseuse.
- **Poser des questions dont la réponse est dans le code** : l'agent doit explorer d'abord ; sinon il fait perdre du temps.
- **Foncer dans l'implémentation** sans avoir nettoyé le vocabulaire ni vérifié les hypothèses — c'est précisément ce que la skill cherche à empêcher.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Matt Pocock | PERSONNE | a_créé | grill-with-docs | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| grill-with-docs | METHODOLOGIE | s_applique_à | éprouver un plan d'architecture avant l'implémentation | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| grill-with-docs | METHODOLOGIE | utilise | interview séquentielle (une question à la fois) | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| grill-with-docs | METHODOLOGIE | s_inspire_de | Domain-Driven Design | METHODOLOGIE | 0.88 | ATEMPOREL | inféré |
| grill-with-docs | METHODOLOGIE | améliore | précision et cohérence de la terminologie métier | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| grill-with-docs | METHODOLOGIE | réduit | dérives de terminologie et hypothèses non vérifiées | CONCEPT | 0.90 | ATEMPOREL | inféré |
| grill-with-docs | METHODOLOGIE | permet | capture du vocabulaire métier dans CONTEXT.md | DOCUMENT | 0.90 | ATEMPOREL | déclaré_article |
| grill-with-docs | METHODOLOGIE | recommande | ne créer un ADR que si décision irréversible, surprenante et issue d'un vrai arbitrage | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| grill-with-docs | METHODOLOGIE | recommande | Create files lazily — only when you have something to write | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| grill-with-docs | METHODOLOGIE | affirme_que | CONTEXT.md should be totally devoid of implementation details | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| CONTEXT.md | DOCUMENT | est_instance_de | glossaire du domaine | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| ADR | DOCUMENT | fait_partie_de | docs/adr/ | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| CONTEXT-MAP.md | DOCUMENT | référence | CONTEXT.md de chaque bounded context | DOCUMENT | 0.87 | ATEMPOREL | déclaré_article |
| grill-with-docs | METHODOLOGIE | s_applique_à | repos multi-domaines (bounded contexts DDD) | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| grill-with-docs | METHODOLOGIE | utilise | balises XML sémantiques séparant instruction et information de référence | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| grill-with-docs | METHODOLOGIE | utilise | modularisation par fichiers annexes (CONTEXT-FORMAT.md, ADR-FORMAT.md) | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| grill-with-docs | METHODOLOGIE | catégorie | Skill d'ingénierie — conception en amont, DDD-flavored | AJOUT |
| grill-with-docs | METHODOLOGIE | fonctionnement | Interview séquentielle + 4 principes (interview, précision du langage, preuves, discipline documentaire) | AJOUT |
| Matt Pocock | PERSONNE | rôle | Auteur de skills d'ingénierie (repo mattpocock/skills) | AJOUT |
| CONTEXT.md | DOCUMENT | nature | Glossaire du vocabulaire métier (sans détails d'implémentation) | AJOUT |
| ADR | DOCUMENT | nature | Architecture Decision Record (docs/adr/), créé sous 3 critères | AJOUT |
| CONTEXT-MAP.md | DOCUMENT | rôle | Pointe vers les CONTEXT.md/docs/adr de chaque bounded context | AJOUT |
| Domain-Driven Design | METHODOLOGIE | rôle | Inspiration (bounded contexts, vocabulaire de domaine) | AJOUT |
