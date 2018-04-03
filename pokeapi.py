import requests
import json

BASE_URL = 'http://pokeapi.co/api/v2'
#wrote this line by line for easy indexing by just seeing line number
RESOURCES = [
'ability', 
'berry', 
'berry-firmness', 
'berry-flavor',
'characteristic', 
'contest-effect', 
'contest-type', 
'egg-group',
'encounter-condition', 
'encounter-condition-value',
'encounter-method', 
'evolution-chain', 
'evolution-trigger',
'gender', 
'generation', 
'growth-rate', 
'item', 
'item-attribute',
'item-category', 
'item-fling-effect', 
'item-pocket', 
'language',
'location', 
'location-area', 
'machine', 
'move', 
'move-ailment',
'move-battle-style', 
'move-category', 
'move-damage-class',
'move-learn-method', 
'move-target', 
'nature', 
'pal-park-area',
'pokeathlon-stat', 
'pokedex', 
'pokemon', 
'pokemon-color',
'pokemon-form', 
'pokemon-habitat', 
'pokemon-shape',
'pokemon-species', 
'region', 
'stat', 
'super-contest-effect',
'type', 
'version', 
'version-group'
]
             
lookup = RESOURCES[36]
#url = '/'.join([BASE_URL, lookup])
#get_data = requests.get(url)
#data_json = json.loads(get_data.text)

#there is a default offset in the pokeapi but we want all of the data
#if data_json['count'] != len(data_json['results']):
#items = data_json['count']
pokemon_index = "6"
url = '/'.join([BASE_URL, lookup, pokemon_index])
get_data = requests.get(url)
data_json = json.loads(get_data.text)
data_json.pop('moves', None)
#ata_json = json.dumps(data_json)

#printing basic info
print("Name: "+data_json['name'])
print("Pokedex Order: "+str(data_json['order']))
print("Weight: "+str(data_json['weight']))
print("Height: "+str(data_json['height']))
print("Base Experience: "+str(data_json['base_experience']))

#printing abilities
print("Abilities:", end=' ')
for ability in data_json['abilities']:
    print(ability['ability']['name'], end=' ')
print()

#printing stats
print("Stats:", end=' ')
for stat in data_json['stats']:
    print(stat['stat']['name']+'('+str(stat['base_stat'])+')', end=' ')
print()

#printing types
print("Types:", end=' ')
for type in data_json['types']:
    print(type['type']['name'], end=' ')
print()

#print(data_json['abilities'])