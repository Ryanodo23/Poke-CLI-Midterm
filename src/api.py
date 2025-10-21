
import requests

def get_pokemon_data(pokemon_name):
    """
    Fetches Pokemon data from the PokeAPI.

    Args:
        pokemon_name (str): The name of the Pokemon to fetch.

    Returns:
        dict: A dictionary containing the Pokemon's data, 
              or None if the request fails.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
