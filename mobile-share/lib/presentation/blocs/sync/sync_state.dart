import 'package:equatable/equatable.dart';

abstract class SyncState extends Equatable {
  const SyncState();

  @override
  List<Object?> get props => [];
}

class SyncIdle extends SyncState {}

class Syncing extends SyncState {
  final int progress;
  final int total;

  const Syncing(this.progress, this.total);

  @override
  List<Object?> get props => [progress, total];
}

class SyncSuccess extends SyncState {
  final int synced;

  const SyncSuccess(this.synced);

  @override
  List<Object?> get props => [synced];
}

class SyncError extends SyncState {
  final String message;

  const SyncError(this.message);

  @override
  List<Object?> get props => [message];
}
