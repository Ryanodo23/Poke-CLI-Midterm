
from api import get_pokemon_data

if __name__ == "__main__":
    pokemon_name = input("Enter a Pokemon name: ")
    data = get_pokemon_data(pokemon_name)
    if data:
        print("Successfully fetched data:")
        # Print a few key pieces of information
        print(f"  Name: {data['name'].capitalize()}")
        print(f"  ID: {data['id']}")
        print(f"  Height: {data['height']}")
        print(f"  Weight: {data['weight']}")
