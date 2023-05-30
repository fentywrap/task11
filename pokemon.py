import requests
while True:
    pokemon = input("which pokemon you need?")
    pokemon = pokemon.lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        print(f"name is\t\t{data['name']}")
        print("abilities:")
        for ability in data['abilities']:
            print(ability['ability']['name'])
    else:
        print("pokemon not found")