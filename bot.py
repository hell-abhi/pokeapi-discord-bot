import discord
from discord.ext import commands
from pokemon_details_by_id_or_name import pokemon_details_by_id_or_name


bot = commands.Bot(description="This is a bot to get Pokemon status of diffrent pokemons.", command_prefix=("+"))

@bot.command(pass_context=True)
async def hello(ctx):
    """THello World!"""
    await bot.send_message(ctx.message.channel, "world!")
    
# @bot.command(pass_context=True)
# async def say(ctx, *, something):
#     await bot.say("**{} said:** {}".format(str(ctx.message.author), something))
#     await bot.delete_message(ctx.message)
    
# @bot.command()
# async def kick(member:discord.Member=None,abc="def"):
#     if member is None:
#         await bot.say("Pass with a member's name")
#     else:
#         await bot.say(member)
#         await bot.say(abc)

@bot.command(pass_context=True)
async def dex(ctx, id_or_name=None):
    if id_or_name is None:
        await bot.say("Wrong Parameter")
    else:
        pokemon_details = pokemon_details_by_id_or_name(id_or_name)
        await bot.send_message(ctx.message.channel, pokemon_details['text'], embed=pokemon_details['image'])

bot.run("NDMwNDUzNTYyNjAzMDc3NjQz.DaQcLg.59bvbbT4uH_50XzukWj22ah_GVM")
