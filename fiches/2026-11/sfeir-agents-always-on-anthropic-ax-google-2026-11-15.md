---
themes: [architecture-construction, agents-codage-ia-skills, outils-plateformes]
source: SFEIR
---
# sfeir-agents-always-on-anthropic-ax-google-2026-11-15

## Veille

Article SFEIR AI publié sur sfeir.com le **15 novembre 2026** (~3 300 mots, 12 sources, un schéma d'architecture), qui rapproche deux textes : le guide *« Building always-on agents »* d'**Anthropic** (signé **William Hu**, 13 novembre 2026) et **Agent Executor (AX)**, runtime open source de **Google** (Apache 2.0, Go, preview depuis mai 2026). Trois apports : (A) la restitution du guide — un agent *« not actually always on »* qui dort entre des **runs**, et **cinq primitives** autour de la boucle : event inbox à worker unique, timers (follow-up et schedule), mémoire en fichiers (*« only hold what the agent can't look up again »*), permissions (proxy de credentials, auto mode, appel d'outil différé), outbox dosée par evals ; coût par tâche résolue annoncé **−78 %** d'Opus 5 à Opus 5.5 sur un sous-ensemble de SWE-bench Pro (1,01 $ → 0,22 $) ; (B) une lecture d'architecte — ces briques sont des patterns connus (consommateur idempotent, transactional outbox, modèle acteur), auxquels le LLM ajoute quatre contraintes, dont l'injection de prompt rapprochée de l'*Agents Rule of Two* de Meta ; (C) AX et **Agent Substrate** (donné à la CNCF avec gVisor le 5 novembre), avec un tableau de recouvrement primitive par primitive, du partiel à l'absent (timers). Les chiffres sont attribués à leurs éditeurs, sans mesure indépendante trouvée. Prolonge la fiche SFEIR sur la mémoire d'agent et le corpus [[Claude-Opus-5]].

## Titre Article

Agents always-on : les cinq primitives d'Anthropic et l'étage AX de Google

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/agents-always-on-anthropic-ax-google/

## Keywords

agents always-on, Building always-on agents, Anthropic, William Hu, run, session, event inbox, timers, mémoire d'agent, permissions, outbox, proxy de credentials, auto mode, appel d'outil différé, Claude Duet, Opus 5.5, Agent Executor, AX, Agent Substrate, gVisor, CNCF, Jaana Dogan, Agents Rule of Two, durable execution, transactional outbox, modèle acteur

## Authors

SFEIR AI (voix éditoriale de SFEIR), article publié sur sfeir.com, site éditorial du groupe SFEIR.

## Ton

Article d'architecture en français, destiné aux architectes, CTO, RSSI et DSI qui passent un agent du prototype à la production ; il précise d'emblée qu'il apporte peu pour un assistant purement conversationnel. Le registre est pédagogique et comparatif : chaque primitive du guide est restituée avec ses citations en anglais traduites entre parenthèses, puis rattachée à des patterns de systèmes distribués que les équipes connaissent déjà. La comparaison avec AX est menée dans un tableau à trois niveaux de recouvrement, en signalant que les deux textes ne se citent pas et qu'aucune comparaison publique n'a été trouvée. Les chiffres sont systématiquement attribués (« mesures d'Anthropic sur un benchmark qu'il a choisi », « chiffres de Google ») et les écarts de documentation relevés (fournisseur Anthropic documenté mais non implémenté dans AX). La conclusion se décline par rôle, puis liste les limites.

## Pense-betes

- **Définition** : agents *« stateful and proactive »* ; l'agent dort et se réveille pour un **run** (événement → tâche → enregistrement), dans une **session** (transcript). Aucun token pendant le sommeil.
- **Coût** : Opus 5.5 −78 % par tâche résolue vs Opus 5 sur tâches longues (−40 % en charge typique) ; 478 problèmes SWE-bench Pro, 1,01 $ → 0,22 $, 91,9 % → 92,8 % de résolution.
- **Claude Duet** (21 octobre 2026, research preview) : brief matinal, VM avec navigateur, accord requis avant envoi, paiement, signature, suppression. Non cité par le guide.
- **Inbox** : table durable, handler HTTP qui acquitte vite, déduplication par `source_id`, **un seul worker actif par inbox**, regroupement des messages ; commencer par une inbox par utilisateur.
- **Timers** : follow-up vs schedule ; table séparée ; un scheduler les dépose dans l'inbox, jamais de run direct.
- **Mémoire** : répertoire de fichiers sur base ou object store ; seul un index chargé au réveil ; pointeurs vers les outils ; dreaming facultatif.
- **Permissions** : proxy de credentials hors sandbox ; auto mode (classifieurs) ; appel d'outil différé (session sauvegardée, réponse via l'inbox, carte MCP Apps).
- **Outbox** : un run finit par un message, rien ou une demande différée ; *« start quiet and then earn more of the user's attention »*, réglé par evals.
- **Quatre contraintes LLM** : réveil payé en tokens, mémoire rédigée par le modèle, entrées non fiables (injection), jugement sur l'envoi. *Agents Rule of Two* (Meta, 31 octobre 2025).
- **AX** : Task, Workspace, Model, Gateway (`ax.io/v1alpha1`), `ax suspend` / `ax resume`, 14 710 étoiles ; *« It's NOT an agentic framework »* (Jaana Dogan). **Agent Substrate** : état de l'acteur séparé du calcul, reprise < 500 ms, 90-95 % du temps en attente.
- **Recouvrement** : inbox partiel, timers absents (triggers côté Managed Agents Gemini), mémoire différente, permissions fortes sur les secrets, outbox faible. Le contrôleur AX n'implémente que le fournisseur Google (issue #371).
- À relier : [[Model-Context-Protocol]], [[Agent-Memory]].

## RésuméDe400mots

L'article de SFEIR présente le guide « Building always-on agents » publié par Anthropic le 13 novembre 2026 et le compare à Agent Executor, le runtime open source de Google. Le guide décrit comment construire un agent qui surveille des outils, relance un dossier ou envoie un point quotidien, sans fournir de produit ni de code.

Anthropic précise qu'un agent dit toujours actif dort en réalité la plupart du temps et se réveille pour des périodes de travail appelées runs. Deux raisons expliquent le retour de ces agents : des modèles qui comprennent mieux quand solliciter l'utilisateur, et un coût en baisse, Opus 5.5 coûtant 78 % de moins qu'Opus 5 par tâche résolue sur un benchmark de code long, selon Anthropic.

Le guide pose cinq briques autour de la boucle d'agent. Une file d'événements durable, servie par un seul worker, évite les runs concurrents et les pertes. Des timers séparés rendent l'agent proactif en déposant leurs échéances dans cette file. La mémoire est un répertoire de fichiers persistants qui ne contient que ce que l'agent ne peut pas retrouver ailleurs, avec un index chargé au réveil. Les permissions reposent sur un proxy qui ajoute les secrets hors de l'environnement de l'agent, sur des classifieurs qui bloquent les actions dangereuses et sur des appels différés qui mettent la session en pause en attendant l'accord de l'utilisateur. Une file de sortie, enfin, dose les messages, l'agent devant commencer discret.

SFEIR rattache ces briques à des patterns connus des systèmes distribués et identifie quatre contraintes propres aux modèles de langage : le coût en tokens de chaque réveil, une mémoire rédigée par le modèle, des entrées non fiables exposées à l'injection de prompt, et le jugement nécessaire pour décider d'envoyer ou non un message.

Agent Executor, publié par Google en mai 2026, se situe un étage plus bas. Il ne sert pas à écrire un agent mais à l'exécuter de façon durable, isolée et reprenable, au-dessus d'Agent Substrate, une couche Kubernetes donnée à la CNCF en novembre. Un tableau montre que son recouvrement avec le guide est partiel : fort sur la protection des secrets, absent sur les timers, différent sur la mémoire. Les deux peuvent se combiner, mais AX n'implémente encore que le fournisseur de modèles de Google.

L'article conclut par des conseils par rôle, du démarrage par la file d'événements à la mesure du coût sur son propre trafic, et rappelle que les chiffres cités sont ceux des éditeurs.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Agents always-on : les cinq primitives d'Anthropic et l'étage AX de Google | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Building always-on agents | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| William Hu | PERSONNE | a_créé | Building always-on agents | DOCUMENT | 0.93 | STATIQUE | déclaré_article |
| Building always-on agents | DOCUMENT | recommande | event inbox à worker unique, timers, mémoire, permissions, outbox | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| agents always-on | TECHNOLOGIE | utilise | event inbox | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| agents always-on | TECHNOLOGIE | utilise | proxy de credentials | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| agents always-on | TECHNOLOGIE | utilise | appel d'outil différé | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| Building always-on agents | DOCUMENT | affirme_que | la mémoire ne doit contenir que ce que l'agent ne peut pas retrouver ailleurs | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Claude Opus 5.5 | TECHNOLOGIE | réduit | coût par tâche résolue −78 % vs Opus 5 (SWE-bench Pro, 1,01 $ → 0,22 $) | MESURE | 0.85 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Claude Duet | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| event inbox | METHODOLOGIE | s_inspire_de | modèle acteur | CONCEPT | 0.78 | ATEMPOREL | inféré |
| Agents Rule of Two | CONCEPT | s_applique_à | agents always-on | TECHNOLOGIE | 0.8 | ATEMPOREL | déclaré_article |
| Meta | ORGANISATION | publie | Agents Rule of Two | CONCEPT | 0.9 | STATIQUE | déclaré_article |
| Google | ORGANISATION | a_créé | Agent Executor | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Jaana Dogan | PERSONNE | affirme_que | It's NOT an agentic framework | CITATION | 0.9 | STATIQUE | déclaré_article |
| Agent Executor | TECHNOLOGIE | utilise | Agent Substrate | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Agent Substrate | TECHNOLOGIE | utilise | gVisor | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Agent Substrate | TECHNOLOGIE | fait_partie_de | CNCF | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |
| Agent Executor | TECHNOLOGIE | converge_avec | proxy de credentials | TECHNOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| Agent Executor | TECHNOLOGIE | utilise | Kubernetes | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | commencer par l'inbox et mesurer le coût par tâche résolue sur son propre trafic | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Building always-on agents | DOCUMENT | publication | Guide d'architecture Anthropic, William Hu, 13 novembre 2026 | AJOUT |
| William Hu | PERSONNE | rôle | Auteur du guide Anthropic sur les agents always-on | AJOUT |
| agents always-on | TECHNOLOGIE | définition | Agents avec état et proactifs, qui dorment entre des runs déclenchés par événements | AJOUT |
| event inbox | METHODOLOGIE | définition | File durable d'événements servie par un seul worker actif, déduplication par source | AJOUT |
| appel d'outil différé | METHODOLOGIE | définition | Run mis en pause, session sauvegardée, reprise par un nouvel événement après accord | AJOUT |
| proxy de credentials | TECHNOLOGIE | rôle | Ajoute les secrets aux requêtes sortantes hors de l'environnement de l'agent | AJOUT |
| Agent Executor | TECHNOLOGIE | catégorie | Runtime d'agents open source de Google (AX), Apache 2.0, Go, preview, 14 710 étoiles | AJOUT |
| Agent Substrate | TECHNOLOGIE | catégorie | Couche Kubernetes séparant état d'acteur et calcul, donnée à la CNCF (Sandbox) | AJOUT |
| Jaana Dogan | PERSONNE | rôle | Coauteure de l'annonce d'Agent Executor chez Google | AJOUT |
| Claude Duet | TECHNOLOGIE | statut | Produit grand public d'agent proactif, research preview depuis le 21 octobre 2026 | AJOUT |
