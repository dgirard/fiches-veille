---
themes: [agents-codage-ia-skills, economie-marche]
source: SFEIR
---
# sfeir-construire-site-agents-phases-temps-2026-11-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 novembre 2026**, volet de la série sur le site conversationnel de sfeir.com consacré au temps passé. **(1)** La mesure de la couche conversationnelle (28 octobre – 14 novembre 2026), tirée des journaux de **Claude Code** : **695 interactions**, soit **23,2 heures humaines** à deux minutes par interaction, **56 heures** de Claude à l'horloge (×2,4) et **89 heures-agent** (×3,8), **265 commits**, **2 302 $** en équivalent API dont 2 073 $ pour Opus 5.5 (calcul par **ccusage**). **(2)** Une estimation sur l'ensemble du site depuis avril : **1 482 commits**, 140 jours actifs, **~432 heures d'activité** réparties en **huit phases**, et ~100 heures humaines obtenues en appliquant aux phases antérieures le rapport mesuré sur la conversation (23 %). **(3)** La méthode et ses limites : journaux locaux conservés **trente jours** par défaut, temps hors session non compté, estimation par les commits présentée comme un ordre de grandeur. Le verdict : *« écrire le code ne représente plus l'essentiel du coût ; le temps humain va aux décisions, à la vérification et à la matière »*. Le texte précise ne pas mesurer une productivité générale : un site, conduit pour l'essentiel par une personne.

## Titre Article

Construire un site avec des agents IA : les phases et le temps réellement passé

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/construire-site-agents-ia-phases-temps/

## Keywords

temps de développement, agents de code, Claude Code, Claude Opus, temps humain, heures-agent, horloge, interactions, journaux de session, cleanupPeriodDays, ccusage, équivalent API, commits, phases de projet, estimation, compound engineering, Sandwich Team, Product Engineer, arbitrages, mesure du ROI, site conversationnel, SFEIR

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article d'analyse chiffrée, écrit par le cabinet sur son propre chantier. Public déclaré : DSI, secondairement CTO et achats.

**Style** : méthodologique d'abord — une section « comment nous avons compté » précède tout chiffre et explicite trois mesures distinctes (temps humain, horloge, heures-agent). Un tableau des huit phases (dates, commits, activité, temps humain, livrables) et deux figures. Le détail descend jusqu'à la journée la plus chargée (13 novembre : 129 interactions, 47 commits).

**Position épistémique** : le texte sépare nettement le mesuré (la phase conversation) de l'estimé (les sept phases antérieures), signale qu'une règle de comptage alternative donnait 52,6 h au lieu de 15,8 h sur la même période, et confronte l'estimation à un point de contrôle (6 h mesurées contre 8 h estimées). Section « ce que ces chiffres ne disent pas » : temps hors session, équivalent API théorique sur abonnement, conduite par une seule personne, journaux perdus.

## Pense-betes

- **Règle de comptage** : 2 min par interaction humaine (message en session principale ou réponse à une question à choix), règle fixée le 10 novembre. L'écart entre messages mesurait aussi l'absence : 52,6 h contre 15,8 h sur la même période.
- **Deux mesures de Claude** : l'horloge (chaque minute une fois) et les heures-agent (somme des agents, sous-agents compris).
- **Conversation, mesurée** : 23,2 h humaines, 56 h horloge, 89,2 h-agent, 2 302 $ API. Trois périodes : moteur et colonne (13,4 h / 32,5 h, 153 commits), sécurité et finitions (3,8 h / 10,5 h), ergonomie, migration, mise en production (6,1 h / 13,2 h). Un modèle d'un autre fournisseur a relu le travail : 33 appels, 39 min.
- **Mois complet** (15 oct. – 14 nov.) : 33,5 h humaines, ~70 h de Claude, **2 994 $** équivalent API.
- **Huit phases** : brief (mars, sans commit), construction (1er-3 avril, ~18 h), durcissement (~52 h), recette et mise en ligne (~30 h), articles et grappes (~113 h), base/sourcing/SEO-GEO (~83 h), offres d'emploi et sécurité (~35 h), conversation (~101 h).
- **Estimation** : temps humain = 23 % de l'activité tirée des commits, appliqué aux phases antérieures. Point de contrôle : 6 h mesurées contre 8 h estimées en octobre ; l'estimation pèche plutôt par défaut.
- **Où passe le temps humain** : décisions (19 arbitrages pendant la revue d'ergonomie, consignés dans le dépôt et relus par l'agent) et vérification.
- **Contributeurs** : cinq personnes du marketing, de la communication et des RH publient via procédures outillées, 125 commits (8 %). Cinq versions de Claude Opus successives (4.6 → 5.5) sans réécriture du site.
- **Leçon CTO** : conserver les journaux au-delà de 30 jours (`cleanupPeriodDays`), une règle de temps humain, des commits qui disent quel agent a travaillé.
- **Leçon DSI** : budgéter la base de connaissances et le temps de ceux qui tranchent.

## RésuméDe400mots

Ce volet de la série sur sfeir.com chiffre le temps réellement passé à construire le site avec des agents. Il s'adresse aux DSI et CTO qui doivent budgéter un projet de ce type, et précise d'emblée ne pas mesurer une productivité générale : il s'agit d'un site, conduit pour l'essentiel par une seule personne.

La méthode est exposée avant les résultats. Le temps humain compte deux minutes par interaction, règle fixée le 10 novembre 2026 ; mesurer l'écart entre messages aurait compté l'absence autant que le travail. Le temps de Claude se lit dans les journaux de deux façons : l'horloge, où chaque minute compte une fois, et les heures-agent, qui additionnent les sous-agents. Le coût est un équivalent au tarif de l'API calculé par l'outil libre ccusage. Comme Claude Code ne conserve ses journaux locaux que trente jours par défaut, seule la période du 15 octobre au 14 novembre est mesurée ; avant, une estimation est tirée de l'horodatage des commits.

La couche conversationnelle, du 28 octobre au 14 novembre, a demandé 695 interactions, soit 23,2 heures humaines, pour 56 heures de Claude à l'horloge et 89 heures-agent. Le chantier aurait coûté 2 302 dollars en équivalent API. Le premier tiers a construit le moteur et la colonne de pages, la fin a porté la revue d'ergonomie et la chaîne de mise en production. Sur le mois complet, avec le reste du site, le total atteint 33,5 heures humaines et 2 994 dollars.

Sur l'ensemble de l'année, le dépôt compte 1 482 commits sur 140 jours, répartis en huit phases d'avril à novembre, pour environ 432 heures d'activité. Le temps humain des sept premières phases est estimé en appliquant le rapport mesuré sur la conversation, 23 %, soit environ 100 heures au total ; l'article le présente comme un ordre de grandeur.

Le temps humain va surtout aux décisions — dix-neuf arbitrages pendant la seule revue d'ergonomie, consignés dans le dépôt — et à la vérification. Cinq personnes non techniques ont publié elles-mêmes 8 % des commits, et cinq versions de Claude Opus se sont succédé sans réécriture du site, ce que l'article rattache au compound engineering.

Les limites sont listées : temps hors session absent, estimation fragile, coût API théorique sur abonnement, journaux d'avril perdus. Les conseils : mesurer dès le premier jour et budgéter la matière et les décideurs plutôt que le code.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | article Construire un site avec des agents IA | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | Claude Opus | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | utilise | ccusage | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | conversation : 695 interactions, 23,2 h humaines, 56 h de Claude à l'horloge, 89 heures-agent | MESURE | 0.93 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | 2 302 $ en équivalent API pour la conversation, 2 994 $ sur le mois mesuré | MESURE | 0.9 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | 1 482 commits, 140 jours actifs, ~432 h d'activité, ~100 h humaines estimées | MESURE | 0.85 | STATIQUE | déclaré_article |
| règle des deux minutes par interaction | METHODOLOGIE | résout | temps d'absence compté comme travail | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | écrire le code ne représente plus l'essentiel du coût ; le temps humain va aux décisions, à la vérification et à la matière | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | mesure | journaux de session locaux conservés trente jours par défaut | MESURE | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | conserver les journaux au-delà de trente jours et fixer une règle de temps humain dès le premier jour | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| sfeir.com | TECHNOLOGIE | est_basé_sur | Compound Engineering | METHODOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | utilise | Sandwich Team | METHODOLOGIE | 0.78 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | budgéter la base de connaissances et le temps de ceux qui tranchent | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| règle des deux minutes par interaction | METHODOLOGIE | définition | Temps humain = 2 min par message ou réponse à une question de l'agent | AJOUT |
| ccusage | TECHNOLOGIE | catégorie | Outil libre (MIT) d'analyse des tokens et coûts d'agents de code à partir des journaux locaux | AJOUT |
| heures-agent | CONCEPT | définition | Somme des minutes de chaque agent, sous-agents compris, distincte du temps d'horloge | AJOUT |
| sfeir.com | TECHNOLOGIE | phases 2026 | Huit phases d'avril à novembre, 1 482 commits | AJOUT |
