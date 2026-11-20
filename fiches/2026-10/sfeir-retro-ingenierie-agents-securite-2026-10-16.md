---
themes: [qualite-securite, agents-codage-ia-skills, outils-plateformes]
source: SFEIR
---
# sfeir-retro-ingenierie-agents-securite-2026-10-16

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **16 octobre 2026** (mis à jour le 23 octobre ; ~1 400 mots, un schéma, huit sources), page d'entrée d'un cluster d'une vingtaine d'articles sur la rétro-ingénierie par agents. Point de départ : le dépôt **REA** (Reverse Engineer Anything), serveur MCP qui donne à un agent de code les outils d'un rétro-ingénieur (**Ghidra**, Hopper, IDA, analyseurs JavaScript, Electron, .NET, Android), passé de **76 998** étoiles GitHub le 11 octobre à **369 860** le 23. Trois apports. **(A)** Le coût de la compréhension d'un logiciel fermé s'effondre : Connor Turland cartographie **Slack 4.52** (529 fichiers JavaScript, 1 904 modules, 45 canaux IPC) en une dizaine de minutes ; *« how much curiosity costs »*. **(B)** La frontière boîte noire / boîte blanche se déplace : l'attaquant se rapproche de la boîte blanche depuis le binaire, tandis que le défenseur possède déjà le code source de ses applications. **(C)** Le code interne passe en premier, avec deux chiffres cités (**2 436** vulnérabilités trouvées par **GLM-5.3** dans 269 projets open source selon Z.ai ; **14,14 → 54,3** vulnérabilités critiques et élevées par application chez Sonatype, 2022-2026). L'article pose ensuite les contraintes : confinement (REA *« n'est pas un bac à sable »*), faux dépôts, **207** outils MCP à gouverner, revue experte des sorties, cadre juridique (directive 2009/24/CE, article L122-6-1 du CPI). Recoupe la fiche SFEIR sur les limites de REA.

## Titre Article

Rétro-ingénierie par agents : ce que ça change pour les équipes sécurité

## Date

2026-10-16

## URL

https://www.sfeir.com/articles/retro-ingenierie-agents-securite/

## Keywords

rétro-ingénierie, reverse engineering, REA, Reverse Engineer Anything, serveur MCP, agent de code, Ghidra, IDA, Hopper, Electron, Slack, boîte noire, boîte blanche, test d'intrusion, red team, code interne, legacy, défragilisation, GLM-5.3, Sonatype, vulnérabilités, confinement, sandbox, faux dépôts, supply chain, malware, firmware, télémétrie, Cyber Resilience Act, directive 2009/24/CE, décompilation, AI Cyber

## Authors

SFEIR AI (voix éditoriale du cabinet), article non signé individuellement — sfeir.com, site éditorial de SFEIR.

## Ton

Profil : article pilier d'une ESN, en français, registre d'analyse sécurité adressé aux RSSI, équipes sécurité et éditeurs de logiciels. L'ouverture est factuelle et datée (compteur d'étoiles à deux dates, source pour chacune), puis le texte bascule sur une question opérationnelle unique : combien de temps faut-il à un attaquant pour comprendre un logiciel fermé ? La structure est pédagogique : définition des deux postures (boîte noire, boîte blanche) avec exemples concrets de failles, puis conséquence pour la défense, puis contraintes. Le texte fonctionne comme une page-hub : la majorité des paragraphes renvoient vers des articles détaillés du cluster (sandbox, malware, firmware, APK, Electron, obfuscation). Un encadré précise que la page n'est pas un conseil juridique. Les FAQ répondent par des phrases courtes et symétriques (« Les deux », « Oui »). La conclusion présente l'offre AI Cyber de SFEIR (analyse par agents, preuve par test, relance à chaque nouveau modèle).

## Pense-betes

- **REA** (Reverse Engineer Anything, dépôt `morluto/rea`) : serveur MCP qui outille un agent de code pour la rétro-ingénierie — **Ghidra / Hopper / IDA** pour le natif, analyseurs statiques pour JavaScript, Electron, .NET, Android. **76 998** étoiles le 11 octobre 2026 (+25 793 en un jour), **369 860** le 23 octobre.
- **Cas Slack** (Connor Turland, 20 octobre) : Slack 4.52.171 → **529** fichiers JS, **1 904** modules, **45** canaux IPC, **8** add-ons natifs, logique « Ne pas déranger » reconstituée en ~10 minutes. Formule : ce qui change, c'est *« how much curiosity costs »*.
- **Boîte noire** = auditeur extérieur sans code (pentest, red team, injection de prompt). **Boîte blanche** = avec le code source, chercher comment l'exploiter (concaténation SQL, route sans contrôle d'accès, désérialisation). Les agents rapprochent l'attaquant de la boîte blanche à partir du binaire (pseudocode, chaînes, appels).
- **Avantage du défenseur** : il a déjà le code source. Faire lire ce code par les mêmes modèles, **un prompt par projet et par type de faille**, un bug à la fois, preuve par test.
- **Code interne d'abord** : audité une fois puis de moins en moins. Z.ai : **2 436** vulnérabilités trouvées par **GLM-5.3** dans **269** projets, âge moyen **26,6 ans**. Sonatype (cohorte fixe juin 2022 → juin 2026) : **14,14 → 54,3** vulnérabilités critiques/élevées par application.
- **Politique plutôt qu'audit** : relancer l'analyse du stock **à chaque nouveau modèle**, legacy d'abord ; modèle à poids ouverts en réseau fermé possible (Aikido Altar).
- **Usages défensifs** : audit de binaire fournisseur (lien CRA/SBOM), malware en local, firmware IoT, télémétrie RGPD, APK, audit de logiciel extra-européen ; côté éditeurs : secrets dans l'ASAR Electron, valeur de l'obfuscation.
- **Contraintes** : REA **n'est pas un sandbox** (SECURITY.md) ; faux dépôt avec cheval de Troie dès le **13 octobre** ; version 6.7.0 = **207 outils MCP** à gouverner ; l'agent se trompe et peut être trompé par le binaire → revue par analyste ; crackmes/CTF pour former.
- **Juridique** : décompilation encadrée par la **directive 2009/24/CE** et l'**article L122-6-1 du CPI** ; posséder un fichier ne donne pas toute permission (DISCLAIMER de REA).

## RésuméDe400mots

Publié par SFEIR le 16 octobre 2026 et mis à jour le 23, cet article examine ce que la rétro-ingénierie assistée par agents change pour les équipes de sécurité. Il part de REA (Reverse Engineer Anything), un serveur MCP qui met à disposition d'un agent de code les outils d'un rétro-ingénieur : Ghidra, Hopper ou IDA pour le code natif, et des analyseurs statiques pour JavaScript, Electron, .NET ou Android. Le dépôt GitHub est passé de 76 998 étoiles le 11 octobre à 369 860 le 23.

Premier constat : le coût de la compréhension d'un logiciel fermé s'effondre. Connor Turland a fait analyser Slack par REA et obtenu en une dizaine de minutes une cartographie de 529 fichiers JavaScript, 1 904 modules et 45 canaux IPC, avec la logique du mode Ne pas déranger. Or comprendre un logiciel précède souvent l'attaque : repérer un endpoint non documenté, une clé embarquée, un contrôle fait côté client. Cette étape demandait des années de pratique ; elle tient dans une session d'agent supervisée.

Deuxième constat : la frontière entre boîte noire et boîte blanche se déplace. L'attaquant qui n'a que le binaire obtient à faible coût du pseudocode et une cartographie des appels. Le défenseur, lui, dispose déjà du code source de ses applications ; c'est son avantage s'il l'exploite le premier, en faisant lire ce code par les mêmes modèles, avec un prompt adapté à chaque projet et chaque type de faille.

Troisième constat : le code interne doit passer en premier. Moins audité que le code exposé, il contient probablement des failles anciennes. L'article cite les 2 436 vulnérabilités revendiquées par Z.ai pour GLM-5.3 dans 269 projets open source, âgées en moyenne de 26,6 ans, et les données de Sonatype montrant une hausse de 14,14 à 54,3 vulnérabilités critiques et élevées par application entre 2022 et 2026. La défragilisation devient une politique, relancée à chaque nouveau modèle.

Les mêmes outils servent la défense : audit de binaires fournisseurs, analyse de malware en local, firmware, télémétrie. Ils imposent aussi des précautions : REA n'est pas un bac à sable, des faux dépôts ont diffusé un cheval de Troie, 207 outils MCP doivent être gouvernés, et les sorties de l'agent se relisent par un analyste. Le cadre juridique européen et français encadre la décompilation de logiciels tiers. L'article recommande de commencer par le code interne, en boîte blanche, en environnement confiné.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Rétro-ingénierie par agents : ce que ça change pour les équipes sécurité | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | est_instance_de | serveur MCP | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | IDA | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | permet | rétro-ingénierie par agents | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | mesure | 369 860 étoiles GitHub le 23 octobre 2026 | MESURE | 0.9 | STATIQUE | déclaré_article |
| Connor Turland | PERSONNE | référence | Slack | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Connor Turland | PERSONNE | affirme_que | « how much curiosity costs » | CITATION | 0.85 | STATIQUE | déclaré_article |
| rétro-ingénierie par agents | METHODOLOGIE | réduit | coût de compréhension d'un logiciel fermé | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les agents rapprochent l'attaquant de la boîte blanche à partir du binaire | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | auditer d'abord le code interne en boîte blanche, en environnement confiné | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| GLM-5.3 | TECHNOLOGIE | mesure | 2 436 vulnérabilités dans 269 projets open source, âge moyen 26,6 ans | MESURE | 0.8 | STATIQUE | déclaré_article |
| Sonatype | ORGANISATION | mesure | 14,14 → 54,3 vulnérabilités critiques et élevées par application (2022-2026) | MESURE | 0.82 | STATIQUE | déclaré_article |
| analyse en boîte blanche | METHODOLOGIE | s_applique_à | code interne legacy | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | REA n'est pas un bac à sable : tout binaire inconnu s'ouvre en environnement isolé | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | mesure | 207 outils MCP en version 6.7.0 | MESURE | 0.84 | STATIQUE | déclaré_article |
| directive 2009/24/CE | DOCUMENT | s_applique_à | rétro-ingénierie par agents | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | a_créé | AI Cyber | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| REA | TECHNOLOGIE | catégorie | Serveur MCP de rétro-ingénierie (Reverse Engineer Anything, dépôt morluto/rea) | AJOUT |
| rétro-ingénierie par agents | METHODOLOGIE | définition | Session d'agent supervisée qui décompile et cartographie un logiciel fermé | AJOUT |
| analyse en boîte blanche | METHODOLOGIE | définition | Audit du code source pour chercher comment un attaquant l'exploiterait | AJOUT |
| Connor Turland | PERSONNE | rôle | Auteur d'un test de REA sur Slack (atcyrus.com) | AJOUT |
| GLM-5.3 | TECHNOLOGIE | catégorie | Modèle de Z.ai utilisé pour la recherche de vulnérabilités | AJOUT |
| Sonatype | ORGANISATION | secteur | Sécurité de la chaîne logicielle | AJOUT |
| directive 2009/24/CE | DOCUMENT | objet | Protection juridique des programmes d'ordinateur (encadre la décompilation) | AJOUT |
| AI Cyber | TECHNOLOGIE | catégorie | Offre SFEIR de défragilisation du code en boîte blanche par agents | AJOUT |
