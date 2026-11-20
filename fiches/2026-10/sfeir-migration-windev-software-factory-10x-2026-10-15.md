---
themes: [agents-codage-ia-skills, architecture-construction, transformation-adoption]
source: SFEIR
---
# sfeir-migration-windev-software-factory-10x-2026-10-15

## Veille

Article méthodologique **SFEIR** (non signé) publié sur sfeir.com le **15 octobre 2026** (~8 000 signes, six étapes, un tableau des rôles, deux sources), qui applique le **SDLC SFEIR à onze phases** à la migration d'une application **WinDev**. Point de départ : *« Donner du WLangage à un agent occupe une petite partie du travail ; le reste tient dans le cycle qui l'entoure »*. Trois apports. **(A)** Six étapes posées sur les phases du cycle, chacune avec un livrable vérifiable : audit du patrimoine (`inventaire.md`, 20 à 40 % de code mort selon Hamadi Jabloun), extraction des règles en Gherkin par un **prompt d'archéologie** exécuté deux fois, spécifications (`spec.md`, `plan.md`), réécriture par agents **Claude Code**, non-régression par **golden master**, bascule en shadow run derrière un feature flag. **(B)** Une règle de test : *« le LLM génère les ENTRÉES. Le code legacy, lui seul, génère les SORTIES »*. **(C)** Une répartition de l'effort humain à **80 % planification et revue / 20 % exécution**, trois gates humaines (Define, Plan, Ship) et une mesure en livrables plutôt qu'en jours-homme, avec **−30 % d'itérations de correction** après dix cycles. Prolonge [[sfeir-sdlc-ia-cycle-11-phases-2026-06-16]].

## Titre Article

Migrer WinDev avec la Software Factory 10x : la méthode SFEIR en six étapes, de l'audit à la bascule

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/migration-windev-methode-software-factory-10x/

## Keywords

migration WinDev, WLangage, modernisation legacy, Software Factory 10x, SDLC à onze phases, Claude Code, agents de codage, gates humaines, Define, Plan, Ship, audit de patrimoine, code mort, extraction des règles métier, prompt d'archéologie, Gherkin, spec-driven development, golden master, tests de non-régression, score de mutation, shadow run, feature flag, HFSQL, PostgreSQL, Compound engineering, Rework Rate, context engineering, preuve d'exécution, Diagnostic 10x

## Authors

SFEIR AI (article non signé), voix éditoriale de SFEIR publiée sur sfeir.com, site éditorial du cabinet.

## Ton

**Profil** : article de méthode d'un cabinet, à la première personne du pluriel, pour DSI et responsables d'applications WinDev. Français technique, structuré par étapes avec une répartition explicite « ce que font les agents / ce que font les humains / livrable ».

**Style** : chaque étape est rattachée à une ou plusieurs phases nommées du SDLC maison et se termine par un artefact nommé (`inventaire.md`, fichiers `.feature`, `spec.md`, `golden_master.json`). Deux règles « non négociables » sont isolées en liste. Les références externes sont peu nombreuses : un billet de Hamadi Jabloun sur sfeir.dev et un playbook public anonyme sur GitHub.

**Position épistémique** : les chiffres sont attribués (code mort selon Jabloun, −30 % d'itérations renvoyé à l'article SDLC du cabinet). La gate Ship est décrite comme une validation *« sur preuve d'exécution, jamais sur la déclaration de l'agent »*. La conclusion mentionne les offres et partenariats du cabinet (Diagnostic 10x, SFEIR Institute, Claude Partner Network) dans une section « passer à l'action » distincte de la méthode.

## Pense-betes

- **Contexte** : Claude Code utilisé par les ingénieurs SFEIR depuis le printemps 2025, par chaque Sfeirian depuis début 2026.
- **Cadre** : SDLC à 11 phases (0 Setup → 10 Deprecation), 3 gates humaines (Define, Plan, Ship). Effort humain ~**80 % planification/revue, 20 % exécution** ; *« le code s'écrit vite, et le risque est d'écrire le mauvais »*.
- **Six étapes** :
  - 1 Audit (Setup, Define) → `inventaire.md`, carte des modules, code mort estimé (20-40 %)
  - 2 Extraction des règles (Define) → `.feature` par module ; prompt d'archéologie à 5 sections, lancé dans deux sessions, divergences relues par un humain
  - 3 Spécifications (Plan) → `spec.md` + `plan.md` ; la stack se décide ici
  - 4 Réécriture (Build, Verify, Review) → agents Claude Code, 4 revues parallèles (code, sécurité, tests, performance)
  - 5 Non-régression (Verify) → `golden_master.json`, score de mutation
  - 6 Bascule (Ship) → migrations à blanc HFSQL→PostgreSQL, shadow run jusqu'à divergence nulle, feature flag
- **Règles non négociables** : aucune nouvelle fonctionnalité pendant la migration d'un module ; tout écart où le nouveau code semble plus juste remonte au métier.
- **Golden master inversé** : le LLM propose les entrées, l'application WinDev exécutée produit les sorties.
- **Capitalisation** : Compound-1/2 transforment chaque correction en règle versionnée ; le module 5 profite des erreurs des modules 1 à 4. Deprecation planifie l'extinction des licences et postes.
- **Rôles** : référent métier, tech lead, architecte, binôme de dev, QA (golden master, shadow run), Ops/SRE.
- **Mesure** : livrables, Rework Rate, itérations de correction par module (−30 % après dix cycles).
- **Contexte agent** : module par module, *« un contexte trop large dilue la précision »*.
- **À relier** : [[sfeir-hfsql-postgresql-migration-donnees-2026-10-15]], [[sfeir-windev-agents-rea-clean-room-2026-10-15]].

## RésuméDe400mots

L'article décrit la méthode suivie par SFEIR pour migrer une application WinDev à l'aide d'agents de codage. Il pose d'emblée que confier du code WLangage à un agent ne représente qu'une petite partie du travail ; l'essentiel tient dans le cycle de production qui encadre l'agent.

Ce cycle est le SDLC à onze phases du cabinet, de Setup à Deprecation, dans lequel des humains tiennent trois gates (Define, Plan, Ship) et les agents exécutent le reste. La Software Factory 10x répartit l'effort humain à environ 80 % sur la planification et la revue et 20 % sur l'exécution, ratio que l'article juge particulièrement justifié pour une migration, où le risque principal est d'écrire rapidement le mauvais code.

La méthode compte six étapes. L'audit du patrimoine fait inventorier par les agents fenêtres, procédures, états, requêtes et dépendances, croisés avec les journaux d'usage pour repérer le code mort, estimé entre 20 et 40 % d'un monolithe mature. L'extraction des règles métier applique un prompt d'archéologie qui interdit toute amélioration et produit règles, scénarios Gherkin, valeurs en dur, incohérences et zones d'ombre ; il tourne dans deux sessions distinctes, et les règles qui n'apparaissent qu'une fois sont relues par un humain. Les spécifications décrivent le comportement attendu et l'architecture cible ; aucune construction ne démarre avant la validation du plan. La réécriture est confiée aux agents Claude Code, qui écrivent, testent et corrigent en boucle, sous quatre revues parallèles. Les tests de non-régression reposent sur un golden master où le modèle propose les entrées et l'application WinDev produit les sorties de référence. La bascule fait tourner le module migré en parallèle de l'ancien jusqu'à divergence nulle, puis l'active derrière un feature flag, la validation humaine se faisant sur preuve d'exécution.

Deux règles sont posées comme non négociables : aucune nouvelle fonctionnalité pendant la migration d'un module, et remontée au métier de tout écart où le nouveau code paraît plus juste. Les phases de capitalisation transforment chaque correction en règle réutilisée par les modules suivants, et la phase de dépréciation planifie l'extinction de l'application, des licences et des postes.

Le pilotage se fait en livrables plutôt qu'en jours-homme, avec deux indicateurs de qualité : le taux de travail refait et le nombre d'itérations de correction, réduit d'environ 30 % après dix cycles selon le cabinet. Les développeurs WinDev deviennent relecteurs et arbitres.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Migrer WinDev avec la Software Factory 10x : la méthode SFEIR en six étapes, de l'audit à la bascule | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| méthode de migration WinDev en six étapes | METHODOLOGIE | est_basé_sur | cycle SFEIR à 11 phases | METHODOLOGIE | 0.93 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | a_créé | méthode de migration WinDev en six étapes | METHODOLOGIE | 0.93 | STATIQUE | déclaré_article |
| méthode de migration WinDev en six étapes | METHODOLOGIE | s_applique_à | WinDev | TECHNOLOGIE | 0.94 | ATEMPOREL | déclaré_article |
| méthode de migration WinDev en six étapes | METHODOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| méthode de migration WinDev en six étapes | METHODOLOGIE | utilise | golden master | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| méthode de migration WinDev en six étapes | METHODOLOGIE | utilise | prompt d'archéologie | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| méthode de migration WinDev en six étapes | METHODOLOGIE | utilise | shadow run | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| golden master | METHODOLOGIE | affirme_que | le LLM génère les entrées, le code legacy seul génère les sorties | CITATION | 0.9 | ATEMPOREL | déclaré_article |
| Software Factory 10x | METHODOLOGIE | mesure | effort humain ~80 % planification et revue, 20 % exécution | MESURE | 0.88 | DYNAMIQUE | déclaré_article |
| Hamadi Jabloun | PERSONNE | mesure | 20 à 40 % de code mort dans un monolithe mature | MESURE | 0.82 | ATEMPOREL | déclaré_article |
| prompt d'archéologie | METHODOLOGIE | s_inspire_de | Hamadi Jabloun | PERSONNE | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | aucune nouvelle fonctionnalité pendant la migration d'un module | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | valider la bascule sur preuve d'exécution, jamais sur la déclaration de l'agent | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Compound engineering | METHODOLOGIE | réduit | ~30 % d'itérations de correction après dix cycles | MESURE | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | piloter en livrables et en Rework Rate plutôt qu'en jours-homme | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | collabore_avec | Anthropic | ORGANISATION | 0.8 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | statut | ESN / cabinet d'ingénierie logicielle, partenaire Preferred du Claude Partner Network (5 octobre 2026) | AJOUT |
| méthode de migration WinDev en six étapes | METHODOLOGIE | étapes | Audit, extraction des règles, spécifications, réécriture, non-régression, bascule | AJOUT |
| Software Factory 10x | METHODOLOGIE | principe | Répartition 80/20 de l'effort humain entre planification-revue et exécution | AJOUT |
| prompt d'archéologie | METHODOLOGIE | sections | Règles, scénarios Gherkin, valeurs en dur, incohérences, zones d'ombre ; double exécution | AJOUT |
| golden master | METHODOLOGIE | livrable | golden_master.json par module, comparaison des écritures, états, exports | AJOUT |
| shadow run | METHODOLOGIE | critère | Module migré en parallèle de l'ancien jusqu'à divergence nulle | AJOUT |
| Claude Code | TECHNOLOGIE | usage | Agent d'exécution de la réécriture (Build, Verify, Review) | AJOUT |
| WinDev | TECHNOLOGIE | catégorie | AGL propriétaire en WLangage, source de la migration | AJOUT |
| Hamadi Jabloun | PERSONNE | support | Auteur sur sfeir.dev (modernisation legacy avec l'IA) | AJOUT |
