import discord
from discord.ext import commands
import random

class general_cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="hello", help="To introduce what kind of bot this is")
    async def hello(self, ctx):
        await ctx.send("Hi im Galzo bot, i am made by Pensil 2B#7277, dedicated to Galzo, a retarded person.")
        await ctx.send("Nice to meet you")

    @commands.command(name="roll", help="To generate random number")
    async def roll(self, ctx):
        number = random.randrange(1, 99)
        await ctx.send("You has been rolled {}".format(number))


