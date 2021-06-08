from discord.ext import commands

class ErrorHandlers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, Sorry, you do not have permission to do this! `Required Permission: {error.missing_perms[0]}`")
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention}, Sorry, you forgot to type an important argument! `Missing Argument: {error.param.name}`")
      if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"{ctx.author.mention}, Sorry, that is not a valid command! Click on this to see all of my commands, https://bit.ly/33N0TTY")
      if isinstance(error, commands.CommandOnCooldown):
        m, s = divmod(error.retry_after, 60)
        fmt = "Try again in {} minutes and {} seconds" \
        .format(round(m), round(s))
        await ctx.send(f"{ctx.author.mention}, You can work/beg again in {fmt}!")

def setup(bot):
    bot.add_cog(ErrorHandlers(bot))