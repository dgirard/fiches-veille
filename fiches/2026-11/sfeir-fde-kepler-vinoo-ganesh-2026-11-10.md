---
themes: [transformation-adoption, strategie-frameworks]
source: SFEIR
---
# sfeir-fde-kepler-vinoo-ganesh-2026-11-10

## Veille

Critique éditoriale **SFEIR AI** publiée sur sfeir.com le **10 novembre 2026**, dans la série de neuf retours sur la playlist *forward deployed engineering* de l'**AI Engineer World's Fair 2026**. Elle porte sur le talk de **Vinoo Ganesh**, cofondateur et CEO de **Kepler**, sept ans chez **Palantir** (créateur du programme **Project Frontline**, ~**350** ingénieurs formés au FDE), 22 min 20, **5 850** vues. Thèse empruntée à **Shyam Sankar** : le FDE relève de la **stratégie produit**, on le juge à ce qu'il a fait entrer dans le produit. Quatre histoires, quatre règles. **(1)** Phoenix, stockage conçu sans clients (14 To de RAM au démarrage). **(2)** Un cahier des charges de **47 pages** remplacé par une alerte Slack construite en **quatre heures** après la question *« What's the first thing you do with this information Monday morning? »*. **(3)** Une visionneuse Parquet écrite en une nuit qui débloque une migration (pipeline de **17 h à 2 h**). **(4)** « vinoo.groovy », script provisoire toujours en production un an plus tard → livrer comme si le code devait tourner **dix-huit mois**. Notes SFEIR : **4/5** et **5/5**, meilleur talk de la série.

## Titre Article

Vinoo Ganesh (Kepler) fait du FDE une stratégie produit, histoires de terrain à l'appui

## Date

2026-11-10

## URL

https://www.sfeir.com/articles/fde-kepler-vinoo-ganesh/

## Keywords

forward deployed engineering, FDE, Kepler, Vinoo Ganesh, Palantir, Project Frontline, Citadel, Shyam Sankar, stratégie produit, AI Engineer World's Fair 2026, Phoenix, Cassandra, cahier des charges, alerte Slack, observation terrain, Parquet, CSV, signaux d'observation, vocabulaire, ontologie, verrouillage par le langage, skills, MCP, script provisoire, règle des dix-huit mois, architecte solutions, ESN, critique de talk

## Authors

SFEIR AI (voix éditoriale non signée), sfeir.com, site éditorial de SFEIR. Critique du talk de Vinoo Ganesh (Kepler).

## Ton

Critique de talk au format fixe de la série SFEIR (encadré, minutages, « Les limites », « Pour une ESN », verdict noté). Registre narratif et favorable : l'article restitue chaque histoire de terrain puis la règle que l'orateur en tire, et recommande le talk *« en entier, de préférence avec votre équipe de delivery »*. Les réserves sont posées en fin de texte : le talk raconte Palantir plus que Kepler, les chiffres viennent de souvenirs (2,3 millions de keyspaces à 5 Mo donnent plutôt 11,5 To que 14), et l'argument du langage décrit une stratégie d'enfermement du client. Public : équipes de delivery, consultants data, responsables FDE.

## Pense-betes

- **Format** : 22 min 20, mis en ligne le 28 juillet 2026, 5 850 vues — quinze fois moins que le « FDE 101 » de Kevin Bai.
- **Orateur** : sept ans chez Palantir (déployé en Irak et Afghanistan), créateur de Project Frontline (~350 personnes, retrouvées comme FDE chez OpenAI, Anthropic, xAI), programme similaire chez Citadel, cofondateur de Kepler.
- **Thèse (vers 2:01)** : FDE = stratégie produit (Shyam Sankar). Chez Palantir, le FDE a servi à découvrir Foundry ; le modèle de vente est venu après. Un ingénieur qui se contente de rendre le client heureux fait le travail d'un architecte solutions.
- **Phoenix (vers 3:02)** : stockage conçu vers 2013 sans parler aux clients ; 2,3 M de keyspaces Cassandra, 14 To de RAM ; dates vides converties au 1er janvier 1970.
- **47 pages (vers 5:05)** : tableau de bord, 14 indicateurs, 3 mois de dev après 4 mois de cadrage → alerte Slack en 4 h. Règle : correction < 1 jour = on livre ; celui qui définit le problème possède la solution.
- **Parquet (vers 8:10)** : ingénieure qui ouvre les CSV d'un double-clic sous Windows ; visionneuse Parquet en une nuit, migration validée en 2 jours, pipeline ~17 h → 2 h.
- **Signaux d'observation** : tâche répétée, copier-coller entre outils, soupir, changement d'onglet, téléphone sorti ; question « quelle est la partie la plus pénible de votre matinée ? ». Il faut un badge chez le client.
- **Langage (vers 12:13)** : customer / client / billing entity / org ID ; fixer le vocabulaire (noms = entités, verbes = opérations) ; l'ontologie de Palantir en est née ; celui qui fixe le langage devient la fondation (exemples : skills, MCP).
- **vinoo.groovy (vers 16:16)** : cinq questions avant de livrer — appel à 2 h du matin dans six mois ? compromis ? à qui je transmets ? qui répond quand ça casse ? produit ou poubelle ?
- **Verdict** : 4/5 et 5/5 ; la vidéo à voir si l'on n'en voit qu'une.

## RésuméDe400mots

SFEIR AI publie le 10 novembre 2026 une critique du talk « How Forward Deployed Engineering is done at Kepler », donné à l'AI Engineer World's Fair 2026 par Vinoo Ganesh, cofondateur et CEO de Kepler. Ancien de Palantir pendant sept ans, il y a créé Project Frontline, programme de rotation qui a transformé environ 350 ingénieurs logiciels en FDE, puis un programme comparable chez Citadel. SFEIR le présente comme le meilleur talk de la playlist.

La thèse reprend une formule de Shyam Sankar, CTO de Palantir : le FDE relève de la stratégie produit, et on le juge à ce qu'il a fait entrer dans le produit. Chez Palantir, le FDE a d'abord servi à découvrir Foundry ; le modèle de vente n'est venu qu'ensuite. Un ingénieur qui se contente de satisfaire le client fait le travail d'un architecte solutions.

Le talk avance par histoires. Phoenix, système de stockage conçu sans parler aux clients, exigeait 14 To de RAM pour démarrer et est mort à l'arrivée. Un transporteur remet un cahier des charges de 47 pages ; un ingénieur se rend sur le site, demande au répartiteur ce qu'il fait en premier le lundi matin, et une alerte Slack construite en quatre heures règle le besoin. Règle : le client décrit une solution, le FDE retrouve le problème, et toute correction de moins d'une journée se livre sans débat. Une ingénieure qualité bloque une migration vers Parquet parce qu'elle vérifie les CSV d'un double-clic ; une visionneuse écrite dans la nuit débloque tout et le pipeline passe de 17 à 2 heures. Ganesh en tire une liste de signaux d'observation, invisibles dans toute documentation.

Il traite ensuite le vocabulaire : un même client désigné par quatre mots casse les intégrations. Le FDE fixe les noms et les verbes ; l'ontologie de Palantir est née de ce travail, et celui qui fixe le langage devient la fondation des solutions suivantes. SFEIR note que l'argument décrit une stratégie d'enfermement. Enfin, un script Groovy provisoire, toujours en production un an plus tard, donne cinq questions à se poser avant de livrer et une règle : livrer comme si le code devait tourner dix-huit mois.

Limites relevées : le talk raconte Palantir plus que Kepler, et les chiffres viennent de souvenirs. Verdict : originalité 4/5, qualité de l'information 5/5.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | critique FDE Kepler Vinoo Ganesh | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| critique FDE Kepler Vinoo Ganesh | DOCUMENT | référence | AI Engineer World's Fair 2026 | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| Vinoo Ganesh | PERSONNE | dirige | Kepler | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Vinoo Ganesh | PERSONNE | a_créé | Project Frontline | METHODOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Project Frontline | METHODOLOGIE | fait_partie_de | Palantir | ORGANISATION | 0.85 | STATIQUE | déclaré_article |
| Vinoo Ganesh | PERSONNE | s_inspire_de | Shyam Sankar | PERSONNE | 0.86 | STATIQUE | déclaré_article |
| Vinoo Ganesh | PERSONNE | affirme_que | le FDE relève de la stratégie produit et se juge à ce qu'il a fait entrer dans le produit | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Vinoo Ganesh | PERSONNE | affirme_que | "What's the first thing you do with this information Monday morning?" | CITATION | 0.88 | ATEMPOREL | déclaré_article |
| Forward Deployed Engineering | METHODOLOGIE | s_oppose_à | architecte solutions | CONCEPT | 0.8 | ATEMPOREL | déclaré_article |
| Forward Deployed Engineering | METHODOLOGIE | permet | ontologie | CONCEPT | 0.82 | STATIQUE | déclaré_article |
| Vinoo Ganesh | PERSONNE | mesure | pipeline passé d'environ 17 h à 2 h après une visionneuse Parquet écrite en une nuit | MESURE | 0.85 | STATIQUE | déclaré_article |
| Vinoo Ganesh | PERSONNE | recommande | livrer tout code comme s'il devait tourner dix-huit mois | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Vinoo Ganesh | PERSONNE | recommande | livrer sans débat toute correction de moins d'une journée | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| Vinoo Ganesh | PERSONNE | affirme_que | celui qui fixe le langage du client devient la fondation des solutions suivantes | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | s_oppose_à | verrouillage du client par le langage | CONCEPT | 0.8 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Vinoo Ganesh | PERSONNE | rôle | Cofondateur et CEO de Kepler ; sept ans chez Palantir ; programme FDE chez Citadel | AJOUT |
| Kepler | ORGANISATION | statut | Start-up où Vinoo Ganesh construit la fonction FDE | AJOUT |
| Project Frontline | METHODOLOGIE | définition | Programme de rotation Palantir transformant des ingénieurs logiciels en FDE (~350 personnes) | AJOUT |
| Shyam Sankar | PERSONNE | rôle | CTO de Palantir | AJOUT |
| verrouillage du client par le langage | CONCEPT | définition | Le fournisseur qui fixe le vocabulaire du client devient la fondation de ses solutions | AJOUT |
| critique FDE Kepler Vinoo Ganesh | DOCUMENT | notes SFEIR | Originalité 4/5, qualité de l'information 5/5 | AJOUT |
