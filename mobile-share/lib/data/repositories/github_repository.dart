import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/github_config.dart';
import '../models/auth_token.dart';
import '../../core/constants/app_constants.dart';

class GitHubRepository {
  final http.Client _client;

  GitHubRepository({http.Client? client}) : _client = client ?? http.Client();

  Future<String?> getFileContent(
    GitHubConfig config,
    AuthToken token,
    String fileName,
  ) async {
    final url = Uri.parse(
      '${AppConstants.githubApiBaseUrl}/repos/${config.username}/${config.repository}/contents/$fileName?ref=${config.branch}',
    );

    final response = await _client.get(
      url,
      headers: {
        'Authorization': 'Bearer ${token.token}',
        'Accept': 'application/vnd.github.v3+json',
      },
    );

    if (response.statusCode == 404) {
      return null; // File doesn't exist
    }

    if (response.statusCode != 200) {
      throw Exception('Failed to fetch file: ${response.statusCode}');
    }

    final data = jsonDecode(response.body);
    final contentBase64 = data['content'] as String;
    final content = utf8.decode(base64.decode(contentBase64.replaceAll('\n', '')));

    return content;
  }

  Future<String?> getFileSha(
    GitHubConfig config,
    AuthToken token,
    String fileName,
  ) async {
    final url = Uri.parse(
      '${AppConstants.githubApiBaseUrl}/repos/${config.username}/${config.repository}/contents/$fileName?ref=${config.branch}',
    );

    final response = await _client.get(
      url,
      headers: {
        'Authorization': 'Bearer ${token.token}',
        'Accept': 'application/vnd.github.v3+json',
      },
    );

    if (response.statusCode == 404) return null;
    if (response.statusCode != 200) {
      throw Exception('Failed to fetch file SHA: ${response.statusCode}');
    }

    final data = jsonDecode(response.body);
    return data['sha'] as String;
  }

  Future<List<String>> checkDuplicates(
    GitHubConfig config,
    AuthToken token,
    List<String> urls,
  ) async {
    final content = await getFileContent(
      config,
      token,
      AppConstants.targetFileName,
    );

    if (content == null) return urls; // File doesn't exist, no duplicates

    final existingUrls = content.split('\n').where((line) => line.trim().isNotEmpty).toSet();

    return urls.where((url) => !existingUrls.contains(url)).toList();
  }

  Future<void> appendUrls(
    GitHubConfig config,
    AuthToken token,
    List<String> urls,
  ) async {
    if (urls.isEmpty) return;

    // Get current content and SHA
    final currentContent = await getFileContent(
      config,
      token,
      AppConstants.targetFileName,
    );
    final sha = await getFileSha(
      config,
      token,
      AppConstants.targetFileName,
    );

    // Build new content
    final newContent = currentContent != null
        ? '$currentContent\n${urls.join('\n')}\n'
        : '${urls.join('\n')}\n';

    final contentBase64 = base64.encode(utf8.encode(newContent));

    // Update file
    final url = Uri.parse(
      '${AppConstants.githubApiBaseUrl}/repos/${config.username}/${config.repository}/contents/${AppConstants.targetFileName}',
    );

    final body = jsonEncode({
      'message': 'Add URLs from mobile-share [${DateTime.now().toIso8601String()}]',
      'content': contentBase64,
      'branch': config.branch,
      if (sha != null) 'sha': sha,
    });

    final response = await _client.put(
      url,
      headers: {
        'Authorization': 'Bearer ${token.token}',
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json',
      },
      body: body,
    );

    if (response.statusCode != 200 && response.statusCode != 201) {
      throw Exception('Failed to update file: ${response.statusCode} ${response.body}');
    }
  }

  Future<Map<String, dynamic>> getUserInfo(AuthToken token) async {
    final url = Uri.parse('${AppConstants.githubApiBaseUrl}/user');

    final response = await _client.get(
      url,
      headers: {
        'Authorization': 'Bearer ${token.token}',
        'Accept': 'application/vnd.github.v3+json',
      },
    );

    if (response.statusCode != 200) {
      throw Exception('Failed to get user info: ${response.statusCode}');
    }

    return jsonDecode(response.body) as Map<String, dynamic>;
  }
}
