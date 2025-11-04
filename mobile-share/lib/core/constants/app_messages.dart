/// User-facing messages and help texts
class AppMessages {
  // Success messages
  static const String urlSavedSuccess = 'URL saved successfully';
  static const String urlDeletedSuccess = 'URL deleted';
  static const String settingsSavedSuccess = 'Settings saved successfully';
  static const String syncSuccess = 'URLs synced to GitHub';
  static const String authSuccess = 'Authentication successful';

  // Info messages
  static const String noUnsyncedUrls = 'All URLs are synced';
  static const String emptyList = 'No URLs saved yet';
  static const String syncInProgress = 'Synchronizing with GitHub...';

  // Validation messages
  static const String usernameRequired = 'GitHub username is required';
  static const String repositoryRequired = 'Repository name is required';
  static const String tokenRequired = 'GitHub token is required';
  static const String urlInvalidFormat = 'Please enter a valid URL';

  // Help texts
  static const String usernameHelp = 'Your GitHub username';
  static const String repositoryHelp = 'Repository name without owner';
  static const String branchHelp = 'Branch name (default: main)';
  static const String tokenHelp = 'Personal Access Token with repo permissions';

  // Instructions
  static const String tokenInstructions = '''
To create a Personal Access Token:

1. Go to GitHub Settings > Developer settings > Personal access tokens
2. Click "Generate new token (classic)"
3. Give it a name (e.g., "Mobile-Share")
4. Select "repo" scope for repository access
5. Click "Generate token"
6. Copy the token and paste it here

⚠️ Keep your token secure and never share it!
''';

  static const String firstTimeSetup = '''
Welcome to Mobile-Share!

Before you can save URLs, please configure your GitHub settings:

1. Enter your GitHub username
2. Enter the repository name where URLs will be saved
3. Enter your Personal Access Token
4. (Optional) Change the branch name

URLs will be saved to urls-to-process.md in the root of your repository.
''';

  // Empty state messages
  static const String emptyStateTitle = 'No URLs yet';
  static const String emptyStateSubtitle =
      'Share a link from any app to save it here';
  static const String emptyStateAction = 'Use Android Share menu to add URLs';
}
