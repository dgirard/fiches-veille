import 'package:flutter/material.dart';

/// Centralized error handling and user-friendly error messages
class ErrorHandler {
  /// Convert technical errors to user-friendly messages
  static String getUserFriendlyMessage(dynamic error) {
    final errorString = error.toString();

    // Network errors
    if (errorString.contains('SocketException') ||
        errorString.contains('Failed host lookup')) {
      return 'No internet connection. Please check your network.';
    }

    // GitHub API errors
    if (errorString.contains('401') || errorString.contains('Unauthorized')) {
      return 'Authentication failed. Please check your token.';
    }

    if (errorString.contains('403') || errorString.contains('Forbidden')) {
      return 'Access denied. Please verify your repository permissions.';
    }

    if (errorString.contains('404') || errorString.contains('Not Found')) {
      return 'Repository or file not found. Please check your settings.';
    }

    if (errorString.contains('422')) {
      return 'Invalid data. Please check your configuration.';
    }

    // Rate limiting
    if (errorString.contains('429') ||
        errorString.contains('rate limit exceeded')) {
      return 'GitHub API rate limit exceeded. Please try again later.';
    }

    // Database errors
    if (errorString.contains('DatabaseException') ||
        errorString.contains('SQLite')) {
      return 'Database error. Please restart the app.';
    }

    // Storage errors
    if (errorString.contains('SecureStorage') ||
        errorString.contains('KeyStore')) {
      return 'Secure storage error. Please check app permissions.';
    }

    // Invalid URL
    if (errorString.contains('Invalid URL')) {
      return 'Invalid URL format. Please enter a valid web address.';
    }

    // Timeout errors
    if (errorString.contains('TimeoutException')) {
      return 'Request timed out. Please try again.';
    }

    // Generic fallback
    return 'An unexpected error occurred. Please try again.';
  }

  /// Show error snackbar
  static void showErrorSnackBar(BuildContext context, dynamic error) {
    final message = getUserFriendlyMessage(error);
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: Colors.red[700],
        behavior: SnackBarBehavior.floating,
        action: SnackBarAction(
          label: 'Dismiss',
          textColor: Colors.white,
          onPressed: () {
            ScaffoldMessenger.of(context).hideCurrentSnackBar();
          },
        ),
        duration: const Duration(seconds: 4),
      ),
    );
  }

  /// Show success snackbar
  static void showSuccessSnackBar(BuildContext context, String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: Colors.green[700],
        behavior: SnackBarBehavior.floating,
        duration: const Duration(seconds: 2),
      ),
    );
  }

  /// Show info snackbar
  static void showInfoSnackBar(BuildContext context, String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: Colors.blue[700],
        behavior: SnackBarBehavior.floating,
        duration: const Duration(seconds: 3),
      ),
    );
  }

  /// Show confirmation dialog
  static Future<bool> showConfirmationDialog(
    BuildContext context, {
    required String title,
    required String message,
    String confirmText = 'Confirm',
    String cancelText = 'Cancel',
  }) async {
    final result = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(title),
        content: Text(message),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(false),
            child: Text(cancelText),
          ),
          ElevatedButton(
            onPressed: () => Navigator.of(context).pop(true),
            child: Text(confirmText),
          ),
        ],
      ),
    );
    return result ?? false;
  }
}
