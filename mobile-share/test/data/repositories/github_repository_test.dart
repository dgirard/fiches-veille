import 'dart:convert';
import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;
import 'package:mobile_share/data/models/auth_token.dart';
import 'package:mobile_share/data/models/github_config.dart';
import 'package:mobile_share/data/repositories/github_repository.dart';
import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';

import 'github_repository_test.mocks.dart';

@GenerateMocks([http.Client])
void main() {
  late GitHubRepository repository;
  late MockClient mockClient;
  late GitHubConfig testConfig;
  late AuthToken testToken;

  setUp(() {
    mockClient = MockClient();
    repository = GitHubRepository(client: mockClient);
    testConfig = const GitHubConfig(
      username: 'testuser',
      repository: 'testrepo',
      branch: 'main',
    );
    testToken = const AuthToken(
      token: 'ghp_test123456',
      type: TokenType.pat,
    );
  });

  group('GitHubRepository - getFileContent', () {
    test('should return file content successfully', () async {
      // Arrange
      const fileContent = 'https://example.com/url1\nhttps://example.com/url2';
      final contentBase64 = base64.encode(utf8.encode(fileContent));
      final responseBody = jsonEncode({
        'content': contentBase64,
        'sha': 'abc123',
      });

      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response(responseBody, 200));

      // Act
      final content = await repository.getFileContent(
        testConfig,
        testToken,
        'urls-to-process.md',
      );

      // Assert
      expect(content, fileContent);
      verify(mockClient.get(
        argThat(predicate((Uri uri) =>
            uri.path.contains('testuser') &&
            uri.path.contains('testrepo') &&
            uri.path.contains('urls-to-process.md'))),
        headers: argThat(
          contains('Authorization'),
          named: 'headers',
        ),
      )).called(1);
    });

    test('should return null when file does not exist (404)', () async {
      // Arrange
      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response('Not Found', 404));

      // Act
      final content = await repository.getFileContent(
        testConfig,
        testToken,
        'urls-to-process.md',
      );

      // Assert
      expect(content, isNull);
    });

    test('should throw exception on API error', () async {
      // Arrange
      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response('Server Error', 500));

      // Act & Assert
      expect(
        () => repository.getFileContent(
          testConfig,
          testToken,
          'urls-to-process.md',
        ),
        throwsException,
      );
    });
  });

  group('GitHubRepository - getFileSha', () {
    test('should return file SHA successfully', () async {
      // Arrange
      final responseBody = jsonEncode({
        'sha': 'abc123def456',
        'content': 'somebase64content',
      });

      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response(responseBody, 200));

      // Act
      final sha = await repository.getFileSha(
        testConfig,
        testToken,
        'urls-to-process.md',
      );

      // Assert
      expect(sha, 'abc123def456');
    });

    test('should return null when file does not exist (404)', () async {
      // Arrange
      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response('Not Found', 404));

      // Act
      final sha = await repository.getFileSha(
        testConfig,
        testToken,
        'urls-to-process.md',
      );

      // Assert
      expect(sha, isNull);
    });
  });

  group('GitHubRepository - checkDuplicates', () {
    test('should filter out duplicate URLs', () async {
      // Arrange
      const existingContent = 'https://example.com/url1\nhttps://example.com/url2\n';
      final contentBase64 = base64.encode(utf8.encode(existingContent));
      final responseBody = jsonEncode({
        'content': contentBase64,
        'sha': 'abc123',
      });

      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response(responseBody, 200));

      final urlsToCheck = [
        'https://example.com/url1', // duplicate
        'https://example.com/url3', // new
        'https://example.com/url2', // duplicate
        'https://example.com/url4', // new
      ];

      // Act
      final newUrls = await repository.checkDuplicates(
        testConfig,
        testToken,
        urlsToCheck,
      );

      // Assert
      expect(newUrls.length, 2);
      expect(newUrls, contains('https://example.com/url3'));
      expect(newUrls, contains('https://example.com/url4'));
      expect(newUrls, isNot(contains('https://example.com/url1')));
      expect(newUrls, isNot(contains('https://example.com/url2')));
    });

    test('should return all URLs when file does not exist', () async {
      // Arrange
      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response('Not Found', 404));

      final urlsToCheck = [
        'https://example.com/url1',
        'https://example.com/url2',
      ];

      // Act
      final newUrls = await repository.checkDuplicates(
        testConfig,
        testToken,
        urlsToCheck,
      );

      // Assert
      expect(newUrls.length, 2);
      expect(newUrls, equals(urlsToCheck));
    });
  });

  group('GitHubRepository - appendUrls', () {
    test('should append URLs to existing file', () async {
      // Arrange
      const existingContent = 'https://example.com/url1\n';
      final contentBase64 = base64.encode(utf8.encode(existingContent));
      final getResponseBody = jsonEncode({
        'content': contentBase64,
        'sha': 'abc123',
      });

      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response(getResponseBody, 200));

      when(mockClient.put(
        any,
        headers: anyNamed('headers'),
        body: anyNamed('body'),
      )).thenAnswer((_) async => http.Response('{}', 200));

      final urlsToAppend = [
        'https://example.com/url2',
        'https://example.com/url3',
      ];

      // Act
      await repository.appendUrls(
        testConfig,
        testToken,
        urlsToAppend,
      );

      // Assert
      final captured = verify(mockClient.put(
        captureAny,
        headers: captureAnyNamed('headers'),
        body: captureAnyNamed('body'),
      )).captured;

      final body = jsonDecode(captured[2] as String);
      expect(body['message'], contains('Add URLs from mobile-share'));
      expect(body['branch'], 'main');
      expect(body['sha'], 'abc123');

      final decodedContent = utf8.decode(base64.decode(body['content']));
      expect(decodedContent, contains('https://example.com/url1'));
      expect(decodedContent, contains('https://example.com/url2'));
      expect(decodedContent, contains('https://example.com/url3'));
    });

    test('should create new file when file does not exist', () async {
      // Arrange
      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response('Not Found', 404));

      when(mockClient.put(
        any,
        headers: anyNamed('headers'),
        body: anyNamed('body'),
      )).thenAnswer((_) async => http.Response('{}', 201));

      final urlsToAppend = [
        'https://example.com/url1',
        'https://example.com/url2',
      ];

      // Act
      await repository.appendUrls(
        testConfig,
        testToken,
        urlsToAppend,
      );

      // Assert
      final captured = verify(mockClient.put(
        captureAny,
        headers: captureAnyNamed('headers'),
        body: captureAnyNamed('body'),
      )).captured;

      final body = jsonDecode(captured[2] as String);
      expect(body.containsKey('sha'), false); // No SHA for new file

      final decodedContent = utf8.decode(base64.decode(body['content']));
      expect(decodedContent, contains('https://example.com/url1'));
      expect(decodedContent, contains('https://example.com/url2'));
    });

    test('should do nothing when URL list is empty', () async {
      // Act
      await repository.appendUrls(
        testConfig,
        testToken,
        [],
      );

      // Assert
      verifyNever(mockClient.get(any, headers: anyNamed('headers')));
      verifyNever(mockClient.put(
        any,
        headers: anyNamed('headers'),
        body: anyNamed('body'),
      ));
    });

    test('should throw exception on PUT failure', () async {
      // Arrange
      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response('Not Found', 404));

      when(mockClient.put(
        any,
        headers: anyNamed('headers'),
        body: anyNamed('body'),
      )).thenAnswer((_) async => http.Response('Error', 500));

      // Act & Assert
      expect(
        () => repository.appendUrls(
          testConfig,
          testToken,
          ['https://example.com/url1'],
        ),
        throwsException,
      );
    });
  });

  group('GitHubRepository - getUserInfo', () {
    test('should return user info successfully', () async {
      // Arrange
      final responseBody = jsonEncode({
        'login': 'testuser',
        'name': 'Test User',
        'email': 'test@example.com',
      });

      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response(responseBody, 200));

      // Act
      final userInfo = await repository.getUserInfo(testToken);

      // Assert
      expect(userInfo['login'], 'testuser');
      expect(userInfo['name'], 'Test User');
      expect(userInfo['email'], 'test@example.com');
    });

    test('should throw exception on API error', () async {
      // Arrange
      when(mockClient.get(
        any,
        headers: anyNamed('headers'),
      )).thenAnswer((_) async => http.Response('Unauthorized', 401));

      // Act & Assert
      expect(
        () => repository.getUserInfo(testToken),
        throwsException,
      );
    });
  });
}
