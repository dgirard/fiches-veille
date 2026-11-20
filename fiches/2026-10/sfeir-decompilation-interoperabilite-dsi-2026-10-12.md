---
themes: [politique-regulation, architecture-construction]
source: SFEIR
---
# sfeir-decompilation-interoperabilite-dsi-2026-10-12

## Veille

Page explicative **SFEIR AI** publiée sur sfeir.com le **12 octobre 2026** (~1 200 mots, six sources), avec l'avertissement *« Ceci n'est pas un conseil juridique »*. Elle détaille, pour une DSI, l'**article 6** de la directive **2009/24/CE** (23 avril 2009), transposé au **IV de l'article L122-6-1** du CPI : le droit de décompiler un programme sans l'accord de son auteur lorsque c'est indispensable à l'**interopérabilité** d'un logiciel créé de façon indépendante. Trois apports. **(A)** Trois conditions cumulatives (droit d'utiliser la copie, information non *« facilement et rapidement »* accessible, actes limités aux parties nécessaires) et trois interdits, dont le plus piégeux pour un projet de réécriture : ne pas produire un programme *« dont l'expression est substantiellement similaire »*. **(B)** La distinction avec le régime de la **correction d'erreurs** (article 5, arrêt **Top System**, CJUE, **2021**), que l'éditeur peut se réserver par contrat, et le rappel de **SAS Institute** (**2012**) sur les formats de fichiers. **(C)** Les conséquences pour l'outillage : un agent équipé de **REA** pilote **Ghidra** et la décompilation *« ne demande plus des semaines d'expert »*, d'où la consigne de cadrer la session (question précise, périmètre de fonctions limité, conservation des preuves) et d'éviter la demande *« reconstruis l'application »*. Page satellite de [[sfeir-clean-room-vs-reverse-engineering-2026-10-11]].

## Titre Article

Décompiler pour interopérer : l'article 6 de la directive expliqué à une DSI

## Date

2026-10-12

## URL

https://www.sfeir.com/articles/decompilation-interoperabilite-dsi/

## Keywords

décompilation, interopérabilité, article 6, directive 2009/24/CE, article L122-6-1, Code de la propriété intellectuelle, exception au droit d'auteur, trois conditions, trois interdits, expression substantiellement similaire, correction d'erreurs, article 5, Top System C-13/20, SAS Institute C-406/10, format de fichiers, clause de licence nulle, REA, Ghidra, rétro-ingénierie par agents, clean-room, legacy, DSI

## Authors

SFEIR AI, voix éditoriale non signée — publié sur sfeir.com, site éditorial de SFEIR.

## Ton

**Profil** : fiche pratique de droit du logiciel vulgarisée, publiée sur le site d'un cabinet, adressée à une DSI qui doit faire dialoguer une application ancienne avec le reste du SI. Français clair, avertissement juridique en ouverture, FAQ en quatre questions.

**Style** : structure didactique — principe, cas typique (application achetée il y a quinze ans, protocole non documenté, éditeur muet), trois conditions, trois interdits, régime voisin, conséquences d'outillage. Les textes sont cités par article et alinéa, les arrêts par date et numéro d'affaire. Un schéma signalé comme *« informatif, pas un conseil juridique »* illustre le troisième interdit.

**Position épistémique** : le texte rappelle que l'exception s'interprète strictement, distingue nettement les deux régimes (interopérabilité et correction d'erreurs) et renvoie la qualification au juriste (*« à vérifier au cas par cas »*). Il note que le cadre juridique *« n'a pas bougé »* alors que l'outillage a changé d'échelle, et s'appuie sur le README et le DISCLAIMER de REA pour situer l'outil.

## Pense-betes

- **Principe** : l'article 6 autorise reproduction et traduction de la forme du code (décompilation) quand c'est indispensable à l'interopérabilité d'un programme créé indépendamment. Exception au monopole de l'auteur, donc interprétée strictement.
- **Trois conditions cumulatives** : (1) droit d'utiliser une copie, ou agir pour qui l'a ; (2) information pas déjà facilement et rapidement accessible ; (3) actes limités aux parties nécessaires.
- **Traiter la condition 2 en premier** : demander la documentation à l'éditeur, chercher spécification publique, SDK, API documentée, et garder la trace de ces démarches.
- **Condition 3 en pratique** : Ghidra importe souvent tout le binaire ; ce qui compte est de limiter l'étude et l'usage aux parties nécessaires, et de le documenter.
- **Trois interdits** : pas d'autre usage que l'interopérabilité ; pas de communication à des tiers sauf nécessité ; pas de programme à l'expression substantiellement similaire ni d'acte portant atteinte au droit d'auteur.
- **Piège de la réécriture** : décompiler pour comprendre un protocole puis réécrire à l'identique la fonction qui le produit sort de l'exception — d'où la méthode clean-room.
- **Correction d'erreurs** : article 5 + Top System (C-13/20, 6 octobre 2021), décompilation possible dans la mesure nécessaire, hors conditions de l'article 6 ; l'éditeur peut se réserver la correction (I de L122-6-1).
- **SAS Institute** : formats et langages non protégés comme expression du programme, sauf protection comme œuvre originale au titre de la directive 2001/29/CE.
- **Clause contraire** : en droit français, une stipulation contraire au IV de L122-6-1 est nulle ; le reste du contrat s'applique.
- **Cadrer une session REA** : question précise (format d'un message, séquence d'un échange), périmètre de fonctions limité, conservation des preuves pour démontrer la proportionnalité.

## RésuméDe400mots

Cette page de SFEIR explique à une DSI le droit de décompiler un logiciel pour le rendre interopérable. Depuis la directive européenne 2009/24/CE, transposée au IV de l'article L122-6-1 du Code de la propriété intellectuelle, il est possible de décompiler un programme sans l'accord de son auteur lorsque c'est indispensable pour obtenir les informations nécessaires à l'interopérabilité d'un logiciel créé de façon indépendante. La page rappelle qu'elle ne constitue pas un conseil juridique et que les outils de rétro-ingénierie par agents, comme REA, ont réduit le coût technique de la décompilation sans modifier ce cadre.

Le cas typique est celui d'une application métier ancienne qui échange des données selon un protocole non documenté, dont l'éditeur ne répond plus, et qu'il faut faire dialoguer avec un nouveau système. L'exception s'applique si trois conditions cumulatives sont réunies : la personne a le droit d'utiliser le programme, l'information n'est pas déjà facilement accessible, et les actes se limitent aux parties nécessaires. La page conseille de commencer par demander la documentation à l'éditeur et de garder la trace de ces démarches.

Trois interdits encadrent l'usage des informations obtenues : elles ne servent qu'à l'interopérabilité, ne se communiquent pas à des tiers sans nécessité, et ne peuvent pas servir à produire un programme dont l'expression est substantiellement similaire. Ce dernier point est présenté comme le piège des projets de réécriture : comprendre un protocole puis réécrire la fonction à l'identique sort de l'exception, ce que la méthode clean-room vise à éviter.

Un régime distinct couvre la correction d'erreurs. L'article 5 de la directive, interprété par l'arrêt Top System de 2021, permet à l'acquéreur légitime de décompiler pour corriger des erreurs, dans la mesure nécessaire et dans le respect du contrat, l'éditeur pouvant se réserver cette correction. L'arrêt SAS Institute de 2012 rappelle que les formats de fichiers ne sont pas protégés comme expression d'un programme, ce qui place la compréhension d'un format d'échange sur un terrain favorable. En droit français, une clause de licence contraire à l'exception d'interopérabilité est nulle.

Côté outillage, un agent équipé de REA peut piloter Ghidra et restituer pseudocode, chaînes et références avec leurs preuves. Pour rester dans l'article 6, la page recommande une question précise, un périmètre de fonctions limité et la conservation des preuves, et déconseille de demander à l'agent de reconstruire l'application.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Décompiler pour interopérer : l'article 6 de la directive expliqué à une DSI | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| directive 2009/24/CE | DOCUMENT | permet | décompilation pour interopérabilité | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | est_basé_sur | directive 2009/24/CE | DOCUMENT | 0.93 | STATIQUE | déclaré_article |
| directive 2009/24/CE | DOCUMENT | affirme_que | les informations obtenues ne peuvent servir à un programme à l'expression substantiellement similaire | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| décompilation pour interopérabilité | METHODOLOGIE | s_applique_à | application legacy à protocole non documenté | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| arrêt Top System | DOCUMENT | affirme_que | la décompilation pour corriger des erreurs relève de l'article 5, pas des conditions de l'article 6 | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| arrêt SAS Institute | DOCUMENT | affirme_que | ni la fonctionnalité, ni le langage, ni le format des fichiers ne sont protégés par le droit d'auteur | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | une clause de licence contraire au IV de L122-6-1 est nulle en droit français | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | permet | rétro-ingénierie par agents | METHODOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| réimplémentation clean-room | METHODOLOGIE | résout | réécriture substantiellement similaire après décompilation | CONCEPT | 0.84 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | demander d'abord la documentation à l'éditeur et garder la trace des démarches | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | cadrer une session REA : question précise, périmètre limité, preuves conservées | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet de conseil, éditeur de sfeir.com | AJOUT |
| directive 2009/24/CE | DOCUMENT | référence | Directive du 23 avril 2009, protection juridique des programmes d'ordinateur, article 6 (décompilation) | AJOUT |
| article L122-6-1 du CPI | DOCUMENT | référence | IV : exception de décompilation pour interopérabilité ; I : correction d'erreurs réservable par contrat | AJOUT |
| décompilation pour interopérabilité | METHODOLOGIE | définition | Exception au droit d'auteur : 3 conditions cumulatives, 3 interdits | AJOUT |
| arrêt Top System | DOCUMENT | référence | CJUE, 6 octobre 2021, C-13/20 | AJOUT |
| REA | TECHNOLOGIE | définition | Outil de rétro-ingénierie par agents pilotant Ghidra, avec preuves et limites de chaque conclusion | AJOUT |
| Ghidra | TECHNOLOGIE | catégorie | Outil de décompilation de binaires natifs | AJOUT |
