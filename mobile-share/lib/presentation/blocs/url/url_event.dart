import 'package:equatable/equatable.dart';

abstract class UrlEvent extends Equatable {
  const UrlEvent();

  @override
  List<Object?> get props => [];
}

class LoadUrls extends UrlEvent {}

class AddUrl extends UrlEvent {
  final String url;

  const AddUrl(this.url);

  @override
  List<Object?> get props => [url];
}

class DeleteUrl extends UrlEvent {
  final int id;

  const DeleteUrl(this.id);

  @override
  List<Object?> get props => [id];
}

class MarkUrlsSynced extends UrlEvent {
  final List<int> ids;

  const MarkUrlsSynced(this.ids);

  @override
  List<Object?> get props => [ids];
}
