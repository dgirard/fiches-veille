# lightrag-simple-fast-rag-hkuds-2024-10-08

## Veille
LightRAG - RAG simple et rapide - Knowledge graphs - Dual-level retrieval - EMNLP2025 - GitHub

## Titre Article
HKUDS/LightRAG: [EMNLP2025] "LightRAG: Simple and Fast Retrieval-Augmented Generation"

## Date
2024-10-08

## URL
https://github.com/HKUDS/LightRAG

## Keywords
knowledge-graph, gpt, rag, gpt-4, large-language-models, llm, genai, retrieval-augmented-generation, graphrag, dual-level retrieval, vector storage, Neo4j, PostgreSQL, Faiss, document processing, multimodal RAG, EMNLP2025

## Authors
Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, Chao Huang (HKUDS - Hong Kong University Data Science)

## Pense-betes
- **22k étoiles** GitHub, **3.3k forks**, licence MIT
- Présentation à **EMNLP 2025** (conférence majeure NLP)
- **Dual-level retrieval** : combinaison knowledge graphs + vector databases
- Support **multimodal** via RAG-Anything (texte, images, tableaux, équations)
- **25+ paramètres** de configuration pour customisation fine
- Recommandations LLM : **minimum 32B paramètres**, contexte **32KB+** (64KB idéal)
- **6 modes de requête** : local, global, hybrid, naive, mix, bypass
- Support **multiples storages** : PostgreSQL, Neo4j, Redis, MongoDB, Milvus, Qdrant, Faiss
- Intégration **RAG-Anything** pour traitement documents (PDF, PPT, CSV)
- **Gestion avancée** : suppression par ID document, par nom d'entité
- **Streaming responses** et historique de conversation
- Support **citations** pour attribution des sources
- **Docker Compose** disponible pour déploiement rapide
- Communauté active : Discord, WeChat, documentation complète

## RésuméDe400mots

LightRAG est un système de Retrieval-Augmented Generation (RAG) développé par HKUDS (Hong Kong University Data Science) qui sera présenté à EMNLP 2025, une conférence majeure en traitement du langage naturel. Avec **22k étoiles** GitHub et sous licence MIT, ce projet vise à simplifier et accélérer l'extraction de connaissances et les requêtes intelligentes via une approche innovante combinant knowledge graphs et bases de données vectorielles.

**Architecture Dual-Level Retrieval**

L'innovation centrale de LightRAG réside dans son système de "dual-level retrieval" qui fusionne deux approches complémentaires : les knowledge graphs pour capturer les relations structurelles entre entités, et les bases de données vectorielles pour la recherche sémantique. Cette hybridation offre **six modes de requête** distincts (local, global, hybrid, naive, mix, bypass) permettant d'adapter la stratégie de récupération selon le contexte et les besoins spécifiques.

**Support Multimodal et Formats Multiples**

L'intégration récente avec RAG-Anything élargit considérablement les capacités de traitement documentaire. Le système gère désormais de manière transparente le texte, les images, les tableaux et les équations depuis divers formats (PDF, DOC, PPT, CSV). Cette approche multimodale transforme LightRAG en solution complète pour l'extraction de connaissances depuis des documents d'entreprise hétérogènes.

**Flexibilité des Storages et Scalabilité**

LightRAG supporte une architecture de stockage modulaire à quatre niveaux : KV storage pour le cache LLM et chunks de texte (Json, PostgreSQL, Redis, MongoDB), Vector storage pour embeddings (NanoVectorDB, Milvus, Chroma, Faiss, Qdrant, PostgreSQL, MongoDB), Graph storage pour le graphe entité-relation (NetworkX, Neo4J, PostgreSQL, AGE), et Document status storage pour tracking du traitement. Cette flexibilité permet de choisir le backend optimal selon les exigences de performance et d'infrastructure. Pour production haute performance, Neo4J est recommandé comme base de données graphe.

**Exigences et Recommandations LLM**

Les spécifications recommandées reflètent la sophistication du système : LLM avec **minimum 32 milliards de paramètres** et longueur de contexte de **32KB** (64KB préféré) pour optimiser l'extraction d'entités-relations. Les modèles d'embedding multilingues mainstream comme BAAI/bge-m3 et text-embedding-3-large sont suggérés. Le système supporte OpenAI (GPT-4o, GPT-4o-mini), Ollama pour modèles locaux, et Hugging Face.

**Configuration et Customisation Avancée**

LightRAG expose **plus de 25 paramètres d'initialisation** offrant un contrôle granulaire : taille de chunk (défaut 1200 tokens), boucles d'extraction d'entités (défaut 1), batch size embedding (défaut 32), paramètres de cache LLM, budgets de tokens pour entités, relations et contexte total. Cette configurabilité permet d'ajuster finement le compromis performance/coût.

**Fonctionnalités Avancées et Gestion**

Le système offre des capacités sophistiquées : suppression de documents par ID, suppression d'entités par nom (maintenant cohérence graph/vector), support de citations pour attribution des sources, réponses en streaming, tracking d'historique conversationnel, et insertion de knowledge graphs personnalisés. L'architecture asynchrone (asyncio) garantit performance et scalabilité.

**Déploiement et Communauté**

Installation flexible via PyPI (`pip install "lightrag-hku[api]"`), depuis source ou Docker Compose avec fichiers d'environnement pré-configurés. La communauté active maintient Discord, WeChat, documentation complète, exemples, vidéos tutorielles. Les mises à jour récentes (support PostgreSQL, citations, suppressions, Neo4J) démontrent un développement actif.
