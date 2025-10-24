import 'package:equatable/equatable.dart';

abstract class SyncEvent extends Equatable {
  const SyncEvent();

  @override
  List<Object?> get props => [];
}

class ManualSync extends SyncEvent {}

class AutoSync extends SyncEvent {}
