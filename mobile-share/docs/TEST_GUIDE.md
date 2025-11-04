# Guide de Test - Mobile-Share

Application déployée avec succès sur **Pixel 7a** (Android 16) ! 🎉

## Configuration Initiale

### 1. Première ouverture
L'application est maintenant ouverte sur votre téléphone. Vous devriez voir l'écran principal avec un message "No URLs yet".

### 2. Configurer GitHub
Pour que l'application fonctionne, vous devez d'abord configurer vos informations GitHub :

1. Tapez sur l'icône **⚙️ Settings** en haut à droite
2. Remplissez les champs :
   - **Username** : Votre nom d'utilisateur GitHub
   - **Repository** : Le nom de votre dépôt (ex: "veille")
   - **Branch** : "main" (ou votre branche par défaut)
   - **Token** : Votre Personal Access Token GitHub

3. Tapez **Save Settings**

### 3. Créer un Personal Access Token GitHub

Si vous n'avez pas encore de token :

1. Allez sur GitHub : https://github.com/settings/tokens
2. Cliquez sur **"Generate new token (classic)"**
3. Donnez un nom : "Mobile-Share"
4. Cochez la case **"repo"** (accès complet aux dépôts)
5. Cliquez sur **"Generate token"**
6. **Copiez le token** (vous ne le verrez qu'une fois !)
7. Collez-le dans l'application

## Tests à Effectuer

### Test 1 : Partager une URL depuis Chrome

1. Ouvrez **Chrome** sur votre téléphone
2. Naviguez vers un site web (ex: https://example.com)
3. Tapez sur le bouton **Partager** (icône de partage)
4. Cherchez **"Save to Veille"** dans la liste
5. Sélectionnez-le

**Résultat attendu** :
- Un toast devrait s'afficher : "URL saved locally"
- L'activité de partage se ferme automatiquement

### Test 2 : Vérifier l'URL dans l'application

1. Ouvrez l'application **Mobile-Share**
2. Vous devriez voir l'URL que vous venez de partager
3. Vérifiez le badge : devrait afficher **"Local"** (pas encore synchronisé)
4. Vérifiez le timestamp (ex: "2 min ago")

### Test 3 : Synchroniser avec GitHub

1. Dans l'application, tapez sur le bouton **🔄 Sync** (en bas à droite)
2. Une barre de progression devrait apparaître
3. Attendez la fin de la synchronisation

**Résultat attendu** :
- Message : "✓ 1 URL(s) synced to GitHub"
- Le badge de l'URL change de "Local" à "Synced"
- Le bouton de sync disparaît (car plus d'URLs non synchronisées)

### Test 4 : Vérifier sur GitHub

1. Allez sur votre dépôt GitHub depuis un navigateur
2. Ouvrez le fichier **urls-to-process.md** à la racine
3. Vérifiez que votre URL y est bien présente

### Test 5 : Tester les doublons

1. Partagez la **même URL** depuis Chrome
2. L'application devrait afficher : "URL already saved"
3. L'URL n'est **pas** ajoutée en doublon

### Test 6 : Supprimer une URL

**Méthode 1 : Swipe**
1. Dans la liste, glissez une URL vers la **gauche**
2. Le fond rouge avec icône de poubelle apparaît
3. Continuez jusqu'au bout pour supprimer

**Méthode 2 : Bouton**
1. Tapez sur l'icône **🗑️** à droite de l'URL
2. L'URL est supprimée immédiatement

**Résultat attendu** :
- Message : "URL deleted"
- L'URL disparaît de la liste

### Test 7 : Ouvrir une URL

1. Tapez sur n'importe quelle URL dans la liste
2. Le lien devrait s'ouvrir dans Chrome

### Test 8 : Ajouter plusieurs URLs

1. Partagez 3-4 URLs différentes depuis Chrome
2. Ouvrez Mobile-Share
3. Vérifiez que toutes les URLs sont listées
4. Synchronisez avec GitHub
5. Vérifiez que le compteur indique le bon nombre (ex: "✓ 4 URL(s) synced")

### Test 9 : Mode hors ligne

1. Activez le **mode avion** sur votre téléphone
2. Partagez une URL depuis Chrome
3. L'URL devrait être sauvegardée localement
4. Essayez de synchroniser → Message d'erreur : "No internet connection"
5. Désactivez le mode avion
6. Synchronisez → Devrait fonctionner

### Test 10 : Rafraîchir la liste

1. Tapez sur l'icône **🔄 Refresh** en haut à droite
2. La liste se recharge

## Vérifications de Qualité

### Performance
- [ ] L'application se lance rapidement (< 2 secondes)
- [ ] Le partage depuis Chrome est instantané
- [ ] La synchronisation est fluide
- [ ] Pas de lag lors du scroll de la liste

### Interface
- [ ] Tous les textes sont lisibles
- [ ] Les icônes sont claires
- [ ] Les couleurs sont cohérentes
- [ ] Les animations sont fluides

### Stabilité
- [ ] Pas de crash lors des tests
- [ ] L'application ne se ferme pas inopinément
- [ ] Les données sont bien persistées (fermer et rouvrir l'app)

## Problèmes Courants et Solutions

### "Authentication failed"
**Cause** : Token GitHub invalide ou expiré
**Solution** : Générez un nouveau token avec le scope "repo"

### "Repository not found"
**Cause** : Nom d'utilisateur ou de dépôt incorrect
**Solution** : Vérifiez l'orthographe exacte de votre username et repo

### "No internet connection"
**Cause** : Téléphone hors ligne ou problème réseau
**Solution** : Vérifiez votre connexion Wi-Fi ou données mobiles

### URLs ne s'affichent pas après partage
**Cause** : L'application n'est pas encore ouverte après le partage
**Solution** : Ouvrez l'application Mobile-Share pour voir les URLs

### Le bouton de sync n'apparaît pas
**Cause** : Toutes les URLs sont déjà synchronisées
**Solution** : Normal ! Ajoutez une nouvelle URL pour voir le bouton réapparaître

## Commandes Utiles (Développement)

### Voir les logs de l'application
```bash
adb -s 34081JEHN11516 logcat -s flutter
```

### Réinstaller l'application
```bash
flutter install -d 34081JEHN11516
```

### Désinstaller l'application
```bash
adb -s 34081JEHN11516 uninstall com.veille.mobile_share
```

### Vider les données de l'application
```bash
adb -s 34081JEHN11516 shell pm clear com.veille.mobile_share
```

## Données de Test

### URLs de test à partager
- https://flutter.dev
- https://github.com
- https://stackoverflow.com
- https://developer.android.com
- https://dart.dev

## Checklist Complète

### Configuration
- [ ] Settings configurés (username, repo, token)
- [ ] Authentification réussie
- [ ] Repo GitHub accessible

### Fonctionnalités Core
- [ ] Partager URL depuis Chrome fonctionne
- [ ] URLs apparaissent dans la liste
- [ ] Badge "Local" affiché correctement
- [ ] Synchronisation vers GitHub fonctionne
- [ ] Badge "Synced" après sync
- [ ] Fichier urls-to-process.md créé sur GitHub
- [ ] Détection de doublons fonctionne

### Interface Utilisateur
- [ ] Empty state s'affiche quand aucune URL
- [ ] Liste d'URLs s'affiche correctement
- [ ] Timestamps formatés (ex: "5 min ago")
- [ ] Bouton sync apparaît/disparaît correctement
- [ ] Progress bar lors de la sync
- [ ] Messages toast pour feedback

### Gestion des URLs
- [ ] Supprimer par swipe fonctionne
- [ ] Supprimer par bouton fonctionne
- [ ] Ouvrir URL lance Chrome
- [ ] Refresh recharge la liste

### Robustesse
- [ ] Mode hors ligne sauvegarde localement
- [ ] Messages d'erreur sont clairs
- [ ] Pas de crash
- [ ] Données persistées après fermeture

## Résultat Attendu

✅ **Application fonctionnelle et prête pour utilisation quotidienne**

Vous devriez pouvoir :
1. Partager des URLs depuis n'importe quelle application
2. Les voir listées dans Mobile-Share
3. Les synchroniser vers votre dépôt GitHub
4. Les retrouver dans `urls-to-process.md`

---

**Bon test ! 🚀**

Si vous rencontrez des problèmes, consultez les logs avec :
```bash
adb -s 34081JEHN11516 logcat -s flutter
```
