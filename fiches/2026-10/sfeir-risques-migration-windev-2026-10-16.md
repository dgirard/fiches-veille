---
themes: [architecture-construction, qualite-securite, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-risques-migration-windev-2026-10-16

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **16 octobre 2026** (~1 700 mots, un schéma, cinq sources), volet « risques » de la série SFEIR sur la migration **WinDev** assistée par l'IA. Point de départ : la réécriture de NomadBiz par **Dev-Booster** en **19 jours**, dont dix de tests et corrections pour cinq de réécriture. Thèse affichée : *« Les migrations WinDev qui échouent le font rarement pour une raison technique. »* Trois apports. **(A)** Dix risques nommés, chacun suivi de sa parade : big bang (→ motif **strangler fig**), règles métier oubliées (→ prompt d'archéologie exécuté deux fois), états sous-estimés, lots invisibles, matériel, tests écrits par le LLM, dérive du legacy pendant le projet, conduite du changement, données, dépendance à une personne clé. **(B)** Le risque jugé le plus sous-estimé : un LLM qui écrit à la fois les tests et les valeurs attendues *« fige son interprétation »* ; la parade est le **golden master inversé** (le LLM propose les entrées, l'application WinDev produit les sorties), complété par un score de mutation. **(C)** Un risque transverse : la fiabilité moindre des modèles sur les langages rares, où SFEIR classe le **WLangage**, d'où double exécution et relecture par un connaisseur. Prolonge [[sfeir-sdlc-ia-cycle-11-phases-2026-06-16]], dont les trois gates humains structurent la méthode.

## Titre Article

Migration WinDev : les 10 risques qui font échouer un projet, et comment les maîtriser

## Date

2026-10-16

## URL

https://www.sfeir.com/articles/risques-migration-windev/

## Keywords

migration WinDev, WLangage, modernisation legacy, big bang, strangler fig, règles métier, prompt d'archéologie, états, reporting, traitements par lots, matériel, Flutter, tests de non-régression, golden master inversé, score de mutation, PIT, mutmut, rework rate, gel fonctionnel, conduite du changement, HFSQL, PostgreSQL, migration de données, rétro-documentation, personne clé, shadow traffic, langages rares, software factory

## Authors

SFEIR AI (voix éditoriale du cabinet), article non signé individuellement — sfeir.com, site éditorial de SFEIR.

## Ton

Profil : article méthodologique d'une ESN, en français, registre de retour d'expérience structuré en liste numérotée, destiné aux DSI, chefs de projet et éditeurs qui préparent la sortie de WinDev. Chaque risque suit le même gabarit à deux temps, « Le risque » / « La parade », ce qui donne au texte une lecture de check-list. Le ton est concret : exemples précis (remise « à partir de 10 articles » codée `> 10`, douchettes et balances, montants en flottant) plutôt que généralités. Les sources externes sont des acteurs du même marché (Dev-Booster, Smartshift, Winfall, Platane) et un article du blog sfeir.dev, cités entre guillemets. La prudence porte sur la transposition des délais (« Sans cette connaissance, le délai n'a aucun sens »). La FAQ tranche en une ou deux phrases. La conclusion renvoie vers la méthode SFEIR et le SDLC piloté par l'IA.

## Pense-betes

- **Repère de délai** : NomadBiz (Dev-Booster) réécrit en **19 jours** = **5 de réécriture + 10 de tests/corrections** (+ le reste). Non transposable : *« nous connaissions déjà NomadBiz, ses utilisateurs et ses règles de gestion »*.
- **Les 10 risques → parades** :
  1. **Big bang** → **strangler fig** : façade qui route module par module ; chaque module migré est débranché de l'ancien.
  2. **Règles métier oubliées** → extraction avant le code, **prompt d'archéologie exécuté deux fois** dans deux sessions, liste de zones d'ombre validée par le métier.
  3. **États** (factures, étiquettes) → inventaire dès l'audit, comparaison PDF/image dans le golden master ; poste *« systématiquement sous-estimé »* (Smartshift).
  4. **Lots invisibles** → recenser planificateurs, services, exécutables secondaires.
  5. **Matériel** (douchettes, imprimantes thermiques, balances) → dès la gate Plan ; conditionne web / desktop / Flutter.
  6. **Tests écrits par le LLM** → **golden master inversé** + score de mutation (**PIT**, **mutmut**).
  7. **Dérive du legacy** → gel fonctionnel du module, recapture du golden master après chaque changement.
  8. **Conduite du changement** → utilisateurs clés dès l'extraction, mesure des parcours (clics, temps de saisie).
  9. **Données** (orphelins, doublons, flottants) → migrations à blanc, recalcul des totaux métier des deux côtés (HFSQL → PostgreSQL).
  10. **Personne clé** → **rétro-documentation comme premier livrable** ; *« les développeurs WLangage se raréfient »* (Platane).
- **Piège du test LLM** : commentaire « remise à partir de 10 articles », code `> 10` → le test LLM échoue sur l'existant → quelqu'un « corrige » le code = règle de facturation changée. Gonfle le **rework rate**.
- **Winfall** : tests C# *« dont les valeurs attendues sont capturées sur l'application d'origine »*.
- **Transverse** : modèles moins fiables sur les langages rares (COBOL, RPG, ABAP, PL/I selon Hamadi Jabloun ; WLangage selon SFEIR) → double exécution + relecture.
- **Fin de cohabitation** : quand le **shadow traffic** ne révèle plus de divergence sur une période représentative, **clôture mensuelle comprise**.

## RésuméDe400mots

Cet article de SFEIR, publié le 16 octobre 2026, recense les dix risques qui font le plus souvent échouer la migration d'une application WinDev et associe à chacun une parade issue de la méthode du cabinet. Il part d'un cas public : Dev-Booster a réécrit son application NomadBiz en dix-neuf jours, dont dix de tests et de corrections pour cinq de réécriture. Sa thèse : ces migrations échouent rarement pour une raison technique, mais parce qu'une règle disparaît, qu'un état est découvert en recette ou qu'un test vert ne prouve rien.

Le premier risque est le big bang, la bascule de toute l'application en un week-end ; la parade est une migration progressive selon le motif strangler fig, module par module. Viennent ensuite les règles métier oubliées, traitées par une extraction préalable avec un prompt d'archéologie exécuté deux fois et une liste de zones d'ombre validée par le métier ; les états (factures, étiquettes), à inventorier dès l'audit et à comparer en sortie ; les traitements par lots invisibles dans l'interface ; et le matériel piloté directement (douchettes, balances, imprimantes), qui conditionne le choix de la cible.

Le sixième risque est présenté comme le plus sous-estimé : lorsque le modèle écrit les tests, il écrit aussi les valeurs attendues à partir de sa lecture du code et fige son interprétation. L'exemple donné est celui d'un commentaire annonçant une remise à partir de dix articles alors que le code teste strictement plus de dix : un test généré échoue, quelqu'un corrige le code, et une règle de facturation change. La parade est le golden master inversé, où le modèle propose les entrées et l'application d'origine produit les sorties, complété par un score de mutation.

Les quatre derniers risques sont la dérive de l'application pendant le projet (gel fonctionnel du module en cours), la conduite du changement (utilisateurs clés associés tôt, parcours mesurés), la qualité des données (migrations à blanc, totaux recalculés des deux côtés) et la dépendance à une personne clé, à laquelle répond une rétro-documentation livrée en premier.

Un risque transverse pèse sur toutes les étapes : les modèles sont moins fiables sur les langages rares, catégorie où SFEIR range le WLangage. Toute sortie sur le code source doit être recoupée par double exécution et relue par un connaisseur. L'ancienne application reste en service jusqu'à ce que le trafic rejoué en parallèle ne montre plus de divergence, clôture mensuelle comprise.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Migration WinDev : les 10 risques qui font échouer un projet | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les migrations WinDev échouent rarement pour une raison technique | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| migration WinDev | METHODOLOGIE | s_applique_à | WinDev | TECHNOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Dev-Booster | ORGANISATION | mesure | NomadBiz réécrit en 19 jours, dont 10 de tests et corrections | MESURE | 0.88 | STATIQUE | déclaré_article |
| strangler fig | METHODOLOGIE | résout | risque du big bang | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| golden master inversé | METHODOLOGIE | résout | tests écrits par le LLM qui figent son interprétation du code | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| golden master inversé | METHODOLOGIE | utilise | score de mutation | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| prompt d'archéologie | METHODOLOGIE | résout | règles métier oubliées | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| rétro-documentation | METHODOLOGIE | réduit | dépendance à une personne clé | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les tests écrits par le LLM sont le risque le plus sous-estimé | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Smartshift | ORGANISATION | affirme_que | « systématiquement sous-estimé » (le poste des états WinDev) | CITATION | 0.8 | STATIQUE | déclaré_article |
| Platane | ORGANISATION | affirme_que | « les développeurs WLangage se raréfient » | CITATION | 0.82 | DYNAMIQUE | déclaré_article |
| Hamadi Jabloun | PERSONNE | affirme_que | les modèles perdent en fiabilité sur les langages rares (COBOL, RPG, ABAP, PL/I) | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | double exécution et relecture par un connaisseur de toute sortie du modèle sur du WLangage | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | garder l'application WinDev jusqu'à absence de divergence en shadow traffic, clôture mensuelle comprise | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| migration WinDev | METHODOLOGIE | est_basé_sur | cycle SFEIR à 11 phases | METHODOLOGIE | 0.78 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| WinDev | TECHNOLOGIE | catégorie | Atelier de génie logiciel propriétaire (langage WLangage) | AJOUT |
| migration WinDev | METHODOLOGIE | définition | Réécriture progressive d'une application WinDev assistée par l'IA, six étapes et trois gates | AJOUT |
| golden master inversé | METHODOLOGIE | définition | Le LLM propose les entrées, l'application d'origine produit les sorties attendues | AJOUT |
| strangler fig | METHODOLOGIE | définition | Façade qui route chaque fonction vers l'ancien ou le nouveau système, module par module | AJOUT |
| prompt d'archéologie | METHODOLOGIE | définition | Extraction des règles métier exécutée deux fois dans deux sessions distinctes | AJOUT |
| Dev-Booster | ORGANISATION | rôle | Éditeur ayant réécrit son application WinDev NomadBiz | AJOUT |
| Hamadi Jabloun | PERSONNE | rôle | Auteur sur sfeir.dev (modernisation du legacy avec l'IA) | AJOUT |
