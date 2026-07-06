import os
from faster_whisper import WhisperModel
import io
import wave

# Répertoire de cache des modèles
os.environ["HF_HOME"] = "/app/models"
os.environ["TORCH_HOME"] = "/app/models/torch"

# Charger le modèle Whisper (base pour un bon équilibre vitesse/qualité)
model = WhisperModel("base", device="cpu", compute_type="int8", download_root="/app/models/whisper")

async def transcribe_stream(raw_audio: bytes, sample_rate=16000) -> str:
    """
    Transcrit un flux audio brut en texte.
    
    Args:
        raw_audio: Bytes audio bruts (PCM 16-bit)
        sample_rate: Fréquence d'échantillonnage (défaut 16000 Hz)
    
    Returns:
        Texte transcrit
    """
    try:
        # Créer un buffer WAV en mémoire
        wav_buffer = io.BytesIO()
        with wave.open(wav_buffer, 'wb') as wf:
            wf.setnchannels(1)  # Mono
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(sample_rate)
            wf.writeframes(raw_audio)
        
        wav_buffer.seek(0)
        
        # Transcrire avec Whisper
        segments, _ = model.transcribe(wav_buffer, beam_size=5, language="fr")
        text = " ".join(seg.text for seg in segments).strip()
        
        return text if text else "(silence détecté)"
    except Exception as e:
        print(f"Erreur STT: {e}")
        return f"[Erreur transcription: {str(e)}]"