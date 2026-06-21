# comparethemarket-context-retrieval-ai-code-review-gkg-rag-2026-03-06

## Veille
Étude empirique de l'équipe engineering **Compare the Market** (Meerkat Careers, UK) qui évalue quatre approches de **récupération de contexte pour la revue de code par IA** : Baseline (pas de contexte additionnel), **RAG** (recherche vectorielle), **GKG** (GitLab Knowledge Graph, graphe de connaissances AST) et **GKG+RAG** (hybride). Évaluation sur **79 merge requests** réelles avec **MLflow sur Databricks**. Résultat-choc : **RAG performe pire que le baseline** sur presque toutes les métriques — le bruit vectoriel est contre-productif pour la revue de code. **GKG surpasse RAG de +21 %** en couverture des commentaires inline (0,696 vs 0,577) grâce à la compréhension structurelle AST (Tree-sitter + base de graphe Kuzu). Le code exige une compréhension **structurelle** (appelants, signatures, hiérarchies), pas une simple similarité sémantique. GKG coûte 4× le baseline mais délivre des améliorations mesurables ; RAG coûte 3× sans amélioration. Implémentation en **sidecar Docker** CI/CD wrappant le binaire GKG (encore en bêta GitLab) avec serveur MCP local.

## Titre Article
Comparing Context Retrieval Approaches for AI Code Review

## Date
2026-03-06

## URL
https://comparethemarketcareers.com/blog/comparing-context-retrieval-approaches-for-ai-code-review/

## Keywords
Compare the Market, Meerkat Careers, revue de code IA, context retrieval, RAG, GKG, GitLab Knowledge Graph, AST, Tree-sitter, Kuzu, graphe de connaissances code, MLflow, Databricks, merge requests, évaluation empirique, inline comments coverage, similarité sémantique vs structurelle, sidecar Docker CI/CD, MCP serveur local, bruit vectoriel contre-productif, code review automatisée, cost-efficiency revue IA, RAG pire que baseline, approche structurelle code

## Authors
Équipe Engineering Compare the Market (Meerkat Careers, UK — site de comparaison d'assurances et services financiers).

## Ton
**Profil** : Article technique publié sur le blog carrières de Compare the Market (marque Meerkat Careers, UK), entreprise de comparaison de prix grand public. Format d'ingénierie interne partagé publiquement — le ton est celui d'une équipe qui a mené une évaluation rigoureuse et en partage les résultats sans fioritures. Public cible : ingénieurs logiciels, DevOps, équipes qualité logicielle cherchant à outiller leur revue de code avec de l'IA, architectes évaluant RAG vs approches structurelles pour du code.

**Style** : Registre technique empirique, données-first. L'article procède méthodiquement : hypothèse → setup expérimental (4 approches, 79 MR, MLflow/Databricks) → métriques → résultats → analyse des causes → recommandations. Pas de hype, pas de promesses marketing : les résultats négatifs du RAG sont présentés frontalement, sans chercher à les adoucir. Le style est celui d'un rapport d'ingénierie interne rendu public — factuel, structuré, avec tableaux de métriques. L'autorité vient des données, pas de la rhétorique.

**Position épistémique** : empiriquement honnête. L'article ne cherche pas à vendre GKG comme solution miracle — il reconnaît le surcoût 4× et le caractère bêta de GKG. Le résultat négatif sur RAG est le finding le plus saillant : démontrer qu'une approche populaire est contre-productive dans un cas d'usage précis est plus utile que de promouvoir l'alternative. L'architecture sidecar Docker est décrite comme un contournement pragmatique (GKG pas encore intégré nativement dans GitLab CI/CD).

## Pense-betes
- **Date / source** : 6 mars 2026, blog Meerkat Careers (Compare the Market, UK). Auteur : équipe engineering (nom(s) individuel(s) non disponibles — site bloqué 403, fiche basée sur le contenu indexé par les moteurs de recherche et sources secondaires).
- **Problème adressé** : quelle est la meilleure façon de fournir du contexte codebase à un reviewer IA ? La similarité sémantique (RAG) suffit-elle, ou faut-il une compréhension structurelle du code (AST/graphe) ?
- **4 approches évaluées** :
  1. **Baseline** — pas de contexte additionnel, le modèle IA ne voit que le diff de la MR.
  2. **RAG** (Retrieval-Augmented Generation) — chunking du code, embeddings, recherche vectorielle pour récupérer des snippets sémantiquement similaires.
  3. **GKG** (GitLab Knowledge Graph) — parsing AST via **Tree-sitter** (`gitlab-code-parser`), graphe de connaissances structuré stocké dans **Kuzu** (base de graphe), requêtes structurelles (appelants, hiérarchie de classes, signatures de fonctions).
  4. **GKG+RAG** (hybride) — combinaison des deux approches.
- **Métriques clés sur 79 merge requests** (évaluation via **MLflow sur Databricks**) :
  | Métrique | GKG | RAG | Écart |
  |----------|-----|-----|-------|
  | Inline Comments Coverage | **0,696** | 0,577 | **+21 %** |
  | Summary Coverage | **0,681** | 0,664 | +3 % |
  | Issue Coverage | **0,929** | 0,926 | marginal |
  | Score Accuracy | **GKG meilleur** | RAG pire que baseline | — |
- **Finding principal : RAG performe pire que le baseline** sur presque toutes les métriques. Ajouter du contexte bruité est contre-productif.
- **4 causes identifiées de l'échec de RAG pour la revue de code** :
  1. **Bruit** — la similarité vectorielle récupère du code qui « ressemble » mais n'est pas pertinent.
  2. **Faux positifs** — RAG trouve des fonctions non reliées au changement.
  3. **Limitation per-file** — RAG n'a aucune compréhension des relations inter-fichiers.
  4. **Effet de distraction** — le contexte additionnel peut induire le modèle en erreur plutôt que l'aider.
- **Pourquoi GKG fonctionne** : la revue de code exige une compréhension **structurelle** — quand on revoit un changement dans une fonction, il faut savoir **qui l'appelle**, **ce qu'elle appelle**, et **comment elle s'inscrit dans l'architecture**. GKG identifie précisément les appelants, comprend les signatures, trace les relations de code. C'est de la **navigation structurelle**, pas de la **similarité sémantique**.
- **Implémentation technique** : GKG encore en bêta, pas encore disponible comme feature native GitLab CI/CD → l'équipe a construit un **sidecar Docker** : conteneur léger wrappant le binaire GKG officiel, monté en parallèle du reviewer dans le pipeline CI. À chaque pipeline de MR : (1) le sidecar monte le source du projet, (2) indexe le codebase complet et construit le graphe de connaissances from scratch, (3) démarre le **serveur MCP GKG** sur un port local, (4) expose un jeu de tool calls auxquels le reviewer IA se connecte.
- **Analyse coût-bénéfice** :
  - GKG : **4× le coût baseline** → améliorations mesurables et justifiées.
  - RAG : **3× le coût baseline** → résultats pires que ne rien ajouter.
  - GKG+RAG : coût cumulé sans bénéfice additionnel vs GKG seul.
  - **Conclusion** : si la qualité est primordiale, utiliser GKG. Éviter RAG et GKG+RAG.
- **Articulation dossier veille** :
  - **Convergence forte** avec la doctrine *« grep wins when you know what you're looking for, AST wins when you need structural relationships »* — tendance 2026 confirmée par les pratiques de Cursor, Claude Code, Devin (cf. MindStudio *"Coding Agents Skipped RAG"*).
  - Rejoint **Zhutov/QMD** (2026-03-01) sur la supériorité de la recherche structurée vs vectorielle pour le code.
  - Prolonge **Trivedy/LangChain** (2026-03-10) *Anatomy of an Agent Harness* : le harnais (ici sidecar GKG + MCP) est plus important que le modèle.
  - Rejoint **Dropbox/Okumura** (2026-05-28) *"the value comes less from the model itself than the systems surrounding it"* — le contexte structurel fait la différence, pas le LLM.
  - Complète le dossier **MCP** : GKG exposé via serveur MCP local, confirmant le pattern sidecar MCP en CI/CD.
  - Corrobore **Anthropic Data Science** (2026-06-03) : *"grep brut sur des milliers de SQL → précision ne bouge que d'un point"* — le goulot est la structure, pas l'accès.
  - Renforce la thèse anti-RAG-naïf de **Seale** (2025-05-30) *Philosophy Eats AI* : l'ontologie (ici l'AST) prime sur la similarité.
- **À mobiliser pour** : choix d'architecture de revue de code IA en entreprise ; argumentaire contre le RAG-par-défaut pour le code ; design de pipelines CI/CD augmentés par agents ; évaluation d'outils de contexte code (GKG, CodeGraphContext, code-review-graph).
- **Limites** : (a) 79 MR = échantillon modeste ; (b) un seul codebase (Compare the Market) — biais de représentativité ; (c) GKG encore en bêta, pas encore validé à grande échelle ; (d) auteur(s) non identifié(s) — site bloqué 403 ; (e) pas de comparaison avec d'autres approches structurelles (Augment Context Engine, CodeGraphContext, etc.).
- **LinkedIn shortlink** : le lien `lnkd.in/dacPc6fM` (en attente depuis 2026-05-15) pointe vers cet article.

## RésuméDe400mots

L'équipe engineering de **Compare the Market** (Meerkat Careers, UK) publie le 6 mars 2026 une évaluation empirique de quatre approches de récupération de contexte pour la **revue de code par IA** : Baseline (aucun contexte additionnel), **RAG** (recherche vectorielle par embeddings), **GKG** (GitLab Knowledge Graph, graphe de connaissances basé sur l'AST via Tree-sitter et la base de graphe Kuzu), et un hybride **GKG+RAG**. L'évaluation porte sur **79 merge requests** réelles, mesurées via **MLflow sur Databricks**.

Le résultat principal est contre-intuitif : **RAG performe pire que le baseline** sur presque toutes les métriques, y compris la couverture des commentaires inline, la couverture du résumé et la précision du score. Ajouter du contexte récupéré par similarité vectorielle est non seulement inutile mais **contre-productif** pour la revue de code. Quatre causes sont identifiées : le **bruit** (la similarité vectorielle récupère du code « qui ressemble » sans être pertinent), les **faux positifs**, l'absence de compréhension des **relations inter-fichiers**, et un **effet de distraction** qui induit le modèle en erreur.

À l'inverse, **GKG surpasse RAG de +21 %** en couverture des commentaires inline (0,696 vs 0,577). La raison est structurelle : la revue de code exige de savoir **qui appelle une fonction**, ce qu'elle appelle, et comment elle s'inscrit dans l'architecture — des informations que l'AST et le graphe de connaissances capturent nativement, mais que la similarité sémantique ne peut fournir. GKG identifie précisément les appelants, comprend les signatures de fonctions, et trace les relations de code.

L'implémentation est pragmatique : GKG étant encore en bêta et pas encore intégré nativement dans GitLab CI/CD, l'équipe a construit un **conteneur Docker sidecar** qui wrappe le binaire GKG, indexe le codebase à chaque pipeline de MR, et expose les outils via un **serveur MCP local**. Le coût est 4× le baseline, mais les améliorations sont mesurables et justifiées. RAG coûte 3× le baseline pour des résultats pires.

Cette étude confirme une tendance lourde de 2026 : pour le code, les approches **structurelles** (AST, graphes de connaissances, grep ciblé) surpassent les approches **vectorielles** (RAG sémantique). Le code n'est pas du texte — sa valeur informationnelle réside dans ses **relations structurelles**, pas dans sa similarité lexicale. Convergence forte avec Zhutov/QMD, Dropbox/Okumura (*"the value comes from the systems surrounding the model"*), et la doctrine Anthropic Data Science (*"le goulot est la structure, pas l'accès"*). À mobiliser comme référence empirique pour le choix d'architecture de revue de code IA et comme contre-argument au RAG-par-défaut dans le domaine du code.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Compare the Market | ORGANISATION | a_créé | évaluation empirique revue de code IA | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| GKG | TECHNOLOGIE | surpasse | RAG | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| GKG | TECHNOLOGIE | mesure | 0,696 inline comments coverage vs RAG 0,577 (+21 %) | MESURE | 0.96 | STATIQUE | déclaré_article |
| RAG | TECHNOLOGIE | mesure | performance pire que baseline sur presque toutes les métriques | MESURE | 0.96 | STATIQUE | déclaré_article |
| GKG | TECHNOLOGIE | utilise | Tree-sitter | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| GKG | TECHNOLOGIE | utilise | Kuzu | TECHNOLOGIE | 0.94 | ATEMPOREL | déclaré_article |
| GKG | TECHNOLOGIE | est_instance_de | GitLab Knowledge Graph | TECHNOLOGIE | 0.97 | ATEMPOREL | déclaré_article |
| Compare the Market | ORGANISATION | affirme_que | le code exige une compréhension structurelle, pas une similarité sémantique | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| RAG | TECHNOLOGIE | réduit | qualité de la revue de code IA (bruit vectoriel contre-productif) | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| GKG | TECHNOLOGIE | permet | identification précise des appelants, signatures, hiérarchies de code | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| évaluation empirique revue de code IA | EVENEMENT | utilise | MLflow sur Databricks | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| évaluation empirique revue de code IA | EVENEMENT | mesure | 79 merge requests évaluées | MESURE | 0.95 | STATIQUE | déclaré_article |
| Compare the Market | ORGANISATION | a_créé | sidecar Docker CI/CD pour GKG | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| sidecar Docker CI/CD pour GKG | TECHNOLOGIE | utilise | serveur MCP local | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| GKG | TECHNOLOGIE | mesure | coût 4× baseline avec améliorations mesurables | MESURE | 0.93 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Compare the Market | ORGANISATION | secteur | Comparaison de prix / assurances (UK), marque Meerkat Careers | AJOUT |
| GKG | TECHNOLOGIE | définition | GitLab Knowledge Graph — parsing AST via Tree-sitter, graphe de connaissances code dans Kuzu, requêtes structurelles (appelants, hiérarchies, signatures) | AJOUT |
| RAG | TECHNOLOGIE | catégorie | Retrieval-Augmented Generation — chunking code + embeddings + recherche vectorielle par similarité sémantique | MISE_A_JOUR |
| Tree-sitter | TECHNOLOGIE | rôle | Parser AST incrémental utilisé par GKG pour construire le graphe de connaissances code | AJOUT |
| Kuzu | TECHNOLOGIE | catégorie | Base de données de graphe embarquée, stockage du graphe de connaissances GKG | AJOUT |
| MLflow | TECHNOLOGIE | rôle | Plateforme d'évaluation utilisée sur Databricks pour l'évaluation des 4 approches | AJOUT |
| Sidecar Docker GKG | TECHNOLOGIE | description | Conteneur léger wrappant le binaire GKG, monté en parallèle du reviewer IA dans le pipeline CI/CD, expose un serveur MCP local | AJOUT |
