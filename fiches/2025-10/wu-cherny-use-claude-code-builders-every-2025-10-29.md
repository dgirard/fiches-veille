# wu-cherny-use-claude-code-builders-every-2025-10-29

## Veille
Claude Code - Cat Wu & Boris Cherny - Antfooding - Plan Mode - Subagents - Slash Commands - Stop Hooks - Settings.json - Dangerous Mode - AI & I Podcast - Every

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

Every (Rhea Purohit) adopte podcast summary voice capturing conversation between Dan Shipper et Claude Code founding engineers. Structure tips-and-themes format (practical recommendations → philosophy → future vision) facilitates actionable takeaways. Langage product insider (antfooding, dangerous mode, stop hooks, settings.json) reveals internal practices external users rarely see. Tone insider-access typical podcast interviews avec builders sharing hard-won lessons. Direct quotes from Wu/Cherny ("In the end, the result is awesome", "this stuff's just moving so fast") preserve authentic practitioner voice. Emphasis extensibility et hackability reflects product philosophy. Typique AI & I podcast format (Every, Latent Space, Acquired) capturing builder wisdom visant practitioner audience seeking competitive edge through insider knowledge.

## Pense-bêtes
- **Antfooding** : Anthropic employees = "ants", dogfooding Claude Code internally, feedback every 5 minutes
- **Plan mode crucial** : double/triple success rate on complex tasks vs one-shot attempts
- **Settings.json shared file** : pre-approve common commands, block risky files, team-wide defaults
- **Stop hooks** : automated actions when Claude finishes (ex: run test suite, fix failures, keep going)
- **Subagents fighting** : code review spawns multiple subagents challenging each other's findings
  - First pass: style, history, obvious bugs
  - Second pass: 5 subagents poking holes in findings
  - Result: finds real issues, eliminates false positives
- **Code migrations** : engineers spending $1,000+/month, main agent creates to-do, subagents tackle parallel
- **Diary entries** : Claude writes logs after tasks (what tried, worked, didn't), separate agents synthesize insights
- **Tacit code sharing** : subagents look at how other apps handle features, no API needed
- **Slash commands favorites** :
  - `/commit` : automate commits/push without permission
  - `/feature-dev` : structured development (spec → plan → to-do → step-by-step)
  - `/code-review` : first pass on pull requests, human approves final merge
- **Top MCPs** : Puppeteer, Playwright, Sentry, Asana
- **Bash as universal interface** : replaces dozens of specialized tools, reduces context, "Swiss Army knife"
- **Dangerous mode** : auto-accept all changes, current models run 30h straight, next likely days
- **Form factors experimenting** : CLI, IDE extension, GUI, GitHub integration, web, mobile
- **Challenge ahead** : Claudes monitoring Claudes, optimize Claude-to-Claude communication
- **Non-technical users** : data scientists, researchers, analysts, product managers adopting
- **VS Code extension** : point-and-click interface vs terminal commands
- **Philosophy** : build for everyone, let experts push edges, observe "abuse" → build for that demand
- **Pruning discipline** : unship features when simpler approach found, don't bloat
- **Every transformation** : each feature makes next easier, CEO ships unknown codebases, non-technical in terminals
- **Meta parallel** : Facebook Dating from observing 60% profile views opposite-gender non-friends

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
| Boris Cherny | PERSONNE | a_cofondé | Claude Code | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Cat Wu | PERSONNE | a_cofondé | Claude Code | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | emploie | Boris Cherny | PERSONNE | 0.97 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | emploie | Cat Wu | PERSONNE | 0.97 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | antfooding | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Boris Cherny | PERSONNE | recommande | plan mode | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Boris Cherny | PERSONNE | recommande | settings.json | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| Boris Cherny | PERSONNE | utilise | subagents | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | s_appuie_sur | Bash | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Cat Wu | PERSONNE | recommande | Puppeteer | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Cat Wu | PERSONNE | recommande | Playwright | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Cherny | PERSONNE | prédit | dangerous mode | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | cible | utilisateurs non-techniques | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| Boris Cherny | PERSONNE | affirme_que | demande latente | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Every | ORGANISATION | a_été_transformé_par | Claude Code | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Boris Cherny | PERSONNE | rôle | Ingénieur fondateur de Claude Code | AJOUT |
| Cat Wu | PERSONNE | rôle | Ingénieure fondatrice de Claude Code | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI / IA | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
| antfooding | METHODOLOGIE | définition | Dogfooding interne chez Anthropic ("ants" = employés) | AJOUT |
| plan mode | CONCEPT | effet | Double ou triple le taux de succès sur tâches complexes | AJOUT |
| settings.json | TECHNOLOGIE | usage | Fichier partagé pour pré-approuver commandes et bloquer fichiers risqués | AJOUT |
| stop hooks | CONCEPT | usage | Actions automatisées déclenchées quand Claude finit une tâche | AJOUT |
| subagents | CONCEPT | usage | Instances Claude parallèles se challengeant mutuellement pour code review | AJOUT |
| dangerous mode | CONCEPT | durée | Modèles actuels capables de tourner 30h en continu | AJOUT |
| Every | ORGANISATION | secteur | Médias / Outils IA | AJOUT |
| Bash | TECHNOLOGIE | rôle | Interface universelle entre Claude Code et le système | AJOUT |
| Puppeteer | TECHNOLOGIE | catégorie | MCP pour automatisation de navigateur | AJOUT |
| Playwright | TECHNOLOGIE | catégorie | MCP pour tests d'applications web | AJOUT |
| demande latente | CONCEPT | source | Observation des usages imprévus ("abuse") par les utilisateurs avancés | AJOUT |
