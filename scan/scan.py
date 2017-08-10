import discord
from discord.ext import commands

class Scan:
    """Scans the user mentioned """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scan(self, user : discord.Member):
        """Scans the mentioned user.. """

        #Your code will go here
        await self.bot.say("takes <:tricorder:340431262613241866> readings of " + user.mention + ", and conducts an analysis the results.")
        await self.bot.say("It's Life " + message.author + "....  but not as we know it!!!.")


def setup(bot):
    bot.add_cog(Scan(bot))
