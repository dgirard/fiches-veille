---
themes: [architecture-construction, transformation-adoption, qualite-securite]
source: SFEIR
---
# sfeir-hfsql-postgresql-migration-donnees-2026-10-15

## Veille

Article méthodologique **SFEIR** (non signé) publié sur sfeir.com le **15 octobre 2026** (~7 000 signes, six étapes, un schéma, quatre sources), rattaché au pilier *software factory* et à la série consacrée à la **migration WinDev**. Point de départ : une base **HFSQL** migrée vers **PostgreSQL** peut *« afficher le bon nombre de lignes dans chaque table et contenir de mauvaises données »*. Trois apports. **(A)** Une table de correspondance des types (montants en `numeric`, jamais en flottant ; dates vides ou `00000000` à interpréter ; séquences d'identifiants à recaler). **(B)** La déclaration des **clés étrangères implicites**, que le code WinDev garantissait « plus ou moins », ce qui fait remonter orphelins et doublons dès la première migration à blanc ; le métier décide (corriger, archiver, tolérer), le script applique. **(C)** Un **rapport de conformité à quatre niveaux** (volumétrie, intégrité, contenu, sens métier) répété jusqu'à **deux rapports consécutifs sans écart**, puis une **phase transitoire** où l'application WinDev existante tourne sur PostgreSQL pendant la réécriture. L'article recense aussi les offres du marché (BTBSofting, Provence Cloud, Dev-Booster, Sealog). Fait partie d'une série SFEIR sur la modernisation WinDev publiée le même jour.

## Titre Article

HFSQL vers PostgreSQL : migrer les données d'une application WinDev sans perte

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/hfsql-vers-postgresql-migration-donnees/

## Keywords

HFSQL, PostgreSQL, WinDev, migration de données, modernisation legacy, software factory, correspondance des types, clés étrangères implicites, intégrité référentielle, orphelins, doublons, nettoyage des données, migration à blanc, rapport de conformité, sommes de contrôle, sens métier, phase transitoire, accès natifs, golden master, bascule, synchronisation des deltas, retour arrière, Cloud SQL, AlloyDB, Google Cloud, MVCC, UniDataTransfer, Sealog

## Authors

SFEIR AI (article non signé), voix éditoriale de SFEIR publiée sur sfeir.com, site éditorial du cabinet.

## Ton

**Profil** : guide pratique de cabinet, à la première personne du pluriel (« notre méthode », « nous déclarons »), destiné aux DSI et responsables d'applications WinDev qui préparent une sortie d'HFSQL. Français technique, sans jargon superflu, appuyé sur un tableau, une figure et une FAQ.

**Style** : progression en six étapes numérotées, chacune ramenée à une décision concrète. Les points de vigilance sont placés à côté de chaque type ou de chaque étape plutôt que regroupés. Les sources externes (Sealog surtout) sont citées entre guillemets pour appuyer deux choix : déclarer les clés et passer par une phase transitoire.

**Position épistémique** : le critère de validation est formulé de manière vérifiable (*« quand les chiffres tombent juste, au centime »*, deux rapports consécutifs sans écart). La section marché cite des prix affichés à une date donnée (199,99 € HT en octobre 2026) et précise ce qui n'est pas public. Le texte borne le périmètre des outils tiers : ils couvrent la donnée, pas l'application ni les décisions sur les anomalies.

## Pense-betes

- **Risque central** : volumétrie juste, contenu faux (factures sans client, doublons tolérés par HFSQL, dates vides).
- **Pourquoi PostgreSQL** : libre, sans redevance, MVCC (lectures non bloquantes), managé partout ; sur Google Cloud, **Cloud SQL pour PostgreSQL** par défaut, **AlloyDB** si le workload le justifie.
- **Correspondance des types** :
  - chaîne → `varchar(n)`/`text` (encodage ANSI ou Unicode)
  - numérique/monétaire → `numeric(p,s)`, **jamais de flottant**
  - date/heure → `date`/`time`/`timestamp` (dates `00000000`)
  - booléen → `boolean` (valeurs historiques en entier)
  - mémo binaire → `bytea` ou stockage objet
  - identifiant auto → `bigint generated always as identity`, séquences à recaler
- **Clés implicites** : Sealog, *« parfois implicites ou gérées de façon non stricte par l'application »* → les déclarer dans PostgreSQL.
- **Nettoyage = livrable** : anomalies par table, règle appliquée, validation ; un agent classe et propose, le responsable métier choisit.
- **Rapport de conformité à 4 niveaux** : volumétrie, intégrité, contenu (checksums, échantillons), **sens métier** (totaux factures, soldes, stocks recalculés). Base source en lecture seule.
- **Critère d'arrêt** : deux rapports consécutifs sans écart ; la durée de la dernière migration à blanc fixe la fenêtre de bascule.
- **Phase transitoire** : WinDev sur PostgreSQL via accès natifs ; les deux applications partagent la base ; vigilance sur le SQL HFSQL écrit à la main.
- **Bascule** : migration initiale + synchronisation des deltas ; retour arrière écrit et testé avant le jour J.
- **Marché** : UniDataTransfer (BTBSofting) 199,99 € HT ; Provence Cloud (audit déduit, migration non facturée en cas d'échec) ; Dev-Booster (outil maison multi-cibles) ; Sealog (outil écrit en WinDev).
- **À relier** : [[sfeir-migration-windev-stack-cible-2026-10-15]], [[sfeir-migration-windev-software-factory-10x-2026-10-15]].

## RésuméDe400mots

L'article de SFEIR décrit une méthode pour migrer la base HFSQL d'une application WinDev vers PostgreSQL sans perte. Il part d'un constat : une migration peut restituer le bon nombre de lignes par table et contenir pourtant de mauvaises données, comme des factures sans client, des doublons que l'ancien moteur tolérait ou des dates vides.

Le choix de PostgreSQL est justifié par sa licence libre, son accessibilité depuis tous les langages et outils de BI, son modèle de concurrence MVCC et sa disponibilité en service managé ; sur Google Cloud, Cloud SQL pour PostgreSQL couvre la plupart des applications de gestion et AlloyDB prend le relais pour les charges plus lourdes.

La méthode comporte six étapes. La première transpose le schéma généré par l'éditeur d'analyses de WinDev en décidant explicitement chaque type : montants en numeric et jamais en flottant, dates vides à interpréter, identifiants automatiques convertis en colonnes d'identité dont les séquences sont recalées après import. La deuxième rend explicites les clés étrangères que le code garantissait de manière plus ou moins fiable ; leur déclaration fait remonter orphelins, doublons et valeurs hors domaine, et chaque anomalie appelle une décision métier. La troisième traite le nettoyage comme un livrable, avant la migration : un agent classe les anomalies et propose des règles de correction, le responsable métier choisit.

La quatrième étape répète des migrations à blanc sur une copie, la base d'origine restant en lecture seule. Chacune produit un rapport de conformité à quatre niveaux : volumétrie, intégrité, contenu par sommes de contrôle, et sens métier par recalcul des totaux de factures, soldes et stocks. La migration est validée quand les chiffres tombent juste au centime, après deux rapports consécutifs sans écart ; la durée de la dernière fixe la fenêtre de bascule.

La cinquième étape, souvent omise selon l'article, fait tourner l'application WinDev existante sur PostgreSQL par ses accès natifs pendant la réécriture : l'entreprise sort d'HFSQL sans attendre, les deux applications partagent la base, et le golden master compare des écritures dans le même moteur. Le SQL propre à HFSQL écrit à la main reste un point de vigilance. La sixième étape est la bascule, avec synchronisation des deltas et procédure de retour arrière testée.

L'article recense enfin les outils et prestations du marché (UniDataTransfer, Provence Cloud, Dev-Booster, Sealog), en précisant qu'ils couvrent la donnée mais pas l'application ni les décisions sur les anomalies, et répond à quelques questions fréquentes (HFSQL Classic, nombre de migrations à blanc, MySQL ou SQL Server).

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | HFSQL vers PostgreSQL : migrer les données d'une application WinDev sans perte | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | a_créé | méthode de migration HFSQL vers PostgreSQL en six étapes | METHODOLOGIE | 0.93 | STATIQUE | déclaré_article |
| méthode de migration HFSQL vers PostgreSQL en six étapes | METHODOLOGIE | s_applique_à | WinDev | TECHNOLOGIE | 0.94 | ATEMPOREL | déclaré_article |
| PostgreSQL | TECHNOLOGIE | remplace | HFSQL | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| HFSQL | TECHNOLOGIE | fait_partie_de | WinDev | TECHNOLOGIE | 0.88 | ATEMPOREL | inféré |
| SFEIR | ORGANISATION | recommande | déclarer dans PostgreSQL les clés étrangères que le code WinDev gardait implicites | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Sealog | ORGANISATION | affirme_que | les clés de HFSQL sont parfois implicites ou gérées de façon non stricte par l'application | CITATION | 0.9 | ATEMPOREL | déclaré_article |
| méthode de migration HFSQL vers PostgreSQL en six étapes | METHODOLOGIE | utilise | rapport de conformité à quatre niveaux | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| méthode de migration HFSQL vers PostgreSQL en six étapes | METHODOLOGIE | utilise | migration à blanc | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | répéter les migrations à blanc jusqu'à deux rapports consécutifs sans écart | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| méthode de migration HFSQL vers PostgreSQL en six étapes | METHODOLOGIE | utilise | phase transitoire WinDev sur PostgreSQL | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| phase transitoire WinDev sur PostgreSQL | METHODOLOGIE | permet | golden master | METHODOLOGIE | 0.82 | ATEMPOREL | déclaré_article |
| phase transitoire WinDev sur PostgreSQL | METHODOLOGIE | s_inspire_de | Sealog | ORGANISATION | 0.8 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | Cloud SQL pour PostgreSQL | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| AlloyDB | TECHNOLOGIE | est_variante_de | PostgreSQL | TECHNOLOGIE | 0.8 | ATEMPOREL | inféré |
| BTBSofting | ORGANISATION | publie | UniDataTransfer | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| UniDataTransfer | TECHNOLOGIE | mesure | 199,99 € HT la licence perpétuelle mono-poste en octobre 2026 | MESURE | 0.85 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle, éditeur de sfeir.com | AJOUT |
| HFSQL | TECHNOLOGIE | catégorie | Moteur de base de données de l'écosystème WinDev (Classic et Client/Serveur) | AJOUT |
| WinDev | TECHNOLOGIE | catégorie | AGL propriétaire (PC SOFT) ciblé par les migrations | AJOUT |
| PostgreSQL | TECHNOLOGIE | rôle | Cible par défaut : libre, MVCC, managé sur tous les clouds | AJOUT |
| méthode de migration HFSQL vers PostgreSQL en six étapes | METHODOLOGIE | étapes | Schéma, clés explicites, nettoyage, migrations à blanc, WinDev sur PostgreSQL, bascule | AJOUT |
| rapport de conformité à quatre niveaux | METHODOLOGIE | niveaux | Volumétrie, intégrité, contenu, sens métier | AJOUT |
| migration à blanc | METHODOLOGIE | règle | Sur copie, source en lecture seule, répétée jusqu'à deux rapports sans écart | AJOUT |
| phase transitoire WinDev sur PostgreSQL | METHODOLOGIE | rôle | Sortir d'HFSQL avant la fin de la réécriture, base partagée | AJOUT |
| Sealog | ORGANISATION | position | Recommande la phase transitoire et un outil de migration écrit en WinDev | AJOUT |
| Cloud SQL pour PostgreSQL | TECHNOLOGIE | usage | Service managé Google Cloud pour la plupart des applications de gestion | AJOUT |
| AlloyDB | TECHNOLOGIE | usage | Relais pour workloads analytiques ou transactionnels plus lourds | AJOUT |
