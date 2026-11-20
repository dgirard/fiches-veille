---
themes: [agents-codage-ia-skills, strategie-frameworks, politique-regulation]
source: SFEIR
---
# sfeir-memoire-agent-souverainete-2026-11-14

## Veille

Article SFEIR AI publié sur sfeir.com le **14 novembre 2026** (~900 mots), qui pose la question de l'emplacement de la mémoire des agents sous l'angle de la souveraineté. Il part d'une chronologie : rachat de **Cursor** par **SpaceX** effectif le 14 août 2026 (**60 Md$** en actions), annonce par **OpenAI** le 28 août de l'arrêt de son contrat avec Cursor, puis prolongation sans date le 12 novembre. Trois apports : (A) trois emplacements — mémoire native de l'éditeur, hub de mémoire (TencentDB Agent Memory), dépôt Git de Markdown (schéma GBrain) ; (B) un tableau sur **six critères** (portabilité, droits, recherche, historique, localisation, coût de sortie), présenté comme une synthèse à tester sur ses propres agents ; (C) une architecture combinée Git + hub + native tenue par trois règles (une seule source de vérité, un index jetable, une maintenance planifiée), rattachée au concept **Design to Exit**. Une section situe les juridictions (CodeBuddy et WorkBuddy à Singapour, éditeurs américains, API Dreams non éligible HIPAA/ZDR). L'article se clôt sur **sept questions**, dont deux à traiter en premier : chronométrer une reconstruction de l'index et écrire ce que devient la mémoire à la fin d'un contrat. Volet de la série SFEIR sur la mémoire d'agent, à rapprocher des fiches [[Cursor-organisation]].

## Titre Article

Mémoire d'agent et souveraineté : Git, base managée ou mémoire native de l'éditeur ?

## Date

2026-11-14

## URL

https://www.sfeir.com/articles/memoire-agent-souverainete-git-base-managee-native/

## Keywords

mémoire d'agent, souveraineté, Design to Exit, réversibilité, Git, Markdown, hub de mémoire, TencentDB Agent Memory, GBrain, mémoire native, Claude Code, Codex, Cursor, SpaceX, OpenAI, juridiction, localisation des données, CodeBuddy, WorkBuddy, API Dreams, HIPAA, Zero Data Retention, Matrice Souveraineté Agentique

## Authors

SFEIR AI (voix éditoriale de SFEIR), article publié sur sfeir.com, site éditorial du groupe SFEIR.

## Ton

Article d'aide à la décision, en français, pour DSI, architectes et responsables de la souveraineté numérique. L'ouverture est factuelle et datée : une chronologie de l'affaire Cursor reconstituée à partir de sources primaires (billet d'OpenAI et sa mise à jour, message de Michael Truell, documentation Cursor), citées en anglais. Le corps est structuré en grilles (trois emplacements, six critères, trois règles, sept questions), avec un tableau comparatif dont l'article précise qu'il résume les autres volets de la série et doit être vérifié sur le terrain. Le registre reste prescriptif mais borné : il conseille une combinaison plutôt qu'un choix exclusif et termine par deux actions concrètes. Les rappels juridictionnels sont formulés sans commentaire, éditeur par éditeur, en renvoyant à la Matrice Souveraineté Agentique pour la classification.

## Pense-betes

- **Chronologie Cursor** : rachat par SpaceX effectif le 14 août 2026 (60 Md$, en actions) ; 28 août, OpenAI annonce *« wind down our contract providing OpenAI models to Cursor »*, arrêt proposé au 12 novembre ; Michael Truell : modèles OpenAI ≈ **5 %** du trafic ; 12 novembre, accès prolongé sans date, pas de futurs modèles OpenAI pour Cursor.
- **Trois emplacements** : (A) mémoire native (Claude Code, memory stores des Managed Agents, mémoires Codex, faits d'Hermes Agent) ; (B) hub de mémoire (TencentDB Agent Memory) ; (C) dépôt Git de Markdown (schéma GBrain).
- **Six critères** : portabilité (C totale, A faible sauf import Codex), droits (B fins, C ceux du dépôt sans granularité par note), recherche (C aucune sans index), historique (C : diff, PR, retour arrière), localisation, coût de sortie (export encore partiel chez TencentDB).
- **Architecture combinée** : Git = copie maîtresse, hub = index et droits, mémoire native limitée à ce que le dépôt sait déjà.
- **Trois règles** : une seule source de vérité ; un index jetable (sa reconstruction se teste comme une restauration) ; une maintenance planifiée (dreaming ou relecture humaine mensuelle).
- **Juridictions** : CodeBuddy Entreprise et WorkBuddy international stockés à Singapour (accès possible d'équipes en Chine pour WorkBuddy) ; Claude, Codex, Cursor = éditeurs américains ; API Dreams non éligible HIPAA ni ZDR hors Managed Agents auto-hébergés. Un dépôt sur forge interne sort la copie maîtresse de l'équation, pas les prompts.
- **Sept questions** : nombre d'agents, fait faux le plus coûteux, relecture des écritures, localisation, temps de reconstruction de l'index, données personnelles et base légale, sort de la mémoire en fin de contrat.
- À relier : [[SpaceX]], [[OpenAI]].

## RésuméDe400mots

L'article part d'un épisode récent pour poser la question de l'emplacement de la mémoire des agents. En août 2026, le rachat de Cursor par SpaceX est devenu effectif ; quelques jours plus tard, OpenAI a annoncé vouloir mettre fin à la fourniture de ses modèles à Cursor, avant de prolonger l'accès sans nouvelle date le 12 novembre. Le CEO de Cursor indiquait que ces modèles représentaient environ 5 % du trafic. Pour SFEIR, une équipe dont la mémoire de travail vit dans le format d'un seul outil doit se demander ce qu'elle en garderait dans ce type de situation.

Trois emplacements sont décrits. La mémoire native de l'éditeur (Claude Code, Managed Agents, Codex, Hermes Agent) fonctionne dès l'installation. Un hub de mémoire comme TencentDB Agent Memory sert plusieurs agents et gère des droits fins. Un dépôt Git de fichiers Markdown, sur le modèle de GBrain, est lisible par tous les agents, avec un index par-dessus.

Un tableau compare ces options sur six critères : portabilité entre agents, droits d'accès, recherche, historique et revue, localisation des données, coût de sortie. Le dépôt Git l'emporte en portabilité et en historique mais n'offre ni recherche sans index ni droits par note ; le hub apporte la recherche et les droits ; la mémoire native dépend de chaque éditeur. L'article invite à tester chaque ligne sur ses propres agents.

L'architecture proposée combine les trois : Git porte la copie maîtresse, le hub porte l'index et les droits, la mémoire native reste active pour le confort mais limitée à ce que le dépôt contient. Trois règles la tiennent : une seule source de vérité, un index jetable dont la reconstruction se teste, une maintenance planifiée des notes. SFEIR y voit l'application du concept Design to Exit au contexte.

La section sur les juridictions rappelle où sont stockées les données de plusieurs outils (Singapour pour CodeBuddy et WorkBuddy, éditeurs américains pour Claude, Codex et Cursor) et les limites d'éligibilité de l'API Dreams d'Anthropic. Un dépôt hébergé sur une forge interne maîtrise la copie maîtresse, mais les prompts et la mémoire injectée partent toujours vers le modèle.

L'article termine par sept questions à se poser avant de choisir et recommande de commencer par deux : mesurer le temps de reconstruction de l'index à partir des fichiers, et décider à l'avance du sort de la mémoire quand un contrat éditeur s'arrête.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Mémoire d'agent et souveraineté : Git, base managée ou mémoire native de l'éditeur ? | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Cursor | ORGANISATION | fait_partie_de | SpaceX | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| rachat de Cursor par SpaceX | EVENEMENT | mesure | 60 milliards de dollars, en actions, effectif le 14 août 2026 | MESURE | 0.92 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | affirme_que | wind down our contract providing OpenAI models to Cursor | CITATION | 0.9 | STATIQUE | déclaré_article |
| Michael Truell | PERSONNE | dirige | Cursor | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Michael Truell | PERSONNE | affirme_que | OpenAI models serve about 5% of Cursor user traffic | CITATION | 0.9 | STATIQUE | déclaré_article |
| dépôt Git de mémoire | METHODOLOGIE | concurrence | mémoire native de l'éditeur | CONCEPT | 0.8 | ATEMPOREL | déclaré_article |
| dépôt Git de mémoire | METHODOLOGIE | concurrence | TencentDB Agent Memory | TECHNOLOGIE | 0.78 | DYNAMIQUE | déclaré_article |
| dépôt Git de mémoire | METHODOLOGIE | est_instance_de | Design to Exit | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| dépôt Git de mémoire | METHODOLOGIE | améliore | portabilité de la mémoire entre agents | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | permet | droits d'accès fins sur la mémoire d'équipe | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| GBrain | TECHNOLOGIE | est_instance_de | dépôt Git de mémoire | METHODOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | une seule source de vérité, un index jetable, une maintenance planifiée | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | CodeBuddy Entreprise et WorkBuddy international stockent leurs données à Singapour | AFFIRMATION | 0.82 | DYNAMIQUE | déclaré_article |
| API Dreams | TECHNOLOGIE | mesure | non éligible HIPAA ni Zero Data Retention hors Managed Agents auto-hébergés | MESURE | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | chronométrer la reconstruction de l'index et prévoir le sort de la mémoire en fin de contrat | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| rachat de Cursor par SpaceX | EVENEMENT | date | Effectif le 14 août 2026, 60 Md$ en actions | AJOUT |
| Michael Truell | PERSONNE | rôle | CEO de Cursor | AJOUT |
| dépôt Git de mémoire | METHODOLOGIE | définition | Mémoire d'agent en fichiers Markdown dans un dépôt Git, index reconstructible par-dessus | AJOUT |
| mémoire native de l'éditeur | CONCEPT | définition | Mémoire intégrée à chaque agent (Claude Code, Codex, Hermes), portabilité faible | AJOUT |
| Design to Exit | METHODOLOGIE | définition | Concevoir pour pouvoir sortir : index jetable, copie maîtresse en format ouvert | AJOUT |
| TencentDB Agent Memory | TECHNOLOGIE | catégorie | Hub de mémoire d'équipe auto-hébergeable, droits fins | AJOUT |
