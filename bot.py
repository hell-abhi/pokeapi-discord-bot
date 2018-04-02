import discord
from discord.ext import commands

bot = commands.Bot(description="This is a bot to get Pokemon status of diffrent pokemons.", command_prefix=("hello","bye"))

@bot.command()
async def ping():
    """This is the command's description.
    This can span multiple lines."""
    await bot.say("Pong!")
    
@bot.command(pass_context=True)
async def say(ctx, *, something):
    await bot.say("**{} said:** {}".format(str(ctx.message.author), something))
    await bot.delete_message(ctx.message)
    
@bot.command()
async def kick(member:discord.Member=None,abc="def"):
    if member is None:
        await bot.say("Pass with a member's name")
    else:
        await bot.say(member)
        await bot.say(abc)

bot.run("NDMwNDUzNTYyNjAzMDc3NjQz.DaQcLg.59bvbbT4uH_50XzukWj22ah_GVM")
