# 🎤 DeepSeek Voice Chat - Conversation Vocale IA

Une application web de chat vocal en temps réel utilisant **DeepSeek AI**, **Whisper** pour la transcription et **TTS** pour la synthèse vocale.

## ✨ Caractéristiques

- 🎙️ **Enregistrement audio** en temps réel via le navigateur
- 🗣️ **Transcription française** avec Whisper (OpenAI)
- 🤖 **Réponses IA** alimentées par DeepSeek
- 🔊 **Synthèse vocale** pour les réponses
- 🐳 **Entièrement dockerisé** - Déployable n'importe où
- 💾 **Modèles persistants** - Pas de re-téléchargement à chaque démarrage

## 🚀 Démarrage rapide

### Avec Docker Compose (recommandé)

```bash
# 1. Cloner le projet
git clone https://github.com/cisenateurci-ai/deepseek-voice-chat.git
cd deepseek-voice-chat

# 2. Lancer avec Docker Compose
docker-compose up -d --build

# 3. Servir le client HTML (dans un autre terminal)
python3 -m http.server 8080

# 4. Accédez à http://localhost:8080/client.html
```

### Sans Docker (développement local)

```bash
# 1. Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # ou `venv\Scripts\activate` sur Windows

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le serveur
uvicorn server:app --host 0.0.0.0 --port 8000

# 4. Dans un autre terminal, servir le client
python3 -m http.server 8080

# 5. Accédez à http://localhost:8080/client.html
```

## 🔧 Configuration

### Utiliser la véritable API DeepSeek

1. Créez un fichier `.env`:
```
DEEPSEEK_API_KEY=sk_live_xxxxxxxxxxxxxxxx
```

2. Décommentez le code de mode réel dans `llm.py`:
```python
# === MODE RÉEL (décommentez pour utiliser l'API DeepSeek) ===
if DEEPSEEK_API_KEY == "dummy-key-for-demo":
    ...
```

3. Relancez le serveur:
```bash
docker-compose restart
# ou
uvicorn server:app --host 0.0.0.0 --port 8000
```

## 📁 Structure du projet

```
deepseek-voice-chat/
├── server.py              # Serveur FastAPI WebSocket principal
├── vad.py                 # Détection de parole (Silero VAD)
├── stt.py                 # Transcription audio (Whisper)
├── llm.py                 # Requêtes à l'API DeepSeek
├── tts.py                 # Synthèse vocale (espeak-ng)
├── client.html            # Interface web (HTML/JS)
├── requirements.txt       # Dépendances Python
├── Dockerfile             # Configuration Docker
├── docker-compose.yml     # Orchestration Docker
├── .dockerignore           # Fichiers ignorés par Docker
├── run.sh                 # Script de lancement
└── README.md              # Ce fichier
```

## 🏗️ Architecture

```
┌─────────────────┐
│   Navigateur    │
│  (client.html)  │
└────────┬────────┘
         │ WebSocket
         │
    ┌────▼─────────────────┐
    │  FastAPI Server      │
    │  (server.py)         │
    ├─────────────────────┤
    │ VAD (vad.py)        │ → Détecte la parole
    │ STT (stt.py)        │ → Whisper → Texte
    │ LLM (llm.py)        │ → DeepSeek → Réponse
    │ TTS (tts.py)        │ → espeak-ng → Audio
    └─────────────────────┘
```

## 🐳 Commandes Docker

```bash
# Démarrer les conteneurs
docker-compose up -d --build

# Voir les logs en direct
docker-compose logs -f

# Arrêter les conteneurs
docker-compose down

# Supprimer tout (conteneurs + images)
docker-compose down --rmi all

# Accéder au shell du conteneur
docker exec -it deepseek-voice-chat /bin/bash
```

## 📋 Dépendances

### Python
- FastAPI - Framework web
- Uvicorn - Serveur ASGI
- faster-whisper - Transcription audio
- torch, torchaudio - IA et audio
- httpx - Requêtes HTTP async
- websockets - Communication temps réel
- silero-vad - Détection de parole

### Système
- libsndfile1 - Traitement audio
- espeak-ng - Synthèse vocale (TTS)
- Python 3.10+

## 🎯 Utilisation

1. **Cliquez sur "🎤 Démarrer"** pour commencer l'enregistrement
2. **Parlez clairement en français** - attendez 1-2 secondes après avoir parlé
3. **Cliquez sur "⏹️ Arrêter"** pour terminer l'enregistrement
4. L'IA transcrit, traite et répond vocalement

## ⚙️ Dépannage

### "Impossible d'accéder au micro"
- Assurez-vous que le navigateur a la permission d'accéder au micro
- Utilisez HTTPS ou localhost (HTTP fonctionne sur localhost)

### "Connexion WebSocket refusée"
```bash
# Vérifiez que le serveur s'exécute
docker-compose ps

# Vérifiez les logs
docker-compose logs voice-server
```

### Les modèles sont réapparus à chaque redémarrage
- Vérifiez que le volume Docker est correctement monté:
```bash
docker volume ls
```

### Erreur "espeak-ng: command not found"
- Le conteneur devrait installer automatiquement espeak-ng
- Si ce n'est pas le cas, exécutez manuellement:
```bash
docker exec deepseek-voice-chat apt-get update && apt-get install -y espeak-ng
```

## 🔒 Sécurité

- Les clés API DeepSeek ne doivent **jamais** être committées au repo
- Utilisez toujours des fichiers `.env` locaux
- Pour la production, utilisez un gestionnaire de secrets (AWS Secrets Manager, etc.)

## 📝 Licence

MIT - Libre d'utilisation

## 🤝 Contribution

Les contributions sont bienvenues! N'hésitez pas à ouvrir des issues ou des pull requests.

---

**Fait avec ❤️ pour les conversations vocales**
