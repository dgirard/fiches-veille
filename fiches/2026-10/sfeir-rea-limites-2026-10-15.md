---
themes: [qualite-securite, outils-plateformes, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-rea-limites-2026-10-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 octobre 2026** (mis à jour le 20 octobre, ~6 500 signes, quatre sources notées). Il recense les limites de **REA** (Reverse Engineer Anything), outil de rétro-ingénierie piloté par agent via **MCP**, d'après trois tests indépendants d'octobre 2026. Trois apports. **(A)** Le volume des sorties : sur une application **Electron** de 100 Mo, REA 6.4.0 a produit **59,2 Mo** de JSON en **52,2 s**, et un seul appel MCP de résumé a renvoyé **1,35 Mo** — *« un modèle de langage qui reçoit 1,35 Mo pour un "résumé" sature sa fenêtre de contexte »*. **(B)** Le poids du catalogue d'outils : **170 outils** et ~1,95 Mo de définitions en 6.4.0 ; en 6.7.0, **207 outils** et 3,16 Mo, que le **profil compact** ramène à **219 Ko** (division par plus de quatorze). **(C)** Une couverture partielle pas toujours signalée : **744 limitations** déclarées, mais deux scripts preload construits à l'exécution manqués sans avertissement. L'article fixe un critère d'usage : REA prend l'avantage quand la question traverse les couches (renderer Electron vers add-on natif). Il s'inscrit dans une série SFEIR sur la rétro-ingénierie par agents et l'outillage MCP.

## Titre Article

Les limites réelles de REA : taille des sorties, coût, couverture

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/rea-limites/

## Keywords

REA, Reverse Engineer Anything, rétro-ingénierie, agents de codage, MCP, catalogue d'outils, tools/list, profil compact, fenêtre de contexte, coût en tokens, Electron, app.asar, IPC, preload, contextBridge, analyse statique, couverture, Ghidra, IDA, Hopper, GhidraMCP, ida-pro-mcp, épinglage de version, AI Cyber, FinOps

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé individuellement, publié sur sfeir.com.

## Ton

Profil : note technique courte d'une ESN, registre factuel et métrologique, en français, public d'ingénieurs sécurité et d'équipes qui envisagent la rétro-ingénierie par agents. Le texte procède par **mesures datées et attribuées** : chaque chiffre est rattaché à un testeur nommé (Choudhary sur HackerNoon, Cañete Arroyo chez Jacar Systems, Turland chez Cyrus) et à une version précise de l'outil. La structure suit trois limites (taille, catalogue, couverture) puis un critère de choix et une FAQ. Le ton est prudent sur la périssabilité des chiffres : une **mise à jour du 20 octobre** corrige en place le constat sur le catalogue, et le texte rappelle que REA publie des versions presque chaque jour. Les recommandations sont formulées à l'impératif opérationnel (« activez-le par défaut », « mesurez vous-même », « un zéro dans un comptage se vérifie toujours à la main »). Clôture sur l'offre **AI Cyber** de SFEIR, présentée comme un cadrage par budget de tokens et version épinglée.

## Pense-betes

- **Sorties volumineuses** : PI-Desktop v0.16.1 (Electron, 100 Mo) → **421** fichiers JS, **3 114 427** nœuds d'AST, zéro échec de parsing, **59,2 Mo** de résultats en **52,2 s**. Un appel MCP de résumé : **60,5 s**, **1 350 868 octets** dont 672 Ko de texte.
- **Le volume croît avec la cible** : Hyper 3.4.1 (app.asar 14 Mo, 2 236 fichiers, 18 canaux IPC) → **253 Mo** de JSON de preuves ; Slack 4.52.171 → **158 Mo**. Ces fichiers sont une archive ; l'agent doit interroger REA par petites questions ciblées.
- **Catalogue d'outils (6.4.0)** : **170 outils MCP**, `tools/list` = **1 954 704 octets**, soit *« roughly half a million tokens »* avant toute action ; profil compact de l'époque : −9 % seulement. Un petit modèle local ne pouvait pas le charger.
- **Mise à jour 6.7.0 (18 octobre)** : **207 outils**, 6 prompts, 153 commandes CLI ; catalogue complet **3 158 352 octets**, profil compact **219 211 octets** (÷14). Recommandation : activer le profil compact par défaut et mesurer soi-même.
- **Coût d'installation** : **222 Mo** et **158 dépendances**.
- **Couverture** : **744 limitations explicites** (dont 365 liées au budget de résultat), mais **zéro preload annoncé** alors que deux étaient chargés via un helper à l'exécution, ce qui a faussé le comptage des API exposées. Les comptages simples concordaient avec grep. Plus d'indirections = moins de couverture.
- **Code natif** : sans Ghidra, Hopper ou IDA, `provider_unavailable` sur un binaire Rust de 20 Mo ; sur Linux arm64, compilation manuelle du décompilateur natif de Ghidra nécessaire.
- **Critère de choix** : simple décompilation avec IDA/Ghidra déjà en place → un pont mono-moteur suffit ; REA vaut son coût quand la question **traverse les couches**.
- **Rappel** : REA ne confine rien (pas un sandbox).

## RésuméDe400mots

L'article de SFEIR documente les limites de REA (Reverse Engineer Anything), un outil de rétro-ingénierie qu'un agent de codage pilote via le protocole MCP. Il s'appuie sur trois tests indépendants publiés en octobre 2026 : celui d'Ishank Choudhary sur HackerNoon (REA 6.4.0), celui de Javier Cañete Arroyo chez Jacar Systems (REA 6.7.0) et celui de Connor Turland chez Cyrus.

Le premier constat porte sur la taille des sorties. L'analyse statique de l'application Electron PI-Desktop, 100 Mo, a pris 52,2 secondes et produit 59,2 Mo de JSON, après avoir parcouru 421 fichiers JavaScript et plus de trois millions de nœuds d'arbre syntaxique sans échec de parsing. Un seul appel MCP de résumé a renvoyé 1,35 Mo, de quoi saturer la fenêtre de contexte d'un modèle avant sa deuxième question. Les volumes augmentent avec la cible : 253 Mo pour Hyper, 158 Mo pour Slack. L'article en conclut que ces fichiers servent d'archive de preuves et que l'agent doit interroger REA par questions ciblées.

Le deuxième constat concerne le catalogue d'outils exposé au modèle. En version 6.4.0, 170 outils MCP pesaient près de 2 Mo de définitions, environ un demi-million de tokens selon Choudhary, et le profil compact ne réduisait ce poids que de 9 %. Une mise à jour du 20 octobre corrige ce point : la version 6.7.0 expose 207 outils pour 3,16 Mo, mais son profil compact descend à 219 Ko, soit une division par plus de quatorze. SFEIR recommande de l'activer par défaut et de refaire la mesure, les chiffres dépendant d'une version précise d'un outil publié presque quotidiennement. L'installation pèse 222 Mo et 158 dépendances.

Le troisième constat touche la couverture. REA déclare beaucoup de ses angles morts (744 limitations explicites sur l'application de 100 Mo), mais en tait d'autres : il a annoncé zéro script preload alors que deux étaient construits à l'exécution par un helper, et a manqué un contrôle d'expéditeur sur une application jouet. Les comptages simples concordaient avec grep ; la couverture baisse avec les indirections. Pour le code natif, REA dépend d'un moteur installé (Ghidra, Hopper ou IDA) et ne fait sinon qu'identifier le format.

L'article donne enfin un critère : pour décompiler des binaires avec IDA ou Ghidra déjà en place, un pont vers un seul moteur ajoute moins de surface ; REA prend l'avantage quand l'analyse traverse les couches, du renderer Electron à un add-on natif. Une FAQ rappelle que la lenteur n'est pas le problème, que le catalogue complet exige un gros modèle et qu'un zéro dans un comptage se vérifie à la main.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Les limites réelles de REA | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Les limites réelles de REA | DOCUMENT | référence | Ishank Choudhary | PERSONNE | 0.93 | STATIQUE | déclaré_article |
| Les limites réelles de REA | DOCUMENT | référence | Jacar Systems | ORGANISATION | 0.92 | STATIQUE | déclaré_article |
| Ishank Choudhary | PERSONNE | mesure | 59,2 Mo de sortie en 52,2 s sur une app Electron de 100 Mo (REA 6.4.0) | MESURE | 0.93 | STATIQUE | déclaré_article |
| Ishank Choudhary | PERSONNE | mesure | catalogue de 170 outils MCP pesant 1 954 704 octets (~500 000 tokens) | MESURE | 0.92 | STATIQUE | déclaré_article |
| Javier Cañete Arroyo | PERSONNE | travaille_chez | Jacar Systems | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |
| profil compact | CONCEPT | réduit | poids du catalogue de 3 158 352 à 219 211 octets (REA 6.7.0) | MESURE | 0.92 | STATIQUE | déclaré_article |
| profil compact | CONCEPT | fait_partie_de | REA | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | Electron | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | concurrence | GhidraMCP | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la couverture de REA baisse avec les indirections et certains angles morts ne sont pas signalés | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | activer le profil compact par défaut et interroger REA par questions ciblées | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | REA vaut son coût quand l'analyse traverse les couches (renderer Electron vers add-on natif) | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| REA | TECHNOLOGIE | catégorie | Outil de rétro-ingénierie piloté par agent via MCP (Reverse Engineer Anything), paquet npm rea-agents | AJOUT |
| profil compact | CONCEPT | rôle | Mode réduit du catalogue d'outils MCP de REA (÷14 en 6.7.0) | AJOUT |
| Ishank Choudhary | PERSONNE | rôle | Auteur d'un test de REA 6.4.0 sur HackerNoon (14 octobre 2026) | AJOUT |
| Javier Cañete Arroyo | PERSONNE | rôle | Testeur de REA 6.7.0 (Jacar Systems, 19 octobre 2026) | AJOUT |
| Jacar Systems | ORGANISATION | secteur | Conseil / publication technique (jacar.es) | AJOUT |
| GhidraMCP | TECHNOLOGIE | catégorie | Pont MCP vers un moteur de décompilation unique (Ghidra) | AJOUT |
