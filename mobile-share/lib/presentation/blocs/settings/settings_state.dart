import 'package:equatable/equatable.dart';
import '../../../data/models/github_config.dart';

abstract class SettingsState extends Equatable {
  const SettingsState();

  @override
  List<Object?> get props => [];
}

class SettingsInitial extends SettingsState {}

class SettingsLoading extends SettingsState {}

class SettingsLoaded extends SettingsState {
  final GitHubConfig? config;

  const SettingsLoaded(this.config);

  @override
  List<Object?> get props => [config];
}

class SettingsSaved extends SettingsState {}

class SettingsError extends SettingsState {
  final String message;

  const SettingsError(this.message);

  @override
  List<Object?> get props => [message];
}
