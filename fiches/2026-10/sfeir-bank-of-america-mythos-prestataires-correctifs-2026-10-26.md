---
themes: [qualite-securite, economie-marche]
source: SFEIR
---
# sfeir-bank-of-america-mythos-prestataires-correctifs-2026-10-26

## Veille

Article **SFEIR AI** publié sur sfeir.com le **26 octobre 2026** (~8 000 signes, neuf sources notées : CNBC, The Register, The Next Web, The Decoder, FinCEN, transcript des résultats). Il part d'une déclaration de **Brian Moynihan**, CEO de **Bank of America**, à CNBC le **14 octobre 2026** : la banque a fait entrer environ **1 000 prestataires** au deuxième trimestre pour corriger les vulnérabilités mises au jour par des modèles d'IA avancés, dont **Claude Mythos**, en renfort des ~**3 000** personnes déjà affectées. Trois apports. **(A)** Le chiffrage : un peu plus de **200 M$** au troisième trimestre, montant qui regroupe remédiation logicielle et conformité anti-blanchiment sans ventilation ; *« That risk is real risk »*. **(B)** Le parallèle avec l'**an 2000** (~**100 Md$** de corrections aux États-Unis) : le coût est dans la correction, pas dans la découverte. **(C)** Deux raisons pour lesquelles la décrue annoncée par Moynihan n'est pas garantie — les modèles progressent et relisent le même code, et le code produit par agents continue d'arriver. Cinq pistes pour les DSI, de la mesure de la capacité de correction au confinement des agents qui patchent. Prolonge [[anthropic-claude-fable-5-mythos-5-2026-06-09]] côté coût de remédiation.

## Titre Article

Bank of America : 1 000 prestataires pour corriger ce que Mythos a trouvé

## Date

2026-10-26

## URL

https://www.sfeir.com/articles/bank-of-america-mythos-1000-prestataires-correctifs/

## Keywords

Bank of America, Brian Moynihan, Claude Mythos, Project Glasswing, Anthropic, vulnérabilités, remédiation, prestataires, capacité de correction, dette de sécurité, an 2000, Y2K, legacy, SDLC sécurisé, contrats fournisseurs, défragilisation, CodeMender, agents de code, confinement, banque, FinCEN, SFEIR

## Authors

SFEIR AI — signature éditoriale de SFEIR, publiée sur sfeir.com (site éditorial de SFEIR).

## Ton

Article d'analyse adossé à l'actualité, registre factuel puis prescriptif. Les chiffres sont systématiquement sourcés et leurs écarts signalés (effectifs « nearly 3,500 » ou « 3,000 or 1.5% » selon la source), de même que les inconnues (part propre à Mythos non ventilée, part de la baisse d'effectifs due à l'IA ignorée). Le parallèle avec l'an 2000 sert de repère pédagogique. Une image filée structure la critique de l'hypothèse de décrue : « une baignoire dont le robinet reste ouvert ». La dernière partie adopte le registre de la recommandation en cinq points, avec renvois vers d'autres pages SFEIR. Public : DSI, RSSI, directions financières des grands comptes.

## Pense-betes

- **14 octobre 2026**, résultats trimestriels : Moynihan confirme à CNBC ~**1 000 prestataires** recrutés au T2 pour corriger des failles trouvées par des modèles frontier, dont **Claude Mythos**, en plus de ~**3 000** personnes. The Decoder : **4 000** personnes au total.
- **Mythos Preview** ouvert le **7 avril 2026** via **Project Glasswing** à des partenaires (banques, tech, agences) ; Anthropic déclare des milliers de failles de haute sévérité.
- Coût : *« couple hundred million plus »* au T3, **remédiation + anti-blanchiment non ventilés** (The Register). La veille, pénalités du Trésor > **1,21 Md$** (FinCEN : > 5 Md$ de transactions suspectes non ou mal déclarées 2018-2025).
- Moynihan : *« Once you patch, you don't have to patch as much »* → décrue attendue.
- En face : ~**130** projets IA internes, économies **300 M$** cette année → **700 M$** en 2027 ; effectifs −~3 400 en un an, −5 % de managers ; prestataires hors décompte.
- **An 2000** : ~**100 Md$** aux États-Unis 1995-2000 (John Koskinen) ; Bank of America avait déjà mis 1 000 personnes sur Y2K en 1998.
- **Décrue non garantie** : (1) chaque génération de modèles relit le même code et trouve ce que la précédente a manqué ; (2) le code produit par agents continue d'arriver — « baignoire au robinet ouvert ».
- Pistes DSI : **mesurer la capacité de correction** hebdomadaire ; **fermer le robinet** dans le SDLC (règles à la génération, revue avant merge, tests de sécurité en CI) ; **relire le legacy** avant un attaquant (défragilisation, cf. CodeMender) ; **contrats fournisseurs** (délais, audit, notification) ; **confiner les agents** qui patchent.

## RésuméDe400mots

Cet article de SFEIR, publié le 26 octobre 2026, part d'une déclaration de Brian Moynihan, CEO de Bank of America, recueillie par CNBC le 14 octobre, jour des résultats trimestriels. La banque a fait entrer environ mille prestataires externes au deuxième trimestre pour corriger les vulnérabilités logicielles mises au jour par des modèles d'IA avancés, dont Claude Mythos d'Anthropic. Ils renforcent les quelque trois mille personnes déjà affectées à ce domaine, sur le code interne comme sur les logiciels des fournisseurs, et restaient en poste mi-octobre.

Anthropic avait ouvert Mythos Preview le 7 avril 2026 à un cercle restreint de partenaires dans le cadre de Project Glasswing, en déclarant que le modèle avait trouvé des milliers de failles de haute sévérité. Bank of America a répondu en ajoutant des effectifs. Moynihan a donné un ordre de grandeur de coût, un peu plus de deux cents millions de dollars au troisième trimestre, mais ce montant regroupe remédiation logicielle et mise en conformité anti-blanchiment, au lendemain de pénalités de plus de 1,21 milliard de dollars infligées par le Trésor. Il prévoit une décrue une fois le stock corrigé. En parallèle, la banque mène environ 130 projets d'IA dont elle attend 700 millions de dollars d'économies en 2027, et ses effectifs ont baissé d'environ 3 400 personnes en un an.

L'article rapproche l'épisode du passage à l'an 2000, dont la correction a coûté environ cent milliards de dollars aux États-Unis : le coût est dans la correction, pas dans la découverte. Chaque vulnérabilité devient un ticket, des heures d'ingénieur, un test de non-régression.

SFEIR estime que la décrue n'est pas garantie, pour deux raisons. Les modèles progressent : chaque génération relira le même code et trouvera ce que la précédente avait manqué. Et le code continue d'arriver, de plus en plus écrit par des agents ; s'il garde le même taux de défauts, les équipes videront une baignoire dont le robinet reste ouvert.

Cinq pistes sont proposées aux DSI : mesurer la capacité de correction hebdomadaire, qui dimensionnera le renfort nécessaire ; fermer le robinet dans le SDLC par des règles de sécurité à la génération, une revue outillée et des tests en intégration continue ; relire le legacy avec ces mêmes outils avant un attaquant, à la manière de CodeMender ; revoir les contrats fournisseurs (délais, audit, notification) ; confiner les agents de code qui participeront aux corrections. Les organisations qui n'ont pas encore reçu leur liste de failles ont, selon l'article, quelques mois pour s'y préparer.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Bank of America : 1 000 prestataires pour corriger ce que Mythos a trouvé | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Brian Moynihan | PERSONNE | dirige | Bank of America | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Bank of America | ORGANISATION | utilise | Claude Mythos | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Bank of America | ORGANISATION | mesure | ~1 000 prestataires ajoutés au T2 2026 à ~3 000 personnes pour corriger les failles trouvées par IA | MESURE | 0.93 | STATIQUE | déclaré_article |
| Bank of America | ORGANISATION | mesure | un peu plus de 200 M$ au T3 2026, remédiation et anti-blanchiment confondus | MESURE | 0.88 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Claude Mythos | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Claude Mythos | TECHNOLOGIE | fait_partie_de | Project Glasswing | METHODOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Brian Moynihan | PERSONNE | prédit | les coûts de remédiation décroîtront une fois le stock de failles corrigé | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | s_oppose_à | les coûts de remédiation décroîtront une fois le stock de failles corrigé | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | chaque génération de modèles relit le même code et trouve ce que la précédente avait manqué | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | référence | passage à l'an 2000 | EVENEMENT | 0.88 | STATIQUE | déclaré_article |
| passage à l'an 2000 | EVENEMENT | mesure | ~100 Md$ de corrections aux États-Unis entre 1995 et 2000 | MESURE | 0.86 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | mesurer la capacité de correction hebdomadaire des vulnérabilités | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | défragilisation | METHODOLOGIE | 0.86 | ATEMPOREL | déclaré_article |
| CodeMender | TECHNOLOGIE | permet | défragilisation | METHODOLOGIE | 0.8 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | confiner les agents de code chargés des correctifs | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Bank of America | ORGANISATION | prédit | économies IA de 300 M$ cette année puis 700 M$ en 2027 (~130 projets) | MESURE | 0.84 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| Bank of America | ORGANISATION | secteur | Banque américaine ; ~4 000 personnes sur la remédiation des failles trouvées par IA | AJOUT |
| Brian Moynihan | PERSONNE | rôle | CEO de Bank of America | AJOUT |
| Claude Mythos | TECHNOLOGIE | accès | Preview ouverte le 7 avril 2026 à des partenaires restreints | AJOUT |
| Project Glasswing | METHODOLOGIE | définition | Programme Anthropic réservant Mythos aux défenseurs de logiciels critiques | AJOUT |
| passage à l'an 2000 | EVENEMENT | repère | Bug connu, coût concentré dans la correction | AJOUT |
| défragilisation | METHODOLOGIE | définition | Réduire le stock de failles de son propre code, une classe à la fois, chaque faille prouvée par un test et corrigée | AJOUT |
