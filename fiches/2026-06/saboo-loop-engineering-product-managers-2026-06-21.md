---
themes: [strategie-frameworks]
source: "X (Shubham Saboo)"
---
# saboo-loop-engineering-product-managers-2026-06-21

## Veille

Essai long format de **Shubham Saboo** (X/Twitter) posant une thèse sur le métier de **Product Manager** à l'ère des agents : la prochaine compétence clé n'est **pas le prompt engineering** mais le **Loop Engineering** — concevoir un *système qui s'améliore à chaque exécution* plutôt qu'écrire le prompt parfait à chaque fois. Une **boucle** = un cycle répété : on modifie ce qui façonne le comportement de l'agent → on exécute → on évalue la sortie → on garde le changement si la qualité monte, on revient en arrière sinon → on **capitalise l'apprentissage** pour que la version suivante démarre en avance. Pour un PM, le point d'entrée n'est pas le code mais les **artefacts durables** qui encodent son jugement : skill de revue de PRD, *summarizer* d'appels clients, rubrique d'évaluation, checklist de lancement, workflow de recherche, `CLAUDE.md`, template de prompt, framework de priorisation. Parce qu'ils sont réutilisés, ces artefacts **composent dans les deux sens** — et **dérivent** silencieusement (CLAUDE.md qui s'allonge, checklist ignorée…) : le modèle n'a pas régressé, les artefacts ont dérivé sans surveillance. Une boucle a **5 parties** : trigger, action, **preuve**, mémoire, **condition d'arrêt** (la plus critique). Les **evals** deviennent du travail de PM (tester l'artefact contre des exemples connus : 3 bons / 3 mauvais PRD, 5 appels compris, 2 lancements passés). La **mémoire** vit sur **GitHub** (le repo devient « mémoire produit » : commits, diffs, résultats d'éval, journal de décision, rollback). Premier loop conseillé : un **weekly product signal loop** (chaque vendredi). Le goût reste central — mais il lui faut désormais une **preuve**. Cite Boris (créateur de Claude Code) : « il n'écrit plus de prompts, il écrit des boucles ».

## Titre Article

Loop Engineering for Product Managers

## Date

2026-06-21

## URL

https://x.com/Saboo_Shubham_/status/2068730090457006588

## Keywords

Loop Engineering, product management, PM augmenté, prompt engineering, artefacts réutilisables, dérive des artefacts, drift, compounding, condition d'arrêt, boucle agentique, evals, rubrique d'évaluation, revue de PRD, summarizer d'appels clients, checklist de lancement, CLAUDE.md, mémoire produit, GitHub, versionnement, weekly product signal loop, vérification, jugement, taste, Boris Cherny, Claude Code

## Authors

Shubham Saboo (@Saboo_Shubham_)

## Ton

Profil : essai d'opinion long format publié en fil X/Twitter, perspective d'un praticien-évangéliste de l'IA produit s'adressant directement à ses pairs PM (« you »), registre didactique et prescriptif en anglais, niveau technique moyen (vocabulaire d'ingénierie rendu accessible aux non-développeurs), public cible product managers, chefs de produit et ops produit travaillant déjà avec des agents. Le ton est celui du **manifeste pédagogique** : une thèse-slogan (« the next PM skill is not prompt engineering, it is Loop Engineering »), une montée en abstraction maîtrisée (du problème concret — la dérive — vers le cadre en 5 parties), et une insistance sur l'**actionnable** (« your first loop », « the skeleton for any loop »). L'autorité s'appuie sur l'expérience terrain (exemples PRD, appels clients, lancements) et sur des cautions externes (Boris, créateur de Claude Code ; la *Loop Library* de Matthew Berman). La rhétorique procède par **oppositions binaires** (prompting une fois vs loop qui améliore à chaque run ; génération résolue vs vérification/jugement restants ; artefact qui compose vs artefact qui décaie) et par formules mémorables (« a loop that can say stop is a loop you can leave running »). Métaphore implicite : l'artefact comme organisme vivant qui, sans surveillance, **pourrit** — et la boucle comme système immunitaire qui le maintient sain. Posture finale équilibrée : « build the loop, but stay the PM ».

## Pense-betes

- **Thèse centrale** : la prochaine compétence du PM n'est pas le **prompt engineering** mais le **Loop Engineering** — *« designing a system that improves every time it runs »*, pas écrire le prompt parfait à chaque fois.
- **Définition d'une boucle** : cycle répété — modifier ce qui façonne l'agent → exécuter → évaluer → garder si la qualité monte / revert sinon → **commit l'apprentissage** pour que la version suivante parte en avance.
- **Le point d'entrée du PM = les artefacts** (pas le code) : skill de **revue de PRD**, **summarizer d'appels clients**, **rubrique d'éval**, **checklist de lancement**, **workflow de recherche**, **`CLAUDE.md`**, template de prompt, framework de priorisation. Ils sont **durables, réutilisés, et encodent le jugement** ; ils façonnent l'agent sur des dizaines de runs.
- **Compounding bidirectionnel** : un bon artefact rend le travail plus tranchant chaque semaine ; un mauvais le ralentit, silencieusement. *« A one-off prompt you can afford to get wrong. A rubric ten people depend on, you cannot. »*
- **Le problème que le prompting ne résout pas — la DÉRIVE** : le CLAUDE.md s'allonge, le skill de revue se durcit, la checklist enfle jusqu'à être à moitié ignorée, les critères d'éval changent sans qu'on sache quand/pourquoi. Un mois plus tard l'agent « semble pire » : *« the model probably did not get worse. Your artifacts drifted, and nothing was watching them. »*
- **Anatomie d'une boucle — 5 parties** : (1) **trigger** (quand elle démarre), (2) **action** (ce que l'agent fait), (3) **proof** (comment on sait que c'est meilleur), (4) **memory** (où l'apprentissage est sauvé), (5) **stop condition** (quand elle s'arrête).
- **La condition d'arrêt est la plus critique** (surtout pour les boucles récursives) : beaucoup de systèmes échouent non parce que le modèle est mauvais, mais parce que la boucle **n'a pas de sortie propre** (scope qui enfle, travail inventé, résumé confiant sans preuves). Une bonne boucle PM doit pouvoir dire : *rien n'a changé / l'input est trop mince / c'est bloqué / la barre qualité n'est pas atteinte / ça demande une décision humaine.* *« A loop that can say stop is a loop you can leave running. »*
- **Les evals deviennent du travail de PM** : pas un benchmark géant — partir d'**exemples connus**. Ex. 3 PRD forts / 3 faibles → l'artefact attrape-t-il les vrais trous sans pinailler, en préservant l'intention ? ; 5 appels déjà compris → capte-t-il la vraie douleur, cite-t-il juste, distingue-t-il signal fort et bruit ? ; 2 lancements passés (1 propre, 1 raté) → aurait-il attrapé ce qui a cassé ? Question : *« did this artifact improve against known product judgment ? »* (pas « l'agent a-t-il l'air intelligent ? »).
- **Couche mémoire = GitHub** : pas pour faire des PM des ingénieurs, mais pour le **version history** des artefacts. Y vivent l'artefact, les changements, les résultats d'éval, le journal de décision, le chemin de rollback. *« The repo becomes product memory. »*
- **Premier loop recommandé — weekly product signal loop** : ne pas commencer par la stratégie (trop large/subjectif) mais par les **ops produit**. Chaque vendredi : lire appels clients, tickets support, notes sales, updates d'expériences, résumés analytics, changements livrés, escalades ouvertes → produire **un memo de signal produit** qui sépare **signal répété** et **bruit isolé**, cite le verbatim client, montre ce qui a changé, signale les preuves minces, et dit quelles hypothèses de roadmap se sont renforcées/affaiblies.
- **Le goût (taste) reste central mais a besoin de PREUVE** : quand on met son jugement dans des artefacts réutilisables, il faut prouver qu'un changement améliore vraiment (sinon on ajoute du bruit ou de la « cérémonie »).
- **Frontière humaine** : une boucle peut résumer des preuves, réviser un PRD, signaler un lancement risqué — elle **ne doit pas** décider seule la stratégie, devenir le leader produit, ni arbitrer sans contexte. *« Build the loop, but stay the PM. »* Augmenter l'autonomie **lentement**, après gain de confiance.
- **Citations & cautions** : Boris (créateur de Claude Code) *« ne prompt plus, il écrit des boucles qui prompt pour lui »* ; *« Generation is solved… Verification and judgment are all that's left »* ; **Loop Library** de **Matthew Berman** (boucles réelles eng/research/ops).
- **À relier (fort)** : converge directement avec le **Compound Engineering** (« chaque unité de travail rend la suivante plus facile », artefacts qui composent) et la **phase Compound du SDLC** ; écho à **Stack Overflow for Agents** (capitaliser/vérifier au lieu de régénérer) et à Monperrus / la doctrine *vérification > génération*. Le `CLAUDE.md` comme artefact vivant à versionner rejoint la doctrine *context engineering*.

## RésuméDe400mots

Dans cet essai long format publié sur X, **Shubham Saboo** soutient que la prochaine compétence décisive du Product Manager à l'ère des agents n'est pas le **prompt engineering** mais le **Loop Engineering**. L'état final n'est pas un PM écrivant le prompt parfait chaque fois qu'il a besoin de quelque chose, mais un PM **concevant un système qui s'améliore à chaque exécution**. Une boucle est un cycle répété : on modifie ce qui façonne le comportement de l'agent, on exécute, on évalue la sortie, on conserve le changement si la qualité progresse et on l'annule sinon, puis on **capitalise l'apprentissage** pour que la version suivante démarre en avance.

Pour un ingénieur, ce cycle part du code. Pour un PM, il part des **artefacts** qui structurent le travail produit : skill de revue de PRD, *summarizer* d'appels clients, rubrique d'évaluation, checklist de lancement, workflow de recherche, `CLAUDE.md`, template de prompt, framework de priorisation. Durables et réutilisés, ils encodent le jugement et façonnent l'agent sur des dizaines de runs — donc ils **composent dans les deux sens**. C'est là qu'intervient le vrai problème : la **dérive**. Le CLAUDE.md s'allonge, la checklist enfle, les critères d'éval changent sans trace ; un mois plus tard l'agent « semble pire ». Le modèle n'a pas régressé : les artefacts ont dérivé sans surveillance, et c'est précisément ce que le Loop Engineering corrige.

Une boucle utile a **cinq parties** : trigger, action, **preuve**, mémoire, **condition d'arrêt**. Cette dernière est la plus critique : beaucoup de systèmes échouent faute de sortie propre (scope qui enfle, résumé confiant sans preuves). Une bonne boucle doit pouvoir dire « stop » — rien n'a changé, input trop mince, bloqué, barre non atteinte, décision humaine requise.

Mettre son jugement dans des artefacts réutilisables impose que le **goût** ait désormais une **preuve** : les **evals** deviennent du travail de PM, à partir d'exemples connus (3 bons / 3 mauvais PRD, 5 appels compris, 2 lancements passés). La question n'est plus « l'agent a-t-il l'air intelligent ? » mais « cet artefact s'améliore-t-il face à un jugement produit connu ? ». L'apprentissage a besoin d'une **mémoire** : **GitHub**, où vivent artefact, diffs, résultats d'éval, journal de décision et rollback — *« the repo becomes product memory »*.

Saboo conseille de commencer petit, par les **ops produit** : un **weekly product signal loop** (chaque vendredi) produisant un memo qui sépare signal répété et bruit isolé. La boucle informe une décision que le PM **garde** : *« build the loop, but stay the PM »*. La génération est résolue ; restent la vérification et le jugement.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Shubham Saboo | PERSONNE | publie | Loop Engineering for Product Managers | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Shubham Saboo | PERSONNE | recommande | le Loop Engineering comme prochaine compétence clé des PM | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Loop Engineering | METHODOLOGIE | remplace | prompt engineering | METHODOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Loop Engineering | METHODOLOGIE | utilise | artefacts réutilisables (revue de PRD, summarizer, rubrique d'éval, checklist) | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Loop Engineering | METHODOLOGIE | résout | dérive des artefacts (artifact drift) | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Loop Engineering | METHODOLOGIE | utilise | condition d'arrêt (stop condition) | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Loop Engineering | METHODOLOGIE | s_applique_à | product management (ops produit) | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| évaluations (evals) | METHODOLOGIE | permet | preuve qu'un artefact s'améliore face à un jugement produit connu | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| GitHub | TECHNOLOGIE | permet | mémoire produit (version history des artefacts) | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| weekly product signal loop | METHODOLOGIE | est_instance_de | Loop Engineering | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| Loop Engineering | METHODOLOGIE | converge_avec | Compound Engineering | METHODOLOGIE | 0.82 | ATEMPOREL | inféré |
| Boris Cherny | PERSONNE | a_créé | Claude Code | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Boris Cherny | PERSONNE | affirme_que | il n'écrit plus de prompts mais des boucles qui prompt pour lui | CITATION | 0.88 | STATIQUE | déclaré_article |
| Shubham Saboo | PERSONNE | affirme_que | la génération est résolue ; vérification et jugement sont tout ce qui reste | CITATION | 0.9 | ATEMPOREL | déclaré_article |
| Matthew Berman | PERSONNE | a_créé | Loop Library | DOCUMENT | 0.85 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Loop Engineering | METHODOLOGIE | définition | Concevoir un système qui s'améliore à chaque run via des boucles à 5 parties (trigger, action, preuve, mémoire, stop) | AJOUT |
| Shubham Saboo | PERSONNE | rôle | Praticien IA produit, auteur de l'essai | AJOUT |
| dérive des artefacts (artifact drift) | CONCEPT | définition | Décroissance silencieuse de la qualité quand les artefacts (CLAUDE.md, rubriques, checklists) évoluent sans surveillance | AJOUT |
| weekly product signal loop | METHODOLOGIE | rôle | Premier loop conseillé : memo hebdo séparant signal répété et bruit isolé (ops produit) | AJOUT |
| évaluations (evals) | METHODOLOGIE | rôle | Tester un artefact contre des exemples connus (3 bons/3 mauvais PRD, 5 appels, 2 lancements) | AJOUT |
| GitHub | TECHNOLOGIE | rôle | Couche mémoire des artefacts PM (« the repo becomes product memory ») | AJOUT |
| condition d'arrêt (stop condition) | CONCEPT | rôle | Sortie propre d'une boucle : la partie la plus critique, surtout en récursif | AJOUT |
| Loop Library | DOCUMENT | rôle | Collection de boucles réelles (eng/research/ops) de Matthew Berman | AJOUT |
| CLAUDE.md | DOCUMENT | rôle | Artefact vivant qui façonne l'agent, sujet à dérive, à versionner | AJOUT |
