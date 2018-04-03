import discord
from discord.ext import commands
import requests
import json
from constants import RESOURCES, BASE_URL

def pokemon_details_by_id_or_name(id_or_name):
        lookup = RESOURCES[36]
        pokemon_index = id_or_name
        url = '/'.join([BASE_URL, lookup, pokemon_index])
        get_data = requests.get(url)
        data_json = json.loads(get_data.text)

        pokemon_details = ''

        #printing basic info
        pokemon_details += "Name: "+data_json['name']
        pokemon_details += '\n'
        pokemon_details += "Pokedex Order: "+str(data_json['order'])
        pokemon_details += '\n'
        pokemon_details += "Weight: "+str(data_json['weight'])
        pokemon_details += '\n'
        pokemon_details += "Height: "+str(data_json['height'])
        pokemon_details += '\n'
        pokemon_details += "Base Experience: "+str(data_json['base_experience'])
        pokemon_details += '\n'

        #printing abilities
        abilities_string = ''
        for ability in data_json['abilities']:
            abilities_string += (ability['ability']['name']+' ')
        pokemon_details += "Abilities: "+abilities_string
        pokemon_details += '\n'

        #printing stats
        stats_string = ''
        for stat in data_json['stats']:
            stats_string += stat['stat']['name']+'('+str(stat['base_stat'])+') '
        pokemon_details += "Stats: "+stats_string
        pokemon_details += '\n'

        #printing types
        types_string = ''
        for type in data_json['types']:
            types_string += type['type']['name']+' '
        pokemon_details += "Types: "+types_string
        pokemon_details += '\n'

        #display image
        imageURL = data_json['sprites']['front_default']
        embed = discord.Embed()
        embed.set_image(url=imageURL)
        pokemon_details += '\n'

        return {'text':pokemon_details, 'image':embed}