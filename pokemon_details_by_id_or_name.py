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
        data_json.pop('moves', None)

        pokemon_details = ''
        embed = discord.Embed()

        #printing basic info
        embed.add_field(name='Name:', value=data_json['name'], inline=False)
        embed.add_field(name='Pokedex Order:', value=str(data_json['order']), inline=False)
        embed.add_field(name='Weight:', value=str(data_json['weight']), inline=True)
        embed.add_field(name='Height:', value=str(data_json['height']), inline=True)
        embed.add_field(name='Base Experience: ', value=str(data_json['base_experience']), inline=False)
        
        #printing abilities
        abilities_string = ''
        for ability in data_json['abilities']:
            abilities_string += (ability['ability']['name']+' ')
        embed.add_field(name='Abilities', value = abilities_string, inline=False)
        # pokemon_details += "Abilities: "+abilities_string
        # pokemon_details += '\n'

        #printing stats
        stats_string = ''
        embed.add_field(name='**Stats**:', value = stats_string, inline=False)
        for stat in data_json['stats']:
            embed.add_field(name=stat['stat']['name'], value=str(stat['base_stat']), inline=True)
        # pokemon_details += "Stats: "+stats_string
        # pokemon_details += '\n'

        #printing types
        types_string = ''
        for type in data_json['types']:
            types_string += type['type']['name']+' '
        embed.add_field(name='Type(s):', value = types_string, inline=False)
        # pokemon_details += "Types: "+types_string
        # pokemon_details += '\n'

        #display image
        imageURL = data_json['sprites']['front_default']
        embed.set_image(url=imageURL)
        embed.colour= 3447003
        # pokemon_details += '\n'

        return embed