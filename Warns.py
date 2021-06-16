import discord
from discord.ext import commands
import datetime
import json

async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['warns'] = 0

async def add_warns(users, user, warns):
    users[f'{user.id}']['warns'] += warns

class Warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, user:discord.Member, *, reason): 

      if user.id == ctx.author.id:
        await ctx.send(f"{ctx.author.mention}, You can't warn yourself!")
        return

      if user.id == 830599839623675925:
        await ctx.send(f"{ctx.author.mention}, You can't warn me!")
        return

      if user:
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title="Warn", description=f"{user.mention} has been warned!", color=0x00FFFF)
        embed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
        embed.add_field(name="**Moderator:**", value=f"{ctx.author.name}", inline=False)
        pfp = user.avatar_url
        embed.set_thumbnail(url=pfp)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"{ctx.guild.name}")
        dmembed=discord.Embed(title="Warn", description="You have been warned!", color=0x00FFFF)
        dmembed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
        pfp = user.avatar_url
        dmembed.add_field(name="**Server:**", value=f"{ctx.guild.name}", inline=False)
        dmembed.add_field(name="**Moderator:**", value=f"{ctx.author.name}", inline=False)
        dmembed.timestamp = datetime.datetime.utcnow()
        dmembed.set_author(name=f"{user.name}", icon_url=pfp)
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

        try:
          if log_channel:
            await ctx.send(embed=embed)
            await user.send(embed=dmembed)
            log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
            logembed=discord.Embed(title="Bot Log", description="Warn Command Used", color=0x00FFFF)
            logembed.add_field(name="**Member:**", value=f"{user}", inline=False)
            logembed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
            logembed.add_field(name="**Moderator:**", value=f"{ctx.author.name}", inline=False)
            author = ctx.message.author
            pfp = author.avatar_url
            logembed.set_author(name=f"{ctx.author.name}", icon_url=pfp)
            logembed.timestamp = datetime.datetime.utcnow()
            await log_channel.send(embed=logembed)
          else:
            await ctx.send(embed=embed)
            await user.send(embed=dmembed)
        except (AttributeError, KeyError):
          await ctx.send(embed=embed)
          await user.send(embed=dmembed)
        with open('warns.json', 'r') as f:
            users = json.load(f)

        await update_data(users, user)
        await add_warns(users, user, 1)

        with open('warns.json', 'w') as f:
            json.dump(users, f, sort_keys=True, ensure_ascii=False, indent=4)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def removewarns(self, ctx, user: discord.Member, amount: int=None):
        if amount == None:
            await ctx.send(f'{ctx.author.mention}, You need to give a number of warns to remove from a member!')
            return
        with open('warns.json', 'r') as f:
            users = json.load(f)

        amount = amount or 1

        await update_data(users, user)
        await add_warns(users, user, -amount)

        if users[f'{user.id}']['warns'] <= 0:
          with open('warns.json', 'w') as f:
            del users[f'{user.id}']['warns']
            del users[f'{user.id}']
            f.write(json.dumps(users, indent=4))
            embed=discord.Embed(description=f'{ctx.author.mention} has removed `{amount}` warns from {user.mention}!', color=0x00FFFF)
            embed.set_thumbnail(url=user.avatar_url)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
            return

        else:
          with open('warns.json', 'w') as f:
            json.dump(users, f, sort_keys=True, ensure_ascii=False, indent=4)

          embed=discord.Embed(description=f'{ctx.author.mention} has removed `{amount}` warns from {user.mention}!', color=0x00FFFF)
          embed.set_thumbnail(url=user.avatar_url)
          embed.timestamp = datetime.datetime.utcnow()
          await ctx.send(embed=embed)
          return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warns(self, ctx, user: discord.Member=None):
        if user == None:
            await ctx.send(f'{ctx.author.mention}, You need to provide a member!')
        user = user or ctx.author
        try:
            with open('warns.json', 'r') as f:
                users = json.load(f)

            warns = users[f'{user.id}']['warns']

            await ctx.send(f'{ctx.author.mention}, {user} has {warns} warnings!')
        except:
            await ctx.send(f"{ctx.author.mention}, {user} doesn't have any warnings!")

def setup(bot):
  bot.add_cog(Warns(bot))