# Release Build Configuration

This document explains how to configure and build a release version of Mobile-Share for distribution.

## Prerequisites

- Flutter SDK installed and configured
- Android SDK with build tools
- Java Development Kit (JDK 11 or higher)

## Step 1: Generate Signing Key

Android requires all APKs to be digitally signed before they can be installed. Follow these steps to create a signing key:

### Create Upload Keystore

```bash
keytool -genkey -v -keystore ~/upload-keystore.jks \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias upload
```

You'll be prompted to enter:
- Keystore password (save this!)
- Key password (save this!)
- Your name and organization information

⚠️ **IMPORTANT**: Keep your keystore file and passwords secure! If you lose them, you cannot update your app.

### Store Keystore Securely

```bash
# Recommended location (adjust as needed)
mkdir -p ~/android-keys
mv ~/upload-keystore.jks ~/android-keys/
chmod 600 ~/android-keys/upload-keystore.jks
```

## Step 2: Configure Key Properties

Create `android/key.properties` (this file is gitignored):

```properties
storePassword=YOUR_STORE_PASSWORD
keyPassword=YOUR_KEY_PASSWORD
keyAlias=upload
storeFile=/Users/YOUR_USERNAME/android-keys/upload-keystore.jks
```

Replace:
- `YOUR_STORE_PASSWORD` with your keystore password
- `YOUR_KEY_PASSWORD` with your key password
- `/Users/YOUR_USERNAME` with your actual home directory path

## Step 3: Update build.gradle.kts

Edit `android/app/build.gradle.kts` to use the signing configuration:

```kotlin
// Add at the top of the file
val keystorePropertiesFile = rootProject.file("key.properties")
val keystoreProperties = java.util.Properties()
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(java.io.FileInputStream(keystorePropertiesFile))
}

android {
    // ... existing configuration ...

    signingConfigs {
        create("release") {
            keyAlias = keystoreProperties["keyAlias"] as String?
            keyPassword = keystoreProperties["keyPassword"] as String?
            storeFile = keystoreProperties["storeFile"]?.let { file(it) }
            storePassword = keystoreProperties["storePassword"] as String?
        }
    }

    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("release")
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}
```

## Step 4: Create ProGuard Rules

Create `android/app/proguard-rules.pro`:

```proguard
# Flutter
-keep class io.flutter.app.** { *; }
-keep class io.flutter.plugin.** { *; }
-keep class io.flutter.util.** { *; }
-keep class io.flutter.view.** { *; }
-keep class io.flutter.** { *; }
-keep class io.flutter.plugins.** { *; }

# Keep native methods
-keepclassmembers class * {
    native <methods>;
}

# Keep custom application classes
-keep class com.veille.mobile_share.** { *; }

# SQLite
-keep class org.sqlite.** { *; }
-keep class org.sqlite.database.** { *; }

# Kotlin
-keep class kotlin.** { *; }
-keep class kotlin.Metadata { *; }
-dontwarn kotlin.**
```

## Step 5: Update App Version

Edit `pubspec.yaml` to update version:

```yaml
version: 1.0.0+1
```

Format: `MAJOR.MINOR.PATCH+BUILD_NUMBER`

For each release:
- Increment BUILD_NUMBER for internal updates
- Increment PATCH for bug fixes
- Increment MINOR for new features
- Increment MAJOR for breaking changes

## Step 6: Build Release

### Build APK

```bash
# Clean previous builds
flutter clean

# Get dependencies
flutter pub get

# Build release APK
flutter build apk --release

# Output location
# build/app/outputs/flutter-apk/app-release.apk
```

### Build App Bundle (for Play Store)

```bash
# Build App Bundle
flutter build appbundle --release

# Output location
# build/app/outputs/bundle/release/app-release.aab
```

App Bundle is the recommended format for Google Play Store as it generates optimized APKs for different device configurations.

## Step 7: Test Release Build

### Install on Device

```bash
# Install APK
flutter install --release

# Or manually with adb
adb install build/app/outputs/flutter-apk/app-release.apk
```

### Test Checklist

- [ ] App installs successfully
- [ ] Share functionality works from other apps
- [ ] URLs are saved to local database
- [ ] GitHub sync works with valid credentials
- [ ] Settings are persisted
- [ ] Delete URLs works
- [ ] No crashes or ANRs
- [ ] Performance is smooth
- [ ] App size is acceptable (< 20MB)

## File Size Optimization

Current build size should be around:
- APK: ~15-20 MB
- App Bundle: ~12-18 MB

### Further Optimization

If the app is too large:

1. **Remove unused resources**
   ```bash
   flutter build apk --release --analyze-size
   ```

2. **Enable split APKs per ABI**
   Edit `android/app/build.gradle.kts`:
   ```kotlin
   splits {
       abi {
           isEnable = true
           reset()
           include("armeabi-v7a", "arm64-v8a", "x86_64")
           isUniversalApk = false
       }
   }
   ```

3. **Compress assets**
   - Optimize images
   - Remove debug symbols in release

## Security Checklist

Before releasing:

- [ ] No hardcoded secrets or tokens
- [ ] ProGuard/R8 obfuscation enabled
- [ ] HTTPS only for all network requests
- [ ] Input validation on all user inputs
- [ ] Secure storage for sensitive data
- [ ] No debug logs in release build

## Distribution

### Google Play Store

1. Create developer account ($25 one-time fee)
2. Create new application in Play Console
3. Upload App Bundle (`.aab` file)
4. Fill out store listing (description, screenshots, etc.)
5. Set up content rating
6. Set pricing & distribution
7. Submit for review

### Direct Distribution (APK)

For internal testing or direct distribution:

1. Upload APK to secure location
2. Enable "Install from Unknown Sources" on device
3. Download and install APK
4. Users will see "Install blocked" warning - this is normal for apps outside Play Store

## Troubleshooting

### Build fails with "Duplicate class" error
```bash
flutter clean
flutter pub get
flutter build apk --release
```

### Signing error
- Verify key.properties file exists and paths are correct
- Check keystore file permissions
- Ensure passwords are correct

### App crashes on startup
- Check ProGuard rules
- Test debug build first
- Check Android logs: `adb logcat`

### Large APK size
- Run `flutter build apk --analyze-size`
- Check for unused dependencies
- Consider split APKs

## Versioning Strategy

Recommended versioning for releases:

| Version | Purpose | Example |
|---------|---------|---------|
| 1.0.0+1 | Initial release | First public release |
| 1.0.1+2 | Bug fix | Fixed crash on Android 12 |
| 1.1.0+3 | Minor update | Added export feature |
| 2.0.0+4 | Major update | Complete UI redesign |

## Continuous Integration

For automated builds, consider setting up CI/CD:

- GitHub Actions
- GitLab CI
- Codemagic
- Bitrise

Example GitHub Actions workflow in `.github/workflows/release.yml`:

```yaml
name: Release Build

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-java@v3
        with:
          java-version: '11'
      - uses: subosito/flutter-action@v2
      - run: flutter pub get
      - run: flutter test
      - run: flutter build apk --release
      - uses: actions/upload-artifact@v3
        with:
          name: release-apk
          path: build/app/outputs/flutter-apk/app-release.apk
```

## References

- [Flutter Build & Release Guide](https://docs.flutter.dev/deployment/android)
- [Android App Signing](https://developer.android.com/studio/publish/app-signing)
- [ProGuard Manual](https://www.guardsquare.com/manual/home)
- [Play Console Help](https://support.google.com/googleplay/android-developer)

---

**Next Steps**: After successful build, proceed with testing on multiple devices before public release.
