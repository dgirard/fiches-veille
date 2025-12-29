import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'core/theme/app_theme.dart';
import 'data/repositories/local_url_repository.dart';
import 'data/repositories/settings_repository.dart';
import 'data/repositories/github_repository.dart';
import 'presentation/blocs/settings/settings_bloc.dart';
import 'presentation/blocs/auth/auth_bloc.dart';
import 'presentation/blocs/url/url_bloc.dart';
import 'presentation/blocs/sync/sync_bloc.dart';
import 'presentation/screens/url_list_screen.dart';
import 'services/share_receiver_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Initialize repositories
  final localUrlRepository = LocalUrlRepository();
  final settingsRepository = SettingsRepository();
  final githubRepository = GitHubRepository();

  runApp(MobileShareApp(
    localUrlRepository: localUrlRepository,
    settingsRepository: settingsRepository,
    githubRepository: githubRepository,
  ));
}

class MobileShareApp extends StatelessWidget {
  final LocalUrlRepository localUrlRepository;
  final SettingsRepository settingsRepository;
  final GitHubRepository githubRepository;

  const MobileShareApp({
    super.key,
    required this.localUrlRepository,
    required this.settingsRepository,
    required this.githubRepository,
  });

  @override
  Widget build(BuildContext context) {
    return MultiRepositoryProvider(
      providers: [
        RepositoryProvider.value(value: localUrlRepository),
        RepositoryProvider.value(value: settingsRepository),
        RepositoryProvider.value(value: githubRepository),
      ],
      child: MultiBlocProvider(
        providers: [
          BlocProvider(
            create: (context) => SettingsBloc(settingsRepository),
          ),
          BlocProvider(
            create: (context) => AuthBloc(settingsRepository, githubRepository),
          ),
          BlocProvider(
            create: (context) => UrlBloc(localUrlRepository),
          ),
          BlocProvider(
            create: (context) => SyncBloc(
              localUrlRepository,
              githubRepository,
              settingsRepository,
              context.read<UrlBloc>(),
            ),
          ),
        ],
        child: Builder(
          builder: (context) {
            // Initialize share receiver service after BLoC providers are available
            ShareReceiverService(context.read<UrlBloc>());
            
            return MaterialApp(
              title: 'Mobile-Share',
              theme: AppTheme.lightTheme,
              debugShowCheckedModeBanner: false,
              home: const UrlListScreen(),
            );
          },
        ),
      ),
    );
  }
}
