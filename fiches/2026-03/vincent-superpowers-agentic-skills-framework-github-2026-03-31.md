# vincent-superpowers-agentic-skills-framework-github-2026-03-31
## Veille
Framework agentique de skills composables pour agents de codage, methodologie developpement logiciel disciplinee, multi-plateforme - GitHub

## Titre Article
Superpowers: An agentic skills framework & software development methodology that works

## Date
2026-03-31

## URL
https://github.com/obra/superpowers

## Keywords
framework agentique, skills composables, agents de codage, methodologie developpement, TDD, sous-agents, brainstorming, specification, planification, Claude Code, Copilot CLI, Gemini CLI, OpenCode, Codex, persuasion LLM, principes Cialdini, discipline ingenieurs, marketplace plugins

## Authors
Jesse Vincent

## Ton
Profil : perspective de createur-mainteneur, registre technique-pragmatique, niveau avance. Jesse Vincent adopte un ton direct et confiant, ancre dans une longue experience open source (Request Tracker, Perl 6, Keyboardio, K-9 Mail). Le README est structure comme un guide d'onboarding efficace : description concise du probleme, explication du workflow, instructions d'installation multi-plateforme, et appel a contribution. Le style est celui d'un ingenieur senior qui a observe les echecs recurrents du codage assiste par IA (agents qui foncent dans le code sans specification) et propose une solution structuree. L'autorite est implicite : le projet a atteint 121 000 etoiles GitHub en cinq mois. Public cible : developpeurs utilisant des agents de codage IA, tech leads, architectes logiciels.

## Pense-betes
- Superpowers est le framework de skills le plus populaire de l'ecosysteme Claude Code avec 121 000+ etoiles GitHub en 5 mois
- Principe fondamental : au lieu de rendre l'agent plus intelligent, on lui impose la discipline que les developpeurs humains ont mis des decennies a construire
- Les skills ne sont pas des suggestions mais des obligations : l'agent DOIT les suivre quand elles existent
- Workflow impose : brainstorming → specification par morceaux digestibles → plan d'implementation → TDD rouge/vert → sous-agents pour l'execution
- L'agent ne saute jamais directement dans le code : il demande d'abord ce qu'on essaie vraiment de faire
- Subagent-driven development : des sous-agents executent chaque tache d'ingenierie, l'agent principal inspecte et revise
- Claude peut travailler de facon autonome pendant plusieurs heures d'affilee grace a ce workflow
- Jesse Vincent a decouvert que les principes classiques de persuasion de Cialdini (autorite, engagement, preuve sociale) fonctionnent sur les LLM comme sur les humains
- Multi-plateforme depuis v5.0 : Claude Code (marketplace officielle), Copilot CLI, Gemini CLI, OpenCode, OpenAI Codex
- v5.0.7 (31 mars 2026) : injection contexte SessionStart pour Copilot CLI, checklists reviewers simplifiees, installation OpenCode en une ligne
- Accepte dans la marketplace officielle Anthropic depuis le 15 janvier 2026
- Skills cles : brainstorming (specification socratique), debugging systematique (4 phases), TDD (rouge/vert strict), planification (taches de 2-5 minutes)
- La fiche existante superpowers-skills-coding-agents-vincent-2025-10-09 couvre le billet de blog initial d'octobre 2025 ; cette fiche couvre l'etat actuel du framework (v5.0.7, 121K stars, multi-plateforme)
- Jesse Vincent est aussi le createur de Request Tracker, ex-gestionnaire de Perl 6, co-fondateur de Keyboardio, et createur de K-9 Mail (devenu Thunderbird Android)

## ResumeDe400mots
Superpowers est un framework de skills agentiques et une methodologie de developpement logiciel creee par Jesse Vincent (Prime Radiant). Avec plus de 121 000 etoiles GitHub en cinq mois, c'est devenu le plugin le plus populaire de l'ecosysteme Claude Code. Son principe fondateur est radical : plutot que de rendre l'agent IA plus intelligent, il lui impose la discipline que les ingenieurs humains ont construite en des decennies de pratique.

Le framework repose sur des skills composables qui ne sont pas de simples suggestions mais des obligations. Lorsqu'une skill existe pour un contexte donne, l'agent doit l'utiliser. Ce mecanisme s'appuie sur une decouverte contre-intuitive : les sept principes de persuasion de Cialdini (autorite, engagement, preuve sociale, etc.) fonctionnent sur les LLM exactement comme sur les humains.

Le workflow impose suit une sequence stricte. Des que l'agent detecte une tache de construction, la skill de brainstorming se declenche automatiquement avant qu'une seule ligne de code ne soit ecrite. Elle pose des questions clarificatrices et affine les specifications par dialogue socratique. La specification est ensuite presentee en morceaux suffisamment courts pour etre reellement lus et valides. Apres approbation, la skill de planification decompose le travail en taches de 2 a 5 minutes avec des details d'implementation complets, en insistant sur le TDD rouge/vert, le YAGNI et le DRY.

L'execution utilise le subagent-driven development : des sous-agents traitent chaque tache d'ingenierie tandis que l'agent principal inspecte et revise le travail. Ce processus permet a Claude de travailler de facon autonome pendant plusieurs heures d'affilee. Le debugging systematique suit un processus en 4 phases incluant le tracage de cause racine et la defense en profondeur.

Depuis la version 5.0 (mars 2026), Superpowers est multi-plateforme : Claude Code (marketplace officielle Anthropic depuis janvier 2026), Copilot CLI, Gemini CLI, OpenCode et OpenAI Codex. La v5.0.7 du 31 mars 2026 ajoute l'injection de contexte SessionStart pour Copilot CLI, simplifie les checklists de review (specification de 7 a 5 categories, plan de 7 a 4), et offre une installation en une ligne pour OpenCode.

Jesse Vincent apporte une credibilite technique profonde : createur de Request Tracker dans les annees 1990, gestionnaire de Perl 6 de 2005 a 2008, co-fondateur de Keyboardio, et createur de K-9 Mail pour Android (acquis par Mozilla et devenu Thunderbird Android). Superpowers incarne sa vision d'une ingenierie logicielle ou les agents IA deviennent des partenaires disciplines plutot que des generateurs de code non supervises.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Predicat | Objet | Type Objet | Confiance | Temporalite | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Jesse Vincent | PERSONNE | a_cree | Superpowers | TECHNOLOGIE | 0.99 | STATIQUE | declare_article |
| Superpowers | TECHNOLOGIE | impose | discipline ingenierie logicielle | CONCEPT | 0.95 | ATEMPOREL | declare_article |
| Superpowers | TECHNOLOGIE | utilise | skills composables | CONCEPT | 0.98 | ATEMPOREL | declare_article |
| Superpowers | TECHNOLOGIE | est_base_sur | principes de persuasion Cialdini | CONCEPT | 0.90 | ATEMPOREL | declare_article |
| Superpowers | TECHNOLOGIE | supporte | Claude Code | TECHNOLOGIE | 0.98 | DYNAMIQUE | declare_article |
| Superpowers | TECHNOLOGIE | supporte | Copilot CLI | TECHNOLOGIE | 0.95 | DYNAMIQUE | declare_article |
| Superpowers | TECHNOLOGIE | supporte | Gemini CLI | TECHNOLOGIE | 0.95 | DYNAMIQUE | declare_article |
| Superpowers | TECHNOLOGIE | supporte | OpenAI Codex | TECHNOLOGIE | 0.92 | DYNAMIQUE | declare_article |
| Superpowers | TECHNOLOGIE | applique | TDD rouge/vert | METHODOLOGIE | 0.95 | ATEMPOREL | declare_article |
| Superpowers | TECHNOLOGIE | applique | subagent-driven development | METHODOLOGIE | 0.95 | ATEMPOREL | declare_article |
| Anthropic | ORGANISATION | a_accepte | Superpowers dans marketplace officielle | EVENEMENT | 0.92 | STATIQUE | declare_article |
| Jesse Vincent | PERSONNE | a_cree | Request Tracker | TECHNOLOGIE | 0.97 | STATIQUE | declare_article |
| Jesse Vincent | PERSONNE | a_cofonde | Keyboardio | ORGANISATION | 0.97 | STATIQUE | declare_article |
| Prime Radiant | ORGANISATION | developpe | Superpowers | TECHNOLOGIE | 0.90 | DYNAMIQUE | declare_article |
| Superpowers | TECHNOLOGIE | a_atteint | 121 000 etoiles GitHub | EVENEMENT | 0.88 | DYNAMIQUE | infere |

### Entites

| Entite | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Superpowers | TECHNOLOGIE | categorie | Framework agentique de skills composables | AJOUT |
| Superpowers | TECHNOLOGIE | version | v5.0.7 (31 mars 2026) | AJOUT |
| Superpowers | TECHNOLOGIE | etoiles_github | 121 000+ | AJOUT |
| Jesse Vincent | PERSONNE | role | Createur de Superpowers, fondateur Prime Radiant | MISE_A_JOUR |
| Prime Radiant | ORGANISATION | secteur | Outils developpement IA | AJOUT |
| Subagent-driven development | METHODOLOGIE | description | Sous-agents executent les taches, agent principal revise | AJOUT |
| Principes de persuasion Cialdini | CONCEPT | description | Autorite, engagement, preuve sociale appliques aux LLM | AJOUT |
| Copilot CLI | TECHNOLOGIE | categorie | Agent de codage Microsoft | AJOUT |
| Gemini CLI | TECHNOLOGIE | categorie | Agent de codage Google | AJOUT |
| OpenCode | TECHNOLOGIE | categorie | Agent de codage open source | AJOUT |
