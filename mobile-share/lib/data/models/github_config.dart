import 'package:equatable/equatable.dart';

class GitHubConfig extends Equatable {
  final String username;
  final String repository;
  final String branch;

  const GitHubConfig({
    required this.username,
    required this.repository,
    this.branch = 'main',
  });

  bool get isValid =>
      username.isNotEmpty && repository.isNotEmpty && branch.isNotEmpty;

  Map<String, dynamic> toMap() {
    return {
      'username': username,
      'repository': repository,
      'branch': branch,
    };
  }

  factory GitHubConfig.fromMap(Map<String, dynamic> map) {
    return GitHubConfig(
      username: map['username'] as String,
      repository: map['repository'] as String,
      branch: map['branch'] as String? ?? 'main',
    );
  }

  @override
  List<Object?> get props => [username, repository, branch];
}
