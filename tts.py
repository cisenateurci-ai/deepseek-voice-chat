import os
import tempfile
import subprocess

async def text_to_speech(text: str) -> bytes:
    """
    Convertit du texte en audio (français).
    
    Utilise espeak-ng pour une synthèse vocale rapide et légère.
    
    Args:
        text: Texte à convertir en parole
    
    Returns:
        Bytes audio WAV (16-bit, 16000 Hz, mono)
    """
    
    if not text or text.strip() == "":
        return b""
    
    try:
        # Créer un fichier temporaire pour la sortie WAV
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            output_path = tmp.name
        
        # Générer le fichier audio avec espeak-ng
        subprocess.run(
            [
                "espeak-ng",
                "-v", "fr",  # Voix française
                "-s", "150",  # Vitesse
                "-w", output_path,  # Fichier de sortie WAV
                text
            ],
            check=True,
            capture_output=True
        )
        
        # Lire le fichier généré
        with open(output_path, "rb") as f:
            audio_bytes = f.read()
        
        # Nettoyer le fichier temporaire
        os.unlink(output_path)
        
        return audio_bytes
    
    except Exception as e:
        print(f"Erreur TTS: {e}")
        return b""  # Retourner du silence en cas d'erreur


async def synthesize(text: str) -> bytes:
    """Wrapper pour la synthèse vocale"""
    return await text_to_speech(text)