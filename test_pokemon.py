import pytest
import requests

def test_status_code():
    response = requests.get(url='https://api.pokemonbattle.me:9104/trainers')
    assert response.status_code == 200
    assert response.json()['trainer_name'] == 'Exity'
