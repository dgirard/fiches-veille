import 'package:sqflite/sqflite.dart';
import '../datasources/local_database.dart';
import '../models/pending_url.dart';

class LocalUrlRepository {
  final LocalDatabase _db = LocalDatabase();

  Future<int> addUrl(PendingUrl url) async {
    final db = await _db.database;
    return await db.insert(
      'pending_urls',
      url.toMap(),
      conflictAlgorithm: ConflictAlgorithm.ignore,
    );
  }

  Future<bool> exists(String url) async {
    final db = await _db.database;
    final result = await db.query(
      'pending_urls',
      where: 'url = ?',
      whereArgs: [url],
    );
    return result.isNotEmpty;
  }

  Future<List<PendingUrl>> getAll() async {
    final db = await _db.database;
    final result = await db.query(
      'pending_urls',
      orderBy: 'timestamp DESC',
    );
    return result.map((map) => PendingUrl.fromMap(map)).toList();
  }

  Future<List<PendingUrl>> getUnsynced() async {
    final db = await _db.database;
    final result = await db.query(
      'pending_urls',
      where: 'synced = ?',
      whereArgs: [0],
      orderBy: 'timestamp ASC',
    );
    return result.map((map) => PendingUrl.fromMap(map)).toList();
  }

  Future<int> markAsSynced(List<int> ids) async {
    final db = await _db.database;
    return await db.update(
      'pending_urls',
      {'synced': 1},
      where: 'id IN (${ids.join(',')})',
    );
  }

  Future<int> delete(int id) async {
    final db = await _db.database;
    return await db.delete(
      'pending_urls',
      where: 'id = ?',
      whereArgs: [id],
    );
  }

  Future<int> count() async {
    final db = await _db.database;
    final result = await db.rawQuery('SELECT COUNT(*) FROM pending_urls');
    return Sqflite.firstIntValue(result) ?? 0;
  }
}
