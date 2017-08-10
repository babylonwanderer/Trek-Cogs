import discord
from discord.ext import commands

class Stun:
    """Stuns the user mentioned """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stun(self, user : discord.Member):
        """Stuns the mentioned user.. """

        #Your code will go here
        await self.bot.say("takes aim at " + user.mention + ", and drops them to the deck with a Type II <:mkii:340431228970860544>")
        await self.bot.say("Poor " + user.mention + " lays motionless for 5 mins.")


def setup(bot):
    bot.add_cog(Stun(bot))
