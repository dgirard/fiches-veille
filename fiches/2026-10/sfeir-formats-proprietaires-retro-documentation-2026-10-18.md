---
themes: [architecture-construction, politique-regulation]
source: SFEIR
---
# sfeir-formats-proprietaires-retro-documentation-2026-10-18

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **18 octobre 2026** (~1 100 mots, trois sources), fiche du cluster SFEIR sur la rétro-ingénierie et le legacy sans code source, consacrée aux données enfermées dans un format de fichier maison. Il s'ouvre sur l'**arrêt SAS Institute** (CJUE, C-406/10, 2 mai 2012) : ni la fonctionnalité d'un programme, ni son langage, ni le format de ses fichiers de données ne sont une forme d'expression protégée par le droit d'auteur. Trois apports. **(A)** Le constat qu'une équipe peut réécrire écrans et traitements mais *« ne peut pas réécrire vingt ans de données »* : la rétro-documentation du format devient la première étape, avant le choix de la stack cible. **(B)** Le cadre juridique, nuancé : un format original reste protégeable comme œuvre (directive 2001/29/CE), le code qui lit le format relève de la décompilation (directive **2009/24/CE**, article L122-6-1 du CPI), le contournement d'une mesure technique d'autres règles encore. **(C)** Une méthode par **échantillons connus** : saisir des enregistrements qui ne diffèrent que d'une valeur, comparer octet par octet, cartographier la structure, écrire un parseur, le passer sur la production et traiter chaque rejet. L'agent et **REA** accélèrent les comparaisons ; *« Sans échantillons connus pour trancher, ses propositions restent des hypothèses. »* Prolonge, sur les données, la fiche SFEIR sur les risques de migration WinDev.

## Titre Article

Formats de fichiers propriétaires : rétro-documenter pour migrer les données

## Date

2026-10-18

## URL

https://www.sfeir.com/articles/formats-proprietaires-retro-documentation/

## Keywords

format de fichier propriétaire, format binaire non documenté, rétro-documentation, migration de données, legacy, éditeur disparu, arrêt SAS Institute, CJUE C-406/10, droit d'auteur, directive 2001/29/CE, directive 2009/24/CE, article L122-6-1, décompilation, interopérabilité, mesure technique de protection, échantillons connus, comparaison octet par octet, en-têtes, décalages, encodage, parseur, rejets, REA, SQLite, migrations à blanc, rapport de conformité, HFSQL, PostgreSQL, Software Factory

## Authors

SFEIR AI (voix éditoriale du cabinet), article non signé individuellement — sfeir.com, site éditorial de SFEIR.

## Ton

Profil : fiche méthodologique d'une ESN, en français, adressée aux DSI et équipes de migration confrontées à des données dans un format non documenté. L'ouverture est juridique (un arrêt daté et numéroté), le corps est procédural : constituer des échantillons, cartographier, écrire un parseur, traiter les rejets. Le ton est prudent sur le droit — réserves successives (format original, code qui lit le format, mesure technique), renvoi systématique au juriste, encadré « pas un conseil juridique » — et précis sur la technique (en-têtes, longueurs, décalages, encodage des dates). Le rôle de l'agent est circonscrit : accélérer un travail répétitif, proposer une structure, sous vérification par échantillon. FAQ en réponses courtes ; conclusion sur l'offre Software Factory et ses rapports de conformité.

## Pense-betes

- **Arrêt SAS Institute** (CJUE, **C-406/10**, 2 mai 2012) : fonctionnalité, langage de programmation et **format des fichiers de données** ne sont pas des formes d'expression du programme protégées par le droit d'auteur.
- **Réserves** : un format **original** peut être protégé comme œuvre (directive **2001/29/CE**) ; le **code** qui lit/écrit le format reste protégé ; décompiler ce code = régime de la directive **2009/24/CE** / **L122-6-1 CPI** ; format chiffré ou protégé par mesure technique = autres règles → juriste.
- **Terrain le plus sûr** : étudier des **fichiers de données que vous possédez** plutôt que décompiler le programme.
- **Blocage type** : fichiers binaires maison, exports au format connu du seul éditeur, configurations chiffrées artisanalement ; fréquent sur stacks legacy et éditeurs disparus.
- **Méthode par échantillons connus** :
  1. saisir des enregistrements choisis (nom plus long, autre date, montant négatif, champ vide), **une seule valeur change** à chaque fois ;
  2. comparer **octet par octet** ;
  3. cartographier en-têtes, longueurs, décalages, types numériques, encodage des chaînes et dates, index ;
  4. écrire un **parseur**, le valider sur les fichiers de référence, le passer sur la production ;
  5. traiter les **rejets** un par un (type rare, ancienne version du format, corruption), avec les utilisateurs si besoin.
- **Agent / REA** : compare des dizaines de fichiers, propose une structure, l'écrit en spécification ; REA inspecte fichiers et bases **SQLite**, pilote un décompilateur si l'on doit voir comment l'application lit le format. Un champ inféré d'un motif = hypothèse tant qu'un échantillon ne l'a pas confirmé.
- **Après** : migration comme un changement de base (structure transposée, règles implicites explicitées, nettoyage, **migrations à blanc** jusqu'à rapport de conformité sans écart) — cf. HFSQL → PostgreSQL.

## RésuméDe400mots

Cet article de SFEIR, publié le 18 octobre 2026, traite d'un obstacle fréquent des projets de modernisation : les données conservées dans un format de fichier propriétaire et non documenté. Il s'ouvre sur un arrêt de la Cour de justice de l'Union européenne, SAS Institute, rendu le 2 mai 2012, selon lequel ni la fonctionnalité d'un programme, ni son langage, ni le format de ses fichiers de données ne constituent une forme d'expression protégée par le droit d'auteur. Pour SFEIR, cette décision fonde la possibilité de comprendre un format pour en extraire ses propres données.

Le blocage décrit est le suivant : une équipe peut réécrire des écrans et des traitements, mais pas vingt ans de données, qui doivent passer d'un système à l'autre sans perte. La question reste technique tant que le format est documenté ou lu par un pilote standard ; elle devient bloquante avec des fichiers binaires maison, des exports connus du seul éditeur ou des configurations chiffrées de façon artisanale, cas fréquent quand l'éditeur a disparu. La rétro-documentation du format devient alors la première étape, avant même le choix de la cible.

Le cadre juridique est présenté avec ses nuances. Un format original peut être protégé comme œuvre ; le code qui lit et écrit le format reste protégé, et sa décompilation obéit aux règles de la directive de 2009 transposée dans le Code de la propriété intellectuelle. Étudier ses propres fichiers de données est un terrain plus sûr que décompiler le programme, et le contournement d'une protection technique relève d'autres règles. L'article renvoie chaque cas au juriste.

La méthode repose sur des échantillons connus. On saisit dans l'application d'origine des enregistrements qui ne diffèrent que d'une valeur, puis la comparaison octet par octet révèle où et comment chaque valeur est stockée. On cartographie ensuite en-têtes, longueurs, décalages, types et encodages, on écrit un parseur validé sur les fichiers de référence, puis on le passe sur la production en traçant chaque enregistrement rejeté. Ces rejets forment la liste des inconnues, traitées une à une. Un agent accélère ce travail répétitif et l'outil REA fournit des inspections de fichiers et de bases SQLite, mais chaque hypothèse se vérifie sur un fichier connu.

Une fois le format compris, la migration suit la logique d'un changement de base de données : transposition de la structure, explicitation des règles implicites, nettoyage et migrations à blanc répétées jusqu'à un rapport de conformité sans écart.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Formats de fichiers propriétaires : rétro-documenter pour migrer les données | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| arrêt SAS Institute | DOCUMENT | affirme_que | le format des fichiers de données n'est pas une forme d'expression protégée du programme | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| directive 2009/24/CE | DOCUMENT | s_applique_à | décompilation à des fins d'interopérabilité | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | étudier ses propres fichiers de données est un terrain plus sûr que décompiler le programme | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| rétro-documentation de format | METHODOLOGIE | fait_partie_de | migration de données | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| rétro-documentation de format | METHODOLOGIE | utilise | méthode par échantillons connus | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| méthode par échantillons connus | METHODOLOGIE | permet | cartographie de la structure d'un format binaire | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| rétro-documentation de format | METHODOLOGIE | utilise | REA | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | SQLite | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | sans échantillons connus, les propositions de structure d'un agent restent des hypothèses | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | valider le parseur sur des fichiers de référence puis tracer chaque rejet en production | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | rétro-documenter le format avant de choisir la stack cible | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| migration de données | METHODOLOGIE | utilise | migrations à blanc | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| migration de données | METHODOLOGIE | s_applique_à | PostgreSQL | TECHNOLOGIE | 0.75 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| arrêt SAS Institute | DOCUMENT | référence | CJUE, C-406/10, 2 mai 2012 | AJOUT |
| directive 2009/24/CE | DOCUMENT | objet | Protection juridique des programmes d'ordinateur (encadre la décompilation) | AJOUT |
| rétro-documentation de format | METHODOLOGIE | définition | Reconstitution de la spécification d'un format de fichier non documenté pour migrer les données | AJOUT |
| méthode par échantillons connus | METHODOLOGIE | étapes | Fichiers différant d'une valeur, comparaison octet par octet, parseur, traitement des rejets | AJOUT |
| REA | TECHNOLOGIE | catégorie | Serveur MCP de rétro-ingénierie (Reverse Engineer Anything) | AJOUT |
