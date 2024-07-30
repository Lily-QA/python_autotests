import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '19c06898244e78d2d850065f134c4095'
HEADER = { 'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
                 "name": "Бульбазаврик",
                 "photo_id": 12
                }

body_changes = {
                 "pokemon_id": "45822",
                 "name": "Бармашмыг",
                 "photo_id": 12
                }

body_catch = {
                 "pokemon_id": "45822"
                }

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER,json = body_create)
print(response.text)'''

'''changes = requests.put(url = f'{URL}/pokemons', headers = HEADER,json = body_changes)
print(changes.text)'''

catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER,json = body_catch)
print(catch.text)
