import 'package:flutter_test/flutter_test.dart';
import 'package:mobile_share/data/models/auth_token.dart';
import 'package:mobile_share/data/models/github_config.dart';
import 'package:mobile_share/data/repositories/settings_repository.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late SettingsRepository repository;

  setUp(() {
    FlutterSecureStorage.setMockInitialValues({});
    repository = SettingsRepository();
  });

  group('SettingsRepository - Config', () {
    test('should save and load GitHub config successfully', () async {
      // Arrange
      const config = GitHubConfig(
        username: 'testuser',
        repository: 'testrepo',
        branch: 'main',
      );

      // Act
      await repository.saveConfig(config);
      final loadedConfig = await repository.loadConfig();

      // Assert
      expect(loadedConfig, isNotNull);
      expect(loadedConfig!.username, 'testuser');
      expect(loadedConfig.repository, 'testrepo');
      expect(loadedConfig.branch, 'main');
    });

    test('should use default branch when not specified', () async {
      // Arrange
      const config = GitHubConfig(
        username: 'testuser',
        repository: 'testrepo',
        branch: 'develop',
      );

      // Act
      await repository.saveConfig(config);
      final loadedConfig = await repository.loadConfig();

      // Assert
      expect(loadedConfig, isNotNull);
      expect(loadedConfig!.branch, 'develop');
    });

    test('should return null when config does not exist', () async {
      // Act
      final loadedConfig = await repository.loadConfig();

      // Assert
      expect(loadedConfig, isNull);
    });
  });

  group('SettingsRepository - Token', () {
    test('should save and load PAT token successfully', () async {
      // Arrange
      const token = AuthToken(
        token: 'ghp_test123456',
        type: TokenType.pat,
      );

      // Act
      await repository.saveToken(token);
      final loadedToken = await repository.loadToken();

      // Assert
      expect(loadedToken, isNotNull);
      expect(loadedToken!.token, 'ghp_test123456');
      expect(loadedToken.type, TokenType.pat);
      expect(loadedToken.isExpired, false);
    });

    test('should save and load OAuth token with expiration', () async {
      // Arrange
      final expiresAt = DateTime.now().add(const Duration(hours: 1));
      final token = AuthToken(
        token: 'gho_test123456',
        type: TokenType.oauth,
        expiresAt: expiresAt,
      );

      // Act
      await repository.saveToken(token);
      final loadedToken = await repository.loadToken();

      // Assert
      expect(loadedToken, isNotNull);
      expect(loadedToken!.token, 'gho_test123456');
      expect(loadedToken.type, TokenType.oauth);
      expect(loadedToken.expiresAt, isNotNull);
      expect(loadedToken.isExpired, false);
    });

    test('should return null when token does not exist', () async {
      // Act
      final loadedToken = await repository.loadToken();

      // Assert
      expect(loadedToken, isNull);
    });

    test('should clear token successfully', () async {
      // Arrange
      const token = AuthToken(
        token: 'ghp_test123456',
        type: TokenType.pat,
      );
      await repository.saveToken(token);

      // Act
      await repository.clearToken();
      final loadedToken = await repository.loadToken();

      // Assert
      expect(loadedToken, isNull);
    });
  });

  group('SettingsRepository - ClearAll', () {
    test('should clear all data successfully', () async {
      // Arrange
      const config = GitHubConfig(
        username: 'testuser',
        repository: 'testrepo',
        branch: 'main',
      );
      const token = AuthToken(
        token: 'ghp_test123456',
        type: TokenType.pat,
      );

      await repository.saveConfig(config);
      await repository.saveToken(token);

      // Act
      await repository.clearAll();

      // Assert
      final loadedConfig = await repository.loadConfig();
      final loadedToken = await repository.loadToken();

      expect(loadedConfig, isNull);
      expect(loadedToken, isNull);
    });
  });
}
