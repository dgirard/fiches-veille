# anthropic-self-service-data-analytics-claude-agentic-stack-2026-06-03

## Veille
REX d'ingénierie de l'équipe **Data Science & Data Engineering d'Anthropic** (Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry) publié le **3 juin 2026** sur le blog Anthropic (catégorie *Enterprise AI*, focus **Claude Code**). **Résultat-phare** : ***« 95 % des requêtes d'analytics métier sont automatisées par Claude, avec ~95 % de précision en agrégat »*** (jusqu'à **~99 %** sur certains domaines). **Problème central** : l'analytics n'est **pas** du code — *« there's often only a single correct answer using a single correct source »* — il faut **mapper une question utilisateur à des entités précises et à jour** du modèle de données. Trois **modes d'échec** : (1) **ambiguïté concept↔entité** (ex. *« active users »* : quelles actions ? exclure les fraudeurs ? quelle fenêtre ?) ; (2) **obsolescence** (assets et connaissance de l'agent deviennent *« subtly wrong »*) ; (3) **échec de retrieval** (*« 80 % des requêtes échouées avaient l'info présente dans le corpus »* mais introuvable). **Solution = « agentic analytics stack » en 4 couches** : (L1) **Data foundations** — dimensional modeling, **canonical datasets** *« single source-of-truth »*, métadonnées *« as a first-class product »*, intégrité par CI/CD ; (L2) **Sources of truth** par ordre de confiance décroissant — **semantic layer** (l'agent est *« structurally required (by skill instruction) to leverage the semantic layer first »*), graphe de lineage, **query corpus** (distillé en docs structurées, **pas** du retrieval brut), business context (knowledge graph : roadmaps, decision logs, org) ; (L3) **Skills** — le levier décisif : ***« without skills … didn't exceed 21 % … Adding skills gets these numbers consistently above 95 % »*** ; structure **par paires** (*Knowledge skill* = routeur vers ~30 fichiers de référence ; *Unbook skill* = workflow de l'analyste senior : clarifier → trouver les sources → exécuter → **revue adversariale**) ; maintenance **colocalisée** (*« a code-review hook flags any reporting-model change that doesn't touch a skill file »* → **~90 % des PR data incluent un changement de skill**) ; (L4) **Validation** — evals offline (seuil ~90 % pour lancer un agent, cible ~100 %), **ablation testing** (résultat négatif notable : grep brut sur des milliers de fichiers SQL → précision bouge *« less than a point »*), online (revue adversariale : **+6 % de précision, +32 % de tokens, +72 % de latence**), **provenance footers** (tier de source + fraîcheur + ownership), **active correction harvesting** (agents planifiés scannant les canaux pour drafter des fixes markdown). **Insight stratégique** : *« documentation generated, definitions owned by humans »* — laisser le LLM **définir** les métriques fut *« net-negative »*. **Démarrage minimal** : quelques canonical datasets + quelques dizaines d'evals + un *thin knowledge skill* captent *« most of the upside »*. Converge fortement avec [[shihipar-claude-code-lessons-building-skills-2026-06-03]] (skills = dossiers, Gotchas, hooks), la doctrine *systems around the model* de [[dropbox-okumura-beyond-code-generation-engineering-productivity-ai-agents-2026-05-28]], le **semantic layer / ontology** de [[talisman-modern-data-101-ontology-pipeline-refresh-2026-05-04]] et [[seale-semantic-agent-model-harness-ontology-data-2026-04-17]], le *context development lifecycle* de [[debois-tessl-context-development-lifecycle-ai-coding-agents-2026-02-19]] et l'UDA/knowledge graph de [[netflix-uda-unified-data-architecture-knowledge-graph-2025-06-12]].

## Titre Article
How Anthropic enables self-service data analytics with Claude

## Date
2026-06-03

## URL
https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude

## Keywords
self-service analytics, data analytics agentique, Claude Code, single correct answer, mapping question entités, modèle de données, modes d'échec, ambiguïté concept-entité, active users, obsolescence des assets, data staleness, échec de retrieval, agentic analytics stack, data foundations, dimensional modeling, canonical datasets, single source of truth, métadonnées first-class product, lineage, semantic layer, structurally required, query corpus, knowledge graph métier, decision logs, skills, knowledge skill, unbook skill, routeur, 30 fichiers de référence, revue adversariale, retention curves, funnel analysis, rate decomposition, Gotchas, colocalisation skill modèle, code-review hook, 90% PR avec skill, validation, evals offline, ground truth snapshot, ablation testing, grep brut résultat négatif, provenance footers, tiers de source, correction harvesting, agents planifiés, definitions owned by humans, documentation generated, 21% sans skills, 95% précision, 99%, 80% info présente, démarrage minimal, gouvernance données, Anthropic Data Science

## Authors
**Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry** — équipe **Data Science & Data Engineering d'Anthropic**. Article publié le **3 juin 2026** sur le blog Anthropic (claude.com/blog), catégorie *Enterprise AI*, ~5 min de lecture.

## Ton
**Profil** : REX d'ingénierie interne (*engineering blog post*), registre **technique-pédagogique et empirique**, niveau élevé (data engineering, semantic layer, evals, ablations), adressé aux **équipes data/analytics et plateforme**. Posture : *« voici ce qui a marché et ce qui n'a pas marché chez nous »*, étayé par des **chiffres** et des **résultats négatifs** assumés.

**Style** : Structuré en **couches** (stack en 4 niveaux) avec un fil conducteur clair (collapse ambiguity → make discoverable → flag staleness). Honnêteté scientifique : mise en avant des **ablations** et **résultats négatifs** (grep brut <1 %, définitions LLM net-negative) qui crédibilisent le propos. Densité de **métriques** précises (21 %, 95 %, 99 %, +6 %/+32 %/+72 %, 80 %, 90 %). Vocabulaire de gouvernance data (canonical, lineage, ownership, tiering).

**Aphorismes-clés** :
- ***« For analytics use cases, there's often only a single correct answer using a single correct source. »***
- ***« Without skills … didn't exceed 21 % … Adding skills gets these numbers consistently above 95 % in aggregate. »***
- ***« Agents are structurally required (by skill instruction) to leverage the semantic layer first. »***
- ***« Treat metadata as a first-class product. »***
- ***« Roughly 90 % of our data-model PRs now include a skill change in the same diff. »***
- (échec silencieux) *« The answer is wrong, but looks plausible and is used without objection. »*

**Métaphores / cadres travaillés** :
- ***Single correct answer*** — l'analytics ≠ le code : on ne valorise pas la créativité du modèle mais l'**exactitude déterministe** ; l'infra prime sur le génératif.
- ***Agentic analytics stack (4 couches)*** — foundations → sources of truth → skills → validation.
- ***Skills par paires*** — *Knowledge* (routeur/recherche) + *Unbook* (workflow analyste senior).
- ***Documentation generated, definitions owned by humans*** — le LLM rédige, l'humain **tranche** les définitions.
- ***Provenance footers*** — traçabilité de la réponse (tier de source / fraîcheur / ownership) comme garde-fou anti-obsolescence.
- ***Le goulot est la structure, pas l'accès*** — l'ablation grep brut prouve que donner plus d'accès ≠ plus de précision.

**Position épistémique** : REX **empirique et mesuré**, avec evals reproductibles et ablations — l'un des billets Anthropic les plus rigoureux sur l'**ingénierie de contexte** appliquée à la donnée. À lire comme **blueprint d'architecture** d'agents analytics de production, transposable hors Anthropic.

**Autorité** : (a) **producteur du modèle** (Anthropic) appliquant Claude à son propre back-office data ; (b) **chiffres et ablations** (résultats négatifs inclus) ; (c) **architecture en couches** directement actionnable ; (d) cohérence avec la doctrine *skills / systems around the model* du reste de l'écosystème.

## Pense-betes

- **Date / source** : **3 juin 2026**, blog Anthropic (*claude.com/blog*, Enterprise AI). Auteurs : équipe **Data Science & Data Engineering d'Anthropic** (Chang, Peng, Leder, Jiao, Cherry).
- **Résultat-phare** : **95 % des requêtes analytics métier automatisées**, **~95 % de précision** agrégée (jusqu'à **~99 %** sur certains domaines).
- **Thèse** : l'analytics ≠ le code — *« only a single correct answer using a single correct source »* → l'enjeu est de **mapper la question aux bonnes entités à jour**, pas de générer.

### 3 modes d'échec

1. **Ambiguïté concept↔entité** — des centaines d'options ; ex. *« active users »* (quelles actions ? exclure fraudeurs ? quelle lookback window ?).
2. **Obsolescence (staleness)** — assets et connaissance de l'agent deviennent *« subtly wrong »* (schémas/définitions changent en continu).
3. **Échec de retrieval** — **80 %** des requêtes échouées avaient pourtant l'info **présente** dans le corpus.
- Danger ultime = **échec silencieux** : *« the answer is wrong, but looks plausible and is used without objection »*.

### Stack agentique en 4 couches

- **L1 — Data foundations** : dimensional modeling, **canonical datasets** (single source-of-truth, owned, consumption-ready), métadonnées *« first-class product »*, intégrité cross-layer via CI/CD.
- **L2 — Sources of truth** (confiance ↓) : **semantic layer** (obligatoire en premier) → **lineage/transformation graph** → **query corpus** (distillé en docs, pas du retrieval brut) → **business context** (knowledge graph : roadmaps, decision logs, org).
- **L3 — Skills** (le levier) : **21 % → 95 %+**. Paires : **Knowledge skill** (routeur → ~**30** fichiers de référence) + **Unbook skill** (workflow analyste senior : clarifier → sources → exécuter → **revue adversariale** ; patterns réutilisables : retention curves, rate decomposition, funnel). Squelette de doc type : Quick reference / Dimensions & key tables / **Gotchas** / Best practices & query patterns / Cross-domain refs.
- **L4 — Validation** : evals offline (seuil **~90 %** pour autoriser un agent, cible ~100 %, ground truth figé sur snapshot, *« store results like telemetry »*), **ablation testing**, online (revue adversariale, provenance footers, data quality checks, **correction harvesting** par agents planifiés).

### Résultats notables (chiffres & ablations)

- **Sans skills ≤ 21 %** ; **avec skills > 95 %** (≈99 % sur certains domaines).
- **Revue adversariale** : **+6 %** précision, mais **+32 %** tokens et **+72 %** latence (arbitrage à assumer).
- **Ablation grep brut** (milliers de fichiers SQL accessibles) : précision bouge ***« less than a point »*** → **le goulot est la structure, pas l'accès**.
- **Définitions générées par LLM** = *« net-negative »* (encodent les ambiguïtés qu'on voulait éliminer) → **definitions owned by humans**.
- **Retrieval non structuré** sur des milliers de requêtes : gain **< 1 point** → corpus à **distiller**, pas à retrouver brut.
- **Maintenance** : hook de code-review → **~90 % des PR data** touchent un fichier skill dans le même diff.

### À mobiliser en mission / présentation

- **Blueprint d'agent analytics de production** transposable : gouvernance data + semantic layer **obligatoire** + skills + evals à seuil.
- **Démarrage minimal** (à reprendre tel quel) : *« a handful of canonical datasets, a few dozen offline evals, and a thin knowledge skill »* captent *« most of the upside »*.
- **Arguments anti-RAG-naïf** : les deux résultats négatifs (grep brut, retrieval non structuré) = munitions contre le *« il suffit de tout donner à l'agent »*.
- **Métrique de gouvernance vivante** : *« 90 % des PR incluent un skill »* = preuve que doc et code évoluent ensemble (anti-staleness).
- Articule : skills (Shihipar/Anthropic), semantic layer/ontology (Talisman, Seale), context engineering (Debois/Tessl), *systems around the model* (Dropbox), knowledge graph data (Netflix UDA).

## RésuméDe400mots

Publié le **3 juin 2026** sur le blog Anthropic, ce REX de l'équipe **Data Science & Data Engineering** (Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry) raconte comment Anthropic a rendu son analytics **self-service** grâce à Claude : **95 % des requêtes métier automatisées**, **~95 % de précision** en agrégat (jusqu'à ~99 % sur certains domaines).

Le point de départ est que l'analytics n'est **pas** du code : *« there's often only a single correct answer using a single correct source »*. L'enjeu n'est pas la créativité générative mais la capacité à **mapper une question à des entités précises et à jour** du modèle de données. Trois modes d'échec menacent : l'**ambiguïté concept↔entité** (que sont les *« active users »* ? exclut-on les fraudeurs ? quelle fenêtre ?), l'**obsolescence** des assets et de la connaissance de l'agent, et l'**échec de retrieval** — **80 %** des requêtes échouées avaient pourtant l'information présente dans le corpus. Le pire étant l'**échec silencieux** : une réponse fausse, plausible, utilisée sans objection.

La réponse est un *« agentic analytics stack »* en **quatre couches**. (1) **Data foundations** : dimensional modeling, **canonical datasets** *« single source-of-truth »*, métadonnées traitées *« as a first-class product »*, intégrité par CI/CD. (2) **Sources of truth** par confiance décroissante : un **semantic layer** que l'agent est *« structurally required (by skill instruction) to leverage first »*, puis le **lineage**, un **query corpus** distillé en documents (pas du retrieval brut), et un **knowledge graph métier** (roadmaps, decision logs, org). (3) **Skills** — le levier décisif : *« without skills … didn't exceed 21 % … Adding skills gets these numbers consistently above 95 % »*. Ils s'organisent **par paires** : un *Knowledge skill* routeur (~30 fichiers de référence) et un *Unbook skill* encodant le workflow de l'analyste senior (clarifier, trouver les sources, exécuter, **revue adversariale**). La maintenance est **colocalisée** : un hook de revue signale tout changement de modèle sans modification de skill — **~90 % des PR data** incluent désormais un skill dans le même diff. (4) **Validation** : evals offline à seuil (~90 % pour autoriser un agent), **ablation testing** et garde-fous online (revue adversariale **+6 %** de précision mais **+32 %** de tokens et **+72 %** de latence ; *provenance footers* ; **correction harvesting** par agents planifiés).

Deux résultats négatifs structurent la doctrine : donner un **grep brut** sur des milliers de fichiers SQL ne bouge la précision *« less than a point »* (le goulot est la **structure**, pas l'accès), et laisser le LLM **définir** les métriques fut *« net-negative »* — d'où la règle : *documentation generated, definitions owned by humans*. Pour démarrer : quelques canonical datasets, quelques dizaines d'evals, un *thin knowledge skill*.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| équipe Data Science Anthropic | ORGANISATION | a_publié | How Anthropic enables self-service data analytics with Claude | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | automatise | 95% de ses requêtes analytics métier via Claude | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| analytics agentique | CONCEPT | exige | une seule bonne réponse depuis une seule bonne source | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| skills | METHODOLOGIE | augmente | la précision de 21% à plus de 95% | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| agent analytics | TECHNOLOGIE | doit_utiliser | le semantic layer en premier (par instruction de skill) | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| query corpus | CONCEPT | doit_être | distillé en docs structurées, pas retrouvé brut | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| retrieval non structuré | METHODOLOGIE | améliore | la précision de moins d'un point | CONCEPT | 0.9 | STATIQUE | déclaré_article |
| accès grep brut au SQL | METHODOLOGIE | ne_change_pas | la précision (goulot = structure, pas accès) | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| revue adversariale | METHODOLOGIE | améliore | la précision de 6% (mais +32% tokens, +72% latence) | CONCEPT | 0.9 | STATIQUE | déclaré_article |
| définitions de métriques générées par LLM | CONCEPT | sont | net-negative sur les evals | CONCEPT | 0.88 | STATIQUE | déclaré_article |
| définitions de métriques | CONCEPT | doivent_être | détenues par des humains | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| hook de code-review | TECHNOLOGIE | impose | qu'un changement de modèle touche un fichier skill | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| 90% des PR data | CONCEPT | incluent | un changement de skill dans le même diff | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| échec silencieux | CONCEPT | produit | une réponse fausse, plausible, utilisée sans objection | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| domain owner | PERSONNE | ne_peut_lancer_agent_que_si | seuil d'eval (~90%) atteint | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| How Anthropic enables self-service data analytics with Claude | DOCUMENT | catégorie | REX ingénierie data (Enterprise AI, blog Anthropic) | AJOUT |
| équipe Data Science & Data Engineering Anthropic | ORGANISATION | membres | Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry | AJOUT |
| agentic analytics stack | METHODOLOGIE | définition | 4 couches : foundations / sources of truth / skills / validation | AJOUT |
| canonical datasets | CONCEPT | définition | Datasets single source-of-truth, owned, consumption-ready, discoverable | AJOUT |
| semantic layer | TECHNOLOGIE | rôle | Définitions compilées de métriques/dimensions, source de confiance n°1 | AJOUT |
| Knowledge skill | METHODOLOGIE | rôle | Routeur top-level réduisant la recherche à ~30 fichiers de référence | AJOUT |
| Unbook skill | METHODOLOGIE | rôle | Workflow analyste senior (clarifier/sources/exécuter/revue adversariale) + patterns | AJOUT |
| skills (analytics) | METHODOLOGIE | impact | Précision 21% → 95%+ (≈99% sur certains domaines) | AJOUT |
| ablation testing | METHODOLOGIE | rôle | Varier un composant, eval fixe — révèle les vrais leviers | AJOUT |
| provenance footers | CONCEPT | définition | Traçabilité réponse : tier de source + fraîcheur + ownership | AJOUT |
| correction harvesting | METHODOLOGIE | définition | Agents planifiés scannant les canaux pour drafter des fixes markdown | AJOUT |
| evals offline | METHODOLOGIE | seuil | ~90% requis pour autoriser un agent, cible ~100%, ground truth figé | AJOUT |
| modes d'échec analytics | CONCEPT | liste | Ambiguïté concept-entité, obsolescence, échec de retrieval | AJOUT |
