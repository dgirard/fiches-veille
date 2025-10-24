import 'package:flutter_bloc/flutter_bloc.dart';
import '../../../data/repositories/local_url_repository.dart';
import '../../../data/models/pending_url.dart';
import 'url_event.dart';
import 'url_state.dart';

class UrlBloc extends Bloc<UrlEvent, UrlState> {
  final LocalUrlRepository _repository;

  UrlBloc(this._repository) : super(UrlsInitial()) {
    on<LoadUrls>(_onLoadUrls);
    on<AddUrl>(_onAddUrl);
    on<DeleteUrl>(_onDeleteUrl);
    on<MarkUrlsSynced>(_onMarkUrlsSynced);
  }

  Future<void> _onLoadUrls(
    LoadUrls event,
    Emitter<UrlState> emit,
  ) async {
    emit(UrlsLoading());
    try {
      final urls = await _repository.getAll();
      emit(UrlsLoaded(urls));
    } catch (e) {
      emit(UrlError('Failed to load URLs: $e'));
    }
  }

  Future<void> _onAddUrl(
    AddUrl event,
    Emitter<UrlState> emit,
  ) async {
    try {
      // Validate URL
      if (!_isValidUrl(event.url)) {
        emit(const UrlError('Invalid URL format'));
        return;
      }

      // Check if URL already exists
      final exists = await _repository.exists(event.url);
      if (exists) {
        // Silently ignore duplicates
        return;
      }

      // Add URL
      final pendingUrl = PendingUrl(
        url: event.url,
        timestamp: DateTime.now(),
        synced: false,
      );

      final id = await _repository.addUrl(pendingUrl);

      if (id > 0) {
        emit(UrlAdded(pendingUrl.copyWith(id: id)));
        // Reload URLs to update list
        add(LoadUrls());
      }
    } catch (e) {
      emit(UrlError('Failed to add URL: $e'));
    }
  }

  Future<void> _onDeleteUrl(
    DeleteUrl event,
    Emitter<UrlState> emit,
  ) async {
    try {
      await _repository.delete(event.id);
      emit(UrlDeleted(event.id));
      // Reload URLs to update list
      add(LoadUrls());
    } catch (e) {
      emit(UrlError('Failed to delete URL: $e'));
    }
  }

  Future<void> _onMarkUrlsSynced(
    MarkUrlsSynced event,
    Emitter<UrlState> emit,
  ) async {
    try {
      await _repository.markAsSynced(event.ids);
      // Reload URLs to update list
      add(LoadUrls());
    } catch (e) {
      emit(UrlError('Failed to mark URLs as synced: $e'));
    }
  }

  bool _isValidUrl(String url) {
    final urlRegex = RegExp(
      r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$',
    );
    return urlRegex.hasMatch(url);
  }
}
