---
themes: [architecture-construction, transformation-adoption, outils-plateformes]
source: SFEIR
---
# sfeir-migrer-webdev-windev-mobile-2026-10-16

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **16 octobre 2026** (~7 000 signes hors schéma, quatre sources notées), rattaché au guide SFEIR de la migration **WinDev**. Il traite les deux produits frères qui partagent le **WLangage**, **WebDev** et **WinDev Mobile**, et ce qui change par rapport au desktop. **(A)** WebDev : le **serveur d'application WEBDEV** est facturé par cœurs, mémoire et nombre de serveurs (vidéo PC SOFT analysée par Louis Planquart), Dev-Booster le chiffrant à **4 490 € HT/an** ; un site public impose un projet **SEO** (inventaire des URL, redirections **301**, suivi d'indexation) ; l'état de session se remplace par des API sans état ; les éditeurs peuvent viser une architecture **SaaS multi-tenant**, cible SFEIR Java/Spring + Angular sur **Google Cloud**. **(B)** WinDev Mobile : le cœur est le **hors ligne** et la **synchronisation** (fraîcheur, conflits, reprise sans doublon), illustré par NomadBiz chez Dev-Booster (SQLite, .NET MAUI / Blazor Hybrid) ; inventaire des terminaux et périphériques dès l'audit ; cible par défaut **Flutter**. **(C)** Ce qui ne change pas : extraction des règles, golden master inversé (enrichi de scénarios de synchronisation ou de parcours), données vers **PostgreSQL**. Volet de la série SFEIR sur la migration WinDev, publié le même jour que les articles sur le coût et les alternatives.

## Titre Article

Migrer WebDev et WinDev Mobile : sites, applications SaaS et applications terrain

## Date

2026-10-16

## URL

https://www.sfeir.com/articles/migrer-webdev-windev-mobile/

## Keywords

WebDev, WinDev Mobile, WinDev, WLangage, PC SOFT, serveur d'application WEBDEV, licence par cœurs, SEO, redirections 301, données structurées, sessions, API sans état, SaaS multi-tenant, Java, Spring, Angular, Google Cloud, Cloud SQL, AlloyDB, PostgreSQL, hors ligne, synchronisation, conflits, SQLite, .NET MAUI, Blazor Hybrid, Flutter, terminaux durcis, douchettes, PWA, golden master inversé

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé individuellement, publié sur sfeir.com.

## Ton

Profil : article technique de conseil d'une ESN, registre structuré et opérationnel, en français, public d'éditeurs et de DSI exploitant des sites WebDev ou des applications terrain WinDev Mobile. La construction est symétrique : une partie par produit, chacune découpée en sous-sujets techniques, puis une section commune « ce qui ne change pas » qui raccroche à la méthode générale de la série. Les listes à puces dominent (checklist SEO, questions de synchronisation). Les chiffres et citations sont attribués à des tiers (Planquart, Dev-Booster, Smartshift) avec leur date, et l'article distingue le choix d'un tiers (MAUI / Blazor Hybrid chez Dev-Booster) de sa propre recommandation (Flutter) en notant que la question de fond se pose à l'identique. Les préférences SFEIR sont énoncées comme telles (« notre cible privilégiée », « notre cible par défaut »). La FAQ traite les questions de praticien (référencement, découpage back-end / mobile, périphériques, PWA). Clôture sur le Diagnostic 10x et l'audit de patrimoine.

## Pense-betes

- **Point commun** : WebDev et WinDev Mobile partagent le **WLangage** avec WinDev ; la méthode générale de la série s'applique.
- **WebDev, coût serveur** : serveur d'application WEBDEV facturé par **cœurs, mémoire, nombre de serveurs** (WinDev passe à la session). Ajouter de la haute disponibilité ou de la mémoire modifie la facture. Dev-Booster : serveur à **4 490 € HT/an** + 100 sessions à 290 € = **33 490 € HT/an**.
- **WebDev, SEO** (site public) : inventaire des URL indexées et du trafic ; plan de **redirections 301** exhaustif testé avant bascule ; reprise des balises et données structurées ; rendu serveur ou statique ; surveillance de l'indexation plusieurs semaines.
- **WebDev, sessions** : état de session serveur, contextes de page, variables globales → API **sans état**, authentification par jeton, état explicite ; la rétro-documentation identifie ce qui est stocké en session et pourquoi.
- **Trajectoire SaaS** : passer à un **multi-tenant**, nouveaux clients sur la nouvelle plateforme, parc existant par vagues. Cible SFEIR : Java/Spring + Angular sur Google Cloud, PostgreSQL sur Cloud SQL ou AlloyDB.
- **Délais** (Smartshift) : *« un chantier ciblé […] se compte en semaines ; la migration d'une application de gestion se compte en mois, par briques »*.
- **WinDev Mobile, hors ligne** : quelles données embarquer et avec quelle fraîcheur ; résolution des conflits ; reprise sans doublon. NomadBiz (vente itinérante) : 100 % hors connexion → SQLite + .NET MAUI / Blazor Hybrid.
- **Terminaux** : terminaux durcis, douchettes, imprimantes, lecteurs de cartes → inventaire dès l'audit ; conditionne cible et renouvellement du parc.
- **Flutter** (cible par défaut) : une base de code Android, iOS, desktop ; base locale pour le hors ligne ; plugins pour les périphériques courants. PWA acceptable pour un usage connecté et léger seulement.
- **Golden master** : + scénarios de synchronisation (mobile), + parcours complets et redirections (web).

## RésuméDe400mots

L'article de SFEIR complète sa série sur la migration WinDev en traitant les deux produits qui partagent le même langage, WLangage : WebDev pour le web et WinDev Mobile pour les applications mobiles. Il expose ce qui change par rapport à une application desktop et ce qui reste identique.

Pour WebDev, la première spécificité est économique. Les applications s'exécutent sur le serveur d'application WEBDEV, que PC SOFT facture selon le nombre de cœurs, la mémoire et le nombre de serveurs, d'après une vidéo de l'éditeur analysée par Louis Planquart ; ajouter de la haute disponibilité ou absorber un pic de trafic modifie donc la facture. Dev-Booster retient 4 490 euros par an pour ce serveur dans sa simulation. Sur une stack ouverte, le dimensionnement se fait sur le trafic seul. La deuxième spécificité concerne les sites publics, pour lesquels la migration est aussi un projet de référencement : inventaire des URL, plan de redirections 301 testé, reprise des balises, rendu côté serveur et surveillance de l'indexation. La troisième porte sur l'état : les applications WebDev s'appuient sur des sessions serveur et des variables globales, qu'une architecture moderne remplace par des API sans état. Pour les éditeurs, la migration ouvre une trajectoire SaaS multi-tenant, la cible privilégiée par SFEIR étant Java/Spring et Angular sur Google Cloud avec PostgreSQL. Smartshift estime qu'un chantier ciblé se compte en semaines et une application de gestion en mois.

Pour WinDev Mobile, le cœur du sujet est le fonctionnement hors ligne des applications de terrain : quelles données embarquer, comment résoudre les conflits entre terminaux, comment reprendre une synchronisation interrompue. Le cas NomadBiz de Dev-Booster, logiciel de vente itinérante devant fonctionner entièrement hors connexion, a conduit à une base SQLite et à une cible .NET MAUI. L'inventaire des terminaux et périphériques doit se faire dès l'audit. La cible par défaut recommandée par SFEIR est Flutter, pour sa base de code unique, sa gestion du hors ligne et ses plugins ; une PWA ne convient qu'à des usages connectés et légers.

Ce qui ne change pas est la méthode : extraction des règles avant réécriture, spécifications validées, réécriture par agents module par module, golden master inversé et bascule progressive. Le golden master intègre des scénarios de synchronisation pour le mobile et des parcours complets avec redirections pour le web, et les données rejoignent PostgreSQL dans les deux cas. La FAQ précise qu'on peut exposer une API sur la nouvelle base avant de migrer l'application mobile.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Migrer WebDev et WinDev Mobile | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| WebDev | TECHNOLOGIE | utilise | WLangage | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| WinDev Mobile | TECHNOLOGIE | utilise | WLangage | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| WebDev | TECHNOLOGIE | utilise | serveur d'application WEBDEV | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Louis Planquart | PERSONNE | affirme_que | PC SOFT facture le serveur WEBDEV selon les cœurs, la mémoire et le nombre de serveurs | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| Dev-Booster | ORGANISATION | mesure | serveur WEBDEV à 4 490 € HT par an dans une simulation à 33 490 € HT | MESURE | 0.86 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | traiter la migration d'un site WebDev public comme un projet SEO avec redirections 301 exhaustives | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | remplacer l'état de session WebDev par des API sans état | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | Java/Spring et Angular sur Google Cloud pour la trajectoire SaaS des éditeurs WebDev | AFFIRMATION | 0.84 | DYNAMIQUE | déclaré_article |
| Flutter | TECHNOLOGIE | remplace | WinDev Mobile | TECHNOLOGIE | 0.86 | DYNAMIQUE | déclaré_article |
| Dev-Booster | ORGANISATION | utilise | .NET MAUI | TECHNOLOGIE | 0.82 | STATIQUE | déclaré_article |
| Dev-Booster | ORGANISATION | utilise | SQLite | TECHNOLOGIE | 0.84 | STATIQUE | déclaré_article |
| synchronisation hors ligne | CONCEPT | s_applique_à | WinDev Mobile | TECHNOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| golden master inversé | METHODOLOGIE | s_applique_à | WebDev | TECHNOLOGIE | 0.82 | ATEMPOREL | déclaré_article |
| Migrer WebDev et WinDev Mobile | DOCUMENT | recommande | migrer les données vers PostgreSQL | AFFIRMATION | 0.84 | DYNAMIQUE | déclaré_article |
| Smartshift | ORGANISATION | affirme_que | un chantier ciblé se compte en semaines, une application de gestion en mois, par briques | CITATION | 0.84 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| WebDev | TECHNOLOGIE | catégorie | AGL web de PC SOFT, exécuté sur le serveur d'application WEBDEV | AJOUT |
| WinDev Mobile | TECHNOLOGIE | catégorie | AGL mobile de PC SOFT, applications terrain hors ligne | AJOUT |
| serveur d'application WEBDEV | TECHNOLOGIE | modèle commercial | Facturé par cœurs, mémoire et nombre de serveurs | AJOUT |
| synchronisation hors ligne | CONCEPT | enjeux | Fraîcheur des données embarquées, conflits entre terminaux, reprise sans doublon | AJOUT |
| Flutter | TECHNOLOGIE | rôle | Cible mobile par défaut de SFEIR pour remplacer WinDev Mobile | AJOUT |
| Dev-Booster | ORGANISATION | secteur | Éditeur de NomadBiz, logiciel de vente itinérante | AJOUT |
