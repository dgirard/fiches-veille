---
themes: [agents-codage-ia-skills, outils-plateformes]
source: "The Pragmatic Engineer"
---
# orosz-salmon-klaric-ramp-inspect-coding-agent-2026-08-25

## Veille

*Deepdive* de **Gergely Orosz**, **Jessica Salmon** et **Ivan Klaric** dans *The Pragmatic Engineer*, publié le **25 août 2026**, à partir d'entretiens avec le CTO de **Ramp** **Rahul Sengottuvelu**, le head of engineering **Hamid Dadkhah** et **Zach Bruggeman**, ingénieur fondateur d'**Inspect**. Article payant : la fiche couvre la partie publique (sections 1 à 3 et l'ouverture de la section 4 ; architecture détaillée, intérieur du sandbox et collaboration restent sous paywall).

**(A)** Un agent de codage *background* interne : sandboxes distants, intégrations internes (télémétrie, feature flags, données), vérification backend et frontend (captures, previews). **75 %** des PR fusionnées chez Ramp viennent d'Inspect, contre **~60 %** en janvier. **(B)** Trois raisons de construire : la limite d'une ou deux sessions par machine locale, l'outillage frontend pour designers, le besoin d'environnements de dev distants. **(C)** Une trajectoire : v1 extension Chrome peu adoptée, v2 (novembre 2025) environnement distant avec **OpenCode** comme harness, choisi pour son API HTTP et son agnosticisme de modèle. **(D)** Une plateforme : plus de **200 agents** internes construits dessus. Principe posé : *« agents should have access to the same context and tools as software engineers »*.

Rejoint [[gray-stripe-minions-coding-agents-part1-2026-02-09]] sur les agents de codage maison des grandes équipes produit.

## Titre Article

Why Ramp built its own in-house coding agent, Inspect

## Date

2026-08-25

## URL

https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect

## Keywords

agent de codage en arrière-plan, background coding agent, agent de codage interne, build vs buy, Ramp, Inspect, OpenCode, sandbox distant, environnement de développement distant, Modal, Cloudflare Durable Objects, Cloudflare Agents SDK, vérification par captures d'écran, boucle de rétroaction, intégrations internes, MCP, plateforme d'agents, ReviewBuddy, Oncall Assistant, Ramp Research, bugfix depuis Slack, agnosticisme de modèle, Minions, Goose

## Authors

Gergely Orosz, Jessica Salmon, Ivan Klaric — *The Pragmatic Engineer* (newsletter Substack de Gergely Orosz).

## Ton

Enquête journalistique d'ingénierie, appuyée sur des entretiens avec la direction technique et l'équipe fondatrice d'Inspect. Le texte part d'une question explicite (pourquoi construire quand l'offre du marché existe) et la traite par le récit : chiffres d'adoption, raisons du choix, historique v1/v2, cas d'usage illustrés de captures de l'interface. Le registre est favorable au sujet : les auteurs jugent l'extension en plateforme *« clever »* et avancent que l'adage *« buy, don't build »* pourrait ne pas s'appliquer aux outils d'IA. Les chiffres proviennent de Ramp et ne sont pas confrontés à une source externe. Le texte situe Inspect parmi d'autres agents internes (Goose chez Block, Minions chez Stripe, River chez Shopify) et renvoie à des contenus antérieurs de la newsletter (Claude Code, podcast avec le créateur d'OpenCode).

## Pense-betes

- **Inspect** : agent de codage *background* de Ramp, ouvert en interne en novembre 2025 ; libre choix d'outil, pourtant **75 %** des PR fusionnées en sont issues (~60 % en janvier 2026).
- **Deux différences revendiquées** face à Claude Code ou Cursor : sandboxes distants (concurrence de sessions illimitée, configuration centralisée, collaboration) et intégrations internes — *« the only constraint on agents' ability is model intelligence »*.
- **Fermer la boucle** : backend = tests, télémétrie, feature flags ; frontend = captures et previews. La vérification par capture existait chez Ramp avant les outils tiers.
- **v1 → v2** : extension Chrome d'édition visuelle pour designers, non adoptée (setup local, peu d'intérêt pour les ingénieurs) ; pivot vers un environnement distant avec agent.
- **OpenCode** retenu comme harness : open source, API HTTP, *« good enough »*, agnostique au modèle.
- **Chiffres** : démarrage d'un environnement provisionné en **moins de 5 s** ; équipe de **5,5** personnes ; **150+** contributeurs ; **~90 %** des PR du dépôt Inspect et **80 %+** de son code écrits par Inspect ; **1 million** de sessions en juillet 2026.
- **Usages** : tâches petites et moyennes en *one-shot*, `@inspect fix this` dans Slack, débogage (debugger, réplique prod en lecture seule assainie, Snowflake).
- **Agents bâtis dessus** : ReviewBuddy (revue de code, une semaine à un ingénieur), Oncall Assistant, Testo (tests Playwright), Ramp Research, Voice of the Customer, PR brouillons depuis Sentry/Datadog.
- **Stack annoncée** : React/Vite, Cloudflare Durable Objects, SQLite, Cloudflare Agents SDK, Modal ; sandbox avec Postgres, Redis, RabbitMQ, Temporal, Chromium, VS Code Server.
- Voisin de [[how-claude-code-is-built-pragmatic-engineer-2025-09-15]].

## RésuméDe400mots

The Pragmatic Engineer consacre un deepdive à Inspect, l'agent de codage interne de la fintech Ramp, à partir d'entretiens avec le CTO Rahul Sengottuvelu, le head of engineering Hamid Dadkhah et l'ingénieur fondateur Zach Bruggeman. Les auteurs rappellent que quelques entreprises écrivent l'essentiel de leur code avec leur propre agent : Goose chez Block, Minions chez Stripe, River chez Shopify. Ils posent la question : pourquoi construire quand Codex, Claude Code, Cursor ou Copilot existent ?

Inspect est un agent *background* ouvert en interne en novembre 2025. Les ingénieurs restent libres de leurs outils, mais 75 % des PR fusionnées proviennent désormais de sessions Inspect, contre environ 60 % en janvier. L'outil se distingue sur deux points. Il tourne dans des sandboxes distants, ce qui lève la limite de sessions parallèles, centralise la configuration et permet la collaboration. Il dispose des mêmes intégrations qu'un ingénieur de Ramp, si bien que seule l'intelligence du modèle borne l'agent. Il vérifie ses changements : tests, télémétrie et feature flags côté backend, captures d'écran et previews côté frontend, une capacité construite avant que les outils tiers ne la proposent.

Trois raisons ont motivé la construction : les machines locales ne permettaient qu'une ou deux sessions Claude Code, l'équipe web voulait un outillage frontend pour designers, et la complexité croissante appelait des environnements de développement distants. La v1, une extension Chrome où l'on désignait une zone de page à modifier, n'a pas été adoptée : les ingénieurs savaient éditer un fichier, et l'installation locale rebutait les non-développeurs. La v2 a pivoté vers un environnement distant avec un agent par-dessus, en s'appuyant sur OpenCode, harness open source exposant une API HTTP et agnostique au modèle. L'adoption a alors fortement progressé.

Les chiffres actuels : moins de 5 secondes pour démarrer un environnement provisionné, une équipe de 5,5 personnes, plus de 150 contributeurs internes, un million de sessions franchi en juillet, et plus de 80 % d'Inspect écrit dans des sessions Inspect.

Les usages couvrent le codage de tâches petites et moyennes, la correction de bugs depuis un fil Slack, et le débogage avec requêtes sur une réplique de production assainie et sur Snowflake. Plus de 200 agents internes reposent sur la plateforme : ReviewBuddy pour la revue de code, Oncall Assistant pour les incidents, Testo pour générer des tests Playwright, Ramp Research comme analyste de données, Voice of the Customer et des PR brouillons créées depuis les alertes Sentry ou Datadog.

Le principe d'architecture : donner aux agents le même contexte et les mêmes outils qu'aux ingénieurs. La suite, payante, détaille la stack (Cloudflare Durable Objects, Agents SDK, Modal) et le sandbox.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Gergely Orosz | PERSONNE | publie | article Why Ramp built its own in-house coding agent, Inspect | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Jessica Salmon | PERSONNE | publie | article Why Ramp built its own in-house coding agent, Inspect | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Ivan Klaric | PERSONNE | publie | article Why Ramp built its own in-house coding agent, Inspect | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Ramp | ORGANISATION | a_créé | Inspect | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Zach Bruggeman | PERSONNE | a_créé | Inspect | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Rahul Sengottuvelu | PERSONNE | travaille_chez | Ramp | ORGANISATION | 0.96 | DYNAMIQUE | déclaré_article |
| Inspect | TECHNOLOGIE | est_instance_de | agent de codage en arrière-plan | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Inspect | TECHNOLOGIE | utilise | OpenCode | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Inspect | TECHNOLOGIE | utilise | Modal | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Inspect | TECHNOLOGIE | utilise | Cloudflare Durable Objects | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Inspect | TECHNOLOGIE | utilise | Cloudflare Agents SDK | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Inspect | TECHNOLOGIE | mesure | 75 % des PR fusionnées chez Ramp en mai 2026 (~60 % en janvier) | MESURE | 0.96 | STATIQUE | déclaré_article |
| Inspect | TECHNOLOGIE | mesure | environnement de dev provisionné en moins de 5 secondes ; 1 million de sessions en juillet 2026 | MESURE | 0.94 | STATIQUE | déclaré_article |
| Inspect | TECHNOLOGIE | permet | vérification par captures d'écran | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| sandbox distant | CONCEPT | permet | sessions d'agents parallèles illimitées | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Inspect | TECHNOLOGIE | concurrence | Claude Code | TECHNOLOGIE | 0.80 | DYNAMIQUE | inféré |
| ReviewBuddy | TECHNOLOGIE | est_basé_sur | Inspect | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| Ramp Research | TECHNOLOGIE | est_basé_sur | Inspect | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Oncall Assistant | TECHNOLOGIE | est_basé_sur | Inspect | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Ramp | ORGANISATION | affirme_que | les agents doivent avoir accès au même contexte et aux mêmes outils que les ingénieurs | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Gergely Orosz | PERSONNE | affirme_que | la convention « buy, don't build » pourrait ne pas s'appliquer aux outils d'IA | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| article Why Ramp built its own in-house coding agent, Inspect | DOCUMENT | référence | Minions | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| article Why Ramp built its own in-house coding agent, Inspect | DOCUMENT | référence | Goose | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Gergely Orosz | PERSONNE | rôle | Auteur de The Pragmatic Engineer | AJOUT |
| Jessica Salmon | PERSONNE | rôle | Co-autrice du deepdive, The Pragmatic Engineer | AJOUT |
| Ivan Klaric | PERSONNE | rôle | Co-auteur du deepdive, The Pragmatic Engineer | AJOUT |
| Ramp | ORGANISATION | secteur | Fintech (cartes et gestion des dépenses) | AJOUT |
| Rahul Sengottuvelu | PERSONNE | rôle | CTO de Ramp | AJOUT |
| Zach Bruggeman | PERSONNE | rôle | Principal engineer, ingénieur fondateur d'Inspect (Ramp) | AJOUT |
| Inspect | TECHNOLOGIE | catégorie | Agent de codage background interne de Ramp sur sandboxes distants, v2 lancée en novembre 2025 | AJOUT |
| OpenCode | TECHNOLOGIE | catégorie | Harness d'agent de codage open source, API HTTP, agnostique au modèle | AJOUT |
| ReviewBuddy | TECHNOLOGIE | catégorie | Système de revue de code interne de Ramp, personnalisable par équipe | AJOUT |
| Ramp Research | TECHNOLOGIE | catégorie | Agent analyste de données de Ramp (Looker, Snowflake, dbt), interrogeable depuis Slack | AJOUT |
| Oncall Assistant | TECHNOLOGIE | catégorie | Agent d'astreinte de Ramp relié aux systèmes de production et d'observabilité | AJOUT |
| sandbox distant | CONCEPT | définition | Environnement de développement cloud provisionné par session d'agent, configuré centralement | AJOUT |
| article Why Ramp built its own in-house coding agent, Inspect | DOCUMENT | catégorie | Deepdive payant de The Pragmatic Engineer, 25 août 2026 | AJOUT |
