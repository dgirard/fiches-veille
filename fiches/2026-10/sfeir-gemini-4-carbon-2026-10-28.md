---
themes: [produits-services, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-gemini-4-carbon-2026-10-28

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **28 octobre 2026** et tenu à jour jusqu'au **15 novembre** (~39 000 signes, quatre mises à jour datées, 30 sources notées). Fiche de suivi de **Gemini 4 Carbon**, modèle frontier de **Google** annoncé par **Koray Kavukcuoglu** quinze jours après l'ouverture de **Gemini 4 Argon**, ouvert le **10 novembre** à tous les clients payants de l'API et aux abonnés Google AI Ultra. Trois apports. **(A)** Une chronologie qui sépare l'officiel, la presse (Business Insider, 9 octobre) et les fuites non confirmées (accès anticipé, LMArena, identifiants internes). **(B)** Une lecture croisée des **17 benchmarks** de Google et des mesures d'**Artificial Analysis** : Carbon premier sur 15 des 17 lignes du tableau de Google, premier de l'Intelligence Index v5 avec **59** le 28 octobre puis quatrième le 10 novembre derrière **Claude Fable 5.2**, deuxième sur l'index des agents de code (59 contre 62 pour Claude Code avec Opus 5.5), lent (**80 tokens/s**, 61e sur 72). Les réserves viennent du document de méthodologie de Google lui-même : scores des concurrents déclarés par leurs éditeurs, plusieurs scores de Carbon calculés avec le harnais de Google. **(C)** Des conseils par rôle (CTO, RSSI, DSI, achats), dont le raisonnement en coût par tâche : *« Raisonnez en coût par tâche plutôt qu'en prix du token. »* Prolonge les fiches du corpus sur la famille Gemini 4 et la lecture des benchmarks frontier.

## Titre Article

Gemini 4 Carbon : forces, limites et usages du modèle de Google pour le code

## Date

2026-10-28

## URL

https://www.sfeir.com/articles/gemini-4-carbon/

## Keywords

Gemini 4 Carbon, Gemini 4 Argon, Gemini 4 Hydrogen, Google, Google DeepMind, modèle frontier, coding agentique, tâches longues, benchmarks, Terminal-Bench 4.0, FrontierSWE 2, SWE-sweep, OSWorld, WebDev Arena, Artificial Analysis Intelligence Index, Vals Index, hallucinations, coût par tâche, prix du token, latence, Fairwind Program, cybersécurité, variante cyber, Antigravity, GitHub Copilot, Claude Opus 5.5, GPT-6 Astra, Claude Fable 5.2, fenêtre de contexte

## Authors

SFEIR AI, voix éditoriale du cabinet SFEIR, article non signé individuellement, publié sur sfeir.com.

## Ton

**Profil** : fiche produit vivante, mise à jour à chaque annonce (bandeau « Statut au 15 novembre 2026 », historique daté en fin d'article). Public : CTO, lead devs, RSSI, DSI, acheteurs. Français technique, tableaux de chronologie, de comparaison et de benchmarks.

**Registre** : le statut de chaque information est explicité, jusque dans une colonne « Statut » de la chronologie (officiel, enquête de presse, non confirmé, mesure indépendante). Les chiffres de Google sont systématiquement mis en regard de mesures tierces ou de leurs conditions de calcul : harnais propre, « mitigations off », colonnes choisies (Claude Sonnet 5.5 absent du tableau alors qu'il devance Carbon chez Vals AI).

**Posture** : ni promotion ni dénigrement ; les retours de testeurs (« plus lent mais moins paresseux ») sont rapportés comme tels puis confrontés à l'annonce, qui en confirme certains et en contredit d'autres. La section finale « Ce qui manque encore pour évaluer Carbon » liste les trous de l'information disponible.

## Pense-betes

- **Chronologie** : Argon annoncé le **30 septembre**, ouvert le **13 octobre** ; fuite Business Insider (**9 octobre**, plateforme interne **Jetski**, noms de code chimiques Argon/Barium/Carbon) ; annonce de Carbon le **28 octobre** (cyberdéfenseurs du Fairwind Program d'abord) ; ouverture générale le **10 novembre** ; Copilot le même jour ; **Gemini 4 Hydrogen** (« adapted from Carbon ») le 12 novembre ; retrait d'Argon de Copilot annoncé pour le **14 décembre**.
- **Positionnement** : modèle à part entière « construit sur Argon », pour les tâches longues (des tâches qui tournent « des jours » en interne). Google recommande toujours **Argon pour la majorité** des usages. Sundar Pichai : *« I did say we'd be releasing our models periodically. »*
- **Benchmarks Google (28 octobre)** : Terminal-Bench 4.0 **65,2 %** (Opus 5.5 : 59,6 %) ; FrontierSWE 2 **61,2 %** (Opus 5.5 : 62,3 %, GPT-6 Astra : 65,5 %) ; OSWorld-2.1 **81,5 %** (Opus 5.5 : 87,2 %) ; GraphWalks 96,2 % ; ExploitGym 54,8 % ; SEC-bench Pro 88,2 % ; WebDev Arena +89 Elo, **4e place**.
- **Réserves de méthode (document Google)** : scores concurrents déclarés par leurs éditeurs ; SWE-sweep, OSWorld, GraphWalks, ExploitGym, SEC-bench Pro calculés par Google ; cyber mesuré **sans garde-fous**. Vals AI : Carbon 2e derrière Claude Sonnet 5.5, absent du tableau.
- **Artificial Analysis** : Intelligence Index **59** (Opus 5.5 : 58 ; Opus 5.5 varie de 35 à 58 selon l'effort) puis **60** et 4e le 10 novembre (Claude Fable 5.2 jusqu'à 65) ; Coding Agent Index **59** contre **62** ; hallucination **11 %** (Argon 4 %, Opus 5.5 et GPT-6 Astra 50 %) ; coût **7,76 $** par tâche (Opus 5.5 : 10,04 $ ; GPT-6 Astra : 6,25 $) ; **200 M** de tokens pour l'index, plus de 3× la médiane.
- **Vitesse** : 80 tokens/s, 61e sur 72, **67 s** avant le premier token en réglage « high » ; la model card range les lenteurs parmi les limites connues. Testeurs : 2 à 4 fois plus lent qu'Argon.
- **Mesures internes Google (10 novembre)** : garde-fous bloquant **99 %** des trajectoires de red teaming ; intrusion par tentative **0,8 %** (Argon 3,1 %) ; honnêteté agentique **92 %** (Argon 70 %) sur 375 tâches.
- **Prix** : identique à Argon, **2 $ / 10 $** par million de tokens jusqu'au 30 novembre, puis **4 $ / 20 $** ; cache 0,10 $ puis 0,20 $ ; lots à moitié prix. Contexte **1 048 576** tokens partagés, sortie 65 536 par défaut, connaissances arrêtées à mars 2026.
- **Variante cyber** : `gemini-4-carbon-cyber-permissive`, via le Fairwind Program (650+ partenaires), emplacements « global » et « us » seulement, pas « eu ».
- **Conseils par rôle** : CTO — banc d'une vingtaine de tâches longues de ses dépôts, plafonds de tokens et de durée ; DSI — couche d'abstraction du modèle ; achats — coût par tâche, traitement par lots.
- **Manques au 10 novembre** : évaluation de sécurité frontière propre à Carbon renvoyée à un rapport distinct ; pas de DeepSWE ; vitesse sur tâches réelles.

## RésuméDe400mots

Gemini 4 Carbon est le modèle frontier présenté par Google le 28 octobre 2026, deux semaines après l'ouverture de Gemini 4 Argon. L'article de SFEIR, mis à jour jusqu'au 15 novembre, en suit la trajectoire. Révélé par Business Insider le 9 octobre comme checkpoint testé en interne, Carbon sort comme un modèle à part entière construit sur Argon, d'abord pour des cyberdéfenseurs du Fairwind Program, puis le 10 novembre pour tous les clients payants de l'API et les abonnés Google AI Ultra, et le même jour dans GitHub Copilot. Le 12 novembre, Google publie Gemini 4 Hydrogen, adapté de Carbon.

Google le présente comme son modèle le plus fort, à l'état de l'art en cybersécurité et sur les tâches de longue durée, tout en recommandant Argon pour la majorité des usages. Son tableau place Carbon en tête sur 15 des 17 lignes. SFEIR rapproche ces chiffres de leurs conditions : scores concurrents déclarés par leurs éditeurs, plusieurs scores de Carbon calculés avec le harnais de Google, bancs cyber mesurés sans garde-fous, concurrents mieux classés absents des colonnes.

Les mesures d'Artificial Analysis nuancent l'ensemble. Carbon prend la tête de l'Intelligence Index avec 59 points le 28 octobre, puis tombe au quatrième rang le 10 novembre derrière Claude Fable 5.2. Sur l'index des agents de code, il reste derrière Claude Code avec Opus 5.5. Son taux d'hallucination est parmi les plus bas mesurés, son coût par tâche inférieur d'environ un quart à celui d'Opus 5.5, mais il est lent : quatre-vingts tokens par seconde, plus d'une minute avant le premier token en réglage haut. Les testeurs l'avaient relevé, Google l'inscrit dans les limites de sa model card.

L'article situe l'usage visé : les tâches longues confiées à un agent, où finir compte plus que la latence. Une tâche qui dure se paie en tokens, et Google confirme que Carbon en consomme plus qu'Argon à prix unitaire égal.

Les conseils sont donnés par rôle. Le CTO teste Carbon sur une vingtaine de tâches longues de ses propres dépôts et plafonne tokens et durée. Le RSSI note que la variante cyber, réservée aux projets du Fairwind Program, n'est pas disponible dans l'emplacement européen de Google Cloud. La DSI isole le choix du modèle derrière une couche d'abstraction face à une cadence de quinze jours. Les achats raisonnent en coût par tâche plutôt qu'en prix du token. Manquent encore une évaluation de sécurité propre au modèle et des mesures indépendantes en code agentique.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Gemini 4 Carbon : forces, limites et usages du modèle de Google pour le code | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Google | ORGANISATION | publie | Gemini 4 Carbon | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Koray Kavukcuoglu | PERSONNE | travaille_chez | Google | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Gemini 4 Carbon | TECHNOLOGIE | est_basé_sur | Gemini 4 Argon | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Gemini 4 Hydrogen | TECHNOLOGIE | est_variante_de | Gemini 4 Carbon | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Gemini 4 Carbon | TECHNOLOGIE | remplace | Gemini 4 Argon | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| Gemini 4 Carbon | TECHNOLOGIE | concurrence | Claude Opus 5.5 | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Gemini 4 Carbon | TECHNOLOGIE | surpasse | Terminal-Bench 4.0 : 65,2 % contre 59,6 % pour Claude Opus 5.5 | MESURE | 0.85 | STATIQUE | déclaré_article |
| Claude Opus 5.5 | TECHNOLOGIE | surpasse | Gemini 4 Carbon | TECHNOLOGIE | 0.82 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | Gemini 4 Carbon à 59 sur l'Intelligence Index v5 le 28 octobre, 4e avec 60 le 10 novembre | MESURE | 0.9 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | Gemini 4 Carbon à 80 tokens/s, 61e sur 72 modèles | MESURE | 0.88 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | 7,76 $ par tâche contre 10,04 $ pour Claude Opus 5.5 | MESURE | 0.88 | STATIQUE | déclaré_article |
| Claude Fable 5.2 | TECHNOLOGIE | surpasse | Gemini 4 Carbon | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Gemini 4 Carbon | TECHNOLOGIE | permet | coding agentique sur tâches longues | METHODOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Fairwind Program | TECHNOLOGIE | permet | accès à la variante cyber de Gemini 4 Carbon | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| GitHub Copilot | TECHNOLOGIE | utilise | Gemini 4 Carbon | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Google | ORGANISATION | affirme_que | Gemini 4 Argon reste le choix idéal pour la majorité du développement logiciel | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| Google | ORGANISATION | mesure | garde-fous bloquant 99 % des trajectoires de red teaming, intrusion à 0,8 % par tentative | MESURE | 0.82 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | raisonner en coût par tâche plutôt qu'en prix du token | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | isoler le choix du modèle derrière une couche d'abstraction | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Gemini 4 Carbon | TECHNOLOGIE | catégorie | Modèle frontier de Google pour tâches longues, annoncé le 28/10/2026, GA API le 10/11/2026 | AJOUT |
| Gemini 4 Carbon | TECHNOLOGIE | prix | 2 $ / 10 $ par million de tokens jusqu'au 30/11/2026, puis 4 $ / 20 $ ; contexte 1 048 576 tokens | AJOUT |
| Gemini 4 Argon | TECHNOLOGIE | catégorie | Modèle frontier Google annoncé le 30/09/2026, ouvert le 13/10/2026 | AJOUT |
| Gemini 4 Hydrogen | TECHNOLOGIE | catégorie | Modèle rapide adapté de Carbon, publié le 12/11/2026 | AJOUT |
| Koray Kavukcuoglu | PERSONNE | rôle | Signataire des annonces Gemini 4 chez Google | AJOUT |
| Artificial Analysis | ORGANISATION | rôle | Évaluateur indépendant, Intelligence Index v5 (60 % de jeux de test privés) | AJOUT |
| Fairwind Program | TECHNOLOGIE | définition | Programme Google DeepMind d'accès des cyberdéfenseurs aux variantes cyber, 650+ partenaires | AJOUT |
| Claude Fable 5.2 | TECHNOLOGIE | rang | En tête de l'Intelligence Index au 10/11/2026, jusqu'à 65 points | AJOUT |
