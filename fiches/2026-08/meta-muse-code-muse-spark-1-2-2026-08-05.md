---
themes: [agents-codage-ia-skills, outils-plateformes, produits-services]
source: "Meta AI Research"
---
# meta-muse-code-muse-spark-1-2-2026-08-05

## Veille

Annonce de **Meta AI Research** publiée le **5 août 2026** (lecture annoncée : 4 minutes, aucune signature individuelle) : **Muse Code** en bêta, *« a terminal coding agent »*, et le modèle qui l'anime, **Muse Spark 1.2**. Meta situe elle-même le lancement : *« This marks our next step toward the frontier, with larger and much more capable models on the way »* — **un pas vers la frontière, pas une prise de tête**. **Trois éléments d'architecture** sont décrits côté harnais : des **agents d'arrière-plan asynchrones** qui *« remain active throughout each session, rather than being spawned for individual tasks »*, afin d'éviter la collecte d'information redondante et de réduire le besoin de pilotage ; un **journal d'événements local** où *« every model call, tool run, approval, and edit is appended »*, faisant du runtime un système *« replay-exact and restart-safe »* capable de reprendre exactement où il s'est arrêté après un plantage ; et **trois skills livrées d'origine** — `/plan` (transforme une tâche en plan soumis à approbation), **`/grill`** (met le plan à l'épreuve *« until it holds up »*) et `/goal`. Côté modèle, Meta revendique un **co-entraînement du modèle avec le harnais** (*« to maximize harness compatibility »*, avec trajectoires de harnais échantillonnées par rejet et optimisations de recette pour les buts, la compaction et les sous-agents), un entraînement **long-horizon** (génération de dépôt entier, projets bout-en-bout, auto-recherche, avec planification, conditionnement par le but et **compaction de contexte**), et une **boucle d'auto-amélioration** où Muse Spark 1.1 génère les environnements et les gabarits d'instructions **puis note les solutions candidates**, produisant un jeu d'entraînement pour la 1.2. ⚠️ **Le fait le plus notable de cette annonce n'est écrit nulle part dans son texte** : les quatre graphiques publiés — Terminal-Bench 2.1, DeepSWE 1.1, un benchmark interne Meta, et l'étude de cas d'optimisation de noyaux GPU — **placent Muse Spark 1.2 derrière Opus 5 dans les quatre cas**, y compris sur le benchmark propriétaire de Meta (70,6 % contre 79,4 %) et sur l'étude de cas, où le modèle finit **quatrième sur six** (+68,7 % contre +74,0 %). ⚠️ **Et le gain réel du modèle est plus faible qu'il n'y paraît** : sur les deux benchmarks publics, la 1.1 est mesurée avec `mini-swe-agent` et la 1.2 avec Muse Code — l'écart de 6,7 points mélange donc modèle et harnais. Sur le benchmark interne, seul comparatif où aucun harnais n'est mentionné, l'écart 1.1 → 1.2 tombe à **2,3 points**.

## Titre Article

Introducing Muse Code and Muse Spark 1.2

## Date

2026-08-05

## URL

https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2

## Keywords

Meta AI Research, Muse Code, Muse Spark 1.2, agent de codage terminal, bêta, harnais, agents d'arrière-plan asynchrones, sous-agents persistants, collecte d'information redondante, journal d'événements, event log, replay-exact, restart-safe, reprise après plantage, tâches longues, skills livrées, plan approuvé, grill, goal, co-entraînement modèle harnais, échantillonnage par rejet, trajectoires de harnais, compatibilité de harnais, long-horizon, génération de dépôt entier, auto-recherche, conditionnement par le but, compaction de contexte, auto-amélioration, génération d'environnements, notation de solutions, Terminal-Bench 2.1, DeepSWE 1.1, benchmark interne, Opus 5, Claude Code, GPT 5.6 Terra, GPT 5.6 Sol, Codex, Grok 4.5, Gemini 3.6 Flash, Antigravity CLI, mini-swe-agent, optimisation de noyaux GPU, Triton, KDA, MLA, NVIDIA Hopper, appels d'outils cumulés, accélération contre baseline, FLA, fusion de noyaux, tiling, Meta Model API, verrouillage par optimisation

## Authors

**Meta AI Research** — publication institutionnelle sans auteur nommé, sur `research.meta.ai`. Le billet renvoie à un **rapport** pour la méthodologie d'évaluation, non repris ici.

**Positionnement à connaître** : Meta arrive sur le terrain de l'agent de codage en terminal **après** Claude Code, Codex, Gemini CLI, Grok Build et Antigravity CLI, et le dit — *« our next step toward the frontier »*. L'annonce couple un **produit** (Muse Code, distribué par `curl … | bash`) et un **modèle** (Muse Spark 1.2, disponible dans Muse Code et dans **Meta Model API** avec *« expanded global access »*), les deux ayant été entraînés ensemble.

## Ton

**Profil** : annonce produit de laboratoire de recherche, format court, registre technique sobre. Aucune hyperbole, aucune revendication de supériorité, aucun superlatif — ce qui est **inhabituel pour un lancement** et constitue en soi une information.

**Style** : le texte procède par **description de mécanismes**, section par section, chacune tenant en un paragraphe et nommant une décision d'ingénierie précise — la persistance des sous-agents, le journal d'événements, le co-entraînement, la compaction. Il n'y a ni cas client, ni citation de dirigeant, ni promesse de productivité. La seule démonstration narrative est une vignette : un utilisateur dépose la vidéo d'une visite de maison en `mp4` dans le terminal, Muse Code l'interprète et produit une page de réservation de location saisonnière.

**Le trait le plus notable est la modestie du cadrage**, posée dès la deuxième phrase : *« This marks our next step toward the frontier, with larger and much more capable models on the way. »* Meta annonce un jalon et prévient que le meilleur est à venir. La conclusion reprend la même posture : *« We have a lot on the horizon, including new harness features and more powerful models. »*

**Cette modestie se vérifie dans les graphiques**, et c'est ce qui rend l'annonce singulière : Meta publie quatre comparatifs où elle ne gagne jamais. Peu de lancements assument de montrer un concurrent en tête sur leur propre page — encore moins sur leur **propre benchmark interne**.

**Formules-marqueurs** : *« our next step toward the frontier »*, *« rather than being spawned for individual tasks »*, *« replay-exact and restart-safe »*, *« /grill stress-tests that plan until it holds up »*, *« to maximize harness compatibility »*.

## Pense-betes

- **Ce qui est lancé** : **Muse Code** (bêta), agent de codage en terminal installé par `curl -fsSL https://dev.meta.ai/install.sh | bash` sur macOS et Linux, et **Muse Spark 1.2**, modèle disponible dans Muse Code et dans **Meta Model API**.

- **⭐⭐ Le résultat d'ensemble, absent du texte et lisible seulement dans les images** — Meta perd ses quatre comparatifs :
  | Comparatif | Vainqueur | Muse Spark 1.2 | Rang |
  |---|---|---|---|
  | Terminal-Bench 2.1 | Opus 5 + Claude Code — **86,7 %** | 82,9 % | 2ᵉ / 6 |
  | DeepSWE 1.1 | Opus 5 + Claude Code — **65,0 %** | 59,3 % | 3ᵉ / 6 |
  | **Meta Internal Coding Bench** | Opus 5 — **79,4 %** | 70,6 % | 2ᵉ / 5 |
  | Étude de cas KDA (accélération) | Opus 5 — **+74,0 %** | +68,7 % | **4ᵉ / 6** |
  → **Sur son propre benchmark propriétaire, Meta se place à 8,8 points derrière Opus 5.** Et sur l'étude de cas qu'elle a choisie pour vitrine, elle passe aussi derrière GPT 5.6 Sol (+71,2 %) et derrière **la génération précédente d'Anthropic**, Opus 4.8 (+69,6 %). C'est le fait central de l'annonce, et il faut aller lire les PNG pour le trouver.

- **⭐⭐ Le gain modèle est plus faible qu'annoncé, et le harnais explique le reste** — la lecture la plus utile de ces chiffres :
  - Sur **Terminal-Bench** et **DeepSWE**, la 1.1 est évaluée avec **`mini-swe-agent`** et la 1.2 avec **Muse Code**. L'écart affiché (76,2 → 82,9, soit **+6,7 points**) mélange donc **progrès du modèle et progrès du harnais**.
  - Sur le **benchmark interne**, seul tableau où **aucun harnais n'est indiqué**, l'écart 1.1 → 1.2 tombe à **68,3 → 70,6, soit +2,3 points**.
  → **Le modèle progresse d'environ deux points ; le reste vient de l'outillage autour de lui.** Meta le dit d'ailleurs à demi-mot en revendiquant le co-entraînement *« to maximize harness compatibility »*. **Aucune de ces comparaisons n'est modèle contre modèle : ce sont des paires modèle + harnais.**

- **⭐ Et cela valide empiriquement la thèse de Mozilla, à trois semaines d'intervalle** : [[mozilla-state-of-open-source-ai-2026-07]] écrivait *« the model is eating the harness »*, constatait que *« on every model where both appear, the lab's own harness now wins »*, et formulait le mécanisme — *« a harness tuned tightly to one lab's weights becomes a fitted component of that lab's product… the tighter the tuning, the less swappable the weights underneath. **Lock-in arrives as a side effect of optimization.** »* **Muse Code + Muse Spark 1.2 est exactement cet objet** : Meta annonce explicitement avoir entraîné le modèle *avec* le harnais pour maximiser leur compatibilité. Le tableau de Terminal-Bench le montre en creux — chaque modèle y est mesuré avec le harnais de son propre laboratoire.

- **Le journal d'événements — la meilleure idée d'ingénierie du billet** : *« a local event log in which every model call, tool run, approval, and edit is appended »*, source unique de vérité qui rend le runtime *« replay-exact and restart-safe »*. Après un plantage, l'agent reprend **exactement** où il s'était arrêté, ce qui autorise les tâches longues. → **Convergence directe avec le manifeste de run et la commande `run resume` d'[[skill-gibbs-hyperresearch-2026-08-03]]**, où le manifeste est décrit comme *« your durable memory »*. Deux équipes indépendantes arrivent au même dispositif : **le contexte ne survit pas, un journal sur disque si.**

- **⭐ Les agents d'arrière-plan persistants — une rupture avec le modèle dominant** : au lieu d'être créés pour une tâche puis détruits, ils *« remain active throughout each session »*, ce qui évite *« redundant information gathering »*, décide **eux-mêmes** quand remonter au principal, et réduit *« latency and the need for steering »*. → À rapprocher du constat inverse de Hugo Lassiège sur les sous-agents jetables — *« je les utilise de moins en moins, les agents récents font eux-mêmes des délégations assez ciblées »* ([[lassiege-usine-logicielle-heure-ia-2026-07-28]]). **Deux réponses opposées au même problème** : Lassiège délègue moins, Meta délègue à des agents qui ne meurent plus.

- **⭐ `/grill` est livrée d'origine, et le nom n'est pas un hasard** : *« /grill stress-tests that plan until it holds up »*. C'est très exactement la fonction de la skill `grill-with-docs` de Matt Pocock, fichée dans ce corpus depuis juin ([[skill-pocock-grill-with-docs-2026-06]]) — une interview adversariale qui met un plan à l'épreuve avant l'implémentation. **Un pattern né dans la communauté des skills arrive préinstallé chez un laboratoire de frontière.** Signal de maturation : les bonnes pratiques de harnais deviennent des primitives produit.

- **Le triptyque livré** — `/plan` (plan **soumis à approbation**), `/grill` (mise à l'épreuve), `/goal` (poursuite de l'objectif) — décrit une boucle **plan → contestation → exécution** avec un **gate humain** à la première étape. C'est la forme canonique documentée par [[osmani-agent-harness-engineering-2026-04-19]], désormais empaquetée.

- **Auto-amélioration, à lire précisément** : *« We also used Muse Spark 1.1 to generate challenging coding environments and instruction-following templates. The model then graded candidate solutions… producing a scalable training dataset for Muse Spark 1.2. »* → **C'est la 1.1 qui génère les environnements *et* qui note**, la 1.2 étant le produit de ce jeu de données. ⚠️ Le sujet de *« the model »* est ambigu et certaines reprises l'ont lu comme la 1.2 ; la lecture naturelle est la 1.1, seule nommée. **Boucle de distillation d'une génération sur elle-même**, dont la limite connue est qu'elle ne peut enseigner que ce que la génération précédente sait déjà évaluer.

- **Étude de cas noyaux GPU — le protocole est plus intéressant que le résultat** : optimisation itérative sur **plus de 1 000 appels d'outils, jusqu'à 24 heures**, sur les noyaux **KDA** et **MLA** pour GPU **NVIDIA Hopper**. Le modèle écrit, compile, profile et améliore progressivement. ⭐ **Contrainte notable** : *« Models were prohibited from importing third-party kernel libraries such as FLA directly »* — il fallait réimplémenter l'algorithme en Triton, pas envelopper une implémentation existante. **C'est ce qui rend le test honnête**, et c'est le genre de garde-fou qui manque à beaucoup de démonstrations d'agents.
  - Sur **KDA** : noyau de préparation parallèle par blocs plus balayage séquentiel inter-blocs, avec re-centrage de la décroissance cumulative au milieu du bloc.
  - Sur **MLA** : pipeline Triton à deux noyaux, réutilisant le latent KV partagé comme K et comme V, mesuré à taille de lot 1, 64 têtes, séquence 8 192, dimension latente 512.
  - ⚠️ **KDA est l'attention linéaire de Kimi** (cf. [[sfeir-kimi-k3-moonshot-frontier-open-weights-2026-07-16]]) : Meta fait donc optimiser par son agent le noyau d'une architecture concurrente open-weights. Détail savoureux et révélateur de la circulation des architectures.

- **⚠️ Trois réserves de méthode sur les graphiques** :
  1. **Aucun chiffre n'apparaît dans le texte.** Les quatre comparatifs sont des **images matricielles** sans données textuelles ni libellé d'accessibilité chiffré. Un lecteur pressé, un agrégateur ou un agent qui lit la page **ne voit aucun résultat**. Les valeurs de cette fiche ont été relevées par lecture visuelle des PNG.
  2. **L'axe des ordonnées du graphique KDA est non linéaire**, ce que Meta signale honnêtement (*« Axis Spaced Linearly In X »*, graduations 0-27-43-53-60-65-69-72-75 %). L'échelle **dilate le haut de la plage**, ce qui accentue visuellement les écarts entre les modèles de tête — au détriment de Meta, en l'occurrence.
  3. **Les configurations comparées ne sont pas homogènes** : `max` pour Opus 5 et GPT 5.6 Terra, `high` pour Grok 4.5 et Gemini 3.6 Flash, rien pour Muse Spark. Et Grok est absent du benchmark interne, GPT 5.6 Sol n'apparaît que dans l'étude de cas. **La composition du panel change d'un graphique à l'autre.**

- **⚠️ Le benchmark interne est invérifiable** : *« Meta Internal Coding Bench »* n'est pas public, sa composition n'est pas décrite dans le billet, et Meta y mesure ses concurrents. Le fait qu'elle y **perde** rend le chiffre plus crédible qu'un score flatteur — mais un benchmark propriétaire reste non reproductible.

- **Ce que l'annonce ne dit pas** : ni prix, ni limites d'usage, ni licence du modèle, ni ouverture des poids — rupture notable avec la tradition Llama de Meta, sur laquelle le billet est muet. Rien non plus sur les langages supportés, la taille de contexte, ni les garanties de confidentialité du code envoyé.

- **Méta / à relier** : confirmation empirique du mécanisme de verrouillage par optimisation décrit dans [[mozilla-state-of-open-source-ai-2026-07]] ; journal d'événements et reprise à rapprocher de [[skill-gibbs-hyperresearch-2026-08-03]] ; `/grill` préinstallé face à [[skill-pocock-grill-with-docs-2026-06]] ; doctrine du harnais dans [[osmani-agent-harness-engineering-2026-04-19]] et [[lassiege-usine-logicielle-heure-ia-2026-07-28]] ; concurrents cités dans [[sfeir-gpt56-sol-terra-luna-coding-agentique-pricing-2026-07-13]] et [[cherny-wu-reflecting-year-claude-code-2026-07-17]] ; noyau KDA et architecture Kimi dans [[sfeir-kimi-k3-moonshot-frontier-open-weights-2026-07-16]].

## RésuméDe400mots

Annonce de **Meta AI Research** du **5 août 2026** : **Muse Code** en bêta, agent de codage en terminal, et **Muse Spark 1.2**, le modèle qui l'anime. Meta situe elle-même le lancement — *« our next step toward the frontier, with larger and much more capable models on the way »*.

**Côté harnais, trois décisions.** Des **agents d'arrière-plan asynchrones** qui *« remain active throughout each session, rather than being spawned for individual tasks »*, évitant la collecte d'information redondante et décidant eux-mêmes quand remonter à l'agent principal. Un **journal d'événements local** consignant chaque appel de modèle, exécution d'outil, approbation et édition, ce qui rend le runtime *« replay-exact and restart-safe »* : après un plantage, l'agent reprend exactement où il s'était arrêté. Et trois **skills livrées d'origine** : `/plan` (plan soumis à approbation), **`/grill`** (met le plan à l'épreuve jusqu'à ce qu'il tienne) et `/goal`.

**Côté modèle**, Meta revendique un **co-entraînement avec le harnais** *« to maximize harness compatibility »*, un entraînement long-horizon (dépôt entier, projets bout-en-bout, auto-recherche, compaction de contexte) et une boucle d'auto-amélioration où la version 1.1 génère les environnements et note les solutions, produisant le jeu d'entraînement de la 1.2.

**Le fait central de cette annonce n'est écrit nulle part dans son texte.** Les quatre comparatifs publiés existent uniquement sous forme d'images, et ils placent Muse Spark 1.2 **derrière Opus 5 dans les quatre cas** : 82,9 % contre 86,7 % sur Terminal-Bench 2.1, 59,3 % contre 65,0 % sur DeepSWE 1.1, **70,6 % contre 79,4 % sur le benchmark interne de Meta elle-même**, et +68,7 % contre +74,0 % sur l'étude de cas d'optimisation de noyaux GPU, où le modèle finit **quatrième sur six**, derrière GPT 5.6 Sol et derrière la génération précédente d'Anthropic.

**Et le gain propre au modèle est plus faible qu'il n'y paraît.** Sur les deux benchmarks publics, la version 1.1 est évaluée avec `mini-swe-agent` et la 1.2 avec Muse Code : l'écart de 6,7 points mélange modèle et harnais. Sur le benchmark interne, seul comparatif sans harnais indiqué, il tombe à **2,3 points**.

L'annonce vaut donc surtout comme **confirmation empirique** d'une thèse déjà posée : la valeur se déplace vers le harnais, et un harnais co-entraîné avec ses propres poids rend ces poids d'autant moins interchangeables.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Meta AI Research | ORGANISATION | publie | Muse Code | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Meta AI Research | ORGANISATION | publie | Muse Spark 1.2 | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Muse Spark 1.2 | TECHNOLOGIE | est_variante_de | Muse Spark 1.1 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Muse Code | TECHNOLOGIE | utilise | Muse Spark 1.2 | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Muse Spark 1.2 | TECHNOLOGIE | est_basé_sur | un co-entraînement avec le harnais Muse Code pour maximiser leur compatibilité | AFFIRMATION | 0.95 | STATIQUE | déclaré_article |
| co-entraînement d'un modèle avec son harnais | CONCEPT | réduit | l'interchangeabilité des poids sous-jacents | AFFIRMATION | 0.85 | ATEMPOREL | inféré |
| journal d'événements local | CONCEPT | permet | de reprendre exactement où l'agent s'est arrêté après un plantage | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| agents d'arrière-plan persistants | CONCEPT | s_oppose_à | les sous-agents créés puis détruits pour chaque tâche | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| agents d'arrière-plan persistants | CONCEPT | réduit | la collecte d'information redondante et le besoin de pilotage | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Muse Code | TECHNOLOGIE | utilise | une skill de mise à l'épreuve du plan avant implémentation | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Muse Spark 1.1 | TECHNOLOGIE | permet | de générer les environnements et de noter les solutions ayant servi à entraîner Muse Spark 1.2 | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Opus 5 | TECHNOLOGIE | surpasse | Muse Spark 1.2 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Muse Spark 1.2 | TECHNOLOGIE | mesure | 82,9 % sur Terminal-Bench 2.1 contre 86,7 % pour Opus 5 avec Claude Code | MESURE | 0.93 | STATIQUE | déclaré_article |
| Muse Spark 1.2 | TECHNOLOGIE | mesure | 59,3 % sur DeepSWE 1.1 contre 65,0 % pour Opus 5 et 64,8 % pour GPT 5.6 Terra | MESURE | 0.93 | STATIQUE | déclaré_article |
| Muse Spark 1.2 | TECHNOLOGIE | mesure | 70,6 % sur le benchmark interne de Meta contre 79,4 % pour Opus 5 | MESURE | 0.92 | STATIQUE | déclaré_article |
| Muse Spark 1.2 | TECHNOLOGIE | mesure | une accélération de noyau KDA de +68,7 %, quatrième derrière Opus 5, GPT 5.6 Sol et Opus 4.8 | MESURE | 0.92 | STATIQUE | déclaré_article |
| comparaison de paires modèle et harnais | CONCEPT | s_oppose_à | une comparaison de modèles isolés, les deux benchmarks publics évaluant chaque modèle avec le harnais de son laboratoire | AFFIRMATION | 0.9 | ATEMPOREL | inféré |
| gain entre versions | CONCEPT | mesure | 2,3 points sur le seul comparatif sans harnais indiqué, contre 6,7 points sur les comparatifs avec harnais | MESURE | 0.88 | STATIQUE | inféré |
| Muse Code | TECHNOLOGIE | s_applique_à | l'optimisation itérative de noyaux GPU sur plus de 1 000 appels d'outils et jusqu'à 24 heures | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| interdiction d'importer une bibliothèque de noyaux tierce | CONCEPT | permet | de tester la réimplémentation d'un algorithme plutôt que l'enveloppement d'une implémentation existante | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Meta AI Research | ORGANISATION | affirme_que | ce lancement est une étape vers la frontière, des modèles plus grands et plus capables étant à venir | CITATION | 0.95 | DYNAMIQUE | déclaré_article |
| benchmarks publiés uniquement en image | CONCEPT | s_oppose_à | la lisibilité des résultats par un agrégateur ou un agent lisant la page | AFFIRMATION | 0.88 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Muse Code | TECHNOLOGIE | définition | Agent de codage en terminal de Meta, en bêta au 5 août 2026 : agents d'arrière-plan persistants, journal d'événements rendant le runtime rejouable et reprenable, et trois skills livrées d'origine — plan approuvé, mise à l'épreuve du plan, poursuite d'objectif | AJOUT |
| Muse Spark 1.2 | TECHNOLOGIE | définition | Modèle orienté codage de Meta, co-entraîné avec le harnais Muse Code, entraîné sur des tâches longues avec compaction de contexte et issu d'une boucle d'auto-amélioration alimentée par la version précédente | AJOUT |
| Muse Spark 1.2 | TECHNOLOGIE | performance | Second derrière Opus 5 sur Terminal-Bench 2.1 (82,9 % contre 86,7 %), troisième sur DeepSWE 1.1 (59,3 %), second sur le benchmark interne Meta (70,6 % contre 79,4 %), quatrième sur six dans l'étude de cas KDA (+68,7 %) | AJOUT |
| Meta AI Research | ORGANISATION | positionnement | Entre sur le marché de l'agent de codage en terminal après ses concurrents et l'assume, en publiant quatre comparatifs où son modèle ne prend jamais la tête, y compris sur son propre benchmark interne | AJOUT |
| agents d'arrière-plan persistants | CONCEPT | définition | Sous-agents spécialisés maintenus actifs pendant toute une session au lieu d'être créés par tâche, ce qui évite de refaire la même collecte d'information et laisse à l'agent le choix du moment où il remonte au principal | AJOUT |
| journal d'événements d'agent | CONCEPT | définition | Trace locale append-only de chaque appel de modèle, exécution d'outil, approbation et édition, servant de source unique de vérité pour rejouer et reprendre une session interrompue | AJOUT |
| Meta Internal Coding Bench | DOCUMENT | référence | Benchmark de codage propriétaire de Meta, non public et de composition non décrite, sur lequel Opus 5 devance Muse Spark 1.2 de 8,8 points | AJOUT |
| Muse Spark 1.1 | TECHNOLOGIE | rôle | Version précédente du modèle, point de comparaison des gains annoncés | AJOUT |
