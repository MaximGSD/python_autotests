import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '976c30a45cd1008f14c75aba84cbf437'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token':TOKEN
          }
TRAINER_ID = '4245'


def test_pokemon_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID })
    assert response.status_code == 200, 'Error'
    
def test_pokemon_trainer_id() :
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID })
    assert response_get.json()["data"][0]["trainer_name"] == "Pythone22" 
    assert response_get.status_code == 200