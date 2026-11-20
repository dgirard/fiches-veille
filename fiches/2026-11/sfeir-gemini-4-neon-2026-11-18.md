---
themes: [produits-services, economie-marche]
source: SFEIR
---
# sfeir-gemini-4-neon-2026-11-18

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **18 novembre 2026**, réécrit le soir même puis mis à jour le **19 novembre** (~22 000 signes, dix-huit sources : billet de Google, model card, documentation, grilles tarifaires, Artificial Analysis, Vals, Arena, Cursor, GitHub, OpenRouter, presse). Il présente **Gemini 4 Neon**, modèle intermédiaire de la génération 4 annoncé par **Koray Kavukcuoglu** (Google DeepMind) : **3 $ / 15 $** le million de tokens, fenêtre de **1 048 576** tokens. Quatre apports. **(A)** Une chronologie de la fuite à l'annonce en trois jours et la disponibilité (API, Antigravity, app Gemini, Agent Platform en GA dont l'emplacement « eu », GitHub Copilot, Cursor, OpenRouter). **(B)** Les chiffres de Google confrontés aux mesures indépendantes : rangs confirmés, mais un coût par tâche inférieur d'environ **17 %** à Carbon chez Artificial Analysis contre **32 %** annoncés, et **283 millions** de tokens de sortie sur l'index pour une médiane de **65,1 millions**. **(C)** La place dans la gamme entre **Hydrogen** et **Carbon**, avec une grille inversée jusqu'au **30 novembre**. **(D)** Le rôle d'**orchestrateur** de sous-agents Hydrogen documenté par Google. Rejoint la logique de coût par tâche de [[walker-onlycfo-ai-tokenomics-2026-10-22]].

## Titre Article

Gemini 4 Neon : le modèle intermédiaire de Google, entre Hydrogen et Carbon

## Date

2026-11-18

## URL

https://www.sfeir.com/articles/gemini-4-neon/

## Keywords

Gemini 4 Neon, Gemini 4 Hydrogen, Gemini 4 Carbon, Gemini 4 Argon, Google DeepMind, prix par million de tokens, cache implicite, niveaux de réflexion, orchestrateur, sous-agents, Antigravity, Interactions API, Gemini Enterprise Agent Platform, Artificial Analysis, Vals Index, Agent Arena, Terminal-Bench, SWE-sweep, coût par tâche, migration, Neon for cyber, SFEIR

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé publié sur sfeir.com, site éditorial du groupe.

## Ton

Article de suivi produit en français, présenté comme une page « mise à jour sur place » avec un historique daté des révisions. Le registre est documentaire : tableaux (chronologie, tarifs par palier, gamme Gemini 4), listes de caractéristiques tirées de la documentation, citations en anglais du billet et des mesures tierces. L'article place côte à côte les chiffres publiés par Google et ceux des évaluateurs indépendants, et signale les écarts sans les commenter au-delà du constat (rang 3 contre rang 6 chez Artificial Analysis, 32 % contre 17 %). Les réactions sur X sont rangées à part comme « des impressions, pas des mesures ». Public visé : CTO, lead devs, architectes de chaînes d'agents, DSI et conformité, chacun recevant une recommandation propre. Clôture sur une liste de ce qu'on ne sait pas encore.

## Pense-betes

- **Annonce** : 18 novembre 2026, billet « Introducing Gemini 4 Neon » de **Koray Kavukcuoglu** (SVP Google DeepMind, Chief AI Architect) + model card. Fuite préalable : site Gemini (16-17 nov.), SKU de facturation Google Cloud, nom « gemini-pro-orchestrator-neon » dans Antigravity CLI 1.5.11.
- **Caractéristiques** : `gemini-4-neon`, **1 048 576** tokens partagés, **65 536** tokens de sortie par segment ; entrées multimodales, sortie texte ; quatre niveaux de réflexion (LOW, MEDIUM, **HIGH par défaut**, XHIGH), MINIMAL et `thinking_budget` en erreur 400 ; `temperature`/`top_p`/`top_k` ignorés ; **cache implicite seul** dès 4 096 tokens ; connaissances arrêtées à mars 2026.
- **Disponibilité** : API (pas de palier gratuit), Gemini for business, Antigravity (fenêtre **512K**), app Gemini (remplace Argon, Gemini 3.1 Pro disparaît), Agent Platform en GA (« global », « us », « eu », réserve *« verified enterprise customers »*), GitHub Copilot (Pro+, Max, Business, Enterprise), Cursor, OpenRouter.
- **Prix** : Standard **3 / 15 $**, lecture de cache **0,15 $** (-95 %) ; Batch et Flex 1,50 / 7,50 ; Priority 5,40 / 27 (+80 %). Agent Platform régional (dont « eu ») **+10 %** ; écriture en cache facturée à partir du **12 janvier 2027** (3,75 $).
- **Chiffres Google** : Intelligence Index AA **61** (xhigh, 3e) ; Coding Agent Index 1er ; Vals 2e (70,9 %) ; Agent Arena 2e (1 336) ; Terminal-Bench 4.1 **65,2 %** (Hydrogen 57 %) ; SWE-sweep **12,8 %** (mini-SWE) contre **39,0 %** (Antigravity) ; coût par tâche **-32 %** vs Carbon en high.
- **Mesures indépendantes** : AA, 3e dans l'article, 6e sur 96 sur la page modèle ; coût en xhigh **6,44 $** contre 7,76 $ pour Carbon (≈ **-17 %**) ; environ 15 % de tokens de sortie de plus que Carbon ; **283 M** de tokens de sortie (médiane 65,1 M) ; 21 min par tâche contre 36. Coding Agent Index 59 (Carbon 55, Claude Code + Fable 5.2 : 58). Arena : derrière Claude Fable 5.2, devant Claude Opus 5.5 et Carbon.
- **Gamme** : Hydrogen 1,50/7,50 (exécution) ; Neon 3/15 (orchestration) ; Argon et Carbon 2/10 jusqu'au 30 novembre puis **4/20**. Google désigne Neon comme cible de migration depuis Gemini 3.1 Pro et Argon (code courant).
- **Orchestrateur** : Neon planifie et vérifie, passe `previous_interaction_id` à des sous-agents Hydrogen (Interactions API).
- **Neon for cyber** : programme Fairwind, AutoBaxBench difficile 76 %, SEC-bench Pro 90,5 %.
- **Inconnues** : écart de rang AA, absence de harnais commun, prix définitif.

## RésuméDe400mots

Le 18 novembre 2026, Koray Kavukcuoglu, SVP de Google DeepMind, présente Gemini 4 Neon, modèle intermédiaire de la génération 4 de Gemini. L'article de SFEIR AI, réécrit le soir même puis mis à jour le lendemain, en rassemble les caractéristiques, les prix et les premières mesures indépendantes.

Neon coûte 3 dollars le million de tokens en entrée et 15 en sortie, pour une fenêtre d'un million de tokens. Son apparition a suivi un scénario déjà vu : référence sur le site Gemini, ligne de facturation Google Cloud, nom « orchestrator » dans Antigravity CLI, documentation, puis billet et model card. Il est disponible dans l'API Gemini (hors palier gratuit), dans Antigravity avec une fenêtre limitée à 512K, dans l'app Gemini où il remplace Argon, et en disponibilité générale sur Gemini Enterprise Agent Platform, y compris dans l'emplacement « eu ». GitHub Copilot, Cursor et OpenRouter l'ont ajouté le jour même. La documentation fixe quatre niveaux de réflexion, HIGH par défaut, et un cache implicite seul.

Google publie une longue liste de résultats : 61 points sur l'Intelligence Index d'Artificial Analysis, première place de son Coding Agent Index, deuxième place sur Vals et Agent Arena, 65,2 % sur Terminal-Bench 4.1, et un coût par tâche inférieur de 32 % à celui de Carbon. Les mesures indépendantes confirment les classements, mais Artificial Analysis mesure un écart de coût d'environ 17 % au niveau xhigh et juge le modèle très verbeux, avec 283 millions de tokens de sortie sur l'index pour une médiane de 65,1 millions. Sur SWE-sweep, le score passe de 12,8 % à 39,0 % selon le harnais.

La grille place Neon entre Hydrogen (1,50 / 7,50) et Argon et Carbon (4 / 20 à partir du 1er décembre). Jusqu'au 30 novembre, le tarif d'introduction de ces derniers inverse la grille. Google désigne Neon comme cible de migration depuis Gemini 3.1 Pro et, pour le code courant, depuis Argon. Le billet et la documentation décrivent Neon en orchestrateur qui planifie et vérifie un workflow, puis délègue des étapes à des sous-agents Hydrogen.

L'article mentionne aussi une variante Neon for cyber réservée au programme Fairwind et les protections reprises de Carbon. Il recommande de tester Neon sur une vingtaine de tâches réelles, de refaire les calculs de coût en décembre, de prévoir un routage configurable par étape, et liste ce qui reste inconnu : l'écart de rang chez Artificial Analysis, une mesure sur harnais commun et le prix définitif.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Gemini 4 Neon : le modèle intermédiaire de Google, entre Hydrogen et Carbon | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Google | ORGANISATION | publie | Gemini 4 Neon | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Koray Kavukcuoglu | PERSONNE | travaille_chez | Google DeepMind | ORGANISATION | 0.93 | DYNAMIQUE | déclaré_article |
| Gemini 4 Neon | TECHNOLOGIE | fait_partie_de | Gemini | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Gemini 4 Neon | TECHNOLOGIE | remplace | Gemini 3.1 Pro | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Gemini 4 Neon | TECHNOLOGIE | utilise | Gemini 4 Hydrogen | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Gemini 4 Neon | TECHNOLOGIE | permet | orchestration de sous-agents | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Gemini 4 Neon | TECHNOLOGIE | concurrence | Gemini 4 Carbon | TECHNOLOGIE | 0.82 | DYNAMIQUE | inféré |
| Gemini 4 Neon | TECHNOLOGIE | mesure | 65,2 % sur Terminal-Bench 4.1 | MESURE | 0.88 | STATIQUE | déclaré_article |
| Google | ORGANISATION | affirme_que | coût par tâche de Neon inférieur de 32 % à Carbon au niveau high | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | coût par tâche de Neon environ 17 % sous Carbon au niveau xhigh | MESURE | 0.88 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | 283 millions de tokens de sortie sur l'index, médiane 65,1 millions | MESURE | 0.86 | STATIQUE | déclaré_article |
| Claude Fable 5.2 | TECHNOLOGIE | surpasse | Gemini 4 Neon | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| Gemini 4 Neon | TECHNOLOGIE | mesure | SWE-sweep de 12,8 % à 39,0 % selon le harnais | MESURE | 0.86 | STATIQUE | déclaré_article |
| Gemini 4 Neon | TECHNOLOGIE | utilise | cache implicite | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| GitHub Copilot | TECHNOLOGIE | utilise | Gemini 4 Neon | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Gemini 4 Neon for cyber | TECHNOLOGIE | est_variante_de | Gemini 4 Neon | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | tester Neon sur une vingtaine de tâches réelles avant la production | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle (groupe SFEIR) | AJOUT |
| Gemini 4 Neon | TECHNOLOGIE | prix | 3 $ / 15 $ le million de tokens, fenêtre de 1 048 576 tokens, 18 novembre 2026 | AJOUT |
| Gemini 4 Hydrogen | TECHNOLOGIE | rôle | Modèle d'exécution rapide de la gamme Gemini 4 (1,50 / 7,50 $) | AJOUT |
| Gemini 4 Carbon | TECHNOLOGIE | rôle | Haut de gamme Gemini 4 pour projets longs (4 / 20 $ après le 30 novembre 2026) | AJOUT |
| Koray Kavukcuoglu | PERSONNE | rôle | SVP Google DeepMind et Chief AI Architect de Google | AJOUT |
| Artificial Analysis | ORGANISATION | rôle | Évaluateur indépendant de modèles (Intelligence Index, Coding Agent Index) | AJOUT |
| Gemini 4 Neon for cyber | TECHNOLOGIE | accès | Variante réservée aux défenseurs du programme Fairwind | AJOUT |
