import os
import httpx
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "dummy-key-for-demo")
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"

async def query_deepseek(prompt: str) -> str:
    """
    Envoie une requête à l'API DeepSeek et retourne la réponse.
    
    Args:
        prompt: Le texte à traiter par DeepSeek
    
    Returns:
        La réponse générée par DeepSeek
    """
    
    # === MODE DÉMO (réponses simulées) ===
    demo_responses = {
        "bonjour": "Bonjour! Comment allez-vous?",
        "salut": "Salut! Enchanté de vous rencontrer!",
        "comment": "Je suis une IA voice chat alimentée par DeepSeek. Comment puis-je vous aider?",
        "help": "Je peux discuter avec vous par voix. Parlez après avoir cliqué sur le bouton micro!",
        "quel": "Je suis un assistant vocal intelligent basé sur DeepSeek.",
        "merci": "De rien! Y a-t-il autre chose que je puisse faire pour vous?",
    }
    
    for key, response in demo_responses.items():
        if key.lower() in prompt.lower():
            return response
    
    return "Je suis en mode démo. Configurez DEEPSEEK_API_KEY pour utiliser l'API réelle!"
    
    # === MODE RÉEL (décommentez pour utiliser l'API DeepSeek) ===
    # if DEEPSEEK_API_KEY == "dummy-key-for-demo":
    #     return "Erreur: DEEPSEEK_API_KEY non configurée. Définez-la dans le fichier .env"
    #
    # try:
    #     async with httpx.AsyncClient() as client:
    #         response = await client.post(
    #             DEEPSEEK_API_URL,
    #             headers={
    #                 "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    #                 "Content-Type": "application/json",
    #             },
    #             json={
    #                 "model": "deepseek-chat",
    #                 "messages": [
    #                     {"role": "system", "content": "Tu es un assistant vocal français utile et amical."},
    #                     {"role": "user", "content": prompt}
    #                 ],
    #                 "temperature": 0.7,
    #                 "max_tokens": 512,
    #             },
    #             timeout=30.0,
    #         )
    #         response.raise_for_status()
    #         result = response.json()
    #         return result["choices"][0]["message"]["content"].strip()
    # except Exception as e:
    #     return f"Erreur API DeepSeek: {str(e)}"