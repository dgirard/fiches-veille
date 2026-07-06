---
themes: [agents-codage-ia-skills]
source: "claude.com (Thariq Shihipar)"
---
# shihipar-claude-code-lessons-building-skills-2026-06-03

## Veille
Article de blog **Anthropic / claude.com** signé **Thariq Shihipar** (Member of Technical Staff, équipe Claude Code), publié le **3 juin 2026**, qui capitalise le **retour d'expérience interne** d'Anthropic sur la conception et l'usage des **Skills**. **Thèse de cadrage** : une Skill n'est pas un simple fichier markdown mais un **dossier** (instructions + scripts + ressources + config + hooks) que l'agent **découvre et manipule** ; *« You should think of the entire file system as a form of context engineering and progressive disclosure. »* L'article propose deux apports structurants. **(A) Une taxonomie de 9 catégories de skills** observées chez Anthropic : (1) **Library/API Reference** (doc de libs/CLI internes avec *gotchas* — ex. `billing-lib`, `internal-platform-cli`, `sandbox-proxy`) ; (2) **Product Verification** (test/vérif via Playwright ou tmux — `signup-flow-driver`, `checkout-verifier`, `tmux-cli-driver`) ; (3) **Data Fetching & Analysis** (accès stacks data/monitoring — `funnel-query`, `cohort-compare`, `grafana`, `datadog`) ; (4) **Business Process Automation** (workflows répétitifs — `standup-post`, `weekly-recap`, `create-<ticket>-ticket`) ; (5) **Code Scaffolding** (boilerplate framework — `new-migration`, `create-app`) ; (6) **Code Quality & Review** (`adversarial-review`, `code-style`, `testing-practices`) ; (7) **CI/CD & Deployment** (`babysit-pr`, `deploy-<service>`, `cherry-pick-prod`) ; (8) **Runbooks** (diagnostic multi-outils — `<service>-debugging`, `oncall-runner`, `log-correlator`) ; (9) **Infrastructure Operations** (maintenance avec garde-fous — `<resource>-orphans`, `cost-investigation`). **(B) Un jeu de bonnes pratiques** : ne pas redire l'évident (*« Claude already knows how to code and can read your codebase »* → cibler ce qui **contredit le comportement par défaut**) ; soigner la **section Gotchas** (*« the highest-signal content in any skill »*) ; **progressive disclosure** via l'arborescence (pointer vers des fichiers de référence selon la situation plutôt que tout charger d'emblée) ; **descriptions pensées pour le modèle** (*« the description field is not a summary, it's a description of when to trigger this skill »*) ; **setup flows** (config dans `config.json`, sinon demander via `AskUserQuestion`) ; **mémoire persistante** (logs append-only / JSON via la variable `${CLAUDE_PLUGIN_DATA}`) ; **helper scripts** (*« lets Claude spend its turns on composition… rather than reconstructing boilerplate »*) ; **hooks conditionnels** (activés seulement le temps de la skill — ex. hook de sécurité bloquant les commandes destructrices). **Distribution chez Anthropic** : skills rangées dans `./.claude/skills`, partage informel via Slack dans un dossier sandbox, puis promotion par **PR** vers le **marketplace** interne quand elles gagnent en traction ; **mesure d'usage** via un **hook `PreToolUse`** qui logue les invocations (révèle les skills populaires et celles sous-utilisées). Suite directe de la fiche [[shihipar-claude-code-html-unreasonable-effectiveness-markdown-2026-05-10]] (même auteur) et complément concret aux fiches Skills d'Anthropic/Willison/Vincent et au *harness engineering*.

## Titre Article
Lessons from building Claude Code: How we use skills

## Date
2026-06-03

## URL
https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills

## Keywords
skills, Claude Code, Anthropic, retour d'expérience interne, dossier de skill, context engineering, progressive disclosure, neuf catégories de skills, library API reference, product verification, data fetching analysis, business process automation, code scaffolding, code quality review, CI/CD deployment, runbooks, infrastructure operations, gotchas, section gotchas, Claude already knows how to code, description as trigger, description field is not a summary, setup flow, config.json, AskUserQuestion, mémoire persistante, append-only logs, CLAUDE_PLUGIN_DATA, helper scripts, composition vs boilerplate, hooks conditionnels, hook de sécurité, PreToolUse hook, mesure d'usage des skills, marketplace interne, .claude/skills, distribution par PR, sandbox Slack, Playwright, tmux, grafana, datadog, adversarial-review, babysit-pr, oncall-runner, Thariq Shihipar, trq212

## Authors
**Thariq Shihipar** (Member of Technical Staff chez Anthropic, équipe **Claude Code** ; @trq212 / @trq sur X, thariqs.github.io), pour le blog **claude.com**. Même auteur que la fiche *Using Claude Code: The Unreasonable Effectiveness of HTML* (2026-05-10). Publié le **3 juin 2026**.

## Ton
**Profil** : Retour d'expérience d'ingénieur-praticien (*builder-to-builder*), première personne du pluriel (*« how we use skills »*, *« we use a PreToolUse hook »*), à destination d'un public technique averti — ingénieurs et power-users construisant leurs propres skills. Registre **didactique-prescriptif, dense et opérationnel**, niveau technique **élevé** (variables d'environnement, hooks, arborescence de fichiers, conventions de nommage).

**Style** : Prose d'ingénierie structurée en deux blocs — une **taxonomie** (9 catégories avec exemples de noms de skills réels d'Anthropic) puis une **liste de bonnes pratiques** actionnables. Autorité par la position d'**insider** : ce que l'équipe qui a construit Claude Code observe *de l'intérieur*. Chaque conseil est ancré dans un constat concret (*« common failure points that Claude runs into »*) plutôt qu'une généralité. Honnêteté sur la finalité réelle des objets (la `description` sert au routage du modèle, pas à l'humain).

**Aphorismes-clés** :
- ***« Claude already knows how to code and can read your codebase. »*** (anti-redondance : ne documentez que ce qui contredit le défaut).
- ***« The highest-signal content in any skill is the Gotchas section. »***
- ***« You should think of the entire file system as a form of context engineering and progressive disclosure. »***
- ***« The description field is not a summary, it's a description of when to trigger this skill. »***
- ***« Giving Claude scripts and libraries lets Claude spend its turns on composition, deciding what to do next rather than reconstructing boilerplate. »***

**Métaphores / cadres travaillés** :
- ***Le système de fichiers comme context engineering*** — l'arborescence d'une skill = dispositif de divulgation progressive, pas un simple sac d'instructions.
- ***La description comme déclencheur (trigger), pas comme résumé*** — réoriente la rédaction vers le routage par le modèle.
- ***Les turns du modèle comme ressource rare*** — les helper scripts économisent le raisonnement pour la composition de haut niveau.
- ***Cycle de vie organique des skills*** — du dossier sandbox partagé sur Slack à la promotion par PR vers le marketplace, mesurée par les hooks d'usage.

**Position épistémique** : témoignage d'autorité interne (Anthropic / équipe Claude Code), riche en exemples nommés ; prescriptif mais ancré dans l'observation empirique d'un usage à l'échelle de l'entreprise. À pondérer comme retour d'expérience d'éditeur (pas une étude indépendante), mais avec une crédibilité forte sur le « comment » opérationnel.

**Autorité** : (a) **insider Anthropic** sur l'outil de référence ; (b) **taxonomie immédiatement réutilisable** (9 catégories couvrant tout le SDLC + ops) ; (c) **exemples concrets** de noms de skills réels ; (d) conseils **testés à l'échelle** (marketplace + mesure d'usage interne).

## Pense-betes

- **Date / source** : **3 juin 2026**, blog **claude.com** (Anthropic). Auteur : **Thariq Shihipar** (équipe Claude Code, @trq212). Suite directe de sa fiche [[shihipar-claude-code-html-unreasonable-effectiveness-markdown-2026-05-10]].
- **Cadrage clé** : une Skill = **un dossier** (instructions + scripts + ressources + config + hooks), pas un seul fichier .md. *« The entire file system as a form of context engineering and progressive disclosure. »*

### Les 9 catégories de skills (taxonomie Anthropic)

| # | Catégorie | Finalité | Exemples cités |
|---|-----------|----------|----------------|
| 1 | **Library/API Reference** | Doc libs/CLI internes + gotchas | `billing-lib`, `internal-platform-cli`, `sandbox-proxy` |
| 2 | **Product Verification** | Test/vérif (Playwright, tmux) | `signup-flow-driver`, `checkout-verifier`, `tmux-cli-driver` |
| 3 | **Data Fetching & Analysis** | Accès data/monitoring + patterns de requête | `funnel-query`, `cohort-compare`, `grafana`, `datadog` |
| 4 | **Business Process Automation** | Workflows répétitifs | `standup-post`, `weekly-recap`, `create-<ticket>-ticket` |
| 5 | **Code Scaffolding** | Boilerplate framework | `new-migration`, `create-app`, `new-<framework>-workflow` |
| 6 | **Code Quality & Review** | Style + revue | `adversarial-review`, `code-style`, `testing-practices` |
| 7 | **CI/CD & Deployment** | Build / push / deploy | `babysit-pr`, `deploy-<service>`, `cherry-pick-prod` |
| 8 | **Runbooks** | Diagnostic multi-outils par symptôme | `<service>-debugging`, `oncall-runner`, `log-correlator` |
| 9 | **Infrastructure Operations** | Maintenance + garde-fous | `<resource>-orphans`, `dependency-management`, `cost-investigation` |

### Bonnes pratiques (checklist)

- **Anti-redondance** : *« Claude already knows how to code »* → ne documenter que ce qui **contredit l'approche par défaut** du modèle.
- **Section Gotchas** = contenu **le plus à fort signal** ; la construire à partir des points d'échec réels (ex. incohérences de nommage de champs, tables append-only).
- **Progressive disclosure** : pointer Claude vers des fichiers de référence selon la situation, plutôt que tout charger d'emblée.
- **Flexibilité** : donner l'info nécessaire sans sur-contraindre — laisser l'agent s'adapter.
- **Setup flow** : stocker la config (`config.json`) ; si manquante, demander à l'utilisateur via **`AskUserQuestion`**.
- **Description = trigger** : rédiger pour le **routage du modèle**, avec phrases d'activation — *« not a summary, it's a description of when to trigger this skill »*.
- **Mémoire** : logs append-only / JSON, répertoire stable via **`${CLAUDE_PLUGIN_DATA}`** → l'agent se souvient des exécutions passées.
- **Helper scripts** : fournir libs/fonctions → l'agent dépense ses *turns* en **composition**, pas en reconstruction de boilerplate.
- **Hooks conditionnels** : activés **seulement** pendant l'invocation de la skill et pour la durée de la session (ex. hook bloquant les commandes destructrices) — utiles en contexte, indésirables en *always-on*.

### Distribution & mesure (chez Anthropic)

- Skills rangées dans **`./.claude/skills`** (repo) ou via **marketplace** de plugins interne.
- **Cycle organique** : dossier sandbox → partage informel Slack → traction → **PR** vers le marketplace.
- **Mesure d'usage** : hook **`PreToolUse`** qui logue les invocations → repère skills populaires vs sous-utilisées.

### À mobiliser en mission / présentation

- **Grille de cartographie** clé en main : auditer les skills d'une équipe par les **9 catégories** (couvre dev + data + ops + process), repérer les trous.
- Le triptyque **Gotchas / progressive disclosure / description-as-trigger** = règles d'or de rédaction de skills, à intégrer dans une *skill-writing guideline* cabinet.
- Converge avec le *harness engineering* (Böckeler, niveau 5 de l'échelle Every [[taylor-entis-every-eight-levels-ai-adoption-2026-06-02]]) et avec les fiches Skills (Anthropic *Agent Skills*, Willison, Vincent *Superpowers*, Lattice). Apport spécifique : le **REX d'usage à l'échelle entreprise** + la **mécanique de distribution/mesure**.

## RésuméDe400mots

Publié le **3 juin 2026** sur le blog d'Anthropic par **Thariq Shihipar** (équipe Claude Code), cet article distille le retour d'expérience interne de l'entreprise sur l'usage des **Skills**. Le cadrage initial corrige une vision réductrice : une Skill n'est pas un fichier markdown isolé mais un **dossier** réunissant instructions, scripts, ressources, configuration et hooks, que l'agent **explore et manipule**. La maxime structurante : *« You should think of the entire file system as a form of context engineering and progressive disclosure. »*

L'article apporte d'abord une **taxonomie de neuf catégories** de skills observées chez Anthropic, illustrées par des noms réels : **(1) Library/API Reference** (doc de libs/CLI internes avec gotchas) ; **(2) Product Verification** (test via Playwright/tmux) ; **(3) Data Fetching & Analysis** (grafana, datadog, requêtes type) ; **(4) Business Process Automation** (standup, recaps, tickets) ; **(5) Code Scaffolding** (boilerplate, migrations) ; **(6) Code Quality & Review** (`adversarial-review`, code-style) ; **(7) CI/CD & Deployment** (`babysit-pr`, deploy) ; **(8) Runbooks** (diagnostic multi-outils par symptôme) ; **(9) Infrastructure Operations** (maintenance avec garde-fous).

Vient ensuite un corpus de **bonnes pratiques**. La première est l'**anti-redondance** : *« Claude already knows how to code and can read your codebase »* — il faut documenter ce qui **contredit le comportement par défaut**, pas l'évident. Le contenu le plus précieux est la **section Gotchas** (*« the highest-signal content in any skill »*), nourrie des points d'échec réellement rencontrés. La **progressive disclosure** s'opère via l'arborescence : on oriente Claude vers le bon fichier de référence selon la situation. Les **descriptions** doivent être pensées pour le **modèle**, pas l'humain : *« the description field is not a summary, it's a description of when to trigger this skill. »* Pour la configuration, un **setup flow** stocke les paramètres (`config.json`) ou interroge l'utilisateur via `AskUserQuestion`. La **mémoire persistante** passe par des logs append-only/JSON dans le répertoire stable `${CLAUDE_PLUGIN_DATA}`. Les **helper scripts** libèrent le raisonnement du modèle : *« lets Claude spend its turns on composition… rather than reconstructing boilerplate. »* Enfin, des **hooks conditionnels** (ex. blocage de commandes destructrices) ne s'activent que le temps de la skill.

Côté **distribution**, Anthropic range ses skills dans `./.claude/skills` ; elles émergent dans un dossier sandbox partagé via Slack, gagnent en traction, puis sont promues par **PR** vers un marketplace interne. L'**usage est mesuré** par un hook `PreToolUse` qui logue les invocations, révélant les skills populaires et celles à retravailler. Un guide opérationnel directement réutilisable pour rédiger, distribuer et mesurer des skills à l'échelle d'une organisation.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Thariq Shihipar | PERSONNE | publie | Lessons from building Claude Code: How we use skills | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Lessons from building Claude Code: How we use skills | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Thariq Shihipar | PERSONNE | fait_partie_de | équipe Claude Code | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Skill | CONCEPT | est_instance_de | dossier d'instructions scripts et ressources | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| système de fichiers d'une skill | CONCEPT | est_instance_de | progressive disclosure | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | utilise | une taxonomie de 9 catégories de skills | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| Thariq Shihipar | PERSONNE | affirme_que | la section Gotchas est le contenu à plus fort signal d'une skill | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| champ description d'une skill | CONCEPT | permet | le déclenchement de la skill par le modèle | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| helper scripts | CONCEPT | permet | de consacrer les turns du modèle à la composition | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| variable CLAUDE_PLUGIN_DATA | TECHNOLOGIE | permet | un répertoire stable de mémoire persistante | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| hooks de skill | TECHNOLOGIE | s_applique_à | la seule durée d'invocation de la skill | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | utilise | un marketplace interne par PR pour distribuer les skills | METHODOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| hook PreToolUse | TECHNOLOGIE | mesure | l'usage des skills | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Thariq Shihipar | PERSONNE | recommande | ne pas documenter ce que Claude sait déjà | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| AskUserQuestion | TECHNOLOGIE | permet | de collecter la configuration manquante d'une skill | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Thariq Shihipar | PERSONNE | rôle | Member of Technical Staff, équipe Claude Code (Anthropic) | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / éditeur de Claude Code | AJOUT |
| Lessons from building Claude Code: How we use skills | DOCUMENT | catégorie | REX / guide opérationnel sur les Skills | AJOUT |
| Skill | CONCEPT | définition | Dossier (instructions + scripts + ressources + config + hooks) découvrable par l'agent | AJOUT |
| taxonomie 9 catégories de skills | CONCEPT | liste | Library/API, Verification, Data, Process, Scaffolding, Quality, CI/CD, Runbooks, Infra Ops | AJOUT |
| section Gotchas | CONCEPT | usage | Documenter les points d'échec réels — contenu à plus fort signal | AJOUT |
| progressive disclosure | METHODOLOGIE | principe | Orienter vers le bon fichier de référence selon la situation | AJOUT |
| champ description | CONCEPT | finalité | Déclencheur de routage pour le modèle, pas résumé humain | AJOUT |
| CLAUDE_PLUGIN_DATA | TECHNOLOGIE | usage | Répertoire stable pour mémoire persistante (logs/JSON append-only) | AJOUT |
| hooks conditionnels | TECHNOLOGIE | usage | Activés seulement le temps de la skill (ex. blocage commandes destructrices) | AJOUT |
| hook PreToolUse | TECHNOLOGIE | usage | Logue les invocations de skills pour mesurer l'usage | AJOUT |
| marketplace interne Anthropic | METHODOLOGIE | mécanique | sandbox Slack → traction → promotion par PR | AJOUT |
