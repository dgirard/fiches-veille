---
themes: [produits-services, agents-codage-ia-skills, economie-marche]
source: SFEIR
---
# sfeir-claude-fable-mythos-5-2-2026-11-10

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **10 novembre 2026** (~30 000 signes, dix sections, trois tableaux, une FAQ, 6 sources notées), suite de l'analyse SFEIR de Fable 5.1. Il porte sur **Claude Fable 5.2** et **Claude Mythos 5.2**, publiés par **Anthropic** le **9 novembre 2026** : un même modèle, Fable avec des classifieurs bloquant la cybersécurité offensive et la biologie de recherche, Mythos sans ces garde-fous et réservé aux programmes de vérification ou aux clients Enterprise via **Claude Security**. Trois apports. **(A)** Le paradoxe du coût : prix au token en baisse de **20 %** (**8 $ / 40 $**), mais coût par tâche d'index **26,54 $** à effort max contre **12,99 $** pour Fable 5.1 selon **Artificial Analysis** ; en effort *high*, Fable 5.2 obtient **62** pour **9,08 $**, devant Opus 5.5 en max (59, 10,04 $). **(B)** Une lecture du tableau d'Anthropic : saut net sur les tâches longues (Remote Labor Index **41,3 %** contre 21,3 % pour Opus 5.5), quelques points sur le code court, lignes cyber réservées à Mythos, démonstrations auto-déclarées. **(C)** Le retour d'usage d'**Ethan Mollick** (« Jagged AGI ») : des irrégularités déplacées vers le jugement sur son propre travail. Consigne centrale : *« Le bon indicateur reste le coût par résultat, pas le prix au token. »* Rejoint les fiches du corpus sur la gamme Claude et sur Gemini 4 Carbon.

## Titre Article

Claude Fable 5.2 et Mythos 5.2 : moins cher au token, plus cher à la tâche si l'on pousse l'effort

## Date

2026-11-10

## URL

https://www.sfeir.com/articles/claude-fable-5-2-mythos-5-2/

## Keywords

Claude Fable 5.2, Claude Mythos 5.2, Anthropic, Claude Opus 5.5, classifieurs, garde-fous, Cyber Verification Program, Life Sciences Verification Program, Claude Security, prix au token, coût par tâche, niveau d'effort, high, xhigh, max, Artificial Analysis, Intelligence Index, verbosité, benchmarks, Remote Labor Index, FrontierCode, advisor, orchestrateur, Lean, Fermat, Ethan Mollick, Jagged AGI, rétention de 30 jours, zero data retention, migration, changements cassants, Gemini 4 Carbon, GPT-6 Astra

## Authors

SFEIR AI, voix éditoriale du cabinet SFEIR, article non signé individuellement, publié sur sfeir.com.

## Ton

**Profil** : analyse de lancement de modèle pour équipes d'ingénierie, CTO et acheteurs, publiée sur le site d'un cabinet partenaire d'Anthropic. Français technique, fiche technique et tableaux de benchmarks et de coûts, FAQ.

**Registre** : chaque chiffre porte son origine (constructeur, évaluation tierce, source secondaire, retour d'usage individuel). Les démonstrations d'Anthropic sont annoncées comme *« auto-déclarées »*, avec leurs réserves (liste d'énoncés intermédiaires pour Fermat, préprints non relus, OS non audité). L'article corrige explicitement une rumeur du jour du lancement (Fable 5.2 dominant « sur tous les benchmarks ») à partir du tableau de l'éditeur.

**Posture** : l'article nuance aussi le titre de la source tierce qu'il cite (R&D World), en montrant qu'en effort *high* Fable 5.2 est à la fois meilleur et moins cher qu'Opus 5.5 en max. Recommandation alignée sur celle d'Anthropic : Opus 5.5 par défaut, Fable 5.2 pour planifier, orchestrer et débloquer. Le retour de Mollick sert de contrepoint qualitatif aux benchmarks.

## Pense-betes

- **Un modèle, deux noms** : mêmes poids ; Fable 5.2 bloque cyber offensive (repli vers **Opus 4.8**) et biologie de recherche (repli vers **Opus 5**) ; Mythos 5.2 sans garde-fous, via Cyber Verification Program, Life Sciences Verification Program ou **Claude Security** (Enterprise). « Réservé à Project Glasswing » ne s'applique plus. Blocages : **−55 %** (cyber −60 %, bio −40 %).
- **Positionnement Anthropic** : Opus 5.5 reste *« our strongest daily driver »* ; Fable/Mythos pour le travail technique ambitieux, ou comme **advisor** / orchestrateur.
- **Fiche technique** : contexte **1M**, sortie **128K**, coupure juin 2026 ; **8 $ / 40 $** (Fable 5.1 : 10 $ / 50 $ ; Opus 5.5 : 4 $ / 20 $) ; cache 0,20 $ ; batch 4 $ / 20 $ ; fast mode 16 $ / 80 $, jusqu'à 2,5x plus rapide (pas sur Bedrock). **Effort par défaut *high*** (Opus 5.5 : *medium*). « Covered Model » : rétention **30 jours**, pas de ZDR sauf autorisation. Retrait pas avant le 9 novembre 2027.
- **Benchmarks (tableau Anthropic)** : FrontierCode 2.0 **49,1 %** (Opus 5.5 45,5 %) ; FrontierSWE v2 69,9 % ; OSWorld 2.1 89,3 % (crédit partiel) ; Remote Labor Index **41,3 %** (Opus 5.5 21,3 %) ; RoboDojo 64,9 % ; BenchCAD 83,5 ; HLE 74,2 %. Gemini 4 Carbon garde AutomationBench (53,9 %), Opus 5.5 l'Elo d'AA-Briefcase. Capacités de R&D IA bridées au niveau d'Opus 5.5.
- **Coût (Artificial Analysis)** : max 65 / **26,54 $** ; xhigh 62 / 14,83 $ ; high **62 / 9,08 $** ; medium 56 / 3,80 $ ; low 54 / 3,10 $ ; Opus 5.5 max 59 / 10,04 $ ; Fable 5.1 max 49 / 12,99 $. **275 M** de tokens de sortie pour l'index (médiane 72,8 M ; Fable 5.1 : 163 M). De high à max : +3 points pour **2,9x** le coût.
- **Consigne de la doc Anthropic** : partir de *high*, *xhigh* pour le code long après mesure, *max* pour mesurer le plafond.
- **Démonstrations (auto-déclarées)** : Fermat formalisé en **Lean** en **30 h** par ~1 000 agents (première formalisation : 11 jours) ; deux problèmes de physique des trous noirs (préprints) ; trois appareils avec **Diode** ; un OS en 8 jours par 1 000+ sous-agents ; migration Python → Rust, démarrage **26x** plus rapide ; capsides d'AAV, 28 sur 34.
- **Ethan Mollick** (« Fable 5.2 and Jagged AGI ») : « presque » une AGI en dents de scie ; Portals : 204 puis 450+ mondes 3D, 28 équipes d'agents, ~25 000 exécutions ; règlement non demandé de **204 sections et 87 500 mots** ; limite : le jugement sur la qualité et la proportion de son propre travail.
- **Sécurité** : audit comportemental 2,67 (Opus 5.5 : 2,79) ; évasions de sandbox **3,1 %** (Mythos 5.1 : 21 %) ; soupçon d'être évalué plus fréquent ; Enterprise Frontier Safeguards (bêta privée) rendent le ZDR possible.
- **Migration** : quatre changements cassants (contrôle de préfixe généralisé, blocs de raisonnement lisibles seulement par 5.2, `computer_20251124` en erreur 400 hors Bedrock, appariements de l'advisor) + effort par défaut depuis Opus 5.5.
- **Recommandations** : Opus 5.5 par défaut ; Fable 5.2 pour planifier et débloquer ; effort explicite ; instrumenter le coût par tâche ; détecter les replis des garde-fous ; revue humaine de la forme.

## RésuméDe400mots

Le 9 novembre 2026, Anthropic publie Claude Fable 5.2 et Claude Mythos 5.2, deux noms pour un même modèle. Fable embarque des classifieurs qui bloquent la cybersécurité offensive et la biologie de recherche, en servant alors la réponse d'un modèle plus ancien ; Mythos en est dépourvu et reste réservé aux organisations vérifiées, avec un accès nouveau pour les clients Enterprise via Claude Security. Les blocages diminuent nettement par rapport à la version précédente.

Le prix au token baisse de 20 %, la sortie gagne en vitesse et les scores progressent sur presque toutes les lignes du tableau de l'éditeur, avec un saut marqué sur les tâches longues et un écart de quelques points seulement sur le code de court horizon. SFEIR rappelle que ces chiffres sont des chiffres constructeur, que les lignes cyber concernent Mythos et non Fable, et que Gemini 4 Carbon et Opus 5.5 conservent certaines premières places.

Le point central est le coût. Selon Artificial Analysis, à effort maximal, une tâche de l'index coûte deux fois plus qu'avec Fable 5.1, parce que le modèle génère beaucoup plus de tokens. Mais en effort haut, réglage par défaut, Fable 5.2 dépasse Opus 5.5 réglé au maximum pour un coût par tâche légèrement inférieur. La documentation d'Anthropic recommande d'ailleurs de partir de ce niveau et de réserver le maximum à la mesure du plafond. L'effort par défaut, plus élevé que celui d'Opus, peut renchérir silencieusement une requête lors d'un changement de modèle.

Anthropic accompagne la sortie de démonstrations auto-déclarées : formalisation du dernier théorème de Fermat en trente heures, résultats de physique en préprint, appareils électroniques, prototype de système d'exploitation, migration vers Rust. Ethan Mollick, qui a eu un accès anticipé, décrit une AGI « en dents de scie » : le modèle tient des chantiers de plusieurs jours, mais juge mal la qualité et la proportion de son propre travail, au point que ses agents ont produit un règlement de plus de deux cents sections que personne n'avait demandé.

Côté conformité, la rétention de trente jours reste la règle, sauf dispositif en bêta privée. La migration comporte quatre changements cassants.

SFEIR recommande de garder Opus 5.5 par défaut, de réserver Fable 5.2 à la planification, à l'orchestration et au déblocage, de fixer l'effort explicitement, d'instrumenter le coût par tâche, d'anticiper les replis des garde-fous et de maintenir une revue humaine de la forme des livrables.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Claude Fable 5.2 et Mythos 5.2 : moins cher au token, plus cher à la tâche | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Claude Fable 5.2 | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Claude Mythos 5.2 | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Claude Mythos 5.2 | TECHNOLOGIE | est_variante_de | Claude Fable 5.2 | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Claude Fable 5.2 | TECHNOLOGIE | remplace | Claude Fable 5.1 | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Claude Security | TECHNOLOGIE | permet | accès des clients Claude Enterprise à Claude Mythos 5.2 | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | coût par tâche de 26,54 $ à effort max contre 12,99 $ pour Fable 5.1 | MESURE | 0.9 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | Fable 5.2 en high : index 62 pour 9,08 $ par tâche, contre 59 et 10,04 $ pour Opus 5.5 en max | MESURE | 0.88 | STATIQUE | déclaré_article |
| Claude Fable 5.2 | TECHNOLOGIE | surpasse | Claude Opus 5.5 | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Claude Fable 5.2 | TECHNOLOGIE | mesure | Remote Labor Index 41,3 % contre 21,3 % pour Opus 5.5 | MESURE | 0.86 | STATIQUE | déclaré_article |
| Gemini 4 Carbon | TECHNOLOGIE | surpasse | AutomationBench : 53,9 % contre 51,4 % pour Fable 5.2 | MESURE | 0.85 | STATIQUE | déclaré_article |
| Claude Fable 5.2 | TECHNOLOGIE | concurrence | GPT-6 Astra | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Claude Fable 5.2 | TECHNOLOGIE | utilise | Lean | TECHNOLOGIE | 0.8 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | collabore_avec | Diode | ORGANISATION | 0.82 | STATIQUE | déclaré_article |
| Ethan Mollick | PERSONNE | publie | Fable 5.2 and Jagged AGI | DOCUMENT | 0.92 | STATIQUE | déclaré_article |
| Ethan Mollick | PERSONNE | affirme_que | les irrégularités de Fable 5.2 se sont déplacées des erreurs vers le jugement sur son propre travail | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | recommande | Claude Opus 5.5 comme modèle par défaut | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | recommande | partir de l'effort high et réserver max à la mesure du plafond | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | instrumenter le coût par tâche plutôt que suivre le prix au token | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | Fable 5.2 pour planifier et orchestrer, Opus 5.5 pour exécuter | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Claude Fable 5.2 | TECHNOLOGIE | catégorie | Modèle Anthropic du 09/11/2026, classifieurs cyber et biologie, effort par défaut high | AJOUT |
| Claude Fable 5.2 | TECHNOLOGIE | prix | 8 $ / 40 $ par million de tokens, contexte 1M, sortie 128K | AJOUT |
| Claude Mythos 5.2 | TECHNOLOGIE | accès | Mêmes poids que Fable 5.2, sans garde-fous ; programmes de vérification ou Claude Security | AJOUT |
| Claude Security | TECHNOLOGIE | catégorie | Offre Anthropic donnant aux clients Enterprise accès à Mythos 5.2 | AJOUT |
| Artificial Analysis | ORGANISATION | rôle | Évaluateur tiers ; coût par tâche de l'Intelligence Index par niveau d'effort | AJOUT |
| Ethan Mollick | PERSONNE | rôle | Professeur à Wharton, auteur de One Useful Thing | AJOUT |
| Fable 5.2 and Jagged AGI | DOCUMENT | publication | One Useful Thing, 9 novembre 2026, accès anticipé | AJOUT |
| Diode | ORGANISATION | secteur | Fabricant de circuits imprimés, partenaire des démonstrations matérielles | AJOUT |
