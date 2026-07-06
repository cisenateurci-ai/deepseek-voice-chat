import os
import torch
from silero_vad import load_silero_vad

# Répertoire de cache des modèles
os.environ["TORCH_HOME"] = "/app/models/torch"

# Charger le modèle VAD Silero
model = load_silero_vad(onnx=False, jit=True)

def detect_speech(raw_audio: bytes, sample_rate=16000) -> bool:
    """
    Détecte si du son contient de la parole.
    
    Args:
        raw_audio: Bytes audio bruts
        sample_rate: Fréquence d'échantillonnage (défaut 16000 Hz)
    
    Returns:
        True si de la parole est détectée, False sinon
    """
    try:
        import numpy as np
        
        # Convertir les bytes en tensor PyTorch
        audio_data = np.frombuffer(raw_audio, dtype=np.int16).astype(np.float32) / 32768.0
        wav = torch.from_numpy(audio_data)
        
        # Exécuter la détection VAD
        with torch.no_grad():
            speech_prob = model(wav, sample_rate).item()
        
        # Seuil de confiance pour considérer qu'il y a de la parole
        return speech_prob > 0.5
    except Exception as e:
        print(f"Erreur VAD: {e}")
        return True  # Par défaut, considérer qu'il y a de la parole

async def is_speech(raw_audio: bytes, sample_rate=16000) -> bool:
    """Wrapper asynchrone pour la détection de parole"""
    return detect_speech(raw_audio, sample_rate)