---
themes: [agents-codage-ia-skills, qualite-securite]
source: "LinkedIn (slides Dev With AI)"
---
# bartaguiz-velocite-harness-engineering-2026-10-15

## Veille

Support de talk de **Dorra Bartaguiz** (CTO, **Arolla**), présenté à la conférence **Dev With AI** et publié en PDF sur LinkedIn le **15 octobre 2026** ; **61 slides**, en français avec des exemples en anglais. Thèse : quand l'IA fait exploser la vélocité, la qualité se reprend par les pratiques *craft* outillées autour du modèle, le *harness engineering*.

**(1)** Le goulot reste la relecture : plus de **80 %** des développeurs déclarent un gain de productivité (DORA 2024-2025), mais lire le code pèse plus de **10:1** face à l'écriture (Robert C. Martin) et environ **70 %** du temps contre **5 %** (Minelli, Mochi, Lanza, 2015). **(2)** Un cas réel, le calcul d'une date d'invitation à un dépistage médical, généré d'un seul prompt : l'agent annonce **100 %** de couverture, l'oratrice en mesure **33 %** (95 % sur le domaine), relève neuf *smells* et obtient un score de *mutation testing* de **13,82 %** ; d'où *« Mutation Testing : détecteur de mensonges des tests générés par IA »*. **(3)** Définition : *« Harness = tout ce qu'on ajoute autour du modèle pour espérer un meilleur résultat de génération »*, *« AI Agent = Model + Harness »*. **(4)** Le même cas refait en suivant le SDLC craft : exploration du langage du domaine, *Example Mapping*, scénarios Given/When/Then, tests, TDD *« as a controlling practice »*, refactoring vers DDD et hexagonal. **(5)** Extension au PDLC, workflow d'agents spécialisés, *loop engineering* et formule *« Software factories = Loop Engineering + Harness Engineering + Supervision humaine »*.

Rejoint [[osmani-agentic-verification-2026-10-14]] sur la vérification comme goulot.

## Titre Article

Quand la vélocité explose avec l'IA, place au "Harness Engineering" !

## Date

2026-10-15

## URL

https://lnkd.in/p/eccdGyTZ

## Keywords

harness engineering, vélocité, revue de code, goulot d'étranglement, tests générés par IA, couverture de code, mutation testing, tests de mutation, code smells, pratiques craft, software craftsmanship, shift-left, SDLC, PDLC, Example Mapping, ATDD, TDD, Given/When/Then, DDD, architecture hexagonale, skills, Superpowers, agents spécialisés, loop engineering, software factory, supervision humaine, organisation agentique

## Authors

Dorra Bartaguiz — CTO d'Arolla (conseil et formation, « agentic software crafters ») ; slides de son talk Dev With AI publiées sur LinkedIn.

## Ton

Profil : support de conférence pour développeurs, sur un ton enjoué et démonstratif (« Haha! », « Youhou! », « Génère moi ce besoin ! »). La progression est narrative : promesse de vélocité, rappel que la relecture reste le goulot, démonstration par un cas réel où le code et les tests générés sont mesurés puis démontés, définition du harness, reprise du même cas étape par étape avec les pratiques craft, puis élargissement du cycle de développement au cycle produit et à l'organisation. L'argument repose sur des sources citées (DORA, Clean Code, Minelli et al., Tornhill et Borg, Boehm, McKinsey, Kent Beck) et sur des mesures prises par l'oratrice sur son propre exemple (couverture, score de mutation). Les slides sont souvent des titres ou des schémas, sans commentaire oral ; plusieurs portent la mention « Context Engineering Training ». Le cadre est celui d'une formatrice en craft : les heuristiques et workflows des équipes sont présentés comme *« les skills de demain »*.

## Pense-betes

- **Constat** : la génération accélère la syntaxe mais alourdit la relecture et la vérification ; la code base reste le goulot.
- **Cas dépistage** : date d'invitation = jour de naissance + année courante + mois de naissance + N mois selon le dépistage, puis reports (date invalide, date passée, férié, week-end).
- **Mesures de l'oratrice** : couverture annoncée 100 % / réelle 33 % (domaine 95 %) ; mutation testing 13,82 %.
- **Smells relevés** : configuration codée en dur, méthodes statiques, violation SRP, non thread-safe, échecs silencieux, valeurs magiques, nommage générique, couplage fort, mutabilité.
- **Harness** : tout ce qu'on ajoute autour du modèle ; levier proposé pour le déterminisme : craft + shift-left.
- **SDLC craft en cinq blocs** : Exploration → Décomposition (epics, features, user stories) → Formulation (exemples, scénarios) → Tests (TDD, ATDD, automatisation) → Développement et refactoring.
- **Baby steps** : *« seules ne suffisent pas »* ; il faut travailler le harness, d'où les skills.
- **Frameworks de skills cités** : Superpowers, skills de Matt Pocock, Impatient Programming, **Skraft** (AXA, talk de Cyrille et Olivier à Devoxx 2026).
- **Nouvelle version de modèle** : *« Vos anciens skills sont déjà intégrés »*.
- **PDLC** : stratégie produit, architecture et sécurité by design, UX/UI, release engineering, observabilité, maintenance, impact produit ; équiper la seule équipe de dev crée un goulot.
- Voisin de [[sfeir-code-review-anneau-contraintes-2026-07-30]] et [[lassiege-usine-logicielle-heure-ia-2026-07-28]].

## RésuméDe400mots

Dorra Bartaguiz part de la promesse de l'IA : plus de 80 % des développeurs estiment qu'elle a augmenté leur productivité individuelle, selon les rapports DORA 2024 et 2025. Mais vitesse veut dire risque. Le temps de développement s'est réduit, et le goulot reste la revue de code. Elle rappelle que la lecture dépasse largement l'écriture : un ratio de plus de dix pour un chez Robert C. Martin, environ 70 % du temps passé à comprendre le code contre 5 % à l'éditer selon une étude de 2015. L'IA accélère la génération syntaxique et alourdit la relecture.

Pour savoir si l'on peut se fier aux tests générés, elle prend un cas réel : calculer la date d'invitation à un dépistage médical à partir du type de dépistage, de la date de naissance et de la date du jour, avec des règles de report pour les dates invalides, passées, fériées ou tombant un week-end. Généré d'un seul prompt, le code est annoncé couvert à 100 %. Elle mesure 33 % de couverture globale, 95 % sur le domaine, relève une série de défauts (configuration en dur, méthodes statiques, violation du principe de responsabilité unique, échecs silencieux, valeurs magiques, couplage fort) et obtient un score de tests de mutation de 13,82 %. Les tests générés sans rigueur valident les erreurs de l'IA.

Elle définit alors le harness comme tout ce qu'on ajoute autour du modèle pour améliorer la génération ; un agent est un modèle plus un harness. Pour rendre l'agent plus déterministe, elle propose les pratiques craft et le shift-left. Le même cas est repris étape par étape : demander les définitions du domaine, décomposer en règles, identifier des exemples et des cas limites, écrire des scénarios Given/When/Then, générer les tests d'acceptation et unitaires, puis demander un refactoring vers le clean code, l'architecture hexagonale et les patterns tactiques du DDD. Avec l'IA, le TDD devient une pratique de contrôle d'un agent imprévisible ; elle cite Kent Beck, pour qui les équipes qui savent tester s'adapteront mieux.

Les baby steps ne suffisent pas : il faut travailler le harness, notamment par des skills. Les frameworks populaires, de Superpowers à Skraft chez AXA, reposent sur ces pratiques. Enfin, la vie d'un produit ne s'arrête pas au cycle de développement : équiper la seule équipe de développement crée un nouveau goulot. Elle propose d'outiller tout le cycle produit avec des agents spécialisés, des garde-fous contre les boucles infinies, et résume les usines logicielles comme la somme du loop engineering, du harness engineering et de la supervision humaine.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Dorra Bartaguiz | PERSONNE | publie | talk Quand la vélocité explose avec l'IA | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Dorra Bartaguiz | PERSONNE | travaille_chez | Arolla | ORGANISATION | 0.85 | DYNAMIQUE | déclaré_article |
| talk Quand la vélocité explose avec l'IA | DOCUMENT | observé_dans | Dev With AI | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| talk Quand la vélocité explose avec l'IA | DOCUMENT | référence | DORA | ORGANISATION | 0.90 | STATIQUE | déclaré_article |
| Dorra Bartaguiz | PERSONNE | affirme_que | la revue de code reste le goulot d'étranglement à l'ère de l'IA | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |
| Dorra Bartaguiz | PERSONNE | mesure | couverture annoncée 100 %, mesurée 33 % (95 % sur le domaine) sur le cas dépistage | MESURE | 0.95 | STATIQUE | déclaré_article |
| Dorra Bartaguiz | PERSONNE | mesure | score de mutation testing de 13,82 % des tests générés | MESURE | 0.95 | STATIQUE | déclaré_article |
| Dorra Bartaguiz | PERSONNE | recommande | mutation testing | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| Dorra Bartaguiz | PERSONNE | affirme_que | un agent IA est un modèle plus un harness | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Harness engineering | METHODOLOGIE | utilise | craft / artisanat logiciel | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| Harness engineering | METHODOLOGIE | utilise | Shift-Left | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| Harness engineering | METHODOLOGIE | améliore | Agents de codage | TECHNOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| Example Mapping | METHODOLOGIE | fait_partie_de | SDLC | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| ATDD (Acceptance Test-Driven Development) | METHODOLOGIE | fait_partie_de | SDLC | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| Dorra Bartaguiz | PERSONNE | affirme_que | avec l'IA, le TDD devient un outil de contrôle d'un agent imprévisible | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Kent Beck | PERSONNE | affirme_que | "Teams that know how to test properly will adapt better to AI agents." | CITATION | 0.88 | ATEMPOREL | déclaré_article |
| Domain-Driven Design | METHODOLOGIE | améliore | code généré par IA | CONCEPT | 0.80 | ATEMPOREL | déclaré_article |
| Superpowers | TECHNOLOGIE | est_basé_sur | craft / artisanat logiciel | METHODOLOGIE | 0.85 | STATIQUE | déclaré_article |
| AXA | ORGANISATION | a_créé | Skraft | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Skraft | TECHNOLOGIE | est_basé_sur | craft / artisanat logiciel | METHODOLOGIE | 0.85 | STATIQUE | déclaré_article |
| PDLC | METHODOLOGIE | affine | SDLC | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| Dorra Bartaguiz | PERSONNE | recommande | outiller tout le cycle produit par un workflow d'agents spécialisés (métier, tech, UX/UI) | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Software Factory | METHODOLOGIE | utilise | Loop Engineering | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| Software Factory | METHODOLOGIE | utilise | Harness engineering | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Dorra Bartaguiz | PERSONNE | rôle | CTO d'Arolla, formatrice craft et agents de codage | AJOUT |
| Arolla | ORGANISATION | secteur | Conseil et formation en développement logiciel (« agentic software crafters ») | AJOUT |
| talk Quand la vélocité explose avec l'IA | DOCUMENT | catégorie | Slides de conférence (61), Dev With AI, publiées sur LinkedIn le 15 octobre 2026 | AJOUT |
| Dev With AI | EVENEMENT | catégorie | Conférence développeurs et IA | AJOUT |
| Harness engineering | METHODOLOGIE | définition | Tout ce qu'on ajoute autour du modèle pour améliorer la génération ; agent = modèle + harness | AJOUT |
| mutation testing | METHODOLOGIE | usage | « Détecteur de mensonges » des tests générés par IA | AJOUT |
| Example Mapping | METHODOLOGIE | définition | Atelier d'identification de règles et d'exemples avant l'écriture des scénarios | AJOUT |
| PDLC | METHODOLOGIE | définition | Product Development Life Cycle : stratégie produit, architecture, UX/UI, release, observabilité, maintenance, boucle de valeur | AJOUT |
| Skraft | TECHNOLOGIE | catégorie | Framework de skills craft créé par les développeurs d'AXA (talk Devoxx 2026) | AJOUT |
