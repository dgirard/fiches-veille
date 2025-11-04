package com.veille.mobile_share

import android.app.Application
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.embedding.engine.FlutterEngineCache
import io.flutter.embedding.engine.dart.DartExecutor

class MobileShareApplication : Application() {
    companion object {
        const val ENGINE_ID = "mobile_share_engine"
    }

    lateinit var flutterEngine: FlutterEngine

    override fun onCreate() {
        super.onCreate()

        // Create and warm up the FlutterEngine
        flutterEngine = FlutterEngine(this)

        // Start executing Dart code to pre-warm the FlutterEngine
        flutterEngine.dartExecutor.executeDartEntrypoint(
            DartExecutor.DartEntrypoint.createDefault()
        )

        // Cache the FlutterEngine to be used by both MainActivity and ShareReceiverActivity
        FlutterEngineCache
            .getInstance()
            .put(ENGINE_ID, flutterEngine)
    }
}
