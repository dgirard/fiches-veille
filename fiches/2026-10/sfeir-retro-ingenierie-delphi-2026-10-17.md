---
themes: [outils-plateformes, architecture-construction]
source: SFEIR
---
# sfeir-retro-ingenierie-delphi-2026-10-17

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **17 octobre 2026** (~900 mots, quatre sources, toutes des dépôts GitHub), fiche technique du cluster SFEIR sur la rétro-ingénierie par agents, dédiée aux applications **Delphi** héritées sans code source. Il part de l'issue #2810 ouverte le 13 octobre sur le dépôt de **REA**, qui propose de décoder statiquement les formulaires VCL : *« For legacy line-of-business software this is often the single richest source of business rules »*. Trois apports. **(A)** Pourquoi Delphi se lit mal dans **Ghidra** ou IDA (classes sans nom, appels indirects par VMT) alors que l'exécutable conserve une partie de ses métadonnées, et que chaque formulaire `.dfm` est rangé en ressource RCDATA (signature TPF0) contenant composants, gestionnaires d'événements et SQL en clair. **(B)** Les outils qui restaurent ces symboles : **IDR** couplé à **dhrake**, et **DelphiReSym** (BSD-3-Clause, Ghidra 11.3+, Delphi 2010 à Delphi 13 Florence). **(C)** L'ordre des opérations : restaurer d'abord les symboles, puis laisser l'agent lire un pseudocode nommé ; *« Sans cette étape, l'agent passe son temps à deviner ce que les outils spécialisés savent déjà. »* Au 17 octobre, REA ne cite pas Delphi parmi ses cibles. Texte parallèle à la fiche SFEIR sur .NET publiée le même jour.

## Titre Article

Applications Delphi : ce que Ghidra et les agents permettent

## Date

2026-10-17

## URL

https://www.sfeir.com/articles/retro-ingenierie-delphi/

## Keywords

Delphi, C++Builder, VCL, formulaires .dfm, RCDATA, TPF0, rétro-ingénierie, décompilation, Ghidra, IDA, VMT, RTTI, métadonnées, symboles, IDR, Interactive Delphi Reconstructor, dhrake, DelphiReSym, pyghidra, REA, issue #2810, règles métier, SQL embarqué, rétro-documentation, legacy sans code source, golden master, malware Delphi, confinement, Software Factory

## Authors

SFEIR AI (voix éditoriale du cabinet), article non signé individuellement — sfeir.com, site éditorial de SFEIR.

## Ton

Profil : fiche technique d'une ESN, en français, registre d'état des lieux outillé adressé aux DSI et équipes de modernisation qui héritent d'applications Delphi. L'article est daté avec insistance (« au 17 octobre 2026 ») et signale ce qui n'existe pas encore (le décodage des formulaires dans REA est une proposition ouverte). Le texte privilégie l'outillage spécialisé et situe l'agent comme couche de lecture et de synthèse qui « ne remplace ni DelphiReSym ni IDR ». Les détails techniques (signature TPF0, versions couvertes, prérequis Ghidra) viennent des README cités. Le workflow final est énoncé en impératifs successifs (inventoriez, restaurez, extrayez, faites analyser, faites relire). FAQ courte, conclusion sur l'offre Software Factory.

## Pense-betes

- **Problème** : Ghidra/IDA voient un exécutable Delphi comme un x86 quelconque → fonctions anonymes, classes sans nom, appels via **VMT**. Or le binaire garde **RTTI, VMT, structures de classes**.
- **Formulaires = source la plus riche** : chaque `.dfm` en ressource **RCDATA**, signature **TPF0** → arbre des composants, gestionnaires d'événements, liaisons de champs, **SQL en clair**. Issue REA **#2810** (13 octobre 2026) : ouverte, non implémentée au 17 octobre.
- **IDR** (Interactive Delphi Reconstructor) extrait les symboles → script IDC → **dhrake** (huettenhain) : DhrakeInit l'importe dans Ghidra, DhrakeParseClass reconstruit une classe depuis sa VMT.
- **DelphiReSym** (WenzWenzWenz, **BSD-3-Clause**) : directement dans Ghidra, **Ghidra 11.3+** (pyghidra intégré) ; **Delphi 2010 → Delphi 13 Florence** ; Delphi 2009 non testé faute de binaires. Conçu aussi pour l'analyse de **malwares Delphi**.
- **REA** ne liste pas Delphi parmi ses cibles ; il pilote Ghidra comme sur tout binaire natif.
- **Ordre** : symboles d'abord (DelphiReSym ou IDR+dhrake), agent ensuite sur un pseudocode nommé.
- **Rôle de l'agent** : rapprocher événements et écrans, relever les requêtes SQL, proposer des règles de gestion — conclusions à vérifier.
- **Workflow** : inventaire exécutables/bibliothèques + version Delphi → restauration des symboles → extraction des formulaires (explorateur de ressources) → analyse par l'agent → relecture des règles par les utilisateurs → réécriture sous **golden master**.
- **Précautions** : VM ou conteneur pour tout binaire de provenance incertaine ; cadre juridique de la décompilation.

## RésuméDe400mots

Cet article de SFEIR, publié le 17 octobre 2026, fait le point sur la rétro-ingénierie des applications Delphi dont le code source a été perdu, et sur la place qu'y prennent les agents. Il s'ouvre sur une proposition déposée le 13 octobre sur le dépôt de l'outil REA : décoder statiquement les formulaires des applications Delphi et C++Builder, présentés par leur auteur comme souvent la source la plus riche de règles métier dans un logiciel de gestion ancien.

Les décompilateurs génériques comme Ghidra et IDA traitent un exécutable Delphi comme n'importe quel binaire x86 : fonctions anonymes, classes sans nom, appels indirects à travers des tables de méthodes virtuelles. Le pseudocode est difficile à lire. Pourtant, le compilateur Delphi laisse dans l'exécutable une partie des métadonnées : informations de types, tables de méthodes virtuelles, structures de classes. Les formulaires sont rangés dans des ressources binaires identifiables qui contiennent l'arbre des composants, les noms des gestionnaires d'événements, les liaisons de champs et, souvent, le SQL en clair. Au 17 octobre, REA ne sait pas encore les décoder.

Plusieurs outils restaurent ces symboles. IDR extrait les symboles d'un binaire Delphi ; dhrake les importe ensuite dans Ghidra et reconstruit les classes à partir de leurs tables virtuelles. DelphiReSym, sous licence BSD, travaille directement dans Ghidra à partir de la version 11.3 et couvre les versions de Delphi 2010 à Delphi 13 Florence ; il a été conçu à la fois pour l'analyse de logiciels malveillants et d'applications legacy.

REA ne cite pas Delphi parmi ses cibles : il pilote Ghidra sur l'exécutable comme sur tout binaire natif. L'article insiste sur l'ordre des opérations : restaurer d'abord les symboles avec les outils spécialisés, puis laisser l'agent lire un pseudocode où classes et méthodes portent un nom. L'agent accélère alors la lecture et la synthèse — rapprocher événements et écrans, relever les requêtes, proposer des règles de gestion — sans remplacer ces outils, et ses conclusions doivent être vérifiées.

Le workflow proposé enchaîne inventaire des exécutables et de la version de Delphi, restauration des symboles, extraction des formulaires, analyse par l'agent et relecture des règles par les utilisateurs. La réécriture suit, sécurisée par un golden master alimenté par l'application d'origine. Tout binaire de provenance incertaine s'ouvre en machine virtuelle ou en conteneur, et la décompilation reste soumise à son cadre juridique.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Applications Delphi : ce que Ghidra et les agents permettent | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | un exécutable Delphi conserve après compilation une partie de ses métadonnées de classes | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| formulaires VCL | CONCEPT | fait_partie_de | Delphi | TECHNOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| formulaires VCL | CONCEPT | permet | extraction des règles métier et du SQL embarqué | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| DelphiReSym | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| DelphiReSym | TECHNOLOGIE | s_applique_à | Delphi | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| DelphiReSym | TECHNOLOGIE | permet | restauration des symboles Delphi | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| dhrake | TECHNOLOGIE | utilise | IDR | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| dhrake | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| IDR | TECHNOLOGIE | permet | restauration des symboles Delphi | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | REA ne cite pas Delphi parmi ses cibles et ne décode pas encore les formulaires VCL au 17 octobre 2026 | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | restaurer les symboles avant de faire lire le pseudocode par l'agent | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| rétro-documentation | METHODOLOGIE | s_applique_à | Delphi | TECHNOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | ouvrir tout binaire de provenance incertaine en machine virtuelle ou conteneur | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| Delphi | TECHNOLOGIE | catégorie | Environnement de développement Pascal objet (VCL), fréquent dans les applications de gestion legacy | AJOUT |
| formulaires VCL | CONCEPT | définition | Fichiers .dfm stockés en ressource RCDATA (signature TPF0) : composants, événements, SQL | AJOUT |
| DelphiReSym | TECHNOLOGIE | catégorie | Extension Ghidra de restauration de symboles Delphi (BSD-3-Clause, Delphi 2010 à 13) | AJOUT |
| dhrake | TECHNOLOGIE | catégorie | Scripts Ghidra qui importent les symboles IDR et reconstruisent les classes depuis la VMT | AJOUT |
| IDR | TECHNOLOGIE | catégorie | Interactive Delphi Reconstructor, extracteur de symboles Delphi | AJOUT |
| REA | TECHNOLOGIE | catégorie | Serveur MCP de rétro-ingénierie (Reverse Engineer Anything) | AJOUT |
| rétro-documentation | METHODOLOGIE | définition | Reconstitution de la documentation d'une application à partir de ses binaires | AJOUT |
