---
themes: [architecture-construction, qualite-securite]
source: SFEIR
---
# sfeir-base-connaissances-site-conversationnel-2026-11-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 novembre 2026**, deuxième volet de la série sur le site conversationnel de sfeir.com. Il décrit la base de connaissances qui sous-tend la conversation : des **fichiers YAML versionnés dans Git**, une notion par fichier, **363 fiches** au 13 novembre 2026 (126 concepts, 126 technologies, 10 méthodologies, 101 personnes). **(1)** La règle *« une notion, une fiche »* : la fiche déclare ses relations (articles, expertises, offres, formations) et le build calcule l'inverse ; **305 fiches** déclarent au moins un article. **(2)** La croissance par à-coups, d'avril (94 fiches) à novembre, au rythme des chantiers éditoriaux. **(3)** Le sourcing : fin août, **131 fiches** indexables sans source ; onze vagues de dix traitées du 26 au 28 août selon une procédure en huit étapes, dont l'étape *chercher le faux déjà en ligne*, jugée la plus rentable. Règle **R13** : *« une fiche courte et exacte est un résultat valide ; une fiche au bon volume portant une donnée fausse est un échec »*. **(4)** L'hygiène des alias du lien automatique. Le verdict : *« la conversation vaut ce que vaut la base »*. Le dispositif rejoint, par sa structure, l'architecture médaillon de ce dépôt de veille, que l'article cite (raw, bronze, silver, gold).

## Titre Article

Base de connaissances : le chantier invisible derrière un site conversationnel

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/base-de-connaissances-site-conversationnel/

## Keywords

base de connaissances, site conversationnel, fiche YAML, une notion une fiche, Git, schéma validé au build, relations déclarées, relation inverse, alias, lien automatique, sourcing, source primaire, vérification, chercher le faux, règle R13, DefinedTerm, schema.org, llms.txt, Forward Deployed Engineer, Michel Serres, médaillon, SFEIR

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article de pratique, récit de l'intérieur d'un chantier éditorial, publié par un cabinet sur son propre site. Public déclaré : DSI et direction marketing, secondairement CTO.

**Style** : factuel et daté au jour près, un fil rouge (la fiche Forward Deployed Engineer) suivi de section en section, un tableau mensuel de croissance, une figure « une fiche écrite une fois, lue par cinq surfaces ». Les erreurs sont racontées avec leurs chiffres : l'alias « CHANGE » qui liait le verbe dans 17 pages, l'article pilier SDLC arrivé treizième, la citation apocryphe de Michel Serres.

**Position épistémique** : l'article se borne à son propre cas (« il ne compare pas les outils du marché ») et termine par une section « ce que la base ne règle pas » : entretien continu, fiches sans source, décisions commerciales humaines, base en français. Les chiffres viennent du dépôt et du contrôle de santé lancé au build.

## Pense-betes

- **Format d'une fiche** : YAML, une phrase de définition, alias, corps en sections, FAQ si questions réelles, sources avec adresse, relations déclarées. Un schéma valide au build : champ mal formé, lien vers une offre inexistante, source sans adresse **bloquent** ; fiche sans source **passe mais est signalée**. Indexable à partir de 300 mots (313 sur 363).
- **Une notion, une fiche** : la définition du FDE n'existe qu'une fois ; sa page, le chat, les données structurées la reprennent. Le lien automatique fait pointer la première mention vers la fiche.
- **Relations à sens unique** : ce sont les fiches qui déclarent les articles, le build inverse (sujet `about` dans les données structurées). La fiche FDE déclare 21 articles ; 106 fiches de technologies rattachées aux expertises le 29 octobre ; 26 fiches reliées aux cours de SFEIR Institute le 30 octobre.
- **Croissance** : 94 fiches en avril, 3 en mai, 17 en juin, 78 en juillet, 14 en août, 53 en septembre, 79 en octobre, 21 au 13 novembre.
- **Procédure de sourcing en 8 étapes** : archiver le dossier, vérifier chaque fait mouvant en source primaire, chercher le faux déjà publié, rédiger, retirer les tics d'écriture des modèles, valider, construire, déployer. La recherche se délègue, la vérification jamais.
- **L'étape la plus rentable** : sur trois vagues, cinq affirmations périmées corrigées (statut réglementaire, versions de modèles, périmètre d'outils). Exemple : « notre tête est dans nos mains », attribué à Michel Serres, absent de *Petite Poucette*.
- **La mesure corrigée** : le contrôle ne comptait que les fiches de moins de 300 mots ; 21 fiches longues non sourcées échappaient (dont FDE, 801 mots). Depuis le 27 août, critère = présence de sources. Au 13 novembre : 277 fiches sourcées, 2 053 sources ; 37 fiches de doctrine interne non sourçables de l'extérieur.
- **Hygiène des alias** : le lien ignore la casse, donc un alias courant lie tout. Alias réduits à leurs formes qualifiées ; un pluriel est un terme distinct ; lien automatique dans les articles limité à 62 notions sans ambiguïté.
- **Ordre des articles dans le chat** : depuis le 10 novembre, les articles dont le titre nomme la fiche passent devant (cas SDLC, 28 autres fiches concernées). Aucun modèle ne choisit les pages : la fiche déclare, des règles ordonnent.
- **Par rôle** : DSI, mesurer l'état des contenus avant le modèle (*« le modèle se change en une ligne de configuration ; la base demande des mois »*).

## RésuméDe400mots

Deuxième article de la série consacrée à sfeir.com, ce texte décrit la base de connaissances sur laquelle repose la conversation lancée en novembre 2026. Sa thèse : la conversation vaut ce que vaut la base, et la base a moins gagné à grossir qu'à corriger ce qu'elle affirmait de faux.

La base tient dans des fichiers texte versionnés dans Git. Chaque fiche est un fichier YAML consacré à une notion : une phrase de définition, des alias, un corps en sections, une FAQ éventuelle, des sources avec leur adresse et les relations que la fiche déclare vers les articles, expertises, offres et formations. Un schéma valide chaque fichier au build ; une source sans adresse ou un lien vers une offre inexistante bloque la publication, une fiche sans source est seulement signalée. Au 13 novembre 2026, la base compte 363 fiches, dont 313 indexables.

La règle centrale est « une notion, une fiche ». La définition du Forward Deployed Engineer, exemple suivi tout au long de la série, n'est écrite qu'une fois et reprise par sa page, le chat, les articles et les données structurées. Les relations ne sont déclarées que dans un sens, par la fiche ; le build calcule l'inverse. 305 fiches déclarent au moins un article.

La base a grandi par à-coups, au rythme des chantiers éditoriaux : 94 fiches en avril, 78 en juillet, 79 en octobre. Fin août, 131 fiches indexables n'avaient aucune source. Le sourcing s'est alors organisé par vagues de dix, selon une procédure en huit étapes où la recherche documentaire se délègue mais où la vérification en source primaire reste interne. L'étape jugée la plus rentable consiste à chercher ce que la fiche affirme déjà de faux : elle a corrigé des affirmations périmées et une citation apocryphe de Michel Serres. La règle R13 prime : rien d'inventé. Le contrôle lui-même a été corrigé, après la découverte de 21 fiches longues non sourcées qui échappaient au compte.

L'article décrit aussi l'hygiène des alias du lien automatique, qui ignore la casse : l'alias « CHANGE » liait le verbe dans 17 pages. Dans le chat, les pages affichées sont déclarées par la fiche et ordonnées par des règles, sans choix par un modèle.

Les limites sont posées : entretien continu, fiches encore sans source, rattachements commerciaux décidés par une personne, base en français. Le conseil aux DSI : mesurer l'état des contenus avant de choisir un modèle.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | article Base de connaissances le chantier invisible | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | base de connaissances sfeir.com | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| base de connaissances sfeir.com | TECHNOLOGIE | utilise | YAML | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| base de connaissances sfeir.com | TECHNOLOGIE | utilise | Git | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| base de connaissances sfeir.com | TECHNOLOGIE | mesure | 363 fiches dont 313 indexables, 277 sourcées, 2 053 sources au 13 novembre 2026 | MESURE | 0.92 | STATIQUE | déclaré_article |
| fiche par notion | METHODOLOGIE | fait_partie_de | base de connaissances sfeir.com | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| procédure de sourcing en huit étapes | METHODOLOGIE | fait_partie_de | base de connaissances sfeir.com | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| procédure de sourcing en huit étapes | METHODOLOGIE | recommande | une fiche courte et exacte est un résultat valide ; une fiche au bon volume portant une donnée fausse est un échec | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | chercher le faux déjà en ligne est l'étape la plus rentable du sourcing | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la conversation vaut ce que vaut la base | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| relations déclarées dans un seul sens | METHODOLOGIE | résout | relations tenues à deux endroits | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | s_oppose_à | « notre tête est dans nos mains » attribué à Michel Serres | CITATION | 0.85 | STATIQUE | déclaré_article |
| Michel Serres | PERSONNE | a_créé | Petite Poucette | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| base de connaissances sfeir.com | TECHNOLOGIE | permet | site conversationnel | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | mesurer l'état des contenus avant de choisir un modèle | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| base de connaissances sfeir.com | TECHNOLOGIE | s_inspire_de | architecture médaillon | METHODOLOGIE | 0.75 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| base de connaissances sfeir.com | TECHNOLOGIE | composition | 126 concepts, 126 technologies, 10 méthodologies, 101 personnes (13/11/2026) | AJOUT |
| fiche par notion | METHODOLOGIE | principe | Une définition unique ; les pages, le chat et les données structurées la reprennent | AJOUT |
| procédure de sourcing en huit étapes | METHODOLOGIE | étapes | Archiver, vérifier en source primaire, chercher le faux, rédiger, détox, valider, construire, déployer | AJOUT |
| relations déclarées dans un seul sens | METHODOLOGIE | principe | La fiche déclare ses liens, le build calcule la relation inverse | AJOUT |
| Petite Poucette | DOCUMENT | référence | Michel Serres, Le Pommier, 2012 | AJOUT |
