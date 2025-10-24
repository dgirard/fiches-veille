import 'package:equatable/equatable.dart';

abstract class AuthState extends Equatable {
  const AuthState();

  @override
  List<Object?> get props => [];
}

class AuthInitial extends AuthState {}

class AuthUnauthenticated extends AuthState {}

class AuthInProgress extends AuthState {}

class AuthAuthenticated extends AuthState {
  final String username;

  const AuthAuthenticated(this.username);

  @override
  List<Object?> get props => [username];
}

class AuthError extends AuthState {
  final String message;

  const AuthError(this.message);

  @override
  List<Object?> get props => [message];
}
