---
themes: [architecture-construction, transformation-adoption, economie-marche]
source: SFEIR
---
# sfeir-migration-windev-ia-sans-big-bang-2026-10-07

## Veille

Article pilier **SFEIR AI** publié sur sfeir.com le **7 octobre 2026** (~3 300 mots, dix-sept sources, dix guides satellites). Il présente la méthode de SFEIR pour sortir de **WinDev** après le rachat de **PC SOFT** par Volaris Group (Constellation Software). Trois apports. **(A)** Une chronologie sourcée : fin des dongles et passage à l'abonnement en **février 2025** (environ **+43 %** par an selon la Wx Alliance), facturation à la session des applications déployées au printemps 2026 (**290 €** par session et par an au catalogue), deux questions écrites à l'Assemblée nationale, action collective préparée par Linklaters, plan de continuité pour les structures de moins de **10 salariés**. **(B)** Un diagnostic technique : pas de convertisseur possible, parce que les sources sont en partie binaires et que *« le code WinDev vit dans l'IHM »* ; l'IA sert à la **rétro-spécification** (prompt d'archéologie, double exécution, validation métier), pas à la transpilation. **(C)** Une méthode en **six étapes** adossée aux trois gates Define, Plan, Ship — audit, extraction des règles, spécifications, réécriture par agents Claude Code, golden master inversé, bascule HFSQL → PostgreSQL — sous motif **strangler fig**, avec une grille rester / geler / migrer. Applique à un legacy précis le cycle décrit dans [[sfeir-sdlc-ia-cycle-11-phases-2026-06-16]].

## Titre Article

Migration WinDev : réécrire vos applications PC SOFT avec l'IA, sans big bang

## Date

2026-10-07

## URL

https://www.sfeir.com/articles/migration-windev/

## Keywords

migration WinDev, PC SOFT, WLangage, WebDev, WinDev Mobile, HFSQL, PostgreSQL, redevance à la session, Volaris Group, Constellation Software, Wx Alliance, modernisation legacy, rétro-spécification, spec first, prompt d'archéologie, Gherkin, ADR, Software Factory 10x, Claude Code, golden master inversé, non-régression, strangler fig, shadow run, code mort, Java/Spring, .NET, Flutter

## Authors

SFEIR AI, voix éditoriale non signée — publié sur sfeir.com, site éditorial de SFEIR.

## Ton

**Profil** : article pilier d'un dossier de dix guides, publié sur le site d'un cabinet, à destination des DSI et des éditeurs de logiciels bâtis sur WinDev. Français direct, perspective « nous » assumée, nombreuses tables et une FAQ finale.

**Style** : l'article enchaîne contexte (pourquoi sortir en 2026), décomposition (ce que l'on migre, en table), objection traitée (pourquoi pas de convertisseur), méthode (six étapes avec livrable et gate), stack cible, données, coûts, risques, grille de décision. Chaque fait de la chronologie est daté et rattaché à sa source (Next, Wx Alliance, Assemblée nationale, ChannelNews, communiqué PC SOFT).

**Position épistémique** : les chiffres tiers sont qualifiés — le +43 % est *« un calcul de l'association, pas un chiffre de l'éditeur »*, le retour d'expérience de Dev-Booster est cité avec ses propres réserves (*« ne doit pas devenir une estimation automatique »*), la modélisation de Yield Studio est signalée comme construite sur des montants relayés. L'article précise que les procédures sont en cours et que rien n'est jugé au fond, et relève la divergence entre « deux ans » et l'échéance de 2028 du plan de continuité.

## Pense-betes

- **Chronologie** : rachat de PC SOFT finalisé fin 2024, annoncé le 26 mai 2025 ; abonnement en février 2025 (1 068 €/an contre 749 € la mise à jour de dongle) ; sessions au printemps 2026 (290 € catalogue, 225 € en offre Solutions & Services, auto-déclaration puis audit), applications compilées à partir de la version 2026 ; questions écrites n° 16261 et 16481 ; pétition à 1 608 signatures ; réunion Linklaters du 1er septembre avec ~200 entreprises.
- **Plan de continuité** (21 septembre 2026, < 10 salariés) : WINDEV Suite 2025 U5 hors Sessions, 2 290 € HT par an et par licence selon la réponse de PC SOFT, échéance 31 décembre 2028 que la Wx Alliance demande de clarifier.
- **Risque ancien** : raréfaction des développeurs WLangage (Platane) ; la redevance rend visible un risque existant.
- **Ce que l'on migre** : données HFSQL reprises ; règles de gestion extraites puis réécrites ; fenêtres réécrites ; états *« systématiquement sous-estimés »* (Smartshift) ; code mort supprimé (20 à 40 % sur un monolithe mature) ; intégrations matérielles à traiter tôt.
- **Pas de convertisseur** : formats binaires gérés par le GDS ; mode texte depuis la version 25, partiel ; règles dispersées dans les événements de champs, boutons, procédures locales, requêtes.
- **Rétro-spécification** : prompt d'archéologie qui interdit la réécriture et exige règles en langage métier, Gherkin, valeurs en dur et zones d'ombre ; double exécution en sessions distinctes (règle présente deux fois = fiable) ; validation métier. Les modèles sont moins bons sur les langages rares.
- **Six étapes** : audit du patrimoine → extraction des règles (gate Define) → spec.md et plan.md (gate Plan) → réécriture par agents → golden master inversé, divergence nulle (gate Ship) → bascule HFSQL module par module.
- **Golden master inversé** : le LLM propose les entrées, l'application WinDev produit les sorties attendues.
- **Stack** : web d'abord ; Java/Spring + Angular par défaut, .NET pour SI Microsoft ou desktop, TypeScript, Flutter pour le mobile terrain, PostgreSQL.
- **Repère de coût** : Dev-Booster, ~60 fenêtres et 25 000 lignes réécrites en .NET en 19 jours. SFEIR chiffre en livrables, jamais en jours-homme.
- **Garde-fous** : strangler fig, cohabitation sur la même base, shadow run, gel fonctionnel du module. Deux actions sans regret : inventorier les postes déployés et documenter les règles.

## RésuméDe400mots

L'article de SFEIR s'adresse aux DSI et aux éditeurs dont les applications reposent sur WinDev. Depuis le rachat de PC SOFT par Volaris Group, filiale de Constellation Software, l'éditeur est passé à l'abonnement en février 2025 et prépare une facturation à la session des applications déployées, à 290 euros par session et par an au tarif catalogue. Deux questions écrites ont été posées à l'Assemblée nationale, une pétition a circulé et le cabinet Linklaters prépare une action collective. Un plan de continuité vise les structures de moins de dix salariés. À ces signaux s'ajoute la raréfaction des développeurs WLangage.

Selon l'article, une migration WinDev se joue sur deux chantiers : retrouver les règles métier enfouies dans vingt ans de fenêtres et prouver que la nouvelle application se comporte comme l'ancienne. Il n'existe pas de convertisseur : les sources sont en partie binaires et la logique est dispersée dans l'interface, si bien qu'une traduction ligne à ligne perd des règles sans bruit. L'IA est donc employée à la rétro-spécification. Un prompt d'archéologie interdit toute réécriture et demande des règles en langage métier, des scénarios Gherkin et les zones d'ombre ; il est exécuté deux fois dans des sessions distinctes, et seules les règles trouvées deux fois sont tenues pour fiables. Le métier tranche le reste.

La méthode suit six étapes rattachées au SDLC piloté par l'IA de SFEIR et à ses trois gates humaines. L'audit inventorie le patrimoine et isole le code mort. L'extraction produit un référentiel de règles validé, gate Define. Les spécifications par module et le plan d'architecture forment la gate Plan. Des agents Claude Code réécrivent ensuite module par module. Les tests de non-régression suivent un golden master inversé, où le LLM propose des entrées et l'application WinDev fournit les sorties attendues ; un module ne bascule qu'à divergence nulle, gate Ship. La bascule des données HFSQL vers PostgreSQL clôt chaque module, souvent préparée en amont en branchant l'application WinDev sur PostgreSQL.

La stack recommandée privilégie le web, avec Java/Spring et Angular par défaut, .NET, TypeScript ou Flutter selon le contexte. Les risques sont traités par migration progressive (strangler fig), cohabitation sur une base commune, shadow run et gel fonctionnel. Une grille indique quand rester, geler via le plan de continuité ou migrer, et deux actions sont jugées sans regret : inventorier les postes et documenter les règles métier.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Migration WinDev : réécrire vos applications PC SOFT avec l'IA | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| PC SOFT | ORGANISATION | a_créé | WinDev | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Volaris Group | ORGANISATION | fait_partie_de | Constellation Software | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Volaris Group | ORGANISATION | dirige | PC SOFT | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |
| Wx Alliance | ORGANISATION | s_oppose_à | redevance à la session | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | aucun convertisseur WinDev n'est possible car le code vit dans l'IHM | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| rétro-spécification | METHODOLOGIE | s_applique_à | WinDev | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| rétro-spécification | METHODOLOGIE | utilise | prompt d'archéologie | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| méthode de migration WinDev en six étapes | METHODOLOGIE | est_basé_sur | cycle SFEIR à 11 phases | METHODOLOGIE | 0.9 | STATIQUE | déclaré_article |
| méthode de migration WinDev en six étapes | METHODOLOGIE | utilise | golden master inversé | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| méthode de migration WinDev en six étapes | METHODOLOGIE | utilise | strangler fig | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| méthode de migration WinDev en six étapes | METHODOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.86 | DYNAMIQUE | déclaré_article |
| PostgreSQL | TECHNOLOGIE | remplace | HFSQL | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| suppression du code mort | METHODOLOGIE | réduit | 20 à 40 % du code d'un monolithe mature | MESURE | 0.8 | ATEMPOREL | déclaré_article |
| Dev-Booster | ORGANISATION | mesure | ~60 fenêtres et 25 000 lignes WLangage réécrites en .NET en 19 jours | MESURE | 0.82 | STATIQUE | déclaré_article |
| Wx Alliance | ORGANISATION | mesure | environ +43 % par an avec l'abonnement | MESURE | 0.8 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | migrer les données HFSQL vers PostgreSQL avant de réécrire l'application | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | inventorier les postes déployés et documenter les règles métier | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet de conseil, éditeur de sfeir.com | AJOUT |
| PC SOFT | ORGANISATION | statut | Éditeur de WinDev, contrôlé par Volaris Group depuis fin 2024 | AJOUT |
| WinDev | TECHNOLOGIE | catégorie | Atelier de développement d'applications de gestion (WLangage), passé à l'abonnement en 2025 | AJOUT |
| HFSQL | TECHNOLOGIE | catégorie | Base de données propriétaire de PC SOFT | AJOUT |
| Wx Alliance | ORGANISATION | rôle | Association d'utilisateurs WinDev, présidée par Patrick Lalemand | AJOUT |
| Volaris Group | ORGANISATION | rôle | Acquéreur de PC SOFT via Two Squared France II | AJOUT |
| rétro-spécification | METHODOLOGIE | définition | L'IA écrit d'abord la spécification de l'ancien code, le nouveau code vient après | AJOUT |
| golden master inversé | METHODOLOGIE | définition | Le LLM propose les entrées, l'application d'origine produit les sorties attendues | AJOUT |
| strangler fig | METHODOLOGIE | définition | Migration progressive où une façade route chaque fonction vers l'ancien ou le nouveau système | AJOUT |
| méthode de migration WinDev en six étapes | METHODOLOGIE | définition | Audit, extraction des règles, spécifications, réécriture par agents, non-régression, bascule HFSQL | AJOUT |
