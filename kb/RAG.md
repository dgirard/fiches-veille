# RAG

> **Type** : TECHNOLOGIE | 9 relations | 3 fiches sources

## Attributs

- **catégorie** : Retrieval-Augmented Generation — chunking code + embeddings + recherche vectorielle par similarité sémantique
- **statut** : Technologie en déclin structurel

## Relations (comme sujet)

### mesure

- « performance pire que baseline sur presque toutes les métriques » (MESURE) — 0.96, STATIQUE
  - [[fiches/2026-03/comparethemarket-context-retrieval-ai-code-review-gkg-rag-2026-03-06\|Étude empirique de l'équipe engineering **Compare the Market** (Meerkat Careers, UK) qui évalue quatre approches de **récupération de contexte pour la revue de code par IA** : Baseline (pas de contexte additionnel), **RAG** (recherche vectorielle), **GKG** (GitLab Knowledge Graph, graphe de connaissances AST) et **GKG+RAG** (hybride). Évaluation sur **79 merge requests** réelles avec **MLflow sur Databricks**. Résultat-choc : **RAG performe pire que le baseline** sur presque toutes les métriques — le bruit vectoriel est contre-productif pour la revue de code. **GKG surpasse RAG de +21 %** en couverture des commentaires inline (0,696 vs 0,577) grâce à la compréhension structurelle AST (Tree-sitter + base de graphe Kuzu). Le code exige une compréhension **structurelle** (appelants, signatures, hiérarchies), pas une simple similarité sémantique. GKG coûte 4× le baseline mais délivre des améliorations mesurables ; RAG coûte 3× sans amélioration. Implémentation en **sidecar Docker** CI/CD wrappant le binaire GKG (encore en bêta GitLab) avec serveur MCP local.]]

### réduit

- « qualité de la revue de code IA (bruit vectoriel contre-productif) » (AFFIRMATION) — 0.94, ATEMPOREL
  - [[fiches/2026-03/comparethemarket-context-retrieval-ai-code-review-gkg-rag-2026-03-06\|Étude empirique de l'équipe engineering **Compare the Market** (Meerkat Careers, UK) qui évalue quatre approches de **récupération de contexte pour la revue de code par IA** : Baseline (pas de contexte additionnel), **RAG** (recherche vectorielle), **GKG** (GitLab Knowledge Graph, graphe de connaissances AST) et **GKG+RAG** (hybride). Évaluation sur **79 merge requests** réelles avec **MLflow sur Databricks**. Résultat-choc : **RAG performe pire que le baseline** sur presque toutes les métriques — le bruit vectoriel est contre-productif pour la revue de code. **GKG surpasse RAG de +21 %** en couverture des commentaires inline (0,696 vs 0,577) grâce à la compréhension structurelle AST (Tree-sitter + base de graphe Kuzu). Le code exige une compréhension **structurelle** (appelants, signatures, hiérarchies), pas une simple similarité sémantique. GKG coûte 4× le baseline mais délivre des améliorations mesurables ; RAG coûte 3× sans amélioration. Implémentation en **sidecar Docker** CI/CD wrappant le binaire GKG (encore en bêta GitLab) avec serveur MCP local.]]

### résout

- [[kb/_entites-mineures#fenêtres-de-contexte-limitées\|fenêtres de contexte limitées]] (CONCEPT) — 0.95, ATEMPOREL
  - [[fiches/2025-10/rag-decline-context-windows-2025-10-08\|Déclin du RAG - Expansion des fenêtres de contexte IA - LinkedIn]]

### utilise

- [[kb/_entites-mineures#vector-databases\|vector databases]] (TECHNOLOGIE) — 0.93, ATEMPOREL
  - [[fiches/2025-11/monigatti-rag-to-agent-memory-evolution-2025-11-03\|Evolution RAG vers Agent Memory - Read-write operations - Gestion données inference - Vector databases - Mémoire persistante agents IA - Leonie Monigatti]]

## Relations (comme objet)

- [[kb/_entites-mineures#Agentic-RAG\|Agentic RAG]] **est_basé_sur** → RAG — 0.97
- [[kb/GKG\|GKG]] **surpasse** → RAG — 0.97
- [[kb/_entites-mineures#cascade-d'échecs-en-cinq-étapes\|cascade d'échecs en cinq étapes]] **observé_dans** → RAG — 0.93
- [[kb/IA-agentique\|IA agentique]] **remplace** → RAG — 0.90
- [[kb/Claude-Code\|Claude Code]] **remplace** → RAG — 0.88

## Fiches sources

- [[fiches/2026-03/comparethemarket-context-retrieval-ai-code-review-gkg-rag-2026-03-06\|Étude empirique de l'équipe engineering **Compare the Market** (Meerkat Careers, UK) qui évalue quatre approches de **récupération de contexte pour la revue de code par IA** : Baseline (pas de contexte additionnel), **RAG** (recherche vectorielle), **GKG** (GitLab Knowledge Graph, graphe de connaissances AST) et **GKG+RAG** (hybride). Évaluation sur **79 merge requests** réelles avec **MLflow sur Databricks**. Résultat-choc : **RAG performe pire que le baseline** sur presque toutes les métriques — le bruit vectoriel est contre-productif pour la revue de code. **GKG surpasse RAG de +21 %** en couverture des commentaires inline (0,696 vs 0,577) grâce à la compréhension structurelle AST (Tree-sitter + base de graphe Kuzu). Le code exige une compréhension **structurelle** (appelants, signatures, hiérarchies), pas une simple similarité sémantique. GKG coûte 4× le baseline mais délivre des améliorations mesurables ; RAG coûte 3× sans amélioration. Implémentation en **sidecar Docker** CI/CD wrappant le binaire GKG (encore en bêta GitLab) avec serveur MCP local.]]
- [[fiches/2025-11/monigatti-rag-to-agent-memory-evolution-2025-11-03\|Evolution RAG vers Agent Memory - Read-write operations - Gestion données inference - Vector databases - Mémoire persistante agents IA - Leonie Monigatti]]
- [[fiches/2025-10/rag-decline-context-windows-2025-10-08\|Déclin du RAG - Expansion des fenêtres de contexte IA - LinkedIn]]
