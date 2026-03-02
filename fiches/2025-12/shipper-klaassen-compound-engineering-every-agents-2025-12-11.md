# shipper-klaassen-compound-engineering-every-agents-2025-12-11
## Veille
Compound Engineering : processus 4 étapes (Plan, Work, Assess, Compound) pour équipes qui codent avec agents IA - Every

## Titre Article
Compound Engineering: How Every Codes With Agents

## Date
2025-12-11

## URL
https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents

## Keywords
compound engineering, agents IA, planification, code review, boucle d'apprentissage, Claude Code, Every, Cora, subagents, compounding, plugin, workflow agentique, spec-driven, 1 développeur = 5, Playwright, MCP, Opus 4.5

## Authors
Dan Shipper, Kieran Klaassen

## Ton
**Profil** : Perspective de CEO tech (Shipper) et de GM produit (Klaassen), registre accessible et enthousiaste, niveau intermédiaire

**Description** : Dan Shipper adopte un ton de manifeste praticien — il part du constat provocateur ("100% du code est écrit par des agents, personne ne code manuellement") pour dérouler un processus structuré en 4 étapes. Le style est celui d'un fondateur qui partage ses pratiques internes avec fierté et pédagogie. Les formulations sont percutantes ("the hard part is almost over" après la planification, "this is the money step" pour le compounding). L'auteur s'appuie sur l'expérience réelle d'Every (5 produits, chacun maintenu par une seule personne) pour crédibiliser un discours qui pourrait sembler utopique. Le public cible est constitué de développeurs et leaders techniques cherchant à transformer leur pratique avec les agents IA.

## Pense-betes
- **Définition compound engineering** : En ingénierie traditionnelle, chaque feature rend la suivante plus difficile. En compound engineering, chaque feature rend la suivante plus facile grâce à une boucle d'apprentissage documentée pour les agents et l'équipe.
- **Boucle en 4 étapes** :
  1. **Plan** (recherche codebase + internet → document de planification complet) — ~40% du temps
  2. **Work** (l'agent exécute le plan step-by-step, utilise MCP/Playwright pour tester en temps réel) — ~10%
  3. **Assess** (review par l'agent + linters + tests + 12 subagents en parallèle, chacun avec une perspective différente) — ~40%
  4. **Compound** (enregistrer les leçons apprises pour les futures sessions) — ~10%
- **Répartition effort** : 80% Plan + Assess, 20% Work + Compound. Le travail de codage proprement dit est la partie la plus simple.
- **Ratio productivité** : 1 développeur avec IA = 5 développeurs d'il y a quelques années, basé sur l'expérience Every.
- **5 produits, 1 personne chacun** : Every gère 5 produits logiciels (dont Cora, Spiral, Sparkle, Monologue) chacun principalement construit et maintenu par une seule personne, utilisés par des milliers de personnes quotidiennement.
- **Plugin compound engineering** : Plugin Claude Code open source qui implémente le workflow exact d'Every. La review utilise 12 subagents parallèles (sécurité, performance, complexité, etc.).
- **Outils** : Claude Code principalement, mais aussi Factory Droid et OpenAI Codex CLI. Approche tool-agnostic.
- **MCP Playwright/XcodeBuildMCP** : L'agent utilise l'app comme un utilisateur pendant le développement — écrit du code, navigue dans l'app, identifie des problèmes, itère.
- **Step Compound — le secret** : Après chaque review, l'agent résume les commentaires et les stocke pour usage futur. Les leçons sont automatiquement distribuées à toute l'équipe car elles vivent dans le codebase ou les plugins. Un nouveau hire est aussi bien armé qu'un vétéran.
- **Questions de routage Cora** : Avant de construire, l'agent doit se demander : "Où est-ce que ça va dans le système ? Faut-il ajouter à l'existant ou créer quelque chose de nouveau ? A-t-on déjà résolu un problème similaire ?"
- **Ce qui devient obsolète** : Écrire des tests manuellement, écrire du code "human-readable" avec documentation abondante, les exercices de code sans internet en entretien, les onboardings de plusieurs semaines, le lock-in technologique dû au legacy.
- **Lien fort avec la veille** : Article fondateur de la philosophie compound engineering qui irrigue Klaassen (Stop Coding Start Planning, Teach AI Think Senior Engineer) et le plugin Every/compound-engineering.

## RésuméDe400mots
Dan Shipper et Kieran Klaassen présentent le **compound engineering**, le processus d'ingénierie développé chez Every où 100% du code est écrit par des agents IA. Le principe fondamental est l'inversion de la complexité : en ingénierie traditionnelle, chaque feature rend la suivante plus difficile ; en compound engineering, chaque feature la rend plus facile grâce à une boucle d'apprentissage qui documente chaque bug, test échoué et insight pour les agents futurs.

Le processus se décompose en **quatre étapes**. Le **Plan** (~40% du temps) commence par une recherche approfondie du codebase, de l'historique git et des meilleures pratiques externes, puis l'agent produit un document de planification complet incluant objectif, architecture proposée, exemples de code et critères de succès. Le **Work** (~10%) est la partie la plus simple : l'agent exécute le plan pas à pas, utilisant des protocoles MCP comme Playwright pour tester l'application comme un utilisateur réel et itérer jusqu'à satisfaction. L'**Assess** (~40%) combine linters, tests unitaires, tests manuels et un système de 12 subagents parallèles qui évaluent le code sous différentes perspectives (sécurité, performance, complexité, architecture). Le **Compound** (~10%) est "l'étape magique" : les leçons de chaque cycle sont résumées par l'agent et stockées pour usage futur.

Le compound engineering fonctionne en pratique chez Every : **5 produits logiciels** (Cora, Spiral, Sparkle, Monologue et autres), chacun principalement construit et maintenu par **une seule personne**, sont utilisés par des milliers d'utilisateurs quotidiennement. L'estimation de productivité est qu'un développeur bien outillé fait aujourd'hui le travail de cinq développeurs d'il y a quelques années.

L'outil principal est **Claude Code**, mais l'approche est tool-agnostic (Factory Droid, OpenAI Codex CLI sont aussi utilisés). Every a publié un **plugin open source** pour Claude Code qui implémente le workflow complet, incluant les 12 subagents de review.

Le mécanisme de compounding est le différenciateur clé : les leçons apprises vivent dans le codebase sous forme de prompts, rendant chaque développeur — y compris les nouveaux arrivants — aussi bien informé qu'un vétéran. L'agent de Cora, par exemple, doit systématiquement se demander où placer une feature dans le système et s'il existe un précédent réutilisable.

Les auteurs concluent que cette approche rend obsolètes de nombreuses pratiques établies : écriture manuelle de tests, documentation exhaustive du code, exercices de codage en entretien sans internet, et lock-in technologique dû au legacy.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Dan Shipper | PERSONNE | a_créé | compound engineering | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Kieran Klaassen | PERSONNE | a_créé | compound engineering | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| compound engineering | METHODOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| compound engineering | METHODOLOGIE | utilise | subagents | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Every | ORGANISATION | pratique | compound engineering | METHODOLOGIE | 0.98 | DYNAMIQUE | déclaré_article |
| Every | ORGANISATION | publie | plugin compound engineering Claude Code | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| compound engineering | METHODOLOGIE | améliore | productivité développeur ×5 | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| Dan Shipper | PERSONNE | affirme_que | 1 développeur IA = 5 développeurs classiques | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| Cora | TECHNOLOGIE | fait_partie_de | Every | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| compound engineering | METHODOLOGIE | est_basé_sur | boucle Plan-Work-Assess-Compound | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| étape Compound | CONCEPT | transforme | leçons apprises en contexte réutilisable | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| plugin compound engineering | TECHNOLOGIE | utilise | 12 subagents parallèles pour review | CONCEPT | 0.96 | DYNAMIQUE | déclaré_article |
| Kieran Klaassen | PERSONNE | gère | Cora | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Dan Shipper | PERSONNE | dirige | Every | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| compound engineering | METHODOLOGIE | catégorie | Processus ingénierie 4 étapes pour développement agentique | AJOUT |
| compound engineering | METHODOLOGIE | étapes | Plan, Work, Assess, Compound | AJOUT |
| Dan Shipper | PERSONNE | rôle | Co-fondateur et CEO, Every | MISE_A_JOUR |
| Kieran Klaassen | PERSONNE | rôle | General Manager Cora, Every | MISE_A_JOUR |
| Every | ORGANISATION | produits | Cora, Spiral, Sparkle, Monologue + incubations | MISE_A_JOUR |
| plugin compound engineering | TECHNOLOGIE | catégorie | Plugin Claude Code open source, workflow Every | AJOUT |
| Cora | TECHNOLOGIE | catégorie | Assistant email IA, produit Every | AJOUT |
