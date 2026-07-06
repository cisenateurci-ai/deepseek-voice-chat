from fastapi import APIRouter, Query
from joke_generator import JokeGenerator
from typing import List

router = APIRouter(
    prefix="/api/jokes",
    tags=["jokes"],
    responses={404: {"description": "Not found"}},
)

@router.get("/random")
async def get_random_joke(category: str = Query("Any", description="Catégorie de blague")):
    """
    Récupère une blague aléatoire.
    
    Catégories disponibles:
    - Any (toutes les catégories)
    - General (blagues générales)
    - Knock-Knock (blagues Knock-Knock)
    - Programming (blagues de programmation)
    - Dark (blagues noires)
    """
    joke = await JokeGenerator.get_random_joke(category)
    return {
        "success": "error" not in joke,
        "data": joke,
        "formatted": JokeGenerator.format_joke(joke)
    }

@router.get("/multiple")
async def get_multiple_jokes(
    count: int = Query(5, ge=1, le=50, description="Nombre de blagues"),
    category: str = Query("Any", description="Catégorie de blague")
):
    """
    Récupère plusieurs blagues aléatoires.
    """
    jokes = await JokeGenerator.get_multiple_jokes(count, category)
    return {
        "count": len(jokes),
        "jokes": jokes,
        "formatted": [JokeGenerator.format_joke(joke) for joke in jokes]
    }

@router.get("/categories")
async def get_joke_categories():
    """
    Récupère la liste des catégories de blagues disponibles.
    """
    categories = await JokeGenerator.get_categories()
    return {
        "categories": categories,
        "count": len(categories)
    }

@router.get("/programming")
async def get_programming_joke():
    """
    Récupère une blague de programmation.
    """
    joke = await JokeGenerator.get_random_joke("Programming")
    return {
        "success": "error" not in joke,
        "data": joke,
        "formatted": JokeGenerator.format_joke(joke)
    }

@router.get("/dark")
async def get_dark_joke():
    """
    Récupère une blague noire.
    """
    joke = await JokeGenerator.get_random_joke("Dark")
    return {
        "success": "error" not in joke,
        "data": joke,
        "formatted": JokeGenerator.format_joke(joke)
    }
