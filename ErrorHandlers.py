from discord.ext import commands
import traceback
import sys

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
        fmt = "{} minutes and {} seconds" \
        .format(round(m), round(s))
        await ctx.send(f"{ctx.author.mention}, You can work/beg again in {fmt}!")
      if isinstance(error, commands.MemberNotFound):
        await ctx.send(f'{ctx.author.mention}, I could not find that member. Please try again by giving the right member name, or mention the member.')
      if isinstance(error, commands.BotMissingPermissions):
        await ctx.channel.send(f'ERROR: I dont have permission to do this! Make sure my Ultimate Bot is high as it can be in the role list, then try again.')
      else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(bot):
    bot.add_cog(ErrorHandlers(bot))