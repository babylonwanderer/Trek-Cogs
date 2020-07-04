import discord
import asyncio
from redbot.core import commands

class Scan:
    """Scans the user mentioned """

    @commands.command()
    async def scan(self, ctx, {0.mention:Member}):
        """Scans the mentioned user.. """

        #Your code will go here
        await self.bot.say("takes <:tricorder:340431262613241866> readings of " + {0.mention:Member} + ", and conducts an analysis the results.")
        await asyncio.sleep(10)
        await self.bot.say("<:tricorder:340431262613241866> readings indicate it is a lifeform, but I have NEVER see anything even remotely similar!!!. :confused:")
