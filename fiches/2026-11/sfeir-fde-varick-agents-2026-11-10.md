---
themes: [transformation-adoption, architecture-construction]
source: SFEIR
---
# sfeir-fde-varick-agents-2026-11-10

## Veille

Critique éditoriale **SFEIR AI** publiée sur sfeir.com le **10 novembre 2026**, dans la série de neuf retours sur la playlist *forward deployed engineering* de l'**AI Engineer World's Fair 2026**. Elle porte sur « AI tools for Forward Deployed Engineering », talk de **Varick Agents** en deux temps, 20 min 23, ~**28 100** vues. **(A)** Douze minutes de **Vasuman Moza**, fondateur et CEO : cartographier le travail réel et ses exceptions, redessiner le processus sans le bouleverser (sur huit étapes, quatre automatisées, trois validées par un humain, une humaine), déployer des agents par-dessus **NetSuite**, Dynamics, SAP ou Salesforce via **Varick OS** ; ROI de 25 à 75 % annoncés sans définition. **(B)** Six minutes de **JD**, responsable plateforme, sur l'agent interne des FDE en trois étages (engagement, workflow, autonome — ce dernier non construit) : chaque entreprise cliente représentée en **graphe de dépendances** sur **Postgres**, modèles open source post-entraînés (un modèle **Kimi** de Moonshot AI), environnement d'**apprentissage par renforcement** pour parcourir le graphe et résoudre les entités. L'article relève que la démonstration contredit l'affirmation du CEO selon laquelle le travail intellectuel serait *« presque résolu »*. Notes SFEIR : **4/5** et **3/5**.

## Titre Article

Varick Agents construit un agent pour ses FDE, et la démonstration technique sauve le talk

## Date

2026-11-10

## URL

https://www.sfeir.com/articles/fde-varick-agents-outils-ia/

## Keywords

forward deployed engineering, FDE, Varick Agents, Vasuman Moza, Varick OS, AI Engineer World's Fair 2026, outils IA pour FDE, agent FDE, agent d'engagement, agent de workflow, graphe de dépendances, résolution d'entités, Postgres, post-entraînement, modèles open source, Kimi, Moonshot AI, apprentissage par renforcement, Granola, NetSuite, SAP, Salesforce, Dynamics, comptes fournisseurs, finance, redesign de processus, ROI, étude MIT 95 %, ESN, critique de talk

## Authors

SFEIR AI (voix éditoriale non signée), sfeir.com, site éditorial de SFEIR. Critique du talk de Vasuman Moza et JD (Varick Agents).

## Ton

Critique de talk au format fixe de la série SFEIR (encadré, minutages, « Une contradiction instructive », « Pour une ESN », verdict noté). Registre contrasté : l'article traite séparément les deux orateurs, juge la première moitié conforme au *« discours ambiant »* (ROI sans définition, un chiffre de 87 % non attribué) et la seconde *« précise et franche sur ce qui ne marche pas »*. Il retient le seul talk de la série consacré à l'outillage du FDE lui-même. Public : équipes qui outillent des consultants ou des FDE avec des agents.

## Pense-betes

- **Format** : 20 min 23, mis en ligne le 28 juillet 2026, ~28 100 vues ; 12 min de Moza puis 6 min de JD.
- **Anecdote d'ouverture** : un client a dépensé 5 M$ et cinq ans pour migrer vers NetSuite → Varick déploie par-dessus l'existant, sans nouvelle migration.
- **Discours de Moza** : modèles et harnais savent exécuter le travail ; goulot = compréhension du fonctionnement réel de l'entreprise ; travail intellectuel « presque résolu ».
- **Méthode FDE (vers 4:04)** : cartographier le travail humain et ses exceptions (écart bon de commande / facture → 4 jours de plus) ; ne pas remplacer onze étapes par une seule (adoption en chute) ; sur huit étapes : 4 automatisées, 3 avec validation humaine, 1 humaine.
- **Chiffres contestés** : ROI 5-10 % des solutions ponctuelles vs 25/50/75 % des transformations de départements, sans définition ni client ; étude MIT (95 % des pilotes d'IA générative sans production) ; un 87 % non attribué.
- **Constat de JD (vers 12:15)** : 150 pages de documentation dans Claude → analyse *« verbose and incorrect and it kind of sucks »*.
- **Agent FDE en trois étages** : engagement (ingère notes Granola, docs, présentations ; répond « qui est responsable ? », « la Sarah de cet e-mail est-elle celle de ce message Slack ? ») ; workflow (signale le cas limite oublié) ; autonome (petites demandes de changement) — pas encore construit.
- **Architecture (vers 15:18)** : graphe de dépendances par entreprise (processus surtout linéaires, avec boucles) ; « Postgres suffit » ; post-entraînement de modèles open source car les modèles frontières sont trop verbeux et sans instinct de consultant ; environnement RL avec outils : deux « Mike » identiques ? cycles redondants ? violations du DAG ?
- **Pour une ESN** : Varick vise plusieurs clients par FDE ; idée transposable = graphe de l'organisation cliente alimenté par les notes de réunion.
- **Verdict** : 4/5 et 3/5 ; à regarder à partir de 12:15.

## RésuméDe400mots

SFEIR AI publie le 10 novembre 2026 une critique de « AI tools for Forward Deployed Engineering », talk de Varick Agents à l'AI Engineer World's Fair 2026. La start-up dit transformer des départements entiers de grandes entreprises, la finance servant d'exemple, ce qui exige beaucoup de forward deployed engineering. Le talk se coupe en deux : douze minutes de Vasuman Moza, fondateur et CEO, puis six minutes de JD, responsable de l'équipe plateforme.

Moza part d'un client qui a dépensé 5 millions de dollars et cinq ans pour migrer vers NetSuite, pour justifier le choix de déployer des agents par-dessus les systèmes existants. Il affirme que les modèles et leurs harnais savent désormais exécuter le travail et que le travail intellectuel est presque résolu ; le goulot devient la compréhension du fonctionnement réel d'une entreprise. Le FDE de Varick cartographie donc le travail humain et ses exceptions, puis redessine le processus sans le bouleverser : sur huit étapes, quatre automatisées, trois validées par un humain, une entièrement humaine. Les agents se déploient au-dessus de NetSuite, Dynamics, SAP ou Salesforce via Varick OS. SFEIR relève ensuite des ROI de 25 à 75 % sans définition ni client, et un chiffre de 87 % sans source.

JD raconte l'origine de l'outil : les FDE chargeaient 150 pages de documentation dans Claude et obtenaient une analyse bavarde et fausse. Varick a construit un agent en trois étages : un agent d'engagement qui ingère notes de réunion, documentation et présentations pour répondre aux questions quotidiennes des FDE ; un agent de workflow qui signale les cas limites oubliés ; un agent autonome pour les petites demandes de changement, qui n'existe pas encore. L'architecture représente chaque entreprise par un graphe de dépendances stocké dans Postgres, post-entraîne des modèles open source comme un modèle Kimi de Moonshot AI, et utilise un environnement d'apprentissage par renforcement pour apprendre au modèle à parcourir le graphe : résolution d'entités, cycles redondants, violations du graphe acyclique.

L'article souligne la contradiction : le CEO annonce le travail intellectuel résolu, l'ingénieur montre qu'une synthèse de dossier résiste aux modèles frontières. Pour une ESN, l'idée à reprendre est le graphe de l'organisation cliente, interrogeable par toute l'équipe de mission. Verdict : originalité 4/5, qualité de l'information 3/5.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | critique FDE Varick Agents | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| critique FDE Varick Agents | DOCUMENT | référence | AI Engineer World's Fair 2026 | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| Vasuman Moza | PERSONNE | dirige | Varick Agents | ORGANISATION | 0.93 | DYNAMIQUE | déclaré_article |
| Varick Agents | ORGANISATION | a_créé | Varick OS | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Varick Agents | ORGANISATION | utilise | Forward Deployed Engineering | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Vasuman Moza | PERSONNE | affirme_que | le travail intellectuel est presque résolu | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| Vasuman Moza | PERSONNE | recommande | automatiser une partie seulement des étapes d'un processus et garder des validations humaines | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| Varick Agents | ORGANISATION | a_créé | agent FDE de Varick | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| agent FDE de Varick | TECHNOLOGIE | utilise | graphe de dépendances de l'entreprise cliente | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| agent FDE de Varick | TECHNOLOGIE | utilise | PostgreSQL | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| agent FDE de Varick | TECHNOLOGIE | utilise | Kimi | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| agent FDE de Varick | TECHNOLOGIE | utilise | apprentissage par renforcement | METHODOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| agent FDE de Varick | TECHNOLOGIE | résout | résolution d'entités | CONCEPT | 0.84 | DYNAMIQUE | déclaré_article |
| Varick Agents | ORGANISATION | affirme_que | les modèles frontières produisent des analyses de dossiers client trop longues et fausses | AFFIRMATION | 0.84 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | s_oppose_à | ROI de 25 à 75 % annoncés sans définition ni client | AFFIRMATION | 0.84 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Vasuman Moza | PERSONNE | rôle | Fondateur et CEO de Varick Agents | AJOUT |
| Varick Agents | ORGANISATION | secteur | Agents déployés par-dessus les ERP/CRM pour transformer des départements entiers (finance) | AJOUT |
| Varick OS | TECHNOLOGIE | catégorie | Plateforme maison de déploiement d'agents de Varick | AJOUT |
| agent FDE de Varick | TECHNOLOGIE | architecture | Trois étages (engagement, workflow, autonome non construit) ; graphe sur Postgres ; modèles open source post-entraînés ; RL | AJOUT |
| graphe de dépendances de l'entreprise cliente | CONCEPT | définition | Représentation des processus métier (linéaires avec boucles), interrogeable par l'équipe de mission | AJOUT |
| critique FDE Varick Agents | DOCUMENT | notes SFEIR | Originalité 4/5, qualité de l'information 3/5 | AJOUT |
