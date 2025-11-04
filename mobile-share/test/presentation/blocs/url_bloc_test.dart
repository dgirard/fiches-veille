import 'package:bloc_test/bloc_test.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mobile_share/data/models/pending_url.dart';
import 'package:mobile_share/data/repositories/local_url_repository.dart';
import 'package:mobile_share/presentation/blocs/url/url_bloc.dart';
import 'package:mobile_share/presentation/blocs/url/url_event.dart';
import 'package:mobile_share/presentation/blocs/url/url_state.dart';
import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';

import 'url_bloc_test.mocks.dart';

@GenerateMocks([LocalUrlRepository])
void main() {
  late UrlBloc bloc;
  late MockLocalUrlRepository mockRepository;

  setUp(() {
    mockRepository = MockLocalUrlRepository();
    bloc = UrlBloc(mockRepository);
  });

  tearDown(() {
    bloc.close();
  });

  group('UrlBloc', () {
    test('initial state is UrlsInitial', () {
      expect(bloc.state, equals(UrlsInitial()));
    });

    group('LoadUrls', () {
      final testUrls = [
        PendingUrl(
          id: 1,
          url: 'https://example.com/article1',
          timestamp: DateTime.now(),
          synced: false,
        ),
        PendingUrl(
          id: 2,
          url: 'https://example.com/article2',
          timestamp: DateTime.now(),
          synced: true,
        ),
      ];

      blocTest<UrlBloc, UrlState>(
        'emits [UrlsLoading, UrlsLoaded] when LoadUrls succeeds',
        build: () {
          when(mockRepository.getAll()).thenAnswer((_) async => testUrls);
          return bloc;
        },
        act: (bloc) => bloc.add(LoadUrls()),
        expect: () => [
          UrlsLoading(),
          UrlsLoaded(testUrls),
        ],
        verify: (_) {
          verify(mockRepository.getAll()).called(1);
        },
      );

      blocTest<UrlBloc, UrlState>(
        'emits [UrlsLoading, UrlError] when LoadUrls fails',
        build: () {
          when(mockRepository.getAll()).thenThrow(Exception('Database error'));
          return bloc;
        },
        act: (bloc) => bloc.add(LoadUrls()),
        expect: () => [
          UrlsLoading(),
          const UrlError('Failed to load URLs: Exception: Database error'),
        ],
      );

      blocTest<UrlBloc, UrlState>(
        'emits [UrlsLoading, UrlsLoaded] with empty list when no URLs exist',
        build: () {
          when(mockRepository.getAll()).thenAnswer((_) async => []);
          return bloc;
        },
        act: (bloc) => bloc.add(LoadUrls()),
        expect: () => [
          UrlsLoading(),
          const UrlsLoaded([]),
        ],
      );
    });

    group('AddUrl', () {
      const validUrl = 'https://example.com/article';

      blocTest<UrlBloc, UrlState>(
        'emits [UrlAdded, UrlsLoading, UrlsLoaded] when URL is added successfully',
        build: () {
          when(mockRepository.exists(validUrl)).thenAnswer((_) async => false);
          when(mockRepository.addUrl(any)).thenAnswer((_) async => 1);
          when(mockRepository.getAll()).thenAnswer((_) async => [
                PendingUrl(
                  id: 1,
                  url: validUrl,
                  timestamp: DateTime.now(),
                  synced: false,
                ),
              ]);
          return bloc;
        },
        act: (bloc) => bloc.add(const AddUrl(validUrl)),
        expect: () => [
          isA<UrlAdded>()
              .having((state) => state.url.url, 'url', validUrl)
              .having((state) => state.url.id, 'id', 1),
          UrlsLoading(),
          isA<UrlsLoaded>().having((state) => state.urls.length, 'count', 1),
        ],
        verify: (_) {
          verify(mockRepository.exists(validUrl)).called(1);
          verify(mockRepository.addUrl(any)).called(1);
          verify(mockRepository.getAll()).called(1);
        },
      );

      blocTest<UrlBloc, UrlState>(
        'emits [UrlError] when URL format is invalid',
        build: () => bloc,
        act: (bloc) => bloc.add(const AddUrl('not-a-valid-url')),
        expect: () => [
          const UrlError('Invalid URL format'),
        ],
        verify: (_) {
          verifyNever(mockRepository.exists(any));
          verifyNever(mockRepository.addUrl(any));
        },
      );

      blocTest<UrlBloc, UrlState>(
        'emits nothing when URL already exists (silent duplicate)',
        build: () {
          when(mockRepository.exists(validUrl)).thenAnswer((_) async => true);
          return bloc;
        },
        act: (bloc) => bloc.add(const AddUrl(validUrl)),
        expect: () => [],
        verify: (_) {
          verify(mockRepository.exists(validUrl)).called(1);
          verifyNever(mockRepository.addUrl(any));
        },
      );

      blocTest<UrlBloc, UrlState>(
        'emits [UrlError] when repository throws exception',
        build: () {
          when(mockRepository.exists(validUrl)).thenAnswer((_) async => false);
          when(mockRepository.addUrl(any)).thenThrow(Exception('Database error'));
          return bloc;
        },
        act: (bloc) => bloc.add(const AddUrl(validUrl)),
        expect: () => [
          const UrlError('Failed to add URL: Exception: Database error'),
        ],
      );

      blocTest<UrlBloc, UrlState>(
        'accepts URLs with http scheme',
        build: () {
          when(mockRepository.exists(any)).thenAnswer((_) async => false);
          when(mockRepository.addUrl(any)).thenAnswer((_) async => 1);
          when(mockRepository.getAll()).thenAnswer((_) async => []);
          return bloc;
        },
        act: (bloc) => bloc.add(const AddUrl('http://example.com/article')),
        expect: () => [
          isA<UrlAdded>(),
          UrlsLoading(),
          isA<UrlsLoaded>(),
        ],
      );

      blocTest<UrlBloc, UrlState>(
        'accepts URLs with www subdomain',
        build: () {
          when(mockRepository.exists(any)).thenAnswer((_) async => false);
          when(mockRepository.addUrl(any)).thenAnswer((_) async => 1);
          when(mockRepository.getAll()).thenAnswer((_) async => []);
          return bloc;
        },
        act: (bloc) => bloc.add(const AddUrl('https://www.example.com/article')),
        expect: () => [
          isA<UrlAdded>(),
          UrlsLoading(),
          isA<UrlsLoaded>(),
        ],
      );
    });

    group('DeleteUrl', () {
      blocTest<UrlBloc, UrlState>(
        'emits [UrlDeleted, UrlsLoading, UrlsLoaded] when URL is deleted successfully',
        build: () {
          when(mockRepository.delete(1)).thenAnswer((_) async => 1);
          when(mockRepository.getAll()).thenAnswer((_) async => []);
          return bloc;
        },
        act: (bloc) => bloc.add(const DeleteUrl(1)),
        expect: () => [
          const UrlDeleted(1),
          UrlsLoading(),
          const UrlsLoaded([]),
        ],
        verify: (_) {
          verify(mockRepository.delete(1)).called(1);
          verify(mockRepository.getAll()).called(1);
        },
      );

      blocTest<UrlBloc, UrlState>(
        'emits [UrlError] when repository throws exception',
        build: () {
          when(mockRepository.delete(1)).thenThrow(Exception('Database error'));
          return bloc;
        },
        act: (bloc) => bloc.add(const DeleteUrl(1)),
        expect: () => [
          const UrlError('Failed to delete URL: Exception: Database error'),
        ],
      );
    });

    group('MarkUrlsSynced', () {
      blocTest<UrlBloc, UrlState>(
        'emits [UrlsLoading, UrlsLoaded] when URLs are marked as synced successfully',
        build: () {
          when(mockRepository.markAsSynced([1, 2])).thenAnswer((_) async => 2);
          when(mockRepository.getAll()).thenAnswer((_) async => []);
          return bloc;
        },
        act: (bloc) => bloc.add(const MarkUrlsSynced([1, 2])),
        expect: () => [
          UrlsLoading(),
          const UrlsLoaded([]),
        ],
        verify: (_) {
          verify(mockRepository.markAsSynced([1, 2])).called(1);
          verify(mockRepository.getAll()).called(1);
        },
      );

      blocTest<UrlBloc, UrlState>(
        'emits [UrlError] when repository throws exception',
        build: () {
          when(mockRepository.markAsSynced([1, 2]))
              .thenThrow(Exception('Database error'));
          return bloc;
        },
        act: (bloc) => bloc.add(const MarkUrlsSynced([1, 2])),
        expect: () => [
          const UrlError('Failed to mark URLs as synced: Exception: Database error'),
        ],
      );

      blocTest<UrlBloc, UrlState>(
        'handles empty ID list',
        build: () {
          when(mockRepository.markAsSynced([])).thenAnswer((_) async => 0);
          when(mockRepository.getAll()).thenAnswer((_) async => []);
          return bloc;
        },
        act: (bloc) => bloc.add(const MarkUrlsSynced([])),
        expect: () => [
          UrlsLoading(),
          const UrlsLoaded([]),
        ],
      );
    });
  });
}
