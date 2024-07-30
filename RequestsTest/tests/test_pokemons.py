import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '19c06898244e78d2d850065f134c4095'
TRAINER_ID = 4254 
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}


def test_get_trainers_status_code():
    response = requests.get(f'{URL}/trainers', headers=HEADER, params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200


def test_trainer_name_in_response():
    response = requests.get(f'{URL}/trainers', headers=HEADER, params={'trainer_id': TRAINER_ID})
    data = response.json()
    print(data)
    trainers = data.get('data', [])
    assert any(trainer['trainer_name'] == 'Лилу' for trainer in trainers)

if __name__ == '__main__':
    pytest.main()