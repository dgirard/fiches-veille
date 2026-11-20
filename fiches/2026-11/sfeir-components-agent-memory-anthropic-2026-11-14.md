---
themes: [agents-codage-ia-skills, recherche-education]
source: SFEIR
---
# sfeir-components-agent-memory-anthropic-2026-11-14

## Veille

Article SFEIR AI publié sur sfeir.com le **14 novembre 2026** (~1 200 mots), qui restitue le billet d'Anthropic Engineering *« The components of agent memory »* du **6 novembre 2026**, rédigé par **Lance Martin**. Trois apports : (A) une définition restrictive — la mémoire d'agent est la connaissance que Claude tire de son expérience et conserve entre sessions sous forme de contexte relisible ; poids, apprentissage en contexte et compaction sont exclus ; (B) une hiérarchie en **quatre couches** (transcripts, notes, représentations type wiki, contexte injecté) et une passe hors ligne, le **dreaming**, rattachée au *sleep-time compute* de Letta et Berkeley ; (C) des mesures : sur CL-Bench, Opus 5.5 passe de **0,655 à 0,838** avec mémoire ; imposer de n'enregistrer que les échecs réduit le gain d'Opus 5 de **0,234** ; wiki et recherche combinés atteignent **61 %** contre 53 % pour la recherche seule. L'article précise que ces chiffres ne sont pas répliqués indépendamment et propose une correspondance, présentée comme sa propre lecture, avec l'architecture 3-tier (Hot/Warm/Cold). Recommandation reprise : *« tell Claude what memory is for, but not how to use it »*. Premier volet d'une série SFEIR sur la mémoire d'agent, qui rejoint les fiches du corpus sur le [[context-engineering]].

## Titre Article

The components of agent memory : ce qu'Anthropic a mesuré, et ce que ça change pour vos agents

## Date

2026-11-14

## URL

https://www.sfeir.com/articles/components-of-agent-memory-anthropic-mesures/

## Keywords

mémoire d'agent, agent memory, Anthropic, Lance Martin, transcripts, notes de mémoire, wiki, contexte injecté, dreaming, sleep-time compute, Letta, CL-Bench, Pokémon Red, Harvey LAB, MEMORY.md, CLAUDE.md, Claude Managed Agents, memory stores, API Dreams, architecture 3-tier, context engineering

## Authors

SFEIR AI (voix éditoriale de SFEIR), article publié sur sfeir.com, site éditorial du groupe SFEIR.

## Ton

Article de restitution technique, en français, destiné aux équipes qui exploitent des agents. Le texte suit le billet source dans son ordre (définition, couches, dreaming, chiffres) et marque systématiquement la provenance : tous les chiffres sont attribués à Anthropic, l'absence de réplication indépendante est signalée, et le fait que plusieurs valeurs ne figurent que sur des graphiques est mentionné. Les limites méthodologiques sont rapportées sans commentaire superflu (comparaison Pokémon sur une seule partie par modèle). Les rapprochements avec les contenus SFEIR (architecture 3-tier) sont explicitement présentés comme une lecture propre et non comme la position d'Anthropic. Le registre devient prescriptif dans la section « Quatre conséquences pratiques », formulée en décisions courtes. La fin situe les produits Anthropic existants (Claude Code, Managed Agents, API Dreams) et annonce la suite de la série sur la mémoire possédée dans un dépôt Git.

## Pense-betes

- **Définition Anthropic** : mémoire = connaissance tirée de l'expérience, conservée entre sessions, sous forme de contexte relisible ; exclut poids, apprentissage en contexte et compaction. En pratique : des fichiers que l'agent écrit, relit et corrige.
- **Quatre couches** (de la plus brute à la plus chère) : transcripts (recherche) → notes écrites par Claude → représentations (wikis de pages reliées) → contexte injecté à chaque session. Plus on monte, plus chaque token coûte.
- **Claude Code** : charge les 200 premières lignes de `MEMORY.md` ou ses 25 premiers Ko.
- **Dreaming** : passe hors ligne entre sessions (relire, corriger, construire des représentations, promouvoir, combler) ; lien avec le *sleep-time compute* (Letta, UC Berkeley). Pokémon Red : note corrigée → Cerulean City à l'action 1 935.
- **Chiffres** : CL-Bench Opus 5.5 0,655 → 0,838 ; Sonnet 4.6 0,330 → 0,364 → 0,641 avec consigne affinée ; règle « n'enregistre que les échecs » : −0,234 pour Opus 5 ; Fable 5 : 9 fichiers, 4 badges vs Sonnet 3.7 : 413 fichiers, 1 badge ; Stainless (420 M tokens) : wiki seul 13 % → 48 %, wiki + recherche 61 % vs 53 %, ~20 000 tokens économisés par question ; questions croisées 87 % vs 73 % ; wiki de 203 Ko pour un corpus de 115 Ko ; 41/57 faits contractuels → 57/57 avec un agent par contrat.
- **Quatre décisions** : écrire l'objectif de la mémoire et laisser l'agent choisir quoi noter ; plafonner la couche injectée ; orienter la maintenance vers ce qui change ; conserver des transcripts cherchables.
- **Produits** : CLAUDE.md (humain) vs auto memory MEMORY.md (agent) ; memory stores de Claude Managed Agents ; API Dreams en research preview depuis le 6 mai 2026 (1 à 100 sessions, non éligible HIPAA).
- À relier : [[Lance-Martin]], [[Agent-Memory]].

## RésuméDe400mots

L'article de SFEIR présente le billet « The components of agent memory » publié le 6 novembre 2026 par l'équipe Engineering d'Anthropic et rédigé par Lance Martin. Le billet commence par une définition : la mémoire d'agent désigne la connaissance que Claude tire de son expérience et garde d'une session à l'autre, sous forme de contexte qu'il peut relire. Les poids du modèle, l'apprentissage en contexte et la compaction en sont exclus. La mémoire se ramène donc à des fichiers que l'agent écrit, relit et corrige.

Anthropic décrit quatre couches, de la plus brute à la plus coûteuse : les transcripts complets des sessions, consultables par recherche ; les notes écrites par Claude ; des représentations comme des wikis de pages reliées ; le contexte injecté à chaque démarrage. Claude Code applique cette logique en ne chargeant que les 200 premières lignes de son fichier MEMORY.md. SFEIR rapproche ces couches de son architecture 3-tier du contexte, en précisant qu'il s'agit de sa propre lecture.

Le billet ajoute une opération de maintenance hors ligne, le dreaming : entre deux sessions, un agent relit les transcripts, corrige les notes fausses, construit des représentations et promeut certaines notes. L'idée est rattachée au sleep-time compute de chercheurs de Letta et de Berkeley.

Les mesures, toutes issues d'Anthropic et non répliquées, sont détaillées. Sur CL-Bench, Opus 5.5 passe de 0,655 à 0,838 avec mémoire. Imposer à l'agent de n'enregistrer que ses échecs réduit nettement le gain. Sur Pokémon Red, un modèle récent qui écrit neuf fichiers obtient quatre badges quand un modèle plus ancien en écrit 413 pour un badge. Sur un grand corpus de code, le wiki combiné à la recherche atteint 61 % des critères contre 53 % pour la recherche seule, et le wiki aide surtout pour les questions qui croisent plusieurs documents. Les limites sont rapportées aussi : un wiki peut dépasser la taille du corpus qu'il résume, et la consigne de construction change le nombre de faits conservés.

La recommandation centrale d'Anthropic est de dire à Claude à quoi sert la mémoire sans lui dicter comment l'utiliser. SFEIR la traduit en quatre décisions : écrire l'objectif et laisser l'agent choisir, plafonner la couche injectée, concentrer la maintenance sur l'information qui change, conserver des transcripts cherchables. L'article recense enfin les produits existants (CLAUDE.md et MEMORY.md, memory stores des Managed Agents, API Dreams) et note que ces mémoires vivent chez l'éditeur, ce qui ouvre la suite de la série.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | article The components of agent memory : ce qu'Anthropic a mesuré | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | référence | The components of agent memory | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | The components of agent memory | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Lance Martin | PERSONNE | a_créé | The components of agent memory | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| The components of agent memory | DOCUMENT | affirme_que | la mémoire d'agent exclut les poids, l'apprentissage en contexte et la compaction | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| mémoire d'agent | CONCEPT | utilise | dreaming | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| dreaming | METHODOLOGIE | s_inspire_de | sleep-time compute | CONCEPT | 0.88 | STATIQUE | déclaré_article |
| Letta | ORGANISATION | a_créé | sleep-time compute | CONCEPT | 0.8 | STATIQUE | déclaré_article |
| mémoire d'agent | CONCEPT | améliore | CL-Bench Opus 5.5 : 0,655 → 0,838 | MESURE | 0.9 | STATIQUE | déclaré_article |
| The components of agent memory | DOCUMENT | mesure | règle « n'enregistrer que les échecs » : gain d'Opus 5 réduit de 0,234 | MESURE | 0.88 | STATIQUE | déclaré_article |
| wiki de mémoire | CONCEPT | améliore | Stainless : 61 % avec wiki et recherche contre 53 % recherche seule | MESURE | 0.88 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | recommande | dire à Claude à quoi sert la mémoire, pas comment l'utiliser | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | MEMORY.md | DOCUMENT | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Managed Agents | TECHNOLOGIE | utilise | memory stores | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| API Dreams | TECHNOLOGIE | fait_partie_de | Claude Managed Agents | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| mémoire d'agent | CONCEPT | converge_avec | architecture 3-tier du contexte | CONCEPT | 0.75 | ATEMPOREL | inféré |
| SFEIR | ORGANISATION | recommande | plafonner la couche injectée et conserver des transcripts cherchables | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| The components of agent memory | DOCUMENT | publication | Billet Anthropic Engineering, 6 novembre 2026 | AJOUT |
| Lance Martin | PERSONNE | rôle | Auteur du billet Anthropic sur la mémoire d'agent | AJOUT |
| mémoire d'agent | CONCEPT | définition | Connaissance conservée entre sessions sous forme de contexte relisible ; 4 couches | AJOUT |
| dreaming | METHODOLOGIE | définition | Passe de maintenance hors ligne de la mémoire entre deux sessions | AJOUT |
| API Dreams | TECHNOLOGIE | statut | Research preview sur demande depuis le 6 mai 2026, 1 à 100 sessions | AJOUT |
| wiki de mémoire | CONCEPT | apport | Utile surtout pour les questions croisant plusieurs documents (87 % vs 73 %) | AJOUT |
