import discord
from discord.ext import commands
import os
from general_cog import general_cog
from music_cog import music_cog 

client = commands.Bot(command_prefix = '-')

client.add_cog(general_cog(client))
client.add_cog(music_cog(client))

@client.event
async def on_ready():
    print('{0.user} has online'.format(client))

client.run(os.environ['TOKENSZ'])