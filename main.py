import requests


response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
              headers={'Content-Type' : 'application/json', 'trainer_token' : 'a323193c050406972716d830050e771c' },
              json={
                "name": "Бульбазавр",
                "photo": "https://dolnikov.ru/pokemons/albums/001.png"})
print(f'text : {response.text}')

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',  
            headers={'Content-Type' : 'application/json', 'trainer_token' : 'a323193c050406972716d830050e771c'},
            json={"pokemon_id": "20835",
                "name": "New Name",
                "photo": "https://dolnikov.ru/pokemons/albums/008.png"})
print(f'text : {response.text}')

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                         headers={'Content-Type' : 'application/json', 'trainer_token' : 'a323193c050406972716d830050e771c' },
                        json={"pokemon_id": "20835"})
print(f'text : {response.text}')