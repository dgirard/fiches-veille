---
themes: [outils-plateformes, qualite-securite, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-rea-trois-schemas-architecture-usage-2026-10-12

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **12 octobre 2026** (mis à jour le 23 octobre, ~20 000 signes, trois schémas, huit sources). Il présente **REA** (*Reverse Engineer Anything*), serveur **MCP** et CLI sous licence **MIT** qui donnent à un agent de code les outils d'un rétro-ingénieur ; dépôt `morluto/rea` créé le 14 avril 2026, **369 860 étoiles** au 23 octobre, paquet npm `rea-agents` en **6.7.0**. Trois schémas. **(1) Installation** : `npx rea-agents setup` (d'abord en `--dry-run`) enregistre le serveur MCP et une skill auprès de l'agent existant ; JavaScript, Electron et .NET sont analysés sans moteur, le natif exige **Ghidra**, IDA ou Hopper. La cible reste locale, mais *« its model provider has its own data policy »*. **(2) Fonctionnement** : REA identifie le format puis oriente vers l'analyse statique, un pont natif, un outil externe ou une capture à l'exécution, et rend des **preuves** assorties de limitations ; il *« is not a sandbox »*. **(3) Usage** : boucle question étroite et prédiction écrite → enquête → lecture vu/inféré/inconnu → vérification, débouchant sur un correctif prouvé par test ou une réimplémentation derrière une barrière **clean-room**. Volet d'une série SFEIR sur REA, avec [[sfeir-rea-limites-2026-10-15]].

## Titre Article

REA en trois schémas : architecture, fonctionnement et usage

## Date

2026-10-12

## URL

https://www.sfeir.com/articles/rea-fonctionnement-installation-usage/

## Keywords

REA, Reverse Engineer Anything, rétro-ingénierie, serveur MCP, CLI, rea-agents, skill, Claude Code, Codex, Cursor, Ghidra, IDA, Hopper, JADX, Binwalk, Electron, .NET, analyse statique, capture à l'exécution, preuves, limitations, sandbox, clean-room, décompilation, CJUE 2021, politique de données, modèle local

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, publiée sur sfeir.com (site éditorial de l'ESN).

## Ton

**Profil** : article pédagogique destiné aux développeurs et responsables d'équipe qui envisagent d'outiller leurs agents pour la rétro-ingénierie. Français technique, commandes et chemins de configuration cités tels quels, trois schémas commentés en légende.

**Style** : construction par schémas numérotés — où l'on installe, ce qui se passe à l'appel, comment s'en servir — chacun suivi d'un paragraphe qui en tire la consigne. Les citations de la documentation du projet restent en anglais (*« results include the evidence and limitations behind each conclusion »*, *« A separate account or container must enforce those restrictions »*). Une FAQ de quatre questions clôt le texte (compatibilité, licence, envoi dans le cloud, point de départ).

**Position épistémique** : sources primaires du dépôt (README, guide d'installation, politique de sécurité, disclaimer) croisées avec trois tests publics d'octobre 2026 (HackerNoon, Analytics Vidhya, Jacar Systems). La partie juridique (décompilation admise par la Cour de justice en 2021, protections au-delà du droit d'auteur) est présentée comme « points d'attention, pas un conseil juridique ». L'article renvoie à d'autres volets de la série (sandbox, limites, lecture d'une sortie, clean-room) et se termine sur l'offre AI Cyber du cabinet.

## Pense-betes

- **Ce qu'est REA** : serveur MCP + CLI, licence MIT, local ; *« One MCP for reverse engineering across binaries, applications, and runtime behavior »*. Ni décompilateur ni service en ligne : il pilote des outils existants.
- **Chiffres du dépôt** : créé le 14/04/2026 ; **76 998** étoiles le 11/10, **369 860** le 23/10 ; `rea-agents` **6.7.0** (18/10) ; catalogue de **207 outils**.
- **Installation** : `npx rea-agents setup` déclare REA auprès de l'agent existant (Claude Code, Codex, Cursor, tout client MCP local) + installe une skill. Pour Claude Code : `~/.claude.json` et `~/.claude/skills` → **tous les projets**.
- **Trois réflexes** : `--dry-run` d'abord (plan en lecture seule, sauvegarde de la config) ; profil séparé via `CLAUDE_CONFIG_DIR` ; version épinglée dans l'enregistrement MCP.
- **Moteurs** : JS, Electron, .NET sans moteur ; natif = Ghidra (gratuit), IDA ou Hopper (licences à acquérir) ; Android = JADX + JDK ; firmware = Binwalk/Unblob sous Linux ; web = navigateur Chrome. Sans moteur natif : `provider_unavailable` (binaire Rust, test HackerNoon).
- **Frontière des données** : le binaire ne part pas, ce que l'agent en extrait si → décision de conformité ; modèle local pour un code sensible.
- **Quatre traitements** : statique intégré (aucune exécution), pont natif authentifié par jeton de session, outils externes, **capture à l'exécution** qui lance la cible *« using your user permissions »* → zone de risque.
- **Sortie en preuves** : constat, localisation, limitations, inconnues ; **744 limitations explicites** sur une app Electron de 100 Mo ; *« this is not evidence that the feature is absent »*.
- **Méthode en 4 étapes** : question étroite + prédiction écrite → enquête → lire vu / inféré / inconnu → vérifier (grep, tests, héritage, source). Cas Analytics Vidhya (sélecteur rapide d'Obsidian) : **7 minutes**, **1,83 $**, formule confrontée à 24 classements relevés à la main.
- **Deux sorties** : déboguer (son logiciel ou un composant légitimement acquis ; CJUE 2021 sur la décompilation pour corriger des erreurs) vs reproduire (spécification sans code protégé, réimplémentation dans un compte ou conteneur sans accès à REA ni à la cible).
- **Disclaimer du projet** : pas de contournement de DRM, licence ou anti-triche ; décompilation IA *« may be incomplete or incorrect »*.
- **Par quoi commencer** : un programme dont on connaît le source, seul cas où chaque réponse se vérifie immédiatement.

## RésuméDe400mots

L'article, signé SFEIR AI, présente REA (Reverse Engineer Anything), un serveur MCP et une CLI publiés sous licence MIT qui donnent à un agent de code les outils d'un rétro-ingénieur. REA n'est ni un décompilateur ni un service en ligne : il tourne sur la machine du développeur et pilote des outils existants. Le dépôt `morluto/rea`, créé le 14 avril 2026, comptait 369 860 étoiles le 23 octobre ; le paquet npm `rea-agents` était en version 6.7.0. Le texte s'organise autour de trois schémas.

Le premier décrit l'installation. Une commande, `npx rea-agents setup`, déclare REA comme serveur MCP auprès de l'agent déjà utilisé (Claude Code, Codex, Cursor) et installe une skill d'enquête. Pour Claude Code, l'enregistrement vaut pour tous les projets ; la documentation recommande un dry-run préalable, un profil séparé via `CLAUDE_CONFIG_DIR` et note que la version est épinglée. REA analyse seul le JavaScript, Electron et .NET ; le code natif exige Ghidra, IDA ou Hopper, Android JADX, le firmware Binwalk ou Unblob. La cible reste locale, mais les résultats d'outils transmis à l'agent partent vers le fournisseur du modèle, ce qui fait de l'analyse d'un code sensible une décision de conformité.

Le deuxième schéma décrit un appel. REA identifie le format puis oriente la cible vers l'analyse statique, un pont authentifié vers un moteur natif, un outil externe ou une capture à l'exécution. Cette dernière lance la cible avec les droits de l'utilisateur. Chaque réponse revient sous forme de preuves — constat, localisation, limitations et inconnues — et un test indépendant relève 744 limitations explicites sur une application Electron de 100 Mo. La politique de sécurité du projet précise que REA n'est pas un sandbox : un binaire inconnu s'ouvre en machine virtuelle ou en conteneur.

Le troisième schéma propose une méthode en quatre étapes : poser une question étroite et écrire sa prédiction, laisser l'agent enquêter, lire les preuves en séparant le vu, l'inféré et l'inconnu, puis vérifier par grep, tests ou source. Le test d'Analytics Vidhya sur Obsidian illustre la boucle : sept minutes, 1,83 dollar. La compréhension débouche sur deux sorties de statut différent. Déboguer son propre logiciel relève d'un cadre connu, la Cour de justice ayant admis en 2021 la décompilation pour corriger des erreurs. Reproduire la fonctionnalité d'un tiers engage d'autres protections, et l'implémentation doit se faire dans un environnement sans accès à REA ni à la cible. L'article conclut que REA abaisse le coût de la compréhension sans supprimer ni le cadre ni la vérification.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | REA en trois schémas : architecture, fonctionnement et usage | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | JADX | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | Electron | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | Claude Code | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | mesure | 369 860 étoiles GitHub au 23 octobre 2026 | MESURE | 0.9 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | permet | sortie en preuves (constat, localisation, limitations, inconnues) | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Ishank Choudhary | PERSONNE | mesure | 744 limitations explicites sur une application Electron de 100 Mo | MESURE | 0.88 | STATIQUE | déclaré_article |
| Analytics Vidhya | ORGANISATION | mesure | enquête sur le sélecteur rapide d'Obsidian en 7 minutes pour 1,83 $ | MESURE | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les résultats d'outils de REA partent vers le fournisseur du modèle même si la cible reste locale | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | REA n'est pas un sandbox : un binaire inconnu s'ouvre en VM ou en conteneur | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | poser une question étroite et écrire sa prédiction avant de lancer l'enquête REA | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| clean-room | METHODOLOGIE | s_applique_à | réimplémentation d'une fonctionnalité tierce | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | réimplémenter dans un compte ou conteneur sans accès à REA ni à la cible | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| CJUE | ORGANISATION | affirme_que | la décompilation est admise pour corriger des erreurs, dans la mesure nécessaire (2021) | AFFIRMATION | 0.84 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| REA | TECHNOLOGIE | catégorie | Outil de rétro-ingénierie piloté par agent via MCP (Reverse Engineer Anything), licence MIT, paquet npm rea-agents 6.7.0 | AJOUT |
| clean-room | METHODOLOGIE | définition | Séparation entre analyse et réimplémentation, imposée par compte ou conteneur distinct | AJOUT |
| Ishank Choudhary | PERSONNE | rôle | Auteur d'un test de REA 6.4.0 sur HackerNoon (14 octobre 2026) | AJOUT |
| Analytics Vidhya | ORGANISATION | rôle | Site technique, test de REA sur Obsidian (18 octobre 2026) | AJOUT |
