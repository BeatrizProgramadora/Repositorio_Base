import requests
res = requests.get('https://pt.wikipedia.org/wiki/Python')
dados_pokemon = res.json()

pokemon = input("Digite o nome de um Pokémon: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    print(f"Nome: {data['name']}")
    print("Tipos:", ", ".join([t['type']['name'] for t in data['types']]))
else:
    print("Pokémon não encontrado.")
