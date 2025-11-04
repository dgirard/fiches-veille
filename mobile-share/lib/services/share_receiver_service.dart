import 'package:flutter/services.dart';
import '../presentation/blocs/url/url_bloc.dart';
import '../presentation/blocs/url/url_event.dart';
import '../presentation/blocs/url/url_state.dart';

class ShareReceiverService {
  static const platform = MethodChannel('com.veille.mobile_share/share');
  final UrlBloc _urlBloc;

  ShareReceiverService(this._urlBloc) {
    print('[ShareReceiverService] Initializing...');
    platform.setMethodCallHandler(_handleMethod);
    print('[ShareReceiverService] Method call handler set');
  }

  Future<dynamic> _handleMethod(MethodCall call) async {
    print('[ShareReceiverService] Received method call: ${call.method}');
    switch (call.method) {
      case 'receiveUrl':
        final url = call.arguments as String;
        print('[ShareReceiverService] Received URL: $url');
        await _handleReceivedUrl(url);
        break;
      default:
        print('[ShareReceiverService] Unknown method: ${call.method}');
        throw PlatformException(
          code: 'Unimplemented',
          details: 'Method ${call.method} not implemented',
        );
    }
  }

  Future<void> _handleReceivedUrl(String url) async {
    // Validate URL
    final isValid = _isValidUrl(url);

    if (!isValid) {
      await _showToast('Invalid URL');
      await _closeActivity();
      return;
    }

    // Add URL via BLoC
    _urlBloc.add(AddUrl(url));

    // Listen for result
    await for (final state in _urlBloc.stream) {
      if (state is UrlAdded) {
        await _showToast('URL saved locally');
        await _closeActivity();
        break;
      } else if (state is UrlError) {
        if (state.message.contains('Invalid URL')) {
          await _showToast('Invalid URL format');
        } else {
          await _showToast('URL already saved');
        }
        await _closeActivity();
        break;
      } else if (state is UrlsLoaded) {
        // URL added successfully (silent duplicate or success)
        await _showToast('URL saved');
        await _closeActivity();
        break;
      }
    }
  }

  bool _isValidUrl(String url) {
    final urlRegex = RegExp(
      r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$',
    );
    return urlRegex.hasMatch(url);
  }

  Future<void> _showToast(String message) async {
    try {
      await platform.invokeMethod('showToast', {'message': message});
    } catch (e) {
      // Silently fail if method not available
    }
  }

  Future<void> _closeActivity() async {
    try {
      await platform.invokeMethod('closeActivity');
    } catch (e) {
      // Silently fail if method not available
    }
  }
}
