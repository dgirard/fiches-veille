---
themes: [agents-codage-ia-skills, outils-plateformes, architecture-construction, economie-marche]
source: "DeepSeek"
---
# deepseek-harness-everything-is-a-plugin-2026-08-13

## Veille

Page produit officielle de **DeepSeek**, publiée le **13 août 2026**, **non signée**, ~450 mots, annonçant la mise en *developer preview* de **DeepSeek Harness** (`dsh`) — un harnais d'agent de codage **open source sous licence MIT**, dont le dépôt est ouvert le même jour. Thèse en trois mots, répétée en titre et en description du dépôt : *« Everything is a plugin »*, assortie d'une seconde promesse, *« Every run is traceable »*. La page pose l'équation *« AGENT = MODEL + HARNESS »* et énumère les capacités enfichables — *« models, tools, skills, sessions, sandboxes, storage, loops, scheduling, and the UI »*. Quatre modes sont livrés : **Standard** (agent de codage complet), **Code** (outils exposés via le *Code Mode SDK*, pour que le modèle compose des opérations multi-étapes dans un programme TypeScript), **Minimal** (*« two-tool coding agent with persistent bash and str_replace_editor »*, explicitement *« for benchmarking models in a minimal environment »*) et **Creator** (inspection du runtime, test de plugins en mémoire). La substance technique est dans le dépôt, non sur la page : `docs/architecture.md` énonce un invariant de journalisation — *« Model-visible means logged. Anything that reaches a model request must be reconstructable from the log, and a runtime invariant asserts it »* — et pose qu'*« il n'y a pas de noyau privilégié à patcher »*. Le noyau technique n'est pas de DeepSeek : DSH est bâti sur **Cordis** (projet `cordiverse`, tiers), **vendoré** dans `vendor/` avec manifeste et procédure de synchronisation, et la page met le *« Cordis paper »* au même rang de navigation que « GitHub » et « Developer docs ». Deux adaptateurs LLM sont livrés — `dsh-llm-deepseek` et `dsh-llm-pi-ai`, adaptateur multi-fournisseurs générique. Le dépôt avertit en capitales : *« THERE WILL BE COMPATIBILITY-BREAKING CHANGES »*, et `CLAUDE.md` précise que `SESSION_FORMAT_VERSION` reste à `0` *« with no compatibility promise »*, les backends rejetant les anciens formats sur disque. Calendrier : DSH sort le jour où **DeepSeek-V4-Pro passe en GA**, trois jours avant une nouvelle grille tarifaire API effective le **16 août 2026 à 16:00 UTC**, en heures pleines / heures creuses avec un creux à **−50 %**.

## Titre Article

DeepSeek Harness developer preview: Everything is a plugin

## Date

2026-08-13

## URL

https://deepseek.com/harness/en/

## Keywords

DeepSeek Harness, dsh, harnais d'agent, agent harness, everything is a plugin, Cordis, cordiverse, composabilité spatiotemporelle, vendoring, plugin, montage démontage, effets réversibles, services typés, contexte partagé, profil, bundle, dsh-base, dsh-web-app, dsh-headless, dump-config, licence MIT, open source, developer preview, breaking changes, SESSION_FORMAT_VERSION, log de session append-only, SessionEvent, deriveMessages, model-visible means logged, invariant runtime, traçabilité, replay, resume, fork, turn, step, agent/pre-step, llm/stream, tools/execute, waterfall, capability seam, couture de capacité, Service Definition, Service Provider, adaptateur LLM, dsh-llm-deepseek, dsh-llm-pi-ai, gateway OpenAI-compatible, mode Standard, mode Code, mode Minimal, mode Creator, Code Mode SDK, str_replace_editor, bash persistant, subagent, workflow, compaction, skill, MCP, ACP, LSP, E2B, sandbox, hooks, DeepSeek-V4-Pro, GA, OpenAI Responses API, Codex, tarification heures pleines heures creuses, Safe Use Policy, injection de prompt, Claude Code, CLAUDE.md, AGENTS.md, harnais d'évaluation, BENCHMARK.md

## Authors

**DeepSeek** (DeepSeek AI, laboratoire chinois), en tant qu'institution. Page produit **non signée** : aucun auteur, aucun ingénieur mis en avant, aucun billet de blog ni papier technique associé. Le « nous » n'apparaît qu'une fois, en dernière phrase — *« We look forward to exploring the limits of intelligence with developers worldwide »*. Publiée le **13 août 2026**. La page est rendue en JavaScript : `curl` sur l'URL renvoie **HTTP 202 avec un corps vide**, le texte n'existant qu'après exécution du bundle. Deux documents de politique sont liés en pied de page — *Safe Use Policy* et *Data Processing Statement*.

## Ton

**Profil** : page de lancement produit d'un laboratoire de modèles, registre note d'architecture abrégée — courte, déclarative, sans superlatif, sans chiffre, sans concurrent nommé. Public : **développeurs de harnais**, pas utilisateurs finaux ; l'adresse est explicite dès le chapeau (*« for agent harness developers worldwide »*).

**Style** : la thèse tient en une phrase nominale répétée à l'identique — *« Everything is a plugin »* est le titre H1, la description du dépôt et l'en-tête de la section design ; la liste des capacités enfichables est elle aussi reprise mot pour mot à trois endroits. Une seule métaphore dans toute la page, adossée à l'équation en capitales *« AGENT = MODEL + HARNESS »* : *« The model is the soul of an agent. »* L'absence de comparatif est totale — ni Claude Code, ni Codex, ni Cline, ni OpenCode, aucun benchmark, aucun prix — et l'appel final s'adresse non à des utilisateurs mais à des contributeurs (*« Join the DSH plugin ecosystem »*). L'aveu d'instabilité monte en intensité selon le support : la page dit *« remains in developer preview […] Its core plugins and APIs will continue to evolve »*, le dépôt dit en gras et en capitales *« THERE WILL BE COMPATIBILITY-BREAKING CHANGES. »* La prose du dépôt relève d'un autre registre, dense et sans remplissage : *« There is no privileged core to patch »*, *« registrations are effects that unwind when their plugin unloads »*, *« Model-visible means logged »*, *« Seams are why one provider swap changes the whole product »*. Elle contient aussi cette recommandation, qui date le document : *« We recommend using an agent to explore the codebase and understand its architecture. »*

**Formules-marqueurs** :
- ***« Everything is a plugin »*** · ***« Every run is traceable »***
- ***« Agent = Model + Harness »*** · ***« The model is the soul of an agent »***
- ***« select, swap, or extend any capability in configuration without changing the DeepSeek Harness source code »***
- ***« Everything the model sees is recorded in an append-only session log »***
- ***« Resume, fork, search, and replay all operate on the same event stream »***
- ***« There is no privileged core to patch »*** (dépôt)
- ***« Model-visible means logged »*** (dépôt)
- ***« THERE WILL BE COMPATIBILITY-BREAKING CHANGES »*** (dépôt)

**Position épistémique** : acteur intéressé qui publie son code. La page n'est vérifiable sur rien, mais elle n'affirme presque rien de vérifiable — elle ne contient ni benchmark, ni comparaison, ni prix, ni numéro de version, ni même mention d'un modèle DeepSeek. Le dépôt, lui, est testable affirmation par affirmation. C'est là que se déplace l'évaluation.

## Pense-betes

- **Date / source** : **13 août 2026**, page produit `deepseek.com/harness`, non signée. Dépôt `deepseek-ai/deepseek-harness` ouvert le même jour sous **MIT**.
- **Cadrage clé** : la composabilité par plugins est banale en 2026 ; l'élément distinctif est ailleurs, dans `docs/architecture.md` et non sur la page de vente.

### L'invariant de journalisation

> *« **Model-visible means logged.** Anything that reaches a model request must be reconstructable from the log, and a runtime invariant asserts it. This is why a new model-visible input requires a new session event: extend `SessionEventMap` and render from the log. »*

Trois propriétés en découlent. C'est une **contrainte exécutable**, non une intention : le harnais échoue si du contexte atteint le modèle sans être inscrit au log. Le log devient la **source** et non le compte rendu — `deriveMessages()` projette l'historique modèle depuis le flux, et *« Fork, resume, transcripts, telemetry, and persistence all derive from this stream »*, sans état parallèle à désynchroniser. Enfin, c'est une réponse d'ingénierie à la question que pose tout post-mortem d'incident agentique : qu'est-ce que l'agent a réellement vu ? Critère extractible pour qui évalue un harnais : *tout ce qui atteint le modèle est-il reconstructible depuis un journal unique, et cette propriété est-elle assertée à l'exécution ?*

### Traçable n'est pas archivable

| Où | Ce qui est écrit |
|---|---|
| Page produit | *« Every run is traceable »* — resume, fork, search, replay sur le même flux |
| `README.md` | *« THERE WILL BE COMPATIBILITY-BREAKING CHANGES. »* |
| `CLAUDE.md` | *« `dsh-session` keeps `SESSION_FORMAT_VERSION` at `0` with no compatibility promise »* ; *« Backends reject old on-disk formats »* |

Concrètement : une session enregistrée aujourd'hui peut devenir illisible après mise à jour, le backend la rejetant activement plutôt que de tenter une migration. La posture est assumée et datée — *« Pre-release stance: foundation over blast radius. Remove this section at the first tagged release. With no external consumers, prefer the correct foundation over compatibility shims »*. Règle pratique : ne pas fonder de conformité, d'audit ou de rétention sur les logs DSH avant la première release taguée ; le repère à guetter est la disparition de la section *« Pre-release stance »* du `CLAUDE.md`, que DeepSeek désigne lui-même comme le signal.

### Le calendrier

| Date | Événement |
|---|---|
| **13 août 2026** | DSH publié sous MIT + **DeepSeek-V4-Pro en GA** (`DeepSeek-V4-Pro-0813`), support natif de l'**OpenAI Responses API**, intégration optimisée pour **Codex** |
| **16 août 2026, 16:00 UTC** | Nouvelle grille tarifaire API : heures pleines / heures creuses, *« Off-peak rates are 50% lower than peak »* |
| **14 août 2026** | Z.ai annonce GLM-5.3 avec le même dispositif de barème horaire — [[zai-glm-53-emergent-cyber-2026-08-14]] |

Le harnais est donné, l'inférence est renchérie : un harnais MIT capable de router vers n'importe quel fournisseur n'a de valeur pour DeepSeek que s'il crée du volume de tokens. Deux prudences : le rapport d'environ 4,5× sur les tokens de sortie V4-Pro vient de la presse et non de l'annonce API, qui ne publie que le principe et le −50 % ; et un barème calé sur un fuseau asiatique déplace le coût réel pour une équipe européenne.

### « Everything is a plugin » : état des lieux au 13 août

| Couche | Ce qui est livré | État |
|---|---|---|
| **Modèles** | `dsh-llm-deepseek` (route `deepseek-official`) et `dsh-llm-pi-ai`, adaptateur multi-fournisseurs générique adossé à `@earendil-works/pi-ai` | tenu — *« un gateway OpenAI-compatible, un serveur auto-hébergé ou un fournisseur plus récent que le catalogue installé est de la configuration, pas un changement de code »* |
| **Exécution / sandbox** | seams `ctx.fs`, `ctx.shell`, `ctx.subprocess`, `ctx.sandbox` ; POC **E2B** | mécanisme en place, un backend distant en POC |
| **UI / distribution** | bundles `dsh-base`, `dsh-web-app`, `dsh-headless` ; profils `web` et `headless` | tenu |
| **Boucle d'agent** | `core/agent-loop` décrit comme *« the default driver »* derrière l'interface `Agent` | tenu par construction |
| **Écosystème tiers** | topic `dsh-plugin`, page « Community plugins » | à observer — un écosystème à J+0 n'existe pas |

La phrase qui rend la promesse crédible est architecturale : *« There is no privileged core to patch: you extend dsh by mounting a plugin beside the others, and registrations are effects that unwind when their plugin unloads. »* Corollaire opérationnel : *« Seams are why one provider swap changes the whole product. Filesystem and subprocess providers share one execution world, so pointing them at a remote sandbox moves Bash, PTY, and LSP with them, with no provider forks. »* Principe réutilisable hors DSH : une couture n'existe que si les trois rôles — Service Definition, Service Provider, Consumer — sont conçus ensemble, *« one role alone is not a seam »*. Vérification en une commande : `dsh --profile web --dump-config` imprime l'arbre réellement démarré, et *« any row it prints can be replaced by a patch of your own »*.

### Le mode Minimal

Livré *« for benchmarking models in a minimal environment »*, avec `BENCHMARK.md` pointant la variante `jsonrpc-agent` du SDK Python. Le contexte éclaire l'intention : le lendemain, un laboratoire chinois documentait mesurer son modèle et ceux de ses concurrents *« in Claude Code 2.1.207 »*, le harnais d'un concurrent servant d'infrastructure de mesure partagée. DSH livre le harnais minimal de benchmark dans le produit, sous MIT. Réserve : au 13 août aucun score n'est publié, et rien n'indique qu'un tiers ait adopté ce harnais. Enjeu de portabilité sous-jacent : [[janakiram-agent-platform-portability-contract-2026-07-20]].

### Le noyau appartient à un tiers

DSH est bâti sur **Cordis** (`cordiverse`, projet indépendant), dont la conception est publiée dans un papier tiers — *A Programming Paradigm for Spatiotemporal Composability*. Dans le dépôt, Cordis est vendoré (`vendor/cordis` et neuf modules frères : `cosmokit`, `hmr`, `loader`, `schemastery`, `timer`…) avec manifeste et procédure de synchronisation. Trois lectures simultanément valables : DeepSeek cite sa dépendance plutôt que de la rebaptiser ; le vendoring gèle la version et supprime la dépendance de disponibilité, au prix d'une synchronisation à tenir ; et l'argument central du produit repose sur la propriété intellectuelle d'un projet communautaire que DeepSeek ne contrôle pas. Pour qui évalue la pérennité de DSH, la santé de `cordiverse/cordis` est une variable au moins aussi importante que celle du dépôt DeepSeek.

### La Safe Use Policy

> *« Because Harness has the ability to run code and execute actions on your machine, it introduces unique security risks. Although most foundation models include **basic** safeguards against prompt injection, inherent risks remain […] In some cases, the Agent may execute commands embedded in content, even if those commands conflict with the assigned task. »*

Les précautions recommandées forment une doctrine d'usage utilisable indépendamment de DSH : machine virtuelle dédiée ; vérifier les sorties ; ne pas fournir d'information sensible ou confidentielle ; exiger une approbation humaine pour toute opération à effet significatif ; découper les instructions complexes en opérations isolées, pour *« reduce the risk that a single erroneous command affects multiple parts of the system simultaneously »* ; n'installer que des plugins, serveurs MCP, Skills, Hooks et dépendances issus de sources fiables et revues. La dernière ligne est à mettre en regard de l'argument de vente : la surface d'attaque croît avec la composabilité. Voir [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]].

### Modélisation `turn` / `step`, empruntable

*« A **step** is one model request plus the tools it calls. A **turn** is zero or more steps: it opens before its first input is claimed and closes once nothing is owed. »* Le flux complet est publié : `turn/start` → `agent/pre-step` → `step/start` → `agent/request` → `llm/stream` → `tool/call*` → `tools/pre-execute|execute|post-execute` → `step/end` → `agent/turn-stopping` → `turn/end`, avec trois domaines d'extension distingués — *session events* (faits durables survivant au rechargement), *agent events* (interception du travail en vol), *capability events* (politique et adaptateurs sur une couture, *« without importing the loop »*). Deux détails de conception issus d'une vraie expérience d'exploitation : *« a rejected or empty first claim still closes a durable turn that spent no step, so the log records the attempt »* — le tour qui n'a rien fait est journalisé, sans quoi le refus serait invisible au post-mortem ; et la distinction **waterfall** (`agent/pre-step`, `agent/request`, `llm/stream`, `tools/*`, où les écouteurs doivent appeler `next()`) **vs sérial** (`agent/turn-stopping`, sans `next()`), qui rend le contrat de délégation explicite par événement.

### Détail de dépôt

L'arborescence racine de `deepseek-ai/deepseek-harness` contient `CLAUDE.md` (copie conforme d'`AGENTS.md`), `.claude/skills` et un répertoire `.agents`. Un dépôt open source publié en 2026 par un laboratoire de pointe documente ses conventions pour agents au même titre que pour humains : standard de dépôt à reprendre.

### Hygiène de citation

1. **Distinguer la page du dépôt.** Les affirmations fortes viennent de `docs/architecture.md`, `CLAUDE.md` et des `README.md` de packages. Citer *« la documentation d'architecture de DSH »*, jamais *« la page de lancement »*.
2. **120 060 étoiles et 11 831 forks en trois jours** (relevés le 16 août 2026 via l'API GitHub) mesurent l'attention, pas l'adoption, et sont périssables.
3. **Les tarifs ne sont pas dans l'annonce fichée** : citer le principe heures pleines/creuses et le −50 %, sourcer les valeurs en $/M ailleurs.
4. **« Open source » signifie ici MIT et rien de plus** : ni gouvernance ouverte, ni feuille de route publique, ni engagement de compatibilité. Du code ouvert publié par un éditeur, non un projet communautaire — distinction travaillée par [[mozilla-state-of-open-source-ai-2026-07]].

## RésuméDe400mots

Page de lancement produit publiée le **13 août 2026** par **DeepSeek**, **non signée**, pour la mise en *developer preview* de **DeepSeek Harness** (`dsh`), harnais d'agent de codage **open source sous licence MIT** dont le dépôt est ouvert le même jour.

**Ce que dit la page.** Deux promesses, en quatre cents mots et sans un chiffre. **« Everything is a plugin »** : toute capacité — modèles, outils, skills, sessions, sandboxes, stockage, boucles, ordonnancement, interface — est un plugin **substituable par configuration, sans modifier le code source**. **« Every run is traceable »** : tout ce que le modèle voit est inscrit dans un **log de session append-only** — prompts système, raisonnement, appels d'outils et résultats, ordonnancement des subagents, chaque injection de contexte — et *« resume, fork, search et replay opèrent tous sur le même flux d'événements »*. Le noyau est **Cordis**, framework tiers vendoré, décrit dans un papier externe et crédité en évidence. Quatre modes d'exécution sont livrés : **Standard** (outillage complet), **Code** (outils exposés via un SDK TypeScript pour combiner plusieurs opérations en un programme), **Minimal** (deux outils, bash persistant et `str_replace_editor`, *« for benchmarking models in a minimal environment »*) et **Creator** (inspection du runtime, test de plugins en mémoire, composition de nouveaux modes). Démarrage : `npx @deepseek-ai/dsh web`.

**Ce que la page ne dit pas.** L'affirmation la plus forte est dans `docs/architecture.md` : ***« Model-visible means logged. Anything that reaches a model request must be reconstructable from the log, and a runtime invariant asserts it. »*** **Une garantie assertée à l'exécution**, pas un affichage — c'est la propriété qui distingue réellement DSH, et elle est absente de l'argumentaire. Le même dépôt en fournit le démenti : `SESSION_FORMAT_VERSION` reste à **`0` sans promesse de compatibilité**, *« backends reject old on-disk formats »*, et le README avertit en capitales qu'il y aura des ruptures. **Traçable maintenant ne veut pas dire archivable demain.**

**Le modèle d'affaires est dans le calendrier.** DSH sort le jour de la **GA de DeepSeek-V4-Pro** et **trois jours avant** une nouvelle grille tarifaire API (16 août, 16:00 UTC ; heures creuses à **−50 %**). **Harnais donné, inférence renchérie** — l'inverse exact du modèle d'Anthropic.

**Ce qui se vérifie.** La substituabilité tient au moins sur la couche modèle : outre l'adaptateur DeepSeek, **`dsh-llm-pi-ai`** rend tout gateway OpenAI-compatible accessible *« par configuration, pas par changement de code »*. Et le mode Minimal livre le **harnais de mesure** dans le produit — tentative de reprendre à Claude Code la définition du benchmark, alors même que le dépôt de DSH contient un `CLAUDE.md` et un `.claude/skills`.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| DeepSeek | ORGANISATION | publie | DeepSeek Harness | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| DeepSeek Harness | TECHNOLOGIE | est_instance_de | Harness | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| DeepSeek Harness | TECHNOLOGIE | est_basé_sur | Cordis | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Cordis | TECHNOLOGIE | permet | de faire contribuer des services, des événements typés et des effets réversibles à un contexte partagé, chaque enregistrement se dénouant au démontage de son plugin — « there is no privileged core to patch » | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Cordis | TECHNOLOGIE | est_basé_sur | A Programming Paradigm for Spatiotemporal Composability | DOCUMENT | 0.92 | STATIQUE | déclaré_article |
| tout est plugin | CONCEPT | s_applique_à | toute capacité d'agent — modèles, outils, skills, sessions, sandboxes, stockage, boucles, ordonnancement et interface — chacune sélectionnable, remplaçable ou extensible par configuration sans modifier le code source du harnais | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| DeepSeek Harness | TECHNOLOGIE | utilise | tout est plugin | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| log de session append-only | CONCEPT | permet | d'enregistrer tout ce que le modèle voit — prompts système, raisonnement, appels d'outils et résultats, ordonnancement des subagents et chaque injection de contexte — la reprise, le fork, la recherche et le replay opérant tous sur le même flux d'événements | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| DeepSeek Harness | TECHNOLOGIE | utilise | log de session append-only | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| log de session append-only | CONCEPT | affirme_que | tout ce qui atteint une requête modèle doit être reconstructible depuis le journal, un invariant runtime l'assurant — « Model-visible means logged » | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| log de session append-only | CONCEPT | s_oppose_à | l'archivage durable tant que SESSION_FORMAT_VERSION reste à 0 sans promesse de compatibilité et que les backends rejettent les anciens formats sur disque | AFFIRMATION | 0.9 | DYNAMIQUE | inféré |
| DeepSeek Harness | TECHNOLOGIE | s_oppose_à | toute promesse de stabilité en préversion : le dépôt avertit en capitales qu'il y aura des changements cassant la compatibilité | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |
| couture de capacité | CONCEPT | affirme_que | une capacité substituable n'existe que si ses trois rôles sont conçus ensemble — Service Definition, Service Provider et Consumer — un seul rôle ne faisant pas une couture | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| couture de capacité | CONCEPT | permet | qu'un seul remplacement de fournisseur change tout le produit : systèmes de fichiers et sous-processus partageant un même monde d'exécution, les pointer vers un sandbox distant y déplace Bash, PTY et LSP sans fork de fournisseur | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| DeepSeek Harness | TECHNOLOGIE | utilise | couture de capacité | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| DeepSeek Harness | TECHNOLOGIE | utilise | pi-ai | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| pi-ai | TECHNOLOGIE | permet | de déclarer un gateway OpenAI-compatible, un serveur auto-hébergé ou un fournisseur plus récent que le catalogue installé comme de la configuration plutôt que comme un changement de code | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| mode Minimal | TECHNOLOGIE | fait_partie_de | DeepSeek Harness | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| mode Minimal | TECHNOLOGIE | permet | d'évaluer des modèles dans un environnement minimal réduit à deux outils, un bash persistant et str_replace_editor | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| mode Minimal | TECHNOLOGIE | concurrence | Claude Code | TECHNOLOGIE | 0.82 | DYNAMIQUE | inféré |
| Claude Code | TECHNOLOGIE | observé_dans | le dépôt de DeepSeek Harness, qui embarque un CLAUDE.md et un répertoire .claude/skills aux côtés d'AGENTS.md | MESURE | 0.9 | STATIQUE | déclaré_article |
| mode Code | TECHNOLOGIE | fait_partie_de | DeepSeek Harness | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| mode Code | TECHNOLOGIE | permet | d'exposer les outils via le Code Mode SDK pour que le modèle combine des opérations multi-étapes dans un seul programme TypeScript | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| DeepSeek | ORGANISATION | publie | DeepSeek-V4-Pro | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| DeepSeek | ORGANISATION | affirme_que | la nouvelle grille tarifaire de l'API entre en vigueur le 16 août 2026 à 16:00 UTC avec des tarifs heures pleines et heures creuses, les heures creuses étant 50 % moins chères que les heures pleines | MESURE | 0.92 | DYNAMIQUE | déclaré_article |
| DeepSeek Harness | TECHNOLOGIE | permet | de découpler la valeur du harnais de celle du modèle : publié sous MIT le jour même de la disponibilité générale de DeepSeek-V4-Pro et trois jours avant une hausse des tarifs d'API, il fonctionne comme produit d'appel vers l'inférence facturée | AFFIRMATION | 0.85 | DYNAMIQUE | inféré |
| Safe Use Policy | DOCUMENT | affirme_que | l'agent peut, dans certains cas, exécuter des commandes embarquées dans le contenu qu'il lit, même lorsque ces commandes entrent en conflit avec la tâche assignée | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Safe Use Policy | DOCUMENT | recommande | une machine virtuelle dédiée, la vérification des sorties, l'absence d'information confidentielle, une approbation humaine pour toute opération à effet significatif, le découpage des instructions complexes en opérations isolées, et de n'installer que des plugins, serveurs MCP, Skills et Hooks issus de sources fiables et revues | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| DeepSeek Harness | TECHNOLOGIE | mesure | 120 060 étoiles et 11 831 forks sur GitHub au 16 août 2026, soit trois jours après l'ouverture du dépôt — un signal d'attention et non d'adoption | MESURE | 0.88 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| DeepSeek Harness | TECHNOLOGIE | définition | Harnais d'agent de codage open source (MIT) publié par DeepSeek le 13 août 2026 en developer preview, commande `dsh`, écrit en TypeScript, bâti sur le noyau Cordis vendoré. Architecture « everything is a plugin » : modèles, outils, skills, sessions, sandboxes, stockage, boucles, ordonnancement et interface sont substituables par configuration. Journal de session append-only comme source unique du contexte modèle, avec invariant runtime « model-visible means logged ». Quatre modes : Standard, Code, Minimal, Creator. Démarrage par `npx @deepseek-ai/dsh web`, Web UI sur 127.0.0.1:3080. Aucune promesse de compatibilité : SESSION_FORMAT_VERSION à 0, backends rejetant les anciens formats sur disque | AJOUT |
| DeepSeek | ORGANISATION | positionnement | Laboratoire d'IA chinois. Le 13 août 2026, publie simultanément son harnais d'agent sous licence MIT et la disponibilité générale de DeepSeek-V4-Pro, trois jours avant une hausse tarifaire d'API assortie d'un barème heures pleines / heures creuses — harnais donné, inférence facturée. Communique par pages produit institutionnelles non signées, sans billet technique ni auteur nommé | MISE_A_JOUR |
| Cordis | TECHNOLOGIE | définition | Framework de composition par plugins du projet tiers cordiverse, noyau de DeepSeek Harness et vendoré dans son dépôt (avec cosmokit, hmr, loader, schemastery, timer et cinq autres modules) selon un manifeste et une procédure de synchronisation. Les plugins contribuent services, événements typés et effets réversibles à un contexte partagé ; le montage, le démontage et les dépendances sont gérés par le noyau, et les enregistrements se dénouent au déchargement du plugin. Point de dépendance externe : l'argument central du produit repose sur un projet que DeepSeek ne contrôle pas | AJOUT |
| A Programming Paradigm for Spatiotemporal Composability | DOCUMENT | rôle | Papier décrivant la conception de Cordis, publié par le projet cordiverse et mis en lien de navigation principal sur la page de lancement de DeepSeek Harness, au même rang que le dépôt GitHub et la documentation développeur | AJOUT |
| tout est plugin | CONCEPT | définition | Principe d'architecture revendiqué par DeepSeek Harness : aucun cœur privilégié à patcher, toute capacité est un plugin monté à côté des autres et remplaçable depuis la configuration — y compris l'adaptateur de modèle, le registre d'outils, le journal de session et la boucle d'agent elle-même. Vérifiable en une commande : `dsh --profile web --dump-config` imprime l'arbre réellement démarré, dont toute ligne peut être remplacée par un patch | AJOUT |
| log de session append-only | CONCEPT | définition | Journal en ajout seul qui est la source du contexte vu par le modèle dans DeepSeek Harness — et non son compte rendu : l'historique modèle en est projeté par `deriveMessages()`, et fork, reprise, transcripts, télémétrie et persistance en dérivent tous. Invariant associé, asserté à l'exécution : tout ce qui atteint une requête modèle doit être reconstructible depuis le journal, de sorte qu'un nouvel input visible du modèle exige un nouvel événement de session. Un tour rejeté sans aucun step est lui-même journalisé, pour que la tentative reste visible. Format non stabilisé en préversion | AJOUT |
| couture de capacité | CONCEPT | définition | Traduction de *capability seam* : capacité substituable définie par trois rôles conçus ensemble — une Service Definition qui déclare l'interface, un Service Provider qui l'implémente, un Consumer qui l'utilise, le plus souvent un outil exposé au modèle. Un seul rôle ne fait pas une couture. C'est le mécanisme par lequel un remplacement de fournisseur change tout le produit, sans fork | AJOUT |
| mode Minimal | TECHNOLOGIE | définition | Mode d'exécution de DeepSeek Harness réduit à deux outils — un bash persistant et `str_replace_editor` — livré explicitement pour évaluer des modèles dans un environnement minimal. Enjeu de marché : reprendre la définition du harnais de mesure, alors que Claude Code s'est imposé en 2026 comme harnais d'évaluation de référence y compris chez les laboratoires concurrents. Aucun score publié au 13 août 2026 | AJOUT |
| mode Code | TECHNOLOGIE | définition | Mode d'exécution de DeepSeek Harness reprenant toutes les capacités du mode Standard, mais exposant les outils via le Code Mode SDK afin que le modèle combine des opérations multi-étapes dans un unique programme TypeScript plutôt qu'en tours d'appels d'outils successifs | AJOUT |
| pi-ai | TECHNOLOGIE | rôle | Bibliothèque tierce (`@earendil-works/pi-ai`) derrière l'adaptateur `dsh-llm-pi-ai`, second fournisseur LLM livré avec DeepSeek Harness aux côtés de l'adaptateur DeepSeek natif. Une instance détient un dictionnaire de profils par route ; une route absente du catalogue se déclare intégralement, de sorte qu'un gateway OpenAI-compatible ou un serveur auto-hébergé relève de la configuration et non du code. C'est la preuve vérifiable que le harnais n'est pas verrouillé sur les modèles DeepSeek | AJOUT |
| DeepSeek-V4-Pro | TECHNOLOGIE | rôle | Modèle de DeepSeek passé en disponibilité générale le 13 août 2026 (`DeepSeek-V4-Pro-0813`), le jour même de la publication du harnais : niveaux d'effort de raisonnement low, high et max, support natif du format OpenAI Responses API avec intégration optimisée pour Codex, disponible en application, en web (« Expert Mode ») et en API. Nouvelle grille tarifaire heures pleines / heures creuses au 16 août 2026 à 16:00 UTC | AJOUT |
| Safe Use Policy | DOCUMENT | définition | Politique d'usage liée en pied de page de la page produit de DeepSeek Harness, sensiblement plus directe que l'argumentaire : l'outil est décrit comme *locally-first* et capable d'exécuter du code sur la machine de l'utilisateur, les garde-fous des modèles de fondation contre l'injection de prompt sont qualifiés de basiques, et l'agent peut exécuter des commandes embarquées dans le contenu qu'il lit même lorsqu'elles contredisent la tâche assignée. Six précautions recommandées, dont la revue préalable de tout plugin, serveur MCP, Skill ou Hook installé — ce qui tempère l'invitation à composer librement | AJOUT |
| Claude Code | TECHNOLOGIE | rôle | Harnais concurrent implicite de DeepSeek Harness — jamais nommé sur la page — mais présent dans le dépôt du projet, qui embarque un `CLAUDE.md` (copie d'`AGENTS.md`) et un répertoire `.claude/skills` : l'outil dont DSH vise la place sert à le construire. Prolonge le constat de la fiche GLM-5.3, où Claude Code servait de harnais d'évaluation à un laboratoire chinois concurrent | MISE_A_JOUR |
| Harness | CONCEPT | rôle | Couche que DeepSeek résume par l'équation « Agent = Model + Harness » : le modèle est *« l'âme de l'agent »*, le harnais est ce qui lui permet de comprendre son environnement, d'utiliser des outils et de continuer à travailler en conditions réelles. DSH en propose une définition opérationnelle par composition de plugins et journal unique, plutôt que par catalogue de fonctionnalités | MISE_A_JOUR |
