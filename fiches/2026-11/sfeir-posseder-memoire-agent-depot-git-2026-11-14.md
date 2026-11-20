---
themes: [agents-codage-ia-skills, architecture-construction]
source: SFEIR
---
# sfeir-posseder-memoire-agent-depot-git-2026-11-14

## Veille

Article SFEIR AI publié sur sfeir.com le **14 novembre 2026** (~1 200 mots), chapeau d'une série de sept volets sur la mémoire d'agent. Il part d'un développeur qui utilise **six agents** (Claude Code, Codex, Cursor, Hermes Agent, CodeBuddy, WorkBuddy), chacun avec sa propre mémoire — un trou que SFEIR nomme **Ephemeral Intelligence Gap**. Trois apports : (A) deux appuis datés — la thèse de **Garry Tan** (*« Own Your Intelligence »*, 6 août 2026 : modèle loué, contexte possédé) et les mesures d'**Anthropic** (6 novembre 2026 : CL-Bench **0,655 → 0,838**) ; (B) une architecture en **deux couches** : copie maîtresse en Markdown dans un dépôt Git privé, index par-dessus (**GBrain** ou **TencentDB Agent Memory**, tous deux MIT), avec la règle que l'index doit pouvoir être supprimé et reconstruit ; (C) quatre risques (empoisonnement, faits périmés, secrets et données personnelles, prolifération) et **cinq règles d'équipe** : un dépôt de contexte par équipe, écritures d'agent par pull request relue, plafond de lignes, maintenance planifiée, test de réversibilité trimestriel. L'article rattache le format au gist *LLM Wiki* d'Andrej Karpathy et cite Brandon Waselnuk : *« confident recall of stale facts is worse than no memory »*. Rejoint les fiches du corpus sur le [[context-engineering]].

## Titre Article

Posséder sa mémoire d'agent : le dépôt Git comme cerveau partagé entre tous vos agents IA

## Date

2026-11-14

## URL

https://www.sfeir.com/articles/posseder-sa-memoire-agent-depot-git/

## Keywords

mémoire d'agent, dépôt Git, Markdown, cerveau partagé, Ephemeral Intelligence Gap, contexte possédé, GBrain, TencentDB Agent Memory, LLM Wiki, Karpathy, Claude Code, MEMORY.md, Codex memory v2, Hermes Agent, CodeBuddy, WorkBuddy, Cursor, dreaming, empoisonnement de mémoire, faits périmés, RGPD, Design to Exit, CDLC, réversibilité

## Authors

SFEIR AI (voix éditoriale de SFEIR), article publié sur sfeir.com, site éditorial du groupe SFEIR.

## Ton

Article chapeau en français, de registre architectural, adressé aux équipes de développement et à leurs responsables. Il installe un cas concret (un développeur, six agents), puis appuie le schéma sur deux sources datées présentées comme la thèse et la preuve technique, avec renvoi systématique vers les volets détaillés de la série. Les chiffres sont attribués à l'éditeur (« chiffre de l'éditeur ») et les limites des outils citées depuis leur propre documentation (README de GBrain sur la reconstruction, absence de Cursor chez TencentDB). Le texte consacre une section aux risques avant de proposer des règles, et distingue explicitement le schéma personnel de sa transposition en équipe. La fin liste les sept articles de la série.

## Pense-betes

- **Constat** : chaque agent garde sa mémoire — CLAUDE.md (humain) + MEMORY.md (agent) pour Claude Code ; Codex « memory v2 » depuis la CLI 0.165.0 (27 octobre 2026), capable d'importer des mémoires d'autres agents ; Hermes Agent stocke faits et skills localement. SFEIR nomme ce trou **Ephemeral Intelligence Gap**.
- **Thèse** (Garry Tan) : modèle loué, contexte possédé, harnais ; *« My brain runs on my own infra, in my own repo, under my own keys. »*
- **Preuve** (Anthropic) : CL-Bench Opus 5.5 0,655 → 0,838 ; conditions : petite couche injectée, correction régulière par dreaming.
- **Origine du format** : gist *LLM Wiki* d'Andrej Karpathy, cité par Anthropic et par TencentDB (actif LLM-Wiki). Maxime d'Addy Osmani : l'agent oublie, le dépôt non.
- **Deux couches** : (1) copie maîtresse Markdown dans un dépôt Git privé (historique, diff, revue, retour arrière) ; (2) index : GBrain (Postgres, graphe, CLI + MCP, mode *company brain*) ou TencentDB Agent Memory (hub d'équipe depuis la 2.0.0 du 3 août 2026, visibilité privée/équipe/restreinte). TencentDB ne couvre pas Cursor au 14 novembre 2026.
- **Règle de construction** : l'index se supprime et se reconstruit depuis les fichiers ; tout fait qui compte vit dans un fichier.
- **Quatre risques** : empoisonnement par injection de prompt ; faits périmés ; secrets et données personnelles (RGPD, l'historique Git complique l'effacement) ; prolifération (413 fichiers → 1 badge, 10 fichiers → 4 badges sur Pokémon Red).
- **Cinq règles d'équipe** : dépôt de contexte par équipe avec les droits du code ; écriture d'agent = PR relue ; plafond de lignes injectées ; maintenance planifiée ; test de réversibilité trimestriel.
- À relier : [[Andrej-Karpathy]], [[Addy-Osmani]].

## RésuméDe400mots

Cet article ouvre une série de SFEIR sur la mémoire des agents. Il part d'une situation courante : un développeur utilise plusieurs agents selon la tâche, Claude Code, Codex, Cursor, Hermes Agent, CodeBuddy et WorkBuddy, et chacun conserve sa propre mémoire dans son propre format. Changer d'outil oblige à répéter le contexte. SFEIR appelle ce manque l'Ephemeral Intelligence Gap.

Le schéma qui circule chez les praticiens en 2026 consiste à donner à tous ces agents un seul cerveau : un dépôt Git privé de fichiers Markdown, que tous lisent et écrivent, surmonté d'un outil qui l'indexe. L'article l'appuie sur deux publications. Le talk de Garry Tan, publié par Y Combinator en août 2026, pose qu'un modèle se loue alors que le contexte se possède. Le billet d'Anthropic de novembre 2026 mesure le gain d'une mémoire en fichiers lisibles et pose deux conditions : une couche chargée à chaque session réduite, et une correction régulière des notes. Le format remonte au wiki maintenu par un modèle de langage décrit par Andrej Karpathy.

L'architecture comporte deux couches. La copie maîtresse est un ensemble de fichiers Markdown dans un dépôt Git, que tout agent sait lire et que Git dote d'historique, de revue et de retour arrière. L'index rend ce dépôt interrogeable ; deux outils open source sous licence MIT sont cités, GBrain de Garry Tan et TencentDB Agent Memory de Tencent Cloud, devenu un hub d'équipe en août 2026. La règle centrale est de pouvoir supprimer l'index et le reconstruire depuis les fichiers, ce qui suppose que tout fait important vive dans un fichier. Les deux index ne couvrent pas les mêmes agents.

Quatre risques sont à instruire : l'empoisonnement d'une note après une injection de prompt, rechargée à chaque session ; les faits périmés rappelés avec assurance ; la présence de secrets et de données personnelles, que l'historique Git rend difficiles à effacer ; la prolifération des fichiers, que les mesures d'Anthropic associent à de moins bons résultats.

Pour passer de l'usage personnel à l'équipe, SFEIR propose cinq règles : un dépôt de contexte par équipe avec les mêmes droits que le code, des écritures d'agent soumises à une pull request relue, un plafond de lignes pour les fichiers injectés, une maintenance planifiée et un test trimestriel de réversibilité de l'index. Ces règles traitent le contexte comme une dépendance logicielle.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Posséder sa mémoire d'agent : le dépôt Git comme cerveau partagé | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | a_créé | Ephemeral Intelligence Gap | CONCEPT | 0.88 | STATIQUE | déclaré_article |
| dépôt Git de mémoire | METHODOLOGIE | résout | Ephemeral Intelligence Gap | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| dépôt Git de mémoire | METHODOLOGIE | est_basé_sur | talk Own Your Intelligence | DOCUMENT | 0.85 | STATIQUE | déclaré_article |
| dépôt Git de mémoire | METHODOLOGIE | est_basé_sur | The components of agent memory | DOCUMENT | 0.85 | STATIQUE | déclaré_article |
| dépôt Git de mémoire | METHODOLOGIE | s_inspire_de | LLM Wiki | DOCUMENT | 0.85 | STATIQUE | déclaré_article |
| Andrej Karpathy | PERSONNE | a_créé | LLM Wiki | DOCUMENT | 0.92 | STATIQUE | déclaré_article |
| GBrain | TECHNOLOGIE | est_instance_de | dépôt Git de mémoire | METHODOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| dépôt Git de mémoire | METHODOLOGIE | utilise | TencentDB Agent Memory | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| Codex memory v2 | TECHNOLOGIE | fait_partie_de | Codex | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | MEMORY.md | DOCUMENT | 0.92 | DYNAMIQUE | déclaré_article |
| Brandon Waselnuk | PERSONNE | affirme_que | confident recall of stale facts is worse than no memory | CITATION | 0.9 | STATIQUE | déclaré_article |
| Brandon Waselnuk | PERSONNE | travaille_chez | Unblocked | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |
| empoisonnement de mémoire | CONCEPT | s_applique_à | dépôt Git de mémoire | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | écritures d'agent en mémoire par pull request relue par un humain | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | un test de réversibilité de l'index par trimestre | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| dépôt Git de mémoire | METHODOLOGIE | converge_avec | CDLC | METHODOLOGIE | 0.8 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| dépôt Git de mémoire | METHODOLOGIE | définition | Copie maîtresse Markdown dans un dépôt Git, index reconstructible par-dessus | AJOUT |
| Ephemeral Intelligence Gap | CONCEPT | définition | Perte de contexte d'un agent à l'autre, chaque agent ayant sa mémoire | AJOUT |
| LLM Wiki | DOCUMENT | auteur | Gist GitHub d'Andrej Karpathy sur le wiki maintenu par LLM | AJOUT |
| Brandon Waselnuk | PERSONNE | rôle | Auteur chez Unblocked, critique des hubs de mémoire d'équipe | AJOUT |
| empoisonnement de mémoire | CONCEPT | définition | Note malveillante écrite après injection de prompt, rechargée à chaque session | AJOUT |
| Codex memory v2 | TECHNOLOGIE | version | Moteur de mémoire de la CLI Codex depuis 0.165.0 (27 octobre 2026) | AJOUT |
