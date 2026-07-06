#!/bin/bash

# Script de lancement du projet DeepSeek Voice Chat

echo "🚀 Démarrage de DeepSeek Voice Chat..."

# Vérifier si Docker Compose est installé
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose n'est pas installé"
    exit 1
fi

# Vérifier si .env existe, sinon le créer
if [ ! -f .env ]; then
    echo "📝 Création du fichier .env..."
    echo "DEEPSEEK_API_KEY=your-api-key-here" > .env
fi

# Construire et lancer les conteneurs
echo "🐳 Construction et lancement des conteneurs..."
docker-compose up -d --build

if [ $? -eq 0 ]; then
    echo "✅ Serveur démarré avec succès!"
    echo ""
    echo "📍 Accédez à l'interface à: http://localhost:8080/client.html"
    echo ""
    echo "Pour servir le client HTML, ouvrez un autre terminal et exécutez:"
    echo "  python3 -m http.server 8080"
    echo ""
    echo "Pour voir les logs du serveur:"
    echo "  docker-compose logs -f"
    echo ""
    echo "Pour arrêter le serveur:"
    echo "  docker-compose down"
else
    echo "❌ Erreur lors du démarrage"
    exit 1
fi