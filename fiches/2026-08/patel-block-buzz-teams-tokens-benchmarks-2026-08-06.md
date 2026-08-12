---
themes: [agents-codage-ia-skills, architecture-construction, economie-marche]
source: "Block Engineering"
---
# patel-block-buzz-teams-tokens-benchmarks-2026-08-06

## Veille

Billet de benchmarks **Block** du **6 août 2026** sur **Buzz** (le workspace humains+agents lancé le 21 juillet, cf. [[longwell-block-buzz-workspace-agents-nostr-2026-07-21]]) : « quelle est l'équipe d'agents **la moins chère qui réussit de façon fiable** ? ». ⭐⭐ **Le titre promet une méthode de composition d'équipe ; le résultat le plus intéressant est un résultat NÉGATIF que l'article publie quand même** : sur **Terminal-Bench 2.1**, **douze compositions d'équipe** ont été testées — paires, triades, essaims bon marché sous un modèle *frontier* — et ***aucune*** n'a battu **l'agent solo** à prix équivalent. Explication donnée : une tâche qui finit en minutes *« n'a pas assez de structure pour être divisée »*, et *« More agents mostly buys you the cost of explaining it twice »*. ⭐ **L'inversion arrive avec l'horizon** : sur **Long-Horizon Terminal-Bench** (une tâche = des heures de travail, 44 tâches, même chef **GPT-5.6 Sol** en effort *high*), le solo termine **15 tâches / 59,1 %**, +2 QuickBees **19 / 64,1 %**, +1 QuickBee +1 WorkerBee **19 / 69,5 %**, **+2 WorkerBees 20 / 71,5 %** — soit **+12,4 pts**, dont **11,4 pts viennent des tâches terminées en plus**. *« Same seats, opposite result, because the work is a different shape. »* ⚠️ Ces runs LHTB ont été faits **à 3× le timeout** (y compris le solo), la coordination ajoutant de la surcharge. ⭐⭐ **Le deuxième fait remarquable, et il est publié par un acteur qui n'y avait aucun intérêt** : sur Terminal-Bench 2.1 en solo, **Opus 5 en effort *xhigh* est le run le plus cher (140,63 $) et marque 75,0 %** — *moins* que six runs allant de 20,08 $ à 109,82 $, tous entre 79,5 % et 88,4 %. Cause déclarée : **sur-raisonnement → 17 des 88 tâches ont tapé le mur du timeout**. ⚠️ **C'est donc autant un artefact de harness qu'un jugement sur le modèle** — mais l'enseignement pratique tient : *« Paying more stops helping, then starts hurting. »* ⭐ **La conclusion économique est la phrase à retenir** : entre les six meilleurs runs, **5,5× d'écart de prix pour 8,9 pts d'écart de score**, un ex æquo à cette taille d'échantillon → *« choosing between them is not a quality decision at all. It is a budget decision. »* **La taxonomie proposée** (vocabulaire *ad hoc* du billet, assumé comme tel) : **QuickBee** (rapide et bon marché : builds, captures d'écran, suite de tests, tri de première passe — GPT-5.6 Luna, DeepSeek V4 Flash, modèles locaux — **à faire tourner en effort max/xhigh/high**), **WorkerBee** (le polyvalent, assez de jugement pour porter un sous-ensemble complet sans surveillance — GPT-5.6 Terra, Gemini 3.6 Flash, modèles ouverts — **high/xhigh**), **SmartBee** (tient la vue d'ensemble, tranche, absorbe les escalades — Claude Opus 5, Kimi K3, GPT-5.6 Sol — **effort medium**), et **l'humain « honorary bee »** : *« The most expensive bee on the team, and the slowest. Also still the smartest. »* ⭐ **Le contre-intuitif sur l'effort de raisonnement** : Luna passe de *medium* (1,61 $ / 57,3 %) à *high* (4,98 $ / 75,0 %) — **plus performant en devenant utilisable**, pour un coût qui reste dérisoire face au reste du tableau → *« on a cheap model, reasoning tokens are the best deal available »*. Inversement, un SmartBee en *medium* suffit à la plupart des tâches. **Deux formes d'équipe** : la **Hive** (équipe permanente d'agents nommés qui accumulent une mémoire de **vos** préférences — *« The tenth time, briefing it is faster than briefing a person »*) et le **Swarm** (équipe jetable qui accumule une mémoire **du projet**, supprimée à la fin). **Le témoignage à retenir** : **Leigh Maddock (ingénieur Block) déclare avoir migré plus de 2 000 apps/projets** avec un Swarm — un Coordinateur, 1 à 10 Migrateurs parallèles, un Vérificateur indépendant — le coordinateur absorbant la majorité des escalades. ⭐ **La règle d'architecture qui en découle** : faire escalader les WorkerBees **vers un coordinateur SmartBee, pas vers l'humain** — *« The human stops being middleware and goes back to being the last reviewer. »* Tout tourne sur **Harbor**, contre de vrais agents Buzz sur un relais **live**, **une tentative par tâche, sans retry**, prix au **2026-07-30**.

## Titre Article

Efficient Tokens & Effective Teams in Buzz

## Date

2026-08-06

## URL

https://engineering.block.xyz/blog/effective-teams-buzz

## Keywords

Buzz, Block, équipes d'agents, composition d'équipe, multi-agents, orchestration, QuickBee, WorkerBee, SmartBee, honorary bee, taxonomie de tiers, tier de modèle, Hive, Swarm, équipe permanente, équipe jetable, mémoire de persona, mémoire de projet, persona, siège plutôt que session, escalade, coordinateur, vérificateur indépendant, humain middleware, dernier relecteur, Terminal-Bench 2.1, Long-Horizon Terminal-Bench, LHTB, Harbor, relais live, résultat négatif, tâches longues, horizon long, tâches courtes, structure divisible, surcoût de coordination, timeout, mur d'horloge, sur-raisonnement, over-reasoning, effort de raisonnement, effort medium, effort high, effort xhigh, effort max, tokens de raisonnement, coût par tâche, décision de budget, écart de prix, plafond de score, rendement décroissant, GPT-5.6 Luna, GPT-5.6 Terra, GPT-5.6 Sol, Claude Opus 5, Gemini 3.6 Flash, DeepSeek V4 Flash, Kimi K3, modèles locaux, modèles ouverts, abonnement Claude Code, Codex, multi-fournisseurs, migration de masse, 2000 apps, Leigh Maddock, Atish Patel, revue de PR, triage de tests instables, flaky test, engineering.block.xyz

## Authors

- **Atish Patel** — *« Building AI solutions @ Block »*. Auteur unique.
- **Leigh Maddock** — Engineer @ Block, cité en encadré pour le témoignage de migration (2 000+ apps/projets).

**Position d'énonciation** : ⭐ **billet de benchmarks écrit par l'éditeur du produit mesuré** — le conflit d'intérêt est structurel, et c'est précisément ce qui rend deux passages notables. D'abord la publication d'un **résultat négatif sur sa propre fonctionnalité phare** (les équipes d'agents perdent contre le solo sur les tâches courtes). Ensuite l'insistance sur le fait que **les modèles ne sont pas de Block** — la mention est répétée trois fois, avec attribution complète (*OpenAI, Anthropic, Google, DeepSeek, Moonshot AI*) : Block se positionne en **arbitre neutre** parce qu'il ne vend aucun modèle, seulement la pièce où ils travaillent. ⚠️ À lire avec la précaution correspondante : la métrique optimisée par le billet (*« le moins cher qui réussit »*) est exactement celle qui valorise un **workspace multi-fournisseurs**.

## Ton

**Profil** : billet de benchmarks à visée prescriptive, registre **ingénieur pragmatique**, structuré comme un guide d'achat. Public : équipes qui exploitent déjà plusieurs agents et regardent leur facture d'inférence.

**Style** : ouverture par un **TL;DR de sept lignes** (chaque ligne = un conseil + son chiffre), puis alternance conseil → graphique → lecture du graphique. Trois traits :

1. **⭐ La métaphore apicole poussée jusqu'à devenir une taxonomie utilisable.** *QuickBee / WorkerBee / SmartBee / honorary bee* avec illustrations (lunettes de course, casque de chantier, cravate). Le billet **désamorce lui-même** l'effet de jargon : *« Note: Hive and Swarm are blog-specific terms we coined »*. La blague sert un objectif déclaré : *« The tier + recommended effort helps you remove the noisy model releases »* — **raisonner en tiers pour cesser de suivre chaque sortie de modèle**.
2. **L'honnêteté mise en scène.** *« the first answer was not the one we were hoping for »*, puis le résultat négatif publié en entier. Idem pour les astérisques du tableau (Opus 5 a *timeout*, Kimi K3 et DeepSeek V4 Flash ne gèrent pas *medium*). C'est le trait qui rend le reste crédible.
3. **La menace budgétaire comme argument.** *« Paying frontier prices for the first one is how you end up explaining a inference bill in a meeting you did not want to attend. »* Registre : le coût comme problème social interne, pas comme ligne de compte.

**Formules-marqueurs** : *« Right bee. Right team. Right task. »*, *« Stop being middleware »*, *« Stop babysitting AI »*, *« Paying more stops helping, then starts hurting »*, *« it is not a quality decision at all. It is a budget decision »*, *« Same seats, opposite result, because the work is a different shape »*, *« More agents mostly buys you the cost of explaining it twice »*, *« on a cheap model, reasoning tokens are the best deal available »*, *« the failure mode of agent tooling is not that the work is bad, it is that every ambiguity becomes a notification »*.

**Position épistémique** : ⭐ **inhabituellement bien bornée pour un billet vendeur**. Les conditions sont posées (Harbor, agents Buzz réels sur relais live, **une tentative par tâche, sans retry**, prix au 2026-07-30, LHTB à 3× le timeout, *« None of the results below were measured on a stripped-down test rig »*), les anomalies sont annotées, et une conclusion est explicitement présentée comme provisoire : *« This might change if models are trained on better collaboration. »* ⚠️ **Ce qui manque** : aucun intervalle de confiance, **n=1 par tâche**, aucun coût publié pour les équipes LHTB (on sait seulement qu'elles coûtent plus cher), et la comparaison d'équipes ne varie qu'un seul chef.

## Pense-betes

- **⭐⭐ Le résultat à retenir avant tout le reste, parce qu'il contredit le discours ambiant sur le multi-agents** : sur **Terminal-Bench 2.1**, **douze compositions** (paires, triades, essaims bon marché sous chef *frontier*) ont été opposées à l'agent solo autour duquel chacune était construite. ***Aucune n'a devancé le SmartBee solo à prix équivalent.*** La raison est structurelle, pas conjoncturelle : une tâche qui finit en minutes **n'a pas assez de structure à diviser**, et *« More agents mostly buys you the cost of explaining it twice. »* → **Règle opérationnelle** : ne pas monter d'équipe pour du travail court et bien spécifié. C'est le contre-poids empirique à l'enthousiasme du billet de lancement ([[longwell-block-buzz-workspace-agents-nostr-2026-07-21]]).

- **⭐⭐ L'horizon est la variable qui retourne le résultat.** Sur **Long-Horizon Terminal-Bench** (44 tâches, une tâche = des heures, chef **GPT-5.6 Sol** en *high* pour tous les rosters) :
  | Roster | Tâches finies /44 | Score |
  |---|---|---|
  | SmartBee solo | 15 | 59,1 % |
  | + 2 QuickBees | 19 | 64,1 % |
  | + 1 QuickBee + 1 WorkerBee | 19 | 69,5 % |
  | **+ 2 WorkerBees** | **20** | **71,5 %** |
  → **+12,4 pts**, dont **11,4 pts sont des complétions supplémentaires** — l'équipe ne fait pas *mieux*, elle **va au bout**. *« Same seats, opposite result, because the work is a different shape. »* ⚠️ **Trois précautions** : runs à **3× le timeout** (solo inclus) ; **le coût des équipes n'est pas publié**, seulement qu'il est supérieur ; **n=1 par tâche**. Le critère de décision proposé reste bon : l'équipe vaut son surcoût *« when the alternative is a human picking up unfinished work »*.

- **⭐⭐ Le chiffre le plus inconfortable du tableau, publié par un acteur sans intérêt à le publier** : sur Terminal-Bench 2.1 en solo, **Opus 5 en effort *xhigh* = 140,63 $, 75,0 %** — le run **le plus cher** et **battu par six runs à 20,08–109,82 $** (79,5–88,4 %). Cause déclarée : **sur-raisonnement → timeout sur 17 des 88 tâches**. ⚠️⚠️ **Ne pas surinterpréter** : c'est d'abord un **artefact de mur d'horloge**, donc une propriété *du couple modèle × harness × timeout*, pas une mesure de capacité brute. GPT-5.6 Sol présenterait le même travers en plus petit. **Ce qui reste vrai et actionnable** : *« Paying more stops helping, then starts hurting »*, et **un SmartBee en effort *medium* suffit pour la plupart des tâches** — la recommandation officielle du billet.

- **⭐ Le contre-intuitif sur l'effort, valable en sens inverse selon le tier.** Sur un **modèle bon marché**, monter l'effort est le meilleur achat disponible : **Luna medium = 1,61 $ / 57,3 %** → **Luna high = 4,98 $ / 75,0 %**, *« moves to usable while being cheaper »* que tout le haut du tableau. Sur un **modèle frontier**, monter l'effort **coûte et dégrade**. D'où la grille :
  | Tier | Effort recommandé | Travail |
  |---|---|---|
  | QuickBee | **max / xhigh / high** | builds, captures d'écran, suite de tests, tri de première passe |
  | WorkerBee | **high / xhigh** | un sous-ensemble complet de bout en bout, sans surveillance |
  | SmartBee | **medium** | vue d'ensemble, arbitrages, absorption des escalades |
  → **À tester sur votre propre outillage avant de généraliser** : le point d'inversion dépend de vos timeouts.

- **⭐ La conclusion économique, à citer telle quelle en comité** : parmi les six meilleurs runs, **5,5× d'écart de prix pour 8,9 pts d'écart de score** — un ex æquo à cette taille d'échantillon. *« Everything from Terra at medium effort upward is the same agent as far as these tasks can tell. Which is good news, because it means choosing between them is not a quality decision at all. It is a budget decision. »* ⚠️ Portée limitée à **ce benchmark, ces prix (2026-07-30), ce harness** — mais l'idée qu'**un plateau de qualité existe au-dessus d'un certain tier** est le levier de négociation le plus concret du billet.

- **⭐ Deux formes d'équipe, à distinguer par ce dont la mémoire doit se souvenir** :
  - **Hive** — équipe **permanente** d'agents nommés, chacun avec un rôle et une mémoire de **vos** préférences. L'argument est cumulatif : *« The second time it reviews your peer's code it knows which nits you wave off. The tenth time, briefing it is faster than briefing a person. »*
  - **Swarm** — équipe **jetable** pour un projet à début et fin (migration, montée de framework, gros refactor), qui accumule une mémoire **du projet** et de ses cas particuliers, puis est **supprimée**.
  → **Le critère de choix** : *le sujet à mémoriser est-il vous, ou le projet ?* C'est un principe de conception de mémoire d'agent réutilisable hors Buzz. Prérequis assumé : l'agent est **un siège, pas une session** (nom, persona, mémoire, présence propre dans le canal).

- **⭐⭐ La topologie qui fait la différence en exploitation : l'escalade remonte au coordinateur, pas à vous.** Le diagnostic est excellent — *« The failure mode of agent tooling is not that the work is bad, it is that every ambiguity becomes a notification. »* Le SmartBee coordinateur absorbe l'ordinaire (test instable, import ambigu, config déplacée) et **écrit les réponses humaines en mémoire**, si bien que **le Swarm devient moins cher à superviser avec le temps**. *« The human stops being middleware and goes back to being the last reviewer. »* → **Question de qualification à poser à tout outil multi-agents** : *où remontent les escalades, et l'outil apprend-il de mes réponses ?*

- **Le témoignage à vérifier mais trop gros pour être ignoré** — **Leigh Maddock, Engineer @ Block** : *« I migrated over 2000 apps/projects using Buzz and a Swarm of agents »*, topologie **1 Coordinateur + 1 à 10 Migrateurs parallèles + 1 Vérificateur indépendant**, le coordinateur traitant la majorité des escalades. ⚠️ **Témoignage, pas mesure** : ni durée, ni coût, ni taux d'échec, ni définition de « migré ». **Le motif reste transposable** — c'est le même patron que les *minions* one-shot de Stripe ([[gray-stripe-minions-coding-agents-part1-2026-02-09]], [[gray-stripe-minions-coding-agents-part2-2026-02-19]]), avec en plus **le vérificateur indépendant** et **la mémoire d'escalade**.

- **Compositions prêtes à l'emploi données par le billet** :
  - **Revue de PR** — SmartBee qui relit la PR + QuickBee qui build en local et produit les captures d'écran.
  - **Triage de test instable** — QuickBee qui relance les tests et collecte les preuves + SmartBee qui lit les preuves et tranche.
  - **Travail court** — un seul agent, avec éventuellement un QuickBee sur des tâches **connexes mais différentes** (builds, screenshots, tests), pas sur des morceaux de la même tâche.
  → Le dénominateur commun : **le tier cher lit et décide, le tier bon marché exécute et rassemble les preuves.**

- **⭐ Le point stratégique qui explique pourquoi Block publie ces chiffres** : Buzz accepte **vos abonnements Claude Code et Codex**, des modèles ouverts, des modèles locaux. *« You are not locked into one provider or forced to give every job to the most expensive model out of laziness. »* La composition type proposée est explicitement **tri-fournisseurs** : Claude Code/Opus 5 en SmartBee, Codex/GPT-5.6 Terra en WorkerBee, un modèle local en QuickBee. ⚠️ **Lire le billet à travers cet intérêt** : la thèse « le meilleur modèle n'est pas toujours le bon » est vraie *et* commercialement utile à qui vend la pièce plutôt que le modèle. Voir aussi la stratégie de tarification IA de Block : [[paymentsdive-block-dorsey-pricing-ia-2026-08-06]].

- **Conditions expérimentales — à recopier si vous rejouez l'exercice** : **Harbor**, vrais agents Buzz sur **relais live** (*« None of the results below were measured on a stripped-down test rig »*), **une tentative par tâche, sans retry**, avec timeouts ; **LHTB à 3× le timeout**, solo compris ; prix au **2026-07-30** ; **Kimi K3 et DeepSeek V4 Flash ne supportent pas l'effort *medium***. ⚠️ **Aucun intervalle de confiance, n=1** : le billet reconnaît d'ailleurs l'ex æquo entre six runs comme un effet de taille d'échantillon. Traiter ces chiffres comme des **ordres de grandeur**, pas comme un classement.

- **La réserve de fond que le billet formule lui-même** : *« One agent is good enough for short, well-specified tasks. **This might change if models are trained on better collaboration.** »* → **Le résultat négatif n'est pas une loi** : il mesure des modèles entraînés à travailler seuls. À rejouer à chaque génération de modèles.

## RésuméDe400mots

Billet de benchmarks de **Block** signé **Atish Patel**, publié le **6 août 2026**, prolongeant le lancement de **Buzz** : puisque monter une équipe d'agents y est devenu trivial, *quelle est la moins chère qui réussit de façon fiable ?*

**Le vocabulaire d'abord.** Le billet propose quatre tiers : **QuickBee** (rapide et bon marché — builds, captures, tests, tri de première passe : GPT-5.6 Luna, DeepSeek V4 Flash, modèles locaux, **à faire tourner en effort élevé**), **WorkerBee** (polyvalent, porte un sous-ensemble complet sans surveillance : GPT-5.6 Terra, Gemini 3.6 Flash, modèles ouverts), **SmartBee** (vue d'ensemble, arbitrages, escalades : Claude Opus 5, Kimi K3, GPT-5.6 Sol, **en effort *medium***) et l'humain, *« the most expensive bee on the team, and the slowest. Also still the smartest »*. Deux formes d'équipe : la **Hive** permanente, qui mémorise **vos** préférences, et le **Swarm** jetable, qui mémorise **le projet** puis disparaît.

**Le résultat solo.** Sur **Terminal-Bench 2.1**, monter l'effort d'un **modèle bon marché** est le meilleur achat : Luna passe de 1,61 $ / 57,3 % (*medium*) à 4,98 $ / 75,0 % (*high*). À l'autre bout, **Opus 5 en *xhigh* est le run le plus cher (140,63 $) et ne marque que 75,0 %**, ayant **atteint le timeout sur 17 des 88 tâches** par sur-raisonnement. Entre les six meilleurs runs : **5,5× d'écart de prix, 8,9 pts d'écart de score**. Conclusion : *« choosing between them is not a quality decision at all. It is a budget decision. »*

**Le résultat d'équipe, en deux temps.** Sur Terminal-Bench 2.1, **douze compositions** ont été testées et **aucune n'a battu le solo à prix équivalent** — une tâche courte n'a pas assez de structure à diviser. Sur **Long-Horizon Terminal-Bench** (44 tâches de plusieurs heures, chef GPT-5.6 Sol, **3× le timeout**), l'inversion est nette : solo **15 tâches / 59,1 %**, +2 WorkerBees **20 / 71,5 %** — **+12,4 pts, dont 11,4 dus aux complétions supplémentaires**. L'équipe coûte plus cher par tâche, ce qui se justifie *« quand l'alternative est un humain qui ramasse du travail inachevé »*.

**La règle d'exploitation.** Faire escalader les workers vers un **coordinateur SmartBee** plutôt que vers l'humain : *« every ambiguity becomes a notification »* est le vrai mode de défaillance. Un ingénieur de Block dit avoir **migré plus de 2 000 apps** avec un Swarm (coordinateur, 1-10 migrateurs, vérificateur indépendant), le coordinateur mémorisant les réponses humaines.

**Réserves** : n=1 par tâche, pas d'intervalle de confiance, coûts d'équipe non publiés, et un aveu — *« this might change if models are trained on better collaboration. »*

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Block | ORGANISATION | publie | des benchmarks d'équipes d'agents exécutés sur de vrais agents Buzz via un relais live, une tentative par tâche et sans retry | AFFIRMATION | 0.96 | STATIQUE | déclaré_article |
| Atish Patel | PERSONNE | travaille_chez | Block | ORGANISATION | 0.96 | DYNAMIQUE | déclaré_article |
| Leigh Maddock | PERSONNE | travaille_chez | Block | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Block | ORGANISATION | mesure | aucune des douze compositions d'équipe testées sur Terminal-Bench 2.1 n'a devancé l'agent solo équivalent en rapport qualité-prix | MESURE | 0.96 | STATIQUE | déclaré_article |
| Block | ORGANISATION | affirme_que | une tâche courte n'a pas assez de structure pour être divisée, et ajouter des agents ne fait qu'acheter le coût de l'expliquer deux fois | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | mesure | sur Long-Horizon Terminal-Bench, une équipe SmartBee + 2 WorkerBees termine 20 tâches sur 44 pour 71,5 %, contre 15 tâches et 59,1 % pour le SmartBee solo | MESURE | 0.96 | STATIQUE | déclaré_article |
| équipe d'agents à horizon long | METHODOLOGIE | améliore | le nombre de tâches menées à terme : +12,4 points de récompense moyenne, dont 11,4 points imputables aux complétions supplémentaires | MESURE | 0.94 | STATIQUE | déclaré_article |
| équipe d'agents à horizon long | METHODOLOGIE | s_applique_à | le travail qui court sur des heures ou se répète sur plusieurs jours, pas les tâches courtes et bien spécifiées | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | mesure | Claude Opus 5 en effort xhigh est le run solo le plus cher de Terminal-Bench 2.1 à 140,63 dollars pour 75,0 %, sous six runs facturés de 20,08 à 109,82 dollars | MESURE | 0.95 | STATIQUE | déclaré_article |
| Claude Opus 5 | TECHNOLOGIE | s_oppose_à | le mur d'horloge du harness en effort xhigh : le sur-raisonnement a provoqué un timeout sur 17 des 88 tâches | AFFIRMATION | 0.93 | STATIQUE | déclaré_article |
| effort de raisonnement élevé | CONCEPT | améliore | le score d'un modèle bon marché pour un coût marginal faible : GPT-5.6 Luna passe de 1,61 dollar et 57,3 % en medium à 4,98 dollars et 75,0 % en high | MESURE | 0.95 | STATIQUE | déclaré_article |
| effort de raisonnement élevé | CONCEPT | s_oppose_à | le rendement d'un modèle frontier, où payer davantage cesse d'aider puis commence à nuire | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | affirme_que | au-delà d'un certain tier les modèles sont indiscernables sur ces tâches, si bien que choisir entre eux n'est plus une décision de qualité mais une décision de budget | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | mesure | un écart de prix de 5,5 fois pour 8,9 points de score entre les six meilleurs runs solo de Terminal-Bench 2.1 | MESURE | 0.94 | STATIQUE | déclaré_article |
| Block | ORGANISATION | recommande | de faire tourner les QuickBees et WorkerBees en effort élevé et de réserver les tokens de SmartBee à la coordination, au jugement et aux décisions difficiles | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Hive | METHODOLOGIE | permet | de maintenir une équipe permanente d'agents nommés dont la mémoire accumule les préférences de l'utilisateur | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Swarm | METHODOLOGIE | permet | de monter une équipe jetable pour un projet borné, dont la mémoire partagée retient les cas particuliers du projet et disparaît avec lui | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Swarm | METHODOLOGIE | est_variante_de | Hive | METHODOLOGIE | 0.85 | ATEMPOREL | inféré |
| escalade agent-vers-agent | METHODOLOGIE | résout | le mode de défaillance de l'outillage agentique, où chaque ambiguïté devient une notification pour l'humain | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| escalade agent-vers-agent | METHODOLOGIE | réduit | le coût de supervision d'un Swarm au fil du temps, le coordinateur écrivant les réponses humaines en mémoire | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Leigh Maddock | PERSONNE | affirme_que | plus de 2 000 apps et projets ont été migrés chez Block avec un Swarm composé d'un coordinateur, de 1 à 10 migrateurs parallèles et d'un vérificateur indépendant | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | permet | à des agents de se déléguer du travail entre eux et de s'escalader des questions sans qu'un humain relaie quoi que ce soit | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | s_applique_à | Claude Code, Codex, modèles ouverts et modèles locaux, avec leurs abonnements existants | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | permet | de composer une équipe tri-fournisseurs : Claude Opus 5 en SmartBee, GPT-5.6 Terra en WorkerBee, un modèle local en QuickBee | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Terminal-Bench 2.1 | DOCUMENT | mesure | la performance d'agents sur des tâches de terminal courtes, achevées en minutes | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Long-Horizon Terminal-Bench | DOCUMENT | mesure | la performance d'agents sur 44 tâches dont chacune représente des heures de travail | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Harbor | TECHNOLOGIE | permet | d'exécuter ces benchmarks contre de vrais agents Buzz sur un relais live plutôt que sur un banc d'essai simplifié | AFFIRMATION | 0.91 | STATIQUE | déclaré_article |
| Block | ORGANISATION | prédit | que la supériorité de l'agent solo sur les tâches courtes pourrait s'inverser si les modèles sont entraînés à mieux collaborer | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| QuickBee | CONCEPT | définition | Tier d'agent rapide et bon marché, réservé au travail documenté : builds, captures d'écran, exécution de la suite de tests, tri de première passe. Modèles cités : GPT-5.6 Luna, DeepSeek V4 Flash, modèles locaux. Effort recommandé : max, xhigh ou high | AJOUT |
| WorkerBee | CONCEPT | définition | Tier polyvalent, doté d'assez de jugement pour porter un sous-ensemble complet de bout en bout sans surveillance, à une fraction du coût frontier. Modèles cités : GPT-5.6 Terra, Gemini 3.6 Flash, modèles ouverts. Effort recommandé : high ou xhigh | AJOUT |
| SmartBee | CONCEPT | définition | Tier qui tient la vue d'ensemble, tranche et absorbe les escalades ; à appairer avec un QuickBee ou un WorkerBee pour ne pas brûler de tokens frontier sur du travail d'exécution. Modèles cités : Claude Opus 5, Kimi K3, GPT-5.6 Sol. Effort recommandé : medium | AJOUT |
| Hive | METHODOLOGIE | définition | Équipe permanente de quelques agents nommés, chacun avec un rôle et une mémoire de persona qui accumule les préférences de l'utilisateur ; la valeur est cumulative, briefer l'agent devenant plus rapide que briefer une personne. Terme forgé par Block pour ce billet | AJOUT |
| Swarm | METHODOLOGIE | définition | Équipe jetable montée pour un projet borné (migration, montée de framework, gros refactor), qui accumule une mémoire partagée des cas particuliers du projet et est supprimée à la fin ; motif efficace : un SmartBee coordinateur, un pool de workers bon marché, un vérificateur indépendant, et une escalade qui remonte au coordinateur plutôt qu'à l'humain. Terme forgé par Block pour ce billet | AJOUT |
| escalade agent-vers-agent | METHODOLOGIE | définition | Topologie où les workers escaladent leurs questions vers un coordinateur qui en résout la majorité et n'expose à l'humain que les cas véritablement nouveaux, en écrivant les réponses humaines en mémoire ; l'humain cesse d'être un intermédiaire et redevient le dernier relecteur | AJOUT |
| Terminal-Bench 2.1 | DOCUMENT | définition | Benchmark de tâches de terminal courtes utilisé par Block pour comparer dix agents solo et douze compositions d'équipe ; 88 tâches, une tentative par tâche, sans retry, avec timeouts | AJOUT |
| Long-Horizon Terminal-Bench | DOCUMENT | définition | Benchmark de 44 tâches dont chacune représente des heures de travail, utilisé pour comparer quatre rosters menés par GPT-5.6 Sol en effort high ; runs exécutés à 3 fois le timeout habituel, solo compris, la coordination ajoutant de la surcharge | AJOUT |
| Harbor | TECHNOLOGIE | définition | Environnement d'exécution des benchmarks de Block, pilotant de vrais agents Buzz sur un relais live plutôt qu'un banc d'essai simplifié | AJOUT |
| Claude Opus 5 | TECHNOLOGIE | résultat de benchmark | Sur Terminal-Bench 2.1 solo, en effort xhigh : run le plus cher du panel à 140,63 dollars pour 75,0 %, sous six runs moins chers, en raison d'un sur-raisonnement ayant provoqué le timeout de 17 tâches sur 88. Cité comme modèle de tier SmartBee, recommandé en effort medium (prix au 2026-07-30) | AJOUT |
| GPT-5.6 Luna | TECHNOLOGIE | résultat de benchmark | Sur Terminal-Bench 2.1 solo : 1,61 dollar et 57,3 % en effort medium, 4,98 dollars et 75,0 % en effort high — illustration que sur un modèle bon marché les tokens de raisonnement sont le meilleur achat disponible (prix au 2026-07-30) | AJOUT |
| Buzz | TECHNOLOGIE | équipes d'agents | Les agents s'appellent entre eux : un SmartBee délègue un sous-ensemble à un WorkerBee, attend, relit et renvoie, sans relais humain. Chaque agent a un nom, une persona, une mémoire et sa propre présence dans le canal — un siège plutôt qu'une session | MISE_A_JOUR |
| Atish Patel | PERSONNE | rôle | Ingénieur chez Block, « Building AI solutions » ; auteur du billet de benchmarks sur les équipes d'agents dans Buzz | AJOUT |
| Leigh Maddock | PERSONNE | rôle | Ingénieur chez Block ; cité pour avoir migré plus de 2 000 apps et projets avec un Swarm Buzz composé d'un coordinateur, de 1 à 10 migrateurs parallèles et d'un vérificateur indépendant | AJOUT |
