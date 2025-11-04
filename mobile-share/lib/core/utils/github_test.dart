import 'dart:convert';
import 'package:http/http.dart' as http;

/// Test script to verify GitHub token and repository access
/// Run with: flutter run lib/core/utils/github_test.dart
void main() async {
  print('=== GitHub Token & Repository Tester ===\n');

  // TODO: Replace these with your actual values
  const token = 'YOUR_GITHUB_TOKEN_HERE';
  const username = 'YOUR_USERNAME_HERE';
  const repository = 'YOUR_REPO_HERE';

  print('Testing with:');
  print('Username: $username');
  print('Repository: $repository');
  print('Token: ${token.substring(0, 10)}...\n');

  final client = http.Client();

  try {
    // Test 1: Verify token works
    print('Test 1: Verifying token...');
    final userResponse = await client.get(
      Uri.parse('https://api.github.com/user'),
      headers: {
        'Authorization': 'Bearer $token',
        'Accept': 'application/vnd.github.v3+json',
      },
    );

    if (userResponse.statusCode == 200) {
      final userData = jsonDecode(userResponse.body);
      print('✓ Token is valid');
      print('  Authenticated as: ${userData['login']}');
      print('  Name: ${userData['name']}');
    } else {
      print('✗ Token verification failed: ${userResponse.statusCode}');
      print('  Response: ${userResponse.body}');
      return;
    }

    print('');

    // Test 2: Check repository access
    print('Test 2: Checking repository access...');
    final repoResponse = await client.get(
      Uri.parse('https://api.github.com/repos/$username/$repository'),
      headers: {
        'Authorization': 'Bearer $token',
        'Accept': 'application/vnd.github.v3+json',
      },
    );

    if (repoResponse.statusCode == 200) {
      final repoData = jsonDecode(repoResponse.body);
      print('✓ Repository is accessible');
      print('  Full name: ${repoData['full_name']}');
      print('  Private: ${repoData['private']}');
      print('  Default branch: ${repoData['default_branch']}');
      print('  Permissions:');
      final permissions = repoData['permissions'] as Map<String, dynamic>;
      print('    - Admin: ${permissions['admin']}');
      print('    - Push: ${permissions['push']}');
      print('    - Pull: ${permissions['pull']}');
    } else if (repoResponse.statusCode == 404) {
      print('✗ Repository not found');
      print('  Make sure the repository name is correct: $username/$repository');
    } else if (repoResponse.statusCode == 403) {
      print('✗ Access forbidden');
      print('  Your token does not have permission to access this repository');
      print('  Make sure your token has the "repo" scope');
    } else {
      print('✗ Repository check failed: ${repoResponse.statusCode}');
      print('  Response: ${repoResponse.body}');
    }

    print('');

    // Test 3: Check token scopes
    print('Test 3: Checking token scopes...');
    final scopeResponse = await client.get(
      Uri.parse('https://api.github.com/user'),
      headers: {
        'Authorization': 'Bearer $token',
        'Accept': 'application/vnd.github.v3+json',
      },
    );

    final scopes = scopeResponse.headers['x-oauth-scopes'] ?? 'none';
    print('Token scopes: $scopes');

    if (scopes.contains('repo')) {
      print('✓ Token has "repo" scope');
    } else {
      print('✗ Token is missing "repo" scope!');
      print('  You need to create a new token with "repo" scope');
    }

    print('');

    // Test 4: Try to access the target file
    print('Test 4: Checking target file (urls-to-process.md)...');
    final fileResponse = await client.get(
      Uri.parse('https://api.github.com/repos/$username/$repository/contents/urls-to-process.md'),
      headers: {
        'Authorization': 'Bearer $token',
        'Accept': 'application/vnd.github.v3+json',
      },
    );

    if (fileResponse.statusCode == 200) {
      print('✓ File exists and is accessible');
      final fileData = jsonDecode(fileResponse.body);
      print('  Size: ${fileData['size']} bytes');
      print('  SHA: ${fileData['sha']}');
    } else if (fileResponse.statusCode == 404) {
      print('⚠ File does not exist yet (this is OK, it will be created)');
    } else {
      print('✗ Cannot access file: ${fileResponse.statusCode}');
      print('  Response: ${fileResponse.body}');
    }

    print('\n=== All tests completed ===');

  } catch (e) {
    print('✗ Error: $e');
  } finally {
    client.close();
  }
}
