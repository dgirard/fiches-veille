import 'package:flutter_bloc/flutter_bloc.dart';
import '../../../data/repositories/local_url_repository.dart';
import '../../../data/repositories/github_repository.dart';
import '../../../data/repositories/settings_repository.dart';
import 'sync_event.dart';
import 'sync_state.dart';
import '../url/url_bloc.dart';
import '../url/url_event.dart';

class SyncBloc extends Bloc<SyncEvent, SyncState> {
  final LocalUrlRepository _localUrlRepository;
  final GitHubRepository _githubRepository;
  final SettingsRepository _settingsRepository;
  final UrlBloc _urlBloc;

  SyncBloc(
    this._localUrlRepository,
    this._githubRepository,
    this._settingsRepository,
    this._urlBloc,
  ) : super(SyncIdle()) {
    on<ManualSync>(_onManualSync);
    on<AutoSync>(_onAutoSync);
  }

  Future<void> _onManualSync(
    ManualSync event,
    Emitter<SyncState> emit,
  ) async {
    await _performSync(emit);
  }

  Future<void> _onAutoSync(
    AutoSync event,
    Emitter<SyncState> emit,
  ) async {
    await _performSync(emit);
  }

  Future<void> _performSync(Emitter<SyncState> emit) async {
    try {
      // Check configuration and authentication
      final config = await _settingsRepository.loadConfig();
      final token = await _settingsRepository.loadToken();

      if (config == null || token == null) {
        emit(const SyncError('Configuration or authentication missing'));
        return;
      }

      if (!config.isValid) {
        emit(const SyncError('Invalid configuration'));
        return;
      }

      // Get unsynced URLs
      final unsyncedUrls = await _localUrlRepository.getUnsynced();

      if (unsyncedUrls.isEmpty) {
        emit(const SyncSuccess(0));
        return;
      }

      emit(Syncing(0, unsyncedUrls.length));

      // Extract URL strings
      final urlStrings = unsyncedUrls.map((u) => u.url).toList();

      // Check for duplicates
      final newUrls = await _githubRepository.checkDuplicates(
        config,
        token,
        urlStrings,
      );

      if (newUrls.isEmpty) {
        // All URLs were duplicates, mark them as synced anyway
        final ids = unsyncedUrls.map((u) => u.id!).toList();
        await _localUrlRepository.markAsSynced(ids);
        _urlBloc.add(MarkUrlsSynced(ids));
        emit(SyncSuccess(unsyncedUrls.length));
        return;
      }

      emit(Syncing(unsyncedUrls.length - newUrls.length, unsyncedUrls.length));

      // Append new URLs to GitHub
      await _githubRepository.appendUrls(
        config,
        token,
        newUrls,
      );

      // Mark all URLs as synced (including duplicates)
      final ids = unsyncedUrls.map((u) => u.id!).toList();
      await _localUrlRepository.markAsSynced(ids);

      // Notify UrlBloc to update UI
      _urlBloc.add(MarkUrlsSynced(ids));

      emit(SyncSuccess(unsyncedUrls.length));
    } catch (e) {
      emit(SyncError('Sync failed: $e'));
    }
  }
}
