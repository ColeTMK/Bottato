from discord.ext import commands
import asyncio

class BumpRemind(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(message):
        if message.content.startswith('!d bump'):

            await message.channel.send(f"{message.author.mention}, thx for the bump! I'll remind you in 2 hours!")
            await asyncio.sleep(10)
            await message.channel.send(f"{message.author.mention}, it's time to bump again!")

def setup(bot):
    bot.add_cog(BumpRemind(bot))        