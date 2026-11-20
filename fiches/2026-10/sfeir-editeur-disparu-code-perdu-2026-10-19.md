---
themes: [architecture-construction, transformation-adoption, qualite-securite]
source: SFEIR
---
# sfeir-editeur-disparu-code-perdu-2026-10-19

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **19 octobre 2026** (~1 100 mots, trois sources notées, encadré « ceci n'est pas un conseil juridique »). Il traite le cas d'une application critique dont l'éditeur a fermé ou a été absorbé, dont le mainteneur est parti et dont le code source est introuvable, et propose un plan de sauvetage en **quatre temps**. **(1) Stabiliser** : figer l'environnement dans une image reproductible, restaurer les sauvegardes, recenser les dates butoirs (fin de support d'OS, licence, certificat). **(2) Récupérer ce qui existe** : sauvegardes, postes d'anciens développeurs, ancien prestataire, **séquestre de code source** (escrow) prévu au contrat. **(3) Rétro-documenter** depuis le binaire, les écrans et les données, avec des outils comme **REA**, en environnement isolé, et en rappelant l'arrêt **Top System** de la CJUE (6 octobre 2021) sur la décompilation pour corriger des erreurs. **(4) Réécrire sous golden master**, l'application d'origine servant d'oracle des tests. Un dernier cas traite l'éditeur racheté (PC SOFT, WinDev). L'article insiste : *« Le code d'origine, lui, ne revient pas »*. S'inscrit dans la série SFEIR d'octobre 2026 sur la rétro-ingénierie par agents.

## Titre Article

Éditeur disparu, code source perdu : plan de sauvetage d'une application critique

## Date

2026-10-19

## URL

https://www.sfeir.com/articles/editeur-disparu-code-perdu/

## Keywords

éditeur disparu, code source perdu, continuité applicative, application critique, legacy, stabilisation, image reproductible, séquestre de code source, escrow, rétro-documentation, rétro-ingénierie par agents, REA, Ghidra, Hopper, IDA, binaire, golden master, réécriture par briques, CJUE Top System, décompilation, correction d'erreurs, article L122-6-1, PC SOFT, WinDev, Software Factory

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

Article pratique et procédural, en français, à destination des DSI et responsables d'applications confrontés à un legacy orphelin. Le registre est celui de la **check-list ordonnée** : quatre temps numérotés, impératifs (« figez », « sauvegardez », « relisez le contrat »), FAQ finale. La prudence juridique est explicite : un encadré rappelle que le conseil juridique n'est pas le métier de SFEIR et renvoie chaque point de droit au juriste du lecteur. L'outillage agentique (REA) est placé au troisième temps seulement, après la stabilisation et la recherche des sources, ce que l'introduction annonce d'emblée. Les références sont courtes et vérifiables (README et SECURITY.md de REA, arrêt de la CJUE). L'article se clôt sur l'offre Software Factory de SFEIR et renvoie à plusieurs pages satellites du même dossier (hub legacy, formats propriétaires, clean-room).

## Pense-betes

- **Scénario** : éditeur fermé ou absorbé, mainteneur parti, source introuvable ; l'application *« facture, planifie ou paie »* encore.
- **Temps 1, stabiliser** : image reproductible (OS, bibliothèques, pilotes, base, paramètres) ; restauration des sauvegardes testée ; gestes d'exploitation notés (*« la seule documentation vivante »*) ; dépendances qui cassent = **dates butoirs** (fin de support d'OS, licence de base, certificat, service externe).
- **Temps 2, récupérer** : vieilles sauvegardes, postes d'anciens développeurs, dépôts oubliés, ancien prestataire ; **séquestre (escrow)** avec conditions de libération en cas de défaillance ; documentation utilisateur, cahiers de recette, exports de paramétrage. Un source partiel ou ancien se lit mieux qu'un binaire, et l'écart avec la production se mesure.
- **Temps 3, rétro-documenter** : REA pilote Hopper, Ghidra ou IDA sur du natif, lit statiquement .NET et JavaScript/Electron, rend conclusions, preuves et limites. Objectif : une **spécification relue par les utilisateurs**, avec la liste des zones obscures.
- **Confinement** : REA *« delegates parsing and analysis to the selected local provider with that user's permissions »* → environnement isolé.
- **Droit** : CJUE, **Top System (C-13/20), 6 octobre 2021** : l'acquéreur légitime peut décompiler pour corriger des erreurs, dans la mesure nécessaire et sous réserve du contrat (I de l'article L122-6-1 CPI).
- **Temps 4, golden master** : capturer les sorties de l'application d'origine sur des entrées représentatives ; la nouvelle doit les reproduire avant chaque bascule de brique.
- **Éditeur racheté** : nouvelle redevance, fin de support, hausse de tarif (exemple PC SOFT / WinDev) ; options négocier, geler, migrer ; la rétro-documentation chiffre le coût d'une sortie.

## RésuméDe400mots

L'article part d'un scénario présenté comme plus fréquent qu'on ne l'avoue : l'éditeur d'une application a fermé ou a été absorbé, le prestataire qui la maintenait est parti, et personne ne retrouve le code source. L'application continue pourtant de facturer, de planifier ou de payer. Depuis octobre 2026, des outils comme REA rendent la rétro-documentation d'un binaire plus accessible, mais SFEIR les place au troisième temps d'un plan qui en compte quatre.

Le premier temps consiste à stabiliser. Il s'agit de figer l'environnement d'exécution dans une image reproductible (système, bibliothèques, pilotes, base de données, paramètres), de sauvegarder les données et de vérifier leur restauration sur une machine de test, et de noter avec les exploitants ce qui fait tomber l'application et ce qui la relève. Les dépendances qui vont casser (fin de support d'un système, licence de base de données, certificat, service externe) fixent chacune une date butoir.

Le deuxième temps vise à récupérer ce qui existe. Le code a rarement disparu partout : vieilles sauvegardes, postes d'anciens développeurs, dépôts oubliés, ancien prestataire, archives de projet. Le contrat peut prévoir un séquestre de code source, avec des conditions de libération en cas de défaillance de l'éditeur. La documentation utilisateur, les cahiers de recette et les exports de paramétrage décrivent le comportement attendu. Même partiel ou ancien, un source change la suite, car un agent le lit mieux qu'un binaire.

Le troisième temps est la rétro-documentation des règles métier à partir de l'exécutable, des écrans et des données. REA pilote Hopper, Ghidra ou IDA sur un exécutable natif et lit statiquement .NET et JavaScript/Electron, en renvoyant preuves et limites. L'analyse se fait en environnement isolé, puisque REA délègue l'analyse au moteur local avec les droits de l'utilisateur. Côté droit, l'article cite l'arrêt Top System de la CJUE (6 octobre 2021) : l'acquéreur légitime peut décompiler pour corriger des erreurs, dans la mesure nécessaire et sous réserve du contrat, et renvoie licence, repreneur des droits et usage de la spécification au juriste.

Le quatrième temps est la réécriture sous golden master : l'application d'origine sert d'oracle, ses sorties sur des entrées représentatives doivent être reproduites avant chaque bascule de brique.

Un dernier cas traite l'éditeur racheté qui change sa politique commerciale, avec l'exemple de PC SOFT et WinDev : les options deviennent négocier, geler ou migrer, et la rétro-documentation chiffre ce que coûterait une sortie. La FAQ rappelle qu'on sauve le comportement, pas le code d'origine, et qu'on commence par stabiliser.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Éditeur disparu, code source perdu | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Éditeur disparu, code source perdu | DOCUMENT | recommande | plan de sauvetage en quatre temps | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| plan de sauvetage en quatre temps | METHODOLOGIE | utilise | séquestre de code source | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| plan de sauvetage en quatre temps | METHODOLOGIE | utilise | rétro-documentation | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| plan de sauvetage en quatre temps | METHODOLOGIE | utilise | golden master | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| rétro-documentation | METHODOLOGIE | utilise | REA | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Hopper | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | IDA Pro | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| arrêt Top System | DOCUMENT | affirme_que | l'acquéreur légitime peut décompiler un programme pour en corriger les erreurs, dans la mesure nécessaire | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| CJUE | ORGANISATION | publie | arrêt Top System | DOCUMENT | 0.92 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | stabiliser l'application avant toute réécriture | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | analyser l'exécutable dans un environnement isolé | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| golden master | METHODOLOGIE | s_applique_à | réécriture par briques d'une application legacy | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| PC SOFT | ORGANISATION | a_créé | WinDev | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| rétro-documentation | METHODOLOGIE | permet | chiffrage d'une sortie d'éditeur | CONCEPT | 0.8 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| plan de sauvetage en quatre temps | METHODOLOGIE | étapes | stabiliser, récupérer, rétro-documenter, réécrire sous golden master | AJOUT |
| séquestre de code source | CONCEPT | définition | dépôt du code chez un tiers, libéré au client sous conditions contractuelles (escrow) | AJOUT |
| REA | TECHNOLOGIE | catégorie | outil open source de rétro-ingénierie par agents (morluto/rea), orchestrateur de moteurs | AJOUT |
| golden master | METHODOLOGIE | rôle | capture des sorties de l'application d'origine servant d'oracle aux tests de la réécriture | AJOUT |
| arrêt Top System | DOCUMENT | référence | CJUE, 6 octobre 2021, C-13/20 | AJOUT |
| PC SOFT | ORGANISATION | produit | éditeur de WinDev, racheté | AJOUT |
