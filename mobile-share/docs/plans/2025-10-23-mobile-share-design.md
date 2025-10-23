# Mobile-Share Application Design
**Date:** 2025-10-23
**Version:** 1.0
**Status:** Approved

---

## Table des matières
1. [Vue d'ensemble](#vue-densemble)
2. [Objectifs et contraintes](#objectifs-et-contraintes)
3. [Architecture technique](#architecture-technique)
4. [Spécifications UX/UI](#spécifications-uxui)
5. [User flows](#user-flows)
6. [Wireframes et maquettes](#wireframes-et-maquettes)
7. [Spécifications des composants](#spécifications-des-composants)
8. [États et gestion d'erreurs](#états-et-gestion-derreurs)

---

## Vue d'ensemble

### Concept
Mobile-Share est une application Android Flutter qui permet de sauvegarder rapidement des URLs d'articles intéressants dans un projet GitHub de veille technologique via le menu "Partager" natif d'Android.

### Proposition de valeur
- **Capture rapide** : Partager une URL depuis n'importe quelle app Android en 2 secondes
- **Synchronisation fiable** : Sauvegarde locale + sync GitHub avec gestion hors ligne
- **Workflow intégré** : S'intègre au workflow de veille existant (fichier `urls-to-process.md`)

### Utilisateur cible
Veilleur technologique qui lit des articles sur mobile et souhaite centraliser les URLs dans son repo GitHub pour traitement ultérieur.

---

## Objectifs et contraintes

### Objectifs fonctionnels
1. ✅ Recevoir des URLs via le menu "Partager" d'Android
2. ✅ Sauvegarder les URLs dans `urls-to-process.md` à la racine du repo GitHub
3. ✅ Gérer l'authentification OAuth GitHub de manière sécurisée
4. ✅ Supporter le mode hors ligne avec synchronisation manuelle
5. ✅ Éviter les doublons silencieusement

### Contraintes techniques
- **Plateforme** : Android uniquement (Flutter)
- **Authentification** : OAuth GitHub + option Personal Access Token (PAT)
- **Configuration** : Username, repo, branch configurables (jamais en dur dans le code)
- **Format fichier** : Une URL par ligne, pas de métadonnées
- **Stockage local** : SQLite pour les URLs en attente
- **Sécurité** : FlutterSecureStorage pour les tokens

### Critères de succès
- L'app apparaît dans le menu "Partager" pour les liens
- Temps de partage < 3 secondes (feedback immédiat)
- Aucune perte de données en mode hors ligne
- Configuration en moins de 2 minutes

---

## Architecture technique

### Pattern architectural : BLoC (Business Logic Component)

```
┌─────────────────────────────────────────────────────────┐
│                  PRESENTATION LAYER                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │ Settings    │  │  UrlList    │  │ShareReceiver│    │
│  │  Screen     │  │   Screen    │  │  Activity   │    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
│         │                 │                │            │
│         ├─────────────────┼────────────────┤            │
│         ▼                 ▼                ▼            │
├─────────────────────────────────────────────────────────┤
│                      BLoC LAYER                         │
│  ┌───────────┐ ┌────────┐ ┌────────┐ ┌──────────┐     │
│  │ Settings  │ │  Url   │ │ Sync   │ │  Auth    │     │
│  │   BLoC    │ │  BLoC  │ │  BLoC  │ │  BLoC    │     │
│  └───────────┘ └────────┘ └────────┘ └──────────┘     │
│         │            │          │           │           │
├─────────┼────────────┼──────────┼───────────┼──────────┤
│         ▼            ▼          ▼           ▼           │
│                    DATA LAYER                           │
│  ┌───────────┐ ┌────────────┐ ┌──────────────┐        │
│  │ Settings  │ │ LocalUrl   │ │   GitHub     │        │
│  │Repository │ │ Repository │ │  Repository  │        │
│  └───────────┘ └────────────┘ └──────────────┘        │
│         │            │                  │               │
│         ▼            ▼                  ▼               │
│  ┌───────────┐ ┌──────────┐     ┌──────────┐          │
│  │  Secure   │ │  SQLite  │     │ GitHub   │          │
│  │  Storage  │ │    DB    │     │ REST API │          │
│  └───────────┘ └──────────┘     └──────────┘          │
└─────────────────────────────────────────────────────────┘
```

### Couches détaillées

#### 1. Presentation Layer
**Responsabilités** : Affichage UI, capture événements utilisateur, navigation

**Composants** :
- `SettingsScreen` : Configuration GitHub + authentification
- `UrlListScreen` : Liste des URLs avec statut sync
- `ShareReceiverActivity` : Activité transparente pour réception partage

**Technologies** : Flutter Widgets, BlocBuilder, BlocListener

#### 2. BLoC Layer
**Responsabilités** : Logique métier, gestion d'état, orchestration

**BLoCs** :
- **SettingsBLoC** : Gestion configuration (save/load/validate)
  - Events: `LoadSettings`, `SaveSettings`, `ValidateConfig`
  - States: `SettingsLoading`, `SettingsLoaded`, `SettingsError`

- **UrlBLoC** : Gestion liste locale d'URLs
  - Events: `AddUrl`, `DeleteUrl`, `LoadUrls`, `MarkAsSynced`
  - States: `UrlsLoading`, `UrlsLoaded`, `UrlAdded`, `UrlError`

- **SyncBLoC** : Synchronisation avec GitHub
  - Events: `ManualSync`, `AutoSync`
  - States: `SyncIdle`, `Syncing`, `SyncSuccess`, `SyncError`

- **AuthBLoC** : Authentification OAuth/PAT
  - Events: `StartOAuth`, `CompleteOAuth`, `UsePAT`, `Logout`, `CheckAuth`
  - States: `AuthUnauthenticated`, `AuthInProgress`, `AuthAuthenticated`, `AuthError`

**Technologies** : flutter_bloc package

#### 3. Data Layer
**Responsabilités** : Accès données, persistance, API externes

**Repositories** :
- **SettingsRepository** : CRUD configuration
  - Méthodes: `saveConfig()`, `loadConfig()`, `clearConfig()`
  - Storage: FlutterSecureStorage

- **LocalUrlRepository** : CRUD URLs locales
  - Méthodes: `addUrl()`, `getAll()`, `getUnsynced()`, `markSynced()`, `delete()`, `exists()`
  - Storage: SQLite (table `pending_urls`)

- **GitHubRepository** : Interaction GitHub API
  - Méthodes: `authenticate()`, `getFileContent()`, `updateFile()`, `checkDuplicates()`
  - API: GitHub REST API v3

**Technologies** : sqflite, flutter_secure_storage, http/dio

### Modèles de données

#### PendingUrl
```dart
class PendingUrl {
  final int? id;
  final String url;
  final DateTime timestamp;
  final bool synced;

  PendingUrl({
    this.id,
    required this.url,
    required this.timestamp,
    this.synced = false,
  });
}
```

#### GitHubConfig
```dart
class GitHubConfig {
  final String username;
  final String repository;
  final String branch;

  GitHubConfig({
    required this.username,
    required this.repository,
    this.branch = 'main',
  });
}
```

#### AuthToken
```dart
class AuthToken {
  final String token;
  final TokenType type; // oauth or pat
  final DateTime? expiresAt;

  AuthToken({
    required this.token,
    required this.type,
    this.expiresAt,
  });
}
```

### Flux de données principaux

#### Flux 1 : Partage d'URL
```
[Autre app] → [Android Share Intent] → [ShareReceiverActivity]
    → UrlBLoC.add(AddUrl(url))
    → LocalUrlRepository.addUrl() + exists() check
    → SQLite INSERT (if not exists)
    → UrlBLoC emits UrlAdded
    → Toast notification
    → [Optional] SyncBLoC.add(AutoSync)
```

#### Flux 2 : Synchronisation manuelle
```
[User clicks Sync button] → SyncBLoC.add(ManualSync)
    → LocalUrlRepository.getUnsynced()
    → GitHubRepository.getFileContent('urls-to-process.md')
    → GitHubRepository.checkDuplicates(urls)
    → GitHubRepository.updateFile(new_urls)
    → LocalUrlRepository.markSynced(urls)
    → SyncBLoC emits SyncSuccess
    → SnackBar confirmation
```

#### Flux 3 : Authentification OAuth
```
[User clicks "Connect GitHub"] → AuthBLoC.add(StartOAuth)
    → Launch browser with OAuth URL
    → User authorizes on GitHub
    → GitHub redirects to mobileshare://oauth-callback?code=XXX
    → AuthBLoC.add(CompleteOAuth(code))
    → Exchange code for token (GitHub API)
    → SettingsRepository.saveToken(token)
    → AuthBLoC emits AuthAuthenticated
```

### Configuration Android

#### AndroidManifest.xml
```xml
<!-- Intent filter for Share functionality -->
<activity
    android:name=".ShareReceiverActivity"
    android:label="Save to Veille"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
    android:excludeFromRecents="true"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.SEND" />
        <category android:name="android.intent.category.DEFAULT" />
        <data android:mimeType="text/plain" />
    </intent-filter>
</activity>

<!-- Deep link for OAuth callback -->
<intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="mobileshare" android:host="oauth-callback" />
</intent-filter>
```

### Dépendances Flutter principales
```yaml
dependencies:
  flutter_bloc: ^8.1.3
  sqflite: ^2.3.0
  flutter_secure_storage: ^9.0.0
  http: ^1.1.0
  url_launcher: ^6.2.1
  connectivity_plus: ^5.0.1

dev_dependencies:
  bloc_test: ^9.1.4
  mockito: ^5.4.2
```

---

## Spécifications UX/UI

### Principes de design

1. **Simplicité** : Interface minimaliste, actions claires
2. **Feedback immédiat** : Chaque action a un retour visuel (< 300ms)
3. **Fiabilité** : Statuts de sync clairs, gestion d'erreurs explicite
4. **Rapidité** : Workflow de partage en 2-3 secondes maximum

### Palette de couleurs

```
Primary Color:   #2196F3  (Blue - rappelle GitHub)
Secondary Color: #4CAF50  (Green - succès, synced)
Accent Color:    #FF9800  (Orange - local, pending)
Error Color:     #F44336  (Red - erreurs)
Background:      #FFFFFF  (White)
Surface:         #F5F5F5  (Light gray)
Text Primary:    #212121  (Dark gray)
Text Secondary:  #757575  (Medium gray)
```

### Typographie

```
Headline 1: Roboto Bold, 24px
Headline 2: Roboto Medium, 20px
Body 1: Roboto Regular, 16px
Body 2: Roboto Regular, 14px
Caption: Roboto Regular, 12px
Button: Roboto Medium, 14px, uppercase
```

### Iconographie

- **Settings** : Material Icons `settings`
- **Sync** : Material Icons `sync`
- **Add** : Material Icons `add`
- **Delete** : Material Icons `delete`
- **Check** : Material Icons `check_circle` (synced)
- **Pending** : Material Icons `schedule` (local)
- **Error** : Material Icons `error_outline`
- **GitHub** : Custom GitHub logo icon

---

## User flows

### Flow 1 : Premier lancement et configuration

```
┌──────────────────┐
│  App Launch      │
│  (First Time)    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  AuthBLoC checks │
│  for saved token │
└────────┬─────────┘
         │ No token
         ▼
┌──────────────────┐
│ SettingsScreen   │
│ (Empty form)     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ User fills:      │
│ - Username       │
│ - Repo name      │
│ - Branch         │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ User clicks      │
│ "Connect GitHub" │
└────────┬─────────┘
         │
         ├─────────┬───────────┐
         │         │           │
         ▼         ▼           ▼
   ┌────────┐ ┌───────┐  ┌─────────┐
   │ OAuth  │ │  PAT  │  │ Cancel  │
   │  Flow  │ │ Input │  │         │
   └───┬────┘ └───┬───┘  └─────────┘
       │          │
       ▼          ▼
┌──────────────────┐
│ Token saved      │
│ Auth successful  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Navigate to      │
│ UrlListScreen    │
│ (Empty state)    │
└──────────────────┘
```

### Flow 2 : Partage d'URL (Happy Path)

```
┌──────────────────┐
│ User browsing    │
│ in Chrome/App    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Tap Share button │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Android Share    │
│ menu appears     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Select           │
│ "Save to Veille" │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ShareReceiverActivity│
│ (Transparent)    │
│ validates URL    │
└────────┬─────────┘
         │
         ├────────────┬─────────────┐
         │            │             │
         ▼            ▼             ▼
    ┌────────┐  ┌─────────┐  ┌──────────┐
    │Invalid │  │Duplicate│  │Valid &   │
    │  URL   │  │ (skip)  │  │New URL   │
    └───┬────┘  └────┬────┘  └────┬─────┘
        │            │             │
        ▼            ▼             ▼
    ┌────────┐  ┌─────────┐  ┌──────────┐
    │ Toast: │  │ Toast:  │  │Save to   │
    │"Invalid│  │"Already │  │SQLite    │
    │  URL"  │  │ saved"  │  └────┬─────┘
    └────────┘  └─────────┘       │
                                   ▼
                            ┌──────────┐
                            │Try auto  │
                            │  sync?   │
                            └────┬─────┘
                                 │
                    ├────────────┴──────────┐
                    │                       │
                    ▼                       ▼
            ┌───────────────┐      ┌────────────┐
            │ Online &      │      │  Offline   │
            │ Authenticated │      │     OR     │
            │               │      │Not auth    │
            └───────┬───────┘      └─────┬──────┘
                    │                    │
                    ▼                    ▼
            ┌───────────────┐      ┌────────────┐
            │ Sync to       │      │Toast:      │
            │ GitHub        │      │"Saved      │
            │               │      │ locally"   │
            └───────┬───────┘      └────────────┘
                    │
                    ▼
            ┌───────────────┐
            │ Toast:        │
            │ "URL saved    │
            │  and synced"  │
            └───────────────┘
```

### Flow 3 : Synchronisation manuelle

```
┌──────────────────┐
│ User opens app   │
│ UrlListScreen    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ See list of URLs │
│ Some with badge  │
│ "📱 Local"       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Tap FAB          │
│ "Sync" button    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Check network &  │
│ authentication   │
└────────┬─────────┘
         │
    ├────┴─────┐
    │          │
    ▼          ▼
┌────────┐ ┌──────────┐
│ Valid  │ │ Invalid  │
└───┬────┘ └────┬─────┘
    │           │
    │           ▼
    │      ┌──────────┐
    │      │SnackBar: │
    │      │"Check    │
    │      │settings" │
    │      └──────────┘
    │
    ▼
┌──────────────────┐
│ Show loading     │
│ indicator        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Fetch file from  │
│ GitHub           │
└────────┬─────────┘
         │
    ├────┴─────┐
    │          │
    ▼          ▼
┌────────┐ ┌──────────┐
│Success │ │  Error   │
└───┬────┘ └────┬─────┘
    │           │
    │           ▼
    │      ┌──────────┐
    │      │SnackBar: │
    │      │"Sync     │
    │      │failed"   │
    │      └──────────┘
    │
    ▼
┌──────────────────┐
│ Check duplicates │
│ Filter new URLs  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Append to file   │
│ Commit to GitHub │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Mark URLs synced │
│ in local DB      │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Update UI        │
│ badges → "✓"     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ SnackBar:        │
│ "X URLs synced"  │
└──────────────────┘
```

---

## Wireframes et maquettes

### Screen 1 : SettingsScreen (Configuration)

```
╔═══════════════════════════════════════╗
║  ← Settings                           ║
╠═══════════════════════════════════════╣
║                                       ║
║  GitHub Configuration                 ║
║  ────────────────────                 ║
║                                       ║
║  Username                             ║
║  ┌─────────────────────────────────┐ ║
║  │ dgirard                         │ ║
║  └─────────────────────────────────┘ ║
║                                       ║
║  Repository                           ║
║  ┌─────────────────────────────────┐ ║
║  │ veille                          │ ║
║  └─────────────────────────────────┘ ║
║                                       ║
║  Branch                               ║
║  ┌─────────────────────────────────┐ ║
║  │ main                            │ ║
║  └─────────────────────────────────┘ ║
║                                       ║
║  ─────────────────────────────────── ║
║                                       ║
║  Authentication                       ║
║  ────────────────                     ║
║                                       ║
║  Status: Not connected                ║
║                                       ║
║  ┌─────────────────────────────────┐ ║
║  │  🔗 Connect with GitHub OAuth   │ ║
║  └─────────────────────────────────┘ ║
║                                       ║
║  ┌─────────────────────────────────┐ ║
║  │  🔑 Use Personal Access Token   │ ║
║  └─────────────────────────────────┘ ║
║                                       ║
║  ─────────────────────────────────── ║
║                                       ║
║           ┌───────────────┐           ║
║           │  Save Config  │           ║
║           └───────────────┘           ║
║                                       ║
╚═══════════════════════════════════════╝
```

**État : Authenticated**
```
║  Authentication                       ║
║  ────────────────                     ║
║                                       ║
║  Status: ✓ Connected as @dgirard      ║
║                                       ║
║  ┌─────────────────────────────────┐ ║
║  │      Disconnect                 │ ║
║  └─────────────────────────────────┘ ║
```

### Screen 2 : UrlListScreen (Liste des URLs)

**État : Liste avec URLs**
```
╔═══════════════════════════════════════╗
║  URLs to Process          ⚙️  🔄      ║
╠═══════════════════════════════════════╣
║                                       ║
║  ┌─────────────────────────────────┐ ║
║  │ https://anthropic.com/blog/...  │ ║
║  │ ✓ Synced                        │ ║
║  │ 2025-10-23 14:23                │🗑║
║  └─────────────────────────────────┘ ║
║                                       ║
║  ┌─────────────────────────────────┐ ║
║  │ https://flutter.dev/docs/...    │ ║
║  │ 📱 Local                        │ ║
║  │ 2025-10-23 15:47                │🗑║
║  └─────────────────────────────────┘ ║
║                                       ║
║  ┌─────────────────────────────────┐ ║
║  │ https://github.blog/...         │ ║
║  │ 📱 Local                        │ ║
║  │ 2025-10-23 16:12                │🗑║
║  └─────────────────────────────────┘ ║
║                                       ║
║                                       ║
║                                  ┌──┐ ║
║                                  │🔄│ ║
║                                  └──┘ ║
╚═══════════════════════════════════════╝
```

**État : Liste vide**
```
╔═══════════════════════════════════════╗
║  URLs to Process          ⚙️  🔄      ║
╠═══════════════════════════════════════╣
║                                       ║
║                                       ║
║           📭                          ║
║                                       ║
║      No URLs pending                  ║
║                                       ║
║   Share a link to get started         ║
║                                       ║
║                                       ║
╚═══════════════════════════════════════╝
```

**État : Synchronisation en cours**
```
╔═══════════════════════════════════════╗
║  URLs to Process          ⚙️  🔄      ║
╠═══════════════════════════════════════╣
║                                       ║
║  ┌─────────────────────────────────┐ ║
║  │ ⏳ Syncing 2 URLs...            │ ║
║  │ ▓▓▓▓▓▓▓▓░░░░░░░░                │ ║
║  └─────────────────────────────────┘ ║
║                                       ║
║  ┌─────────────────────────────────┐ ║
║  │ https://flutter.dev/docs/...    │ ║
║  │ 📱 Local                        │ ║
║  │ 2025-10-23 15:47                │🗑║
║  └─────────────────────────────────┘ ║
║                                       ║
╚═══════════════════════════════════════╝
```

### Screen 3 : ShareReceiverActivity (Activité transparente)

**Visuel :** Pas d'écran visible, seulement un Toast en bas de l'écran courant

```
┌───────────────────────────────────────┐
│                                       │
│  [Navigateur ou autre app continue]  │
│                                       │
│                                       │
│  ┌─────────────────────────────────┐ │
│  │ ✓ URL saved locally             │ │ ← Toast
│  └─────────────────────────────────┘ │
└───────────────────────────────────────┘
```

### Dialog : OAuth Flow

**Étape 1 : Confirmation**
```
╔═══════════════════════════════════════╗
║  Authenticate with GitHub             ║
╠═══════════════════════════════════════╣
║                                       ║
║  You will be redirected to GitHub     ║
║  to authorize Mobile-Share.           ║
║                                       ║
║  Permissions requested:               ║
║  • Read/Write repository access       ║
║                                       ║
║  ┌───────────┐      ┌──────────┐     ║
║  │  Cancel   │      │ Continue │     ║
║  └───────────┘      └──────────┘     ║
╚═══════════════════════════════════════╝
```

**Étape 2 : Browser GitHub OAuth (externe)**

**Étape 3 : Retour app avec succès**
```
╔═══════════════════════════════════════╗
║  ✓ Authentication successful          ║
╠═══════════════════════════════════════╣
║                                       ║
║  Connected as @dgirard                ║
║                                       ║
║           ┌──────────┐                ║
║           │   OK     │                ║
║           └──────────┘                ║
╚═══════════════════════════════════════╝
```

### Dialog : Personal Access Token (PAT)

```
╔═══════════════════════════════════════╗
║  Personal Access Token                ║
╠═══════════════════════════════════════╣
║                                       ║
║  Enter your GitHub PAT with           ║
║  'repo' scope.                        ║
║                                       ║
║  ┌─────────────────────────────────┐ ║
║  │ ghp_xxxxxxxxxxxxxxxxxxxx        │ ║
║  └─────────────────────────────────┘ ║
║                                       ║
║  📘 How to create a PAT?              ║
║                                       ║
║  ┌───────────┐      ┌──────────┐     ║
║  │  Cancel   │      │   Save   │     ║
║  └───────────┘      └──────────┘     ║
╚═══════════════════════════════════════╝
```

---

## Spécifications des composants

### Composant : URL Card (Item de liste)

**Anatomie :**
```
┌─────────────────────────────────────────────┐
│ https://example.com/article              🗑 │ ← URL (cliquable) + Delete button
│ [Badge: ✓ Synced | 📱 Local]                │ ← Status badge
│ 2025-10-23 14:23                            │ ← Timestamp
└─────────────────────────────────────────────┘
```

**Spécifications :**
- **Hauteur** : 80dp
- **Padding** : 16dp horizontal, 12dp vertical
- **URL** :
  - Typographie : Body1 (16px)
  - Couleur : Text Primary (#212121)
  - Max lines : 2, ellipsis
  - Tap : Ouvre URL dans navigateur
- **Badge** :
  - Synced : Chip vert (#4CAF50), texte "✓ Synced"
  - Local : Chip orange (#FF9800), texte "📱 Local"
  - Typographie : Caption (12px)
  - Padding : 6dp horizontal, 4dp vertical
- **Timestamp** :
  - Typographie : Caption (12px)
  - Couleur : Text Secondary (#757575)
  - Format : YYYY-MM-DD HH:mm
- **Delete button** :
  - Icon : Material Icons `delete`
  - Taille : 24dp
  - Couleur : Text Secondary, devient Error on hover
  - Action : Swipe to delete OU tap icon

**États :**
1. **Normal** : Comme ci-dessus
2. **Pressed** : Ripple effect
3. **Swipe left** : Révèle fond rouge avec icône delete
4. **Deleting** : Fade out animation (300ms)

### Composant : FloatingActionButton (Sync)

**Spécifications :**
- **Position** : Bottom-right, 16dp margin
- **Taille** : 56dp x 56dp
- **Couleur** : Primary (#2196F3)
- **Icon** : Material Icons `sync`, blanc, 24dp
- **Élévation** : 6dp
- **Visible** : Seulement si URLs non-synced > 0

**États :**
1. **Idle** : Icon statique
2. **Syncing** : Icon rotation animation (360°, 1s, repeat)
3. **Success** : Icon change to `check` (300ms), puis retour `sync`
4. **Error** : Icon shake animation (300ms)

### Composant : Empty State

**Anatomie :**
```
        📭

   No URLs pending

Share a link to get started
```

**Spécifications :**
- **Icon** : Emoji 📭 ou Material Icon `inbox`, 64dp, couleur Text Secondary
- **Headline** : Headline 2 (20px), Text Primary
- **Subtitle** : Body2 (14px), Text Secondary
- **Vertical spacing** : 16dp entre éléments
- **Centré** : Verticalement et horizontalement

### Composant : Sync Progress Indicator

**Anatomie :**
```
┌─────────────────────────────────────┐
│ ⏳ Syncing 3 URLs...                │
│ ▓▓▓▓▓▓▓▓░░░░░░░░  50%              │
└─────────────────────────────────────┘
```

**Spécifications :**
- **Container** : Card, padding 16dp, margin 16dp
- **Couleur fond** : Surface (#F5F5F5)
- **Progress bar** : LinearProgressIndicator, Primary color
- **Text** : Body2, Text Primary
- **Animation** : Smooth progress 0-100%

### Composant : Toast Notification

**Types :**
1. **Success** : "✓ URL saved" / "✓ URL saved and synced"
2. **Info** : "URL already saved"
3. **Error** : "Invalid URL" / "Sync failed"

**Spécifications :**
- **Durée** : 2 secondes
- **Position** : Bottom, 48dp from bottom
- **Background** : Dark gray (#424242) avec 90% opacity
- **Text** : Blanc, Body2 (14px)
- **Padding** : 16dp horizontal, 12dp vertical
- **Border radius** : 4dp
- **Animation** : Slide up + fade in (200ms), fade out (150ms)

### Composant : SnackBar (post-sync)

**Exemple :**
```
┌─────────────────────────────────────────┐
│ ✓ 3 URLs synced to GitHub      [UNDO]  │
└─────────────────────────────────────────┘
```

**Spécifications :**
- **Durée** : 4 secondes
- **Position** : Bottom, au-dessus du FAB si présent
- **Background** : Primary (#2196F3)
- **Text** : Blanc, Body2
- **Action button** : "VIEW" (ouvre repo GitHub) OU "UNDO" (si applicable)
- **Animation** : Slide up (250ms)

---

## États et gestion d'erreurs

### États de l'application

#### 1. États d'authentification (AuthBLoC)

| État | Description | UI Impact |
|------|-------------|-----------|
| `AuthUnauthenticated` | Pas de token valide | Redirect vers SettingsScreen |
| `AuthInProgress` | OAuth en cours | Loading spinner sur SettingsScreen |
| `AuthAuthenticated` | Token valide | Enable partage et sync |
| `AuthError` | Échec authentification | Dialog erreur + retry option |
| `TokenExpired` | Token expiré (401) | Notification "Re-authenticate required" |

#### 2. États de synchronisation (SyncBLoC)

| État | Description | UI Impact |
|------|-------------|-----------|
| `SyncIdle` | Aucune sync en cours | FAB normal |
| `Syncing` | Sync en cours | FAB icon rotation + progress card |
| `SyncSuccess` | Sync réussie | SnackBar success + update badges |
| `SyncPartialSuccess` | Certaines URLs synced | SnackBar warning avec détails |
| `SyncError` | Échec sync | SnackBar error + URLs restent local |

#### 3. États des URLs (UrlBLoC)

| État | Description | UI Impact |
|------|-------------|-----------|
| `UrlsLoading` | Chargement depuis DB | Shimmer placeholders |
| `UrlsLoaded` | Liste chargée | Affichage liste ou empty state |
| `UrlAdded` | URL ajoutée | Animation insert + Toast |
| `UrlDeleted` | URL supprimée | Animation remove |
| `UrlError` | Erreur DB | SnackBar error |

### Gestion des erreurs

#### Erreurs réseau

| Erreur | Cause | Message utilisateur | Action corrective |
|--------|-------|---------------------|-------------------|
| `NoInternetConnection` | Pas de réseau | "No internet connection. URL saved locally." | Retry automatique quand réseau revient |
| `TimeoutException` | Timeout API GitHub | "Request timeout. Please try again." | Bouton retry |
| `ServerError (5xx)` | GitHub down | "GitHub is temporarily unavailable. Try later." | Retry avec backoff exponentiel |

#### Erreurs d'authentification

| Erreur | Cause | Message utilisateur | Action corrective |
|--------|-------|---------------------|-------------------|
| `InvalidToken` | Token malformé | "Invalid token. Please re-authenticate." | Redirect vers settings |
| `Unauthorized (401)` | Token expiré/révoqué | "Session expired. Please log in again." | Clear token + redirect auth |
| `Forbidden (403)` | Permissions insuffisantes | "Insufficient permissions. Check token scope." | Guide vers GitHub settings |

#### Erreurs de configuration

| Erreur | Cause | Message utilisateur | Action corrective |
|--------|-------|---------------------|-------------------|
| `RepositoryNotFound` | Repo inexistant | "Repository not found. Check settings." | Redirect vers settings |
| `BranchNotFound` | Branche inexistante | "Branch 'X' not found. Using default branch." | Fallback vers default branch |
| `InvalidUsername` | Username invalide | "Invalid GitHub username." | Validation inline |

#### Erreurs de données

| Erreur | Cause | Message utilisateur | Action corrective |
|--------|-------|---------------------|-------------------|
| `InvalidUrl` | URL malformée | "Invalid URL format." | Ignore silencieusement |
| `DuplicateUrl` | URL déjà existe | (Rien - silent skip) | Pas de message |
| `FileTooLarge` | Fichier > 1MB | "Too many URLs. Consider archiving old ones." | Suggérer cleanup |
| `ConflictError` | SHA mismatch | "File was modified. Retrying..." | Retry automatique avec nouveau SHA |

### Scénarios edge cases

#### Cas 1 : Partage multiple rapide
**Problème :** User partage 5 URLs en 10 secondes
**Solution :** Queue les requêtes, process séquentiellement, feedback groupé

#### Cas 2 : App tuée pendant sync
**Problème :** Process killed, URLs semi-synced
**Solution :** Transaction atomique, rollback si échec, retry au prochain lancement

#### Cas 3 : Fichier GitHub supprimé manuellement
**Problème :** 404 sur GET file
**Solution :** Créer automatiquement avec message "File recreated by mobile-share"

#### Cas 4 : Changement de repo/branch
**Problème :** URLs existantes pour ancien repo
**Solution :** Dialog confirmation "URLs will be re-synced to new repo. Continue?"

#### Cas 5 : Révocation token pendant utilisation
**Problème :** 401 mid-session
**Solution :** Catch 401 → AuthEvent.TokenExpired → Notification persistante

---

## Annexes

### A. GitHub API Endpoints utilisés

```
POST https://github.com/login/oauth/access_token
  → Exchange code for token

GET /repos/{owner}/{repo}/contents/{path}
  → Read urls-to-process.md
  Response: { content: "base64...", sha: "abc123..." }

PUT /repos/{owner}/{repo}/contents/{path}
  → Update urls-to-process.md
  Body: { message: "...", content: "base64...", sha: "abc123..." }

GET /user
  → Get authenticated user info (for username display)
```

### B. SQLite Schema

```sql
CREATE TABLE pending_urls (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT NOT NULL UNIQUE,
  timestamp INTEGER NOT NULL,
  synced INTEGER NOT NULL DEFAULT 0
);

CREATE INDEX idx_synced ON pending_urls(synced);
CREATE INDEX idx_timestamp ON pending_urls(timestamp DESC);
```

### C. FlutterSecureStorage Keys

```
'github_token' : OAuth/PAT token
'github_username' : GitHub username
'github_repo' : Repository name
'github_branch' : Branch name
'token_type' : 'oauth' | 'pat'
```

### D. Considérations de sécurité

1. **Token Storage** : FlutterSecureStorage (AES encryption, Android Keystore)
2. **HTTPS Only** : Toutes les requêtes API via HTTPS
3. **Input Validation** : Regex validation des URLs, sanitization
4. **Permissions minimales** : Seul scope `repo` nécessaire
5. **No logging sensitive data** : Jamais log tokens ou credentials

### E. Accessibilité

1. **Semantic labels** : Tous les boutons et icônes ont labels
2. **Contrast ratio** : Minimum 4.5:1 pour texte normal
3. **Touch targets** : Minimum 48dp x 48dp
4. **Screen reader** : Support complet TalkBack
5. **Font scaling** : Respect des préférences système (jusqu'à 200%)

### F. Performance

**Objectifs :**
- Cold start : < 2 secondes
- Share to toast : < 1 seconde (local)
- Sync 10 URLs : < 5 secondes (réseau normal)
- Liste 100 URLs : Smooth scrolling (60fps)

**Optimisations :**
- SQLite indexes sur timestamp et synced
- Lazy loading liste (ListView.builder)
- Cache GitHub file SHA (éviter GET si pas modifié)
- Debounce search/filter à 300ms
- Background isolate pour parsing JSON

---

## Changelog

**Version 1.0 - 2025-10-23**
- Design initial approuvé
- Architecture BLoC définie
- Spécifications UX/UI complètes
- User flows documentés
- Gestion d'erreurs détaillée

---

**Document validé le : 2025-10-23**
**Prêt pour : Design UX/UI + Développement**
