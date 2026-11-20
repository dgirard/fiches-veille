---
themes: [politique-regulation, qualite-securite]
source: SFEIR
---
# sfeir-rgpd-verifier-telemetrie-application-2026-10-18

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **18 octobre 2026** (~1 200 mots, cinq sources), fiche du cluster SFEIR sur la rétro-ingénierie par agents, adressée aux **DPO**. Point de départ : le **RGPD** (règlement UE 2016/679) demande un registre des traitements et l'encadrement des transferts hors Union, alors que pour une application tierce ce registre *« repose souvent sur la seule déclaration de l'éditeur »* ; *« l'écart entre les deux est le sujet »*. Trois apports. **(A)** Ce que l'analyse statique par **REA** fournit selon la cible (modules et canaux IPC sur Electron, manifeste et classes via JADX sur une APK, chaînes sur un binaire natif) et ce qu'on y cherche : domaines en dur, SDK de télémétrie, permissions, flux d'une donnée personnelle vers un appel réseau ; le test d'Ishank Choudhary sert d'ordre de grandeur (**52 secondes** pour une archive Electron de **100 Mo**, deux scripts de préchargement manqués). **(B)** La distinction centrale : *« Le statique montre le possible, la capture montre le réel »* ; la capture réseau (HAR, SAZ) exige l'exécution, donc une VM dédiée, un compte de test et un proxy d'inspection, la capture elle-même contenant des données personnelles. **(C)** Le cadre : article **L122-6-1** du CPI (observation permise, décompilation limitée), d'où un audit fondé d'abord sur l'observation. Texte voisin de la fiche SFEIR sur l'audit de binaire fournisseur.

## Titre Article

RGPD : vérifier ce qu'une application envoie vraiment

## Date

2026-10-18

## URL

https://www.sfeir.com/articles/rgpd-verifier-telemetrie-application/

## Keywords

RGPD, règlement (UE) 2016/679, DPO, responsable de traitement, sous-traitant, registre des traitements, transfert hors UE, télémétrie, SDK d'analytics, suivi des plantages, SDK publicitaire, politique de confidentialité, analyse statique, capture réseau, HAR, SAZ, proxy d'inspection, machine virtuelle, compte de test, REA, Electron, APK, JADX, Ghidra, Ishank Choudhary, article L122-6-1, observation, décompilation, arrêt Top System, écart de conformité, AI Cyber

## Authors

SFEIR AI (voix éditoriale du cabinet), article non signé individuellement — sfeir.com, site éditorial de SFEIR.

## Ton

Profil : fiche de conformité appliquée d'une ESN, en français, destinée aux DPO, RSSI et responsables de traitement. Le texte s'organise autour d'une opposition simple et répétée — déclaration de l'éditeur contre comportement observé, possible contre réel — qui structure les sections. Le registre est prudent : encadré « pas un conseil juridique », qualification des rôles RGPD renvoyée au DPO, décompilation d'une application tierce présentée comme demandant « en principe » l'accord de l'éditeur. Les capacités de l'outil sont attribuées à son README, et un test public est cité avec ses résultats et ses ratés. La section finale décline une chaîne de décision concrète (preuve, demande d'explication, désactivation, blocage, retrait, mise à jour du registre). FAQ factuelle, conclusion sur l'offre AI Cyber.

## Pense-betes

- **Base RGPD** : registre des traitements (article 30) et encadrement des transferts hors UE (chapitre V). Rôle de l'éditeur (sous-traitant, responsable distinct ou conjoint) à qualifier avec le DPO.
- **Sources de fuite** : SDK d'analytics, outils de suivi des plantages, services publicitaires embarqués.
- **Statique avec REA** (selon README) : Electron/JS → modules, imports, routes, canaux IPC ; .NET → métadonnées, dépendances ; **APK** → manifeste, classes, méthodes via **JADX** ; natif → chaînes, symboles via Ghidra/Hopper/IDA.
- **À chercher** : URL et domaines en dur, bibliothèques de télémétrie connues, permissions mobiles, points où identifiant / e-mail / localisation partent vers le réseau. Chaque trouvaille est localisée dans le fichier → vérifiable.
- **Repère Electron** (Ishank Choudhary) : **52 s** pour **100 Mo**, comptages conformes à une recherche manuelle, **deux scripts de préchargement manqués**.
- **Possible vs réel** : un domaine présent peut ne jamais être appelé ; une URL peut être construite à l'exécution → **capture réseau** nécessaire ; REA relit des captures **HAR / SAZ**.
- **Confinement** : REA n'est pas un bac à sable ; VM dédiée, compte de test sans données réelles, trafic via proxy d'inspection. Inspecter n'autorise pas forcément exécuter ou intercepter (DISCLAIMER de REA). **La capture contient des données personnelles.**
- **Écart constaté** → tracer donnée / domaine / version / preuve → décision : explication du fournisseur, désactivation, blocage réseau, mise à jour du registre, retrait.
- **Droit** : **L122-6-1 III** — observer, étudier, tester pendant un usage autorisé ; décompilation : interopérabilité (IV) ou correction d'erreurs (arrêt Top System) → audit de confidentialité fondé d'abord sur l'**observation**.

## RésuméDe400mots

Cet article de SFEIR, publié le 18 octobre 2026, s'adresse aux délégués à la protection des données qui doivent savoir ce qu'une application tierce envoie réellement. Le RGPD impose à chaque responsable de traitement de tenir un registre de ses traitements et d'encadrer les transferts de données hors de l'Union. Pour un logiciel installé sur les postes ou les téléphones de l'entreprise, ce registre repose souvent sur la seule déclaration de l'éditeur. Les outils de rétro-ingénierie par agents, comme REA, rendent la vérification du comportement réel plus accessible, et c'est l'écart entre déclaration et comportement qui intéresse le DPO.

Un éditeur qui embarque un SDK d'analytics, un outil de suivi des plantages ou un service publicitaire fait sortir des données que sa politique de confidentialité décrit plus ou moins fidèlement. Vérifier ce comportement fait partie de la diligence attendue.

La première étape est l'analyse statique, qui lit le logiciel sans l'exécuter. Selon sa documentation, REA restitue les modules et canaux d'une application Electron, le manifeste et les classes d'une APK Android, les chaînes et symboles d'un binaire natif. On y cherche les domaines inscrits en dur, les bibliothèques de télémétrie connues, les permissions demandées et les endroits où une donnée personnelle part vers le réseau. Un test public sur une application Electron donne un ordre de grandeur : 52 secondes pour une archive de 100 Mo, avec des résultats conformes à une recherche manuelle mais deux scripts manqués.

L'analyse statique montre ce qui est possible ; seule la capture du trafic montre ce qui se passe. Un domaine présent dans le code peut ne jamais être appelé, une adresse peut être construite à l'exécution. Il faut donc exécuter l'application, dans une machine virtuelle dédiée, avec un compte de test et un proxy d'inspection, REA sachant relire les captures enregistrées. La capture contient elle-même des données personnelles et se traite comme telle.

Un écart constaté se documente — quelle donnée, vers quel domaine, dans quelle version, avec quelle preuve — puis appelle une décision : demande d'explication, désactivation, blocage, mise à jour du registre ou retrait. Sur le plan juridique, le Code de la propriété intellectuelle permet à l'utilisateur légitime d'observer et de tester le fonctionnement d'un logiciel, mais limite la décompilation à l'interopérabilité ou à la correction d'erreurs. Un audit de confidentialité s'appuie donc d'abord sur l'observation, la décompilation d'une application tierce demandant en principe l'accord de l'éditeur.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | RGPD : vérifier ce qu'une application envoie vraiment | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| RGPD | CONCEPT | s_applique_à | responsable de traitement | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | pour une application tierce, le registre des traitements repose souvent sur la seule déclaration de l'éditeur | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| audit de télémétrie | METHODOLOGIE | utilise | REA | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| audit de télémétrie | METHODOLOGIE | utilise | analyse statique | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| audit de télémétrie | METHODOLOGIE | utilise | capture réseau | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | utilise | JADX | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le statique montre le possible, la capture montre le réel | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Ishank Choudhary | PERSONNE | mesure | 52 secondes pour analyser une archive Electron de 100 Mo, deux scripts de préchargement manqués | MESURE | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | exécuter l'application en VM dédiée, avec un compte de test et un proxy d'inspection | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | une capture réseau contient elle-même des données personnelles | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | permet | observer, étudier et tester le fonctionnement d'un logiciel lors d'un usage autorisé | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | fonder l'audit de confidentialité d'abord sur l'observation, la décompilation d'un logiciel tiers demandant l'accord de l'éditeur | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | documenter chaque écart (donnée, domaine, version, preuve) avant décision du responsable de traitement | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| RGPD | CONCEPT | référence | Règlement (UE) 2016/679 ; registre des traitements (art. 30), transferts hors UE (chap. V) | AJOUT |
| audit de télémétrie | METHODOLOGIE | définition | Vérification des données réellement émises par une application, par analyse statique puis capture réseau isolée | AJOUT |
| capture réseau | METHODOLOGIE | formats | HAR, SAZ ; exécution en VM dédiée avec proxy d'inspection | AJOUT |
| REA | TECHNOLOGIE | catégorie | Serveur MCP de rétro-ingénierie (Reverse Engineer Anything) | AJOUT |
| Ishank Choudhary | PERSONNE | rôle | Auteur d'un test public de REA sur une application Electron (HackerNoon) | AJOUT |
| article L122-6-1 du CPI | DOCUMENT | portée | Exceptions d'observation et de décompilation pour l'utilisateur légitime d'un logiciel | AJOUT |
