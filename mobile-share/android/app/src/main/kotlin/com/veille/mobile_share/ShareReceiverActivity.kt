package com.veille.mobile_share

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.widget.Toast

class ShareReceiverActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        handleSendIntent(intent)
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        handleSendIntent(intent)
    }

    private fun handleSendIntent(intent: Intent?) {
        if (intent?.action == Intent.ACTION_SEND && intent.type == "text/plain") {
            val sharedText = intent.getStringExtra(Intent.EXTRA_TEXT)
            if (sharedText != null) {
                // Forward to MainActivity with the shared URL
                val mainIntent = Intent(this, MainActivity::class.java).apply {
                    action = "com.veille.mobile_share.SHARE_URL"
                    putExtra("shared_url", sharedText)
                    flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_SINGLE_TOP
                }
                startActivity(mainIntent)
            } else {
                Toast.makeText(this, "No URL found", Toast.LENGTH_SHORT).show()
            }
        }
        finish()
    }
}
