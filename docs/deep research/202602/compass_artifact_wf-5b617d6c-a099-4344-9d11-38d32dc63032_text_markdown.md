# Building a local on-device knowledge graph for conversational AI in Flutter

**A personal knowledge graph that lives entirely on the phone, grows from every conversation, and makes each future interaction smarter — this is achievable today with Flutter/Dart.** The core architecture combines SQLite-based persistent graph storage with in-memory graph querying, LLM-driven entity extraction via structured outputs, and Personalized PageRank retrieval for injecting graph context into prompts. The Kin app (mykin.ai) has already proven this pattern viable on mobile using libSQL with vector extensions. This report synthesizes findings from 100+ sources across eight languages to deliver a complete end-to-end blueprint — from data model to extraction pipeline to retrieval strategy — with specific Flutter packages, code patterns, and implementation guidance.

---

## Pillar 1: Architecture and storage for an on-device knowledge graph

### Why property graphs beat RDF for conversational knowledge

The first architectural decision — data model — is decisive. **Property graphs are strongly recommended over RDF** for on-device conversational knowledge. Property graphs treat relationships as first-class objects that carry their own attributes (confidence scores, timestamps, source conversation IDs), which is essential for conversational knowledge like `(User)-[LIKES {confidence: 0.85, learned_at: "2025-01-15"}]->(Italian_Food)`. RDF's triple model requires verbose reification to attach metadata to edges. Property graphs are also schema-optional, meaning new entity types and relationship types emerge organically from conversations without upfront ontology engineering. RDF's advantages — formal reasoning, W3C interoperability, SPARQL — add complexity without proportional benefit for a private, single-device knowledge store.

The recommended schema draws from Zep's Graphiti architecture (arXiv:2501.13956), which introduced a **bi-temporal model** that represents the state of the art for conversational temporal knowledge graphs. Every relationship tracks two time dimensions: *event time* (when the fact was true in the real world) and *ingestion time* (when the system learned it). This enables historical queries and graceful handling of facts that change. The schema consists of three core tables:

```sql
-- Entities (nodes)
CREATE TABLE entities (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  type TEXT NOT NULL,         -- Person, Organization, Concept, Event...
  aliases TEXT,               -- JSON array of alternative names
  summary TEXT,
  embedding BLOB,             -- vector for semantic search
  created_at INTEGER,
  updated_at INTEGER,
  access_count INTEGER DEFAULT 0,
  importance REAL DEFAULT 0.5
);

-- Relationships (edges with temporal metadata)
CREATE TABLE relationships (
  id TEXT PRIMARY KEY,
  from_id TEXT REFERENCES entities(id),
  to_id TEXT REFERENCES entities(id),
  type TEXT NOT NULL,          -- works_at, knows, prefers, etc.
  fact_text TEXT,              -- natural language form of the triple
  confidence REAL DEFAULT 1.0,
  valid_from INTEGER,          -- event time: when fact became true
  valid_until INTEGER,         -- event time: when fact stopped being true
  t_observed INTEGER,          -- ingestion time: when system learned this
  source_episode_id TEXT,
  is_current BOOLEAN DEFAULT TRUE,
  embedding BLOB
);

-- Episodes (raw conversational ground truth)
CREATE TABLE episodes (
  id TEXT PRIMARY KEY,
  conversation_id TEXT,
  content TEXT,
  timestamp INTEGER,
  speaker TEXT                 -- user or assistant
);
```

This three-table structure mirrors Graphiti's three-tier subgraph hierarchy: an **episode subgraph** preserving raw conversation data as non-lossy ground truth, a **semantic entity subgraph** of extracted entities and relationships with embeddings, and a **community subgraph** of clustered entity groups for high-level summaries. The episode layer is critical — it allows tracing any extracted fact back to its source conversation, and reprocessing episodes if extraction improves.

### The Flutter storage landscape: what actually works

After evaluating every relevant Dart package and embedded database, two practical architectures emerge for Flutter. The choice depends on how much infrastructure complexity is acceptable.

**Architecture A (Recommended for MVP): SQLite via Drift + graph_kit in memory.** This is the pragmatic path. Use Drift (the actively maintained, type-safe SQLite wrapper for Dart) for durable graph persistence with the adjacency-list schema above. SQLite's recursive CTEs enable graph traversal to arbitrary depth — finding all entities within 3 hops of a seed node takes under 100ms on 10K+ nodes with proper indexing. Load working subgraphs into memory as `graph_kit` objects (a Dart package providing typed directed multigraphs with Cypher-inspired pattern queries, JSON serialization, and graph algorithms). The `graph_kit` package supports typed nodes, typed edges with properties, variable-length path queries, shortest path computation, and connected component detection — essentially an in-memory property graph database. For visualization, `graphview` provides force-directed, hierarchical, and tree layouts with animation support.

Key indexes that make SQLite graph queries fast:
```sql
CREATE INDEX idx_edges_source_type ON relationships(from_id, type);
CREATE INDEX idx_edges_target_type ON relationships(to_id, type);
CREATE INDEX idx_entities_type ON entities(type);
CREATE VIRTUAL TABLE entities_fts USING fts5(name, summary);
```

**Architecture B (Production-grade): CozoDB via Rust FFI.** CozoDB is a Rust-based embedded database that combines relational, graph, and vector capabilities in one engine. It runs natively on iOS, Android, and WASM with swappable storage backends (SQLite for mobile). Its Datalog query language is more expressive than SQL recursive CTEs for graph recursion, and it includes built-in HNSW vector indexes, time-travel queries, PageRank, and community detection — all features that would otherwise require separate libraries. The **~50MB memory footprint** and **100K+ QPS for OLTP** workloads fit mobile constraints. Integration with Flutter requires building Rust FFI bindings exposed through `dart:ffi`, which adds upfront complexity but delivers a unified graph-vector-temporal engine. CozoDB is MIT-licensed and actively maintained.

**What about other options?** ObjectBox deserves mention: it offers the only official Flutter package with built-in HNSW vector search, ToOne/ToMany relationships, and claims 10-70x faster CRUD than sqflite. However, its relationship traversal beyond 2 hops becomes inefficient (no recursive query support), and its commercial license for sync features may be restrictive. Isar (community fork `isar_ce`) has link features but was abandoned by its original author, and lazy-loading links create N+1 query problems for graph traversal. Hive and sembast lack relationship primitives entirely and are not recommended. Kuzu, an excellent embedded property graph database with Cypher support, was **acquired by Apple in February 2026** and its open-source repository has been archived — use pre-acquisition releases cautiously but plan alternatives. For RDF interoperability, the `rdf_core` Dart package provides full W3C RDF 1.1 support with Turtle, JSON-LD, and N-Triples codecs, useful for import/export but not as the primary storage model.

| Solution | Query Power | Flutter Integration | Mobile Scalability | Best For |
|----------|------------|--------------------|--------------------|----------|
| **Drift/SQLite + graph_kit** | ★★★★ (CTEs + in-memory Cypher) | ★★★★★ (native) | ★★★★★ (proven) | MVP and most apps |
| **CozoDB via FFI** | ★★★★★ (Datalog + vector + temporal) | ★★★ (Rust FFI) | ★★★★ (SQLite backend) | Production systems |
| **ObjectBox** | ★★★ (1-2 hop relations + vector) | ★★★★★ (official package) | ★★★★ (fast CRUD) | Simple graphs + vector search |
| **libSQL + sqlite-vec** | ★★★★ (CTEs + native vector) | ★★★★ (sqflite compatible) | ★★★★★ (proven by Kin app) | Graph + vector hybrid |

### How much graph fits on a phone?

A mature personal knowledge graph from hundreds of conversations is surprisingly small. **10,000 entities at ~500 bytes each = ~5 MB. 50,000 relationships at ~300 bytes each = ~15 MB. 10,000 episodes at ~1 KB each = ~10 MB. Vector indices (384-dimensional, 60K vectors) = ~45 MB. Total: ~75–150 MB** — well within the budget of even low-end devices with 32 GB storage. In-memory, a 10K-node graph with properties consumes roughly 2–5 MB of RAM. Modern mid-range phones provide 8–12 GB RAM with a practical per-app budget of 256–512 MB.

For larger graphs, implement a three-tier memory architecture: a **hot tier** (~10 MB in memory) holding active conversation entities and their 1-hop neighbors via LRU cache; a **warm tier** (~50 MB memory-mapped) for vector indices and frequently accessed clusters; and a **cold tier** (on-disk) for full episode history, invalidated edges, and rarely accessed subgraphs. Graph compaction uses importance scoring: `importance = α × access_frequency + β × connectivity_degree + γ × recency_score + δ × confidence_score`. Nodes below threshold get pruned; invalidated relationships older than a configurable window (e.g., 90 days) get archived.

---

## Pillar 2: Extracting entities and relationships from conversations

### The LLM is your best extractor

The central insight from current research is that **the LLM already generating the conversational response is also the best tool for extracting structured knowledge from that conversation**. Dedicated NER models (spaCy, REBEL, FLAIR) struggle with conversational text — informal language, pronouns, ellipsis, implicit relationships. Meanwhile, GPT-4-class models achieve **89.7% precision and 92.3% recall** on entity extraction with few-shot learning, handle coreference resolution natively, and can extract implicit relationships that dedicated models miss entirely.

The recommended approach uses **structured output** capabilities now offered by all major LLM providers. OpenAI's structured outputs achieve **100% schema adherence** with compatible models. Anthropic's tool use, Google Gemini's JSON mode, and the open-source Instructor library (supporting 15+ providers) all enable reliable schema-compliant extraction. The key architectural decision: extract triples *in the same API call* that generates the conversational response, adding only ~10–15% marginal token cost.

Here is a concrete prompt template that produces both a natural language response and structured graph data:

```
System: You are a conversational AI assistant with a knowledge graph memory.
For each response, alongside your natural language reply, extract factual
information as structured triples. Resolve all pronouns to specific entity
names. Categorize each fact's temporal type.

Respond in this JSON format:
{
  "response": "Your natural language reply",
  "extracted_triples": [
    {
      "subject": "entity name",
      "subject_type": "PERSON|ORG|LOCATION|CONCEPT|EVENT|PREFERENCE",
      "predicate": "relationship (1-3 words, verb form)",
      "object": "entity name or value",
      "object_type": "type",
      "confidence": 0.0-1.0,
      "temporal_type": "STATIC|DYNAMIC|ATEMPORAL",
      "valid_from": "ISO date or null",
      "source": "user_stated|inferred|assistant_generated"
    }
  ],
  "entity_updates": [
    {
      "entity": "name",
      "attribute": "key",
      "new_value": "current",
      "action": "ADD|UPDATE|INVALIDATE"
    }
  ]
}
```

Research from TextMine (2024) shows that prompts with ontology specifications and examples improve extraction accuracy by **up to 44.2%**, reduce hallucinations by **22.5%**, and increase consistency by **20.9%**. For higher-quality extraction on critical conversations, a multi-stage approach works: first detect entities and types, then generate relation candidates for each entity pair, then normalize and canonicalize, then assemble final triples. The KGGen framework (Mo et al., 2025) implements this two-stage pattern with DSPy for consistent JSON output, and benchmarks show it outperforms both OpenIE and Microsoft GraphRAG on the MINE metric.

### Entity resolution: the make-or-break problem

As the graph grows, the same entity will appear with different surface forms: "Dr. Sarah Chen," "Sarah," "Dr. Chen," "my colleague." Without entity resolution, the graph fragments into disconnected islands of duplicates. The iText2KG/ATOM approach provides the most efficient merge pattern for mobile: compute cosine similarity between the new entity's embedding and existing entity embeddings. If similarity exceeds a threshold (~0.85), merge by updating the entity name to the most complete version, merging alias lists, and preserving all source episode references. If below threshold, create a new entity. This distance-metric approach is critical — it avoids expensive LLM calls for resolution, achieving **93.8% latency reduction** versus sequential LLM-based approaches in ATOM benchmarks.

For Flutter implementation, entity embeddings can be generated on-device using a quantized MiniLM model (~20 MB) via ONNX Runtime's Flutter plugin, or computed server-side during the LLM extraction call. The cosine similarity comparison against existing entities runs efficiently on-device with sqlite-vec or ObjectBox's built-in vector search — comparing against 10,000 entity embeddings takes under 10ms.

### Handling contradictions and temporal evolution

When the user says "I just started at Microsoft" but the graph already contains `(User, works_at, Google)`, the system must handle this gracefully. The recommended approach follows the OpenAI Temporal Agents Cookbook (2025), which classifies facts into three categories:

- **STATIC** facts are point-in-time events that don't change ("graduated in 2020") — stored with `valid_at` date, no invalidation
- **DYNAMIC** facts are time-bounded and can be superseded ("works at Company X") — when contradicted, set `valid_until` on the old triple and insert a new triple with `valid_from`
- **ATEMPORAL** facts are always true ("born in France") — no temporal bounds needed

For exclusive relations (a person has one employer, one birthday), the most recent information wins: invalidate the old triple (but preserve it for history) and insert the new one. For non-exclusive relations (friends, interests), add alongside existing triples. Mem0's approach adds a confirmation layer: when confidence is similar between old and new conflicting facts, flag for user confirmation rather than silently overwriting. This contradiction resolution pipeline — detect via semantic similarity against existing edges, classify temporal type, then apply the appropriate update strategy — runs entirely on-device using the local graph.

### What about on-device extraction without an API?

Dart/Flutter has **no mature on-device NER solution** currently. Google ML Kit's entity extraction (available via Flutter plugin) handles addresses, dates, emails, and phone numbers but not general named entities. The most viable path for offline extraction: export a quantized BERT-based NER model (like DistilBERT-NER) to ONNX format, deploy via the `onnxruntime_flutter` plugin, and run token classification on-device. This handles basic entity detection but not relationship extraction. For a true offline fallback, small on-device LLMs (Gemma 2B, Phi-3-mini) running via llama.cpp can perform extraction, though quality drops compared to GPT-4-class models. Samsung Research has demonstrated running 30B-parameter models in under 3 GB of memory through aggressive quantization — on-device extraction quality is improving rapidly.

---

## Pillar 3: RAG strategies with the local knowledge graph

### Personalized PageRank is the mobile-friendly retrieval method

Of all GraphRAG architectures, **HippoRAG** (NeurIPS 2024) is the most adaptable for on-device use. Inspired by hippocampal memory indexing theory, it works in two phases. Offline, the LLM extracts OpenIE triples and builds a schemaless knowledge graph with synonym links. Online, it extracts entities from the user's query, links them to graph nodes, then runs **Personalized PageRank (PPR)** with query entities as seed nodes to diffuse relevance scores across the graph. The top-ranked nodes and their neighborhoods form the retrieval context.

Why PPR excels on mobile: it's a lightweight iterative sparse matrix-vector multiplication — no LLM call needed at retrieval time, no complex query translation, just 15–20 iterations of `ppr = (1-α) × A^T × ppr + α × teleport` where A is the adjacency matrix. For a 10K-node graph, this completes in **single-digit milliseconds**. HippoRAG achieves **10–20x cheaper and 6–13x faster** multi-hop retrieval compared to iterative LLM-based methods, while matching or exceeding their accuracy. HippoRAG 2 extends this with dual-node graphs (passage nodes + phrase nodes) for an additional +7 F1 gain on associative reasoning benchmarks.

The on-device retrieval pipeline in pseudocode:

```dart
// 1. Extract entities from user query (lightweight, on-device)
final queryEntities = extractKeyPhrases(userQuery);

// 2. Link to graph nodes via fuzzy match + vector similarity
final seedNodes = queryEntities
    .map((e) => graphStore.findBestMatch(e, threshold: 0.8))
    .whereType<Entity>();

// 3. Run PPR from seed nodes (15-20 iterations, <10ms)
final pprScores = personalizedPageRank(
  graph: adjacencyMatrix,
  seedNodes: seedNodes,
  alpha: 0.15,
  iterations: 20,
);

// 4. Extract top-K subgraph
final relevantEntities = pprScores.topK(15);
final subgraph = extractNeighborhood(relevantEntities, maxHops: 2);
```

### Hybrid retrieval outperforms either graph or vector alone

The HybridRAG paper (Sarmah et al., arXiv:2408.04948) demonstrates that combining graph-based and vector-based retrieval consistently outperforms either alone. Graph retrieval handles entity-specific factual queries ("When did I meet Sarah?") and multi-hop relational queries ("What does Sarah's colleague think about AI?"). Vector similarity handles semantic/vague queries ("Tell me something interesting") and thematic queries ("What have I been thinking about lately?"). The fusion uses **Reciprocal Rank Fusion (RRF)**: for each result appearing in either list, compute `score = Σ 1/(k + rank)` across both lists, then sort by combined score. This is a parameter-free fusion method that works well in practice.

For on-device vector search, two Flutter-compatible options stand out. **sqlite-vec** provides SIMD-accelerated KNN search that compiles into the SQLite binary — storing graph structure and vector embeddings in a single database file. **ObjectBox** offers the first official Flutter package with built-in HNSW vector search alongside its object store. Both support float32 embeddings; sqlite-vec additionally supports float16, int8, and 1-bit quantization for aggressive storage savings (1-bit quantization reduces vector storage by 32x with Hamming distance search).

### Constructing effective prompts from graph context

Once the relevant subgraph is retrieved, it must be serialized into the LLM prompt. Research shows LLMs process natural language context most effectively, so the recommended serialization converts triples to sentences:

```
Known context about the user:
- Sarah works at Acme Corp as a software engineer (learned Jan 15, 2026)
- Sarah expressed concerns about the AI Ethics Project (Jan 15, 2026)
- The AI Ethics Project at Acme Corp is led by Dr. Chen
- User is interested in Dr. Chen's research on responsible AI
- User prefers vegetarian restaurants
```

Token budget management uses a greedy knapsack: score each retrieved fact by `relevance × recency × importance`, sort descending, and greedily fill the context window until the token budget is exhausted (typically 1,000–2,000 tokens for context, leaving room for conversation history and the system prompt). Bold the 2–3 most relevant facts for emphasis. The full prompt structure becomes:

```
System: You are {persona}. You have a personal knowledge graph about the user.

PERSONAL CONTEXT (from knowledge graph):
{serialized_subgraph}

CONVERSATION HISTORY:
{recent_turns}

User: {current_message}

Instructions: Use the personal context when relevant. Extract new facts
from this exchange for the knowledge graph. Output structured triples
alongside your response.
```

### Microsoft GraphRAG and LlamaIndex patterns — what's adaptable

Microsoft's GraphRAG (arXiv:2404.16130) introduced community-based hierarchical summarization: cluster the graph using the Leiden algorithm, then generate LLM summaries for each community. This excels at "global sensemaking" questions ("What are the main themes in my conversations?") that traditional RAG cannot answer. For mobile adaptation, pre-compute community summaries during background processing and store them as additional entity properties. When the user asks a thematic question, retrieve community summaries instead of individual triples — this is dramatically cheaper than Microsoft's original approach of generating partial responses from every community and aggregating them.

LlamaIndex's PropertyGraphIndex offers four retriever types: `LLMSynonymRetriever` (keyword expansion), `VectorContextRetriever` (embedding search), `TextToCypherRetriever` (natural language to Cypher), and `CypherTemplateRetriever` (parameterized queries). For on-device use, the vector context retriever pattern translates directly — embed the query, find similar nodes, then fetch their 1-2 hop neighborhoods. The Text-to-Cypher pattern is too expensive for mobile (requires an LLM call for query translation), but pre-defined query templates for common patterns ("find everything about person X," "what are the user's preferences about topic Y") work well.

---

## Lessons from production memory systems

### Three systems define the design space

**Mem0** (arXiv:2504.19413) operates as a two-phase pipeline: an extraction phase transforms conversations into atomic facts via LLM, then an update phase compares each fact against existing memories using vector similarity and decides ADD, UPDATE, DELETE, or NOOP. This achieves **26% higher accuracy** than OpenAI's built-in memory and **90%+ token cost savings** versus full-context approaches. Its graph variant (Mem0g) stores memories as a directed labeled graph using Neo4j. The key lesson: **the ADD/UPDATE/DELETE/NOOP decision framework** is the right abstraction for incremental graph construction.

**Zep's Graphiti** (arXiv:2501.13956, 20K+ GitHub stars) takes a fundamentally different approach with its three-tier hierarchy and bi-temporal model. Facts are never deleted — only invalidated with timestamps. This preserves historical accuracy and enables temporal queries ("What was the user's employer last year?"). Graphiti's hybrid retrieval combines semantic embeddings, keyword search, graph traversal, and multiple rerankers (RRF, MMR, episode-mentions, node distance, cross-encoder) for sub-200ms P95 latency. The key lesson: **non-lossy temporal tracking** is essential for conversational knowledge that evolves.

**MemGPT/Letta** (arXiv:2310.08560) introduces a different paradigm: the agent manages its own memory using tool calls (`memory_replace`, `archival_memory_insert`, `conversation_search`). A two-tier architecture mimics OS memory management — a small "main context" of editable core memory blocks, plus a large "external storage" of vector-indexed archival memory. Letta's recent "sleep-time compute" innovation performs memory consolidation asynchronously during agent downtime, separating it from active conversation. The key lesson: **background asynchronous memory processing** prevents graph updates from blocking the conversation UI.

### Kin proves personal knowledge graphs work on mobile

The most directly relevant precedent is **Kin** (mykin.ai), a privacy-focused iOS/Android app that runs a personal knowledge graph entirely on-device. Kin uses **libSQL** (Turso's open-source SQLite fork) with native vector search extensions, modeling its "concept graph enhanced with event-based structures" in relational tables. Events are first-class citizens — the system understands what happened, when, and why, representing what Kin calls "semantic spacetime." The tech stack uses `@op-engineering/op-sqlite` bindings and edge ML for minimum latency. This validates the core thesis: **personal knowledge graphs with vector search run viably on mobile devices using embedded SQL databases with vector extensions**, because no graph-native mobile database exists yet.

---

## Insights from international research across eight languages

Research across French, German, Japanese, Chinese, Korean, Spanish, and Portuguese sources reveals distinctive regional perspectives that enrich the architecture.

**Chinese researchers pioneer multi-model voting for quality control.** NebulaGraph's Chinese-language guide demonstrates using ChatGLM alongside BERT-based NER and rule-based systems in a voting ensemble, achieving ~70–80% accuracy with LLM alone but higher when combined. The Local Knowledge Graph tool on GitHub provides interactive on-device KG construction with reasoning visualization — a directly relevant Chinese open-source project. Huawei Cloud and Tencent Cloud both offer one-stop KG construction platforms, and CN-DBpedia (built from Chinese encyclopedia data, stored in MongoDB rather than a graph DB) represents a pragmatic engineering choice relevant to mobile deployment.

**Korean hardware research enables the on-device future.** Samsung Research (2025) demonstrated running 30B-parameter models in under 3 GB of memory through model compression and quantization. SK Hynix's analysis establishes that on-device AI requires models under 4B parameters (~4 GB) for current smartphones, with next-generation devices pushing this boundary. These hardware constraints directly inform what's possible for on-device extraction and embedding computation.

**Japanese emphasis on continuous verification** adds an important dimension. NTT Data's analysis and the Fintan research center at TIS both stress ongoing knowledge verification and maintenance — not just construction. This aligns with the need for periodic graph quality audits: re-embedding entities as semantic drift occurs, validating old facts against new conversations, and running deduplication sweeps.

**German researchers bridge conversational AI and knowledge graphs directly.** Onlim (Austria) published a whitepaper specifically on "More Knowledge for Chatbots and Voice Assistants" through KG integration. The SEMANTiCS conference series provides a European venue for this intersection. SAP Germany's emphasis on semantic data fabric — connecting distributed knowledge without centralization — mirrors the on-device philosophy.

**Spanish and Brazilian communities contribute unique tooling.** GNOSS, a 20-year-old Spanish semantic AI platform, offers enterprise KG solutions emphasizing regulatory compliance and auditability aligned with the EU AI Act — relevant for European deployments. Brazilian researchers at PUC-Rio and SBBD 2024 produced practical GraphRAG tutorials, and the ELLAS project demonstrates multilingual KG construction across Brazil, Bolivia, and Peru.

---

## Complete implementation blueprint for Flutter

### The end-to-end data flow

Every conversation turn triggers a pipeline with on-device and API components:

```
USER INPUT
    ↓
┌─────────────────────────────────────────┐
│ 1. GRAPH QUERY (on-device, <20ms)       │
│    Extract keywords from user message   │
│    Link to graph entities               │
│    PPR retrieval + vector search        │
│    Select top-K context subgraph        │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 2. PROMPT CONSTRUCTION (on-device)      │
│    Serialize subgraph as natural text   │
│    Combine: system prompt + context     │
│    + conversation history + user msg    │
│    + extraction instructions            │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 3. LLM API CALL (cloud, 200ms-2s)      │
│    Structured output: response +        │
│    extracted triples + entity updates   │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 4. DISPLAY RESPONSE (immediate)         │
│    Show natural language to user        │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ 5. GRAPH UPDATE (on-device, background) │
│    In a Dart Isolate:                   │
│    - Normalize extracted entities       │
│    - Deduplicate (embedding similarity) │
│    - Detect contradictions              │
│    - Insert/update/invalidate triples   │
│    - Store episode                      │
│    - Update importance scores           │
└─────────────────────────────────────────┘
```

Steps 1 and 2 run on-device before the API call, adding less than 20ms of latency. Step 3 is the LLM call, which dominates latency. Step 4 displays the response immediately. Step 5 runs asynchronously in a Dart Isolate so graph updates never block the UI. This is the MemGPT/Letta "sleep-time compute" pattern adapted for mobile.

### Flutter-specific implementation patterns

**Isolates for background graph processing.** Dart Isolates run on separate threads with their own memory, preventing graph operations from blocking the UI. The graph update pipeline (step 5) should run entirely in an Isolate. Since Isolates don't share memory, pass extracted triples as serializable messages:

```dart
// In main isolate
final receivePort = ReceivePort();
await Isolate.spawn(graphUpdateWorker, receivePort.sendPort);

void graphUpdateWorker(SendPort sendPort) {
  final db = openDatabase('knowledge_graph.db'); // own DB connection
  final port = ReceivePort();
  sendPort.send(port.sendPort);
  
  port.listen((message) {
    if (message is ExtractedTriples) {
      resolveEntities(db, message.triples);
      detectContradictions(db, message.triples);
      insertTriples(db, message.triples);
      updateImportanceScores(db);
    }
  });
}
```

**State management with Riverpod.** Use Riverpod providers to expose graph state reactively. A `graphServiceProvider` manages the database connection and exposes methods for querying. A `knowledgeContextProvider` computes the relevant subgraph for the current conversation. The graph visualization can observe a `graphSnapshotProvider` that updates after each background processing cycle.

**Platform channels for native performance (if needed).** If CozoDB is used, Rust FFI bindings go through `dart:ffi` directly — no platform channel needed. For sqlite-vec, compile the extension statically into the app's SQLite binary using the Flutter build system. On iOS, statically link the extension; on Android, load it as a shared library.

### Phased implementation roadmap

**Phase 1 — Foundation (weeks 1–4).** Implement SQLite storage via Drift with the three-table schema. Use `graph_kit` for in-memory graph operations. Build the LLM integration with structured output for triple extraction using a single prompt template. Implement naive entity resolution (exact name matching + Levenshtein distance). Store extracted triples and episodes. Skip vector search initially. The graph will work but with limited retrieval sophistication.

**Phase 2 — Intelligence (weeks 5–8).** Add vector embeddings: compute entity embeddings via the LLM API (or a lightweight API call to an embedding model), store in sqlite-vec or ObjectBox. Implement cosine-similarity entity deduplication (threshold 0.85). Add the bi-temporal model for contradiction handling. Implement PPR-based retrieval with hybrid vector fusion. Add importance scoring and recency weighting. The system now retrieves intelligently and handles knowledge evolution.

**Phase 3 — Sophistication (weeks 9–12).** Implement community detection (Leiden or label propagation) with LLM-generated community summaries during background processing. Add graph compaction and pruning for storage management. Implement the three-tier memory architecture (hot/warm/cold). Add graph visualization using `graphview`. Build an on-device fallback using ONNX Runtime with a quantized NER model for basic offline extraction.

**Phase 4 — Optimization (weeks 13–16).** Profile and optimize on target devices. Implement vector quantization (float16 or int8) for storage reduction. Add precomputed neighborhood caches for high-importance entities. Benchmark retrieval latency and tune PPR parameters. Consider migrating to CozoDB if SQLite's recursive CTEs become a bottleneck. Implement periodic graph quality audits (deduplication sweeps, stale fact detection).

### Concrete package selection

| Component | Package | Role |
|-----------|---------|------|
| Persistent storage | `drift` + `sqlite3_flutter_libs` | Adjacency-list graph tables with FTS5 |
| Vector search | `sqlite3` + sqlite-vec extension OR `objectbox` | Embedding-based similarity |
| In-memory graph | `graph_kit` | Pattern queries, algorithms, traversal |
| Graph algorithms | `graphs` (Dart team) | Shortest path, connected components |
| Graph visualization | `graphview` | Force-directed and hierarchical layouts |
| RDF interop | `rdf_core` | Import/export Turtle, JSON-LD |
| On-device ML | `onnxruntime_flutter` | NER model for offline fallback |
| LLM integration | `http` or `dio` | API calls with structured output |
| State management | `riverpod` | Reactive graph state |
| Background work | `dart:isolate` | Async graph updates |

---

## Conclusion

Building a local knowledge graph for conversational AI on Flutter is not only feasible — it's a well-timed architectural bet. The convergence of structured LLM outputs, lightweight embedded databases with vector extensions, and mobile hardware capable of running small ML models creates a practical implementation path that didn't exist two years ago.

Three architectural decisions matter most. First, **use the LLM itself as the primary extractor** with structured output mode — dedicated NER/RE models add complexity without proportional benefit for conversational text. Second, **store the graph in SQLite with adjacency-list tables** and use an in-memory graph library for complex queries — this leverages Flutter's strongest ecosystem while delivering sufficient query power for personal-scale graphs. Third, **implement Personalized PageRank for retrieval** rather than LLM-based query translation — it's the only GraphRAG pattern that runs in single-digit milliseconds on-device without an API call.

The temporal dimension is non-negotiable. Personal knowledge evolves — jobs change, preferences shift, relationships develop. The bi-temporal model from Graphiti (event time + ingestion time) with non-lossy invalidation rather than deletion provides the foundation for a knowledge graph that grows honestly and can answer questions about both current and historical states.

The most underappreciated insight from this research: **the graph doesn't need to be large to be valuable.** A personal knowledge graph of 1,000–5,000 entities built from hundreds of conversations occupies under 50 MB, queries in under 10ms, and provides conversational context that transforms a generic LLM into a deeply personalized assistant. Start with the simplest viable architecture — SQLite + structured LLM extraction + PPR retrieval — and let the complexity grow alongside the graph itself.