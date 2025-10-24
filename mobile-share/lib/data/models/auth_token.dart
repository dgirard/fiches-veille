import 'package:equatable/equatable.dart';

enum TokenType { oauth, pat }

class AuthToken extends Equatable {
  final String token;
  final TokenType type;
  final DateTime? expiresAt;

  const AuthToken({
    required this.token,
    required this.type,
    this.expiresAt,
  });

  bool get isExpired {
    if (expiresAt == null) return false;
    return DateTime.now().isAfter(expiresAt!);
  }

  Map<String, dynamic> toMap() {
    return {
      'token': token,
      'type': type.name,
      'expiresAt': expiresAt?.toIso8601String(),
    };
  }

  factory AuthToken.fromMap(Map<String, dynamic> map) {
    return AuthToken(
      token: map['token'] as String,
      type: TokenType.values.firstWhere((e) => e.name == map['type']),
      expiresAt: map['expiresAt'] != null
          ? DateTime.parse(map['expiresAt'] as String)
          : null,
    );
  }

  @override
  List<Object?> get props => [token, type, expiresAt];
}
