import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'eec0ae3cfb2c543afdb1cce54face2b0'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token':TOKEN
          }
BODY_POKEMON_ID = {
    "pokemon_id": "28144"
}
body_pokemons = {
    "name": "ПитонПтоныч",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_changename = {
    "pokemon_id": "28144",
    "name": "Питоныч22",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
'''response = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_pokemons)
print(response.text)
'''
response_changename = requests.put(url = f'{URL}/pokemons' , headers = HEADER, json = body_changename)
print(response_changename.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_POKEMON_ID)
print(response_add_pokeball.text)