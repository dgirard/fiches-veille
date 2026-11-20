---
themes: [qualite-securite, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-garde-fous-site-agents-ia-2026-11-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 novembre 2026**, volet de la série sur le site conversationnel de sfeir.com consacré aux contrôles. Point de départ : sur **1 482 commits** du 1er avril au 13 novembre 2026, **1 137 (77 %)** sont co-signés par un agent de code. L'article décrit *« trois filets et une personne »*. **(1)** Avant d'écrire : un fichier d'instructions de **609 lignes** relu à chaque session, 109 plans, 34 notes de solutions, neuf procédures outillées, et des règles éditoriales datées (rien d'inventé, aucun client nommé dans un cas client, chiffres d'offre mesurés seulement, citations jamais réécrites). **(2)** Au build : *bloquer ce qui est binaire, signaler ce qui demande un jugement* — lexique, chiffres du groupe, CSP, structure, données structurées bloquent ; santé de la base et synchronisations signalent ; plus de **1 200 tests**. **(3)** En production : réponse tirée des seuls contenus publiés, masquage des données personnelles, questions venues d'un lien `/?q=` affichées en citation sans réponse rédigée. **(4)** Une personne qui approuve toute écriture hors du dépôt et rend les arbitrages. Un journal daté de huit incidents, chacun devenu contrôle, illustre la boucle du compound engineering.

## Titre Article

Contenus écrits par des agents IA : les garde-fous qui gardent un site juste

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/garde-fous-site-ecrit-agents-ia/

## Keywords

garde-fous, contenu généré par IA, agents de code, CLAUDE.md, fichier d'instructions, règles éditoriales, contrôles de build, bloquer vs signaler, lexique interdit, CSP, données structurées, tests, passe anti-slop, relecture croisée, approbation humaine, injection par lien, masquage des données personnelles, journal des incidents, compound engineering, cache Cloudflare, gouvernance, SFEIR

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article de confiance et de gouvernance, écrit par le cabinet sur son propre site. Public déclaré : RSSI, conformité et direction marketing, secondairement DSI et CTO.

**Style** : structuré par les trois filets d'une figure, deux tableaux (contrôles de build avec leur effet, incidents datés avec la correction qui en est née). Les règles sont formulées à l'impératif et datées quand elles résultent d'une décision (cas clients anonymisés le 12 novembre). Le registre reste descriptif ; les leçons sont réservées à la section finale par rôle.

**Position épistémique** : le journal des incidents est présenté sans atténuation — cinq mois sans synchronisation des offres d'emploi, 129 adresses de cas clients servies par le cache après renommage, schémas de 27 articles passés au noir. Une section « ce que ces filets ne garantissent pas » pose que les contrôles *« lisent du texte, pas du sens »* et que les approbations reconnaissent une commande à son texte. Source externe unique : le dépôt stop-slop d'Olivier Rafal.

## Pense-betes

- **Chiffre d'entrée** : 77 % des commits co-signés par un agent ; *« un agent écrit vite, et se trompe avec assurance »*.
- **Filet 1, avant d'écrire** : fichier d'instructions de 609 lignes, décisions datées, 109 plans, 34 notes de solutions, neuf procédures outillées (événement, fiche, offres d'emploi, grappe d'articles, présentation).
- **Règles éditoriales** : rien d'inventé ; faits mouvants datés dans la phrase ; aucun cas client ne nomme son client ; offres = chiffres mesurés avec méthode ; citation jamais réécrite ; aucun compteur mouvant dans un titre ; signature « SFEIR AI » par défaut.
- **Deux passes** : anti-slop (adaptée du travail d'Olivier Rafal, WEnvision) ; relecture croisée par un modèle d'un autre fournisseur, dont chaque remarque retenue est revérifiée à la source.
- **Filet 2, au build** : bloque si la faute est binaire et se corrige en un mot, signale si elle demande un jugement. Règle d'usage : *on nettoie d'abord, on bannit ensuite*. 89 fichiers de tests, plus de 1 200 tests.
- **Filet 3, en production** : sources limitées au catalogue déployé, colonne par règles, e-mails et numéros masqués avant modèle, cache et journaux ; refus des demandes de données personnelles et des changements de rôle.
- **Liens `/?q=`** : une question non écrite par SFEIR s'affiche en citation avec avertissement, reçoit la colonne mais ni réponse rédigée ni cache tant que le visiteur ne l'envoie pas lui-même.
- **Une personne** : approbation humaine pour toute écriture hors dépôt ; la synchronisation refuse de supprimer plus d'un quart des offres et met en quarantaine une offre nommant un client. Dix-neuf arbitrages consignés le 12 novembre.
- **Incidents → contrôles** : synchronisation jamais programmée (5 mois) ; dates de plan du site faussées par un clone partiel ; 21 fiches longues non comptées ; alias « CHANGE » ; cache Cloudflare non purgeable sans zone ; 103 extraits sur 368 mal formés ; 27 schémas au noir ; faux ami « assurance qualité ».
- **Conseil CTO** : *une porte qui bloque sur une question de goût finit contournée*.

## RésuméDe400mots

Ce volet de la série sur sfeir.com décrit les contrôles qui encadrent un site dont 77 % des commits, 1 137 sur 1 482 entre avril et novembre 2026, sont co-signés par un agent de code. L'article part d'un constat : un agent écrit vite et se trompe avec assurance. Ce qui garde le site juste tient en trois filets et une personne.

Le premier filet est un texte. Le fichier d'instructions du projet, lu par l'agent à chaque session, compte 609 lignes et renvoie à des décisions datées, 109 plans, 34 notes de solutions et neuf procédures outillées. Les règles éditoriales y sont écrites une fois : rien d'inventé, faits vérifiés en source primaire, aucun client nommé dans un cas client, chiffres d'offre mesurés uniquement, citations jamais réécrites, signature collective par défaut. Deux passes complètent l'écriture : une passe anti-slop qui retire les tics des modèles de langage, et une relecture croisée par un modèle d'un autre fournisseur, dont les remarques sont revérifiées.

Le deuxième filet tourne à chaque build. Un contrôle bloque quand la faute est binaire et se corrige en un mot ; il signale quand la correction demande un jugement. Lexique interdit, chiffres du groupe, absence de script en ligne, structure des titres et données structurées bloquent ; fiches sans sources et synchronisations anciennes sont signalées. Un terme n'est banni qu'après nettoyage du corpus. Plus de 1 200 tests complètent le build.

Le troisième filet protège le visiteur de la conversation : réponse tirée des seuls contenus publiés, sources prises dans le catalogue, données personnelles masquées, mesure sans IP ni réponse, deux portes de santé au déploiement. Une question arrivée par un lien est affichée en citation, avec un avertissement, sans réponse rédigée tant que le visiteur ne l'a pas envoyée lui-même.

Enfin, toute commande qui écrit hors du dépôt attend une approbation humaine, et les arbitrages éditoriaux et commerciaux sont pris par une personne et consignés.

L'article publie un journal de huit incidents datés, chacun transformé en règle, contrôle ou test : synchronisation des offres jamais programmée pendant cinq mois, cache Cloudflare impossible à purger, alias trop courant, extraits mal formés. Il pose aussi les limites : les contrôles lisent du texte et non du sens, et un signal non bloquant n'agit que si quelqu'un le lit.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | article Contenus écrits par des agents IA les garde-fous | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | mesure | 1 137 commits sur 1 482 (77 %) co-signés par un agent de code | MESURE | 0.93 | STATIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | CLAUDE.md | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| trois filets de contrôle | METHODOLOGIE | fait_partie_de | sfeir.com | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| bloquer le binaire, signaler le jugement | METHODOLOGIE | fait_partie_de | trois filets de contrôle | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | une porte qui bloque sur une question de goût finit contournée | CITATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | transformer chaque incident en contrôle | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| trois filets de contrôle | METHODOLOGIE | est_basé_sur | Compound Engineering | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| passe anti-slop | METHODOLOGIE | s_inspire_de | stop-slop.fr | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Olivier Rafal | PERSONNE | a_créé | stop-slop.fr | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Olivier Rafal | PERSONNE | travaille_chez | WEnvision | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |
| relecture croisée multi-fournisseur | METHODOLOGIE | fait_partie_de | trois filets de contrôle | METHODOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| approbation humaine | METHODOLOGIE | réduit | écritures hors du dépôt par l'agent | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| question venue d'un lien en citation | METHODOLOGIE | réduit | injection de prompt par lien | CONCEPT | 0.84 | ATEMPOREL | inféré |
| SFEIR | ORGANISATION | affirme_que | les contrôles lisent du texte, pas du sens | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| sfeir.com | TECHNOLOGIE | mesure | plus de 1 200 tests dans 89 fichiers au 13 novembre 2026 | MESURE | 0.88 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| trois filets de contrôle | METHODOLOGIE | composition | Règles avant l'écriture, contrôles au build, protections en production, plus une personne qui décide | AJOUT |
| bloquer le binaire, signaler le jugement | METHODOLOGIE | principe | Bloque si la faute se corrige en un mot ; signale si elle demande un jugement ; bannir après nettoyage | AJOUT |
| passe anti-slop | METHODOLOGIE | rôle | Retrait des tics d'écriture des modèles de langage, adaptée au français de SFEIR | AJOUT |
| relecture croisée multi-fournisseur | METHODOLOGIE | principe | Relecture par un modèle d'un autre fournisseur ; remarques revérifiées à la source | AJOUT |
| Olivier Rafal | PERSONNE | rôle | Auteur de stop-slop.fr (WEnvision) | AJOUT |
