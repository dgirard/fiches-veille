---
themes: [qualite-securite, strategie-frameworks, politique-regulation]
source: SFEIR
---
# sfeir-budgets-2027-dette-securite-2026-11-08

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **8 novembre 2026** (~24 000 signes, neuf sections, une FAQ, 17 sources notées), destiné aux DSI et RSSI qui bouclent leurs budgets 2027. Il rapproche deux chiffres de **Bank of America** : **1 000 personnes** relisant **200 millions** de lignes pour l'an 2000 (audition au Congrès du 24 mars 1998), et **1 000 prestataires** recrutés au deuxième trimestre 2026 pour corriger les failles mises au jour par des modèles comme **Claude Mythos** (Brian Moynihan sur CNBC, 14 octobre 2026). Trois apports. **(A)** L'analogie et sa limite : une dette ancienne rendue visible d'un coup, mais sans cause unique ni échéance, puisque chaque génération de modèles relit le même code ; *« Le chantier devient permanent. »* **(B)** Un état du stock et du flux : **82 %** des organisations portent une dette de sécurité (Veracode), **129 000** vulnérabilités vérifiées par les partenaires de Glasswing, CVE NVD multipliées par **2,24**, **75 %** du nouveau code de Google généré par IA. **(C)** Une distinction budgétaire tirée de *Antifragile* de **Taleb** : une ligne qui paie le choc (relecture et correction du stock) et une ligne qui fait baisser la facture suivante (retrait de code, contrôle du code généré, correction outillée, clauses fournisseurs), pilotée par le **coût d'une faille corrigée** d'une génération de modèles à l'autre. Cadre réglementaire : lettre de la **BCE**, articles 25 et 30 de **DORA**, Cyber Resilience Act. Fait suite à [[sfeir-exploit-goulot-delai-correction-2026-11-06]].

## Titre Article

Budgets 2027 : il faut défragiliser le SI

## Date

2026-11-08

## URL

https://www.sfeir.com/articles/budgets-2027-dette-securite-bug-an-2000/

## Keywords

budgets 2027, défragiliser, dette de sécurité, bug de l'an 2000, Bank of America, Brian Moynihan, Claude Mythos, Project Glasswing, remédiation, prestataires, Veracode, State of Software Security, NVD, CVE, code généré par IA, Antifragile, Taleb, via negativa, décommissionnement, dépendances, CodeMender, Codex Security, VulnCheck, exploitabilité, coût d'une faille corrigée, BCE, DORA, Cyber Resilience Act, clauses fournisseurs, droit d'audit, DSI, RSSI

## Authors

SFEIR AI, voix éditoriale du cabinet SFEIR, article non signé individuellement, publié sur sfeir.com.

## Ton

**Profil** : tribune budgétaire pour DSI, RSSI et comités de direction, publiée sur le site d'un cabinet en période de préparation des budgets. Français soutenu, ouverture historique, référence littéraire (Taleb), FAQ finale.

**Registre** : argumentation par analogie, bornée explicitement (*« La comparaison s'arrête au calendrier »*). Les chiffres d'éditeurs sont signalés comme tels (Veracode *« vend les outils pour réduire cette dette »*, chiffres d'Anthropic et de Google *« invérifiables de l'extérieur »*), et l'article précise ce que mesure un volume de CVE : l'activité de ceux qui cherchent autant que l'insécurité du logiciel.

**Posture** : prescriptive et assumée. L'article reconnaît la rationalité du choix de Bank of America à court terme tout en le classant dans la catégorie « encaisser ». Il se termine par une déclaration de partenariat : *« SFEIR est partenaire d'Anthropic et de Google : lisez cet article avec ce filtre. »*

## Pense-betes

- **1998** : audition du 24 mars, John LaFalce cite Bank of America — **1 000 personnes**, **200 M** de lignes, **250 M$** ; estimation SPR de **700 000 années-personnes** ; 200 000 recrutements dans le conseil et l'audit.
- **2026** : Brian Moynihan (CNBC, 14 octobre) — **1 000 prestataires** recrutés au T2 pour corriger les failles trouvées par l'IA dans son code et celui de ses fournisseurs, en renfort de 3 000 personnes ; *« That risk is real risk »*. Plus de **200 M$** de charges du T3 couvrent deux remédiations (Mythos et anti-blanchiment) ; *« we expect that the Mythos remediation costs run down »*.
- **Analogie et limite** : même mécanisme (dette dormante rendue visible, correction en heures humaines) ; l'an 2000 avait une cause unique et une échéance, les failles trouvées par IA non.
- **Glasswing** (7 avril 2026) : failles de **27 ans** dans OpenBSD et de **16 ans** dans FFmpeg.
- **Stock** (Veracode/Cyentia, 1,6 M d'applications) : dette de sécurité (failles ouvertes > 1 an) chez **82 %** des organisations (74 % un an plus tôt), critique chez **60 %** ; **243 jours** pour corriger la moitié des failles ; ~10 % de l'arriéré fermé par mois ; deux tiers de la dette critique viennent du code tiers, 358 jours de demi-correction.
- **Flux** : **129 000** vulnérabilités vérifiées par les partenaires Glasswing (avril-juillet), plus de 33 000 critiques ou hautes ; NVD **92 319** CVE de janvier à octobre 2026 (×2,24) ; 516 corrigées sur 6 157 signalées aux mainteneurs ; exploitation 7 jours avant le correctif en moyenne (Mandiant 2025).
- **Code neuf** : 75 % du nouveau code de Google généré par IA (avril 2026) ; Veracode : faille dans **38 %** des tâches de génération (44 % en juillet), meilleurs modèles à 73 % de réussite, les moins sûrs entre 44 et 50 %.
- **Taleb** : fragile / robuste / antifragile ; Bank of America a acheté *« de quoi encaisser »*. **Défragiliser** = que chaque vague coûte moins cher que la précédente.
- **Leviers** : *via negativa* (décommissionner, supprimer code mort et dépendances, retirer les privilèges) ; sécurité au moment de la génération (règles données à l'agent, revue avant fusion, tests en CI, choix du modèle) ; correction industrialisée (CodeMender, Codex Security ; priorisation par exploitabilité : **2 sur 300** failles exploitées selon VulnCheck) ; chaîne de livraison en heures ; clauses fournisseurs avec délai de correction et droit d'audit.
- **Budget** : deux lignes — choc (dimensionner sur une application représentative puis extrapoler) et sortie du choc. Indicateur : **coût d'une faille corrigée** d'une génération de modèles à l'autre.
- **Régulation** : lettre de **Claudia Buch** (BCE) début juillet 2026, plans attendus fin octobre ; **DORA** art. 25 (examens du code source) et art. 30 (droits d'accès, d'inspection et d'audit chez le prestataire TIC) ; **Cyber Resilience Act**, signalement des vulnérabilités exploitées depuis le **11 septembre 2026** (éditeurs, pas le code maison).

## RésuméDe400mots

L'article ouvre sur deux scènes. En mars 1998, devant une commission du Congrès, un élu cite Bank of America : mille personnes relisent deux cents millions de lignes de code pour le passage à l'an 2000. En octobre 2026, le dirigeant de la même banque explique avoir fait entrer mille prestataires pour corriger les failles que des modèles d'IA comme Claude Mythos ont mises au jour dans son code et celui de ses fournisseurs. SFEIR y voit l'ordre de grandeur qui manquait aux DSI et RSSI en pleine préparation des budgets 2027.

Le mécanisme est commun : une dette dormait dans le code et devient visible d'un coup, et sa correction se paie en heures humaines. La différence tient au calendrier. Le bug de l'an 2000 avait une cause et une date ; les failles trouvées par les modèles n'ont ni l'une ni l'autre, chaque génération relisant le même code avec de meilleurs yeux.

Le stock est important : selon Veracode, plus de quatre organisations sur cinq portent des failles ouvertes depuis plus d'un an, et la moitié des failles met des mois à être corrigée. Le flux grossit : découvertes massives revendiquées par les partenaires de Project Glasswing, CVE publiées plus que doublées sur un an, mainteneurs qui ne suivent pas, exploitation qui précède le correctif. Le code neuf, de plus en plus généré par IA, contient encore des failles dans plus d'un tiers des tâches mesurées.

Reprenant la distinction de Taleb entre fragile, robuste et antifragile, l'article classe le choix de Bank of America parmi les achats qui permettent d'encaisser la vague actuelle sans réduire le coût de la suivante. Défragiliser consiste à faire baisser ce coût vague après vague : retirer du code, des dépendances et des privilèges, sécuriser le code au moment de sa génération, financer la correction plutôt que de nouveaux scanners, prioriser par l'exploitabilité, livrer un correctif en quelques heures et contractualiser délais et droits d'audit avec les fournisseurs.

Pour le comité budgétaire, il propose deux lignes : l'une paie le choc, dimensionnée en passant une application représentative au crible, l'autre paie la sortie du choc. Un indicateur suffit à juger la seconde : le coût d'une faille corrigée, suivi d'une génération de modèles à l'autre.

Le cadre réglementaire pousse dans le même sens : la BCE a demandé aux grandes banques un plan face aux risques cyber de l'IA de frontière, DORA prévoit revues de code et droits d'audit, le Cyber Resilience Act oblige les éditeurs à signaler les failles exploitées.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Budgets 2027 : il faut défragiliser le SI | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Brian Moynihan | PERSONNE | dirige | Bank of America | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Bank of America | ORGANISATION | mesure | 1 000 prestataires recrutés au T2 2026 pour corriger les failles trouvées par l'IA | MESURE | 0.92 | STATIQUE | déclaré_article |
| Bank of America | ORGANISATION | utilise | Claude Mythos | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les failles révélées par l'IA reproduisent le bug de l'an 2000 sans date de fin | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| défragiliser | METHODOLOGIE | s_inspire_de | Antifragile | DOCUMENT | 0.9 | ATEMPOREL | déclaré_article |
| Nassim Nicholas Taleb | PERSONNE | a_créé | Antifragile | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| défragiliser | METHODOLOGIE | réduit | coût d'une faille corrigée d'une génération de modèles à l'autre | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| Veracode | ORGANISATION | mesure | 82 % des organisations portent une dette de sécurité, 60 % une dette critique | MESURE | 0.88 | STATIQUE | déclaré_article |
| Veracode | ORGANISATION | mesure | faille dans 38 % des tâches de génération de code par IA en octobre 2026 | MESURE | 0.86 | STATIQUE | déclaré_article |
| Project Glasswing | EVENEMENT | mesure | 129 000 vulnérabilités vérifiées entre avril et juillet 2026 | MESURE | 0.85 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | a_créé | Project Glasswing | EVENEMENT | 0.92 | STATIQUE | déclaré_article |
| CodeMender | TECHNOLOGIE | permet | correctif prouvé par un test et relu par un humain | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Codex Security | TECHNOLOGIE | concurrence | CodeMender | TECHNOLOGIE | 0.78 | DYNAMIQUE | inféré |
| BCE | ORGANISATION | recommande | plans des grandes banques face aux risques cyber de l'IA de frontière | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Claudia Buch | PERSONNE | travaille_chez | BCE | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |
| règlement DORA | DOCUMENT | affirme_que | examens du code source et droits d'audit chez les prestataires TIC pour les fonctions critiques | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Cyber Resilience Act | DOCUMENT | s_applique_à | fabricants de produits comportant des éléments numériques | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | séparer au budget 2027 la ligne qui paie le choc de celle qui fait baisser la facture suivante | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | retirer code mort, dépendances et privilèges inutiles avant d'ajouter | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Bank of America | ORGANISATION | fait | 1 000 relecteurs pour l'an 2000 (1998), 1 000 prestataires pour les failles Mythos (2026) | AJOUT |
| Brian Moynihan | PERSONNE | rôle | Dirigeant de Bank of America | AJOUT |
| défragiliser | METHODOLOGIE | définition | Faire en sorte que chaque vague de découvertes de failles coûte moins cher que la précédente | AJOUT |
| dette de sécurité | CONCEPT | définition | Failles connues restées ouvertes plus d'un an (Veracode) | AJOUT |
| Antifragile | DOCUMENT | référence | Nassim Nicholas Taleb, Random House, 2012 ; via negativa | AJOUT |
| Project Glasswing | EVENEMENT | date | Ouverture de Claude Mythos Preview à des partenaires, 7 avril 2026 | AJOUT |
| Veracode | ORGANISATION | rôle | Éditeur de sécurité applicative, rapport State of Software Security 2026 | AJOUT |
| règlement DORA | DOCUMENT | référence | Règlement (UE) 2022/2554, applicable depuis le 17 janvier 2025, articles 25 et 30 | AJOUT |
| Claudia Buch | PERSONNE | rôle | Présidente du conseil de surveillance prudentielle de la BCE | AJOUT |
