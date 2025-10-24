import 'package:flutter_bloc/flutter_bloc.dart';
import '../../../data/repositories/settings_repository.dart';
import '../../../data/repositories/github_repository.dart';
import '../../../data/models/auth_token.dart';
import 'auth_event.dart';
import 'auth_state.dart';

class AuthBloc extends Bloc<AuthEvent, AuthState> {
  final SettingsRepository _settingsRepository;
  final GitHubRepository _githubRepository;

  AuthBloc(this._settingsRepository, this._githubRepository)
      : super(AuthInitial()) {
    on<CheckAuth>(_onCheckAuth);
    on<StartOAuth>(_onStartOAuth);
    on<CompleteOAuth>(_onCompleteOAuth);
    on<UsePAT>(_onUsePAT);
    on<Logout>(_onLogout);
    on<TokenExpired>(_onTokenExpired);
  }

  Future<void> _onCheckAuth(
    CheckAuth event,
    Emitter<AuthState> emit,
  ) async {
    try {
      final token = await _settingsRepository.loadToken();

      if (token == null) {
        emit(AuthUnauthenticated());
        return;
      }

      if (token.isExpired) {
        emit(AuthUnauthenticated());
        return;
      }

      // Verify token by getting user info
      try {
        final userInfo = await _githubRepository.getUserInfo(token);
        final username = userInfo['login'] as String;
        emit(AuthAuthenticated(username));
      } catch (e) {
        // Token invalid
        await _settingsRepository.clearToken();
        emit(AuthUnauthenticated());
      }
    } catch (e) {
      emit(AuthError('Failed to check authentication: $e'));
    }
  }

  Future<void> _onStartOAuth(
    StartOAuth event,
    Emitter<AuthState> emit,
  ) async {
    // OAuth flow would require a backend to exchange code for token
    // For now, we'll just emit an in-progress state
    // Implementation would involve:
    // 1. Open browser with GitHub OAuth URL
    // 2. Redirect to deep link after authorization
    // 3. CompleteOAuth event triggered with code
    emit(AuthInProgress());
  }

  Future<void> _onCompleteOAuth(
    CompleteOAuth event,
    Emitter<AuthState> emit,
  ) async {
    try {
      emit(AuthInProgress());

      // This would require a backend to exchange code for token
      // For MVP, we recommend using PAT instead

      emit(const AuthError('OAuth not implemented. Please use Personal Access Token.'));
    } catch (e) {
      emit(AuthError('OAuth failed: $e'));
    }
  }

  Future<void> _onUsePAT(
    UsePAT event,
    Emitter<AuthState> emit,
  ) async {
    try {
      emit(AuthInProgress());

      // Create PAT token
      final token = AuthToken(
        token: event.token,
        type: TokenType.pat,
      );

      // Verify token by getting user info
      final userInfo = await _githubRepository.getUserInfo(token);
      final username = userInfo['login'] as String;

      // Save token
      await _settingsRepository.saveToken(token);

      emit(AuthAuthenticated(username));
    } catch (e) {
      emit(AuthError('Invalid token: $e'));
    }
  }

  Future<void> _onLogout(
    Logout event,
    Emitter<AuthState> emit,
  ) async {
    try {
      await _settingsRepository.clearToken();
      emit(AuthUnauthenticated());
    } catch (e) {
      emit(AuthError('Failed to logout: $e'));
    }
  }

  Future<void> _onTokenExpired(
    TokenExpired event,
    Emitter<AuthState> emit,
  ) async {
    await _settingsRepository.clearToken();
    emit(AuthUnauthenticated());
  }
}
