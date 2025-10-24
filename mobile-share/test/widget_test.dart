// Basic widget test for Mobile-Share

import 'package:flutter_test/flutter_test.dart';

import 'package:mobile_share/main.dart';
import 'package:mobile_share/data/repositories/local_url_repository.dart';
import 'package:mobile_share/data/repositories/settings_repository.dart';
import 'package:mobile_share/data/repositories/github_repository.dart';

void main() {
  testWidgets('App loads successfully', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(MobileShareApp(
      localUrlRepository: LocalUrlRepository(),
      settingsRepository: SettingsRepository(),
      githubRepository: GitHubRepository(),
    ));

    // Verify that the app title is displayed
    expect(find.text('Mobile-Share'), findsOneWidget);
  });
}
