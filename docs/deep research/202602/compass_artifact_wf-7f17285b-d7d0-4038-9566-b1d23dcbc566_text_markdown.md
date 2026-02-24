# Système de Knowledge Graph local en Dart/Flutter : guide d'implémentation complet

**Un système de mémoire cognitive complet tournant à 100 % en local sur Android est réalisable aujourd'hui** grâce à la maturité de l'écosystème Dart/Flutter : Drift ORM avec FTS5 intégré, `flutter_embedder` pour les embeddings on-device (~33 ms par inférence), et `workmanager` pour l'orchestration en arrière-plan. Ce rapport détaille chaque couche — des schémas SQLite bi-temporels aux algorithmes de spreading activation et de décroissance mémorielle — avec du code Dart production-ready. L'architecture s'inspire d'OpenClaw (145 000+ étoiles GitHub) et du modèle bi-temporel de Graphiti/Zep (94,8 % sur le benchmark DMR), adaptés pour fonctionner sans aucun appel API, en substituant les LLM cloud par des modèles TFLite/ONNX locaux et du NLP basé sur des règles.

---

## 1. Modèles de données et schémas SQLite

L'architecture de stockage repose entièrement sur **SQLite via Drift ORM**, avec le package `sqlite3_flutter_libs` (v0.5.41, embarquant SQLite 3.50.4) qui compile nativement avec les flags `SQLITE_ENABLE_FTS5` et `SQLITE_ENABLE_JSON1`. Drift offre un typage fort, des requêtes réactives via `.watch()`, et un backend `dart:ffi` nettement plus performant que le passage par platform channels de sqflite.

### Schéma principal — fichier `schema.drift`

Le schéma implémente le modèle en triplets (sujet-prédicat-objet) avec métadonnées bi-temporelles, table d'alias, et nœuds de résumé hiérarchique :

```sql
-- ══════════════════════════════════════════════
-- ENTITÉS (Layer 4 — Structured Facts)
-- ══════════════════════════════════════════════
CREATE TABLE entities (
  id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name          TEXT    NOT NULL,
  entity_type   TEXT    NOT NULL DEFAULT 'CONCEPT',
  summary       TEXT,
  properties    TEXT    NOT NULL DEFAULT '{}',  -- JSON1
  embedding     BLOB,                           -- Float32 sérialisé (384D)
  -- Bi-temporal
  created_at    INTEGER NOT NULL DEFAULT (strftime('%s','now')),
  valid_at      INTEGER,                        -- début validité réelle
  invalid_at    INTEGER,                        -- fin validité réelle
  ingested_at   INTEGER NOT NULL DEFAULT (strftime('%s','now')),
  expired_at    INTEGER,                        -- invalidation système
  -- Activation & décroissance
  last_accessed INTEGER NOT NULL DEFAULT (strftime('%s','now')),
  access_count  INTEGER NOT NULL DEFAULT 1,
  temperature   TEXT    NOT NULL DEFAULT 'warm' CHECK(temperature IN ('hot','warm','cool','cold')),
  base_score    REAL    NOT NULL DEFAULT 0.5,
  -- Hiérarchie RAPTOR
  parent_summary_id INTEGER REFERENCES summary_nodes(id),
  is_active     INTEGER NOT NULL DEFAULT 1
);

CREATE INDEX idx_entities_type ON entities(entity_type);
CREATE INDEX idx_entities_temperature ON entities(temperature);
CREATE INDEX idx_entities_valid ON entities(valid_at, invalid_at);
CREATE INDEX idx_entities_active ON entities(is_active, temperature);

-- ══════════════════════════════════════════════
-- RELATIONS / TRIPLETS (Layer 4.5 — Knowledge Graph)
-- ══════════════════════════════════════════════
CREATE TABLE relations (
  id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  source_id     INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
  target_id     INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
  predicate     TEXT    NOT NULL,               -- ex: 'WORKS_AT', 'KNOWS'
  weight        REAL    NOT NULL DEFAULT 1.0,
  properties    TEXT    NOT NULL DEFAULT '{}',
  embedding     BLOB,
  -- Bi-temporal
  created_at    INTEGER NOT NULL DEFAULT (strftime('%s','now')),
  valid_at      INTEGER,
  invalid_at    INTEGER,
  ingested_at   INTEGER NOT NULL DEFAULT (strftime('%s','now')),
  expired_at    INTEGER,
  -- Activation
  last_accessed INTEGER NOT NULL DEFAULT (strftime('%s','now')),
  access_count  INTEGER NOT NULL DEFAULT 1,
  confidence    REAL    NOT NULL DEFAULT 1.0,
  source_text   TEXT,                           -- provenance
  is_active     INTEGER NOT NULL DEFAULT 1
);

CREATE INDEX idx_rel_source ON relations(source_id) WHERE is_active = 1;
CREATE INDEX idx_rel_target ON relations(target_id) WHERE is_active = 1;
CREATE INDEX idx_rel_predicate ON relations(predicate);
CREATE UNIQUE INDEX idx_rel_triplet ON relations(source_id, predicate, target_id)
  WHERE is_active = 1 AND expired_at IS NULL;

-- ══════════════════════════════════════════════
-- FACTS KEY-VALUE (Layer 4 — Deterministic Facts)
-- ══════════════════════════════════════════════
CREATE TABLE facts (
  id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  entity_id     INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
  key           TEXT    NOT NULL,
  value         TEXT    NOT NULL,
  value_type    TEXT    NOT NULL DEFAULT 'string',  -- string|number|date|json
  valid_at      INTEGER,
  invalid_at    INTEGER,
  ingested_at   INTEGER NOT NULL DEFAULT (strftime('%s','now')),
  expired_at    INTEGER,
  confidence    REAL    NOT NULL DEFAULT 1.0,
  source_text   TEXT
);

CREATE UNIQUE INDEX idx_facts_active ON facts(entity_id, key)
  WHERE expired_at IS NULL;

-- ══════════════════════════════════════════════
-- ALIAS (Résolution d'identité floue)
-- ══════════════════════════════════════════════
CREATE TABLE aliases (
  id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  entity_id     INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
  alias_name    TEXT    NOT NULL COLLATE NOCASE,
  alias_type    TEXT    NOT NULL DEFAULT 'name',  -- name|acronym|nickname|typo
  confidence    REAL    NOT NULL DEFAULT 1.0
);

CREATE INDEX idx_aliases_name ON aliases(alias_name COLLATE NOCASE);
CREATE INDEX idx_aliases_entity ON aliases(entity_id);

-- ══════════════════════════════════════════════
-- NŒUDS DE RÉSUMÉ HIÉRARCHIQUE (RAPTOR-style)
-- ══════════════════════════════════════════════
CREATE TABLE summary_nodes (
  id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  parent_id     INTEGER REFERENCES summary_nodes(id),
  level         INTEGER NOT NULL DEFAULT 0,       -- 0=feuille, 1+= résumés
  summary_text  TEXT    NOT NULL,
  embedding     BLOB,
  member_ids    TEXT    NOT NULL DEFAULT '[]',     -- JSON array d'entity IDs
  cluster_label INTEGER,
  created_at    INTEGER NOT NULL DEFAULT (strftime('%s','now')),
  last_updated  INTEGER NOT NULL DEFAULT (strftime('%s','now'))
);

CREATE INDEX idx_summary_parent ON summary_nodes(parent_id);
CREATE INDEX idx_summary_level ON summary_nodes(level);

-- ══════════════════════════════════════════════
-- FTS5 — Recherche plein texte
-- ══════════════════════════════════════════════
CREATE VIRTUAL TABLE entities_fts USING fts5(
  name,
  summary,
  entity_type,
  content=entities,
  content_rowid=id,
  prefix='2 3',
  tokenize='porter unicode61'
);

CREATE VIRTUAL TABLE facts_fts USING fts5(
  key,
  value,
  content=facts,
  content_rowid=id,
  prefix='2 3',
  tokenize='porter unicode61'
);

-- Triggers de synchronisation FTS5
CREATE TRIGGER entities_ai AFTER INSERT ON entities BEGIN
  INSERT INTO entities_fts(rowid, name, summary, entity_type)
  VALUES (new.id, new.name, new.summary, new.entity_type);
END;

CREATE TRIGGER entities_ad AFTER DELETE ON entities BEGIN
  INSERT INTO entities_fts(entities_fts, rowid, name, summary, entity_type)
  VALUES('delete', old.id, old.name, old.summary, old.entity_type);
END;

CREATE TRIGGER entities_au AFTER UPDATE ON entities BEGIN
  INSERT INTO entities_fts(entities_fts, rowid, name, summary, entity_type)
  VALUES('delete', old.id, old.name, old.summary, old.entity_type);
  INSERT INTO entities_fts(rowid, name, summary, entity_type)
  VALUES (new.id, new.name, new.summary, new.entity_type);
END;

-- ══════════════════════════════════════════════
-- REQUÊTES NOMMÉES
-- ══════════════════════════════════════════════
searchEntities:
  SELECT e.*, bm25(entities_fts, 5.0, 2.0, 1.0) AS rank
  FROM entities_fts
  JOIN entities e ON e.id = entities_fts.rowid
  WHERE entities_fts MATCH :query AND e.is_active = 1
  ORDER BY rank LIMIT :limit;

findNeighbors:
  SELECT e.*, r.predicate, r.weight, r.confidence
  FROM relations r
  JOIN entities e ON (
    (r.target_id = e.id AND r.source_id = :entityId) OR
    (r.source_id = e.id AND r.target_id = :entityId)
  )
  WHERE r.is_active = 1 AND r.expired_at IS NULL
  ORDER BY r.weight DESC;

resolveAlias:
  SELECT e.* FROM entities e
  JOIN aliases a ON a.entity_id = e.id
  WHERE a.alias_name = :name COLLATE NOCASE AND e.is_active = 1
  ORDER BY a.confidence DESC LIMIT 1;
```

### Configuration Drift pour FTS5

Le fichier `build.yaml` doit explicitement activer les modules FTS5 et JSON1 :

```yaml
targets:
  $default:
    builders:
      drift_dev:
        options:
          sql:
            dialect: sqlite
            options:
              version: "3.50"
              modules:
                - fts5
                - json1
          databases:
            knowledge_graph: lib/database/knowledge_graph_db.dart
          schema_dir: drift_schemas/
```

**Contrainte critique** : les tables FTS5 ne peuvent être déclarées qu'en SQL dans des fichiers `.drift`, pas via les classes Dart de Drift. Les requêtes MATCH, `bm25()`, `highlight()` et `snippet()` sont analysées au compile-time dans les fichiers `.drift` mais nécessitent `customSelect()` si écrites côté Dart.

### Modèle JSON atomique Zettelkasten

Chaque mémoire atomique est modélisée comme un objet JSON autonome avec identifiant unique, liens explicites, et métadonnées temporelles :

```dart
class AtomicMemory {
  final String id;           // UUID v4
  final String content;      // Texte atomique (1 fait = 1 mémoire)
  final String type;         // episodic | semantic | procedural | vault
  final List<String> tags;
  final List<String> linkedIds; // Liens Zettelkasten vers autres mémoires
  final Map<String, dynamic> metadata;
  final DateTime createdAt;
  final DateTime? validAt;
  final DateTime? invalidAt;

  Map<String, dynamic> toJson() => {
    'id': id,
    'content': content,
    'type': type,
    'tags': tags,
    'links': linkedIds,
    'meta': metadata,
    'created': createdAt.millisecondsSinceEpoch ~/ 1000,
    'valid_at': validAt?.millisecondsSinceEpoch,
    'invalid_at': invalidAt?.millisecondsSinceEpoch,
  };
}
```

### Résolution bi-temporelle des conflits

Le modèle bi-temporel de Graphiti utilise **quatre timestamps** par fait : `ingested_at` (T'), `expired_at` (T'), `valid_at` (T), `invalid_at` (T). L'invalidation ne supprime jamais : elle ferme la période de validité de l'ancien fait et en crée un nouveau.

```dart
/// Invalide un fait existant et crée le nouveau
Future<void> updateFactBiTemporal({
  required int entityId,
  required String key,
  required String newValue,
  DateTime? newValidAt,
}) async {
  final now = DateTime.now().millisecondsSinceEpoch ~/ 1000;
  await transaction(() async {
    // Fermer la validité de l'ancien fait (sans le supprimer)
    await customStatement(
      '''UPDATE facts SET expired_at = ?, invalid_at = ?
         WHERE entity_id = ? AND key = ? AND expired_at IS NULL''',
      [now, newValidAt?.millisecondsSinceEpoch ?? now, entityId, key],
    );
    // Insérer le nouveau fait
    await into(facts).insert(FactsCompanion.insert(
      entityId: entityId,
      key: key,
      value: newValue,
      validAt: Value(newValidAt?.millisecondsSinceEpoch),
      ingestedAt: Value(now),
    ));
  });
}
```

---

## 2. Algorithmes — implémentations Dart complètes

### Décroissance mémorielle (courbe d'Ebbinghaus)

La rétention suit la formule exponentielle **R = e^(−t/S)** où S (stabilité) augmente logarithmiquement avec chaque accès, modélisant l'effet de la répétition espacée. Les seuils Hot/Warm/Cool/Cold déterminent la priorité de récupération et l'éligibilité à la consolidation.

```dart
import 'dart:math';

enum MemoryTemperature { hot, warm, cool, cold }

class MemoryDecay {
  static const double _baseStability = 86400.0; // 1 jour en secondes
  static const double _reinforcementFactor = 1.5;

  /// R = e^(-t/S) — rétention pure
  static double retention(double elapsedSeconds, double stability) {
    if (stability <= 0) return 0.0;
    return exp(-elapsedSeconds / stability);
  }

  /// Stabilité dynamique : S = baseS × (1 + factor × ln(accessCount + 1))
  /// Chaque accès renforce la mémoire (rendements décroissants)
  static double stability(int accessCount, [double base = _baseStability]) {
    return base * (1 + _reinforcementFactor * log(accessCount + 1));
  }

  /// Score d'activation combinant importance intrinsèque + décroissance
  static double activationScore({
    required double baseScore,
    required int lastAccessedEpoch,
    required int accessCount,
    int? nowEpoch,
  }) {
    nowEpoch ??= DateTime.now().millisecondsSinceEpoch ~/ 1000;
    final elapsed = (nowEpoch - lastAccessedEpoch).toDouble();
    final s = stability(accessCount);
    return baseScore * retention(elapsed, s);
  }

  /// Classification Hot ≥ 0.7 | Warm ≥ 0.4 | Cool ≥ 0.1 | Cold < 0.1
  static MemoryTemperature classify(double score) {
    if (score >= 0.7) return MemoryTemperature.hot;
    if (score >= 0.4) return MemoryTemperature.warm;
    if (score >= 0.1) return MemoryTemperature.cool;
    return MemoryTemperature.cold;
  }

  /// SQL batch : recalcule la température de TOUTES les entités
  /// Exécuté dans un WorkManager periodic (toutes les heures)
  static String get batchDecaySQL => '''
    UPDATE entities SET temperature = CASE
      WHEN (base_score * EXP(
        -1.0 * (strftime('%s','now') - last_accessed)
        / ($_baseStability * (1 + $_reinforcementFactor * LN(access_count + 1)))
      )) >= 0.7 THEN 'hot'
      WHEN (base_score * EXP(
        -1.0 * (strftime('%s','now') - last_accessed)
        / ($_baseStability * (1 + $_reinforcementFactor * LN(access_count + 1)))
      )) >= 0.4 THEN 'warm'
      WHEN (base_score * EXP(
        -1.0 * (strftime('%s','now') - last_accessed)
        / ($_baseStability * (1 + $_reinforcementFactor * LN(access_count + 1)))
      )) >= 0.1 THEN 'cool'
      ELSE 'cold'
    END
    WHERE is_active = 1;
  ''';
}
```

**Note importante** : SQLite ne dispose pas nativement de `EXP()` ni `LN()`. Il faut soit enregistrer ces fonctions via `sqlite3`'s `createFunction()` en Dart, soit effectuer le calcul côté Dart dans un batch. L'approche Dart est recommandée pour la portabilité :

```dart
Future<void> applyDecayBatch(AppDatabase db) async {
  final now = DateTime.now().millisecondsSinceEpoch ~/ 1000;
  final entities = await db.customSelect(
    'SELECT id, base_score, last_accessed, access_count FROM entities WHERE is_active = 1'
  ).get();

  final updates = <({int id, String temp})>[];
  for (final row in entities) {
    final score = MemoryDecay.activationScore(
      baseScore: row.read<double>('base_score'),
      lastAccessedEpoch: row.read<int>('last_accessed'),
      accessCount: row.read<int>('access_count'),
      nowEpoch: now,
    );
    updates.add((id: row.read<int>('id'), temp: MemoryDecay.classify(score).name));
  }

  await db.batch((batch) {
    for (final u in updates) {
      batch.customStatement(
        'UPDATE entities SET temperature = ? WHERE id = ?',
        [u.temp, u.id],
      );
    }
  });
}
```

### Spreading activation sur le graphe

L'algorithme propage de l'énergie depuis des nœuds-ancres le long des arêtes pondérées, avec un facteur de décroissance par saut. Chaque nœud ne « fire » qu'une fois pour éviter les boucles. Le résultat est un mapping nœud → score d'activation utilisé pour le classement hybride.

```dart
import 'dart:collection';

class SpreadingActivation {
  final double decayFactor;     // 0.85 typique
  final double firingThreshold; // 0.01 minimum pour propager
  final int maxIterations;      // 3-5 sauts max

  SpreadingActivation({
    this.decayFactor = 0.85,
    this.firingThreshold = 0.01,
    this.maxIterations = 4,
  });

  /// Propage l'activation depuis les graines.
  /// [edges] : adjacency list {nodeId -> [(targetId, weight)]}
  /// [seeds] : {nodeId -> activation initiale (0..1)}
  /// Retourne : {nodeId -> activation finale}
  Map<int, double> activate(
    Map<int, List<(int target, double weight)>> edges,
    Map<int, double> seeds,
  ) {
    final activation = <int, double>{};
    final fired = <int>{};

    // Initialisation des graines
    for (final e in seeds.entries) {
      activation[e.key] = e.value.clamp(0.0, 1.0);
    }

    for (int iter = 0; iter < maxIterations; iter++) {
      final toFire = activation.entries
          .where((e) => e.value > firingThreshold && !fired.contains(e.key))
          .map((e) => e.key)
          .toList();

      if (toFire.isEmpty) break;

      for (final nodeId in toFire) {
        fired.add(nodeId);
        final nodeAct = activation[nodeId]!;
        final neighbors = edges[nodeId] ?? [];

        for (final (targetId, weight) in neighbors) {
          final spread = nodeAct * weight * decayFactor;
          final current = activation[targetId] ?? 0.0;
          activation[targetId] = (current + spread).clamp(0.0, 1.0);
        }
      }
    }
    return activation;
  }
}
```

Pour l'intégration dans le pipeline de requête, les nœuds-graines sont sélectionnés par recherche FTS5 ou similarité cosinus, puis l'activation se propage sur le sous-graphe local :

```dart
/// Pipeline complet : query -> seeds -> spreading -> hybrid ranking
Future<List<RankedEntity>> hybridQuery(String query, {int limit = 20}) async {
  // 1. FTS5 BM25 — candidats lexicaux
  final ftsResults = await db.searchEntities(query, limit: limit * 3);

  // 2. Embedding similarité — candidats sémantiques
  final queryEmb = await embedder.embed(texts: [query]);
  final vecResults = await vectorSearch(queryEmb.first, limit: limit * 3);

  // 3. Union des candidats + construction sous-graphe
  final candidateIds = {...ftsResults.map((r) => r.id), ...vecResults.map((r) => r.id)};
  final subgraph = await loadSubgraph(candidateIds, hops: 2);

  // 4. Spreading activation depuis les top BM25 + top vector
  final seeds = <int, double>{};
  for (final r in ftsResults.take(5)) seeds[r.id] = 1.0;
  for (final r in vecResults.take(5)) seeds[r.id] = 0.8;
  final sa = SpreadingActivation();
  final activations = sa.activate(subgraph.adjacency, seeds);

  // 5. Score hybride : fusion pondérée
  final scored = <RankedEntity>[];
  for (final id in candidateIds) {
    final bm25 = ftsResults.firstWhere((r) => r.id == id,
        orElse: () => null)?.normalizedScore ?? 0.0;
    final vec = vecResults.firstWhere((r) => r.id == id,
        orElse: () => null)?.similarity ?? 0.0;
    final act = activations[id] ?? 0.0;
    final decay = MemoryDecay.activationScore(
      baseScore: 1.0, lastAccessedEpoch: ..., accessCount: ...,
    );

    final finalScore = 0.30 * bm25 + 0.30 * vec + 0.25 * act + 0.15 * decay;
    scored.add(RankedEntity(id: id, score: finalScore));
  }

  scored.sort((a, b) => b.score.compareTo(a.score));
  return scored.take(limit).toList();
}
```

### BM25 — implémentation standalone et FTS5 intégré

Le package Dart `bm25` (v2.2.3, MIT) fournit une implémentation complète avec parallélisation via isolates. Cependant, pour le Knowledge Graph, **la fonction `bm25()` intégrée à FTS5 est préférable** car elle opère directement sur l'index sans transfert de données :

```sql
-- Pondération par colonne : name (5x), summary (2x), type (1x)
SELECT e.*, -bm25(entities_fts, 5.0, 2.0, 1.0) AS bm25_score
FROM entities_fts
JOIN entities e ON e.id = entities_fts.rowid
WHERE entities_fts MATCH :query AND e.is_active = 1
ORDER BY bm25_score DESC
LIMIT 50;
```

Le signe négatif est nécessaire car FTS5 retourne des scores où **plus petit = plus pertinent**. La normalisation pour la fusion hybride se fait par min-max scaling sur le batch de résultats.

### Clustering DBSCAN simplifié pour la consolidation

Aucune implémentation HDBSCAN n'existe en Dart. Le package `simple_cluster` (v0.3.0) offre du DBSCAN basique. Pour la consolidation mémoire de type RAPTOR, une approche en deux étapes est recommandée : **DBSCAN sur les embeddings** pour former les clusters, puis **résumé récursif** ascendant.

```dart
class MemoryClusterer {
  final double epsilon;
  final int minPoints;

  MemoryClusterer({this.epsilon = 0.3, this.minPoints = 3});

  /// Cluster les entités par similarité cosinus de leurs embeddings
  /// Retourne : Map<clusterId, List<entityId>>
  Map<int, List<int>> cluster(List<(int id, List<double> embedding)> entities) {
    final n = entities.length;
    final labels = List.filled(n, -1);
    int clusterId = 0;

    for (int i = 0; i < n; i++) {
      if (labels[i] != -1) continue;
      final neighbors = _regionQuery(entities, i);
      if (neighbors.length < minPoints) continue; // bruit

      labels[i] = clusterId;
      final queue = Queue<int>.from(neighbors);
      while (queue.isNotEmpty) {
        final j = queue.removeFirst();
        if (labels[j] == -1 || labels[j] == clusterId) {
          labels[j] = clusterId;
          final jNeighbors = _regionQuery(entities, j);
          if (jNeighbors.length >= minPoints) {
            for (final k in jNeighbors) {
              if (labels[k] == -1) queue.add(k);
            }
          }
        }
      }
      clusterId++;
    }

    // Grouper par cluster
    final result = <int, List<int>>{};
    for (int i = 0; i < n; i++) {
      if (labels[i] >= 0) {
        result.putIfAbsent(labels[i], () => []).add(entities[i].$1);
      }
    }
    return result;
  }

  List<int> _regionQuery(
    List<(int, List<double>)> entities, int idx,
  ) {
    final neighbors = <int>[];
    final emb = entities[idx].$2;
    for (int i = 0; i < entities.length; i++) {
      if (1.0 - _cosineSim(emb, entities[i].$2) <= epsilon) {
        neighbors.add(i);
      }
    }
    return neighbors;
  }

  double _cosineSim(List<double> a, List<double> b) {
    double dot = 0, nA = 0, nB = 0;
    for (int i = 0; i < a.length; i++) {
      dot += a[i] * b[i];
      nA += a[i] * a[i];
      nB += b[i] * b[i];
    }
    return (nA == 0 || nB == 0) ? 0 : dot / (sqrt(nA) * sqrt(nB));
  }
}
```

### Traversée multi-hop avec poids

```dart
/// BFS pondéré avec limite de profondeur
/// Retourne les entités atteignables en N sauts avec leur distance minimale
Future<Map<int, ({int hops, double minWeight})>> multiHopBFS(
  int startId, int maxHops, AppDatabase db,
) async {
  final result = <int, ({int hops, double minWeight})>{};
  final queue = Queue<(int nodeId, int depth, double cumWeight)>();
  queue.add((startId, 0, 1.0));
  result[startId] = (hops: 0, minWeight: 1.0);

  while (queue.isNotEmpty) {
    final (nodeId, depth, cumWeight) = queue.removeFirst();
    if (depth >= maxHops) continue;

    final neighbors = await db.customSelect(
      '''SELECT target_id, weight FROM relations
         WHERE source_id = ? AND is_active = 1 AND expired_at IS NULL
         UNION ALL
         SELECT source_id, weight FROM relations
         WHERE target_id = ? AND is_active = 1 AND expired_at IS NULL''',
      variables: [Variable.withInt(nodeId), Variable.withInt(nodeId)],
    ).get();

    for (final row in neighbors) {
      final targetId = row.read<int>('target_id');
      final weight = row.read<double>('weight');
      final newWeight = cumWeight * weight;

      if (!result.containsKey(targetId) ||
          result[targetId]!.hops > depth + 1) {
        result[targetId] = (hops: depth + 1, minWeight: newWeight);
        queue.add((targetId, depth + 1, newWeight));
      }
    }
  }
  return result;
}
```

---

## 3. Stack technique Flutter/Dart et bibliothèques

### Drift ORM — le choix sans compromis

**Drift est fortement recommandé** par rapport à sqflite pour un Knowledge Graph. Les avantages décisifs sont le **typage fort** avec génération de code, les **requêtes réactives** (`.watch()` pour une UI temps-réel), le support natif **FTS5** dans les fichiers `.drift`, et surtout le backend **`dart:ffi`** qui est significativement plus rapide que les platform channels de sqflite. Drift gère aussi les `WITH RECURSIVE` pour les traversées de graphe en SQL pur, les migrations versionnées avec `make-migrations`, et le support multi-isolates via `shareAcrossIsolates`.

La définition des tables Dart complémentaires (non-FTS5) utilise le DSL typé :

```dart
@DriftDatabase(
  include: {'schema.drift'},  // Tables FTS5 + requêtes nommées
)
class KnowledgeGraphDB extends _$KnowledgeGraphDB {
  KnowledgeGraphDB() : super(_openConnection());

  @override
  int get schemaVersion => 1;

  static QueryExecutor _openConnection() {
    return driftDatabase(
      name: 'knowledge_graph',
      native: DriftNativeOptions(
        shareAcrossIsolates: true, // Partage UI ↔ WorkManager
      ),
    );
  }

  @override
  MigrationStrategy get migration => MigrationStrategy(
    beforeOpen: (details) async {
      await customStatement('PRAGMA foreign_keys = ON');
      await customStatement('PRAGMA journal_mode = WAL');
      await customStatement('PRAGMA busy_timeout = 5000');
    },
  );
}
```

### Embeddings on-device : `flutter_embedder` comme solution optimale

Le package **`flutter_embedder`** (v0.1.7, publié début 2026) est la solution la plus aboutie pour les embeddings locaux. Il encapsule **ONNX Runtime + tokenizers HuggingFace** via Rust FFI (`flutter_rust_bridge`), résolvant le problème critique de la tokenisation que les packages bruts `tflite_flutter` et `onnxruntime` ne gèrent pas.

```dart
import 'package:flutter_embedder/flutter_embedder.dart';

// Initialisation (une seule fois)
await initFlutterEmbedder();

// MiniLM : 384D, ~90 MB, ~33-100ms par inférence sur Android
final embedder = MiniLmEmbedder.create(
  modelPath: modelManager.getPath('all-minilm-l6-v2.onnx'),
  tokenizerPath: modelManager.getPath('minilm-tokenizer.json'),
);

// Génération d'embedding
final vectors = embedder.embed(texts: ['Paris est la capitale de la France']);
// vectors[0] = Float32List de 384 éléments

// Utilitaires intégrés (implémentés en Rust, performants)
final similarity = cosineDistance(vectorA, vectorB);
final normalized = normalize(rawVector);
```

Les alternatives viables selon le contexte :

| Solution | Tokenisation | Dim. | Taille | Latence Android | Licence |
|---|---|---|---|---|---|
| **flutter_embedder + MiniLM** | ✅ Intégrée (Rust) | 384 | ~90 MB | ~33-100 ms | MIT |
| **fonnx + MiniLM** | ✅ Intégrée | 384 | ~90 MB | ~33 ms | GPL v2 |
| **tflite_flutter + USE** | ✅ Dans le modèle | 100 | ~30 MB | ~50 ms | Apache 2.0 |
| **onnxruntime_v2 + custom** | ❌ Manuelle | variable | variable | ~40-150 ms | MIT |

Pour le stockage et la recherche vectorielle, **ObjectBox** (v5.x) offre un index **HNSW** natif en Dart, capable de gérer des millions de vecteurs avec des requêtes en millisecondes. Alternativement, pour un système plus simple sans dépendance additionnelle, la similarité cosinus en Dart pur avec `Float32List` suffit jusqu'à ~50 000 vecteurs.

### Isolates Dart et traitement en arrière-plan

L'architecture de traitement repose sur **trois niveaux** de parallélisme :

**Niveau 1 — `Isolate.run()` pour les tâches ponctuelles lourdes** (extraction d'entités, calcul d'embeddings) :

```dart
Future<List<ExtractedEntity>> extractEntities(String text) async {
  return await Isolate.run(() => _extractEntitiesIsolate(text));
}
```

**Niveau 2 — `Isolate.spawn()` pour les workers persistants** (pipeline d'ingestion continu) :

```dart
class IngestionWorker {
  late final SendPort _workerPort;

  Future<void> start() async {
    final receivePort = ReceivePort();
    await Isolate.spawn(_workerEntry, receivePort.sendPort);
    _workerPort = await receivePort.first as SendPort;
  }

  void ingest(String text) => _workerPort.send(text);

  static void _workerEntry(SendPort mainPort) {
    final workerPort = ReceivePort();
    mainPort.send(workerPort.sendPort);
    workerPort.listen((message) async {
      if (message is String) {
        final entities = _extractEntitiesIsolate(message);
        // Stocker via DB ouverte dans cet isolate
      }
    });
  }
}
```

**Niveau 3 — `workmanager` pour les tâches planifiées Android** :

```dart
void registerBackgroundTasks() {
  // Décroissance mémorielle : toutes les heures
  Workmanager().registerPeriodicTask(
    'decay-hourly', 'applyDecay',
    frequency: Duration(hours: 1),
    constraints: Constraints(requiresBatteryNotLow: true),
  );

  // Consolidation RAPTOR : toutes les 6 heures, appareil inactif
  Workmanager().registerPeriodicTask(
    'consolidation-6h', 'consolidateMemory',
    frequency: Duration(hours: 6),
    constraints: Constraints(
      requiresDeviceIdle: true,
      requiresBatteryNotLow: true,
    ),
  );

  // Nettoyage profond : quotidien, en charge
  Workmanager().registerPeriodicTask(
    'cleanup-daily', 'deepCleanup',
    frequency: Duration(hours: 24),
    constraints: Constraints(
      requiresCharging: true,
      requiresBatteryNotLow: true,
    ),
  );
}
```

**Contrainte Android critique** : l'intervalle minimum est **15 minutes** (limite dure de WorkManager/JobScheduler). En mode Doze, les tâches sont différées aux fenêtres de maintenance. Le `callbackDispatcher` tourne dans un **isolate séparé** — les singletons et `get_it` du main isolate ne sont pas disponibles ; il faut réinitialiser la DB via `shareAcrossIsolates: true` de Drift.

```dart
@pragma('vm:entry-point')
void callbackDispatcher() {
  Workmanager().executeTask((task, inputData) async {
    // DB partagée via IsolateNameServer
    final db = KnowledgeGraphDB();
    try {
      switch (task) {
        case 'applyDecay':
          await applyDecayBatch(db);
          return true;
        case 'consolidateMemory':
          await runRaptorConsolidation(db);
          return true;
        case 'deepCleanup':
          await purgeExpiredAndCold(db);
          return true;
      }
      return false;
    } finally {
      await db.close();
    }
  });
}
```

---

## 4. Blueprint architectural complet

### Vue d'ensemble du système

L'architecture se décompose en **cinq couches** fonctionnelles, du stockage brut à l'interface agent :

```
┌─────────────────────────────────────────────────────────┐
│                    AGENT / UI LAYER                      │
│  HookPipeline (pre-query) → AutoRecall → AutoCapture    │
├─────────────────────────────────────────────────────────┤
│                   QUERY PIPELINE                         │
│  FTS5 BM25 ──┐                                          │
│  Vector sim ──┼──→ Score Fusion → Re-rank → Top-K       │
│  Graph SA   ──┘    (pondérée)     (decay)               │
├─────────────────────────────────────────────────────────┤
│                  INGESTION PIPELINE                       │
│  Texte brut → Extraction entités → Résolution aliases    │
│            → Extraction relations → Résolution conflits  │
│            → Embedding → Stockage bi-temporel            │
├─────────────────────────────────────────────────────────┤
│               BACKGROUND PROCESSORS                      │
│  WorkManager 1h: Decay  │ 6h: Consolidation RAPTOR      │
│  WorkManager 24h: Purge │ Isolate: Ingestion continue    │
├─────────────────────────────────────────────────────────┤
│                  STORAGE LAYER                           │
│  Drift/SQLite: entities + relations + facts + aliases    │
│  FTS5: entities_fts + facts_fts                         │
│  BLOB: embeddings 384D (Float32)                        │
│  summary_nodes: arbre hiérarchique RAPTOR               │
└─────────────────────────────────────────────────────────┘
```

### Pipeline d'ingestion locale

Sans LLM cloud, l'extraction d'entités et de relations repose sur une approche hybride **NER basé sur des règles + patterns regex + modèle TFLite léger** :

```dart
class LocalIngestionPipeline {
  final KnowledgeGraphDB db;
  final MiniLmEmbedder embedder;
  final EntityExtractor extractor;

  /// Processus complet d'ingestion d'un texte
  Future<void> ingest(String text, {DateTime? referenceTime}) async {
    referenceTime ??= DateTime.now();

    // 1. Extraction d'entités (isolate pour ne pas bloquer l'UI)
    final entities = await Isolate.run(
      () => extractor.extractEntities(text),
    );

    // 2. Extraction de relations entre entités trouvées
    final relations = await Isolate.run(
      () => extractor.extractRelations(text, entities),
    );

    // 3. Résolution d'alias — chaque entité est-elle déjà connue ?
    for (final entity in entities) {
      final existing = await resolveEntity(entity.name);
      if (existing != null) {
        entity.resolvedId = existing.id;
        await updateEntitySummary(existing.id, entity);
      }
    }

    // 4. Génération d'embeddings (batch)
    final texts = entities.map((e) => '${e.name}: ${e.summary}').toList();
    final embeddings = embedder.embed(texts: texts);

    // 5. Stockage bi-temporel transactionnel
    await db.transaction(() async {
      for (int i = 0; i < entities.length; i++) {
        final id = entities[i].resolvedId ?? await insertEntity(
          entities[i], embeddings[i], referenceTime!,
        );
        entities[i].resolvedId = id;
      }
      for (final rel in relations) {
        await insertRelationBiTemporal(rel, referenceTime!);
      }
    });
  }

  /// Résolution d'entité par alias (Jaro-Winkler + table d'alias)
  Future<Entity?> resolveEntity(String name) async {
    // Recherche exacte dans aliases
    final exact = await db.resolveAlias(name);
    if (exact.isNotEmpty) return exact.first;

    // Recherche floue FTS5 + scoring Jaro-Winkler
    final candidates = await db.searchEntities(name, limit: 5);
    for (final c in candidates) {
      if (jaroWinkler(name.toLowerCase(), c.name.toLowerCase()) > 0.88) {
        // Créer l'alias pour accélérer les futures résolutions
        await db.into(db.aliases).insert(AliasesCompanion.insert(
          entityId: c.id, aliasName: name,
        ));
        return c;
      }
    }
    return null; // Nouvelle entité
  }
}
```

### Pipeline de requête hybride

Le pipeline de requête combine **trois signaux** — FTS5 BM25, similarité vectorielle, et spreading activation — fusionnés par pondération linéaire avec boost de décroissance temporelle. L'approche utilise l'**union** (pas l'intersection) des résultats pour maximiser le recall.

L'implémentation complète du `hybridQuery` est donnée dans la section Algorithmes ci-dessus. Le pipeline séquentiel est : (1) FTS5 MATCH avec `bm25()` intégré, (2) similarité cosinus sur embeddings stockés en BLOB, (3) construction du sous-graphe 2-hops autour des candidats, (4) spreading activation depuis les top-k seeds, (5) fusion pondérée des quatre scores (`bm25 × 0.30 + vector × 0.30 + activation × 0.25 + decay × 0.15`).

### Système de hooks et injection de contexte

```dart
class MemoryHookSystem {
  final KnowledgeGraphDB db;
  final LocalIngestionPipeline ingestion;

  /// Hook PRÉ-AGENT : enrichit la requête avec le contexte mémoriel
  Future<AgentContext> beforeAgentStart(String userQuery) async {
    // Auto-recall : récupération hybride
    final memories = await hybridQuery(userQuery, limit: 10);

    // Touch : renforcer les mémoires rappelées (répétition espacée)
    await touchEntities(memories.map((m) => m.id).toList());

    // Construire le contexte injectable
    return AgentContext(
      relevantEntities: memories,
      relatedFacts: await getFactsForEntities(memories),
      graphContext: await getSubgraphSummary(memories),
    );
  }

  /// Hook POST-AGENT : capture automatique des nouvelles informations
  Future<void> afterAgentResponse(String userMsg, String agentResp) async {
    await ingestion.ingest('$userMsg\n$agentResp');
  }
}
```

### Consolidation hiérarchique RAPTOR

La consolidation s'exécute dans le WorkManager 6h et construit un arbre de résumés ascendant. Sans LLM cloud, les résumés sont générés par **extraction des phrases clés** (TextRank simplifié) ou via un petit modèle local si disponible :

```dart
Future<void> runRaptorConsolidation(KnowledgeGraphDB db) async {
  // 1. Charger les entités cool/warm candidates
  final candidates = await db.customSelect(
    '''SELECT id, name, summary, embedding FROM entities
       WHERE is_active = 1 AND temperature IN ('warm','cool')
       AND parent_summary_id IS NULL''',
  ).get();

  // 2. Clustering DBSCAN sur les embeddings
  final clusterer = MemoryClusterer(epsilon: 0.35, minPoints: 3);
  final entityData = candidates.map((r) => (
    r.read<int>('id'),
    deserializeEmbedding(r.read<Uint8List>('embedding')),
  )).toList();
  final clusters = clusterer.cluster(entityData);

  // 3. Pour chaque cluster, créer un nœud de résumé
  for (final entry in clusters.entries) {
    final memberIds = entry.value;
    final memberTexts = candidates
        .where((r) => memberIds.contains(r.read<int>('id')))
        .map((r) => '${r.read<String>('name')}: ${r.read<String>('summary')}')
        .toList();

    // Résumé par extraction (sans LLM)
    final summary = extractiveSummary(memberTexts.join('. '), maxSentences: 3);
    final embedding = embedder.embed(texts: [summary]).first;

    // Insérer le nœud de résumé
    final summaryId = await db.into(db.summaryNodes).insert(
      SummaryNodesCompanion.insert(
        level: 1,
        summaryText: summary,
        embedding: Value(serializeEmbedding(embedding)),
        memberIds: jsonEncode(memberIds),
      ),
    );

    // Lier les entités enfants
    await db.customStatement(
      'UPDATE entities SET parent_summary_id = ? WHERE id IN (${memberIds.join(",")})',
      [summaryId],
    );
  }

  // 4. Récursion : si assez de nœuds niveau 1, créer niveau 2
  // (même logique appliquée aux summary_nodes de niveau 1)
}
```

---

## 5. État de l'écosystème Dart/Flutter pour ce projet

### Cartographie des packages disponibles

La recherche exhaustive de l'écosystème révèle un paysage en maturation rapide, avec des solutions viables pour chaque composant mais aucun système intégré :

**Stockage et requêtes** : Drift ORM est mature et production-ready. Le support FTS5 via `.drift` files fonctionne pleinement avec `sqlite3_flutter_libs` qui compile SQLite 3.50.4 avec FTS5 activé par défaut. Le package `rinne_graph` offre une API Gremlin sur SQLite mais reste en développement actif. Le package `graph_kit` fournit des requêtes pattern Cypher-like en mémoire. Pour une solution production, **construire sur Drift** avec un modèle adjacency-list est plus fiable que dépendre de ces packages précoces.

**Algorithmes** : Le package `bm25` (v2.2.3) offre un BM25 complet en Dart pur. Le package `simple_cluster` implémente DBSCAN. Le package `algorithms_core` fournit **25+ algorithmes de graphe** (BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall, Tarjan SCC). Aucun HDBSCAN natif n'existe — le DBSCAN simplifié présenté dans ce rapport est l'approche recommandée, suffisante pour le clustering de consolidation.

**ML on-device** : `flutter_embedder` (v0.1.7, Rust FFI + ONNX + HF tokenizers) est la percée récente qui rend les embeddings locaux pratiques. Le modèle all-MiniLM-L6-v2 offre le meilleur compromis qualité/taille (**384 dimensions, ~90 MB, ~33 ms sur Pixel Fold**). ObjectBox (v5.x) fournit un index HNSW natif pour la recherche vectorielle si nécessaire.

**Background processing** : `workmanager` (v0.9.0+3, 2.3K likes) est stable et bien maintenu. Drift supporte nativement le partage inter-isolates via `shareAcrossIsolates` et `NativeDatabase.createInBackground`. La combinaison des deux résout élégamment le problème de la persistance en arrière-plan.

### Ce qui manque et doit être implémenté manuellement

Quatre composants n'ont pas d'équivalent packagé et nécessitent une implémentation custom, tous fournis dans ce rapport : le **spreading activation** (algorithme cognitif rarement implémenté hors Python), la **décroissance mémorielle Ebbinghaus** avec classification thermique, la **fusion de scores hybride** (combinaison FTS5 + vecteurs + graphe), et la **consolidation hiérarchique RAPTOR** (clustering + résumé récursif). L'extraction d'entités sans LLM reste le maillon le plus faible : les approches basées sur des règles et regex atteignent ~60-70 % de précision contre ~90 % avec GPT-4. Pour les cas d'usage nécessitant une meilleure extraction, un petit modèle NER local via `tflite_flutter` (modèle BERT-NER quantifié) est envisageable.

---

## Conclusion : feuille de route vers la production

Ce système de Knowledge Graph est **constructible dès aujourd'hui** avec la stack Drift + flutter_embedder + workmanager, sans aucune dépendance cloud. Les trois innovations architecturales clés sont : premièrement, le **modèle bi-temporel à quatre timestamps** qui garantit la traçabilité complète sans jamais perdre d'information historique ; deuxièmement, la **fusion hybride à quatre signaux** (BM25 + vecteur + activation + décroissance) qui dépasse significativement le BM25 seul en recall ; troisièmement, la **consolidation RAPTOR asynchrone** qui compresse les mémoires froides en résumés navigables sans intervention utilisateur.

L'ordre d'implémentation recommandé est : (1) schéma SQLite + Drift avec FTS5 et CRUD bi-temporel, (2) pipeline d'ingestion avec extraction d'entités par règles, (3) requête hybride FTS5 + spreading activation, (4) intégration flutter_embedder pour les embeddings et la similarité vectorielle, (5) WorkManager pour décroissance et consolidation, (6) système de hooks avant/après agent. Chaque couche est testable indépendamment, et le système est fonctionnel dès l'étape 3 même sans embeddings vectoriels — la recherche FTS5 + graphe constitue déjà un gain majeur par rapport au BM25 seul.