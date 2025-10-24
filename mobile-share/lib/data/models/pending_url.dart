import 'package:equatable/equatable.dart';

class PendingUrl extends Equatable {
  final int? id;
  final String url;
  final DateTime timestamp;
  final bool synced;

  const PendingUrl({
    this.id,
    required this.url,
    required this.timestamp,
    this.synced = false,
  });

  // toMap for SQLite
  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'url': url,
      'timestamp': timestamp.millisecondsSinceEpoch,
      'synced': synced ? 1 : 0,
    };
  }

  // fromMap for SQLite
  factory PendingUrl.fromMap(Map<String, dynamic> map) {
    return PendingUrl(
      id: map['id'] as int?,
      url: map['url'] as String,
      timestamp: DateTime.fromMillisecondsSinceEpoch(map['timestamp'] as int),
      synced: (map['synced'] as int) == 1,
    );
  }

  // copyWith for immutability
  PendingUrl copyWith({
    int? id,
    String? url,
    DateTime? timestamp,
    bool? synced,
  }) {
    return PendingUrl(
      id: id ?? this.id,
      url: url ?? this.url,
      timestamp: timestamp ?? this.timestamp,
      synced: synced ?? this.synced,
    );
  }

  @override
  List<Object?> get props => [id, url, timestamp, synced];
}
