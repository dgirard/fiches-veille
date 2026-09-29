---
themes: [agents-codage-ia-skills, qualite-securite, outils-plateformes]
source: "Anthropic (claude.dev)"
---
# lancemartin-anthropic-automating-eval-design-hillclimbing-2026-09-28

## Veille

Article **Playbooks** de **Lance Martin**, publié sur le blog claude.dev le **28 septembre 2026** (12 min de lecture, neuf figures). Il présente deux sous-commandes ajoutées à la skill **claude-api** de Claude Code, `/claude-api build-eval` et `/claude-api hillclimb`, après avoir posé les principes qu'elles appliquent. Trois apports. **(A)** Quatre propriétés d'une bonne évaluation : tâches représentatives de la production, scores qui montent avec le modèle et l'effort, marge de progression sous **100 %** au sommet, faible variance d'un run à l'autre ; plus l'*échantillonnage adversarial* : on retient un cas difficile parce qu'un humain sait dire pourquoi, non parce que le modèle du jour l'échoue. **(B)** Un hillclimbing discipliné : une modification par tour, jeu **train/test** séparé, patch annulé si le train monte et que le test reste plat. **(C)** Deux exemples chiffrés : un benchmark de support client (**44** tickets) dont le coût passe d'environ **4,6 à 1 centime** par ticket, et l'évaluation de la skill claude-api elle-même, de **66 %** à environ **88 %**. Rappel du texte : *« il est important de lire un échantillon de transcriptions notées avant de croire votre évaluateur »*. À rapprocher de l'auteur sur le cache de prompt, [[lancemartin-anthropic-prompt-auto-caching-claude-2026-02]].

## Titre Article

Automating eval design and hillclimbing with Claude

## Date

2026-09-28

## URL

https://claude.dev/blog/automating-eval-design-and-hillclimbing/

## Keywords

évaluation, eval design, hillclimbing, claude-api, build-eval, hillclimb, Claude Code, skill, échantillonnage adversarial, jeu d'entraînement et jeu de test, surapprentissage de l'évaluation, LLM-as-judge, grader programmatique, variance, intervalle de confiance, marge de progression, réduction de coût, effort, prompt caching, harnais, reward hacking, Opus 5.5, Sonnet 5

## Authors

Lance Martin (Anthropic), blog claude.dev, avec remerciements à Misha Khalman pour le développement de la skill.

## Ton

**Profil** : guide pratique d'ingénierie, écrit par un praticien d'Anthropic pour les équipes qui construisent une application ou une skill sur l'API Claude. Public : développeurs et responsables qualité de systèmes à base de LLM.

**Style** : deux parties symétriques (conception de l'évaluation, puis hillclimbing), chacune posant d'abord les principes puis la commande qui les applique, avant deux exemples chiffrés. Listes numérotées, figures schématiques, définitions données en cours de route (harnais, bruit). Le texte présente ses propres outils comme la mise en œuvre des principes annoncés.

**Position épistémique** : les chiffres des deux exemples proviennent de benchmarks internes à Anthropic (support client, évaluation de la skill claude-api) et ne sont pas reproductibles depuis l'article. Le résultat de référence est celui du jeu de test tenu à l'écart (90,5 % contre 78,6 %), les scores sur le jeu de recherche servant au réglage.

## Pense-betes

- **Quatre marques d'une bonne évaluation.** Tâches issues de la production ; score qui croît avec un modèle plus fort et plus d'effort ; meilleur modèle nettement sous 100 % ; variance faible. Signal d'alerte : une tâche qui échoue à chaque run quel que soit le nombre de répétitions est probablement ambiguë ou mal notée.
- **Critère d'une bonne tâche.** Deux experts du domaine rendent le même verdict et tout ce que le grader vérifie est énoncé dans la tâche. La variance peut aussi venir de la configuration (effort mal appliqué) ou de l'environnement (état résiduel, historique git qui livre la réponse).
- **Échantillonnage adversarial.** Choisir les cas que le modèle actuel échoue revient à échantillonner les vallées d'un seul modèle. On retient les cas jugés difficiles par un humain, et ceux tirés de bugs ou de tickets. Le trafic utilisateur brut peut biaiser vers le facile, les utilisateurs tentant ce dont ils attendent le succès.
- **`build-eval`, ordre des sources.** Transcriptions de production (après question sur la rétention et les données sensibles), rapports de bugs et tickets, cinq à dix cas écrits à la main, cas synthétisés depuis le code. Une page générée montre toutes les entrées et attend la confirmation de l'utilisateur.
- **Choix du grader.** Le moins cher qui convient : vérification programmatique si les sorties sont contraintes ; sinon LLM-as-judge avec une grille en affirmations vérifiables (pas une échelle de 1 à 5), un modèle juge distinct du modèle testé, et comparaison à l'aveugle en ordre aléatoire face à une référence.
- **Contrôles diagnostiques sur la ligne de base.** Grader rejoué deux fois sur la même sortie ; plomberie (délais, erreurs d'API, réponses tronquées) ; marge de progression, avec alerte si la base dépasse environ 95 %, auquel cas viser le coût ou la latence.
- **Où appliquer le hillclimbing.** Surface peu coûteuse à modifier (prompts, skills plutôt que code du harnais), score attribuable à cette surface (taux de déclenchement d'une skill et sa description), objectif cadré. Le coût est un objectif robuste même sur une évaluation saturée.
- **Trois parades au surapprentissage.** Séparer train et test ; ne jamais coller le contenu des échecs dans le prompt ; garder les réponses hors de portée structurelle du modèle. Exemples de fuites : un outil d'OCR ajouté parce que l'évaluation en profite, ou un dépôt public d'où le harnais récupère la solution.
- **Boucle `hillclimb`.** Choix de la surface modifiable (prompt système, skills, descriptions d'outils, modèle et effort, code du harnais), objectif, découpage aléatoire train/test, vérification préalable que le bruit est inférieur au plus petit gain utile. Chaque tour lit les transcriptions train et propose un patch ; conservé si train et test montent, annulé sinon. Livraison de la version la meilleure sur le test, avec intervalles de confiance ; si le gain est dans le bruit, recommandation de ne pas fusionner.
- **Étape de réflexion.** Quand le score stagne deux ou trois tours, aucune édition : chaque échec restant est classé par cause. Elle a révélé du contenu de skill présent mais ignoré, Claude écrivant d'anciennes formes d'API issues de ses acquis (budget de réflexion fixe au lieu de la réflexion adaptative), et des tâches ou graders défectueux.
- **Exemple coût (support client).** 44 tickets, 30 pour la recherche et 14 en test. Départ : Opus 4.8 en effort élevé, 74,4 % de précision, 4,6 centimes par ticket. Audit du prompt, puis Opus 5.5 en effort bas (87,8 %, 1,9 centime), puis Sonnet 5 en effort bas (88,9 %, 1 centime), enfin prompt amélioré (98,9 %). Sur les 14 tickets tenus à l'écart : 90,5 % contre 78,6 %, pour environ un cinquième du coût.
- **Exemple performance (skill claude-api).** De 66 % à 74 % en ajoutant huit fonctionnalités manquantes, 77 % après correction des tables de types C# et Java, 80 % avec une table de correspondance des anciennes vers les nouvelles formes d'API, environ 88 % après correction de deux tâches et graders défectueux.

## RésuméDe400mots

Lance Martin, d'Anthropic, publie sur le blog claude.dev un guide sur la conception d'évaluations et sur l'amélioration d'une application ou d'une skill contre elles, sans se tromper soi-même. Il annonce l'ajout de deux sous-commandes à la skill claude-api de Claude Code : `/claude-api build-eval` construit une évaluation dans le dépôt, `/claude-api hillclimb` améliore l'application contre elle, une modification à la fois, avec un jeu d'exemples tenu à l'écart pour détecter le surapprentissage.

La première partie énonce quatre propriétés d'une bonne évaluation. Les tâches reflètent la production. Les scores montent avec un modèle plus capable et un effort plus élevé, faute de quoi des tâches ambiguës ou un grader mal calibré sont en cause. Le meilleur modèle reste nettement sous 100 %, sans que l'écart tienne à des tâches impossibles : une tâche qui échoue à chaque run est suspecte, et une bonne tâche est celle sur laquelle deux experts donnent le même verdict. Enfin la variance est faible, ce qui suppose un grader stable, un effort appliqué de façon constante et un environnement sans état résiduel. L'auteur ajoute une mise en garde sur l'échantillonnage adversarial : choisir les cas que le modèle actuel échoue mesure son empreinte d'échec plutôt que la difficulté réelle. Il préconise des cas jugés difficiles par un humain, des échecs réels tirés de tickets ou de bugs, tout en notant que le trafic brut peut biaiser vers le facile.

`build-eval` interroge l'utilisateur, puis construit l'évaluation avec des pauses d'approbation. Les entrées viennent, dans l'ordre, des transcriptions de production, des tickets, de cinq à dix cas écrits à la main, puis de cas synthétisés. Le grader est le moins cher qui convienne : programmatique quand les sorties sont contraintes, sinon un modèle juge avec une grille d'affirmations vérifiables. Claude note quelques cas et demande si l'utilisateur les aurait jugés autrement, puis lance la ligne de base avec intervalle de confiance et trois contrôles : stabilité du grader, plomberie, marge de progression.

La seconde partie traite du hillclimbing. Il convient aux surfaces peu coûteuses à modifier, dont le score est attribuable, avec un objectif cadré ; le coût en est un bon. Pour le surapprentissage, trois parades : séparer train et test, ne jamais coller les échecs dans le prompt, garder les réponses hors de portée. La commande découpe l'évaluation, vérifie que le bruit est inférieur au gain visé, propose un patch par tour et le retire si le train monte seul. Sur stagnation, elle classe les échecs par cause avant d'éditer.

Deux exemples illustrent l'ensemble. Sur un benchmark de support de 44 tickets, le passage d'Opus 4.8 à Opus 5.5 puis à Sonnet 5 en effort bas, avec un prompt amélioré, donne 90,5 % contre 78,6 % sur les tickets tenus à l'écart, pour environ un cinquième du coût. Sur la skill claude-api, l'évaluation passe de 66 % à environ 88 % : sections manquantes, tables de types, table des formes d'API à abandonner, correction de tâches et graders défectueux.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Lance Martin | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | article Automating eval design and hillclimbing | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| claude-api | TECHNOLOGIE | fait_partie_de | Claude Code | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| claude-api build-eval | METHODOLOGIE | fait_partie_de | claude-api | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| claude-api hillclimb | METHODOLOGIE | fait_partie_de | claude-api | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| claude-api build-eval | METHODOLOGIE | utilise | LLM-as-judge | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| Échantillonnage adversarial | CONCEPT | s_applique_à | conception d'évaluation | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| Lance Martin | PERSONNE | recommande | choisir les cas difficiles parce qu'un humain sait dire pourquoi ils le sont | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Lance Martin | PERSONNE | recommande | lire un échantillon de transcriptions notées avant de croire l'évaluateur | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Hillclimbing | METHODOLOGIE | utilise | jeu train/test séparé | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Jeu train/test séparé | CONCEPT | résout | surapprentissage de l'évaluation | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Surapprentissage de l'évaluation | CONCEPT | observé_dans | outil d'OCR ajouté au harnais parce que l'évaluation en profite | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| claude-api hillclimb | METHODOLOGIE | recommande | annuler un patch quand le train monte et que le test reste plat | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Hillclimbing | METHODOLOGIE | réduit | coût par ticket à performance constante | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Claude Opus | TECHNOLOGIE | mesure | 74,4 % de précision à 4,6 centimes par ticket (Opus 4.8, effort élevé, départ) | MESURE | 0.93 | STATIQUE | déclaré_article |
| Claude Sonnet | TECHNOLOGIE | mesure | 90,5 % contre 78,6 % sur 14 tickets tenus à l'écart, pour environ un cinquième du coût | MESURE | 0.93 | STATIQUE | déclaré_article |
| Claude Opus | TECHNOLOGIE | améliore | coût des tokens : 20 % de moins en entrée et sortie, 60 % de moins en lecture de cache (Opus 5.5 face à 4.8) | MESURE | 0.9 | STATIQUE | déclaré_article |
| claude-api | TECHNOLOGIE | mesure | 66 % de réussite au départ, environ 88 % après hillclimbing | MESURE | 0.93 | STATIQUE | déclaré_article |
| claude-api | TECHNOLOGIE | observé_dans | Claude écrit d'anciennes formes d'API issues de ses acquis malgré le contenu présent | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Étape de réflexion sur les échecs | METHODOLOGIE | permet | de détecter des tâches ou graders défectueux | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Lance Martin | PERSONNE | rôle | Auteur de l'article, Anthropic | AJOUT |
| Anthropic | ORGANISATION | secteur | IA ; éditeur de Claude Code et de la skill claude-api | AJOUT |
| article Automating eval design and hillclimbing | DOCUMENT | nature | Playbook du blog claude.dev, 28 septembre 2026 | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI hébergeant la skill claude-api | AJOUT |
| claude-api | TECHNOLOGIE | catégorie | Skill de Claude Code : guidance sur l'API Claude et sous-commandes build-eval et hillclimb | AJOUT |
| claude-api build-eval | METHODOLOGIE | définition | Entretien guidé qui construit dans le dépôt un jeu d'évaluation, son grader et un runner, avec approbation de l'utilisateur | AJOUT |
| claude-api hillclimb | METHODOLOGIE | définition | Boucle d'amélioration un patch par tour, séparation train/test, annulation en cas de surapprentissage ou de régression | AJOUT |
| Hillclimbing | METHODOLOGIE | définition | Amélioration itérative d'un prompt, d'une skill ou d'un paramètre contre une évaluation | AJOUT |
| LLM-as-judge | METHODOLOGIE | forme retenue | Grille d'affirmations vérifiables ; modèle juge distinct du modèle testé ; comparaison à l'aveugle en ordre aléatoire | AJOUT |
| Échantillonnage adversarial | CONCEPT | définition | Sélectionner les cas parce qu'un humain les juge difficiles, non parce que le modèle du jour les échoue | AJOUT |
| Jeu train/test séparé | CONCEPT | rôle | Le hillclimber lit le train ; le test n'est jamais vu | AJOUT |
| Surapprentissage de l'évaluation | CONCEPT | symptôme | Train en hausse, test plat ; ajouts au harnais sans effet en production | AJOUT |
| Claude Opus | TECHNOLOGIE | versions citées | Opus 4.8 (départ), Opus 5.5 (effort bas : 87,8 % à 1,9 centime par ticket) | AJOUT |
| Claude Sonnet | TECHNOLOGIE | version citée | Sonnet 5 en effort bas : 88,9 % à 1 centime par ticket, puis 98,9 % avec prompt amélioré | AJOUT |
