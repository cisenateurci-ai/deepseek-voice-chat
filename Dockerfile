FROM python:3.10-slim

WORKDIR /app

# Installation des dépendances système nécessaires à PyAudio / wave etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    libsndfile1 \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers de dépendances et installation Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY *.py .
COPY client.html .

# Volume pour persister les modèles téléchargés (Silero VAD, Whisper)
VOLUME /app/models

# Exposition du port WebSocket
EXPOSE 8000

# Commande de démarrage
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]