import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'dart:convert';
import '../models/github_config.dart';
import '../models/auth_token.dart';
import '../../core/constants/app_constants.dart';

class SettingsRepository {
  final FlutterSecureStorage _storage = const FlutterSecureStorage();

  // GitHub Config
  Future<void> saveConfig(GitHubConfig config) async {
    await _storage.write(
      key: AppConstants.keyGithubUsername,
      value: config.username,
    );
    await _storage.write(
      key: AppConstants.keyGithubRepo,
      value: config.repository,
    );
    await _storage.write(
      key: AppConstants.keyGithubBranch,
      value: config.branch,
    );
  }

  Future<GitHubConfig?> loadConfig() async {
    final username = await _storage.read(key: AppConstants.keyGithubUsername);
    final repo = await _storage.read(key: AppConstants.keyGithubRepo);
    final branch = await _storage.read(key: AppConstants.keyGithubBranch);

    if (username == null || repo == null) return null;

    return GitHubConfig(
      username: username,
      repository: repo,
      branch: branch ?? 'main',
    );
  }

  // Auth Token
  Future<void> saveToken(AuthToken token) async {
    final tokenMap = token.toMap();
    await _storage.write(
      key: AppConstants.keyGithubToken,
      value: jsonEncode(tokenMap),
    );
  }

  Future<AuthToken?> loadToken() async {
    final tokenJson = await _storage.read(key: AppConstants.keyGithubToken);
    if (tokenJson == null) return null;

    final tokenMap = jsonDecode(tokenJson) as Map<String, dynamic>;
    return AuthToken.fromMap(tokenMap);
  }

  Future<void> clearToken() async {
    await _storage.delete(key: AppConstants.keyGithubToken);
  }

  Future<void> clearAll() async {
    await _storage.deleteAll();
  }
}
