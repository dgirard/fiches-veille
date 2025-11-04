import 'package:flutter/services.dart';
import '../presentation/blocs/auth/auth_bloc.dart';
import '../presentation/blocs/auth/auth_event.dart';

class DeepLinkService {
  static const platform = MethodChannel('com.veille.mobile_share/deeplink');
  final AuthBloc _authBloc;

  DeepLinkService(this._authBloc) {
    platform.setMethodCallHandler(_handleMethod);
  }

  Future<dynamic> _handleMethod(MethodCall call) async {
    switch (call.method) {
      case 'oauthCallback':
        final code = call.arguments['code'] as String?;
        final state = call.arguments['state'] as String?;
        if (code != null) {
          await _handleOAuthCallback(code, state);
        }
        break;
      default:
        throw PlatformException(
          code: 'Unimplemented',
          details: 'Method ${call.method} not implemented',
        );
    }
  }

  Future<void> _handleOAuthCallback(String code, String? state) async {
    // Trigger OAuth completion in AuthBloc
    // The AuthBloc will handle token exchange with GitHub
    _authBloc.add(CompleteOAuth(code));
  }
}
