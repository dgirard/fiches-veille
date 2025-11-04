import 'package:flutter_test/flutter_test.dart';
import 'package:mobile_share/data/models/pending_url.dart';
import 'package:mobile_share/data/repositories/local_url_repository.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';

void main() {
  late LocalUrlRepository repository;

  setUpAll(() {
    // Initialize FFI for testing
    sqfliteFfiInit();
    databaseFactory = databaseFactoryFfi;
  });

  setUp(() async {
    repository = LocalUrlRepository();
    // Clear any existing data
    final urls = await repository.getAll();
    for (final url in urls) {
      if (url.id != null) {
        await repository.delete(url.id!);
      }
    }
  });

  PendingUrl createTestUrl(String url) {
    return PendingUrl(
      url: url,
      timestamp: DateTime.now(),
      synced: false,
    );
  }

  group('LocalUrlRepository', () {
    group('addUrl', () {
      test('should add a new URL successfully', () async {
        // Arrange
        final testUrl = createTestUrl('https://example.com/article1');

        // Act
        final id = await repository.addUrl(testUrl);

        // Assert
        expect(id, greaterThan(0));

        final urls = await repository.getAll();
        expect(urls.length, 1);
        expect(urls.first.url, testUrl.url);
        expect(urls.first.synced, false);
      });

      test('should ignore duplicate URL and return 0', () async {
        // Arrange
        final testUrl = createTestUrl('https://example.com/article1');
        await repository.addUrl(testUrl);

        // Act
        final id = await repository.addUrl(testUrl);

        // Assert
        expect(id, 0);

        final urls = await repository.getAll();
        expect(urls.length, 1);
      });
    });

    group('exists', () {
      test('should return true for existing URL', () async {
        // Arrange
        final testUrl = createTestUrl('https://example.com/article1');
        await repository.addUrl(testUrl);

        // Act
        final exists = await repository.exists(testUrl.url);

        // Assert
        expect(exists, true);
      });

      test('should return false for non-existing URL', () async {
        // Act
        final exists = await repository.exists('https://example.com/nonexistent');

        // Assert
        expect(exists, false);
      });
    });

    group('getAll', () {
      test('should return all URLs ordered by timestamp descending', () async {
        // Arrange
        await repository.addUrl(createTestUrl('https://example.com/article1'));
        await Future.delayed(const Duration(milliseconds: 10));
        await repository.addUrl(createTestUrl('https://example.com/article2'));
        await Future.delayed(const Duration(milliseconds: 10));
        await repository.addUrl(createTestUrl('https://example.com/article3'));

        // Act
        final urls = await repository.getAll();

        // Assert
        expect(urls.length, 3);
        expect(urls[0].url, 'https://example.com/article3'); // Most recent first
        expect(urls[1].url, 'https://example.com/article2');
        expect(urls[2].url, 'https://example.com/article1');
      });

      test('should return empty list when no URLs exist', () async {
        // Act
        final urls = await repository.getAll();

        // Assert
        expect(urls, isEmpty);
      });
    });

    group('getUnsynced', () {
      test('should return only unsynced URLs', () async {
        // Arrange
        await repository.addUrl(createTestUrl('https://example.com/article1'));
        await Future.delayed(const Duration(milliseconds: 10));
        await repository.addUrl(createTestUrl('https://example.com/article2'));
        await Future.delayed(const Duration(milliseconds: 10));
        await repository.addUrl(createTestUrl('https://example.com/article3'));

        final allUrls = await repository.getAll();

        // Find URLs by content to get their IDs
        final url1 = allUrls.firstWhere((u) => u.url == 'https://example.com/article1');
        final url2 = allUrls.firstWhere((u) => u.url == 'https://example.com/article2');

        // Mark first two as synced
        await repository.markAsSynced([url1.id!, url2.id!]);

        // Act
        final unsynced = await repository.getUnsynced();

        // Assert
        expect(unsynced.length, 1);
        expect(unsynced.first.url, 'https://example.com/article3');
        expect(unsynced.first.synced, false);
      });

      test('should return empty list when all URLs are synced', () async {
        // Arrange
        await repository.addUrl(createTestUrl('https://example.com/article1'));
        await repository.addUrl(createTestUrl('https://example.com/article2'));

        final allUrls = await repository.getAll();
        final ids = allUrls.map((url) => url.id!).toList();
        await repository.markAsSynced(ids);

        // Act
        final unsynced = await repository.getUnsynced();

        // Assert
        expect(unsynced, isEmpty);
      });
    });

    group('markAsSynced', () {
      test('should mark URLs as synced', () async {
        // Arrange
        await repository.addUrl(createTestUrl('https://example.com/article1'));
        await repository.addUrl(createTestUrl('https://example.com/article2'));

        final allUrls = await repository.getAll();
        final ids = allUrls.map((url) => url.id!).toList();

        // Act
        final updated = await repository.markAsSynced(ids);

        // Assert
        expect(updated, 2);

        final urls = await repository.getAll();
        expect(urls.every((url) => url.synced), true);
      });

      test('should return 0 when marking non-existent IDs', () async {
        // Act
        final updated = await repository.markAsSynced([999, 1000]);

        // Assert
        expect(updated, 0);
      });
    });

    group('delete', () {
      test('should delete a URL by ID', () async {
        // Arrange
        await repository.addUrl(createTestUrl('https://example.com/article1'));
        await repository.addUrl(createTestUrl('https://example.com/article2'));

        final allUrls = await repository.getAll();
        final idToDelete = allUrls.first.id!;

        // Act
        final deleted = await repository.delete(idToDelete);

        // Assert
        expect(deleted, 1);

        final urls = await repository.getAll();
        expect(urls.length, 1);
      });

      test('should return 0 when deleting non-existent ID', () async {
        // Act
        final deleted = await repository.delete(999);

        // Assert
        expect(deleted, 0);
      });
    });

    group('count', () {
      test('should return correct count of URLs', () async {
        // Arrange
        await repository.addUrl(createTestUrl('https://example.com/article1'));
        await repository.addUrl(createTestUrl('https://example.com/article2'));
        await repository.addUrl(createTestUrl('https://example.com/article3'));

        // Act
        final count = await repository.count();

        // Assert
        expect(count, 3);
      });

      test('should return 0 when database is empty', () async {
        // Act
        final count = await repository.count();

        // Assert
        expect(count, 0);
      });
    });
  });
}
