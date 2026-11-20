---
themes: [agents-codage-ia-skills, transformation-adoption, strategie-frameworks]
source: SFEIR
---
# girard-rieseberg-ambition-ia-equipe-2026-10-19

## Veille

Article signé **Didier Girard** sur sfeir.com, le **19 octobre 2026** (~2 600 mots, quinze sources notées). Il relit pour une équipe d'ingénierie le tutoriel de **Felix Rieseberg** (Anthropic) publié six jours plus tôt, *How to be more ambitious*. **(A) Restitution** des quatre types d'ambition : **Speed** (l'acquis), **Altitude** (*« what do you want to happen next? »*, l'exemple « keep our apps crash-free » et sa plomberie), **Depth** (cinq techniques et le prompt de *deepening*), **Range** (remplacer les noms par des verbes, sans jeu de rôle), puis la partie sur la self-efficacy (Locke et Latham, Dantzig, Bannister, Sawe). **(B) Réception** : la consigne *« Do not ask the model to judge itself »* reprise par Paul Kuo, et la conversion du texte en skills en quelques jours (work-hard-protocol de Ken Huang, be-ambitious de RoboNuggets et de Dan McAteer, ambition d'Erik MacKinnon, deepen-prompt). **(C) Conséquences pour une équipe** : l'altitude est un chantier d'infrastructure, le juge extérieur devient un livrable, la profondeur se joue au cadrage, l'ambition se standardise par une skill partagée. Prolonge la fiche source [[rieseberg-how-to-be-more-ambitious-2026-10-13]].

## Titre Article

Être plus ambitieux avec l'IA : la méthode de Felix Rieseberg, lue par une équipe d'ingénierie

## Date

2026-10-19

## URL

https://www.sfeir.com/articles/etre-plus-ambitieux-ia-felix-rieseberg/

## Keywords

ambition, IA, Felix Rieseberg, Anthropic, Speed, Altitude, Depth, Range, prompt de deepening, juge extérieur, validation externe, auto-évaluation, evals, tests, crash-free, revue trimestrielle, QBR, self-efficacy, Locke et Latham, fixation d'objectifs, skills, work-hard-protocol, be-ambitious, deepen-prompt, Claude Code, MCP, AI Engineering, erreurs corrélées

## Authors

Didier Girard, SFEIR (signature individuelle), publié sur sfeir.com, site éditorial du cabinet.

## Ton

Article de lecture commentée, en français, à la première personne (« ce que j'en retiens »), destiné aux responsables d'équipes d'ingénierie et aux DSI. Le texte alterne restitution fidèle du tutoriel de Rieseberg, abondamment cité en anglais avec renvoi systématique à la source, et traduction dans le métier (tests, benchmarks, jeux d'évaluation, métriques de production). Le registre est pédagogique et appuyé sur un schéma des quatre axes. Les exemples historiques (Dantzig, Bannister, Landy, Sawe, Torvalds) sont datés et sourcés, parfois complétés par rapport au texte d'origine. La partie réception recense la communauté qui a transformé le texte en skills et souligne leur point commun (une réécriture avant exécution, un juge explicite). Une mise en garde clôt l'article : l'ambition a un coût en calcul et, sans juge ni budget, devient une boucle. L'auteur situe SFEIR comme « AI Engineering Company » et termine par un appel à l'action concret.

## Pense-betes

- **Quatre types d'ambition** (Rieseberg, 13 octobre 2026) : **Speed** (même tâche plus vite, *« bread and butter »*), **Altitude** (confier le résultat, pas la tâche), **Depth** (travailler comme le meilleur expert), **Range** (mobiliser plus de disciplines).
- **Altitude** : de « corrige ce crash » à *« simply keep our apps crash-free »* ; prérequis : rapports de crash, lien version ↔ commit git, machines Windows, macOS et Linux. Formule de l'article : *« L'altitude se paie en plomberie »*. Exemple QBR en trois paliers ; *« Claude, go make money »* ne fonctionne pas encore.
- **Depth, cinq techniques** : outils des meilleurs (bases de données, modèles statistiques), objectifs déraisonnables (200 ms au lieu de 5 s), hypothèses confrontées aux données brutes, connaissance nouvelle, juge extérieur.
- **Prompt de deepening** : *« I want a deeper version of this task, not a bigger one »* ; ce qu'un professionnel ferait, la matière la plus brute, les outils, ce qui prouverait hors du modèle que c'est juste, puis réécriture.
- **Juge extérieur** : *« Do not ask the model to judge itself »* ; Paul Kuo (17 octobre) cite Kim et al. : deux modèles qui se trompent donnent la même mauvaise réponse **environ six fois sur dix** (plus de 350 modèles).
- **Range** : remplacer les noms par des verbes (Kelley et Littman) ; *faire* ce que fait un short seller, pas *écrire comme* lui ; prérequis : un ordinateur et des accès (connecteurs MCP).
- **Réception** : annonce à plus de **3,1 millions de vues** au 15 octobre (Ken Huang) ; skills dérivées : work-hard-protocol (MIT, sept règles, trois protocoles, quatre playbooks), be-ambitious (RoboNuggets, Dan McAteer), ambition (Erik MacKinnon), deepen-prompt (arome3), « prompt de la hauteur » (zoesagan.com).
- **Quatre conséquences pour une équipe** : altitude = infrastructure et droits d'accès des agents ; juge extérieur = livrable (tests, observabilité, evals) ; profondeur = rituel de revue de conception ; ambition = skill partagée dans le dépôt.
- **Réserve de l'auteur** : sans juge ni budget, un objectif déraisonnable devient une boucle patch après patch.

## RésuméDe400mots

Didier Girard commente pour une équipe d'ingénierie le tutoriel publié le 13 octobre 2026 par Felix Rieseberg, engineering manager chez Anthropic, qui a dirigé l'ingénierie de Claude.ai, de Cowork et de Claude Code Desktop et co-maintient Electron. Le tutoriel veut rendre opérationnel un slogan, « soyez plus ambitieux avec l'IA », devenu selon Rieseberg un cri de ralliement sans mode d'emploi.

Rieseberg découpe l'ambition en quatre types. La vitesse, même travail en moins de temps, est l'acquis ; l'auteur note que mesurer un assistant au nombre de lignes produites revient à rester au rez-de-chaussée. L'altitude consiste à confier au modèle le résultat plutôt que la tâche : Rieseberg est passé de la correction de crashs un par un à la consigne de garder les applications sans crash, ce qui a exigé l'accès aux rapports de crash, le lien entre versions et commits, et des machines de test sur trois systèmes. L'exemple de la revue trimestrielle décline trois paliers, jusqu'à concevoir un meilleur dispositif de détection éprouvé sur l'historique. La profondeur consiste à travailler comme le meilleur du domaine : outils d'expert, objectifs déraisonnables, hypothèses confrontées aux données brutes, connaissance nouvelle et juge extérieur, avec un prompt de « deepening » qui fait réécrire la demande. L'étendue mobilise d'autres disciplines en remplaçant les noms par des verbes, sans jeu de rôle.

L'article met en avant la consigne de ne pas demander au modèle de se juger lui-même. Paul Kuo la reprend en citant une étude selon laquelle deux modèles qui se trompent donnent la même mauvaise réponse environ six fois sur dix. La dernière partie du tutoriel porte sur la self-efficacy, appuyée sur Locke et Latham, Dantzig, Bannister et le premier marathon sous deux heures.

La réception a été rapide : plus de 3,1 millions de vues pour l'annonce, et plusieurs skills dérivées (work-hard-protocol, be-ambitious, ambition, deepen-prompt, un « prompt de la hauteur » en français), qui ajoutent toutes une étape de réécriture avant exécution et un juge explicite.

L'auteur en tire quatre conséquences : l'altitude est d'abord un chantier d'infrastructure et de droits d'accès ; le juge extérieur doit devenir un livrable (tests, observabilité, evals) ; la profondeur se ritualise en revue de conception ; l'ambition se standardise par une skill partagée. Il conclut sur une réserve, le coût en calcul d'un objectif sans juge ni budget, et invite à reposer une tâche un niveau plus haut avec un juge.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Didier Girard | PERSONNE | travaille_chez | SFEIR | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | publie | Être plus ambitieux avec l'IA | DOCUMENT | 0.96 | STATIQUE | déclaré_article |
| Être plus ambitieux avec l'IA | DOCUMENT | référence | billet How to be more ambitious | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Felix Rieseberg | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Felix Rieseberg | PERSONNE | publie | billet How to be more ambitious | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| billet How to be more ambitious | DOCUMENT | recommande | Quatre types d'ambition | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Felix Rieseberg | PERSONNE | recommande | Do not ask the model to judge itself | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| Quatre types d'ambition | CONCEPT | utilise | prompt de deepening | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| Quatre types d'ambition | CONCEPT | utilise | juge extérieur | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Paul Kuo | PERSONNE | soutient | juge extérieur | CONCEPT | 0.86 | STATIQUE | déclaré_article |
| Correlated Errors in Large Language Models | DOCUMENT | mesure | deux modèles qui se trompent donnent la même mauvaise réponse environ six fois sur dix | MESURE | 0.82 | STATIQUE | déclaré_article |
| Ken Huang | PERSONNE | a_créé | work-hard-protocol | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| work-hard-protocol | TECHNOLOGIE | est_basé_sur | billet How to be more ambitious | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| Erik MacKinnon | PERSONNE | a_créé | skill ambition | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Didier Girard | PERSONNE | affirme_que | l'altitude est un chantier d'infrastructure avant d'être un prompt | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | recommande | faire du juge extérieur un livrable (tests, observabilité, evals) | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | recommande | standardiser l'ambition par une skill partagée dans le dépôt | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| billet How to be more ambitious | DOCUMENT | est_basé_sur | théorie de la fixation d'objectifs | CONCEPT | 0.8 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Didier Girard | PERSONNE | rôle | auteur, SFEIR | AJOUT |
| Felix Rieseberg | PERSONNE | rôle | engineering manager chez Anthropic, co-mainteneur d'Electron | AJOUT |
| billet How to be more ambitious | DOCUMENT | publication | tutoriel de Felix Rieseberg, 13 octobre 2026 | AJOUT |
| Quatre types d'ambition | CONCEPT | définition | quatre types d'ambition avec un modèle | AJOUT |
| prompt de deepening | METHODOLOGIE | ouverture | « I want a deeper version of this task, not a bigger one » | AJOUT |
| juge extérieur | CONCEPT | définition | validation hors du modèle : tests, benchmarks, jeux non vus, métriques de production | AJOUT |
| work-hard-protocol | TECHNOLOGIE | catégorie | skill MIT de Ken Huang : sept règles, trois protocoles, quatre playbooks | AJOUT |
| Paul Kuo | PERSONNE | apport | vérification contre sources et outils exécutables (paulkuo.tw, 17 octobre 2026) | AJOUT |
