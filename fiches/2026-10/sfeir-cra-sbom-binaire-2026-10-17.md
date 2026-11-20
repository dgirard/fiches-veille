---
themes: [politique-regulation, qualite-securite]
source: SFEIR
---
# sfeir-cra-sbom-binaire-2026-10-17

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **17 octobre 2026** (~1 300 mots, une frise, quatre sources dont le texte du règlement), page réglementaire du cluster SFEIR sur la rétro-ingénierie par agents. Il part de l'ouverture par l'**ENISA**, le **11 septembre 2026**, de la plateforme unique de signalement du **Cyber Resilience Act** (règlement UE **2024/2847**). Trois apports. **(A)** Un calendrier restitué depuis le texte : entrée en vigueur le 10 décembre 2024 ; obligations de signalement de l'article 14 depuis septembre 2026, avec alerte précoce sous **24 h**, notification sous **72 h**, rapport final **14 jours** après la mesure corrective ; application générale (exigences essentielles, marquage CE) le **11 décembre 2027**. **(B)** Le statut de la **SBOM** : exigence de l'annexe I, lisible par machine, couvrant au minimum les dépendances de premier niveau, applicable en 2027 et que le fabricant n'est pas tenu de transmettre à ses clients. Une DSI qui achète pour son usage interne *« n'est pas fabricant, mais elle hérite du problème »*. **(C)** Une méthode en quatre temps avec **REA** — analyser, extraire bibliothèques et versions, recouper avec les CVE, produire un inventaire daté qui garde visibles ses inconnues — lues *« comme un trou dans l'inventaire, jamais comme une absence de composant »*. Texte jumeau de la fiche SFEIR sur l'audit de binaire fournisseur, publiée le même jour.

## Titre Article

Cyber Resilience Act et SBOM : inventorier un binaire livré sans inventaire

## Date

2026-10-17

## URL

https://www.sfeir.com/articles/cra-sbom-binaire/

## Keywords

Cyber Resilience Act, CRA, règlement (UE) 2024/2847, ENISA, plateforme unique de signalement, Single Reporting Platform, article 14, vulnérabilité activement exploitée, incident grave, alerte précoce 24 heures, notification 72 heures, rapport final, marquage CE, exigences essentielles, annexe I, SBOM, nomenclature logicielle, dépendances de premier niveau, fabricant, DSI, CSIRT coordinateur, REA, Ghidra, cargo-auditable, CVE, inventaire daté, rétro-ingénierie, AI Cyber

## Authors

SFEIR AI (voix éditoriale du cabinet), article non signé individuellement — sfeir.com, site éditorial de SFEIR.

## Ton

Profil : article de veille réglementaire appliquée d'une ESN, en français, destiné aux DSI, RSSI et responsables conformité. Le registre est explicatif et précis : articles et annexe du règlement cités, dates exactes, délais en heures et en jours, distinction nette entre ce qui s'applique déjà (signalement) et ce qui viendra (exigences essentielles, SBOM). Le texte prend soin de qualifier le périmètre : qui est fabricant, qui ne l'est pas, ce que le règlement n'impose pas (transmettre la SBOM au client). La partie méthode est sobre, en quatre verbes, et insiste sur la discipline de lecture des inconnues. Deux précautions closent le développement (confinement, provenance de l'outil après l'épisode du faux dépôt). Encadré « pas un conseil juridique », FAQ factuelle, conclusion sur l'offre AI Cyber.

## Pense-betes

- **CRA** = règlement (UE) **2024/2847**, exigences de cybersécurité pour les produits comportant des éléments numériques (matériel et logiciel), sur tout le cycle de vie ; en vigueur le **10 décembre 2024**.
- **Qui est visé** : le **fabricant** qui met un produit sur le marché européen. DSI qui intègre un composant dans un produit commercialisé = fabricant. DSI qui achète pour usage interne = pas fabricant, mais doit suivre les vulnérabilités sans SBOM garantie.
- **Article 14 (depuis le 11 septembre 2026)** — vulnérabilité activement exploitée : alerte précoce **24 h**, notification **72 h**, rapport final **14 jours** après mise à disposition du correctif ; incident grave : rapport final **un mois** après la notification de 72 h.
- **Application générale** : **11 décembre 2027** (exigences essentielles, marquage CE).
- **Plateforme ENISA** : « initial operating capability » au 11 septembre 2026, interface web, **sans API**, en anglais ; signalement volontaire (art. 15) plus tard ; le fabricant choisit un **CSIRT coordinateur**.
- **SBOM (annexe I)** : format courant, lisible par machine, au minimum **dépendances de premier niveau** ; s'applique en 2027 ; mise à disposition du client facultative, exigible par les autorités de surveillance.
- **Méthode REA** : natif via Ghidra/Hopper/IDA ; Rust + **cargo-auditable** (crates et versions) ; Go (compilateur, modules) ; .NET (métadonnées, dépendances natives) ; Electron (modules JS). Quatre temps : **analyser → extraire → recouper avec les CVE → inventaire daté** avec inconnues visibles.
- L'inventaire reconstruit **n'est pas la SBOM officielle** : base de travail, preuve de diligence, appui contractuel.
- **Précautions** : environnement isolé (REA n'est pas un bac à sable) ; vérifier la provenance de l'outil (faux dépôt REA avec cheval de Troie en octobre 2026).

## RésuméDe400mots

Cet article de SFEIR, publié le 17 octobre 2026, relie le calendrier du Cyber Resilience Act à un problème pratique : comment inventorier un composant logiciel livré en binaire, sans liste de ses dépendances. Il part d'un événement daté : le 11 septembre 2026, l'ENISA a ouvert la plateforme unique sur laquelle les fabricants doivent désormais notifier les vulnérabilités activement exploitées et les incidents graves touchant leurs produits.

Le Cyber Resilience Act, règlement européen 2024/2847 entré en vigueur le 10 décembre 2024, impose des exigences de cybersécurité aux produits comportant des éléments numériques. Il vise le fabricant. Une DSI qui intègre un composant tiers dans un produit qu'elle commercialise le devient ; une DSI qui achète un logiciel pour son usage interne ne l'est pas, mais doit malgré tout suivre les vulnérabilités de ce qu'elle exploite, sans que ses fournisseurs soient tenus de lui remettre une nomenclature.

Deux dates structurent le calendrier. Depuis septembre 2026, l'article 14 impose une alerte précoce sous 24 heures, une notification sous 72 heures et un rapport final dans les 14 jours suivant la mise à disposition d'un correctif. Le 11 décembre 2027, l'application générale fera entrer en vigueur les exigences essentielles et le marquage CE. La plateforme de l'ENISA fonctionne pour l'instant par interface web, sans API.

Parmi ces exigences essentielles figure la SBOM : le fabricant devra documenter les composants de son produit dans un format lisible par machine, au minimum les dépendances de premier niveau. Cette obligation s'applique en 2027 et n'impose pas de transmettre la SBOM au client. Un binaire sans inventaire crée donc une zone d'ombre : impossible de savoir si une vulnérabilité publiée concerne le produit, et de tenir des délais comptés en heures.

La méthode proposée s'appuie sur un agent équipé de REA, qui lit le binaire sans code source : chaînes et symboles d'un exécutable natif via Ghidra, crates d'un binaire Rust compilé avec cargo-auditable, modules d'un binaire Go, métadonnées d'une assembly .NET. Elle tient en quatre temps : analyser, extraire bibliothèques et versions, recouper avec les CVE, produire un inventaire daté où les inconnues restent visibles. Cet inventaire ne vaut pas SBOM officielle ; il documente la diligence et accélère la réaction. Deux précautions complètent le propos : analyser en environnement isolé et vérifier la provenance de l'outil, un faux dépôt REA ayant diffusé un cheval de Troie en octobre 2026.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Cyber Resilience Act et SBOM : inventorier un binaire livré sans inventaire | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Cyber Resilience Act | DOCUMENT | s_applique_à | fabricants de produits comportant des éléments numériques | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| Cyber Resilience Act | DOCUMENT | affirme_que | alerte précoce sous 24 h, notification sous 72 h, rapport final 14 jours après correctif | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Cyber Resilience Act | DOCUMENT | recommande | documenter les composants par une SBOM lisible par machine, au minimum les dépendances de premier niveau | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| ENISA | ORGANISATION | publie | plateforme unique de signalement CRA | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| plateforme unique de signalement CRA | TECHNOLOGIE | fait_partie_de | Cyber Resilience Act | DOCUMENT | 0.8 | DYNAMIQUE | inféré |
| SFEIR | ORGANISATION | affirme_que | une DSI qui achète pour usage interne n'est pas fabricant mais hérite du suivi des vulnérabilités | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le règlement n'oblige pas le fabricant à transmettre sa SBOM à ses clients | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| inventaire de binaire par agent | METHODOLOGIE | utilise | REA | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| inventaire de binaire par agent | METHODOLOGIE | permet | SBOM | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| inventaire de binaire par agent | METHODOLOGIE | utilise | CVE | CONCEPT | 0.84 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | lire les inconnues de l'analyse comme un trou dans l'inventaire, jamais comme une absence de composant | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | analyser un binaire inconnu en environnement isolé et vérifier la provenance de l'outil | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| Cyber Resilience Act | DOCUMENT | référence | Règlement (UE) 2024/2847 ; signalement depuis le 11/09/2026, application générale le 11/12/2027 | AJOUT |
| ENISA | ORGANISATION | rôle | Agence européenne de cybersécurité, opère la plateforme de signalement CRA | AJOUT |
| plateforme unique de signalement CRA | TECHNOLOGIE | état | Capacité initiale au 11/09/2026, interface web, sans API, en anglais | AJOUT |
| SBOM | CONCEPT | définition | Nomenclature logicielle exigée par l'annexe I du CRA | AJOUT |
| inventaire de binaire par agent | METHODOLOGIE | étapes | Analyser, extraire, recouper avec les CVE, produire un inventaire daté | AJOUT |
| REA | TECHNOLOGIE | catégorie | Serveur MCP de rétro-ingénierie (Reverse Engineer Anything) | AJOUT |
