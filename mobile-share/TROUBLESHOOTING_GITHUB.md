# 🔧 Résolution du problème "Access Denied" / "Verify Repository Permission"

## Diagnostic Rapide

### ✅ Checklist : Vérifiez ces 5 points dans l'ordre

#### 1. Vérifiez que votre dépôt GitHub existe

Ouvrez votre navigateur et allez sur :
```
https://github.com/VOTRE_USERNAME/VOTRE_REPO
```

**Remplacez** :
- `VOTRE_USERNAME` par votre nom d'utilisateur GitHub
- `VOTRE_REPO` par le nom de votre dépôt

**Résultat attendu** : La page du dépôt s'affiche
**Si erreur 404** : Le dépôt n'existe pas → créez-le d'abord

---

#### 2. Vérifiez le nom exact du dépôt

Dans l'application Mobile-Share → Settings :

**Username** : Doit être EXACTEMENT votre nom d'utilisateur GitHub
- ❌ Erreur : `Didier Girard` (avec espace)
- ❌ Erreur : `didier-girard` (avec tiret si c'est pas le bon)
- ✅ Correct : `didiergirard` (tel quel sur GitHub)

**Repository** : Doit être EXACTEMENT le nom du dépôt
- ❌ Erreur : `https://github.com/didiergirard/veille` (URL complète)
- ❌ Erreur : `veille/` (avec slash)
- ✅ Correct : `veille` (juste le nom)

**Branch** : Doit être la branche par défaut
- ❌ Erreur : `master` (si votre branche est `main`)
- ✅ Correct : `main` (la plupart des nouveaux dépôts)
- ✅ Correct : `master` (anciens dépôts)

**Pour vérifier la branche par défaut** :
- Allez sur votre dépôt GitHub
- Regardez en haut à gauche, le bouton de branche affiche la branche actuelle

---

#### 3. Créez un nouveau Personal Access Token

**Étapes détaillées** :

1. Allez sur : https://github.com/settings/tokens

2. Cliquez sur **"Generate new token"** → **"Generate new token (classic)"**

3. Remplissez le formulaire :
   - **Note** : `Mobile-Share-App`
   - **Expiration** : `No expiration` (ou 90 jours)

4. **CRITIQUE** : Cochez le scope **`repo`** :
   ```
   ☑ repo (Full control of private repositories)
     ☑ repo:status (Access commit status)
     ☑ repo_deployment (Access deployment status)
     ☑ public_repo (Access public repositories)
     ☑ repo:invite (Access repository invitations)
     ☑ security_events (Read and write security events)
   ```

   **⚠️ IMPORTANT** : Si vous ne cochez que `public_repo`, ça ne marchera PAS pour les dépôts privés !

5. Cliquez sur **"Generate token"** en bas de la page

6. **COPIEZ LE TOKEN** (commence par `ghp_...`)
   - ⚠️ Vous ne le verrez qu'une seule fois !
   - Exemple : `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

#### 4. Entrez le token dans l'application

Sur votre téléphone :

1. Ouvrez **Mobile-Share**
2. Tapez sur **⚙️ Settings**
3. Dans le champ **GitHub Token** :
   - Effacez l'ancien token
   - Collez le NOUVEAU token (celui que vous venez de copier)
4. Tapez **Save Settings**

**Vous devriez voir** :
- Un message vert : "Settings saved successfully"
- Le statut d'authentification passe à "Authenticated"

---

#### 5. Testez la synchronisation

1. Partagez une URL depuis Chrome vers "Save to Veille"
2. Ouvrez Mobile-Share
3. Tapez le bouton **🔄 Sync**

**Résultat attendu** :
- Message : "✓ 1 URL(s) synced to GitHub"
- Le badge de l'URL change de "Local" à "Synced"

**Si ça marche** : ✅ Problème résolu !

**Si ça ne marche toujours pas** : Continuez ci-dessous ⬇️

---

## 🔍 Diagnostic Avancé

### Test manuel du token depuis votre ordinateur

Ouvrez un terminal et testez votre token :

```bash
# Test 1 : Vérifier que le token fonctionne
curl -H "Authorization: Bearer ghp_VotreTOKEN" https://api.github.com/user

# Résultat attendu : vos informations GitHub en JSON
```

```bash
# Test 2 : Vérifier l'accès au dépôt
curl -H "Authorization: Bearer ghp_VotreTOKEN" \
     https://api.github.com/repos/VOTRE_USERNAME/VOTRE_REPO

# Résultat attendu : informations du dépôt en JSON
# Si erreur 404 : le dépôt n'existe pas
# Si erreur 403 : le token n'a pas accès
```

```bash
# Test 3 : Vérifier les scopes du token
curl -v -H "Authorization: Bearer ghp_VotreTOKEN" \
     https://api.github.com/user 2>&1 | grep x-oauth-scopes

# Résultat attendu : x-oauth-scopes: repo, ...
# Si "repo" n'apparaît pas : le token n'a pas les bonnes permissions
```

---

## 🆘 Problèmes Spécifiques

### Erreur : "Repository not found"

**Causes possibles** :
1. Le nom du dépôt est mal orthographié
2. Le dépôt est privé et le token n'a pas accès
3. Le dépôt n'existe pas encore

**Solution** :
- Créez le dépôt sur GitHub si nécessaire
- Vérifiez l'orthographe exacte (majuscules/minuscules comptent !)

---

### Erreur : "Access denied" ou "403 Forbidden"

**Causes possibles** :
1. Le token n'a pas le scope `repo`
2. Le token a expiré
3. Le token a été révoqué

**Solution** :
- Créez un NOUVEAU token avec le scope `repo`
- NE PAS réutiliser un ancien token

---

### Erreur : "Invalid credentials" ou "401 Unauthorized"

**Causes possibles** :
1. Le token est incorrect
2. Le token a été supprimé sur GitHub

**Solution** :
- Vérifiez que vous avez bien copié tout le token (commence par `ghp_`)
- Créez un nouveau token si nécessaire

---

### Erreur : "Rate limit exceeded"

**Causes possibles** :
1. Trop de requêtes à l'API GitHub

**Solution** :
- Attendez 1 heure
- Utilisez un token (augmente la limite à 5000 requêtes/heure)

---

## 📋 Récapitulatif de la Configuration Correcte

Sur GitHub (https://github.com/settings/tokens) :
```
Token Name: Mobile-Share-App
Expiration: No expiration
Scopes: ☑ repo (avec toutes les sous-cases)
```

Dans Mobile-Share → Settings :
```
Username:   didiergirard          (votre username exact)
Repository: veille                 (juste le nom, pas l'URL)
Branch:     main                   (ou master selon votre dépôt)
Token:      ghp_xxxxxxxxxxxx...    (le token complet)
```

Sur votre dépôt GitHub :
```
URL: https://github.com/didiergirard/veille
Le fichier urls-to-process.md sera créé automatiquement à la racine
```

---

## ✅ Vérification Finale

Avant de tester à nouveau, vérifiez que TOUS ces points sont corrects :

- [ ] Le dépôt existe sur GitHub
- [ ] Le nom d'utilisateur est correct (sans espace, sans majuscule incorrecte)
- [ ] Le nom du dépôt est correct (juste le nom, pas l'URL)
- [ ] La branche est correcte (`main` ou `master`)
- [ ] Le token a été créé avec le scope **repo** complet
- [ ] Le token a été copié en ENTIER (commence par `ghp_`)
- [ ] Le token a été collé dans l'application
- [ ] Les settings ont été sauvegardés

Si TOUS ces points sont cochés et que ça ne marche toujours pas, il y a un bug dans l'application qu'il faudra corriger.

---

**Bonne chance ! 🚀**
