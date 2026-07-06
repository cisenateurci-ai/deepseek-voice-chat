import httpx
import asyncio
from typing import Optional
from pydantic import BaseModel

class Joke(BaseModel):
    setup: Optional[str] = None
    delivery: Optional[str] = None
    joke: Optional[str] = None
    type: str
    id: int

class JokeGenerator:
    """Générateur de blagues utilisant l'API JokeAPI"""
    
    BASE_URL = "https://v2.jokeapi.dev/joke"
    
    @staticmethod
    async def get_random_joke(category: str = "Any") -> dict:
        """
        Récupère une blague aléatoire d'une catégorie spécifique.
        
        Args:
            category: Catégorie de blague (Any, General, Knock-Knock, Programming, Dark)
        
        Returns:
            Dict contenant la blague
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{JokeGenerator.BASE_URL}/{category}",
                    timeout=10.0
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    async def get_multiple_jokes(count: int = 5, category: str = "Any") -> list:
        """
        Récupère plusieurs blagues aléatoires.
        
        Args:
            count: Nombre de blagues à récupérer
            category: Catégorie de blague
        
        Returns:
            Liste de blagues
        """
        tasks = [
            JokeGenerator.get_random_joke(category)
            for _ in range(count)
        ]
        return await asyncio.gather(*tasks)
    
    @staticmethod
    def format_joke(joke_data: dict) -> str:
        """
        Formate la blague pour l'affichage.
        
        Args:
            joke_data: Données brutes de la blague
        
        Returns:
            Blague formatée en texte
        """
        if "error" in joke_data:
            return f"Erreur: {joke_data['error']}"
        
        if joke_data.get("type") == "single":
            return joke_data.get("joke", "Blague non disponible")
        elif joke_data.get("type") == "twopart":
            setup = joke_data.get("setup", "")
            delivery = joke_data.get("delivery", "")
            return f"{setup}\n\n{delivery}"
        else:
            return "Format de blague non reconnu"
    
    @staticmethod
    async def get_categories() -> list:
        """
        Récupère la liste des catégories disponibles.
        
        Returns:
            Liste des catégories
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "https://v2.jokeapi.dev/categories",
                    timeout=10.0
                )
                response.raise_for_status()
                data = response.json()
                return data.get("categories", [])
        except Exception as e:
            return []
