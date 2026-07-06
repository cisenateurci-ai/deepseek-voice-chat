from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
import asyncio
import json
import os

from vad import is_speech
from stt import transcribe_stream
from llm import query_deepseek
from tts import synthesize

app = FastAPI(title="DeepSeek Voice Chat")

# Servir les fichiers statiques (client.html)
@app.get("/")
async def get_root():
    if os.path.exists("client.html"):
        return FileResponse("client.html", media_type="text/html")
    return {"message": "DeepSeek Voice Chat Server - Connectez-vous via WebSocket sur /ws"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    try:
        while True:
            # Recevoir l'audio brut du client
            data = await websocket.receive_bytes()
            
            # Déterminer le type de message
            if len(data) < 5:
                continue
            
            # Les 4 premiers bytes indiquent le type
            msg_type = data[:4].decode('utf-8', errors='ignore')
            payload = data[4:]
            
            if msg_type == "AUDR":  # Audio Raw
                # Vérifier s'il y a de la parole
                has_speech = await is_speech(payload, sample_rate=16000)
                
                if has_speech:
                    # Transcrire l'audio
                    text = await transcribe_stream(payload, sample_rate=16000)
                    await websocket.send_json({"type": "text", "content": text})
                    
                    # Obtenir la réponse de DeepSeek
                    response = await query_deepseek(text)
                    await websocket.send_json({"type": "response", "content": response})
                    
                    # Synthétiser la réponse en audio
                    audio = await synthesize(response)
                    if audio:
                        await websocket.send_bytes(b"AUDT" + audio)  # AUDT = Audio Transcribed
                    
            elif msg_type == "PING":  # Keep-alive
                await websocket.send_json({"type": "pong"})
    
    except WebSocketDisconnect:
        print("Client déconnecté")
    except Exception as e:
        print(f"Erreur WebSocket: {e}")
        await websocket.send_json({"type": "error", "content": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)