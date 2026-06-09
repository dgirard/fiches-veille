# dembo-byo-agent-m5stack-tinkering-opus-cloudflare-2026-06-07

## Veille
Billet de bricolage du dimanche de **Mark Dembo** (Head of Solutions, Developer Platform & AI chez **Cloudflare**) publié le **7 juin 2026** sur son blog perso. **Récit** : inspiré par **Steve Ruiz**, l'auteur achète un petit appareil **M5Stack Stick 3** (~30 €) et, profitant de la sortie d'**Opus 4.8**, se construit un **agent IA DIY** « par pure curiosité, sans objectif ». **Itération 1 (45 min)** : il jette la doc de l'appareil à **Claude Code**, qui génère des scripts Python (~200 LOC, *« zero blast radius »*) affichant la météo de Munich, puis de plusieurs villes ; un **backend Cloudflare Workers + Workers AI** ajoute la **synthèse vocale (TTS)**, le **push-to-talk** (speech-to-text) et un **petit LLM** central pour répondre aux questions. **Itération 2 (vrai agent)** : passage des endpoints REST au transport **WebSocket** via le **Cloudflare Agents SDK** + **Dynamic Worker execution** → le pattern ***« Code Mode »*** (l'agent écrit et exécute du code pour accomplir sa tâche). L'agent répond alors à des questions à données publiques (11 ! = factorielle, vainqueur de la Ligue des Champions via `fetch()` sur Wikipédia, météo de n'importe quelle ville). **Itération 3 (vrais pouvoirs)** : connexion à **Todoist** via flux **MCP OAuth** → 50 outils d'un coup, d'où deux problèmes : **bloat du contexte** et **risque de dégâts réels**. Solution reprise du **MCP Server Portal Cloudflare** + des réglages connecteurs Claude : par outil, **Always allow / Ask for approval / Disable** (les *Disabled* n'entrent jamais dans le contexte ; un **classifieur LLM** n'accepte que les « allow » distincts et **défaut = deny**). **Posture revendiquée** : réduire son rôle à ***« idea generator, executor and judge »*** (et rarement guide technique), un flux « human-in-the-loop » jugé peu *« 2026 »* (copier-coller dans l'UIFlow). **Ce qu'il n'a PAS fait** : pas d'optimisation de latence/streaming, pas d'appels LLM optimistes, pas d'évals, ***« I did not even look at the code once »***. **Émerveillement** : 30 € + une fenêtre de session Anthropic + quelques cents d'inférence Cloudflare → un objet qui écoute et parle, piloté en langage naturel ; *« the true unlock is how accessible it is »*. Contraste vif avec [[thomas-pragdave-failing-faster-code-rot-ai-velocity-2026-06-06]] (ici le *« zero blast radius »* justifie de ne jamais regarder le code) ; illustre concrètement *Code Mode* / *« the agent just writing and executing code »*, le pattern **MCP** ([[claude-skills-bigger-than-mcp-willison-2025-10-16]]), la gouvernance d'outils façon *Ask for approval* ([[uber-engineering-agent-identity-crisis-zero-trust-spire-2026-05-21]]), et la doctrine *systems around the model* de [[dropbox-okumura-beyond-code-generation-engineering-productivity-ai-agents-2026-05-28]].

## Titre Article
BYO Agent with M5Stack Stick 3

## Date
2026-06-07

## URL
https://markpauldembo.com/blog/tinkering-byo-ai

## Keywords
BYO agent, bring your own AI, bricolage, tinkering, M5Stack Stick 3, appareil 30 euros, hardware DIY, Steve Ruiz, Opus 4.8, Claude Code, UIFlow, zero blast radius, idea generator executor judge, human-in-the-loop, Cloudflare Workers, Workers AI, text-to-speech, speech-to-text, push-to-talk, petit LLM, Cloudflare Agents SDK, WebSocket, Dynamic Worker execution, Code Mode, agent écrit et exécute du code, fetch, Wikipedia, factorielle, MCP, MCP OAuth, Todoist, 50 outils, bloat du contexte, MCP Server Portal, connecteurs Claude, Always allow Ask for approval Disable, classifieur LLM, défaut deny, accessibilité, I did not even look at the code once, curiosité, exploration, Mark Dembo

## Authors
**Mark Dembo** (@darkmembo / @mdembo), **Head of Solutions – Developer Platform & AI** chez **Cloudflare** (auparavant auteur sur le blog Cloudflare). Billet personnel publié sur son blog *markpauldembo.com* le **7 juin 2026** (description : *« Thoughts about tinkering on a Sunday »*).

## Ton
**Profil** : Récit de bricolage à la première personne, registre **geek-enthousiaste et décontracté**, niveau technique élevé sur la stack (Workers, Agents SDK, MCP, Code Mode) mais ton léger et auto-ironique. Public : développeurs et *builders* curieux. Posture : **praticien Cloudflare** qui « mange sa propre nourriture » sur un projet sans enjeu.

**Style** : Narratif, étape par étape (3 itérations + une section *« What I did not do »*), parsemé d'humour (*« the pomodoro timers of the modern age »* pour les *session limit windows*, *« Value add! Value add! »* en autodérision sur le copier-coller manuel). Émerveillement assumé (*« wow, I cannot believe how far we have come »*). Vidéos de démo intégrées.

**Aphorismes-clés** :
- ***« The goal? There is no goal. Pure exploration and curiosity. And that feels just great. »***
- ***« This reduced my jobs to the following three: idea generator, executor and judge. »***
- ***« Given that these are ~200 LOC Python scripts with zero blast radius, I can afford to not care about the code at all. »***
- ***« I did not even look at the code once. And you know what? That's the nice part of it. »***
- ***« That we have this capability is great … how accessible it is is the true unlock. »***

**Métaphores / cadres travaillés** :
- ***BYO Agent*** — se construire son propre agent matériel/logiciel à partir d'un appareil à 30 €.
- ***Code Mode*** — l'agent écrit et exécute du code pour accomplir sa tâche (vs appel d'outils figés), pattern favori de l'auteur.
- ***Idea generator / executor / judge*** — la réduction du rôle humain face à un agent qui code seul.
- ***Always allow / Ask for approval / Disable*** — gouvernance par outil pour maîtriser bloat de contexte et blast radius (50 outils Todoist).
- ***Session limit windows = pomodoros modernes*** — l'humour sur le rythme imposé par les fenêtres de session.

**Position épistémique** : témoignage exploratoire **sans prétention méthodologique** (assume explicitement n'avoir fait ni évals, ni optimisation, ni revue de code) — la valeur est dans la **démonstration d'accessibilité** et le **plaisir d'apprendre**, pas dans la rigueur d'ingénierie.

**Autorité** : (a) **expertise Cloudflare** (Head of Solutions Dev & AI) sur la stack mobilisée ; (b) **REX concret et reproductible** (hardware + SDK + MCP réels) ; (c) **honnêteté sur les raccourcis** assumés (zero blast radius). À lire comme **vitrine du possible** plus que comme guide de production.

## Pense-betes

- **Date / source** : **7 juin 2026**, blog perso **markpauldembo.com**. Auteur : **Mark Dembo**, Head of Solutions Developer Platform & AI **Cloudflare**. Inspiration : **Steve Ruiz**.
- **Cadre** : bricolage du dimanche, **~30 €** (M5Stack Stick 3) + **Opus 4.8** fraîchement sorti. *« No goal. Pure exploration and curiosity. »*

### Itération 1 — du zéro à un objet qui parle (45 min)

- Doc de l'appareil → **Claude Code** → scripts **Python ~200 LOC**, *« zero blast radius »* → *« I can afford to not care about the code at all »*.
- Flux **human-in-the-loop** (jugé peu 2026) : Opus génère → copier-coller dans **UIFlow** → run → reporter le résultat à Claude.
- Rôle réduit à **idea generator / executor / judge** (+ rarement guide technique).
- Backend **Cloudflare Workers + Workers AI** : **TTS**, **push-to-talk** (STT), **petit LLM** central pour répondre.

### Itération 2 — un vrai mini-agent

- **Cloudflare Agents SDK** : REST → **WebSocket** + **Dynamic Worker execution** = pattern ***« Code Mode »*** (l'agent écrit/exécute du code).
- Données publiques OK : **11 !** (one-liner), vainqueur **Champions League** (via `fetch()` sur Wikipedia — accès internet donné à l'agent), météo de n'importe quelle ville.
- Limite : **pas d'accès aux données privées** → mission suivante.

### Itération 3 — de vrais pouvoirs (et leur garde-fou)

- Connexion **Todoist** via **MCP OAuth** (ajouté en minutes par Claude) → **50 outils** d'un coup.
- Deux problèmes : (1) **bloat du contexte** (la plupart des outils inutiles) ; (2) **blast radius réel** (un mauvais appel = suppression d'une tâche importante).
- Solution (MCP Server Portal Cloudflare + connecteurs Claude) : par outil **Always allow / Ask for approval / Disable** ; *Disabled* hors contexte ; **classifieur LLM** n'accepte que les « allow » distincts, **défaut = deny**.

### Ce qu'il n'a PAS fait (assumé)

- Pas d'optimisation latence/streaming audio+LLM (*« yes, I know, it's slow »*).
- Pas d'appels LLM optimistes, **pas d'évals** modèles/prompts.
- ***« I did not even look at the code once »*** — et c'est revendiqué comme le plaisir du truc.

### À mobiliser en mission / présentation

- **Proof-point d'accessibilité** : 30 € + 1 fenêtre de session + quelques cents d'inférence → objet conversationnel. *« The true unlock is how accessible it is. »*
- Démonstration concrète de **Code Mode** + **MCP** + **gouvernance d'outils** (allow/ask/disable, default-deny) — réutilisable pour cadrer la sécurité agentique.
- **Contraste pédagogique** avec *Failing Faster* (Pragdave) : ici le *« zero blast radius »* justifie de ne jamais regarder le code — la discipline dépend du **blast radius**, pas du dogme.

## RésuméDe400mots

Dans ce billet du **7 juin 2026**, **Mark Dembo** (Head of Solutions – Developer Platform & AI chez **Cloudflare**) raconte un bricolage de dimanche : se construire un **agent IA DIY** à partir d'un petit appareil **M5Stack Stick 3** acheté ~30 €, inspiré par **Steve Ruiz** et motivé par la sortie d'**Opus 4.8**. Le mot d'ordre : *« There is no goal. Pure exploration and curiosity. And that feels just great. »*

**Première itération (45 minutes).** Il jette la documentation de l'appareil à **Claude Code**, qui produit des scripts Python d'environ **200 lignes**. Comme ils ont un *« zero blast radius »*, il s'autorise à **ne pas se soucier du code**. Le flux reste *human-in-the-loop* (peu *« 2026 »* à son goût) : Opus génère, il copie-colle dans l'interface web **UIFlow**, lance, et rapporte le résultat. Son rôle se réduit à trois fonctions — ***idea generator, executor et judge***. Un backend **Cloudflare Workers + Workers AI** ajoute vite la **synthèse vocale**, le **push-to-talk** (reconnaissance vocale) et un **petit LLM** central : l'objet écoute, répond et fait de mauvaises blagues.

**Deuxième itération.** Visant un vrai agent, il pointe Opus vers le **Cloudflare Agents SDK**, bascule de REST vers le transport **WebSocket** et active la **Dynamic Worker execution** — débloquant le pattern qu'il préfère, ***« Code Mode »*** : l'agent **écrit et exécute du code** pour accomplir sa tâche. Doté d'un accès internet, l'agent calcule **11 !** par un one-liner, trouve le vainqueur de la Ligue des Champions via `fetch()` sur Wikipédia et donne la météo de n'importe quelle ville. Sa limite : aucune **donnée privée**.

**Troisième itération.** Il connecte **Todoist** via un flux **MCP OAuth** (ajouté en quelques minutes par Claude) — et hérite d'un coup de **50 outils**, donc de deux problèmes : le **gonflement du contexte** et un **blast radius réel** (un mauvais appel pourrait détruire une tâche critique). Sa parade, inspirée du **MCP Server Portal** de Cloudflare et des connecteurs Claude : régler chaque outil sur **Always allow / Ask for approval / Disable** — les outils désactivés n'entrent jamais dans le contexte, un **classifieur LLM** n'accepte que des autorisations explicites et **défaut = deny**.

**Ce qu'il n'a pas fait** : ni optimisation de latence, ni évals, ni appels optimistes — *« I did not even look at the code once. And you know what? That's the nice part of it. »* L'émerveillement final porte moins sur la capacité que sur son **accessibilité** : 30 € et quelques cents d'inférence pour un objet qu'on pilote en langage naturel.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Mark Dembo | PERSONNE | publie | BYO Agent with M5Stack Stick 3 | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Mark Dembo | PERSONNE | travaille_chez | Cloudflare | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Mark Dembo | PERSONNE | a_créé | agent IA DIY sur M5Stack Stick 3 | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Mark Dembo | PERSONNE | s_inspire_de | Steve Ruiz | PERSONNE | 0.9 | STATIQUE | déclaré_article |
| Mark Dembo | PERSONNE | utilise | Claude Code | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Cloudflare Agents SDK | TECHNOLOGIE | permet | le pattern Code Mode (l'agent écrit et exécute du code) | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| agent IA DIY sur M5Stack Stick 3 | TECHNOLOGIE | utilise | données publiques via fetch() (Wikipedia) | CONCEPT | 0.9 | STATIQUE | déclaré_article |
| MCP OAuth | TECHNOLOGIE | permet | la connexion de l'agent à Todoist (50 outils) | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| 50 outils Todoist | TECHNOLOGIE | permet | bloat de contexte et risque de blast radius | CONCEPT | 0.9 | STATIQUE | déclaré_article |
| Mark Dembo | PERSONNE | recommande | gouvernance par outil Always allow / Ask for approval / Disable (défaut deny) | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| Mark Dembo | PERSONNE | affirme_que | « I did not even look at the code once » | CITATION | 0.95 | STATIQUE | déclaré_article |
| zero blast radius | CONCEPT | permet | de ne pas se soucier du code | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Mark Dembo | PERSONNE | affirme_que | l'accessibilité de la capacité IA (30 € + quelques cents d'inférence) est le vrai déblocage | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Mark Dembo | PERSONNE | rôle | Head of Solutions – Developer Platform & AI chez Cloudflare | AJOUT |
| BYO Agent with M5Stack Stick 3 | DOCUMENT | catégorie | Billet de bricolage / REX exploratoire | AJOUT |
| M5Stack Stick 3 | TECHNOLOGIE | catégorie | Petit appareil hardware (~30 €) support de l'agent DIY | AJOUT |
| Opus 4.8 | TECHNOLOGIE | rôle | Modèle utilisé via Claude Code (sorti peu avant) | AJOUT |
| Cloudflare Workers / Workers AI | TECHNOLOGIE | usage | Backend : TTS, STT (push-to-talk), petit LLM, inférence | AJOUT |
| Cloudflare Agents SDK | TECHNOLOGIE | usage | WebSocket + Dynamic Worker execution → Code Mode | AJOUT |
| Code Mode | CONCEPT | définition | L'agent écrit et exécute du code pour accomplir sa tâche | AJOUT |
| MCP (OAuth) | TECHNOLOGIE | usage | Connexion de l'agent à Todoist (50 outils) | AJOUT |
| gouvernance d'outils MCP | METHODOLOGIE | définition | Always allow / Ask for approval / Disable, classifieur LLM, défaut deny | AJOUT |
| zero blast radius | CONCEPT | définition | Faible surface de risque justifiant l'absence de revue de code | AJOUT |
| idea generator / executor / judge | CONCEPT | définition | Réduction du rôle humain face à un agent qui code seul | AJOUT |
