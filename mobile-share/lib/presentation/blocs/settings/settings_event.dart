import 'package:equatable/equatable.dart';
import '../../../data/models/github_config.dart';

abstract class SettingsEvent extends Equatable {
  const SettingsEvent();

  @override
  List<Object?> get props => [];
}

class LoadSettings extends SettingsEvent {}

class SaveSettings extends SettingsEvent {
  final GitHubConfig config;

  const SaveSettings(this.config);

  @override
  List<Object?> get props => [config];
}

class ClearSettings extends SettingsEvent {}
