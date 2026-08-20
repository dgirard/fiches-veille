---
themes: [agents-codage-ia-skills, architecture-construction, qualite-securite]
source: "Eventuallycoding"
---
# lassiege-usine-logicielle-heure-ia-2026-07-28

## Veille

Page de référence publiée sur **eventuallycoding.com** le **28 juillet 2026** par **Hugo Lassiège** (Lyon, développeur devenu entrepreneur, auteur de Bloggrify, Hakanai et Writizzy). L'auteur l'annonce comme telle : *« Ce sera plus une page de référence qu'un article »*, destinée à sa propre page ressources. **Objet** : la description exhaustive et outillée d'une **usine logicielle solo** où *« le code produit est désormais quasi 100 % généré »*, sur plusieurs monorepos polyglottes (Nuxt, Kotlin, JS — Hakanai, Writizzy, Bloggrify) en **déploiement continu en production**. **Distinction posée d'entrée** : ce n'est pas du **vibe coding** au sens de Karpathy (expérimentation, se laisser porter) mais du **context engineering** — *« donner tout le contexte nécessaire, au bon moment, pour que le logiciel corresponde à une intention et soit contrôlé systématiquement »*, avec la phrase qui fonde la responsabilité : *« Même si je n'écris pas le code, j'en suis responsable et je dois garder le contrôle dessus. »* **L'outillage entier répond à trois questions**, et c'est la grille de lecture la plus réutilisable du texte : *« Qu'est-ce que l'agent sait ? »* (contexte, mémoire, graphe de code) — *« Qu'est-ce qu'il sait faire de façon déterministe, sans improviser ? »* (skills, procédures) — *« Qu'est-ce qui l'arrête quand il se trompe ? »* (hooks, tests d'architecture, quality gates). **Six couches détaillées** : (1) **contexte** — `CLAUDE.md` racine + `.claude/rules/*.md` thématiques à chargement conditionnel par `paths:` + `.agents/*.md` pour le non-technique (personas, positionnement, ton) ; (2) **skills** — une trentaine, critère d'existence *« si j'explique la même chose une troisième fois »* ; (3) **outils** — MCP IDE JetBrains, **GitNexus** (graphe de code : `impact(symbole)`, `detect_changes()`), Claude-mem, wrapper de filtrage RTK, Sentry, base en lecture seule ; (4) **garde-fous exécutables** — hooks du harness, **tests d'architecture**, lint de patterns (**ast-grep** pour les décisions d'architecture, pas seulement ESLint) ; (5) **usine** — quality gate bloquante avec `needs:` sur le job de qualité, cinq étages de tests ; (6) **process produit** — specs numérotées avec skill de rédaction **et skill de clôture**, design dans Claude Design, livraison par étapes sous feature flag, distinction **feature flipping** (Unleash) vs **gating** (contrat client). **La règle qui résume tout** : *« Ce qui compte doit être exécutable. Une consigne est suivie "la plupart du temps"… Un hook ou un test est suivi tout le temps. »* **Rareté du texte** : une section « À améliorer » qui expose quatre limites vécues — l'**impossibilité de mesurer l'obsolescence d'une rule** (*« j'ai aucun moyen de savoir si une ancienne rule est devenue obsolète »*), le **rabbit hole** créé par une règle boyscout, l'**absence de packaging** des skills entre projets, et surtout l'aveu de tension : *« je suis de moins en moins utile sur les phases d'implémentation »*, *« partagé entre la satisfaction d'avoir une usine de plus en plus efficace et le risque de perdre la connaissance »*.

## Titre Article

Mon usine logicielle à l'heure de l'IA

## Date

2026-07-28

## URL

https://eventuallycoding.com/p/mon-usine-logicielle-a-l-heure-de-l-ia

## Keywords

usine logicielle, context engineering, vibe coding, Karpathy, code 100% généré, solo dev, monorepo, polyglotte, Nuxt, Kotlin, déploiement continu, CLAUDE.md, rules, chargement conditionnel, paths, agents.md, personas, contexte permanent, budget de contexte, économie de tokens, skills, procédure rejouable, sous-agents, délégation, MCP, JetBrains, GitNexus, graphe de code, impact, rayon d'explosion, detect_changes, flux d'exécution, Claude-mem, mémoire persistante, RTK, filtrage des sorties, Sentry, base en lecture seule, garde-fous exécutables, hooks, harness, tests d'architecture, frontière open source, lint de patterns, ast-grep, ESLint, typecheck, quality gate bloquante, GitHub Actions, needs, étages de tests, conteneurs jetables, testcontainers, end-to-end, process produit, spec numérotée, clôture de spec, Claude Design, maquette, feature flag, Unleash, feature flipping, gating, trunk based, Marty Cagan, quatre risques, obsolescence des rules, rabbit hole, boyscout, packaging des skills, perte de connaissance, Hugo Lassiège

## Authors

**Hugo Lassiège** — développeur devenu entrepreneur, basé à **Lyon**, écrit du code depuis 2001 et tient **eventuallycoding.com** (le blog a porté le nom `hakanai.free.fr` avant de devenir *Eventuallycoding* en 2013). *Eventuallycoding* est le nom-parapluie qui regroupe ses projets, sa chaîne YouTube et ses blogs.

**Les trois produits cités sont les siens**, et c'est ce qui donne son poids au texte : **Bloggrify** (générateur de blog statique, open source), **Hakanai** (application de newsletter pour blogs statiques) et **Writizzy** (plateforme de blogging — qui propulse la page elle-même, *« Propulsé par Writizzy »* en pied de page). Il ne décrit donc pas une méthode conseillée à des clients mais **le dispositif avec lequel il fait tourner ses propres produits en production**, seul.

## Ton

**Profil** : **page de référence technique** assumée comme telle — *« Ce sera plus une page de référence qu'un article et je vais la référencer sur la page ressources du site »*. Registre de **praticien solo** documentant son propre poste de travail : ni thought leadership, ni retour d'expérience d'entreprise, ni tutoriel. Public : développeurs qui outillent déjà des agents et cherchent une configuration de référence à comparer à la leur.

**Style** : **architecture en couches numérotées** (1 à 6), chacune ouverte par sa fonction, densément **tabulée** — la page compte une dizaine de tableaux à deux colonnes (fichier/contenu, famille/ce qu'elles encodent, déclencheur/effet, étage/couverture, besoin/mécanisme). C'est une **fiche technique**, pas une démonstration : les tableaux portent l'information, la prose porte les raisons. Extraits de configuration réels et non maquillés (une `rule` complète avec son frontmatter `paths:` et son tableau de routage vers neuf skills, le schéma ASCII du pipeline CI, le contenu de `boyscout.md`).

**Trois traits qui distinguent le texte de la littérature ambiante** :

1. **La modestie sur la portée des règles.** *« Une contrainte c'est propre à un projet et à une personne. C'est pas une question de qualité logicielle au sens strict. »* L'auteur refuse explicitement de présenter ses conventions comme des bonnes pratiques universelles — rare dans un genre qui verse vite au prescriptif.
2. **L'auto-évaluation honnête des outils.** Sur Claude-mem : *« j'ai honnêtement un peu de mal à mesurer l'impact négatif ou positif. J'ai pas encore assez de recul »*. Sur le wrapper RTK : *« le gain est parfois annulé car Claude lance deux fois la commande »*. Sur les sous-agents : *« je les utilise de moins en moins »*. **On lit ce qui ne marche pas, ou plus.**
3. **L'aveu final, non résolu.** *« Je suis de moins en moins utile sur les phases d'implémentation »*, *« c'est limite flippant et plus rigoureux que 99 % des humains »*, *« partagé entre la satisfaction d'avoir une usine logicielle de plus en plus efficace et le risque de perdre la connaissance »*. Le texte se termine sur un problème ouvert, pas sur une conclusion.

**Formules-marqueurs** : *« Même si je n'écris pas le code, j'en suis responsable »*, *« Inutile de dire à une IA d'écrire du code de qualité, ça ne rime à rien. Il faut expliciter ses propres contraintes »*, *« Ce qui compte doit être exécutable »*, *« Le contexte est un budget »*, *« 1 bug résolu, 10 de produits »*, *« La doc de spec meurt si sa clôture n'est pas dans le process »*, *« si j'explique la même chose une troisième fois, ça devient une skill »*, *« ça ne peut pas être contourné, à l'inverse d'une rule »*.

## Pense-betes

- **Date / source** : **28 juillet 2026**, eventuallycoding.com, **Hugo Lassiège**. Page de référence assumée comme telle, décrivant le dispositif avec lequel l'auteur fait tourner ses propres produits en production, seul.
- **Cadrage clé** : ce n'est pas du vibe coding — *« Le vibe coding tel que défini par Karpathy c'était de l'expérimentation et le fait de se laisser porter. Ici, je vais parler de context engineering. »* Avec la clause de responsabilité : *« Même si je n'écris pas le code, j'en suis responsable et je dois garder le contrôle dessus. »*

### La grille des trois questions

Tout l'outillage répond à trois questions, et c'est l'apport le plus réutilisable du texte :

| Question | Ce qui y répond |
|---|---|
| Qu'est-ce que l'agent **sait** ? | contexte, mémoire, graphe de code |
| Qu'est-ce qu'il sait faire de façon **déterministe** ? | skills, procédures |
| Qu'est-ce qui **l'arrête** quand il se trompe ? | hooks, tests d'architecture, quality gates |

Posée devant une installation agentique, elle révèle laquelle des trois est vide. Principe directeur associé : *« Ce qui compte doit être exécutable. Une consigne est suivie "la plupart du temps", mais elle peut être oubliée. Un hook ou un test est suivi tout le temps. »* Et sur les tests d'architecture : *« ça ne peut pas être contourné, à l'inverse d'une rule. »*

### Les six couches

| # | Couche | Contenu |
|---|--------|---------|
| 1 | **Contexte** | `CLAUDE.md` racine permanent et court (architecture, conventions, index des specs) ; `.claude/rules/*.md` conditionnels activés par frontmatter `paths:` ; `.agents/*.md` pour le non technique (positionnement, personas, ton) |
| 2 | **Skills** | une trentaine, six familles ; critère d'existence : la troisième répétition |
| 3 | **Outils** | MCP IDE JetBrains, **GitNexus** (graphe de code), Claude-mem, Sentry, base en lecture seule |
| 4 | **Garde-fous** | hooks du harnais, tests d'architecture, lint de patterns (`ast-grep`) |
| 5 | **Usine** | quality gate bloquante, cinq étages de tests |
| 6 | **Process produit** | specs numérotées, skill de rédaction **et** skill de clôture, feature flags |

**Couche 1** — le contexte permanent porte l'index, pas le contenu : la rule vue en entier est une table de routage listant neuf skills avec la tâche qui les déclenche. *« Si l'IA ne fait pas de changement de schéma, aucun intérêt d'aller ouvrir la skill db-migration. »*

**Couche 2** — les skills « procédure multi-fichiers » sont les plus rentables : *« ajouter un bloc à l'éditeur de contenu touche trois surfaces de rendu ; sans skill, l'agent en oublie systématiquement une »*. Nuance : *« Ce chargement automatique peut parfois échouer. Dans ce cas, il faut demander explicitement d'utiliser la skill. »* Sous-agents en recul, réservés aux tâches *« qui génèrent beaucoup de lecture sans beaucoup de décision »* — *« Je les utilise de moins en moins, les agents récents font eux-mêmes des délégations assez ciblées. »*

**Couche 3** — GitNexus indexe le dépôt en graphe et donne `impact(symbole)` avant de modifier, `detect_changes()` avant de commiter, la recherche d'un flux d'exécution plutôt qu'un grep, et le renommage via le graphe d'appels. Justification de l'auteur : *« Le vrai sujet c'est pas la vitesse, c'est de détecter tous les effets de bord d'une modification. »* MCP traité comme une dépense de contexte à justifier : *« J'essaie d'éviter les MCP qui sont plus consommateurs en contexte. »*

**Couche 4** — les hooks sont *« des scripts déclenchés par le harness de l'agent, pas par l'agent lui-même »* : refuser le build natif et rediriger vers le build IDE, lancer le formateur après écriture. Distinction du lint : ESLint pour la syntaxe, **`ast-grep` pour les décisions d'architecture** (interdire tout appel à `fetch` sans passer par le client OpenAPI), typecheck pour le typage.

**Couche 5** — `push sur main → quality gate (lint → lint de patterns → typecheck → tests) → build image → registry → webhook de déploiement`, le job de déploiement portant un **`needs:` sur le job de qualité**. Cinq étages : unitaire, intégration avec conteneurs jetables (*« base de données et broker réels, pas de mock »*), architecture, composants front, end-to-end sur les parcours critiques uniquement.

**Couche 6** — specs encadrées par deux skills, dont une **pour clôturer** en mettant la spec à jour avec ce qui a réellement été construit : *« La doc de spec meurt si sa clôture n'est pas dans le process. »* Règle anti-hallucination : *« Si une spec est floue ou incohérente avec l'existant, l'agent doit poser la question, pas deviner. »* Livraison par étapes sous feature flag, motivée par la dégradation du contexte long — *« ça me permet de faire plusieurs petites sessions d'implémentation plutôt qu'une grosse session, qui a tendance à se dégrader en qualité »*. Distinction **feature flipping** (Unleash : rollout, kill-switch) vs **gating** (contrat client, plan).

### Le geste le plus instructif : une contrainte future déjà garantie

L'auteur prévoit d'open-sourcer une partie du code. La règle *« le code destiné à l'open source ne doit jamais dépendre du code propriétaire »* est **écrite dans les rules** et **vérifiée par un test d'architecture**. *« Écrire une contrainte future dans le contexte évite de payer une refonte plus tard. »*

### Par où commencer, dans l'ordre donné

1. La **quality gate** d'abord si elle n'existe pas. 2. Un `CLAUDE.md` léger décrivant l'essentiel **et le pourquoi**. 3. Des rules au fil de l'eau sur les patterns d'architecture importants. 4. Des skills dès qu'une procédure revient. 5. CLI et MCP pour les outils principaux. Avertissement : *« tout skill, MCP, code repris depuis l'extérieur doit être scruté. Ce sont des dépendances qui peuvent être des vecteurs d'attaques. »*

### Les quatre limites vécues

1. **L'obsolescence des rules n'est pas mesurable.** *« Milieu 2025, "écris un test pour chaque nouveau service" faisait sens. Aujourd'hui c'est du bruit et Claude le fait naturellement… J'ai aucun moyen de mesurer et de savoir si une ancienne rule est devenue obsolète. »*
2. **Le rabbit hole.** Une rule `boyscout.md` produit *« des sessions sans fin »* et de la surcharge cognitive ; correctif envisagé, router ces constats vers une TODO list et déplacer la maintenance dans un workflow séparé.
3. **Pas de packaging.** Skills et rules sont copiés-collés d'un projet à l'autre, parfois dépendants du poste.
4. **Dépendance à Claude**, jugée *« risque modéré »*, et IDE devenu inadapté : *« j'utilise encore IntelliJ mais je ne le trouve plus adapté à notre époque. »*

### L'aveu de fond

*« Les dernières versions d'Opus sont de plus en plus autonomes… Soyons honnête, je suis de moins en moins utile sur les phases d'implémentation, mais je ne veux pas perdre le contrôle du code produit. Je suis partagé entre la satisfaction d'avoir une usine logicielle de plus en plus efficace et le risque de perdre la connaissance. »* Le dispositif garantit que le code est correct ; il ne garantit pas que l'humain le comprenne encore. Question laissée ouverte : *« Je dois trouver un moyen pour contrôler a posteriori les designs, de m'approprier le résultat. »* Même problème que celui posé par [[osmani-cognitive-surrender-comprehension-debt-2026-05-05]].

### Portée

Dispositif **solo**, sur des produits personnels, avec un seul décideur : aucune coordination multi-développeurs, aucune revue par un pair, aucune contrainte de conformité. Se transposent en entreprise la grille des trois questions, le principe de l'exécutable, la clôture de spec et le lint de patterns ; ne se transpose pas l'absence de gate humaine autre que soi. Même thèse, énoncée en doctrine deux jours plus tard, dans [[sfeir-code-review-anneau-contraintes-2026-07-30]].

## RésuméDe400mots

Page de référence publiée le **28 juillet 2026** par **Hugo Lassiège** sur eventuallycoding.com, documentant son **usine logicielle solo** pour des produits en production (Hakanai, Writizzy, Bloggrify) dont *« le code produit est désormais quasi 100 % généré »*.

**Le cadrage.** Ce n'est pas du **vibe coding** — qui était, chez Karpathy, de l'expérimentation — mais du **context engineering** : *« donner tout le contexte nécessaire, au bon moment, pour que le logiciel corresponde à une intention et soit contrôlé systématiquement »*. La responsabilité ne se délègue pas : *« Même si je n'écris pas le code, j'en suis responsable. »* Et la qualité logicielle dépasse le code — elle inclut l'intention et les **quatre risques de Marty Cagan**.

**La grille.** Tout l'outillage répond à trois questions : ce que l'agent **sait** (contexte, mémoire, graphe de code), ce qu'il sait faire **de façon déterministe** (skills), et **ce qui l'arrête** quand il se trompe (hooks, tests, gates).

**Six couches.** Le **contexte** est stratifié par moment de chargement : `CLAUDE.md` court et permanent, `rules` conditionnelles activées par chemin, `.agents/*.md` pour les personas et le positionnement — une rule servant de **table de routage** vers des skills à n'ouvrir qu'au besoin. Les **skills** (une trentaine) naissent à la troisième répétition ; les plus rentables sont celles qui couvrent une **procédure multi-fichiers**. Les **outils** délèguent le déterministe : MCP IDE, **GitNexus** qui indexe le dépôt en graphe pour mesurer le rayon d'explosion d'une modification — *« le vrai sujet c'est pas la vitesse, c'est de détecter tous les effets de bord »*. Les **garde-fous** sont exécutables : hooks déclenchés par le harness, **tests d'architecture** qui cassent la CI, et **`ast-grep`** pour transformer une décision d'architecture en règle de lint. L'**usine** impose une quality gate dont le job de déploiement dépend (`needs:`), avec cinq étages de tests. Le **process produit** part d'une spec numérotée, encadrée par une skill de rédaction **et une skill de clôture** — *« sans elle, les specs deviennent obsolètes en six mois »* —, livrée par étapes sous feature flag.

**Le principe.** *« Ce qui compte doit être exécutable. Une consigne est suivie "la plupart du temps"… Un hook ou un test est suivi tout le temps. »*

**Les limites, exposées.** L'obsolescence d'une rule n'est pas mesurable ; une règle boyscout produit des sessions sans fin ; les skills se copient-collent faute de packaging. Et l'aveu final : *« je suis de moins en moins utile sur les phases d'implémentation »*, partagé entre l'efficacité de l'usine et *« le risque de perdre la connaissance »*.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Hugo Lassiège | PERSONNE | publie | Mon usine logicielle à l'heure de l'IA | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Hugo Lassiège | PERSONNE | a_créé | Bloggrify | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Hugo Lassiège | PERSONNE | a_créé | Writizzy | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Hugo Lassiège | PERSONNE | affirme_que | ce qui compte doit être exécutable : une consigne est suivie la plupart du temps, un hook ou un test est suivi tout le temps | CITATION | 0.97 | ATEMPOREL | déclaré_article |
| test d'architecture | CONCEPT | surpasse | une rule de contexte, parce qu'il ne peut pas être contourné | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| context engineering | METHODOLOGIE | s_oppose_à | vibe coding | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Hugo Lassiège | PERSONNE | affirme_que | même sans écrire le code, l'humain en reste responsable et doit en garder le contrôle | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Hugo Lassiège | PERSONNE | recommande | expliciter ses propres contraintes plutôt que demander à une IA d'écrire du code de qualité | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| usine logicielle | CONCEPT | est_basé_sur | trois questions : ce que l'agent sait, ce qu'il fait de façon déterministe, ce qui l'arrête quand il se trompe | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| contexte permanent | CONCEPT | permet | d'indexer les skills sans les charger, le contenu n'étant ouvert qu'au besoin | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| skill | METHODOLOGIE | est_instance_de | procédure écrite une fois et rejouée à l'identique, créée dès la troisième répétition | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| GitNexus | TECHNOLOGIE | permet | de mesurer le rayon d'explosion d'une modification et d'en détecter tous les effets de bord | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| graphe de code | CONCEPT | surpasse | le grep de nom de fonction pour retrouver un flux d'exécution | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| hooks | CONCEPT | fait_partie_de | harness de l'agent | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| ast-grep | TECHNOLOGIE | permet | de transformer une décision d'architecture en règle de lint | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| quality gate | CONCEPT | permet | d'empêcher tout déploiement non validé, via une dépendance du job de déploiement au job de qualité | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| clôture de spec | METHODOLOGIE | résout | l'obsolescence des specs, qui deviennent périmées en six mois sans elle | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| feature flag | CONCEPT | permet | de livrer une spec par étapes et d'éviter les longues sessions dont la qualité se dégrade | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Unleash | TECHNOLOGIE | s_applique_à | l'activation et la désactivation de fonctionnalités sans redéploiement | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Hugo Lassiège | PERSONNE | affirme_que | rien ne permet de mesurer si une ancienne rule est devenue obsolète | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| règle d'amélioration continue | CONCEPT | s_oppose_à | la terminaison d'une session, en produisant des sessions sans fin | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| Hugo Lassiège | PERSONNE | affirme_que | l'efficacité croissante de l'usine logicielle s'accompagne d'un risque de perdre la connaissance du code | CITATION | 0.94 | DYNAMIQUE | déclaré_article |
| skills et MCP repris de l'extérieur | CONCEPT | s_oppose_à | la sécurité de la chaîne, en constituant des dépendances vectrices d'attaques | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| qualité logicielle | CONCEPT | est_basé_sur | les quatre risques de Marty Cagan — valeur, utilisabilité, faisabilité, viabilité — au-delà de la production de code | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| sous-agents | CONCEPT | s_applique_à | les tâches à forte lecture et faible décision, rendant une conclusion plutôt qu'un dump de fichiers | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Hugo Lassiège | PERSONNE | rôle | Développeur devenu entrepreneur, basé à Lyon ; auteur d'eventuallycoding.com et créateur de Bloggrify, Hakanai et Writizzy | AJOUT |
| Mon usine logicielle à l'heure de l'IA | DOCUMENT | catégorie | Page de référence (28 juil. 2026) décrivant en six couches un dispositif solo de développement à code quasi entièrement généré | AJOUT |
| usine logicielle | CONCEPT | définition | Ensemble outillé — contexte, skills, outils, garde-fous exécutables, quality gate, process produit — qui encadre un code produit par des agents pour qu'il corresponde à une intention et reste contrôlé | AJOUT |
| garde-fou exécutable | CONCEPT | définition | Contrôle qui s'applique automatiquement (hook, test d'architecture, lint de patterns, quality gate) par opposition à une consigne de contexte, qu'un modèle peut ignorer | AJOUT |
| GitNexus | TECHNOLOGIE | définition | Indexation d'un dépôt en graphe de symboles, relations et flux d'exécution, exposée par MCP ; sert à mesurer le rayon d'explosion d'une modification avant édition et à vérifier le périmètre réellement touché avant commit | AJOUT |
| clôture de spec | METHODOLOGIE | définition | Étape de fin de cycle où la spécification est mise à jour avec ce qui a réellement été construit — sans elle, les specs se périment en six mois | AJOUT |
| lint de patterns | CONCEPT | définition | Vérification automatique de décisions d'architecture par analyse de l'arbre syntaxique (ast-grep), distincte du lint de syntaxe et du typecheck | AJOUT |
| context engineering | METHODOLOGIE | application | Donner tout le contexte nécessaire au bon moment, stratifié par moment de chargement : permanent court, conditionnel par chemin, spécialisé à la demande | MISE_A_JOUR |
| Writizzy | TECHNOLOGIE | catégorie | Plateforme de blogging développée par Hugo Lassiège, qui propulse eventuallycoding.com (dogfooding) | AJOUT |
| Bloggrify | TECHNOLOGIE | catégorie | Générateur de blog statique open source développé par Hugo Lassiège | AJOUT |
