# 🚀 Guide de Déploiement Cloud

Déployez le DeepSeek Voice Chat sur le cloud GRATUITEMENT ! ☁️

---

## 📊 Comparaison des plateformes

| Plateforme | Gratuit | Facilité | Temps démarrage | Limite |
|-----------|--------|---------|-----------------|--------|
| **Railway** | ✅ $5/mois | ⭐⭐⭐ | 30s | 500h/mois |
| **Render** | ✅ | ⭐⭐⭐ | 2m | Auto-sleep |
| **Fly.io** | ✅ | ⭐⭐ | 1m | 3 shared-cpu |
| **Heroku** | ❌ (payant) | ⭐⭐⭐ | 30s | - |

---

## 🚄 Option 1 : Railway (Recommandé) ⭐

### Étapes :

1. **Aller sur https://railway.app**
2. **Se connecter avec GitHub**
3. **Cliquer sur "New Project"**
4. **Sélectionner "Deploy from GitHub repo"**
5. **Choisir votre repo `deepseek-voice-chat`**
6. **Railway configure automatiquement tout**
7. **Attendre 2-3 minutes**
8. **Votre URL sera : `https://votre-projet.up.railway.app`**

### Utilisation sur téléphone :
```
https://votre-projet.up.railway.app/client.html
```

---

## 🎨 Option 2 : Render

### Étapes :

1. **Aller sur https://render.com**
2. **Se connecter avec GitHub**
3. **Cliquer sur "+ New Web Service"**
4. **Connecter votre repo GitHub**
5. **Remplir les infos :**
   - **Name** : `deepseek-voice-chat`
   - **Runtime** : `Python 3`
   - **Build command** : `pip install -r requirements-cloud.txt`
   - **Start command** : `uvicorn server:app --host 0.0.0.0 --port $PORT`
6. **Cliquer "Create Web Service"**
7. **Attendre 5-10 minutes**
8. **Votre URL sera : `https://deepseek-voice-chat.onrender.com`**

---

## ✈️ Option 3 : Fly.io

### Étapes :

1. **Installer Fly CLI** :
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Se connecter** :
   ```bash
   flyctl auth login
   ```

3. **Créer l'app** :
   ```bash
   flyctl launch --image deepseek-voice-chat
   ```

4. **Déployer** :
   ```bash
   flyctl deploy
   ```

5. **Votre URL sera : `https://deepseek-voice-chat.fly.dev`**

---

## 🔑 Configuration des variables d'environnement

### Sur Railway :
1. Aller à **"Variables"**
2. Ajouter :
   ```
   DEEPSEEK_API_KEY=sk_live_votre_clé_ici
   ```

### Sur Render :
1. Aller à **"Environment"**
2. Ajouter la même clé

---

## 📱 Accès sur téléphone Android

Une fois déployé :

1. **Ouvrez Chrome sur votre téléphone**
2. **Allez à : `https://votre-domaine.app/client.html`**
3. **Autorisez l'accès au micro**
4. **Commencez à parler !** 🎤

---

## ⚡ Optimisation pour mobile

L'interface est déjà optimisée pour :
- ✅ Petits écrans
- ✅ Connexions lentes
- ✅ HTTPS (obligatoire pour le micro)
- ✅ Mode hors ligne partiellement

---

## 🔧 Dépannage

### "Erreur de connexion WebSocket"
- Vérifiez que vous utilisez **HTTPS** (pas HTTP)
- Sur Railway/Render, c'est automatique

### "Le serveur prend du temps au premier appel"
- C'est normal, les modèles se chargent
- Après 5 minutes, ce sera rapide

### "Le conteneur s'arrête après 30 minutes"
- Railway maintient le serveur actif
- Render met en sleep après 15 min (free plan)

---

## 💰 Coûts estimés

- **Railway** : $5-10/mois (très bon rapport)
- **Render** : Gratuit (avec limitations)
- **Fly.io** : $5-15/mois (si dépassement)
- **Heroku** : $7/mois minimum (après fermeture de l'offre gratuite)

---

## ✅ Checklist finale

- [ ] Code pushé sur GitHub
- [ ] Plateforme choisie
- [ ] Repo connecté
- [ ] Variables d'env configurées
- [ ] Déploiement lancé
- [ ] URL accessible
- [ ] Micro fonctionne sur téléphone

---

**Besoin d'aide ? Ouvrez une issue sur GitHub !** 🆘
