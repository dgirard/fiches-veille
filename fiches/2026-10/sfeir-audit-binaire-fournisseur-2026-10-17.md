---
themes: [qualite-securite, politique-regulation, outils-plateformes]
source: SFEIR
---
# sfeir-audit-binaire-fournisseur-2026-10-17

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **17 octobre 2026** (~1 300 mots, six sources), rattaché au cluster SFEIR sur la rétro-ingénierie par agents. Il part du calendrier du **Cyber Resilience Act** : signalement à l'**ENISA** des vulnérabilités activement exploitées depuis le **11 septembre 2026**, documentation des composants (dont une nomenclature logicielle) exigée à partir du **11 décembre 2027**. Question posée à la DSI qui intègre un composant livré en binaire : que contient-il, qu'appelle-t-il, quelles bibliothèques embarque-t-il ? Trois apports. **(A)** Ce que **REA** restitue selon la cible : pseudocode, chaînes et appels sur du natif (avec **Ghidra**, Hopper ou IDA), modules et canaux IPC sur Electron, métadonnées et CIL sur .NET, crates et versions sur un binaire Rust compilé avec cargo-auditable, modules sur Go, signataire Authenticode sur Windows. **(B)** Le passage du constat à un *« embryon de SBOM »*, croisé avec les CVE, qui complète ou vérifie la SBOM du fournisseur sans la remplacer. **(C)** Le cadre : audit confiné en VM ou conteneur, analyse statique d'abord, clause d'audit au contrat, article **L122-6-1** du CPI (observation protégée, décompilation plus strictement encadrée). Recoupe la fiche SFEIR sur les limites de REA.

## Titre Article

Auditer un binaire fournisseur sans son code source

## Date

2026-10-17

## URL

https://www.sfeir.com/articles/audit-binaire-fournisseur/

## Keywords

audit de binaire, composant fournisseur, due diligence logicielle, code source absent, rétro-ingénierie, REA, Ghidra, Electron, .NET, Rust, cargo-auditable, Go, Authenticode, SBOM, nomenclature logicielle, CVE, Cyber Resilience Act, ENISA, signalement de vulnérabilités, confinement, analyse statique, clause d'audit, article L122-6-1, décompilation, interopérabilité, arrêt Top System, divulgation coordonnée, Sonatype, AI Cyber

## Authors

SFEIR AI (voix éditoriale du cabinet), article non signé individuellement — sfeir.com, site éditorial de SFEIR.

## Ton

Profil : fiche pratique d'une ESN, en français, registre de conseil opérationnel adressé aux DSI, acheteurs et RSSI qui intègrent des composants tiers. L'ouverture est réglementaire et datée (deux échéances du CRA), puis le texte déroule un parcours en quatre temps : le problème, ce que l'outil révèle, ce qu'on en fait, comment le faire sans risque. La partie technique est descriptive et attribue chaque capacité au README de REA (« selon son README ») plutôt que de la revendiquer. Le texte borne systématiquement la portée : l'inventaire « ne remplace pas » la SBOM du fournisseur, chaque trouvaille « doit être relue », les inconnues sont « assumées ». Un encadré rappelle que la page n'est pas un conseil juridique ; la partie droit distingue observation et décompilation avec précision. FAQ en réponses brèves, conclusion sur l'offre AI Cyber.

## Pense-betes

- **Calendrier CRA** (règlement UE 2024/2847) : signalement à l'**ENISA** des vulnérabilités activement exploitées depuis le **11 septembre 2026** ; exigences essentielles, dont documentation des composants via **SBOM**, au **11 décembre 2027**.
- **Composants concernés** : pilote d'équipement, module d'export comptable, client lourd d'éditeur, agent de supervision — livrés compilés, avec droits étendus et accès réseau.
- **Volume de failles** : Sonatype, cohorte fixe juin 2022 → juin 2026, **14,14 → 54,3** vulnérabilités critiques et élevées par application.
- **Ce que REA renvoie, par cible** (selon son README) :
  - natif (+ Ghidra/Hopper/IDA) : pseudocode, assembleur, chaînes, symboles, appels ;
  - JavaScript / Electron : modules, imports, routes, canaux IPC, add-ons natifs, sans exécution ;
  - .NET : métadonnées, CIL, dépendances natives, sans charger le code ;
  - **Rust + cargo-auditable** : noms, versions, sources des crates ; **Go** : version du compilateur, modules ; **Windows signé** : signataire Authenticode.
- REA rend aussi **ce qu'il n'a pas résolu** → localise les trous de l'inventaire.
- **Embryon de SBOM** croisé avec les **CVE** ; le CRA n'oblige pas le fournisseur à remettre sa SBOM au client → l'inventaire client complète, vérifie ou supplée, et sert de **pièce de diligence datée**.
- **Confinement** : REA n'est pas un bac à sable (le binaire est parsé avec vos droits) → VM/conteneur dédié, statique d'abord, aucun secret dans l'environnement ; les résultats partent chez le fournisseur du modèle.
- **Contrat** : droit d'audit technique, remise d'une SBOM, notification des vulnérabilités.
- **Droit français** : **L122-6-1 CPI** — observer, étudier, tester le fonctionnement pendant un usage autorisé, clause contraire nulle ; décompilation sans autorisation limitée à l'**interopérabilité** ou, selon l'arrêt **Top System**, à la correction d'erreurs.
- Vulnérabilité trouvée → preuves, **divulgation coordonnée**, mesures compensatoires.

## RésuméDe400mots

Publié par SFEIR le 17 octobre 2026, cet article explique comment une DSI peut auditer un composant logiciel livré par un fournisseur sous forme binaire, sans code source ni inventaire. Le contexte est réglementaire : depuis le 11 septembre 2026, le Cyber Resilience Act impose aux fabricants de signaler à l'ENISA les vulnérabilités activement exploitées, et à partir du 11 décembre 2027 ses exigences essentielles leur demanderont de documenter les composants de leurs produits, notamment par une nomenclature logicielle.

Beaucoup de composants arrivent compilés — pilotes, modules d'export, clients lourds, agents de supervision — et tournent pourtant avec des droits étendus. Répondre aux questions de base (bibliothèques et versions, domaines contactés, permissions, secrets en dur) demandait plusieurs jours de spécialiste. L'article rappelle la hausse mesurée par Sonatype, de 14,14 à 54,3 vulnérabilités critiques et élevées par application entre 2022 et 2026.

Les agents de rétro-ingénierie rendent cette due diligence abordable. REA orchestre des outils existants et renvoie chaque conclusion avec ses preuves et ses limites. Sa couverture dépend du binaire : pseudocode et chaînes sur un exécutable natif, modules et canaux IPC sur une application Electron, métadonnées et instructions CIL sur une assembly .NET. Certaines cibles servent directement l'inventaire : les crates d'un binaire Rust compilé avec cargo-auditable, les modules d'un binaire Go, le signataire d'un exécutable Windows. REA signale aussi ce qu'il n'a pas pu résoudre, ce qui montre où l'inventaire reste incomplet ; chaque trouvaille doit être relue.

Reconstituer bibliothèques et versions produit un embryon de SBOM, que l'on croise avec les bases de CVE. Comme le règlement n'oblige pas le fournisseur à transmettre sa SBOM au client, cet inventaire la complète, la vérifie ou pallie son absence, et constitue une pièce de diligence datée.

L'audit doit être confiné : REA n'est pas un bac à sable, et l'ouverture d'un binaire le fait analyser avec les droits de l'utilisateur. D'où une VM ou un conteneur dédié, l'analyse statique en premier et le choix du modèle selon la sensibilité des données. Sur le plan juridique, le cas le plus sain est un contrat prévoyant droit d'audit, remise de SBOM et notification des vulnérabilités. À défaut, l'article L122-6-1 du Code de la propriété intellectuelle protège l'observation du fonctionnement lors d'un usage autorisé, tandis que la décompilation reste encadrée plus strictement. Une vulnérabilité découverte se traite par divulgation coordonnée.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Auditer un binaire fournisseur sans son code source | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Cyber Resilience Act | DOCUMENT | s_applique_à | fabricants de produits comportant des éléments numériques | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Cyber Resilience Act | DOCUMENT | utilise | ENISA | ORGANISATION | 0.8 | DYNAMIQUE | inféré |
| Cyber Resilience Act | DOCUMENT | recommande | documenter les composants par une nomenclature logicielle à partir du 11 décembre 2027 | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| audit de binaire fournisseur | METHODOLOGIE | utilise | REA | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | cargo-auditable | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| audit de binaire fournisseur | METHODOLOGIE | permet | SBOM | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| SBOM | CONCEPT | utilise | CVE | CONCEPT | 0.8 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | l'inventaire par agent complète ou vérifie la SBOM du fournisseur sans la remplacer | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Sonatype | ORGANISATION | mesure | 14,14 → 54,3 vulnérabilités critiques et élevées par application (2022-2026) | MESURE | 0.82 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | confiner l'audit en VM ou conteneur dédié, en analyse statique d'abord | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | prévoir au contrat droit d'audit, remise d'une SBOM et notification des vulnérabilités | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | permet | observer, étudier et tester le fonctionnement d'un logiciel lors d'un usage autorisé | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | s_applique_à | décompilation à des fins d'interopérabilité | CONCEPT | 0.82 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | traiter une vulnérabilité découverte par divulgation coordonnée | AFFIRMATION | 0.84 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| audit de binaire fournisseur | METHODOLOGIE | définition | Due diligence d'un composant tiers livré compilé, par agent de rétro-ingénierie confiné | AJOUT |
| REA | TECHNOLOGIE | catégorie | Serveur MCP de rétro-ingénierie (Reverse Engineer Anything) | AJOUT |
| Cyber Resilience Act | DOCUMENT | échéances | Signalement ENISA au 11/09/2026 ; exigences essentielles au 11/12/2027 | AJOUT |
| SBOM | CONCEPT | définition | Nomenclature logicielle des composants et versions embarqués | AJOUT |
| article L122-6-1 du CPI | DOCUMENT | portée | Exceptions d'observation et de décompilation pour l'utilisateur légitime d'un logiciel | AJOUT |
| cargo-auditable | TECHNOLOGIE | rôle | Outil Rust qui embarque la liste des crates dans le binaire | AJOUT |
