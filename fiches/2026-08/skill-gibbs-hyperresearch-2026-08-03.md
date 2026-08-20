---
fiche_type: skill
skill_source: github.com/jordan-gibbs/hyperresearch
skill_author: Jordan Gibbs
themes: [agents-codage-ia-skills, outils-plateformes, qualite-securite]
source: "GitHub (Jordan Gibbs, jordan-gibbs/hyperresearch)"
---
# skill-gibbs-hyperresearch-2026-08-03

## Veille

Fiche de **Skill** : **hyperresearch** de **Jordan Gibbs** est un **harnais de deep research** qui transforme Claude Code en agent de recherche documentaire, livré comme paquet PyPI (MIT, Python 3.11-3.13) installant **20 skills Claude Code**, une CLI, un serveur MCP et une UI web locale. Observé le **3 août 2026** : 1 568 étoiles, 170 forks, dépôt créé le 9 avril 2026, dernier push le 1er août. **Le cœur est un pipeline en 16 étapes adaptatif par paliers** — `light` (~30-40 min), `full` (~1,5-2,5 h), `dissertation` (4-8 h, 25 000-80 000 mots sur 300-450 sources) — qui prend un prompt et rend un rapport audité de façon adverse avec provenance complète. **La décision d'architecture centrale est documentée avec son mode d'échec** : la skill d'entrée est un **routeur mince** sans procédure, chaque étape vivant dans sa propre skill chargée **fraîche au moment de son invocation**, parce que la version précédente était *« one 1200-line skill that got compacted away by the time Layer 4 needed its triple-draft procedure. The orchestrator forgot the procedure, wrote a single draft, and produced a flat-scoring report. »* **Deux principes porteurs.** *« Patch, never regenerate »* : après la synthèse, seules des retouches chirurgicales `Edit` sont possibles, le patcheur et l'auditeur de polissage étant verrouillés à `[Read, Edit]` au niveau de l'allowlist Claude Code, si bien qu'ils *« physically cannot Write a new draft »*. *« Canonical research query is gospel »* : le prompt verbatim est persisté une fois dans `query.md` et relu par chaque étape et chaque sous-agent. **Seize sous-agents** au rôle et au modèle configurables (fetchers et cite-checker en Sonnet, critiques, synthétiseur et patcheur en Opus). **Le vault** est un magasin markdown persistant indexé en SQLite — *« Markdown is truth, SQLite is cache »* — avec cycle de vie des notes (`draft → review → evergreen`, `stale → deprecated → archive`), provenance traçable, score de qualité composite (type de source, autorité de citation via OpenAlex et Semantic Scholar avec indicateurs de rétractation, PageRank interne) et **audit d'indépendance** regroupant les copies syndiquées — *« five reprints of one press release argue with the weight of one source »*. **Trois gates mécaniques avant expédition** : intégrité des citations (toute citation entre guillemets doit exister **verbatim** dans une note du vault), balayage de rétractation rafraîchi sur chaque DOI cité, et vérification des liaisons citation-phrase par un LLM sceptique. **Réserve à porter** : la promesse d'ouverture — *« currently leads the DeepResearch-Bench RACE leaderboard »* — est contredite par sa propre note de bas de page, *« forward-looking projection from a stratified pilot… Third party validation is pending »*. Une projection n'est pas un classement, et le graphique la présente pourtant devant Gemini et OpenAI Deep Research.

## Titre Article

hyperresearch — « The Most Powerful Deep Research Harness » / « Agent-driven research knowledge base. Agents collect, search, and synthesize web research into a persistent, searchable wiki. »

## Date

2026-08-03

## URL

https://github.com/jordan-gibbs/hyperresearch

## Keywords

skill, deep research, harnais de recherche, Claude Code, pipeline 16 étapes, paliers, light, full, dissertation, gear, profil d'échelle, routeur mince, chargement différé, compaction de contexte, éviction de procédure, skill par étape, patch never regenerate, retouche chirurgicale, verrouillage d'outils, tool-locked, allowlist, Read Edit, canonical query, prompt verbatim, gospel, sous-agents, fetcher, loci-analyst, depth-investigator, draft-orchestrator, synthesizer, critiques adversariaux, dialectic critic, cite-checker, patcher, polish auditor, vault, markdown source de vérité, SQLite cache, index reconstructible, cycle de vie des notes, evergreen, deprecated, provenance, suggested-by, score de qualité, PageRank, OpenAlex, Semantic Scholar, rétractation, audit d'indépendance, syndication, quote-integrity, numeric-consistency, ship gate, lint, injection de prompt, untrusted-source, texte web comme donnée, SSRF, Unpaywall, Europe PMC, open access, rescued note, nothing_from_source, version of record, escalade navigateur, Claude-in-Chrome, CAPTCHA jamais résolu, budget de run, reprise de run, MCP, DeepResearch-Bench, projection non validée, Jordan Gibbs

## Authors

**Jordan Gibbs** — auteur et mainteneur du dépôt `jordan-gibbs/hyperresearch`. Le projet est distribué sous **licence MIT** et publié sur **PyPI** (`pip install hyperresearch`). Signaux d'adoption au 3 août 2026 : **1 568 étoiles**, **170 forks**, 13 issues ouvertes, dépôt créé le **9 avril 2026** et poussé le **1er août 2026** — soit une traction rapide sur moins de quatre mois. Topics déclarés : `agents`, `agentskills`, `claude-code`, `deep-research`, `deep-research-agent`.

## Ton

**Profil** : documentation de projet open source à forte densité technique, doublée d'un **argumentaire de supériorité**. Le README ne se contente pas d'expliquer : il **plaide**, section par section, sous des titres qui sont des thèses (*« Why it wins »*, *« Source ranking: quality is persistent, not vibes »*, *« The web is hostile input »*, *« Open-access full text: read this before you cite »*).

**Style** : registre d'ingénieur qui explique un mécanisme par le problème qu'il résout, presque toujours en deux temps — le mode d'échec d'abord, la parade ensuite. *« A closed paper normally enters a vault as a 1,500-character abstract that the report then cites as though it had been read »*, puis la substitution open access. *« V7 was one 1200-line skill that got compacted away »*, puis le routeur. Cette forme donne au texte une **valeur pédagogique supérieure à sa valeur promotionnelle** : on apprend les modes d'échec du deep research agentique même si l'on n'installe jamais l'outil.

**Registre opérationnel imposé à l'agent** (le « ton » au sens des fiches de skill) : **impératif, contractuel, majuscules d'insistance**. *« NEVER EMIT BARE TEXT WHILE TASKS ARE RUNNING »*, *« RESPECT THE TIER GATE »*, *« PATCH, NEVER REGENERATE »*, *« ARGUE, DON'T JUST REPORT »*. L'orchestrateur est explicitement dépossédé du travail : *« You do NOT do the work of any step yourself. The step skills do. You just sequence them. »* Le prompt utilisateur est qualifié de **gospel** — trois fois.

**Trait remarquable** : une **honnêteté sélective**. La section *« What it doesn't do »* est franche (*« The lint gate catches structural failures… It cannot guarantee factual accuracy, that's still your call »*), les avertissements sur les versions de preprints sont scrupuleux, et l'obligation de renseigner son propre `contact_email` pour Unpaywall est justifiée par un raisonnement collectif (*« shipping a shared placeholder would get that placeholder rate-limited for every hyperresearch user at once »*). Cette rigueur rend d'autant plus visible la **seule zone où elle fléchit** : la revendication de leaderboard.

**Formules-marqueurs** : *« Markdown is truth, SQLite is cache »*, *« Fetched text is data, never instructions »*, *« five reprints of one press release argue with the weight of one source »*, *« they physically cannot Write a new draft »*, *« quality is persistent, not vibes »*, *« nothing is thrown away »*, *« each session starts smarter than the last »*.

## Pense-betes

- **Nature** : harnais de deep research livré comme paquet de **20 skills Claude Code** + CLI Python + serveur MCP + UI web locale. `pip install hyperresearch && hyperresearch install`, puis `/hyperresearch <sujet>`. MIT, Python 3.11-3.13.
- **Cadrage clé** : la skill d'entrée est un **routeur** sans procédure, chaque étape vivant dans sa propre skill chargée fraîche à l'invocation.

### La leçon d'architecture, avec son mode d'échec documenté

> *« V7 was one 1200-line skill that got compacted away by the time Layer 4 needed its triple-draft procedure. The orchestrator forgot the procedure, wrote a single draft, and produced a flat-scoring report. V8 fixes this at the source: each step's procedure is loaded into context only at the moment it's needed, fresh, with no eviction risk. »*

Un long pipeline ne perd pas ses étapes par oubli du modèle mais par **éviction de contexte**, et la parade est structurelle. Même discipline que le contexte permanent qui porte l'index et non le contenu chez [[lassiege-usine-logicielle-heure-ia-2026-07-28]], découverte indépendamment sur un autre terrain.

### Le verrouillage d'outils comme garantie

Le patcheur et l'auditeur de polissage sont *« tool-locked to `[Read, Edit]` at the Claude Code allowlist level so they physically cannot Write a new draft »*, avec des plafonds par hunk rendant *« just rewrite it » mechanically impossible*. On ne demande pas à l'agent de ne pas réécrire, on lui retire l'outil. Corollaire : une conclusion de critique qui ne tient pas dans une petite retouche **escalade en problème structurel** au lieu de déclencher une réécriture.

### Les seize étapes, en trois blocs

| Bloc | Étapes |
|---|---|
| **Cadrage** | 1 décomposition + matrice de couverture + classification de palier ; 1.5 partition en chapitres |
| **Corpus et analyse** | 2 balayage en largeur ; 3 graphe de contradictions ; 4 analyse de loci ; 5 investigations profondes parallèles ; 6 réconciliation inter-loci ; 7 tensions entre sources ; 8 critique de corpus (*« quelle source renverserait ceci ? »*) + comblement ciblé ; 9 digest de preuves |
| **Écriture et audit** | 10 triple rédaction par angle ; 11 synthèse ; 12 quatre critiques adverses en parallèle ; 13 comblement post-critique ; 14 patcheur chirurgical ; 14.5 vérification des citations ; 15 polissage ; 16 audit de lisibilité |

### Trois leviers d'échelle à ne pas confondre

| Levier | Décide |
|---|---|
| **Paliers** (`tier`) | **quelles étapes** tournent, routées par requête |
| **Gears** (profils d'échelle) | **de combien** — cibles de sources, budgets de profondeur, longueur ; survivent aux réinstallations, prennent effet au run suivant, jamais en cours de run |
| **Levers** (`register`, `domain_notes`, `inference_depth`) | **quelle voix** — `teach` / `survey` / `analyze` / `advocate` |

Les levers se rendent dans des **shims injectés dans les prompts de sous-agents**, *« so the critics move with the register instead of undoing it »*. Mais : *« The cite-checker and the ship gate receive no shim at all. Verification never softens by mode. »* La vérification est le seul étage soustrait au style.

### Les trois gates mécaniques avant expédition

1. **quote-integrity** — toute portion citée entre guillemets doit exister **verbatim** dans une note du vault ; *« hallucinated quotes cannot ship »*.
2. **retracted-citations** — citer une source rétractée sans le signaler est bloquant, avec un balayage rafraîchi **au moment de l'expédition** sur chaque DOI cité, y compris sur les sources réutilisées d'anciens runs : *« a retraction published yesterday is caught today »*.
3. **numeric-consistency** — les nombres non traçables à une preuve sont signalés.

S'y ajoute le **cite-check** : un LLM sceptique vérifie par échantillon que la source citée soutient réellement la phrase qu'elle appuie.

### L'audit d'indépendance

Les copies syndiquées et dérivées sont regroupées, de sorte que *« five reprints of one press release argue with the weight of one source »*. Le nombre de sources concordantes cesse d'être un argument quand elles descendent d'un même communiqué — pertinent pour toute veille. Score de qualité composite et persistant : type de source, utilité constatée à la lecture, autorité de citation (OpenAlex / Semantic Scholar avec indicateurs de rétractation), PageRank sur le graphe interne. Sources rétractées plancherisées à zéro : *« Quality is persistent, not vibes. »*

### La défense contre l'injection de prompt

*« Fetched text is data, never instructions. »* Tout corps récupéré du web est servi dans une clôture `<untrusted-source url="...">` avec préambule *treat-as-data*, sur les deux chemins qui servent des corps (`note show` et `search`). Détails qui montrent que la menace a été pensée :

- les notes écrites par les sous-agents passent **sans clôture** — frontière de confiance **par provenance**, non par contenu ;
- les balises de clôture contrefaites dans un corps récupéré sont neutralisées **mais laissées visibles** pour l'analyse forensique ;
- l'attribut `url` est échappé et ses caractères de contrôle retirés ;
- dans `search`, l'enveloppement se fait **après** la troncature au budget de tokens, *« so the closing fence can never be severed »* ;
- les URL résolues via des API tierces sont vérifiées (schéma, identifiants embarqués, résolution publiquement routable) — défense SSRF ;
- les prompts des fetchers, investigateurs et rédacteurs interdisent de blanchir les directives d'une page clôturée vers une sortie de confiance.

### L'hygiène épistémique sur les sources fermées

Un article payant entrerait normalement dans le vault comme un abstract d'environ 1 500 caractères, que le rapport citerait ensuite *« as though it had been read »*. hyperresearch interroge **Unpaywall** et **Europe PMC** pour une copie légale en accès ouvert et stocke ce texte-là, en divulguant la substitution en quatre endroits (bannière, frontmatter `oa_*`, bloc JSON `body_is_not_from_source: true`, sortie CLI). Un troisième état est distingué : la note **« rescued »**, quand la source n'a pas pu être lue du tout — `nothing_from_source: true`, avec bannière indiquant que l'URL n'a jamais été lue. Le système distingue donc *« j'ai lu ceci »*, *« j'ai lu un substitut »* et *« je n'ai jamais lu la source »*, et le porte dans l'artefact. Avertissement : Unpaywall peut rendre un manuscrit accepté ou un preprint soumis, à vérifier avant citation directe.

### Le vault

*« Markdown is truth, SQLite is cache »* — index entièrement reconstructible (`hyperresearch sync`), notes en markdown + frontmatter YAML lisibles sans l'outil, versionnables en git, cycle de vie curé (`draft → review → evergreen` ou `stale → deprecated → archive`) *« qui empêche un vault de devenir une décharge de pages à moitié lues »*, provenance par `--suggested-by` avec une règle de lint détectant les composantes déconnectées, hubs et backlinks. C'est l'architecture de ce corpus de veille, découverte indépendamment. Ce que hyperresearch a en plus : score de qualité par source, audit d'indépendance, balayage de rétractation, recherche sémantique optionnelle, statut de cycle de vie explicite. Piste d'inspiration pour `scripts/`.

### Reprise et budget

Chaque run possède un espace isolé (`research/runs/<tag>/`) et un manifeste servant de *« durable memory »* : un run planté reprend exactement à l'étape morte (`run resume`). `run init --budget 50` **bloque** le run au franchissement du plafond *« rather than letting it quietly balloon »*.

### Réserves

- **La revendication de classement ne tient pas.** Le README annonce *« currently leads the DeepResearch-Bench RACE leaderboard (benchmarked internally) »* avec un graphique le plaçant devant Gemini et OpenAI Deep Research ; la note sous le graphique dit *« Forward-looking projection from a stratified pilot… Third party validation is pending. »* Une projection issue d'un pilote auto-administré n'est pas un classement. Citer le dispositif, jamais le classement.
- **Dépendance Anthropic** : *« It runs on Anthropic models via the subagent roster »* — Opus pour critiques, synthétiseur et patcheur, Sonnet pour les fetchers. Portage Codex souhaité mais non fait.
- **Coût non chiffré** : `premier` vise 100-130 sources et ~3-5 h, `dissertation` 300-450 sources et 4-8 h ; le budget se plafonne en *API-equivalent spend*, pas en coût constaté.
- **Limite assumée par l'auteur** : *« The lint gate catches structural failures… It cannot guarantee factual accuracy, that's still your call. »* Vérification structurelle n'est pas exactitude factuelle.
- **Frontière dure** : *« CAPTCHAs, 2FA, and logins are never solved automatically »* — consolidés et rendus à l'humain.
- **Surface de dépendance** : 20 skills, 16 sous-agents et une CLI qui pilote un navigateur authentifié, sur un dépôt de moins de quatre mois.

## RésuméDe400mots

**hyperresearch** (Jordan Gibbs, MIT, PyPI) transforme Claude Code en agent de deep research. Observé le 3 août 2026 : 1 568 étoiles, dépôt créé en avril. L'installation dépose **20 skills**, une CLI, un serveur MCP et une UI web locale.

**Le pipeline** compte 16 étapes adaptatives par paliers : `light` (~30-40 min) pour les questions bornées, `full` (1,5-2,5 h) pour l'analyse argumentative avec revue adverse, `dissertation` (4-8 h, 25 000-80 000 mots, 300-450 sources) sur demande explicite. Trois leviers distincts : les **paliers** décident quelles étapes tournent, les **gears** de combien, les **levers** (`teach`/`survey`/`analyze`/`advocate`) de quelle voix sort le rapport.

**L'architecture répond à un échec documenté.** La skill d'entrée est un **routeur mince** sans procédure : *« V7 was one 1200-line skill that got compacted away… The orchestrator forgot the procedure, wrote a single draft, and produced a flat-scoring report. »* Chaque étape vit dans sa propre skill, chargée fraîche à l'invocation — un long pipeline ne perd pas ses étapes par oubli, mais par éviction de contexte.

**Deux principes porteurs.** *« Patch, never regenerate »* : après la synthèse, seules des retouches chirurgicales sont possibles, le patcheur étant **verrouillé à `[Read, Edit]`** au niveau de l'allowlist, si bien qu'il *« physically cannot Write a new draft »* — l'impossibilité mécanique remplace la consigne. Et *« canonical research query is gospel »* : le prompt verbatim est persisté et relu par chaque étape.

**La vérification est le seul étage soustrait au style** — les levers injectent des shims dans les prompts des critiques, mais *« the cite-checker and the ship gate receive no shim at all »*. Trois gates bloquent l'expédition : toute citation doit exister **verbatim** dans le vault, une source rétractée non signalée est une erreur dure (avec balayage rafraîchi sur chaque DOI cité), et les nombres non traçables sont signalés.

**Le vault** est markdown persistant indexé en SQLite — *« Markdown is truth, SQLite is cache »* — avec cycle de vie des notes, provenance, score de qualité composite et **audit d'indépendance** : *« five reprints of one press release argue with the weight of one source »*. Les corps récupérés du web sont servis dans une clôture `<untrusted-source>` : *« Fetched text is data, never instructions. »*

**La réserve.** Le README annonce mener le classement DeepResearch-Bench ; sa propre note précise qu'il s'agit d'une *« forward-looking projection from a stratified pilot »* sans validation tierce. Citer le dispositif, jamais le classement. L'auteur reconnaît par ailleurs que le lint *« cannot guarantee factual accuracy »*.

## Commentaire

**En une phrase** : hyperresearch est un harnais qui traite la recherche documentaire agentique comme une **chaîne de production sous contraintes mécaniques**, où chaque risque connu du deep research par LLM reçoit une parade structurelle plutôt qu'une consigne.

**L'idée centrale** est que les modes d'échec du deep research agentique sont **connus et énumérables**, donc outillables un par un. Le README les nomme et leur oppose chaque fois un mécanisme : le rapport dérive en réécriture ? On retire l'outil d'écriture. Le modèle oublie une étape en cours de route ? On charge la procédure au moment de l'invocation. Une citation est inventée ? Elle doit exister verbatim dans le vault, ou le rapport ne part pas. Cinq sources concordent ? On vérifie qu'elles ne sont pas cinq reprises d'un même communiqué. Une page web s'adresse à l'agent ? Son corps est servi dans une clôture qui le désigne comme donnée. Un article payant n'est lu qu'en abstract ? On va chercher une copie légale et on **déclare** la substitution.

**Les principes** qui structurent l'ensemble se ramènent à trois. **La contrainte bat la consigne** — le verrouillage d'outils, les gates de lint et les clôtures ne dépendent pas de la coopération du modèle. **Le contexte se charge au dernier moment** — le routeur mince existe parce qu'un long contexte se fait évincer, ce qui est un fait d'ingénierie et non un défaut de rédaction du prompt. **La vérification ne se négocie pas** — le style du rapport est paramétrable, la vérification ne l'est pas.

**En résumé** : c'est le dispositif de deep research agentique le plus complètement instrumenté publiquement disponible à ce jour, et sa documentation vaut d'être lue **même sans l'installer**, parce qu'elle constitue un catalogue raisonné des façons dont une recherche menée par agent se trompe. Sa faiblesse est ailleurs : une revendication de performance que ses propres notes de bas de page ne soutiennent pas.

## Lecture commentée du SKILL.md

Le fichier commenté est la skill d'entrée, `src/hyperresearch/skills/hyperresearch.md` (~24 Ko).

**Le frontmatter annonce la nature du fichier — un routeur, pas une procédure** :

```yaml
name: hyperresearch
description: >
  Deep research via the HYPERRESEARCH V8 architecture — a tier-adaptive 16-step
  pipeline (light / full / dissertation) … This entry skill is a ROUTER.
  It does not contain step procedures — it tells you which Skill to invoke
  for each step, in order.
```

*Glose* : la `description` est ce que l'agent lit pour décider de charger la skill ; y écrire en majuscules **ROUTER** et nier explicitement la présence de procédures est un choix de design — l'agent est prévenu qu'il devra invoquer autre chose. On notera les **marqueurs de gabarit** `<< p.time_estimate >>` : le fichier est **rendu à l'installation** depuis le profil d'échelle, ce qui explique que changer de gear « prenne effet au run suivant, jamais en cours de run ».

**La dépossession de l'orchestrateur, énoncée d'emblée** :

> *« You are the orchestrator. Your entire job in this conversation is: 1. Read this file once at the start. 2. Bootstrap canonical inputs… 3. Invoke each step skill in sequence via the `Skill` tool. 4. Between steps, do nothing except mark todos and (optionally) think… You do NOT do the work of any step yourself. »*

*Glose* : la contre-mesure vise la tendance d'un orchestrateur à « aider » en faisant lui-même le travail de l'étape suivante — ce qui contaminerait son contexte et casserait le bénéfice du chargement différé.

**Le passage le plus instructif du dépôt, la justification du design** :

> *« Why this design? Context compaction. V7 was one 1200-line skill that got compacted away by the time Layer 4 needed its triple-draft procedure. The orchestrator forgot the procedure, wrote a single draft, and produced a flat-scoring report. V8 fixes this at the source: each step's procedure is loaded into context **only at the moment it's needed**, fresh, with no eviction risk. »*

*Glose* : un **post-mortem** intégré à la documentation d'architecture. Le symptôme (un seul brouillon au lieu de trois) était silencieux — rien n'échouait, la qualité baissait. C'est le mode d'échec le plus dangereux d'un pipeline long, et la seule parade fiable est de ne pas dépendre de la persistance du contexte.

**Le bootstrap installe la mémoire durable avant toute étape** — sept points numérotés dont trois portent l'essentiel :

> *« Persist the query file. Write the verbatim canonical query to `research/runs/<vault_tag>/query.md` … This file is the **canonical query reference for the entire pipeline**. Every step skill and every subagent reads it by path. »*

> *« The manifest is your durable memory: record every step transition with `hyperresearch run step <vault_tag> <N> --status running|done -j` as you go. »*

> *« Seed the TodoWrite list … The todo list survives context compaction; it's your durable memory of where you are in the chain. »*

*Glose* : **trois mémoires externes redondantes** — le fichier de requête pour *quoi*, le manifeste pour *où j'en suis* de façon persistante et interrogeable, la todo list pour *où j'en suis* dans la fenêtre courante. Toutes trois existent parce que le contexte, lui, ne survit pas. Le choix de nommer la todo list « durable memory » dit tout du problème traité.

**Les quatre règles canoniques, en majuscules** :

> *« 1. NEVER EMIT BARE TEXT WHILE TASKS ARE RUNNING. In non-interactive (`-p`) mode, a text-only response (no tool call) triggers `end_turn` — the process exits and the pipeline dies. »*

*Glose* : une contrainte **du harnais**, pas du modèle — en mode `-p`, une réponse sans appel d'outil termine le processus. La parade recommandée (écrire ses pensées dans `orchestrator-notes.md`) transforme une limite d'exécution en journal de raisonnement. Détail révélateur d'un projet qui tourne vraiment en non-interactif.

> *« 2. PATCH, NEVER REGENERATE. … Both subagents are tool-locked to `[Read, Edit]`. If a critic's finding would require rewriting a whole section, it escalates to you as a structural issue — not a rewrite. »*

> *« 4. RESPECT THE TIER GATE. Don't add steps "for thoroughness." Don't drop steps "for budget." The tier is a binding contract. »*

*Glose* : la règle 4 traite les deux dérives symétriques d'un agent zélé — en ajouter « pour bien faire » et en retirer « pour économiser ». Ailleurs le texte insiste : *« The tier classification is a product decision: simple queries should produce fast, right-sized answers. Trust the classification. »*

**Choix de design à retenir** : la **modularisation par fichiers annexes** (une skill par étape) n'est pas ici une commodité de lecture mais la réponse à un mode d'échec mesuré ; le **gabarit rendu à l'installation** rend les paramètres d'échelle inspectables dans les fichiers eux-mêmes plutôt que cachés dans du code ; et la **redondance des mémoires externes** est assumée comme un coût nécessaire.

## Déclencheur

**Quand la skill s'active** : sur invocation explicite `/hyperresearch <sujet>` dans Claude Code, après `pip install hyperresearch && hyperresearch install` dans le projet (ou `--global` pour toutes les sessions, au prix d'environ quinze lignes dans le *system reminder* de chaque session).

**Entrées attendues** :
- un **prompt de recherche en langue naturelle**, dont la forme verbale détermine le registre du rapport (« explique-moi X » → `teach` ; « quel est le paysage » → `survey` ; défaut → `analyze` ; « défends la thèse que » → `advocate`) ;
- optionnellement, une demande explicite de palier `dissertation` — jamais choisi automatiquement ;
- optionnellement, un plafond de dépense (`run init --budget`), un gear installé (`profile use premier`), ou des directives explicites de registre qui l'emportent sur l'inférence.

**Ce qui est résolu automatiquement au démarrage** : création du vault si absent, installation des 16 skills d'étapes si absentes, archivage des artefacts d'anciennes versions, frappe d'un `vault_tag` unique, initialisation de l'espace de run.

**Quand ne pas la déclencher** : question factuelle simple à réponse connue (le palier `light` existe mais reste une trentaine de minutes), sujet sans littérature accessible, ou besoin d'une réponse immédiate.

## Fonctionnement

**La boucle de l'orchestrateur** est délibérément pauvre : lire le fichier d'entrée une fois → bootstrapper les entrées canoniques → invoquer `Skill(skill: "hyperresearch-N-...")` dans l'ordre dicté par le palier → entre deux étapes, ne rien faire d'autre que marquer les todos et consigner des notes. L'orchestrateur **ne fait le travail d'aucune étape**.

**Le mécanisme d'échelle**, en trois couches indépendantes :

| Couche | Décide | Quand elle s'applique |
|---|---|---|
| **Palier** (`tier`) | quelles étapes tournent | classé par l'étape 1, par requête |
| **Gear** (profil) | l'ampleur : sources, profondeur, longueur | rendu à l'installation, effectif au run suivant |
| **Levers** | le registre et la profondeur d'inférence | inférés du prompt, surchargeables |

**Le fan-out** repose sur seize sous-agents aux rôles fixes et aux modèles configurables : fetchers (8-12 en parallèle par vague), analystes de sources longues, analystes de loci, investigateurs de profondeur (K en parallèle), trois rédacteurs d'angle, un synthétiseur, **quatre critiques adverses en parallèle** (dialectique, profondeur, largeur, instruction), un patcheur, un vérificateur de citations, un auditeur de polissage, un recommandeur de lisibilité, un fetcher-navigateur.

**La chaîne de contrôle en fin de course** est ce qui distingue le dispositif : les critiques attaquent le brouillon → leurs conclusions ne peuvent être appliquées que par un patcheur **incapable d'écrire un fichier** → les conclusions trop larges pour une retouche remontent comme problèmes structurels → un vérificateur sceptique échantillonne les liaisons citation-phrase → une batterie de vérifications bloque l'expédition (citation verbatim, rétractation, cohérence numérique).

**La boucle longue** est le vault : chaque source lue y demeure, indexée et scorée, et la session suivante y cherche **avant** de récupérer quoi que ce soit du web — *« each session starts smarter than the last »*.

## Artefacts

**Espace de run** — `research/runs/<vault_tag>/` :
- `query.md` — le prompt utilisateur verbatim, référence canonique de tout le pipeline
- `run.json` — le manifeste (transitions d'étapes, dépense, file d'escalades) ; support de la reprise
- `scaffold.md` — document de planification privé, **interdit d'apparition dans le rapport final**
- `prompt-decomposition.json` — items atomiques, matrice de couverture, palier retenu
- `loci.json`, `comparisons.md`, `source-tensions.json`, `evidence-digest.md` — sorties d'analyse intermédiaires
- `temp/orchestrator-notes.md` — journal de raisonnement de l'orchestrateur
- `final_report.md` — le livrable

**Vault** — `research/notes/` : une note markdown par source, frontmatter YAML (dont `oa_url`, `oa_version`, `oa_recovery_kind`, `raw_file`, statut de cycle de vie), PDF bruts en `research/raw/<note-id>.pdf`, index SQLite **reconstructible** par `hyperresearch sync`, pages d'index générées, graphe de liens et de provenance.

**Sorties hors Claude Code** : serveur MCP (treize outils dont `search_notes`, `read_many`, `get_backlinks`, `lint_vault`), UI web locale sur le port 8080 sans dépendance JavaScript, exports JSON et vault filtré.

## Anti-patterns

- **Citer le classement DeepResearch-Bench.** La revendication de tête de leaderboard est une **projection auto-administrée en attente de validation tierce**, selon la note du dépôt lui-même. Citer l'architecture, jamais le rang.
- **Confondre vérification structurelle et exactitude.** L'auteur le dit : *« It cannot guarantee factual accuracy, that's still your call. »* Le dispositif garantit qu'une citation existe et qu'elle soutient sa phrase — pas que la source ait raison.
- **Lancer `full` ou `premier` sur une question bornée.** Le palier `light` existe pour ça, et la skill interdit explicitement de monter en palier « pour être exhaustif ».
- **Traiter une note `rescued` comme une lecture de la source.** `nothing_from_source: true` signifie que **rien** — ni titre, ni auteurs, ni corps — ne vient de l'URL en `source:`. À prendre au pied de la lettre.
- **Citer directement depuis une version non finale.** Si `oa_version` vaut `acceptedVersion` ou `submittedVersion`, vérifier la citation contre l'article publié.
- **Installer en `--global` sans y penser.** Coût permanent d'environ quinze lignes dans le *system reminder* de **toutes** les sessions Claude Code, y compris sans rapport avec la recherche.
- **Adopter sans revue de la chaîne de dépendances.** 20 skills, 16 sous-agents, une CLI pilotant un navigateur authentifié, sur un dépôt de moins de quatre mois — exactement la surface que [[lassiege-usine-logicielle-heure-ia-2026-07-28]] recommande de scruter.
- **Compter sur un portage hors Anthropic.** Le roster suppose Opus et Sonnet ; le portage Codex est souhaité par l'auteur, pas réalisé.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Jordan Gibbs | PERSONNE | a_créé | hyperresearch | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| hyperresearch | METHODOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| hyperresearch | METHODOLOGIE | permet | de transformer un agent de codage en agent de recherche documentaire profonde | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| skill d'entrée routeur | CONCEPT | résout | l'éviction par compaction de la procédure d'une étape dans un pipeline long | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| hyperresearch | METHODOLOGIE | affirme_que | une skill unique de 1200 lignes se fait évincer du contexte et l'orchestrateur en oublie silencieusement des étapes | CITATION | 0.95 | STATIQUE | déclaré_article |
| verrouillage d'outils | CONCEPT | permet | de rendre une réécriture mécaniquement impossible plutôt que déconseillée | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| verrouillage d'outils | CONCEPT | surpasse | une consigne de prompt pour garantir un comportement d'agent | AFFIRMATION | 0.92 | ATEMPOREL | inféré |
| hyperresearch | METHODOLOGIE | recommande | de ne modifier un rapport synthétisé que par retouches chirurgicales, jamais par régénération | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| prompt utilisateur verbatim | CONCEPT | fait_partie_de | contrat canonique relu par chaque étape et chaque sous-agent | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| audit d'indépendance des sources | CONCEPT | réduit | le poids d'un consensus apparent formé de reprises d'un même communiqué | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| vérification de l'intégrité des citations | CONCEPT | résout | l'expédition de citations hallucinées, en exigeant leur présence verbatim dans le corpus | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| balayage de rétractation | CONCEPT | s_applique_à | chaque DOI cité au moment de l'expédition, y compris sur des sources réutilisées | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| hyperresearch | METHODOLOGIE | affirme_que | le texte récupéré du web est une donnée et jamais une instruction | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| clôture untrusted-source | CONCEPT | réduit | le risque d'injection de prompt par une page web lue par un agent | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| notes produites par les sous-agents du pipeline | CONCEPT | s_oppose_à | les corps récupérés du web, servis sous clôture — frontière de confiance par provenance | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| récupération en accès ouvert | CONCEPT | résout | la citation d'un article payant lu seulement en abstract, comme s'il avait été lu | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| hyperresearch | METHODOLOGIE | utilise | Unpaywall | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| hyperresearch | METHODOLOGIE | utilise | Europe PMC | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| note rescued | CONCEPT | affirme_que | ni le titre, ni les auteurs, ni le corps ne proviennent de l'URL déclarée en source | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| hyperresearch | CONCEPT | est_basé_sur | markdown comme source de vérité et index SQLite reconstructible comme cache | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| hyperresearch | CONCEPT | converge_avec | l'architecture médaillon d'un corpus de veille en fichiers | CONCEPT | 0.85 | ATEMPOREL | inféré |
| score de qualité de source | CONCEPT | est_basé_sur | type de source, utilité constatée, autorité de citation avec rétractations, et centralité PageRank interne | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| vérification | CONCEPT | s_oppose_à | le paramétrage par registre, qui module les critiques mais jamais le contrôle des citations | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| hyperresearch | METHODOLOGIE | affirme_que | le gate de lint attrape les défaillances structurelles mais ne garantit pas l'exactitude factuelle | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| hyperresearch | METHODOLOGIE | mesure | une position de tête sur DeepResearch-Bench RACE, présentée comme projection prospective auto-administrée sans validation tierce | MESURE | 0.75 | DYNAMIQUE | déclaré_article |
| hyperresearch | METHODOLOGIE | utilise | modèles Anthropic Opus et Sonnet via un roster de seize sous-agents | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| hyperresearch | METHODOLOGIE | s_oppose_à | la résolution automatique des CAPTCHA, de la double authentification et des connexions | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| hyperresearch | METHODOLOGIE | définition | Harnais de deep research pour Claude Code : 20 skills, CLI Python, serveur MCP et UI locale, orchestrant un pipeline de 16 étapes adaptatif par paliers vers un rapport audité de façon adverse avec provenance complète | AJOUT |
| hyperresearch | METHODOLOGIE | adoption | MIT, PyPI, Python 3.11-3.13 ; dépôt créé le 9 avril 2026, 1 568 étoiles et 170 forks au 3 août 2026 | AJOUT |
| Jordan Gibbs | PERSONNE | rôle | Auteur et mainteneur de hyperresearch | AJOUT |
| skill routeur | CONCEPT | définition | Skill d'entrée qui ne contient aucune procédure et se borne à invoquer une skill par étape, afin que chaque procédure soit chargée fraîche au moment utile et échappe à l'éviction par compaction | AJOUT |
| verrouillage d'outils | CONCEPT | définition | Restriction de l'allowlist d'un sous-agent à un jeu d'outils donné, rendant un comportement mécaniquement impossible au lieu de le déconseiller par consigne | AJOUT |
| audit d'indépendance des sources | CONCEPT | définition | Regroupement des copies syndiquées et dérivées afin qu'un ensemble de reprises d'une même origine ne compte que pour une voix dans l'évaluation d'un consensus | AJOUT |
| clôture untrusted-source | CONCEPT | définition | Enveloppe délimitant tout corps récupéré du web comme donnée et non comme instruction, appliquée sur chaque chemin qui sert un corps, avec neutralisation des balises contrefaites et enveloppement postérieur à la troncature | AJOUT |
| note rescued | CONCEPT | définition | Note construite entièrement depuis une copie en accès ouvert parce que la source déclarée n'a pas pu être lue du tout — marquée nothing_from_source et signalée par bannière | AJOUT |
| vault de recherche | CONCEPT | définition | Magasin persistant de sources en markdown avec index reconstructible, cycle de vie curé des notes, provenance traçable et score de qualité, consulté avant toute nouvelle récupération | AJOUT |
| DeepResearch-Bench | DOCUMENT | référence | Classement public de harnais de deep research ; la position de tête revendiquée par hyperresearch est une projection prospective auto-administrée, validation tierce en attente | AJOUT |
