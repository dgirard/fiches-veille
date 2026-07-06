---
themes: [agents-codage-ia-skills]
source: "voodootikigod.com (Chris Williams)"
---
# williams-adlc-7-built-with-the-lifecycle-2026-06-12

## Veille

Septième et dernier volet ADLC : Williams présente un toolkit open-source de dix-huit outils construit *avec* le cycle lui-même (boucle build-prosecute-fix, agents parallèles, core `@adlc/core` gelé puis fan-out — « pinned means merged »). Le cœur doctrinal est « frontier-free » : atteindre les cibles de précision avec des modèles mid-tier (Opus/Sonnet/Haiku-class) plutôt que frontier, via cinq substitutions (search remplace insight, décomposition remplace horizon, banking remplace présence, mesure remplace métacognition, le generator-verifier gap fait tourner le moteur), l'humain restant le tier « frontier » sur les deux portes de spec. Fil rouge de la série : « replace trust with structure, and structure with measurement. »

## Titre Article

The ADLC Toolkit

## Date

2026-06-12

## URL

https://www.voodootikigod.com/adlc-7-built-with-the-lifecycle

## Keywords

ADLC, toolkit, dix-huit outils, @adlc/core, pinned means merged, frontier-free, modèles mid-tier, generator-verifier gap, search replaces insight, décomposition, banking, mesure vs métacognition, judge panels, premortem, parallax, lesson-foundry, séquencement d'adoption, replace trust with structure, npx, exit codes, github.com/voodootikigod/adlc

## Authors

Chris Williams (@voodootikigod)

## Ton

Profil : clôture-démonstration d'une série technique (perspective praticien-builder en anglais, registre synthétique et doctrinal), niveau technique très élevé, public cible ingénieurs et équipes prêts à adopter le cycle. Le ton est celui de la preuve par l'artefact : le toolkit a été construit avec le cycle qu'il outille, ce qui fait de l'article à la fois une documentation et une démonstration auto-référentielle. L'autorité s'appuie sur le code livré (repo public, package npm, outils npx zéro-dépendance à exit codes déterministes) et sur une « honest loss account » qui assume explicitement ce que la doctrine sacrifie. Style récapitulatif et axiomatique : cinq substitutions numérotées, séquencement d'adoption ordonné, anti-pattern nommé, et une formule-somme qui clôt les sept volets — « replace trust with structure, and structure with measurement ».

## Pense-betes

- **Auto-référence** : le toolkit (dix-huit outils) a été construit *via* le cycle ADLC — agents parallèles suivant la boucle build-prosecute-fix, avec un core gelé `@adlc/core` (appels LLM, opérations git, conventions CLI, findings ledgers).
- **Principe structurel** : « pinned means merged » — le core partagé est mergé **avant** le fan-out, pour éviter le dependency hell en développement parallèle.
- **Cinq phases d'outils** : Specify (`spec-lint`, `premortem`, `parallax`, `coldstart`) ; Rail + Build (`rails-guard`, `hollow-test`, `preflight`, `merge-forecast`, `model-router`, `flail-detector`, `consensus-fix`) ; Prosecute (`review-calibration`) ; Integrate (`behavior-diff`, `gate-manifest`) ; Distill (`lesson-foundry`, `skill-rot`, `model-ratchet`, `rejection-mining`).
- **Doctrine frontier-free** : atteindre les cibles de précision avec des modèles mid-tier (classe Opus/Sonnet/Haiku) plutôt que frontier. Cinq substitutions remplacent les capacités frontier : (1) le **generator-verifier gap** fait tourner le moteur — vérifier est moins cher que générer, « you never need a model smarter than the gate it must pass » ; (2) **search remplace insight** — N tentatives diverses sélectionnées par jugement mid-tier battent un seul passage frontier ; (3) **décomposition remplace horizon** — des tickets plus petits gardent les modèles sous le seuil de dégradation ; (4) **banking remplace présence** — les modèles chers frappent des structures permanentes (contrats, skills, lints) puis sortent, les mid-tier opèrent dedans ; (5) **mesure remplace métacognition** — divergence de parallax, stats de consensus et lacunes énumérées remplacent les requêtes de confiance.
- **Sixième substitution** : l'humain est le tier frontier, occupant les deux portes de spécification où la vérification d'intention est la vérité-terrain.
- **Honest loss account** : la doctrine sacrifie l'élégance architecturale en un seul passage, l'intuition transversale subtile, la latence, et les refactors à long horizon sans résistance à la décomposition. Mitigations : judge panels, premortems, portes humaines ; le résidu (~5 % du travail) tourne à supervision maximale.
- **Séquencement d'adoption** : (1) prosecution des PRs existantes (zéro changement de workflow, construit la confiance) ; (2) rails et génération de tests (installe l'ancre de confiance) ; (3) interrogation (questionnement de spec après que les agents manquent des exigences) ; (4) parallélisme complet et distillation (une fois les habitudes établies). **Anti-pattern** : mandater le cycle complet dès le jour 1 crée de la cérémonie avant que le compounding ne se matérialise.
- **Fil rouge des sept volets** : « replace trust with structure, and structure with measurement » — le mécanisme s'amplifie avec des modèles plus forts, ce qui en fait un lifecycle et non un workaround.
- **Livraison** : repo `github.com/voodootikigod/adlc`, package `@adlc/core` (npm), outils npx zéro-dépendance à exit codes déterministes (0 = pass, 2 = gate échoué) pour intégration CI.

## RésuméDe400mots

Le septième volet clôt la série par la preuve : un toolkit de dix-huit outils, open-source, construit avec le cycle ADLC lui-même. Des agents parallèles ont suivi la boucle build-prosecute-fix autour d'un core gelé, `@adlc/core`, qui centralise appels LLM, opérations git, conventions CLI et findings ledgers. Le principe structurel — « pinned means merged » — veut que ce core partagé soit mergé avant tout fan-out, afin d'éviter le dependency hell du développement parallèle. Les outils s'organisent selon les cinq phases : Specify (spec-lint, premortem, parallax, coldstart), Rail+Build (rails-guard, hollow-test, preflight, merge-forecast, model-router, flail-detector, consensus-fix), Prosecute (review-calibration), Integrate (behavior-diff, gate-manifest) et Distill (lesson-foundry, skill-rot, model-ratchet, rejection-mining).

Le cœur doctrinal est « frontier-free » : viser les cibles de précision avec des modèles mid-tier (classe Opus, Sonnet, Haiku) plutôt que frontier. Cinq substitutions remplacent les capacités frontier. D'abord, le generator-verifier gap fait tourner le moteur : vérifier coûte moins cher que générer, et « on n'a jamais besoin d'un modèle plus intelligent que le gate qu'il doit passer ». Ensuite, search remplace insight : N tentatives diverses, triées par un jugement mid-tier, surpassent un seul passage frontier — et la mesure prouve la capacité de la stack. Décomposition remplace horizon : des tickets plus petits maintiennent les modèles sous leur seuil de dégradation. Banking remplace présence : les modèles chers frappent une fois des structures permanentes (contrats, skills, lints) puis sortent, et les mid-tier opèrent à l'intérieur. Enfin, mesure remplace métacognition : divergence de parallax, statistiques de consensus et lacunes énumérées remplacent les requêtes de confiance. Une sixième substitution place l'humain comme tier frontier, sur les deux portes de spécification où l'intention est la vérité-terrain.

Williams tient une « honest loss account » : la doctrine sacrifie l'élégance architecturale en un seul jet, l'intuition transversale subtile, la latence et les refactors à long horizon réticents à la décomposition. Les mitigations sont des judge panels, des premortems et les portes humaines ; le résidu, environ 5 % du travail, tourne à supervision maximale.

Côté adoption, il rejette le big-bang : commencer par la prosecution des PRs existantes (zéro changement de workflow), puis les rails et la génération de tests, puis l'interrogation, et seulement ensuite le parallélisme complet et la distillation. Mandater le cycle entier dès le premier jour est l'anti-pattern, car il impose la cérémonie avant que le compounding ne paie. Le fil rouge des sept volets se résume d'une formule : « replace trust with structure, and structure with measurement » — un mécanisme qui s'amplifie avec des modèles plus forts, donc un lifecycle et non un workaround. Le code est livré sur github.com/voodootikigod/adlc, en outils npx zéro-dépendance à exit codes déterministes pour la CI.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Chris Williams | PERSONNE | publie | The ADLC Toolkit | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Chris Williams | PERSONNE | a_créé | ADLC Toolkit | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| ADLC Toolkit | TECHNOLOGIE | est_basé_sur | cycle ADLC (build-prosecute-fix en agents parallèles) | METHODOLOGIE | 0.92 | STATIQUE | déclaré_article |
| ADLC Toolkit | TECHNOLOGIE | utilise | @adlc/core | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Chris Williams | PERSONNE | affirme_que | « pinned means merged » : merger le core avant le fan-out | CITATION | 0.90 | ATEMPOREL | déclaré_article |
| doctrine frontier-free | CONCEPT | recommande | atteindre la précision cible avec des modèles mid-tier | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Chris Williams | PERSONNE | affirme_que | on n'a jamais besoin d'un modèle plus intelligent que le gate qu'il doit passer | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| generator-verifier gap | CONCEPT | permet | fonctionnement frontier-free du cycle (vérifier moins cher que générer) | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| search | METHODOLOGIE | remplace | insight d'un modèle frontier | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| décomposition | METHODOLOGIE | réduit | dégradation des modèles sur long horizon | CONCEPT | 0.89 | ATEMPOREL | déclaré_article |
| humains | PERSONNE | est_instance_de | tier frontier sur les deux portes de spécification | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| ADLC | METHODOLOGIE | affirme_que | « replace trust with structure, and structure with measurement » | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| Chris Williams | PERSONNE | recommande | adopter le cycle par séquencement de la douleur, pas en big-bang | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| ADLC Toolkit | TECHNOLOGIE | utilise | outils npx à exit codes déterministes (0 pass / 2 gate échoué) | TECHNOLOGIE | 0.89 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| ADLC Toolkit | TECHNOLOGIE | catégorie | Suite open-source de 18 outils npx zéro-dépendance pour le cycle ADLC | AJOUT |
| @adlc/core | TECHNOLOGIE | rôle | Core gelé : appels LLM, opérations git, conventions CLI, findings ledgers | AJOUT |
| pinned means merged | CONCEPT | principe | Merger le core partagé avant le fan-out parallèle pour éviter le dependency hell | AJOUT |
| doctrine frontier-free | CONCEPT | définition | Atteindre la précision cible avec des modèles mid-tier via cinq substitutions | AJOUT |
| cinq substitutions | CONCEPT | liste | Generator-verifier gap, search vs insight, décomposition vs horizon, banking vs présence, mesure vs métacognition | AJOUT |
| honest loss account | CONCEPT | sacrifices | Élégance en un passage, intuition transversale, latence, refactors long-horizon ; ~5 % du travail à supervision max | AJOUT |
| séquencement d'adoption | METHODOLOGIE | ordre | Prosecution des PRs → rails/tests → interrogation → parallélisme + distillation | AJOUT |
| replace trust with structure | CONCEPT | rôle | Formule-somme des sept volets : confiance → structure → mesure | AJOUT |
| ADLC Toolkit | TECHNOLOGIE | livraison | github.com/voodootikigod/adlc, package @adlc/core (npm) | AJOUT |
