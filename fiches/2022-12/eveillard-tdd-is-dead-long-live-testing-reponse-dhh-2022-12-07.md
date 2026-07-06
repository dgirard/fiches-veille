---
themes: [qualite-securite]
source: "mathieueveillard.com (Mathieu Eveillard)"
---
# eveillard-tdd-is-dead-long-live-testing-reponse-dhh-2022-12-07

## Veille
**Mathieu Eveillard** publie sur son blog personnel le **7 décembre 2022** (dernière mise à jour 17 mars 2025) une **contre-argumentation point à point** au célèbre essai de **David Heinemeier Hansson (DHH)** *"TDD is dead. Long live testing."* (RailsConf 2014). Article catégorisé **craft / best-of**, position d'**artisan logiciel** qui défend le **Test-Driven Development** sans dogmatisme. **Distinction-pivot** que DHH manque selon Eveillard : ***"Test-first"*** (écrire tous les tests avant le moindre code) vs ***"Test-Driven Development"*** (les tests me **guident** dans l'écriture du code, donc j'écris à chaque fois un peu de code *"en réaction"* à un nouveau test). DHH critique le *Test-first* en l'appelant TDD — confusion qui **cache une tout autre façon de programmer**. **Réponses point à point** : (1) *"TDD as hammer to beat down the nonbelievers"* — Eveillard concède le point déontologique mais redéfinit *"bon code"* : pas seulement absence de bugs mais **tests unitaires fins** documentant le comportement au plus bas niveau, co-localisés avec le code, **filet de sécurité** ; (2) *"Rebalance from unit to system"* — TDD **ne dit rien** des tests système et **ne dit pas** qu'il n'y a rien en dehors du TDD ; tests système ne **remplacent pas** unitaires (impôt sur le revenu en e2e n'a aucun sens) ; **pyramide de tests** — chaque type apporte sa pierre, unitaires pour feedback **millisecondes** + détection bug précoce ; (3) *"Horrendous monstrosities of architecture (service objects, command patterns)"* — Eveillard répond qu'il **ne connaît pas ces effets en programmation fonctionnelle**, donc l'effet est probablement dû à la **POO**, pas au TDD ; mais concède que trop d'injection de dépendances peut coupler test et implémentation. **Conclusion équilibrée** : *"Le TDD n'est pas une religion, c'est un outil"*. Le TDD se prête particulièrement bien au **code du domaine** (noyau fonctionnel d'un *bounded context*, *cœur de l'hexagone*) — moteur de calcul, règles de gestion fines, cas limites — ***"30% au plus de la codebase"***. Mention de la **Loi de l'Instrument** (si l'outil n'aide pas, c'est qu'on tombe dedans). **Pertinence dossier** : article **craft hors-corpus IA** mais à archiver pour positionner les débats actuels sur les coding agents (Beck *Augmented Coding Beyond Vibes* 2025-06-25, Vibe Coding vs TDD, Frizzo *writing muscle atrophy*) dans la lignée historique des débats craft autour du TDD. À mobiliser comme **fond de bibliothèque** pour formations.

## Titre Article
TDD is dead. Long live testing. (Une contre-argumentation point à point à l'article phare de David Heinemeier Hansson, détracteur du Test-driven development)

## Date
2022-12-07

## URL
https://www.mathieueveillard.com/blog/tdd-is-dead-long-live-testing

## Keywords
Mathieu Eveillard, TDD, Test-driven development, contre-argumentation DHH, David Heinemeier Hansson, TDD is dead long live testing 2014, Test-first vs Test-driven development distinction, tests unitaires bas niveau, filet de sécurité, pyramide de tests, feedback millisecondes, détection bug précoce, programmation fonctionnelle, injection de dépendances, couplage test implémentation, code du domaine, bounded context, cœur de l'hexagone, hammer to beat down nonbelievers, rebalance from unit to system, horrendous monstrosities of architecture, service objects command patterns, religion vs outil, Loi de l'Instrument, 30 pourcent codebase, Glenn Gould pianiste, craft, best-of, artisanat logiciel, blog Mathieu Eveillard, 7 décembre 2022, mise à jour 17 mars 2025, articulation avec débats coding agents 2025-2026, Kent Beck Augmented Coding Beyond Vibes

## Authors
**Mathieu Eveillard** — développeur / coach craft / formateur (blog personnel mathieueveillard.com, services *Accompagnement* et *Office hours*). Identité publique : *artisan logiciel* avec une pratique pédagogique autour du TDD, du DDD et du craft. Newsletter hebdomadaire (*"Chaque mercredi, une idée pour démarrer la journée"*).

## Ton
**Profil** : Article blog craft individuel, format long-form essai polémique mesuré, ton d'**artisan logiciel humble mais ferme**. Public cible : développeurs intermédiaires à seniors, tech leads, formateurs craft, lecteurs DHH/Rails curieux de l'autre côté de l'argument. Public secondaire : managers qui essaient de comprendre les débats internes équipe sur TDD.

**Style** : Voix première personne en français, **registre conversationnel courtois** (*"je doute que le monsieur attende quelque réponse de ma part"*), structuré en **3 sections** correspondant aux 3 citations DHH choisies. Pas d'ad hominem : Eveillard reconnaît DHH comme *"un personnage aux multiples facettes"* (créateur Ruby on Rails + vainqueur 24h du Mans), salue ses idées *"iconoclastes"*, mais réfute fermement les conclusions. **Argumentation point à point** dans la grande tradition rhétorique. Métaphores soignées (Glenn Gould pianiste non-académique, *cœur de l'hexagone*, *cœur du réacteur*).

**Aphorismes-clés** :
- ***"Le TDD n'est pas une religion, c'est un outil."*** (la conclusion-pivot).
- ***"Garder à l'esprit que je peux me tromper, et que ce qui est bon pour moi ne l'est pas forcément pour un autre."*** (l'humilité de l'artisan).
- ***"Plus un bug est détecté tôt, moins il coûte cher."*** (la justification économique du TDD).
- ***"Au final, cela ne représente qu'une petite partie de la codebase, 30% au plus."*** (le périmètre raisonnable du TDD).

**Métaphores travaillées** :
- ***Filet de sécurité*** — les tests comme filet protégeant des régressions.
- ***Pyramide de tests*** — chaque type de tests apporte sa pierre à l'édifice (référence Mike Cohn).
- ***Cœur de l'hexagone / cœur du réacteur*** — référence à l'**hexagonal architecture** (Alistair Cockburn) — le noyau fonctionnel d'un bounded context.
- ***Glenn Gould pianiste non-académique*** — analogie artistique : un grand interprète peut sortir des canons académiques tout en produisant un résultat magistral. Permet à Eveillard de concéder à DHH que le **résultat compte avant tout**.
- ***Loi de l'Instrument*** — si l'outil n'aide pas, c'est qu'on est tombé dans le piège de Maslow (*"si l'on tient un marteau, tout ressemble à un clou"*).

**Position épistémique** : **équilibrée et auto-critique**. Eveillard :
1. Concède des points à DHH (déontologie, pas montrer du doigt, résultat compte).
2. **Lève la confusion** Test-first vs TDD.
3. Limite le **périmètre du TDD à 30% de la codebase** (code domaine).
4. Refuse simultanément le **dogmatisme TDD** et le **rejet TDD**.

**Autorité** : construite par (a) la **précision technique** (distinctions Test-first/TDD, hexagonal, bounded context, FP), (b) la **rigueur rhétorique** point à point sans paille, (c) la **humilité explicite** (*"je peux me tromper"*), (d) la **références internes blog** (DDD stratégique vs tactique, DevOps malentendu) qui montrent un corpus cohérent. Limite : **autorité de blog individuel** sans validation institutionnelle ou empirique.

## Pense-betes

- **Date / source** : **7 décembre 2022** (initial), **17 mars 2025** (dernière mise à jour). Blog personnel **mathieueveillard.com**. Catégories : `craft`, `best-of`.
- **Auteur** : **Mathieu Eveillard** — développeur / coach craft / formateur.
- **Cible** : DHH, *"TDD is dead. Long live testing."* (RailsConf 2014, post Signal v Noise).
- **Thèse-pivot** : ***Le TDD n'est pas une religion, c'est un outil***. Et DHH critique en réalité le ***Test-first***, pas le **TDD**.

### La distinction-pivot Eveillard

| Concept | Définition |
|---------|-----------|
| **Test-first** | J'écris **tous** les tests **avant** d'écrire la moindre ligne de code |
| **Test-Driven Development** | Les tests me **guident** dans l'écriture du code — j'écris à chaque fois un peu de code **en réaction** à un nouveau test |

> *"Dommage que cette confusion ne soit jamais levée, car elle cache une tout autre façon de programmer."*

### Les 3 réfutations point à point

#### (1) *"TDD as a hammer to beat down the nonbelievers"*

**DHH** : TDD utilisé comme marteau pour montrer du doigt les non-croyants, les déclarer non-professionnels.

**Eveillard concède** : pas de sens à montrer du doigt, oppose à l'humilité de l'artisan.

**Mais redéfinit "bon code"** :
- Au-delà de l'absence de bugs ;
- **Tests unitaires** documentant le comportement au plus bas niveau ;
- **Co-localisés** avec le code ;
- **Filet de sécurité** — *"Plus les mailles sont fines, mieux on évite les régressions"*.

#### (2) *"Rebalance the testing spectrum from unit to system"*

**DHH** : passer des tests unitaires (avec mocks) aux tests système.

**Eveillard répond** :
- TDD **n'interdit rien d'autre** que les tests unitaires.
- Tests système ne **remplacent pas** les unitaires (impôt sur le revenu en e2e = absurde).
- **Pyramide de tests** — chaque type apporte sa valeur :
  - Unitaires = feedback en **millisecondes** → guide l'écriture du code par TDD ;
  - Détection bug précoce → moindre coût.

**Sur l'architecture** : *"horrendous monstrosities (service objects, command patterns)"* — Eveillard ne connaît pas ces effets en **programmation fonctionnelle**, donc imputable à la **POO**, pas au TDD.

#### (3) *"I do not write software test-first"*

**DHH** : utilise *"Test first"* alors que titre annonce TDD.

**Eveillard pointe** la **confusion sémantique** Test-first / TDD comme l'erreur fondamentale de l'argumentaire DHH.

### Le périmètre raisonnable du TDD

> *"Le TDD se prête particulièrement bien au code du domaine, le noyau fonctionnel d'un bounded context. Le coeur de l'hexagone, le coeur du réacteur. Un moteur de calcul, des règles de gestion fines, des cas limites à tout-va. Là, je ne sais pas faire autrement qu'en TDD. Mais au final, cela ne représente qu'une petite partie de la codebase, 30% au plus."*

| Code | TDD pertinent ? |
|------|----------------|
| Domaine / règles métier / moteur calcul | **OUI fortement** |
| Glue code / orchestration / IO | Moins |
| UI / framework boilerplate | Pas obligatoire |
| **Estimation Eveillard** | **30% codebase max** |

### Articulation dossier veille

#### Pertinence pour le corpus IA / coding agents 2025-2026

L'article est de **2022** (donc avant l'explosion coding agents) mais **résonne** avec les débats actuels :

- **Kent Beck — Vibe Coding vs TDD** (2024-10-17) : Beck observe que vibe coding et TDD ne s'excluent pas — le TDD reste pertinent pour le code du domaine, exactement la position Eveillard.
- **Beck — Augmented Coding Beyond Vibes** (2025-06-25) : la position *"augmented coding"* repose sur des **garde-fous** (tests) que TDD fournit naturellement.
- **Frizzo** *Year With Claude Code* (2026-05-05) : *"writing muscle atrophy"* — préserver une pratique de TDD est précisément un antidote à l'atrophie de la pratique manuelle.
- **Osmani Cognitive Surrender** (2026-05-05) : *"PRs ~100 lignes max"*, **solo keyboard time** — converge avec l'idée Eveillard que le TDD garde le développeur **dans la pratique méthodologique du métier**.
- **Lattice** (2026-05-05) : Atoms / Molecules / Refiners — granularité fine, exactement ce que TDD encourage.

#### Convergence "outil pas religion"

- **Eveillard** : *"Le TDD n'est pas une religion, c'est un outil."*
- **Karpathy** (2026-04-29) : *"jagged intelligence"* — outil avec frontières d'efficacité.
- **DORA ROI 2026** (2026-04-21) : *"all models are wrong but useful"* — humilité méthodologique.
- **Talisman Ontology Pipeline Refresh** (2026-05-04) : *"the work cannot be skipped"* — méthodologie comme outil disciplinaire.
- → **Convergence éthique** : refuser le **dogmatisme** ET le **rejet** d'un outil méthodologique.

#### Convergence "périmètre limité"

- **Eveillard** : TDD = 30% codebase max (code domaine).
- **Stanford** (citée DORA) : 35-40% productivity greenfield vs ≤10% brownfield — **distribution inégale par contexte**.
- **Ng The Batch n°350** (2026-04-24) : Frontend > Backend > Infra > Recherche — **acceleration différentielle par contexte**.
- → **Convergence** : **aucun outil méthodologique n'est universellement applicable** — toujours évaluer le **périmètre pertinent**.

### Limites à signaler

- **Article hors-corpus IA** stricto sensu — focus craft / TDD historique. Pertinent indirectement.
- **Pas de chiffres empiriques** — argumentation conceptuelle, pas étude.
- **Pas d'engagement avec coding agents** dans la version 2025 (la mise à jour mars 2025 ne semble pas avoir intégré le débat IA/agents).
- **Périmètre 30%** est une **estimation** non sourcée par Eveillard — discutable selon contexte (un compilateur peut être 80% domaine).
- **Frame fortement orienté FP/hexagonal** — peut paraître dogmatique pour les développeurs fortement OOP/Rails.
- **N'aborde pas** le débat **CI/CD impact testing strategy** que d'autres auteurs (DORA notamment) jugent critique.

### À mobiliser pour

- **Formations craft / TDD internes** : matériel pédagogique français de référence.
- **Débats équipe sur TDD** : argumentaire structuré pour clarifier *Test-first vs TDD*.
- **Articulation avec corpus 2026 coding agents** : positionner les débats actuels (vibe coding, agents, AI-augmented) dans la **continuité historique** des débats craft.
- **Sourcing** : aphorisme *"Le TDD n'est pas une religion, c'est un outil"* — formule synthétique mobilisable.

## RésuméDe400mots

**Mathieu Eveillard** publie le **7 décembre 2022** (dernière mise à jour 17 mars 2025) sur son blog personnel une **contre-argumentation point à point** à l'essai célèbre de **David Heinemeier Hansson** (DHH) *"TDD is dead. Long live testing."* (2014). Article catégorisé `craft / best-of`.

**Distinction-pivot** que DHH manque selon Eveillard : ***Test-first*** (écrire tous les tests avant le moindre code) vs ***Test-Driven Development*** (les tests me **guident** dans l'écriture du code, j'écris à chaque fois un peu de code *en réaction* à un nouveau test). DHH critique en réalité le **Test-first** en l'appelant TDD — confusion qui *"cache une tout autre façon de programmer"*.

**Trois réfutations** : (1) *TDD as hammer to beat down the nonbelievers* — Eveillard concède le point déontologique mais redéfinit *"bon code"* comme tests unitaires fins, co-localisés, filet de sécurité ; (2) *Rebalance from unit to system* — TDD **ne dit rien** des tests système et **ne dit pas** qu'il n'y a rien en dehors du TDD ; tests système **ne remplacent pas** unitaires (impôt sur le revenu en e2e = absurde) ; **pyramide de tests** — unitaires pour feedback millisecondes + détection bug précoce ; (3) *Horrendous monstrosities of architecture (service objects, command patterns)* — Eveillard ne connaît pas ces effets en **programmation fonctionnelle**, donc imputable à la POO pas au TDD.

**Conclusion équilibrée** : ***"Le TDD n'est pas une religion, c'est un outil."*** Le TDD se prête particulièrement bien au **code du domaine** (noyau fonctionnel d'un *bounded context*, *cœur de l'hexagone*) — moteur de calcul, règles de gestion fines, cas limites — soit ***"30% au plus de la codebase"***. Mention de la **Loi de l'Instrument** (si l'outil n'aide pas, c'est qu'on est tombé dans le piège du marteau).

**Pertinence dossier veille IA** : article **craft hors-corpus IA** stricto sensu mais résonne avec **Kent Beck** (Vibe Coding vs TDD 2024-10 + Augmented Coding 2025-06), **Frizzo** *writing muscle atrophy*, **Osmani Cognitive Surrender* (PRs 100 lignes max + solo keyboard time), **Lattice** (granularité fine atoms/molecules). **Convergence éthique** *"outil pas religion"* avec **Karpathy** (jagged intelligence), **DORA** (*"all models are wrong but useful"*), **Talisman** (*"the work cannot be skipped"*). **Convergence périmètre limité** avec **Stanford 35-40% greenfield vs ≤10% brownfield** et **Ng** *Frontend > Backend > Infra > Recherche*.

À mobiliser pour formations craft internes, débats équipe sur TDD, articulation avec corpus 2026 coding agents, sourcing aphorisme synthétique.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Mathieu Eveillard | PERSONNE | publie | TDD is dead. Long live testing. (réponse à DHH) | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Mathieu Eveillard | PERSONNE | s_oppose_à | David Heinemeier Hansson (DHH) | PERSONNE | 0.96 | DYNAMIQUE | déclaré_article |
| DHH | PERSONNE | publie | TDD is dead. Long live testing. (article original, 2014) | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Test-first | METHODOLOGIE | est_variante_de | Test-Driven Development | METHODOLOGIE | 0.96 | ATEMPOREL | déclaré_article |
| Mathieu Eveillard | PERSONNE | affirme_que | DHH critique Test-first en l'appelant TDD | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |
| Mathieu Eveillard | PERSONNE | affirme_que | le TDD n'est pas une religion, c'est un outil | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| TDD | METHODOLOGIE | s_applique_à | code du domaine, bounded context, cœur hexagone | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Mathieu Eveillard | PERSONNE | affirme_que | le code domaine TDD-pertinent représente 30% de la codebase au plus | AFFIRMATION | 0.91 | ATEMPOREL | déclaré_article |
| Tests unitaires | CONCEPT | permet | feedback millisecondes + détection bug précoce | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Mathieu Eveillard | PERSONNE | affirme_que | les tests système ne remplacent pas les tests unitaires | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Tests unitaires + intégration + acceptance + e2e | CONCEPT | fait_partie_de | Pyramide de tests | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Programmation fonctionnelle | METHODOLOGIE | réduit | service objects + command patterns monstrosities | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| Trop d'injection de dépendances | CONCEPT | permet | couplage test implémentation | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Loi de l'Instrument | CONCEPT | s_applique_à | TDD utilisé inappropriément | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Bilan Eveillard | CONCEPT | converge_avec | Beck Vibe Coding vs TDD, Beck Augmented Coding, Frizzo writing muscle, Osmani Cognitive Surrender | CONCEPT | 0.90 | DYNAMIQUE | inféré |
| Position outil_pas_religion | CONCEPT | converge_avec | Karpathy jagged intelligence, DORA all models wrong, Talisman work cannot be skipped | CONCEPT | 0.89 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Mathieu Eveillard | PERSONNE | rôle | Développeur / coach craft / formateur français, blog personnel mathieueveillard.com, services Accompagnement et Office hours, newsletter hebdomadaire | AJOUT |
| David Heinemeier Hansson (DHH) | PERSONNE | rôle | Créateur Ruby on Rails, fondateur Basecamp/HEY, vainqueur 24h du Mans 82e édition, auteur essai "TDD is dead. Long live testing." (2014) | AJOUT |
| Test-Driven Development | METHODOLOGIE | définition | Méthodologie où les tests guident l'écriture du code — j'écris à chaque fois un peu de code "en réaction" à un nouveau test. À distinguer de Test-first (écriture tous tests avant code) | AJOUT |
| Test-first | METHODOLOGIE | définition | Pratique d'écriture de tous les tests avant la moindre ligne de code. Confondu avec TDD par DHH 2014, distinction levée par Eveillard 2022 | AJOUT |
| "Le TDD n'est pas une religion, c'est un outil" | CONCEPT | source | Aphorisme conclusion Eveillard — refus simultané du dogmatisme TDD et du rejet TDD. Position d'artisan logiciel | AJOUT |
| Pyramide de tests | CONCEPT | définition | Modèle Mike Cohn — tests unitaires (base, nombreux, rapides) > intégration > acceptance > e2e (sommet, peu nombreux, lents). Eveillard mobilise pour réfuter "rebalance from unit to system" | AJOUT |
| Code domaine / bounded context / cœur hexagone | CONCEPT | définition | Référence DDD (Domain-Driven Design) + hexagonal architecture (Cockburn) — noyau fonctionnel d'une application. Eveillard estime ce code à 30% max de codebase et y voit le périmètre principal du TDD | AJOUT |
| Loi de l'Instrument | CONCEPT | définition | Concept Maslow ("si l'on tient un marteau, tout ressemble à un clou") — Eveillard l'applique au TDD : si l'outil n'aide pas, on est tombé dans la Loi de l'Instrument | AJOUT |
| 30% codebase max TDD | CONCEPT | source | Estimation Eveillard du périmètre code domaine où le TDD est pertinent. À adapter selon contexte (compilateur peut être 80% domaine) | AJOUT |
| Article DHH 2014 "TDD is dead" | DOCUMENT | description | Essai polémique David Heinemeier Hansson 2014 contre le Test-Driven Development, déclarant la mort du TDD. Cible de la contre-argumentation Eveillard 2022. Confond Test-first et TDD selon Eveillard | AJOUT |
| craft / artisanat logiciel | CONCEPT | description | Mouvement post-Agile valorisant la qualité du code, les pratiques techniques (TDD, refactoring, pair programming) et la responsabilité individuelle de l'artisan. Position Eveillard et corpus FR | AJOUT |
| Articulation TDD / coding agents 2026 | CONCEPT | description | Pertinence indirecte article 2022 pour corpus IA 2025-2026 : Beck Vibe Coding vs TDD, Beck Augmented Coding, Frizzo writing muscle atrophy, Osmani Cognitive Surrender — TDD comme antidote méthodologique à l'atrophie pratique manuelle | AJOUT |
