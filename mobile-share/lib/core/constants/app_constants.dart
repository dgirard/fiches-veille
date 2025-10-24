class AppConstants {
  // GitHub OAuth
  static const String githubClientId = 'YOUR_CLIENT_ID'; // À configurer via env
  static const String githubOAuthUrl = 'https://github.com/login/oauth/authorize';
  static const String githubTokenUrl = 'https://github.com/login/oauth/access_token';
  static const String githubApiBaseUrl = 'https://api.github.com';

  // App
  static const String appName = 'Mobile-Share';
  static const String deepLinkScheme = 'mobileshare';
  static const String oauthCallbackPath = 'oauth-callback';

  // Files
  static const String targetFileName = 'urls-to-process.md';

  // Storage keys
  static const String keyGithubToken = 'github_token';
  static const String keyGithubUsername = 'github_username';
  static const String keyGithubRepo = 'github_repo';
  static const String keyGithubBranch = 'github_branch';
  static const String keyTokenType = 'token_type';
}
