import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:intl/intl.dart';
import '../../data/models/pending_url.dart';
import '../../core/theme/app_theme.dart';

class UrlCard extends StatelessWidget {
  final PendingUrl url;
  final VoidCallback onDelete;

  const UrlCard({
    super.key,
    required this.url,
    required this.onDelete,
  });

  Future<void> _launchUrl() async {
    final uri = Uri.parse(url.url);
    if (await canLaunchUrl(uri)) {
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Dismissible(
      key: Key(url.id.toString()),
      direction: DismissDirection.endToStart,
      background: Container(
        alignment: Alignment.centerRight,
        padding: const EdgeInsets.only(right: 16),
        color: AppTheme.errorColor,
        child: const Icon(Icons.delete, color: Colors.white),
      ),
      onDismissed: (_) => onDelete(),
      child: Card(
        child: InkWell(
          onTap: _launchUrl,
          child: Padding(
            padding: const EdgeInsets.all(12),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // URL icon
                Icon(
                  Icons.link,
                  color: AppTheme.primaryColor,
                  size: 20,
                ),
                const SizedBox(width: 12),

                // Content
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // URL
                      Text(
                        url.url,
                        style: const TextStyle(
                          fontSize: 16,
                          color: AppTheme.textPrimary,
                        ),
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                      ),
                      const SizedBox(height: 8),

                      // Status badge and timestamp
                      Row(
                        children: [
                          // Status badge
                          Container(
                            padding: const EdgeInsets.symmetric(
                              horizontal: 8,
                              vertical: 4,
                            ),
                            decoration: BoxDecoration(
                              color: url.synced
                                  ? AppTheme.secondaryColor.withValues(alpha: 0.2)
                                  : AppTheme.accentColor.withValues(alpha: 0.2),
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: Row(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Icon(
                                  url.synced ? Icons.cloud_done : Icons.smartphone,
                                  size: 14,
                                  color: url.synced
                                      ? AppTheme.secondaryColor
                                      : AppTheme.accentColor,
                                ),
                                const SizedBox(width: 4),
                                Text(
                                  url.synced ? 'Synced' : 'Local',
                                  style: TextStyle(
                                    fontSize: 12,
                                    color: url.synced
                                        ? AppTheme.secondaryColor
                                        : AppTheme.accentColor,
                                    fontWeight: FontWeight.w500,
                                  ),
                                ),
                              ],
                            ),
                          ),
                          const SizedBox(width: 12),

                          // Timestamp
                          Text(
                            _formatTimestamp(url.timestamp),
                            style: const TextStyle(
                              fontSize: 12,
                              color: AppTheme.textSecondary,
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),

                // Delete button
                IconButton(
                  icon: const Icon(Icons.delete_outline),
                  color: AppTheme.textSecondary,
                  onPressed: onDelete,
                  tooltip: 'Delete',
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  String _formatTimestamp(DateTime timestamp) {
    final now = DateTime.now();
    final difference = now.difference(timestamp);

    if (difference.inMinutes < 60) {
      return '${difference.inMinutes} min ago';
    } else if (difference.inHours < 24) {
      return '${difference.inHours} hours ago';
    } else {
      return DateFormat('MMM d, HH:mm').format(timestamp);
    }
  }
}
