import requests

def get_wanted_pokemon():
    wanted_pokemon = str(input("Type the pokemon you want: "))
    wanted_pokemon = wanted_pokemon.strip().lower()
    return wanted_pokemon

#Without handling errors, it´s just to upload the repository
def get_pokemon(wanted_pokemon, url="https://pokeapi.co/api/v2/") -> dict:
    retrieved_pokemon = requests.get(f"{url}/pokemon/{wanted_pokemon}")
    json_instance = retrieved_pokemon.json() 
    weight = json_instance["weight"]
    return f"The pokemon {wanted_pokemon} weights {weight} pounds"

print(get_pokemon(get_wanted_pokemon()))