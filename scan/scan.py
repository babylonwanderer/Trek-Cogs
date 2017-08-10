import discord
from discord.ext import commands
import asyncio

class Scan:
    """Scans the user mentioned """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scan(self, user : discord.Member):
        """Scans the mentioned user.. """

        #Your code will go here
        await self.bot.say("takes <:tricorder:340431262613241866> readings of " + user.mention + ", and conducts an analysis the results.")
        await asyncio.sleep(10)
        await self.bot.say("<:tricorder:340431262613241866> readings indicate it is a lifeform, but I have NEVER see anything even remotely similar!!!. :confused:")


def setup(bot):
    bot.add_cog(Scan(bot))
