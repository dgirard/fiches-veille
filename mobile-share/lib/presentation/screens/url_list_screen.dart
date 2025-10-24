import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import '../blocs/url/url_bloc.dart';
import '../blocs/url/url_event.dart';
import '../blocs/url/url_state.dart';
import '../blocs/sync/sync_bloc.dart';
import '../blocs/sync/sync_event.dart';
import '../blocs/sync/sync_state.dart';
import '../widgets/url_card.dart';
import '../widgets/empty_state.dart';
import 'settings_screen.dart';
import '../../core/theme/app_theme.dart';

class UrlListScreen extends StatefulWidget {
  const UrlListScreen({super.key});

  @override
  State<UrlListScreen> createState() => _UrlListScreenState();
}

class _UrlListScreenState extends State<UrlListScreen> {
  @override
  void initState() {
    super.initState();
    context.read<UrlBloc>().add(LoadUrls());
  }

  void _navigateToSettings() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => const SettingsScreen()),
    );
  }

  void _refreshUrls() {
    context.read<UrlBloc>().add(LoadUrls());
  }

  void _syncUrls() {
    context.read<SyncBloc>().add(ManualSync());
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Mobile-Share'),
        backgroundColor: AppTheme.primaryColor,
        foregroundColor: Colors.white,
        actions: [
          IconButton(
            icon: const Icon(Icons.settings),
            onPressed: _navigateToSettings,
            tooltip: 'Settings',
          ),
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: _refreshUrls,
            tooltip: 'Refresh',
          ),
        ],
      ),
      body: MultiBlocListener(
        listeners: [
          BlocListener<SyncBloc, SyncState>(
            listener: (context, state) {
              if (state is SyncSuccess) {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text('✓ ${state.synced} URL(s) synced to GitHub'),
                    backgroundColor: AppTheme.secondaryColor,
                  ),
                );
              }
              if (state is SyncError) {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text(state.message),
                    backgroundColor: AppTheme.errorColor,
                  ),
                );
              }
            },
          ),
          BlocListener<UrlBloc, UrlState>(
            listener: (context, state) {
              if (state is UrlError) {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text(state.message),
                    backgroundColor: AppTheme.errorColor,
                  ),
                );
              }
            },
          ),
        ],
        child: Column(
          children: [
            // Sync progress indicator
            BlocBuilder<SyncBloc, SyncState>(
              builder: (context, state) {
                if (state is Syncing) {
                  return Card(
                    margin: const EdgeInsets.all(16),
                    color: AppTheme.surfaceColor,
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: Column(
                        children: [
                          Row(
                            children: [
                              const SizedBox(
                                width: 20,
                                height: 20,
                                child: CircularProgressIndicator(strokeWidth: 2),
                              ),
                              const SizedBox(width: 12),
                              Text(
                                'Syncing ${state.progress}/${state.total} URLs...',
                                style: const TextStyle(
                                  fontSize: 14,
                                  fontWeight: FontWeight.w500,
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 8),
                          LinearProgressIndicator(
                            value: state.total > 0
                                ? state.progress / state.total
                                : 0,
                          ),
                        ],
                      ),
                    ),
                  );
                }
                return const SizedBox.shrink();
              },
            ),

            // URL List
            Expanded(
              child: BlocBuilder<UrlBloc, UrlState>(
                builder: (context, state) {
                  if (state is UrlsLoading) {
                    return const Center(child: CircularProgressIndicator());
                  }

                  if (state is UrlsLoaded) {
                    if (state.urls.isEmpty) {
                      return const EmptyState();
                    }

                    return ListView.builder(
                      padding: const EdgeInsets.symmetric(vertical: 8),
                      itemCount: state.urls.length,
                      itemBuilder: (context, index) {
                        final url = state.urls[index];
                        return UrlCard(
                          url: url,
                          onDelete: () {
                            context.read<UrlBloc>().add(DeleteUrl(url.id!));
                          },
                        );
                      },
                    );
                  }

                  return const EmptyState();
                },
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: BlocBuilder<UrlBloc, UrlState>(
        builder: (context, urlState) {
          // Show FAB only if there are unsynced URLs
          if (urlState is UrlsLoaded) {
            final hasUnsyncedUrls =
                urlState.urls.any((url) => !url.synced);

            if (hasUnsyncedUrls) {
              return BlocBuilder<SyncBloc, SyncState>(
                builder: (context, syncState) {
                  final isSyncing = syncState is Syncing;

                  return FloatingActionButton(
                    onPressed: isSyncing ? null : _syncUrls,
                    backgroundColor:
                        isSyncing ? Colors.grey : AppTheme.primaryColor,
                    tooltip: 'Sync to GitHub',
                    child: isSyncing
                        ? const SizedBox(
                            width: 24,
                            height: 24,
                            child: CircularProgressIndicator(
                              strokeWidth: 2,
                              color: Colors.white,
                            ),
                          )
                        : const Icon(Icons.sync),
                  );
                },
              );
            }
          }

          return const SizedBox.shrink();
        },
      ),
    );
  }
}
