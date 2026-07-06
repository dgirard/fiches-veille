---
themes: [agents-codage-ia-skills]
source: "Every AI & I Podcast"
---
# wu-cherny-use-claude-code-builders-every-2025-10-29

## Veille
Cat Wu et Boris Cherny (Anthropic) expliquent comment utiliser Claude Code comme ses créateurs : antfooding, plan mode, subagents, hooks et extensibilité — podcast AI & I d'Every

## Titre Article
How to Use Claude Code Like the People Who Built It

## Date
2025-10-29

## URL
https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it

## Keywords
Claude Code, Cat Wu, Boris Cherny, Anthropic, antfooding, plan mode, subagents, slash commands, stop hooks, settings.json, dangerous mode, code review, code migrations, tacit code sharing, MCP, Puppeteer, Playwright, Sentry, Asana, Bash as universal interface, CLI, IDE extension, GUI, non-technical users, extensibility

## Authors
Rhea Purohit (interviewer: Dan Shipper), Cat Wu, Boris Cherny

## Ton
**Profil:** Podcast-Interview-Technical | Troisième personne journalistique | Éducative-Insights | Intermédiaire-Expert

Every (Rhea Purohit) adopte une voix de synthèse de podcast capturant la conversation entre Dan Shipper et les ingénieurs fondateurs de Claude Code. La structure en conseils et thèmes (recommandations pratiques → philosophie → vision future) facilite les enseignements actionnables. Le langage d'initié produit (antfooding, dangerous mode, stop hooks, settings.json) révèle des pratiques internes rarement visibles des utilisateurs externes. Ton d'accès privilégié typique des interviews de podcast avec des bâtisseurs partageant des leçons durement acquises. Les citations directes de Wu/Cherny (« In the end, the result is awesome », « this stuff's just moving so fast ») préservent la voix authentique des praticiens. L'accent sur l'extensibilité et la « hackabilité » reflète la philosophie produit. Format typique des podcasts AI & I (Every, Latent Space, Acquired) capturant la sagesse des bâtisseurs pour un public de praticiens cherchant un avantage compétitif via la connaissance d'initié.

## Pense-betes
- **Antfooding** : employés Anthropic = « ants », dogfooding interne de Claude Code, feedback toutes les 5 minutes
- **Plan mode crucial** : double/triple le taux de succès sur tâches complexes vs tentatives en one-shot
- **Settings.json partagé** : pré-approuver les commandes courantes, bloquer les fichiers risqués, défauts pour toute l'équipe
- **Stop hooks** : actions automatisées quand Claude termine (ex : lancer la suite de tests, corriger les échecs, continuer)
- **Subagents qui s'affrontent** : la revue de code lance plusieurs subagents qui se contestent mutuellement
  - Premier passage : style, historique, bugs évidents
  - Deuxième passage : 5 subagents cherchent les failles des constats initiaux
  - Résultat : trouve les vrais problèmes, élimine les faux positifs
- **Migrations de code** : des ingénieurs dépensent 1 000 $+/mois, l'agent principal crée la to-do, les subagents traitent en parallèle
- **Entrées de journal** : Claude écrit des logs après chaque tâche (essayé, réussi, raté), des agents séparés synthétisent les enseignements
- **Partage de code tacite** : les subagents regardent comment d'autres apps gèrent une fonctionnalité, sans API
- **Slash commands favorites** :
  - `/commit` : automatise commits/push sans permission
  - `/feature-dev` : développement structuré (spec → plan → to-do → pas à pas)
  - `/code-review` : premier passage sur les pull requests, l'humain approuve le merge final
- **Top MCPs** : Puppeteer, Playwright, Sentry, Asana
- **Bash comme interface universelle** : remplace des dizaines d'outils spécialisés, réduit le contexte, « couteau suisse »
- **Dangerous mode** : auto-acceptation de tous les changements, modèles actuels tournent 30 h d'affilée, prochains probablement des jours
- **Form factors en expérimentation** : CLI, extension IDE, GUI, intégration GitHub, web, mobile
- **Défi à venir** : des Claude surveillant des Claude, optimiser la communication Claude-à-Claude
- **Utilisateurs non techniques** : data scientists, chercheurs, analystes, product managers adoptent l'outil
- **Extension VS Code** : interface pointer-cliquer vs commandes terminal
- **Philosophie** : construire pour tous, laisser les experts repousser les limites, observer les « abus » → construire pour cette demande
- **Discipline d'élagage** : retirer des fonctionnalités quand une approche plus simple est trouvée, ne pas alourdir
- **Transformation d'Every** : chaque fonctionnalité facilite la suivante, le CEO livre sur des codebases inconnues, des non-techniciens dans le terminal
- **Parallèle Meta** : Facebook Dating né de l'observation de 60 % de vues de profils de genre opposé hors amis

## RésuméDe400mots

Cat Wu et Boris Cherny, founding engineers de Claude Code chez Anthropic, partagent dans le podcast AI & I d'Every comment ils utilisent leur propre produit et ce qu'ils ont appris en observant des centaines d'ingénieurs l'adopter via "antfooding" (Anthropic employees = "ants", leur version du dogfooding).

**Insights pratiques d'utilisation**

**Plan mode est critique** : ne pas tenter de one-shot tout. Activer plan mode (Claude map step-by-step avant code) double ou triple chances de succès sur tâches complexes en alignant l'approche avant exécution.

**Settings.json partagé** : créer fichier settings dans codebase avec commands pré-approuvées (routine tasks sans permission) et fichiers bloqués (jamais toucher). Équipe entière hérite sensible defaults vs configuration individuelle.

**Stop hooks créatifs** : actions automatisées quand Claude finit. Exemple : run test suite, si failures, dire à Claude fix problems et continue testing au lieu de s'arrêter. "You can just make the model keep going until the thing is done."

**Subagents combattants** : Cherny spawn plusieurs subagents pour code review se challengeant mutuellement. Premier pass : style guidelines, project history, obvious bugs. Deuxième pass : 5 subagents poking holes dans findings originaux. Résultat : capture real issues sans false alarms.

**Code migrations** : engineers dépensent $1,000+/mois. Main agent crée to-do list, subagents tackle items en parallèle. Particulièrement efficace pour switching testing frameworks où output facile à vérifier.

**Diary entries et institutional knowledge** : Claude écrit logs après chaque tâche. Agents séparés review et distillent en insights réutilisables. Défi : distinguer instructions one-off ("make button pink") vs genuine best practices applicables universellement.

**Tacit code sharing chez Every** : lors de nouvelle feature, subagents examinent comment autres apps l'ont déjà fait. "You don't need API or ask anyone, just [ask AI] 'How do we do this already?'"

**Slash commands favoris** : `/commit` (automate commits/push), `/feature-dev` (spec → plan → to-do → execution structurée), `/code-review` (first pass PRs, human final approval).

**Philosophie produit**

**Build for everyone, experts push edges** : produit simple enough pour anyone, powerful enough pour advanced users discovering novel use cases creators never imagined. Observer comment users "abuse" produit révèle latent demand pour nouvelles features. Parallèle Meta : Facebook Dating née de 60% profile views opposite-gender non-friends.

**Extensibility core belief** : chaque engineering environment unique. Slash commands, hooks, plugins permettent users shape workflow. "Insert determinism at pretty much any step." Nouveau user experience intuitive : "drop in and it works."

**Simplify as you scale** : discipline de pruning autant que building. Unship features quand approche plus simple trouvée. Bash comme universal interface remplace dozens specialized tools, réduit context : "Swiss Army knife vs drawer full single-purpose gadgets."

**Vision future**

**New form factors exploration** : CLI, IDE extension, GUI, GitHub integration, web, mobile. "No one knows what [new] form factors are, this stuff's moving so fast."

**Dangerous mode evolution** : current models run 30h straight. Next generation likely days. Problème pratique : can't leave laptop open days. Challenge émergent : Claudes monitoring other Claudes, optimize Claude-to-Claude communication vs human inspection.

**Non-technical users** : data scientists, researchers, analysts, PMs adoptent. VS Code extension offre point-and-click interface vs terminal. Every lance Claude Code for Beginners camp (Nov 19) : hands-on workshop, install, give tasks, build app end-to-end, no programming experience required.

L'article illustre comment Every transformed via Claude Code : chaque feature rend suivante easier, CEO ships unknown codebases, non-technical people soudain dans terminals.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Boris Cherny | PERSONNE | a_créé | Claude Code | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Cat Wu | PERSONNE | a_créé | Claude Code | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | emploie | Boris Cherny | PERSONNE | 0.97 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | emploie | Cat Wu | PERSONNE | 0.97 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | antfooding | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Boris Cherny | PERSONNE | recommande | plan mode | METHODOLOGIE | 0.96 | ATEMPOREL | déclaré_article |
| Boris Cherny | PERSONNE | recommande | settings.json | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| Boris Cherny | PERSONNE | utilise | subagents | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | Bash | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Cat Wu | PERSONNE | recommande | Puppeteer | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Cat Wu | PERSONNE | recommande | Playwright | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Boris Cherny | PERSONNE | prédit | les prochains modèles tourneront plusieurs jours en autonomie | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | s_applique_à | utilisateurs non-techniques | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| Boris Cherny | PERSONNE | affirme_que | l'observation des usages imprévus révèle la demande latente | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | améliore | Every | ORGANISATION | 0.92 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Boris Cherny | PERSONNE | rôle | Ingénieur fondateur de Claude Code | AJOUT |
| Cat Wu | PERSONNE | rôle | Ingénieure fondatrice de Claude Code | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI / IA | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
| antfooding | METHODOLOGIE | définition | Dogfooding interne chez Anthropic ("ants" = employés) | AJOUT |
| plan mode | METHODOLOGIE | effet | Double ou triple le taux de succès sur tâches complexes | AJOUT |
| settings.json | TECHNOLOGIE | usage | Fichier partagé pour pré-approuver commandes et bloquer fichiers risqués | AJOUT |
| stop hooks | CONCEPT | usage | Actions automatisées déclenchées quand Claude finit une tâche | AJOUT |
| subagents | CONCEPT | usage | Instances Claude parallèles se challengeant mutuellement pour code review | AJOUT |
| dangerous mode | CONCEPT | durée | Modèles actuels capables de tourner 30h en continu | AJOUT |
| Every | ORGANISATION | secteur | Médias / Outils IA | AJOUT |
| Bash | TECHNOLOGIE | rôle | Interface universelle entre Claude Code et le système | AJOUT |
| Puppeteer | TECHNOLOGIE | catégorie | MCP pour automatisation de navigateur | AJOUT |
| Playwright | TECHNOLOGIE | catégorie | MCP pour tests d'applications web | AJOUT |
| demande latente | CONCEPT | source | Observation des usages imprévus ("abuse") par les utilisateurs avancés | AJOUT |
