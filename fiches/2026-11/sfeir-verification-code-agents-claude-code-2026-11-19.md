---
themes: [agents-codage-ia-skills, qualite-securite]
source: SFEIR
---
# sfeir-verification-code-agents-claude-code-2026-11-19

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **19 novembre 2026** (~13 000 signes, trois sources). Il restitue le billet d'**Addy Osmani** « How the Claude Code team thinks about verification » (blog Claude Code, **16 novembre 2026**), qui ouvre sur *« the vast majority of our code (~90%) is written and reviewed by Claude »*. Quatre apports. **(A)** Trois familles de tests jugées difficiles à tromper pour un agent : **end-to-end** en priorité, **de propriétés**, **différentiels** pour les migrations. **(B)** La vérification par exécution : un skill **`verify`**, **trois tentatives** avant de passer la main à un humain. **(C)** Des règles hors de portée du changement : une checklist de fiabilité de **39 items** déclenchés par le diff (**3 à 10** par changement), un `REVIEW.md` lu depuis la branche de base, et une barrière de commit à trois positions (**off**, **observe**, **enforce**). **(D)** La mesure des vérificateurs eux-mêmes (rappel à trois étages, constats Important/Nit/Pre-existing) et la conversion des ratés en règles. L'article signale que les chiffres sont déclarés par Anthropic et non mesurés indépendamment. Prolonge [[osmani-agentic-verification-2026-10-14]].

## Titre Article

Comment l'équipe Claude Code vérifie le code écrit par ses agents

## Date

2026-11-19

## URL

https://www.sfeir.com/articles/verification-code-agents-equipe-claude-code/

## Keywords

vérification, Claude Code, Addy Osmani, agents de codage, tests end-to-end, tests de propriétés, property-based testing, tests différentiels, feature map, skill verify, trois tentatives, checklist de fiabilité, REVIEW.md, branche de base, barrière de commit, mode observe, tests instables, flaky tests, rappel, revue de code, CLAUDE.md, hooks, SFEIR

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé publié sur sfeir.com, site éditorial du groupe.

## Ton

Article de restitution méthodologique en français, adressé aux équipes qui confient du code à des agents. Le texte suit le billet source section par section et en cite largement la lettre en anglais (« If a check is still failing after three rounds, Claude stops and brings in a human »), chaque pratique étant rattachée à la note. Le registre est didactique : un tableau compare les trois familles de tests (ce que fait le test, quand l'utiliser, outils), des listes détaillent les règles de revue et les positions de la barrière de commit. L'article ajoute une couche de transposition, « Ce que votre équipe peut reprendre », en cinq étapes ordonnées, et des renvois vers ses propres articles (golden master WinDev, anneau de contraintes). Il termine par une réserve explicite : les chiffres (90 %, 10 points, 39 items) sont déclarés par Anthropic.

## Pense-betes

- **Source** : Addy Osmani, « How the Claude Code team thinks about verification », blog Claude Code, 16 novembre 2026 ; environ **90 %** du code de l'équipe écrit et revu par Claude.
- **Calcul d'ouverture** : sans boucles de vérification, *« one or two Claudes at a time »* ; avec, *« dozens or hundreds in parallel »*. Un correcteur séparé notant contre une grille : jusqu'à **+10 points** de taux de réussite (mesure interne, non reproduite).
- **Principe** : vérifier coûtait cher (tests, specs, end-to-end), le demander à un agent ne coûte presque plus rien. Échec répété → **hook** ou règle dans `CLAUDE.md`.
- **À écarter** : tests **instables** (ils apprennent à l'agent à relancer) et **lents**.
- **Trois familles** : **end-to-end** (*« If you have to focus on one test type, pick end-to-end »*, trace + capture + diagnostic ; *feature map* = guide et grille) ; **propriétés** (invariants, aller-retour, idempotence ; fast-check, Hypothesis, proptest ; cas *« not created with the same bias as the agent »*) ; **différentiel** (ancien système = oracle, pour migrations).
- **Exécuter** : *« Running the app end to end matters more than tests. »* Skill **`verify`** dans `.claude/skills/` près du code (extension Chrome, MCP iOS/Android, computer use) ; **trois tentatives** puis un humain.
- **Règles hors de portée** : les propriétaires du code écrivent les contrôles ; checklist de **39 items** déclenchés par le diff (**3 à 10** lancés) ; un relecteur, plusieurs passes ; **`REVIEW.md` lu depuis la branche de base**, jamais depuis la PR ; contrôles bon marché avant la PR.
- **Barrière de commit** : tampon de vérification sur chaque commit (y compris « none ») ; **off / observe / enforce** ; démarrage en observe ; soupape après deux blocages.
- **Vérifier les vérificateurs** : reverts, rejets, rappel à trois étages, constats Important / Nit / Pre-existing ; motifs vus dans **≥ 2 PR** soumis à trois agents contradicteurs puis approuvés par un humain.
- **Tests instables** : ni skip, ni sleep, ni retry ; sinon suppression motivée. Tout s'élague.
- **À relier** : [[osmani-lunt-wang-code-review-claude-code-2026-10-15]] (revue de code chez Claude Code).

## RésuméDe400mots

L'article de SFEIR AI restitue un billet publié le 16 novembre 2026 par Addy Osmani sur le blog de Claude Code, « How the Claude Code team thinks about verification ». Le point de départ est un chiffre déclaré : environ 90 % du code de l'équipe est écrit et revu par Claude. Personne ne relit chaque diff ; l'équipe a donc construit une couche de vérification qui demande aux agents de prouver que leurs changements fonctionnent, et traite cette couche comme un système à part entière.

Selon le billet, sans boucles de vérification, un développeur ne pilote qu'un ou deux agents ; avec elles, des dizaines ou des centaines. Un correcteur séparé, qui note le travail contre une grille, a amélioré le taux de réussite de jusqu'à dix points sur une tâche interne. Les tests, autrefois coûteux à écrire, ne coûtent presque plus rien à demander à un agent, et les échecs répétés deviennent des hooks ou des règles de CLAUDE.md.

L'équipe écarte les tests instables et lents, puis investit dans trois familles. Le test end-to-end vient en premier parce qu'un agent le trompe difficilement et qu'il produit un meilleur diagnostic ; une feature map sert de guide et de grille. Les tests de propriétés couvrent les cas que l'agent ne pense pas à tester. Les tests différentiels font de l'ancien système l'oracle du nouveau lors des migrations.

Vérifier veut d'abord dire exécuter. Un skill verify, rangé près du code, décrit comment lancer et piloter l'application ; après trois tentatives infructueuses, Claude s'arrête et appelle un humain. Les règles de contrôle sont écrites par les propriétaires du code, une checklist de 39 items se déclenche selon le diff, et le fichier REVIEW.md est lu depuis la branche de base pour qu'un agent ne puisse pas réécrire les règles qui le jugent. Chaque commit porte un tampon de vérification, et une barrière de commit passe par trois positions, off, observe et enforce, en démarrant toujours en observe.

L'équipe mesure aussi ses vérificateurs : reverts, rejets, rappel à trois étages, classement des constats. Les ratés deviennent des règles après validation par des agents contradicteurs et un humain. Les tests instables ne peuvent être ni ignorés ni relancés en boucle.

L'article propose cinq étapes à reprendre hors de Claude Code, du parcours end-to-end à la barrière en mode observe, et rappelle que les chiffres cités sont déclarés par Anthropic.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Comment l'équipe Claude Code vérifie le code écrit par ses agents | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Addy Osmani | PERSONNE | publie | How the Claude Code team thinks about verification | DOCUMENT | 0.96 | STATIQUE | déclaré_article |
| Comment l'équipe Claude Code vérifie le code écrit par ses agents | DOCUMENT | référence | How the Claude Code team thinks about verification | DOCUMENT | 0.96 | STATIQUE | déclaré_article |
| How the Claude Code team thinks about verification | DOCUMENT | mesure | environ 90 % du code de l'équipe Claude Code écrit et revu par Claude | MESURE | 0.88 | STATIQUE | déclaré_article |
| correcteur séparé | METHODOLOGIE | améliore | jusqu'à +10 points de taux de réussite | MESURE | 0.8 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | tests end-to-end | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | tests de propriétés | METHODOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| tests différentiels | METHODOLOGIE | s_applique_à | migrations à grande échelle | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| skill verify | METHODOLOGIE | fait_partie_de | Claude Code | TECHNOLOGIE | 0.86 | DYNAMIQUE | déclaré_article |
| Addy Osmani | PERSONNE | recommande | prioriser les tests end-to-end | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | REVIEW.md | DOCUMENT | 0.88 | DYNAMIQUE | déclaré_article |
| REVIEW.md | DOCUMENT | réduit | modification par l'agent des règles qui le jugent | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| barrière de commit | METHODOLOGIE | utilise | mode observe | CONCEPT | 0.86 | DYNAMIQUE | déclaré_article |
| Addy Osmani | PERSONNE | affirme_que | après trois tentatives échouées, Claude s'arrête et appelle un humain | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| Addy Osmani | PERSONNE | prédit | le métier passe de la relecture des diffs à la définition du « fini » et à la revue des preuves | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | lire les règles de revue depuis la branche de base, jamais depuis la PR | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les chiffres de l'article sont déclarés par Anthropic sans mesure indépendante | AFFIRMATION | 0.86 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle (groupe SFEIR) | AJOUT |
| Addy Osmani | PERSONNE | publication | « How the Claude Code team thinks about verification », 16 novembre 2026 | AJOUT |
| How the Claude Code team thinks about verification | DOCUMENT | support | Blog Claude Code (claude.dev), 16 novembre 2026 | AJOUT |
| skill verify | METHODOLOGIE | rôle | Procédure de démarrage et de pilotage de l'application, rangée dans .claude/skills/ | AJOUT |
| REVIEW.md | DOCUMENT | règle | Lu depuis la branche de base, jamais depuis les changements de la PR | AJOUT |
| barrière de commit | METHODOLOGIE | positions | off, observe, enforce ; démarrage en observe, soupape après deux blocages | AJOUT |
| tests différentiels | METHODOLOGIE | principe | Ancien et nouveau système sur les mêmes entrées, l'ancien sert d'oracle | AJOUT |
| tests de propriétés | METHODOLOGIE | outils | fast-check, Hypothesis, proptest | AJOUT |
