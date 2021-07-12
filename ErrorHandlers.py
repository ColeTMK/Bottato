from discord.ext import commands
import json

def get_prefix(bot, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
  return prefixes[str(message.guild.id)]

class ErrorHandlers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, you do not have permission to do this! `Required Permission: {error.missing_perms[0]}`")
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention}, you forgot to type an important argument! `Missing Argument: {error.param.name}`")
      if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"{ctx.author.mention}, that is not a valid command! Type `{get_prefix(self.bot, ctx.message)}help` for help!")
      if isinstance(error, commands.CommandOnCooldown):
        m, s = divmod(error.retry_after, 60)
        fmt = "{} minutes and {} seconds" \
        .format(round(m), round(s))
        await ctx.send(f"{ctx.author.mention}, you can work/beg again in {fmt}!")
      if isinstance(error, commands.MemberNotFound):
        await ctx.send(f'{ctx.author.mention}, I could not find that member. Please try again by giving the right member name, or mention the member.')
      if isinstance(error, commands.BotMissingPermissions):
        await ctx.send(f'ERROR: I dont have permission to do this! Make sure my `Ultimate Bot role` is high as it can be in the role list, then try again.')
      if isinstance(error, commands.MissingRole):
        await ctx.send(f'{ctx.author.mention}, you need a role called `Giveaways` in order to run this command!')

def setup(bot):
    bot.add_cog(ErrorHandlers(bot))