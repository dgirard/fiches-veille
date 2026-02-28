package com.veille.mobile_share

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel

class MainActivity : FlutterActivity() {
    private val CHANNEL = "com.veille.mobile_share/share"
    private var methodChannel: MethodChannel? = null
    private var pendingUrl: String? = null

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)

        methodChannel = MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL)
        methodChannel?.setMethodCallHandler { call, result ->
            when (call.method) {
                "showToast" -> {
                    val message = call.argument<String>("message") ?: "Message"
                    Toast.makeText(this, message, Toast.LENGTH_SHORT).show()
                    result.success(null)
                }
                "closeActivity" -> {
                    result.success(null)
                }
                else -> result.notImplemented()
            }
        }

        // Send pending URL if any
        pendingUrl?.let { url ->
            methodChannel?.invokeMethod("receiveUrl", url)
            pendingUrl = null
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        handleIntent(intent)
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        handleIntent(intent)
    }

    private fun handleIntent(intent: Intent?) {
        if (intent?.action == "com.veille.mobile_share.SHARE_URL") {
            val sharedUrl = intent.getStringExtra("shared_url")
            if (sharedUrl != null) {
                if (methodChannel != null) {
                    methodChannel?.invokeMethod("receiveUrl", sharedUrl)
                } else {
                    // Flutter engine not ready yet, store for later
                    pendingUrl = sharedUrl
                }
            }
        }
    }
}
