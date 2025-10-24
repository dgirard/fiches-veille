import 'package:equatable/equatable.dart';
import '../../../data/models/pending_url.dart';

abstract class UrlState extends Equatable {
  const UrlState();

  @override
  List<Object?> get props => [];
}

class UrlsInitial extends UrlState {}

class UrlsLoading extends UrlState {}

class UrlsLoaded extends UrlState {
  final List<PendingUrl> urls;

  const UrlsLoaded(this.urls);

  @override
  List<Object?> get props => [urls];
}

class UrlAdded extends UrlState {
  final PendingUrl url;

  const UrlAdded(this.url);

  @override
  List<Object?> get props => [url];
}

class UrlDeleted extends UrlState {
  final int id;

  const UrlDeleted(this.id);

  @override
  List<Object?> get props => [id];
}

class UrlError extends UrlState {
  final String message;

  const UrlError(this.message);

  @override
  List<Object?> get props => [message];
}
