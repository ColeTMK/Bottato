import discord
from discord.ext import commands
import datetime
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
        missingperm=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f'You do not have `{error.missing_perms[0]}` perms to run this command!', color=0xFF0000)
        missingperm.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=missingperm)
      if isinstance(error, commands.MissingRequiredArgument):
        missingarg=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f'You forgot the `{error.param.name}` argument for that command!', color=0xFF0000)
        missingarg.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=missingarg)
      if isinstance(error, commands.CommandNotFound):
        commandnotfound=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f'That is an invalid command! Type `{get_prefix(self.bot, ctx.message)}help` for help!', color=0xFF0000)
        commandnotfound.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=commandnotfound)
      if isinstance(error, commands.CommandOnCooldown):
        m, s = divmod(error.retry_after, 60)
        fmt = "{} minutes and {} seconds" \
        .format(round(m), round(s))
        cooldown=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f'You are on cooldown for this command! Try again in `{fmt}.`', color=0xFF0000)
        cooldown.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=cooldown)
      if isinstance(error, commands.MemberNotFound):
        membernotfound=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f'Member not found!', color=0xFF0000)
        membernotfound.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=membernotfound)
      if isinstance(error, commands.BotMissingPermissions):
        botnoperm=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f'I do not have permission to execute this command! Please make sure I have the proper perms to execute this command.', color=0xFF0000)
        botnoperm.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=botnoperm)
      if isinstance(error, commands.MissingRole):
        missingrole=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f'You need a role called `Giveaways` to execute this command!', color=0xFF0000)
        missingrole.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=missingrole)
      if isinstance(error, commands.RoleNotFound):
        norole=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f'Role not found!', color=0xFF0000)
        norole.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=norole)
      if isinstance(error, commands.ChannelNotFound):
        nochannel=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f'Channel not found!', color=0xFF0000)
        nochannel.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=nochannel)
      if isinstance(error, commands.TooManyArguments):
        manyarg=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f'You gave too many arguments!', color=0xFF0000)
        manyarg.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=manyarg)
      if isinstance(error, commands.BotMissingAnyRole):
        missingroles=discord.Embed(title='<a:xmark:865222057414230056> Error', description=f"I either don't have a role to execute this command or I don't have permission to!", color=0xFF0000)
        missingroles.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=missingroles)

def setup(bot):
    bot.add_cog(ErrorHandlers(bot))