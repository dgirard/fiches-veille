import 'package:equatable/equatable.dart';

abstract class AuthEvent extends Equatable {
  const AuthEvent();

  @override
  List<Object?> get props => [];
}

class CheckAuth extends AuthEvent {}

class StartOAuth extends AuthEvent {}

class CompleteOAuth extends AuthEvent {
  final String code;

  const CompleteOAuth(this.code);

  @override
  List<Object?> get props => [code];
}

class UsePAT extends AuthEvent {
  final String token;

  const UsePAT(this.token);

  @override
  List<Object?> get props => [token];
}

class Logout extends AuthEvent {}

class TokenExpired extends AuthEvent {}
