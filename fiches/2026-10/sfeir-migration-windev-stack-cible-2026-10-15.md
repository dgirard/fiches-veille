---
themes: [architecture-construction, strategie-frameworks, transformation-adoption]
source: SFEIR
---
# sfeir-migration-windev-stack-cible-2026-10-15

## Veille

Article de position **SFEIR** (non signé) publié sur sfeir.com le **15 octobre 2026** (~6 000 signes, une matrice de décision, un arbre de décision, six sources), dans la série du pilier *software factory* sur la sortie de **WinDev**. Il part du réflexe *« nous sommes sous Windows, donc .NET »*, qui *« tombe parfois juste, mais il saute l'examen »*. Trois apports. **(A)** Une position par défaut : **le web d'abord** (back-end en API, front moderne, **PostgreSQL**), qui supprime le déploiement sur poste et ouvre une trajectoire SaaS aux éditeurs ; le desktop et **Flutter** restent pour les exceptions (périphériques, hors-ligne prolongé, postes industriels). **(B)** Une **matrice** croisant quatre cibles (Java/Spring + Angular, .NET, TypeScript, Flutter) et huit critères, présentée explicitement comme *« une position SFEIR »* qu'*« un autre acteur […] remplirait autrement »* ; le couple **Spring Boot + Angular** y est mis en avant, rare selon le texte dans les catalogues des acteurs de la migration. **(C)** Deux chantiers .NET que les devis oublient, rapportés d'après Smartshift : le champ Table WinDev sans équivalent natif, et les états à reconstruire. La stack se décide à la **gate Plan**, après l'inventaire. Pièce de la même série que [[sfeir-hfsql-postgresql-migration-donnees-2026-10-15]].

## Titre Article

WinDev vers Java, .NET, TypeScript ou Flutter : comment choisir sa stack cible

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/migration-windev-choisir-stack-cible/

## Keywords

migration WinDev, stack cible, modernisation legacy, Java, Spring Boot, Angular, .NET, C#, WPF, WinForms, Blazor, TypeScript, Node, React, Electron, Flutter, Dart, WinDev Mobile, PostgreSQL, HFSQL, web d'abord, trajectoire SaaS, matrice de décision, arbre de décision, Google Cloud, Cloud Run, GKE, Cloud SQL, AlloyDB, champ Table, états WinDev, DevExpress, Telerik, gate Plan, WLangage, langages rares

## Authors

SFEIR AI (article non signé), voix éditoriale de SFEIR publiée sur sfeir.com, site éditorial du cabinet.

## Ton

**Profil** : article d'aide à la décision, à la première personne du pluriel, destiné aux DSI et éditeurs de logiciels qui préparent la sortie d'une application WinDev. Français direct, phrases courtes, une matrice, un arbre de décision et une liste de questions.

**Style** : la position est posée d'emblée (« notre position : le web d'abord »), puis justifiée stack par stack en un paragraphe chacune. Les exceptions sont nommées (périphériques, hors-ligne, postes industriels) et traitées comme telles plutôt que comme des contre-arguments. La FAQ ramène la décision dans le calendrier de la méthode (gate Plan, après l'audit).

**Position épistémique** : le texte assume sa subjectivité en précisant que la matrice vient des chantiers et du vivier de recrutement du cabinet. Il signale l'appartenance de SFEIR au statut de Google Cloud Premier Partner à côté de la recommandation GCP. Les limites des modèles sur le langage source sont rapportées d'après Hamadi Jabloun (sfeir.dev), qui observe une chute de qualité sur les langages rares, catégorie où le texte range le WLangage.

## Pense-betes

- **Position par défaut** : cible web (API + front moderne + PostgreSQL) sauf contrainte matérielle forte. Gains : plus de parc à mettre à jour, accès distant, trajectoire SaaS pour un éditeur.
- **Exceptions** : périphériques pilotés en direct, hors-ligne prolongé, postes industriels → client lourd ciblé ou Flutter, le reste en web.
- **Matrice (position SFEIR)** :
  - SI Java ou multi-technologies → Java/Spring + Angular très adapté
  - SI 100 % Microsoft, desktop imposé → .NET très adapté (WPF, WinForms)
  - mobile terrain hors ligne → Flutter très adapté
  - forte volumétrie transactionnelle → Java ou .NET ; Flutter hors sujet
  - vivier de recrutement en France : très large sauf Flutter (en croissance)
- **Java/Spring + Angular** : Spring Boot pour la logique transactionnelle, Angular pour les écrans de gestion denses (« proche dans l'esprit des fenêtres WinDev »), déploiement Cloud Run/GKE + Cloud SQL/AlloyDB.
- **.NET** : cible la plus directe pour un SI Microsoft. Pièges (Smartshift) : champ Table sans équivalent natif (DataGridView insuffisant → DevExpress, Telerik, Syncfusion sous licence) ; états au coût *« systématiquement sous-estimé »*.
- **TypeScript** : applications moyennes, équipes JavaScript ; pour un cœur métier lourd, back-end Java ou .NET + front TypeScript.
- **Flutter** : réponse à WinDev Mobile (Android, iOS, desktop, hors-ligne).
- **Arbre de décision** : desktop imposé ? → .NET ; mobile terrain ? → Flutter ; cœur métier lourd ? → Java/Spring + Angular ; sinon TypeScript.
- **Six questions** : techno maîtrisée et mainteneur à 5 ans, accès hors réseau, matériel piloté, trajectoire SaaS, volumétrie, lieu d'hébergement.
- **Mix de stacks** fréquent ; desktop choisi poste par poste.
- **À relier** : [[sfeir-migration-windev-software-factory-10x-2026-10-15]].

## RésuméDe400mots

L'article de SFEIR aide à choisir la technologie qui remplacera une application WinDev. Il part d'un réflexe répandu, choisir .NET parce que l'entreprise est sous Windows, et soutient que ce choix dépend en réalité du système d'information existant, des équipes, des usages et de la durée de vie visée.

La position du cabinet est de privilégier le web : un back-end exposé en API, un front moderne et une base PostgreSQL. Cette cible supprime le déploiement sur les postes, facilite l'accès à distance et ouvre, pour un éditeur, une trajectoire SaaS où les nouveaux clients signent sur la nouvelle plateforme pendant que le parc existant migre. Les exceptions (périphériques pilotés directement, fonctionnement hors réseau prolongé, postes industriels) se traitent au cas par cas, par un client lourd ciblé ou par Flutter.

Une matrice de décision compare quatre cibles (Java/Spring avec Angular, .NET, TypeScript et Flutter) sur huit critères : SI existant, maintien du desktop, cible web, mobile terrain, volumétrie, vivier de recrutement en France et hébergement sur Google Cloud. L'article précise qu'il s'agit d'une position tirée de ses chantiers, qu'un autre acteur remplirait autrement.

Le couple Spring Boot et Angular est mis en avant : Spring pour la logique métier transactionnelle, Angular pour des écrans de gestion denses, l'ensemble déployé sur Cloud Run ou GKE avec PostgreSQL managé. .NET reste la cible la plus directe pour un SI Microsoft qui doit rester desktop ; l'article reprend deux difficultés signalées par Smartshift, l'absence d'équivalent natif au champ Table de WinDev et la reconstruction des états, souvent sous-estimée. TypeScript convient aux applications de taille moyenne et aux équipes orientées JavaScript. Flutter répond aux usages de WinDev Mobile, avec une base de code unique et une bonne gestion du hors-ligne.

Quelle que soit la stack, PostgreSQL est recommandé comme socle commun ; un arbre de décision en trois questions (desktop imposé, mobile terrain, cœur métier lourd) résume la grille. Six questions préalables sont proposées, de la technologie maîtrisée par le SI au lieu d'hébergement des données.

La FAQ précise que la stack se décide à la gate Plan, après l'inventaire et l'extraction des règles, que plusieurs stacks peuvent coexister, que le desktop n'est pas condamné, et que les modèles d'IA sont à l'aise sur toutes les cibles, la difficulté se situant du côté du WLangage, langage rare.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | WinDev vers Java, .NET, TypeScript ou Flutter : comment choisir sa stack cible | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | une cible web (API, front moderne, PostgreSQL) sauf contrainte matérielle forte | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | Spring Boot | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | Angular | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | PostgreSQL | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| .NET | TECHNOLOGIE | s_applique_à | SI 100 % Microsoft avec application desktop | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Flutter | TECHNOLOGIE | remplace | WinDev Mobile | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| TypeScript | TECHNOLOGIE | s_applique_à | applications de taille moyenne et équipes orientées JavaScript | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| Smartshift | ORGANISATION | affirme_que | le champ Table WinDev n'a pas d'équivalent natif en .NET et le coût des états est sous-estimé | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| matrice de décision de stack cible | METHODOLOGIE | s_applique_à | WinDev | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | a_créé | matrice de décision de stack cible | METHODOLOGIE | 0.9 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la stack se décide à la gate Plan, après l'inventaire et l'extraction des règles | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Hamadi Jabloun | PERSONNE | affirme_que | la qualité des modèles chute sur les langages rares (COBOL, RPG, ABAP, PL/I) | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | collabore_avec | Google Cloud | ORGANISATION | 0.85 | DYNAMIQUE | déclaré_article |
| Airmessoft | ORGANISATION | concurrence | SFEIR | ORGANISATION | 0.75 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | statut | ESN / cabinet d'ingénierie logicielle, Google Cloud Premier Partner | AJOUT |
| WinDev | TECHNOLOGIE | catégorie | AGL propriétaire (WLangage), source des migrations | AJOUT |
| matrice de décision de stack cible | METHODOLOGIE | contenu | 4 cibles × 8 critères, position assumée du cabinet | AJOUT |
| Spring Boot | TECHNOLOGIE | rôle | Back-end transactionnel recommandé, avec Angular | AJOUT |
| Angular | TECHNOLOGIE | rôle | Front pour écrans de gestion denses | AJOUT |
| .NET | TECHNOLOGIE | rôle | Cible la plus directe pour un SI Microsoft desktop (WPF, WinForms) | AJOUT |
| Flutter | TECHNOLOGIE | rôle | Mobile terrain et hors-ligne, base de code unique | AJOUT |
| PostgreSQL | TECHNOLOGIE | rôle | Socle de données commun à toutes les cibles | AJOUT |
| Smartshift | ORGANISATION | activité | Prestataire de migration WinDev vers .NET | AJOUT |
| Hamadi Jabloun | PERSONNE | support | Auteur sur sfeir.dev (modernisation legacy avec l'IA) | AJOUT |
