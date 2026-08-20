---
themes: [agents-codage-ia-skills, architecture-construction, economie-marche]
source: "Block Engineering"
---
# patel-block-buzz-teams-tokens-benchmarks-2026-08-06

## Veille

Billet de benchmarks **Block Engineering** du **6 août 2026**, signé **Atish Patel**, portant sur **Buzz** — le workspace humains + agents lancé le 21 juillet — et posant une question de coût : quelle est l'équipe d'agents **la moins chère qui réussit de façon fiable** ? Trois résultats. **(A) Un résultat négatif, publié en entier** : sur **Terminal-Bench 2.1**, **douze compositions d'équipe** (paires, triades, essaims bon marché sous un modèle *frontier*) ont été opposées à l'agent solo autour duquel chacune était construite, et **aucune ne l'a devancé à prix équivalent**. L'explication est structurelle — une tâche qui finit en minutes *« n'a pas assez de structure pour être divisée »*, et *« More agents mostly buys you the cost of explaining it twice »*. **(B) L'horizon retourne le résultat** : sur **Long-Horizon Terminal-Bench** (44 tâches, une tâche valant des heures de travail, même chef **GPT-5.6 Sol** en effort *high*), le solo termine 15 tâches pour 59,1 %, +2 QuickBees 19 pour 64,1 %, +1 QuickBee +1 WorkerBee 19 pour 69,5 %, **+2 WorkerBees 20 pour 71,5 %** — soit **+12,4 points**, dont 11,4 proviennent des tâches menées à leur terme. *« Same seats, opposite result, because the work is a different shape. »* Ces runs ont été conduits à **3× le timeout**, solo compris. **(C) Le prix cesse d'acheter de la qualité au-delà d'un seuil** : en solo sur Terminal-Bench 2.1, **Opus 5 en effort *xhigh* est le run le plus cher (140,63 $) pour 75,0 %**, derrière six runs allant de 20,08 $ à 109,82 $ et de 79,5 % à 88,4 % — cause déclarée, un sur-raisonnement ayant conduit 17 des 88 tâches au timeout. Entre les six meilleurs runs, **5,5× d'écart de prix pour 8,9 points d'écart de score** : *« choosing between them is not a quality decision at all. It is a budget decision. »* Le billet propose une taxonomie assumée comme *ad hoc* — **QuickBee**, **WorkerBee**, **SmartBee**, plus l'humain *« honorary bee »* — et deux formes d'équipe, la **Hive** permanente qui mémorise vos préférences et le **Swarm** jetable qui mémorise le projet. Conditions : tout tourne sur **Harbor**, contre de vrais agents Buzz sur un relais **live**, **une tentative par tâche, sans retry**, prix arrêtés au **2026-07-30**.

## Titre Article

Efficient Tokens & Effective Teams in Buzz

## Date

2026-08-06

## URL

https://engineering.block.xyz/blog/effective-teams-buzz

## Keywords

Buzz, Block, équipes d'agents, composition d'équipe, multi-agents, orchestration, QuickBee, WorkerBee, SmartBee, honorary bee, taxonomie de tiers, Hive, Swarm, équipe permanente, équipe jetable, mémoire de persona, mémoire de projet, siège plutôt que session, escalade, coordinateur, vérificateur indépendant, humain middleware, dernier relecteur, Terminal-Bench 2.1, Long-Horizon Terminal-Bench, LHTB, Harbor, relais live, résultat négatif, tâches longues, structure divisible, surcoût de coordination, timeout, sur-raisonnement, effort de raisonnement, effort medium, effort high, effort xhigh, tokens de raisonnement, coût par tâche, décision de budget, rendement décroissant, GPT-5.6 Luna, GPT-5.6 Terra, GPT-5.6 Sol, Claude Opus 5, Gemini 3.6 Flash, DeepSeek V4 Flash, Kimi K3, modèles locaux, abonnement Claude Code, Codex, multi-fournisseurs, migration de masse, Leigh Maddock, Atish Patel, revue de PR, triage de test instable

## Authors

- **Atish Patel** — *« Building AI solutions @ Block »*, auteur unique du billet, publié le **6 août 2026** sur `engineering.block.xyz`.
- **Leigh Maddock** — Engineer @ Block, cité en encadré pour un témoignage de migration (2 000+ apps/projets).

Billet de benchmarks écrit par l'éditeur du produit mesuré. Deux éléments à porter avec cette réserve : Block publie un **résultat négatif sur sa propre fonctionnalité phare**, et rappelle trois fois que **les modèles ne sont pas les siens** (OpenAI, Anthropic, Google, DeepSeek, Moonshot AI) — la métrique optimisée, *« le moins cher qui réussit »*, étant aussi celle qui valorise un workspace multi-fournisseurs.

## Ton

**Profil** : billet de benchmarks à visée prescriptive, registre ingénieur pragmatique, structuré comme un guide d'achat. Public : équipes qui exploitent déjà plusieurs agents et regardent leur facture d'inférence.

**Style** : ouverture par un **TL;DR de sept lignes**, chaque ligne associant un conseil et son chiffre, puis alternance conseil → graphique → lecture du graphique. La métaphore apicole est poussée jusqu'à devenir une taxonomie utilisable (QuickBee, WorkerBee, SmartBee, *honorary bee*), avec illustrations, et le billet désamorce lui-même l'effet de jargon : *« Note: Hive and Swarm are blog-specific terms we coined »*. L'objectif déclaré de cette grille est explicite — *« The tier + recommended effort helps you remove the noisy model releases »* : raisonner en tiers pour cesser de suivre chaque sortie de modèle. L'honnêteté est mise en scène et tenue : *« the first answer was not the one we were hoping for »*, suivi du résultat négatif publié en entier, et des astérisques annotant les anomalies du tableau (Opus 5 en timeout, Kimi K3 et DeepSeek V4 Flash ne gérant pas l'effort *medium*). Le coût est présenté comme un problème social interne : *« Paying frontier prices for the first one is how you end up explaining a inference bill in a meeting you did not want to attend. »*

**Formules-marqueurs** :
- ***« Right bee. Right team. Right task. »***
- ***« Stop being middleware »*** · ***« Stop babysitting AI »***
- ***« Paying more stops helping, then starts hurting »***
- ***« it is not a quality decision at all. It is a budget decision »***
- ***« Same seats, opposite result, because the work is a different shape »***
- ***« More agents mostly buys you the cost of explaining it twice »***
- ***« on a cheap model, reasoning tokens are the best deal available »***
- ***« the failure mode of agent tooling is not that the work is bad, it is that every ambiguity becomes a notification »***

**Position épistémique** : inhabituellement bien bornée pour un billet d'éditeur. Les conditions sont posées (Harbor, agents Buzz réels sur relais live, une tentative par tâche sans retry, prix au 2026-07-30, LHTB à 3× le timeout, *« None of the results below were measured on a stripped-down test rig »*), les anomalies sont annotées, et une conclusion est donnée pour provisoire : *« This might change if models are trained on better collaboration. »* Manquent en revanche tout intervalle de confiance, le coût des équipes LHTB, et la variation du chef dans la comparaison d'équipes ; **n=1 par tâche**.

## Pense-betes

- **Date / source** : **6 août 2026**, `engineering.block.xyz`, signé **Atish Patel**. Mesures sur **Harbor**, agents Buzz réels sur relais live, **une tentative par tâche, sans retry**, prix au **2026-07-30**.
- **Cadrage clé** : la question posée n'est pas « quelle est la meilleure équipe » mais « quelle est la moins chère qui réussit de façon fiable ». Tous les résultats en découlent.

### Résultat négatif sur les tâches courtes

Sur **Terminal-Bench 2.1**, douze compositions — paires, triades, essaims bon marché sous chef *frontier* — opposées à l'agent solo autour duquel chacune était construite : **aucune ne l'a devancé à prix équivalent**. Raison donnée comme structurelle : une tâche qui finit en minutes n'a pas assez de structure à diviser, et *« More agents mostly buys you the cost of explaining it twice. »* Règle qui en découle : ne pas monter d'équipe pour du travail court et bien spécifié. Contrepoids empirique au billet de lancement [[longwell-block-buzz-workspace-agents-nostr-2026-07-21]].

### L'horizon retourne le résultat

Long-Horizon Terminal-Bench, 44 tâches, chef GPT-5.6 Sol en effort *high* pour tous les rosters :

| Roster | Tâches finies /44 | Score |
|---|---|---|
| SmartBee solo | 15 | 59,1 % |
| + 2 QuickBees | 19 | 64,1 % |
| + 1 QuickBee + 1 WorkerBee | 19 | 69,5 % |
| **+ 2 WorkerBees** | **20** | **71,5 %** |

+12,4 points, dont **11,4 sont des complétions supplémentaires** : l'équipe ne fait pas mieux, elle va au bout. Trois précautions : runs à 3× le timeout (solo inclus), coût des équipes non publié, n=1 par tâche. Critère de décision proposé par le billet : l'équipe vaut son surcoût *« when the alternative is a human picking up unfinished work »*.

### Le plafond de rendement du prix

En solo sur Terminal-Bench 2.1, **Opus 5 en effort *xhigh* = 140,63 $ pour 75,0 %**, soit le run le plus cher, devancé par six runs entre 20,08 $ et 109,82 $ (79,5 % à 88,4 %). Cause déclarée : sur-raisonnement, avec 17 des 88 tâches au timeout. C'est d'abord un artefact de mur d'horloge — une propriété du couple modèle × harnais × timeout, non une mesure de capacité brute. Ce qui reste actionnable : *« Paying more stops helping, then starts hurting »*, et un SmartBee en effort *medium* suffit pour la plupart des tâches.

Parmi les six meilleurs runs : **5,5× d'écart de prix pour 8,9 points d'écart de score**, que le billet traite comme un ex æquo à cette taille d'échantillon. *« Everything from Terra at medium effort upward is the same agent as far as these tasks can tell. Which is good news, because it means choosing between them is not a quality decision at all. It is a budget decision. »* Portée limitée à ce benchmark, ces prix et ce harnais.

### Effort de raisonnement : l'arbitrage s'inverse selon le tier

Sur un modèle bon marché, monter l'effort est le meilleur achat : **Luna medium = 1,61 $ / 57,3 %** → **Luna high = 4,98 $ / 75,0 %**. Sur un modèle frontier, monter l'effort coûte et dégrade.

| Tier | Effort recommandé | Travail | Exemples cités |
|---|---|---|---|
| **QuickBee** | max / xhigh / high | builds, captures d'écran, suite de tests, tri de première passe | GPT-5.6 Luna, DeepSeek V4 Flash, modèles locaux |
| **WorkerBee** | high / xhigh | un sous-ensemble complet de bout en bout, sans surveillance | GPT-5.6 Terra, Gemini 3.6 Flash, modèles ouverts |
| **SmartBee** | medium | vue d'ensemble, arbitrages, absorption des escalades | Claude Opus 5, Kimi K3, GPT-5.6 Sol |
| **Humain** | — | *« The most expensive bee on the team, and the slowest. Also still the smartest. »* | — |

Le point d'inversion dépend des timeouts locaux : à retester avant de généraliser.

### Hive ou Swarm : que doit mémoriser l'équipe ?

- **Hive** — équipe **permanente** d'agents nommés, chacun avec un rôle et une mémoire de **vos** préférences. Argument cumulatif : *« The second time it reviews your peer's code it knows which nits you wave off. The tenth time, briefing it is faster than briefing a person. »*
- **Swarm** — équipe **jetable** pour un projet à début et fin (migration, montée de framework, gros refactor), qui accumule une mémoire **du projet** puis est supprimée.

Critère de choix : le sujet à mémoriser est-il vous, ou le projet ? Prérequis assumé : l'agent est **un siège, pas une session** — nom, persona, mémoire, présence propre dans le canal.

### Topologie d'escalade

Diagnostic : *« The failure mode of agent tooling is not that the work is bad, it is that every ambiguity becomes a notification. »* Le SmartBee coordinateur absorbe l'ordinaire (test instable, import ambigu, config déplacée) et **écrit les réponses humaines en mémoire**, de sorte que le Swarm devient moins cher à superviser avec le temps. *« The human stops being middleware and goes back to being the last reviewer. »* Question de qualification à poser à tout outil multi-agents : où remontent les escalades, et l'outil apprend-il des réponses ?

### Témoignage de migration

**Leigh Maddock**, Engineer @ Block : *« I migrated over 2000 apps/projects using Buzz and a Swarm of agents »*, avec 1 coordinateur, 1 à 10 migrateurs parallèles et 1 vérificateur indépendant, le coordinateur traitant la majorité des escalades. Témoignage et non mesure : ni durée, ni coût, ni taux d'échec, ni définition de « migré ». Le motif reste transposable — même patron que les *minions* one-shot décrits dans [[gray-stripe-minions-coding-agents-part1-2026-02-09]], avec en plus le vérificateur indépendant et la mémoire d'escalade.

### Compositions prêtes à l'emploi

| Cas | Composition |
|---|---|
| Revue de PR | SmartBee qui relit la PR + QuickBee qui build en local et produit les captures |
| Triage de test instable | QuickBee qui relance les tests et collecte les preuves + SmartBee qui tranche |
| Travail court | un seul agent, éventuellement un QuickBee sur des tâches connexes mais différentes |

Dénominateur commun : le tier cher lit et décide, le tier bon marché exécute et rassemble les preuves.

### Position commerciale

Buzz accepte les abonnements **Claude Code** et **Codex**, des modèles ouverts et des modèles locaux : *« You are not locked into one provider or forced to give every job to the most expensive model out of laziness. »* La composition type proposée est explicitement tri-fournisseurs. La thèse « le meilleur modèle n'est pas toujours le bon » est vraie et commercialement utile à qui vend la pièce plutôt que le modèle. Voir aussi [[paymentsdive-block-dorsey-pricing-ia-2026-08-06]].

### Conditions expérimentales, à recopier si l'exercice est rejoué

Harbor ; agents Buzz réels sur relais live (*« None of the results below were measured on a stripped-down test rig »*) ; une tentative par tâche, sans retry, avec timeouts ; LHTB à 3× le timeout, solo compris ; prix au 2026-07-30 ; Kimi K3 et DeepSeek V4 Flash ne supportent pas l'effort *medium*. Aucun intervalle de confiance, n=1 — le billet reconnaît lui-même l'ex æquo entre six runs comme un effet de taille d'échantillon. Traiter ces chiffres comme des ordres de grandeur.

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
