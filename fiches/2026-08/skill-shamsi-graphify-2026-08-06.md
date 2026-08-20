---
fiche_type: skill
skill_source: github.com/Graphify-Labs/graphify
skill_author: Safi Shamsi
themes: [agents-codage-ia-skills, architecture-construction, outils-plateformes]
source: "GitHub (Safi Shamsi, Graphify-Labs/graphify)"
---
# skill-shamsi-graphify-2026-08-06

## Veille

Fiche de **Skill** : **graphify** de **Safi Shamsi** (Graphify Labs, Y Combinator S26) transforme un projet entier — code, docs, PDF, images, vidéos — en **graphe de connaissance interrogeable**, invocable par `/graphify` depuis Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot et une quinzaine d'autres clients. Observé le **6 août 2026** : **103 187 étoiles**, **10 024 forks**, dépôt créé le **3 avril 2026**. Apache-2.0, Python 3.10+, branche par défaut **v8**. **Trois partis pris de conception**, énoncés dans le README. *« Code maps for free, fully local »* : le code est parsé en **AST tree-sitter**, de façon déterministe et sans LLM, rien ne quittant la machine. *« Every edge is explained »* : chaque arête est étiquetée **`EXTRACTED`** (explicite dans la source) ou **`INFERRED`** (résolue par graphify), une troisième valeur `AMBIGUOUS` apparaissant dans le rapport. *« Not a vector index »* : *« no embeddings, no vector store: a real graph you traverse »*. **Trois sorties** : `graph.html` (graphe interactif), `GRAPH_REPORT.md` (god nodes, connexions surprenantes, questions suggérées) et `graph.json` (graphe persistant, interrogeable des semaines plus tard sans relire les fichiers). **Trois modes d'interrogation** en remplacement du grep : `query` (sous-graphe pour une question en langue naturelle), `path A B` (plus court chemin entre deux entités) et `explain` (voisinage d'un concept). **Couverture** : 36 grammaires tree-sitter (~40 langages), plus Terraform, Apex, configurations MCP, manifestes de paquets, Office, Google Workspace, PDF, images, et vidéo/audio transcrits localement par faster-whisper. Communautés détectées par **Leiden**, labellisées sans LLM. **Benchmarks** : sur LOCOMO, recall@10 de **0,497** contre 0,149 pour supermemory et 0,048 pour mem0, mais exactitude QA inférieure (45,3 % contre 49,7 %) ; sur LongMemEval-S, **76 %**, à égalité avec un RAG dense ; et *« Graph build — LLM credits: 0 »*. **Points à consigner** : la branche `main` porte un README de l'ère v1 décrivant un produit différent (skill Claude Code uniquement, argument « 71,5× moins de tokens ») ; le paquet PyPI s'appelle **`graphifyy`** avec deux *y*, le temps que le nom `graphify` soit récupéré ; et un **journal de requêtes** est écrit par défaut dans `~/.cache/graphify-queries.log`, désactivable par variable d'environnement.

## Titre Article

graphify — « Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store. »

## Date

2026-08-06

## URL

https://github.com/Graphify-Labs/graphify

## Keywords

skill, graphe de connaissance, knowledge graph, AST, tree-sitter, analyse statique déterministe, extraction locale, sans LLM, NetworkX, Leiden, détection de communautés, god node, connexions surprenantes, EXTRACTED, INFERRED, AMBIGUOUS, provenance d'arête, confiance, pas de vecteurs, no embeddings, no vector store, traversée de graphe, query, path, explain, graph.json, graph.html, GRAPH_REPORT, cache SHA256, mise à jour incrémentale, watch, hook post-commit, wiki crawlable par agent, MCP stdio, Neo4j, GraphML, Obsidian, multimodal, PDF, vision, faster-whisper, transcription locale, Terraform, Apex, configurations MCP, manifestes de paquets, Google Workspace, LOCOMO, LongMemEval, recall, mem0, supermemory, RAG dense, zéro crédit LLM, résidence des données, Ollama, Bedrock, journal de requêtes, télémétrie, Y Combinator, Graphify Labs, Safi Shamsi

## Authors

**Safi Shamsi** — créateur et mainteneur de graphify, et de **Graphify Labs**, société passée par **Y Combinator (promotion S26)** selon le badge du dépôt. Il maintient aussi le site d'annuaire `graphify.net` (cf. [[graphify-net-annuaire-ia-coding-2026-08-06]]) et publie un livre, *The Memory Layer*, sur les idées et l'architecture derrière le projet.

**Trace d'historique à connaître** : le dépôt s'appelait `safishamsi/graphify` avant son transfert vers l'organisation `Graphify-Labs`. Le README de la branche `main` porte encore l'ancien chemin dans son badge d'intégration continue et dans sa procédure d'installation manuelle.

**Signaux d'adoption au 6 août 2026** : 103 187 étoiles, 10 024 forks, 823 issues ouvertes, dernier push la veille. Le dépôt affiche un badge Trendshift et propose son README en **33 langues**. Communauté sur Discord, page LinkedIn d'entreprise.

## Ton

**Profil** : documentation de projet open source à forte densité, écrite pour être lue par un développeur pressé **et** par un agent. Registre technique, très peu de promesses, beaucoup de tableaux — types de fichiers, grammaires, variables d'environnement, référence complète des commandes.

**Style** : **la démonstration précède l'argument**. Le README montre une sortie réelle avant d'expliquer quoi que ce soit — une commande `graphify explain "APIRouter"` avec son voisinage annoté ligne par ligne, puis un `graphify path "FastAPI" "ModelField"` qui affiche le chemin en trois sauts. On voit le produit fonctionner sur un dépôt que le lecteur connaît (FastAPI) avant d'entendre un seul argument commercial.

**Trois traits notables** :

1. **La position se définit par une négation assumée.** *« Not a vector index. No embeddings, no vector store: a real graph you traverse. »* Le projet se situe **contre** le RAG vectoriel devenu standard, et cette opposition structure tout le reste — le déterminisme, le coût nul, la traçabilité des arêtes.
2. **L'honnêteté sur ses propres benchmarks.** Le tableau publie une **défaite** : 45,3 % d'exactitude QA sur LOCOMO contre 49,7 % pour supermemory. Peu de projets publient la colonne où ils perdent.
3. **La frontière vie privée posée par type de fichier, pas par principe.** Le code reste local, la vidéo aussi (transcription par faster-whisper), les documents et images partent vers le modèle. La section *Privacy* énumère les cas plutôt que de promettre le local.

**Registre opérationnel imposé à l'agent** (le « ton » au sens des fiches de skill) : l'outil ne dicte rien à l'agent, il lui **fournit un substrat**. Le README consacre une section entière à *« Make your assistant always use the graph »* — l'objectif est que l'agent consulte le graphe **avant** de lire les fichiers.

**Formules-marqueurs** : *« query instead of grepping »*, *« Code maps for free, fully local »*, *« Every edge is explained »*, *« you always know what was found vs guessed »*, *« a real graph you traverse »*, *« Graph build — LLM credits: 0 »*.

## Pense-betes

- **Nature** : skill `/graphify` + CLI Python, Apache-2.0, distribuée en PyPI sous le nom **`graphifyy`** (deux *y*, le temps de récupérer `graphify`). `uv tool install graphifyy && graphify install`. Fonctionne dans Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot et une quinzaine d'autres clients.
- **Cadrage clé** : le graphe remplace le grep — on demande une relation, pas une occurrence de chaîne.

### Les trois partis pris, et pourquoi ils se tiennent

1. **Le code est parsé localement, sans LLM** — AST tree-sitter, déterministe, *« nothing leaves your machine »*. Un corpus purement code ne demande aucune clé d'API et tourne hors ligne ; documents, PDF et images passent en revanche par un modèle.
2. **Chaque arête porte sa provenance** — `EXTRACTED` (explicite dans la source), `INFERRED` (résolue par graphify), `AMBIGUOUS` dans le rapport : *« You always know what was found vs guessed. »*
3. **Pas d'index vectoriel** — ni embeddings ni magasin de vecteurs, un graphe qu'on traverse.

Les trois se renforcent : le déterminisme rend le coût nul, le coût nul rend la reconstruction fréquente possible, et l'étiquetage des arêtes rend le résultat auditable.

### Les benchmarks, lus correctement

| Benchmark | Métrique | graphify | Champ |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0,497** | supermemory 0,149 · mem0 0,048 |
| LOCOMO (n=300) | exactitude QA | 45,3 % | **supermemory 49,7 %** · mem0 27,3 % |
| LongMemEval-S (n=50) | exactitude QA | 76 % | **à égalité** avec un RAG dense |
| Construction du graphe | crédits LLM | **0** | facturé au token ailleurs |

graphify domine largement le rappel, **perd en exactitude QA**, égale le RAG dense sur le second benchmark, et construit son graphe gratuitement. Le différenciateur défendable est donc le **coût et la traçabilité**, non la qualité de réponse : présenter graphify comme « meilleur que le RAG » serait démenti par ses propres chiffres. Protocole crédité : même harnais, même modèle, mêmes budgets, juge validé en aveugle contre un second juge (90,6 % d'accord, kappa de Cohen 0,81).

À rapprocher du seul chiffre comparable du corpus : Compare the Market mesurait un graphe AST à ~70 % contre ~58 % pour un RAG vectoriel sur 79 merge requests, le RAG faisant pire que pas de contexte du tout — voir [[comparethemarket-context-retrieval-ai-code-review-gkg-rag-2026-03-06]]. Deux mesures indépendantes convergent sur la supériorité du graphe structuré pour le code.

### Interrogation et couverture

`query "<question>"` rend un sous-graphe pour une question en langue naturelle, `path A B` trace le chemin entre deux entités, `explain X` déplie le voisinage d'un concept. L'exemple du README : `path "FastAPI" "ModelField"` rend un chemin en trois sauts avec le type de chaque arête. Même bénéfice que celui attribué à GitNexus dans [[lassiege-usine-logicielle-heure-ia-2026-07-28]].

Couverture plus large que « du code » : 36 grammaires tree-sitter (~40 langages, jusqu'à CUDA, Metal, Zig, Elixir, Julia, Dart, SystemVerilog, Fortran), plus SQL, Terraform/HCL, Apex Salesforce, les **configurations MCP** (`.mcp.json`, `claude_desktop_config.json` — serveurs, paquets et variables d'environnement requises), les manifestes de paquets (`pyproject.toml`, `go.mod`, `pom.xml`, un nœud canonique par paquet), Office, Google Workspace, PDF, images, vidéo et audio. Graphifier ses propres configurations MCP est un usage inattendu et immédiatement utile pour cartographier sa surface d'outillage.

### Le « pourquoi » comme objet de première classe

Les commentaires `# NOTE:`, `# WHY:`, `# HACK:`, les docstrings et le raisonnement de conception présent dans la documentation deviennent des **nœuds séparés reliés au code qu'ils expliquent**. L'intention est traitée comme une entité du graphe : on peut demander *pourquoi*, non seulement *quoi*.

### Fraîcheur et sorties

Trois mécanismes de fraîcheur : cache SHA256 (seuls les fichiers changés sont retraités), `--watch` (reconstruction instantanée sur sauvegarde, **AST seul, sans LLM** ; documents et images notifient qu'un `--update` est nécessaire), et `graphify hook install` (hook post-commit, sans processus d'arrière-plan). Le mode `--watch` est justifié pour les flux multi-agents : *« the graph stays current between waves automatically »*.

Sorties pour agents : `--wiki` produit des articles par communauté avec un `index.md` — *« point any agent at index.md and it can navigate the knowledge base by reading files instead of parsing JSON »* — et `--mcp` démarre un serveur MCP stdio. Exports Obsidian, GraphML, Neo4j (cypher), SVG.

### Vie privée, frontière fine

| Traitement | Où |
|---|---|
| Code (tree-sitter), vidéo et audio (faster-whisper) | **local** ; `--code-only` force ce mode sur un dépôt mixte |
| Documents, PDF, images | **envoyés au modèle** ; chaîne de priorité automatique Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama |

**Kimi route vers des serveurs Moonshot AI en Chine** — le README le signale, et `--backend ollama` donne le mode entièrement local. Pas de télémétrie ni de suivi d'usage, mais un **journal de requêtes écrit par défaut** dans `~/.cache/graphify-queries.log` (horodatage, question, corpus, nœuds rendus, durée ; les sous-graphes ne sont pas stockés). Désactivation par `GRAPHIFY_QUERY_LOG_DISABLE=1`. Local, mais actif sans opt-in : à connaître avant un déploiement en contexte sensible.

### Deux pièges documentaires du dépôt

1. **La branche `main` est périmée** : elle porte un README de l'ère v1 (7 Ko) décrivant *« a Claude Code skill »* mono-client, met en avant l'argument « 71,5× moins de tokens » sur un corpus de 52 fichiers, et pointe encore `safishamsi/graphify`. La branche par défaut est **v8** (57 Ko). Lire v8, jamais `main`.
2. **Le nom du paquet** : `pip install graphifyy` avec deux *y* ; la CLI et la commande de skill restent `graphify`.

### Modèle économique et traction

La skill open source est la porte d'entrée d'une plateforme commerciale sur `graphify.com` — *« the always-on layer… applies the same graph approach to your entire working context: meetings, files, docs, and code, updating continuously in the background »*, en liste d'attente. Open source local d'un côté, service continu hébergé de l'autre.

**103 187 étoiles en quatre mois** est un rythme exceptionnel, mais le chiffre ne dit rien de l'usage réel, et le site officiel du projet en affiche encore 3 700 — signe que la communication n'a pas suivi. Citer l'étoile comme signal d'attention, jamais comme mesure d'adoption.

**Désambiguïsation** : le site `graphify.net` est une propriété distincte de `graphify.com`, la plateforme commerciale.

## RésuméDe400mots

**graphify** (Safi Shamsi, Graphify Labs, Y Combinator S26) transforme un projet entier en **graphe de connaissance interrogeable**, invocable par `/graphify` depuis Claude Code, Cursor, Codex, Gemini CLI et une quinzaine d'autres clients. Observé le 6 août 2026 : **103 187 étoiles** pour un dépôt créé le 3 avril, Apache-2.0, Python.

**Trois partis pris fondent le projet.** Le **code est parsé localement** en AST tree-sitter, sans LLM : déterministe, rien ne quitte la machine, aucune clé d'API requise pour un corpus purement code. **Chaque arête porte sa provenance** — `EXTRACTED` si elle est explicite dans la source, `INFERRED` si graphify l'a résolue —, *« so you can tell what was read directly from what was inferred »*. Et le projet se définit **contre le RAG vectoriel** : *« Not a vector index. No embeddings, no vector store: a real graph you traverse. »*

**L'usage remplace le grep.** `query` rend un sous-graphe pour une question en langue naturelle, `path A B` trace le chemin entre deux entités, `explain` déplie un concept. Trois sorties : un graphe interactif, un rapport lisible (god nodes, connexions surprenantes, questions suggérées) et un `graph.json` persistant, interrogeable des semaines plus tard.

**La couverture dépasse le code** : 36 grammaires tree-sitter, mais aussi SQL, Terraform, Apex, les **configurations MCP**, les manifestes de paquets, Office, PDF, images, et la vidéo transcrite localement. Les commentaires `# WHY:` et le raisonnement de conception deviennent des **nœuds à part entière reliés au code qu'ils expliquent**.

**Les benchmarks méritent une lecture précise.** Sur LOCOMO, graphify domine le rappel (0,497 contre 0,149 et 0,048) mais **perd en exactitude QA** (45,3 % contre 49,7 %) ; sur LongMemEval-S il **égale un RAG dense** à 76 %. La ligne qui compte est ailleurs : *« Graph build — LLM credits: 0 »*. Le différenciateur défendable est **le coût et la traçabilité, pas la qualité de réponse**.

**Trois précautions.** La branche `main` porte un README périmé de l'ère v1 décrivant un autre produit : lire `v8`. Le paquet PyPI s'appelle `graphifyy`, le temps de récupérer le nom. Et un **journal de requêtes local** est actif par défaut, désactivable par variable d'environnement.

La skill sert par ailleurs de porte d'entrée à une plateforme commerciale en liste d'attente sur graphify.com, qui applique la même approche en continu à l'ensemble du contexte de travail.

## Commentaire

**En une phrase** : graphify parie que, pour du code, **un graphe déterministe construit gratuitement bat un index vectoriel payant** — et publie les chiffres qui le nuancent.

**L'idée centrale** tient dans une asymétrie que le projet exploite bien. Le code a une structure formelle : un analyseur syntaxique sait dire, sans deviner, que telle fonction en appelle telle autre. Le RAG vectoriel jette cette information pour la remplacer par une proximité statistique, et paie des tokens pour le faire. graphify garde la structure là où elle existe (le code, en AST local) et ne convoque un modèle que là où elle manque (la prose, les images). D'où les trois propriétés qui découlent l'une de l'autre : le déterminisme rend l'extraction gratuite, la gratuité rend la reconstruction fréquente possible, et la reconstruction fréquente rend le graphe fiable au lieu de périmé.

**Le second principe est la traçabilité.** Étiqueter chaque arête `EXTRACTED` ou `INFERRED` paraît mineur et change tout : on peut faire confiance différemment à deux relations selon leur origine, et un agent qui traverse le graphe sait quand il marche sur du solide. C'est la même discipline épistémique que les types de source dans une fiche de veille, ou que la distinction entre lecture et substitution dans [[skill-gibbs-hyperresearch-2026-08-03]].

**En résumé** : l'outil est utile, ses chiffres sont honnêtes, et son argument le plus fort est économique avant d'être qualitatif. Sa faiblesse tient à sa documentation — un dépôt dont la branche `main` décrit un produit périmé et dont le site officiel affiche 3 700 étoiles quand GitHub en compte 103 000 n'inspire pas confiance sur sa capacité à tenir sa propre cartographie à jour.

## Lecture commentée du SKILL.md

Le fichier commenté est le README de la branche `v8` (57 Ko), qui fait office de spécification publique de la skill, et le `skills/graphify/skill.md` qu'installe la commande `graphify install`.

**L'énoncé de mission, en une phrase, place le verbe au bon endroit** :

> *« Type `/graphify` in your AI coding assistant and it maps your entire project (code, docs, PDFs, images, videos) into a **knowledge graph** you can **query instead of grepping** through files. »*

*Glose* : la promesse n'est pas « comprendre votre code » mais **remplacer une opération précise** — le grep. Une skill qui se définit par le geste qu'elle supprime est plus facile à évaluer qu'une skill qui promet de la compréhension.

**Les trois puces qui suivent sont la spécification réelle** :

> *« **Code maps for free, fully local.** Code is parsed with tree-sitter AST: deterministic, no LLM, nothing leaves your machine. (Docs, PDFs, images and video use your assistant's model, or a configured API key, for a semantic pass.) »*

*Glose* : la parenthèse fait le travail honnête. Elle dit exactement où finit le local. Beaucoup d'outils annoncent « fully local » et laissent le lecteur découvrir l'exception.

> *« **Every edge is explained.** Each connection is tagged `EXTRACTED` (explicit in the source) or `INFERRED` (resolved by graphify), so you can tell what was read directly from what was inferred. »*

*Glose* : la définition des deux étiquettes est donnée **dans la même phrase** que leur nom. Un agent qui lit cette ligne sait comment pondérer une arête sans consulter d'autre documentation.

> *« **Not a vector index.** No embeddings, no vector store: a real graph you traverse. »*

*Glose* : positionnement par la négation, assumé. Le projet se situe dans un paysage où le RAG vectoriel est le défaut, et refuse d'y entrer.

**La sortie montrée avant d'être décrite** — choix de rédaction remarquable :

```text
$ graphify path "FastAPI" "ModelField"
Shortest path (3 hops):
  FastAPI --uses--> DefaultPlaceholder <--references-- get_request_handler() --references--> ModelField
```

*Glose* : trois sauts, le sens de chaque arête, son type. Le lecteur comprend en une ligne ce que « traverser un graphe » veut dire, sur un dépôt qu'il connaît. C'est plus efficace que n'importe quel paragraphe d'explication.

**La section qui trahit l'intention profonde** s'intitule *« Make your assistant always use the graph »*.

*Glose* : l'objectif n'est pas qu'un humain lance une commande, c'est que **l'agent consulte le graphe avant de lire les fichiers**. La skill vise à s'insérer dans la boucle par défaut de l'assistant, pas à rester un outil invoqué à la demande. C'est le même mouvement que la rule de routage vers les skills chez Hugo Lassiège : rendre le bon réflexe automatique.

**Choix de design à retenir** : l'**extraction hybride par type de fichier** (déterministe où la structure existe, sémantique ailleurs) est la décision qui produit toutes les autres propriétés ; le **cache SHA256** et le **hook post-commit** traitent la fraîcheur comme un problème d'ingénierie et non de discipline ; et la **sortie en wiki markdown** reconnaît qu'un agent lit mieux des fichiers qu'il ne parse du JSON.

## Déclencheur

**Quand la skill s'active** : sur `/graphify <chemin>` dans un assistant de codage, après `uv tool install graphifyy && graphify install`. En dehors d'un assistant, la CLI `graphify extract` fait le même travail en mode headless, avec une clé d'API pour la partie sémantique.

**Entrées attendues** : un **répertoire quelconque** — dépôt de code, dossier de notes, corpus de PDF, mélange des trois. Aucune structure préalable n'est requise.

**Options qui changent le comportement** : `--code-only` (n'indexe que le code, donc aucun appel réseau), `--update` (ne retraite que les fichiers modifiés), `--watch` (reconstruction continue), `--wiki` (sortie navigable par un agent), `--mcp` (serveur MCP stdio), `--backend ollama` (tout en local, y compris la partie sémantique).

**Quand ne pas la déclencher** : sur un corpus de quelques fichiers qui tient déjà dans une fenêtre de contexte — le README le dit lui-même à propos de son exemple à 6 fichiers, *« graph value there is structural clarity, not compression »*. Et sur un corpus dont les documents sont confidentiels sans backend local configuré, puisque la passe sémantique les enverrait à un modèle distant.

## Fonctionnement

**Le pipeline se lit en quatre temps.**

1. **Extraction, par type de fichier.** Le code passe par tree-sitter : AST, graphe d'appels, docstrings, le tout déterministe et local. La prose, les PDF et les images passent par un modèle. La vidéo et l'audio sont transcrits localement par faster-whisper, puis traités comme de la prose. Les commentaires d'intention (`# WHY:`, `# HACK:`) sont extraits comme nœuds distincts.
2. **Résolution et fusion.** Les nœuds et arêtes sont fusionnés dans un graphe NetworkX. Les liens inter-fichiers (`calls`, `imports`, `inherits`, `mixes_in`) sont résolus à travers ~40 langages. Un paquet référencé depuis plusieurs manifestes devient **un seul nœud canonique**, donc un hub.
3. **Structuration.** L'algorithme **Leiden** découpe le graphe en communautés, **labellisées sans LLM**. Les nœuds de plus fort degré sont désignés *god nodes*. Les connexions inattendues sont classées par un score composite, une arête code-article pesant plus qu'une arête code-code.
4. **Restitution.** Trois artefacts, plus les exports optionnels. Chaque arête conserve son étiquette de provenance jusqu'à la sortie.

**La boucle de fraîcheur** est traitée à trois niveaux de coût croissant : le cache SHA256 évite tout retraitement inutile ; `--watch` reconstruit instantanément sur sauvegarde d'un fichier de code, **sans appel LLM** ; le hook post-commit reconstruit à chaque commit sans processus résident.

**L'interrogation** se fait ensuite contre `graph.json`, sans relire les fichiers sources : `query` pour une question ouverte, `path` pour une relation entre deux entités, `explain` pour un voisinage.

## Artefacts

**Sorties principales**, dans `graphify-out/` :
- `graph.html` — graphe interactif, nœuds cliquables, filtres par communauté, recherche
- `GRAPH_REPORT.md` — god nodes, connexions surprenantes avec leur justification en clair, 4-5 questions suggérées, étiquettes de confiance
- `graph.json` — le graphe complet, persistant et interrogeable

**Sorties optionnelles** : `wiki/` (articles par communauté avec `index.md`, pour navigation par un agent), `obsidian/` (coffre Obsidian), `graph.svg`, `graph.graphml` (Gephi, yEd), `cypher.txt` (Neo4j), serveur MCP stdio, `converted/` (passerelles markdown pour Google Workspace).

**Sous-produits** : `cache/` (empreintes SHA256 par fichier) et `~/.cache/graphify-queries.log` (journal des requêtes, actif par défaut).

## Anti-patterns

- **Lire la branche `main`.** Elle décrit un produit de l'ère v1, mono-client, avec un argument marketing (« 71,5× moins de tokens ») que la version courante n'utilise plus. La branche par défaut est `v8`.
- **Citer « graphify bat le RAG ».** Ses propres benchmarks le contredisent : il perd en exactitude QA sur LOCOMO et **égale** un RAG dense sur LongMemEval-S. L'argument défendable est le coût nul et la traçabilité.
- **Annoncer « fully local » sans nuance.** Seul le code et la transcription vidéo le sont. Documents, PDF et images partent vers un modèle, sauf backend Ollama explicite.
- **Déployer en contexte sensible sans couper le journal de requêtes.** `~/.cache/graphify-queries.log` enregistre chaque question par défaut ; poser `GRAPHIFY_QUERY_LOG_DISABLE=1`.
- **Laisser la chaîne de priorité choisir le backend** dans un contexte à contrainte de résidence des données : la détection automatique peut router vers Kimi, donc vers des serveurs en Chine. Passer un `--backend` explicite.
- **Graphifier un corpus minuscule** en attendant un gain de tokens : en dessous de la taille d'une fenêtre de contexte, l'apport est structurel, pas économique.
- **Traiter 103 000 étoiles comme une mesure d'adoption.** C'est un signal d'attention sur quatre mois, rien de plus.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Safi Shamsi | PERSONNE | a_créé | graphify | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Graphify Labs | ORGANISATION | publie | graphify | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| graphify | METHODOLOGIE | permet | d'interroger un projet par traversée de graphe au lieu de grepper des fichiers | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| graphify | METHODOLOGIE | utilise | tree-sitter | TECHNOLOGIE | 0.97 | ATEMPOREL | déclaré_article |
| graphify | METHODOLOGIE | utilise | NetworkX | TECHNOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| graphify | METHODOLOGIE | utilise | algorithme de Leiden | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| analyse AST locale | CONCEPT | permet | une extraction de code déterministe, sans appel de modèle et sans sortie de données | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| graphify | METHODOLOGIE | s_oppose_à | l'index vectoriel, refusant embeddings et magasin de vecteurs | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| étiquetage EXTRACTED et INFERRED | CONCEPT | permet | de distinguer une relation lue dans la source d'une relation déduite | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| graphify | METHODOLOGIE | mesure | un recall@10 de 0,497 sur LOCOMO contre 0,149 pour supermemory et 0,048 pour mem0 | MESURE | 0.93 | STATIQUE | déclaré_article |
| graphify | METHODOLOGIE | mesure | une exactitude QA de 45,3 % sur LOCOMO, inférieure aux 49,7 % de supermemory | MESURE | 0.93 | STATIQUE | déclaré_article |
| graphify | METHODOLOGIE | mesure | 76 % d'exactitude sur LongMemEval-S, à égalité avec un RAG dense | MESURE | 0.92 | STATIQUE | déclaré_article |
| construction du graphe par AST | CONCEPT | réduit | le coût de construction à zéro crédit de modèle | MESURE | 0.95 | ATEMPOREL | déclaré_article |
| graphe de code structuré | CONCEPT | surpasse | la récupération vectorielle pour la compréhension de code | AFFIRMATION | 0.85 | ATEMPOREL | inféré |
| graphify | METHODOLOGIE | s_applique_à | code, documents, PDF, images, vidéo, configurations MCP et manifestes de paquets | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| commentaires d'intention | CONCEPT | fait_partie_de | le graphe, comme nœuds distincts reliés au code qu'ils expliquent | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| cache par empreinte et hook post-commit | CONCEPT | résout | la péremption du graphe face à un code qui change | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| sortie en wiki markdown | CONCEPT | permet | à un agent de naviguer la base de connaissance en lisant des fichiers plutôt qu'en analysant du JSON | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| graphify | METHODOLOGIE | utilise | faster-whisper pour transcrire vidéo et audio localement | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| journal de requêtes local | CONCEPT | s_oppose_à | l'absence totale de trace, étant actif par défaut et désactivable par variable d'environnement | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| détection automatique de backend | CONCEPT | s_oppose_à | une contrainte de résidence des données, pouvant router vers des serveurs situés en Chine | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| graphify | METHODOLOGIE | converge_avec | GitNexus | TECHNOLOGIE | 0.85 | DYNAMIQUE | inféré |
| Graphify Labs | ORGANISATION | publie | une plateforme commerciale appliquant la même approche en continu à tout le contexte de travail | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| branche main du dépôt | DOCUMENT | s_oppose_à | la branche v8, en décrivant un produit de génération antérieure | AFFIRMATION | 0.92 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| graphify | METHODOLOGIE | définition | Skill et CLI transformant un projet multi-format en graphe de connaissance interrogeable : code parsé localement en AST tree-sitter sans modèle, prose et images traitées sémantiquement, chaque arête étiquetée selon sa provenance, sans index vectoriel | AJOUT |
| graphify | METHODOLOGIE | adoption | Apache-2.0, paquet PyPI `graphifyy` ; dépôt créé le 3 avril 2026, 103 187 étoiles et 10 024 forks au 6 août 2026 ; branche par défaut v8, README en 33 langues | AJOUT |
| Safi Shamsi | PERSONNE | rôle | Créateur et mainteneur de graphify et de Graphify Labs (Y Combinator S26) ; maintient aussi le site d'annuaire graphify.net et publie le livre The Memory Layer | AJOUT |
| Graphify Labs | ORGANISATION | rôle | Société éditrice de graphify, passée par Y Combinator promotion S26 ; construit une plateforme commerciale continue au-dessus de la skill open source | AJOUT |
| provenance d'arête | CONCEPT | définition | Étiquetage de chaque relation d'un graphe selon son origine — explicite dans la source, déduite par résolution, ou ambiguë — de sorte qu'un lecteur ou un agent sait ce qui a été lu et ce qui a été supposé | AJOUT |
| extraction hybride par type de fichier | CONCEPT | définition | Principe consistant à extraire de façon déterministe là où la source porte une structure formelle (code, en AST) et à ne convoquer un modèle que là où elle n'en porte pas (prose, images) | AJOUT |
| tree-sitter | TECHNOLOGIE | rôle | Analyseur syntaxique incrémental fournissant l'AST de ~40 langages ; socle de l'extraction déterministe et locale de graphify | AJOUT |
| algorithme de Leiden | CONCEPT | rôle | Détection de communautés appliquée au graphe de code pour en dégager des sous-systèmes, avec labellisation sans modèle | AJOUT |
| LOCOMO | DOCUMENT | référence | Benchmark de mémoire à long terme (n=300) sur lequel graphify obtient 0,497 de recall@10 et 45,3 % d'exactitude QA | AJOUT |
| LongMemEval | DOCUMENT | référence | Benchmark de mémoire longue (variante S, n=50) sur lequel graphify obtient 76 %, à égalité avec un RAG dense | AJOUT |
