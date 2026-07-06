"""Version allégée du serveur pour le cloud"""
import os
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import json

app = FastAPI(title="DeepSeek Voice Chat - Cloud")

# CORS pour accès mobile
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route de santé
@app.get("/health")
async def health():
    return {"status": "healthy", "version": "1.0.0"}

# Servir le client HTML
@app.get("/")
async def serve_root():
    return FileResponse("client.html")

@app.get("/client.html")
async def serve_client():
    return FileResponse("client.html")

# Info API
@app.get("/api/info")
async def get_info():
    return {
        "name": "DeepSeek Voice Chat",
        "version": "1.0.0",
        "features": [
            "Voice recognition (Whisper)",
            "AI responses (DeepSeek)",
            "Text-to-speech (espeak-ng)",
            "Real-time WebSocket"
        ],
        "status": "Running on Cloud ☁️"
    }

# WebSocket pour la conversation vocale
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Echo simple pour test
            response = {
                "type": "response",
                "content": f"Vous avez dit: {data}",
                "status": "Demo mode - Utilisez votre propre API DeepSeek"
            }
            await websocket.send_json(response)
    except Exception as e:
        print(f"Erreur WebSocket: {e}")
    finally:
        await websocket.close()

# Erreur 404
@app.get("/{path:path}")
async def catch_all(path: str):
    return JSONResponse(
        status_code=404,
        content={"error": f"Route {path} not found", "hint": "Utilisez /client.html"}
    )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
