import 'package:flutter/material.dart';
import 'core/theme/app_theme.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // TODO: Initialize dependencies (repositories, BLoCs)

  runApp(const MobileShareApp());
}

class MobileShareApp extends StatelessWidget {
  const MobileShareApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mobile-Share',
      theme: AppTheme.lightTheme,
      home: const Scaffold(
        body: Center(
          child: Text(
            'Mobile-Share - Setup Complete ✓',
            style: TextStyle(fontSize: 20),
          ),
        ),
      ),
    );
  }
}
