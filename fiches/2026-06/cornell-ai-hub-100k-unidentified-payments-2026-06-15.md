---
cabinet_promotion_candidate: true
proposed_class: Pattern
proposed_capability: capability/software-factory
notes: "Contre-exemple précieux au récit 'AI4Business ne crée pas de valeur' : un cas où l'IA crée une valeur mesurable (100 000 $ récupérés sur un 1er lot, backlog ~1 M$) DANS un processus métier (finance/trésorerie), précisément parce qu'il applique le modèle Lab + Crowd d'Ethan Mollick (AI Hub central + experts métier Treasury) et une discipline 'contexte d'abord, plan puis build' (Claude Code Plan Mode). Datapoints mobilisables : 99% des paiements portent un nom de fournisseur vs <4% un n° de facture ; backtest 9 131 paiements ; 97%→100% de précision avec la chaîne IA ; un semestre de notes → outil en une session. Illustre concrètement le concept Mollick de récompense/preuve visible (vivid win) et de pipeline Crowd→Lab. À relier à [[mollick-making-ai-work-leadership-lab-crowd-2025-05-22]]."
---
# cornell-ai-hub-100k-unidentified-payments-2026-06-15

## Veille

Retour d'expérience publié par le **Cornell AI Innovation Hub** (15 juin 2026) : comment une collaboration de deux semestres entre l'AI Hub, des étudiants de master et l'équipe Trésorerie de Cornell a transformé une investigation manuelle chronophage en un outil IA qui a permis de **récupérer 100 000 $** de paiements non identifiés sur un premier lot. Cas d'usage **AI4Business** (processus financier) réussi qui illustre presque point par point le framework **Leader-Lab-Crowd** d'**Ethan Mollick** : l'**AI Hub** joue le rôle du **Lab** (équipe centrale ambidextre, technologistes + étudiants) ; la **Trésorerie** (Cheryl Barnes, Marie Graves…) est la **Crowd** porteuse de la connaissance métier et de la douleur réelle ; et les **100 000 $** constituent la **récompense visible** (vivid win) qui ancre l'adoption — exactement le levier d'incitation que Mollick juge décisif. Méthode-clé : **« contexte d'abord, plan puis build »** via **Claude Code Plan Mode**, chaîne **fuzzy-matching → Gemini Enterprise Web Search → synthèse Claude**, le tout dans le **Cornell AI Gateway** gouverné. *« The $100,000 is a start. »*

## Titre Article

How Cornell Recovered $100,000 in Unidentified Payments With AI

## Date

2026-06-15

## URL

https://innovationhub.ai.cornell.edu/articles/how-cornell-recovered-100000-in-unidentified-payments-with-ai/

## Keywords

Cornell AI Innovation Hub, paiements non identifiés, rapprochement de paiements, trésorerie, finance, AI4Business, Leader-Lab-Crowd, Ethan Mollick, récompense, incitation, vivid win, Lab, Crowd, connaissance métier, Claude Code, Plan Mode, contexte d'abord, fuzzy matching, Gemini Enterprise Web Search, synthèse Claude, Cornell AI Gateway, gouvernance des données, know your data, backtest, escheatment, Oracle GL, Kyriba, n8n, skill /treasury, pilote Claude, conduite du changement, automatisation, ROI mesurable

## Authors

**Pete Stergion** — Desktop Engineer au Cornell AI Innovation Hub, co-tech lead du projet (avec Phil Williammee). Article institutionnel signé de l'AI Hub.

## Ton

**Profil** : retour d'expérience institutionnel (case study / *progress report*) à la première personne du pluriel (*« we »*), publié sur le blog du Cornell AI Innovation Hub. Public cible : équipes opérationnelles d'universités et d'entreprises, dirigeants IT, praticiens de la conduite du changement IA. Registre **sobre, pédagogique et honnête**, niveau technique moyen (assume fuzzy matching, pipeline, GL, backtest) mais lisible par un non-ingénieur.

**Style** : narration en étapes (*The Problem / The Team / How We Built It / The Pipeline / The Results / What's Next / The Takeaway*), alternance récit + chiffre, avec une **honnêteté maîtrisée** qui renforce la crédibilité : on documente la **limite** de l'outil (fournisseurs payant plusieurs départements), on rappelle que *« resolution still depends on treasury staff follow-up »*, et on insiste sur la gouvernance (*« know your data »*, Cornell AI Gateway, PII retirées). Pas de survente : la thèse de clôture n'est pas « l'IA fait des miracles » mais *« the project worked because the team put in the groundwork »*. Formule-marqueur partageable : *« The $100,000 is a start. »*

## Pense-betes

- **Le chiffre-titre** : **100 000 $** récupérés sur un **premier lot** — 23 départements contactés, **7 réponses**, **5 paiements confirmés**. Backlog actif ~**1 M$** (pic historique **4 M$**) sur quelques centaines de transactions. Enjeu réglementaire : la loi de l'État de New York impose l'**escheatment** (reversement des fonds non réclamés à l'État) si non résolus à temps.
- **L'insight qui structure tout** : les **noms de fournisseurs figurent sur 99 %** des paiements non identifiés, alors que les **numéros de facture/PO sont sur moins de 4 %**. → on mise sur le nom du fournisseur, pas sur l'identifiant manquant.
- **Lecture Mollick (cœur de la demande)** : le cas illustre le framework **Leader-Lab-Crowd** ([[mollick-making-ai-work-leadership-lab-crowd-2025-05-22]]).
  - **Lab** = l'**AI Hub** (Pete Stergion, Phil Williammee, cohorte d'étudiants) : équipe centrale qui *package* la solution.
  - **Crowd** = la **Trésorerie** (Cheryl Barnes, Marie Graves, Kevin Mooney, Debra Federation) : connaissance métier + données (Kevin fournit **3 ans de GL Oracle, 10 000+ enregistrements**). C'est la douleur du terrain (jusqu'à **une demi-journée de travail** sur ce problème) qui devient l'opportunité.
  - **Récompense / vivid win** : Mollick recommande de **récompenser les employés qui découvrent des usages transformationnels** et de fournir une **image vivante** du futur IA. Les **100 000 $** sont précisément cette preuve concrète et légitimante — elle rend la valeur tangible et désirable.
  - **Réassurance anti-licenciement** : l'IA **retire la corvée** (recherches d'emails, googling d'abréviations, recoupements) plutôt que de remplacer les agents ; l'objectif affiché est *« a sustainable workflow the team owns and operates directly »* (onboarding dans le pilote Claude + skill **`/treasury`**). C'est la réponse au *« reassure your workers »* de Mollick.
- **Méthode « contexte d'abord, plan puis build »** : via **Claude Code Plan Mode**, on charge *tout* le contexte (background, processus manuel, notes du semestre, prototypes étudiants, données assainies) ; Claude Code **propose une architecture complète à valider avant d'écrire une ligne**. Résultat : d'un **semestre de notes à un outil fonctionnel en une seule session**.
- **Pipeline (3 étapes), exposé comme un *skill* dans Claude Code** : (1) **rapprochement historique** (fuzzy matching sur le GL ; filtre les mots-bruit *Inc/LLC/Corp* ; *gate* sur recouvrement de tokens pour éviter les faux positifs) ; (2) **recherche fournisseur** via **Gemini Enterprise Web Search** (dans le Cornell AI Gateway) ; (3) **synthèse Claude** (pèse les preuves → département probable, **niveau de confiance**, contact suggéré). Sortie : **Excel trié par confiance**, en quelques minutes. Entrée : export **Kyriba** (TMS).
- **Backtest sérieux** : 3 scénarios sur **9 131 paiements** déjà résolus, réponses cachées. Fournisseurs récurrents : **97 %** (fuzzy seul, 500 paiements test) → **100 %** avec la chaîne IA complète. Fournisseurs inconnus : **76 % → 100 %** une fois Gemini + Claude activés. **Limite documentée** : fournisseurs payant plusieurs départements (bon fournisseur mais pas toujours le bon compte départemental).
- **Gouvernance** : données financières *moderate-risk*, **Cornell AI Gateway**, **non utilisées pour entraîner des modèles externes**, accès restreint, **PII retirées**, approche *« know your data »*. Modèles testés au fil de l'eau : **Gemini, GPT, Claude** ; prototypage initial en **n8n**.
- **Contre-récit utile** : à mobiliser face au narratif « l'IA ne crée pas de valeur sur les processus métier ». Ici elle en crée — **parce que** Lab + Crowd + groundwork. *« When it came time to build, the AI had everything it needed to design a real solution rather than a generic one. »*

## RésuméDe400mots

Le Cornell AI Innovation Hub raconte (15 juin 2026) comment une collaboration de deux semestres a permis de **récupérer 100 000 $** de paiements non identifiés grâce à l'IA. Le problème : chaque année, Cornell reçoit des centaines de virements et paiements ACH sans information suffisante pour les router (pas de numéro de facture, nom de fournisseur vague). Les fonds s'accumulent dans un compte d'attente — backlog actif ~**1 M$**, pic historique **4 M$** — et la **loi de l'État de New York impose l'escheatment** s'ils ne sont pas résolus à temps. Deux agentes de la trésorerie y passaient jusqu'à **une demi-journée** par jour.

La structure du projet illustre le framework **Leader-Lab-Crowd** d'Ethan Mollick. Le **Lab**, c'est l'**AI Hub** (Pete Stergion et Phil Williammee, co-tech leads, plus une cohorte d'étudiants). La **Crowd**, c'est la **Trésorerie** (Cheryl Barnes, Marie Graves, Kevin Mooney, Debra Federation), détentrice de la connaissance métier et des données — Kevin fournit **3 ans d'historique GL Oracle (10 000+ enregistrements)**. L'analyse étudiante dégage l'insight clé : **99 %** des paiements portent un nom de fournisseur, contre **moins de 4 %** un numéro de facture.

La construction suit une discipline **« contexte d'abord, plan puis build »** : via **Claude Code Plan Mode**, l'équipe charge tout le contexte (notes, processus manuel, prototypes, données assainies) ; Claude Code **propose une architecture à valider avant d'écrire du code**. D'un semestre de notes naît un **outil en une seule session**. Le **pipeline Python** (exposé comme *skill* `/treasury`) enchaîne trois étapes : **fuzzy matching** sur le GL (filtrage des mots-bruit Inc/LLC/Corp), **recherche fournisseur** via **Gemini Enterprise Web Search**, puis **synthèse Claude** produisant pour chaque paiement un département probable, un **niveau de confiance** et un contact. Sortie : un Excel trié par confiance, en quelques minutes — le tout dans le **Cornell AI Gateway** gouverné (PII retirées, pas d'entraînement externe).

Le **backtest** (9 131 paiements résolus) montre **97 % → 100 %** de précision pour les fournisseurs récurrents avec la chaîne IA, et **76 % → 100 %** pour les inconnus. Limite documentée : les fournisseurs multi-départements. Résultat opérationnel : 23 départements contactés, 7 réponses, **5 paiements = 100 000 $** confirmés.

Au-delà du chiffre, le cas est un **contre-exemple** au récit « l'IA ne crée pas de valeur métier » : elle en crée parce qu'on a réuni un **Lab**, une **Crowd** experte et un **vrai travail de fond**. Et les 100 000 $ jouent le rôle de **récompense visible** chère à Mollick — la preuve tangible qui légitime et diffuse l'adoption, en retirant la corvée plutôt que les emplois. *« The $100,000 is a start. »*

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Pete Stergion | PERSONNE | travaille_chez | Cornell AI Innovation Hub | ORGANISATION | 0.96 | DYNAMIQUE | déclaré_article |
| Cornell AI Innovation Hub | ORGANISATION | collabore_avec | Cornell Treasury Operations | ORGANISATION | 0.97 | STATIQUE | déclaré_article |
| Cornell AI Innovation Hub | ORGANISATION | a_créé | pipeline de rapprochement des paiements non identifiés | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| pipeline de rapprochement des paiements non identifiés | TECHNOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| pipeline de rapprochement des paiements non identifiés | TECHNOLOGIE | utilise | Gemini Enterprise Web Search | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| pipeline de rapprochement des paiements non identifiés | TECHNOLOGIE | utilise | Cornell AI Gateway | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Claude Code Plan Mode | METHODOLOGIE | permet | passer d'un semestre de notes à un outil fonctionnel en une seule session | AFFIRMATION | 0.90 | STATIQUE | déclaré_article |
| pipeline de rapprochement des paiements non identifiés | TECHNOLOGIE | mesure | 100 % de précision au backtest avec la chaîne IA complète (vs 97 % en fuzzy-matching seul) | MESURE | 0.93 | STATIQUE | déclaré_article |
| Cornell AI Innovation Hub | ORGANISATION | mesure | 100 000 $ récupérés sur un premier lot (5 paiements, 23 départements contactés, 7 réponses) | MESURE | 0.95 | STATIQUE | déclaré_article |
| Cornell AI Innovation Hub | ORGANISATION | affirme_que | les noms de fournisseurs figurent sur 99 % des paiements non identifiés, contre moins de 4 % pour les numéros de facture | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Cornell AI Innovation Hub | ORGANISATION | est_instance_de | Lab (framework Leader-Lab-Crowd) | CONCEPT | 0.85 | ATEMPOREL | inféré |
| Cornell Treasury Operations | ORGANISATION | est_instance_de | Crowd (framework Leader-Lab-Crowd) | CONCEPT | 0.85 | ATEMPOREL | inféré |
| Ethan Mollick | PERSONNE | recommande | récompenser les employés qui découvrent des usages transformationnels de l'IA | AFFIRMATION | 0.90 | ATEMPOREL | généré_assistant |
| récupération de 100 000 $ | CONCEPT | est_instance_de | récompense visible de l'adoption IA (vivid win, Mollick) | CONCEPT | 0.82 | ATEMPOREL | généré_assistant |
| Cornell AI Innovation Hub | ORGANISATION | recommande | une approche « contexte d'abord » (groundwork avant build) | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Cornell AI Innovation Hub | ORGANISATION | rôle | Lab IA central de Cornell ; conçoit/déploie des outils IA pour les problèmes opérationnels | AJOUT |
| Cornell Treasury Operations | ORGANISATION | rôle | Équipe métier (trésorerie) ; détentrice de la connaissance et des données (GL Oracle) | AJOUT |
| Pete Stergion | PERSONNE | rôle | Desktop Engineer, Cornell AI Innovation Hub ; co-tech lead et auteur | AJOUT |
| Phil Williammee | PERSONNE | rôle | Co-tech lead du projet, Cornell AI Innovation Hub | AJOUT |
| pipeline de rapprochement des paiements non identifiés | TECHNOLOGIE | catégorie | Pipeline Python en 3 étapes, exposé comme skill `/treasury` dans Claude Code | AJOUT |
| Claude Code Plan Mode | METHODOLOGIE | définition | Mode « contexte d'abord, plan puis build » : architecture proposée et validée avant d'écrire du code | AJOUT |
| Gemini Enterprise Web Search | TECHNOLOGIE | usage | Recherche d'identité fournisseur sur les cas inconnus | AJOUT |
| Cornell AI Gateway | TECHNOLOGIE | catégorie | Passerelle IA gouvernée (données non utilisées pour l'entraînement externe, accès restreint, PII retirées) | AJOUT |
| framework Leader-Lab-Crowd | METHODOLOGIE | source | Ethan Mollick — *Making AI Work: Leadership, Lab, and Crowd* | AJOUT |
| récompense visible de l'adoption IA | CONCEPT | définition | Preuve tangible (ici 100 000 $) qui légitime et diffuse l'adoption, en retirant la corvée plutôt que les emplois | AJOUT |
| escheatment | CONCEPT | contexte | Obligation légale (État de New York) de reverser à l'État les fonds non réclamés non résolus | AJOUT |
| Kyriba | TECHNOLOGIE | usage | Système de gestion de trésorerie (TMS) — export des paiements non identifiés | AJOUT |
