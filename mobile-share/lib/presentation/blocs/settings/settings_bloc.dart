import 'package:flutter_bloc/flutter_bloc.dart';
import '../../../data/repositories/settings_repository.dart';
import 'settings_event.dart';
import 'settings_state.dart';

class SettingsBloc extends Bloc<SettingsEvent, SettingsState> {
  final SettingsRepository _repository;

  SettingsBloc(this._repository) : super(SettingsInitial()) {
    on<LoadSettings>(_onLoadSettings);
    on<SaveSettings>(_onSaveSettings);
    on<ClearSettings>(_onClearSettings);
  }

  Future<void> _onLoadSettings(
    LoadSettings event,
    Emitter<SettingsState> emit,
  ) async {
    emit(SettingsLoading());
    try {
      final config = await _repository.loadConfig();
      emit(SettingsLoaded(config));
    } catch (e) {
      emit(SettingsError('Failed to load settings: $e'));
    }
  }

  Future<void> _onSaveSettings(
    SaveSettings event,
    Emitter<SettingsState> emit,
  ) async {
    emit(SettingsLoading());
    try {
      await _repository.saveConfig(event.config);
      emit(SettingsSaved());
      emit(SettingsLoaded(event.config));
    } catch (e) {
      emit(SettingsError('Failed to save settings: $e'));
    }
  }

  Future<void> _onClearSettings(
    ClearSettings event,
    Emitter<SettingsState> emit,
  ) async {
    try {
      await _repository.clearAll();
      emit(const SettingsLoaded(null));
    } catch (e) {
      emit(SettingsError('Failed to clear settings: $e'));
    }
  }
}
