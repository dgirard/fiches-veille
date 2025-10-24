// Basic widget test for Mobile-Share

import 'package:flutter_test/flutter_test.dart';

import 'package:mobile_share/main.dart';

void main() {
  testWidgets('App loads successfully', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const MobileShareApp());

    // Verify that setup complete message is displayed
    expect(find.text('Mobile-Share - Setup Complete ✓'), findsOneWidget);
  });
}
