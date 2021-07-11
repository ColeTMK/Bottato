import discord
from discord import User
from discord.ext import commands
import random
import requests
import json
import asyncio
import datetime
from discord.ext.commands import Greedy

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

def get_prefix(bot, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
  return prefixes[str(message.guild.id)]

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def leaveserver(self, ctx, guild:discord.Guild):
      if ctx.author.id == 467715040087244800:
        await ctx.send(f"Leaving {guild.name}... GUILD ID: {guild.id}")
        await guild.leave()
      if ctx.author.id != 467715040087244800:
        await ctx.send(f'{ctx.author.mention}, Cole can only do this command!')


    @commands.command()
    async def servernames(self, ctx):
      if ctx.author.id == 467715040087244800:
        for server in self.bot.guilds:
          await ctx.send(f"{server.name, server.id}")
      if ctx.author.id != 467715040087244800:
        await ctx.send(f'{ctx.author.mention}, Cole can only do this command!')
      
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
      with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = prefix

      with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

      embed=discord.Embed(title="Server Prefix", description=f"The prefix has been changed to `{prefix}` successfully!", color=0x00FFFF)
      author = ctx.author
      pfp = author.avatar_url
      embed.set_author(name=f"Admin: {ctx.author}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)
      await ctx.author.send(f"you changed {ctx.guild.name}'s prefix to `{prefix}`")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def setlogchannel(self, ctx, channel: discord.TextChannel):
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
        log_channel = json.load(fp)

      try:
        log_channel[str(ctx.guild.id)] = channel.id
      except KeyError:
        new = {str(ctx.guild.id): channel.id}
        log_channel.update(new)

      embed=discord.Embed(title="Log Channel Set", color=0x00FFFF)
      embed.add_field(name="**Channel Name:**", value=f"{channel}")
      embed.add_field(name="**Moderator:**", value=f"{ctx.author}")
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)
      await ctx.author.send(f"you just set the log channel for **{ctx.guild.name}** to **{channel}**!")

      with open('logchannel.json', 'w', encoding='utf-8') as fpp:
        json.dump(log_channel, fpp, indent=2)

    @commands.command()
    async def fact(self, ctx):

      fun_facts = ["Banging your head against a wall for one hour burns 150 calories.", "Snakes can help predict earthquakes.", "7% of American adults believe that chocolate milk comes from brown cows.", "If you lift a kangaroo’s tail off the ground it can’t hop.", "Bananas are curved because they grow towards the sun.", "More human twins are being born now than ever before.", "The first person convicted of speeding was going eight mph.", "New car smell is the scent of dozens of chemicals.", "The world wastes about 1 billion metric tons of food each year.", "Hair and nails grow faster during pregnancy.", "Some sea snakes can breathe through their skin.", "The moon has moonquakes.", "Goosebumps are meant to ward off predators.", "The wood frog can hold its pee for up to eight months.", "your nostrils work one at a time.", "The M's in M&Ms stand for Mars and Murrie.", "Copper door knobs are self-disinfecting.", "Cotton candy was invented by a dentist.", "The first computer was invented in the 1940s."]

      fact = random.choice(fun_facts)
      embed=discord.Embed(title="Random Fact", description=(fact), color=0x00FFFF)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    async def quote(self, ctx):
      quote = get_quote()
      embed=discord.Embed(title="Random Quote", description=f"{quote}", color=0x00FFFF)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=None):
      if amount == None:
        await ctx.send(f'{ctx.author.mention}, you need to give an amount of messages to delete!')
        return
      amount = int(amount)
      if amount <= 0:
        await ctx.send(f"{ctx.author.mention}, you need to give a positive number!")
        return
      if amount > 100:
        await ctx.send(f"{ctx.author.mention}, The maximum amount of messages you can delete is 100!")
        return
      try:
        await ctx.channel.purge(limit=amount+1)
      except:
        await ctx.send(f'{ctx.author.mention}, I cannot delete messages that are over 14 days old!')
        return
      embed=discord.Embed(title="Messages Cleared", description=f'{amount} messages were deleted!', color=0x00FFFF)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
        log_channel = json.load(fp)

      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          msg = await ctx.send(embed=embed)
          await asyncio.sleep(3)
          await msg.delete()
          logembed=discord.Embed(title="Bot Log", description="Clear Command Used", color=0xFFA500)
          logembed.add_field(name="**Amount:**", value=f"{amount} Messages", inline=False)
          logembed.add_field(name="**Channel:**", value=f"{ctx.channel.name}", inline=False)
          logembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
          author = ctx.message.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          logembed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
      except (AttributeError, KeyError):
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await msg.delete()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):

      if reason is None:
        reason = 'No reason given'

      if member.id == ctx.message.author.id:
       await ctx.send(f"{ctx.author.mention}, you can't ban yourself!")
       return

      await member.ban(reason=reason)
      embed=discord.Embed(title="Ban", color=0x00FFFF)
      embed.add_field(name="**Member:**", value=f"{member}", inline=False)
      embed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
      embed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      dmembed=discord.Embed(title="Ban", description="you have been banned!", color=0x00FFFF)
      dmembed.timestamp = datetime.datetime.utcnow()
      dmembed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
      memberpfp = member.avatar_url
      dmembed.add_field(name="**Server:**", value=f"{ctx.guild.name}", inline=False)
      dmembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
      dmembed.set_author(name=f"{member.name}", icon_url=memberpfp)
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
        log_channel = json.load(fp)

      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          logembed=discord.Embed(title="Bot Log", description="Ban Command Used", color=0xFFA500)
          logembed.add_field(name="**Member:**", value=f"{member}", inline=False)
          logembed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
          logembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
          author = ctx.message.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          logembed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
      except:
          pass

      try:
        await member.send(embed=dmembed)
      except:
        pass
      try:
        await ctx.send(embed=embed)
      except:
        pass

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):

      if reason is None:
        reason = 'No reason given'

      if member.id == ctx.message.author.id:
       await ctx.send(f"{ctx.author.mention}, you can't kick yourself!")
       return

      await member.kick(reason=reason)
      embed=discord.Embed(title="Kick", color=0x00FFFF)
      embed.add_field(name="**Member:**", value=f"{member}", inline=False)
      embed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
      embed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
      embed.timestamp = datetime.datetime.utcnow()
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      dmembed=discord.Embed(title="Kick", description="you have been kicked!", color=0x00FFFF)
      dmembed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
      memberpfp = member.avatar_url
      dmembed.add_field(name="**Server:**", value=f"{ctx.guild.name}", inline=False)
      dmembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
      dmembed.set_author(name=f"{member.name}", icon_url=memberpfp)
      dmembed.timestamp = datetime.datetime.utcnow()
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
        log_channel = json.load(fp)

      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          logembed=discord.Embed(title="Bot Log", description="Kick Command Used", color=0xFFA500)
          logembed.add_field(name="**Member:**", value=f"{member}", inline=False)
          logembed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
          logembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
          author = ctx.message.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          logembed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
      except:
        pass

      try:
        await member.send(embed=dmembed)
      except:
        pass
      try:
        await ctx.send(embed=embed)
      except:
        pass

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def lockchannel(self, ctx):
      await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
      embed=discord.Embed(title="Channel Lockdown", description="Channel lockdown in progress!", color=0xFF0000)
      embed.add_field(name="**Channel Name:**", value=f"{ctx.channel.name}", inline=True)
      embed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=True)
      embed.timestamp = datetime.datetime.utcnow()
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
        log_channel = json.load(fp)

      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          await ctx.send(embed=embed)
          logembed=discord.Embed(title="Bot Log", description="Lock Channel Used", color=0xFFA500)
          logembed.add_field(name="**Channel:**", value=f"{ctx.channel.name}", inline=False)
          logembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
          author = ctx.message.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          embed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
      except (AttributeError, KeyError):
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlockchannel(self, ctx):
      await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
      embed=discord.Embed(title="**Channel Unlock**", description="Channel unlocking in progress!", color=0xFF0000)
      embed.add_field(name="**Channel Name:**", value=f"{ctx.channel.name}", inline=True)
      embed.timestamp = datetime.datetime.utcnow()
      embed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=True)
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
        log_channel = json.load(fp)

      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          await ctx.send(embed=embed)
          logembed=discord.Embed(title="Bot Log", description="Unlock Channel Used", color=0xFFA500)
          logembed.add_field(name="**Channel:**", value=f"{ctx.channel.name}", inline=False)
          logembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
          author = ctx.message.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          logembed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
      except (AttributeError, KeyError):
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds:int=None):
      if seconds == None:
        await ctx.send(f'{ctx.author.mention}, you need to give a duration to change the slowmode!')
        return
      if seconds > 21600:
        await ctx.send(f'{ctx.author.mention}, The maximum slowmode is 6 hours (21,600 seconds)!')
      await ctx.channel.edit(slowmode_delay=seconds)
      embed=discord.Embed(title="Slowmode Changed", description=f'Slowmode is now `{seconds} seconds`', color=0x00FFFF)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
            log_channel = json.load(fp)
          
      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          logembed=discord.Embed(title="Bot Log", description="Slowmode Command Used", color=0xFFA500)
          logembed.add_field(name="**Channel:**", value=f"{ctx.channel.name}", inline=False)
          logembed.add_field(name="**Slowmode:**", value=f"{seconds} Seconds", inline=False)
          logembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
          author = ctx.message.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          logembed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
          await ctx.send(embed=embed)
      except (AttributeError, KeyError):
        await ctx.send(embed=embed)
      
    @commands.command()
    async def ping(self, ctx):
      embed=discord.Embed(title="Pong!", description=f'My ping is {round(self.bot.latency*1000)}ms.', color=0x00FFFF)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)
 
    @commands.command()
    async def deadchat(self, ctx):
      await ctx.channel.purge(limit=1)
      embed=discord.Embed(description="AYOOO CHAT IS DEAD! SPEAK HUMANS SPEAKKK you MUST!", color=0x00FFFF)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
 
      if reason is None:
        reason = 'No reason given'

      if member.id == ctx.message.author.id:
       await ctx.send(f"{ctx.author.mention}, you can't mute yourself!")
       return

      if member:
        role = discord.utils.get(ctx.guild.roles, name='muted')

        if role == None:
          await ctx.send(f"{ctx.author.mention}, Please make sure your muted role is called `muted` all in lowercase! Then try again.")
          return
 
        if role in ctx.guild.roles:
          await member.add_roles(role)
          embed=discord.Embed(title="Muted", description=f"Member: {member.mention}", color=0x00FFFF)
          embed.add_field(name="**Reason:**", value=f'{reason}', inline=False)
          embed.add_field(name="**Moderator:**", value=f'{ctx.author}', inline=False)
          author = ctx.message.author
          pfp = author.avatar_url
          embed.set_author(name=f"{ctx.author}", icon_url=pfp)
          embed.timestamp = datetime.datetime.utcnow()
          dmembed=discord.Embed(title="Mute", description="you have been muted!", color=0x00FFFF)
          dmembed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
          memberpfp = member.avatar_url
          dmembed.add_field(name="**Server:**", value=f"{ctx.guild.name}", inline=False)
          dmembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
          dmembed.set_author(name=f"{member.name}", icon_url=memberpfp)
          dmembed.timestamp = datetime.datetime.utcnow()
          with open('logchannel.json', 'r', encoding='utf-8') as fp:
            log_channel = json.load(fp)
          
          try:
            if log_channel:
              log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
              await ctx.send(embed=embed)
              await member.send(embed=dmembed)
              logembed=discord.Embed(title="Bot Log", description="Mute Command Used", color=0xFFA500)
              logembed.add_field(name="**Member:**", value=f"{member.name}", inline=False)
              logembed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
              logembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
              author = ctx.message.author
              pfp = author.avatar_url
              logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
              logembed.timestamp = datetime.datetime.utcnow()
              await log_channel.send(embed=logembed)
          except (AttributeError, KeyError):
            await ctx.send(embed=embed)
          try:
            await member.send(embed=dmembed)
          except:
            pass
 
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
  
      if member.id == ctx.author.id:
       await ctx.send(f"{ctx.author.mention}, your not muted!")
       return

      if member:
        role = discord.utils.get(ctx.guild.roles, name='muted')

        if role == None:
          await ctx.send(f"{ctx.author.mention}, Please make sure your muted role is called `muted` all in lowercase then try again!")
          return
  
        await member.remove_roles(role)
        embed=discord.Embed(title="Unmute", description=f"Member: {member.mention}", color=0x00FFFF)
        embed.add_field(name="**Moderator:**", value=f'{ctx.author}', inline=True)
        author = ctx.message.author
        pfp = author.avatar_url
        embed.set_author(name=f"{ctx.author}", icon_url=pfp)
        dmembed=discord.Embed(title="Unmute", description="you have been unmuted!", color=0x00FFFF)
        memberpfp = member.avatar_url
        dmembed.add_field(name="**Server:**", value=f"{ctx.guild.name}", inline=False)
        dmembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
        dmembed.set_author(name=f"{member.name}", icon_url=memberpfp)
        embed.timestamp = datetime.datetime.utcnow()
        dmembed.timestamp = datetime.datetime.utcnow()
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)
          
        try:
          if log_channel:
            log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
            await ctx.send(embed=embed)
            logembed=discord.Embed(title="Bot Log", description="Unmute Command Used", color=0xFFA500)
            logembed.add_field(name="**Member:**", value=f"{member.name}", inline=False)
            logembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
            author = ctx.message.author
            pfp = author.avatar_url
            logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
            logembed.timestamp = datetime.datetime.utcnow()
            await log_channel.send(embed=logembed)
        except:
          await ctx.send(embed=embed)
        try:
          await member.send(embed=dmembed)
        except:
            pass

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def tempmute(self, ctx, member : discord.Member, time=0, *, reason=None):

      if reason is None:
        reason = 'No reason given'

      if time is int(0):
        await ctx.send(f"{ctx.author.mention}, you need to give the duration!")
        return

      if time <= int(0):
        await ctx.send(f"{ctx.author.mention}, you need to give a positive time!")
        return

      if member.id == ctx.message.author.id:
       await ctx.send(f"{ctx.author.mention}, you can't mute yourself!")
       return
      
      if member:
        role = discord.utils.get(ctx.guild.roles, name="muted")

        if role == None:
          await ctx.send(f"{ctx.author.mention}, Please make sure your muted role is called `muted` all in lowercase then try again!")
          return

        if role in ctx.guild.roles:
          await member.add_roles(role)
          embed=discord.Embed(title="Temp. Mute", description=f"Member: {member.mention}", color=0x00FFFF)
          embed.add_field(name="**Duration:**", value=f'{time} seconds', inline=True)
          embed.add_field(name="**Reason:**", value=f'{reason}', inline=True)
          embed.add_field(name="**Moderator:**", value=f'{ctx.author}', inline=True)
          embed.timestamp = datetime.datetime.utcnow()
          dmembed=discord.Embed(title="Temp. Mute", description="you have been temp. muted!", color=0x00FFFF)
          dmembed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
          dmembed.add_field(name="**Duration:**", value=f"{time} Seconds", inline=False)
          dmembed.timestamp = datetime.datetime.utcnow()
          memberpfp = member.avatar_url
          dmembed.add_field(name="**Server:**", value=f"{ctx.guild.name}", inline=False)
          dmembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
          dmembed.set_author(name=f"{member.name}", icon_url=memberpfp)
          with open('logchannel.json', 'r', encoding='utf-8') as fp:
            log_channel = json.load(fp)
          
      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          await ctx.send(embed=embed)
          logembed=discord.Embed(title="Bot Log", description="Temp. Mute Command Used", color=0xFFA500)
          logembed.add_field(name="**Member:**", value=f"{member.name}", inline=False)
          logembed.add_field(name="**Reason:**", value=f"{reason}", inline=False)
          logembed.add_field(name="**Duration:**", value=f"{time} Seconds", inline=False)
          logembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
          logembed.timestamp = datetime.datetime.utcnow()
          author = ctx.message.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          await log_channel.send(embed=logembed)
          await asyncio.sleep(time)
          await member.remove_roles(role)
      except (AttributeError, KeyError):
        await ctx.send(embed=embed)
        await asyncio.sleep(time)
        await member.remove_roles(role)
      try:
      	await member.send(dmembed)
      except:
        pass

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def giverole(self, ctx, member:discord.Member, *, role:discord.Role):
      if role in member.roles:
        await ctx.send(f'{ctx.author.mention}, this member already has this role!')
        return
      await member.add_roles(role)
      embed=discord.Embed(title="Role Gived", color=0x0FFFF)
      embed.add_field(name='**Role Name:**', value=f'{role}', inline=False)
      embed.add_field(name='**Member:**', value=f'{member}', inline=False)
      memberpfp = member.avatar_url
      embed.set_thumbnail(url=memberpfp)
      embed.timestamp = datetime.datetime.utcnow()
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
        log_channel = json.load(fp)
      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          await ctx.send(embed=embed)
          logembed=discord.Embed(title="Bot Log", description="Give Role Command Used", color=0xFFA500)
          logembed.add_field(name='**Role Name:**', value=f'{role}', inline=False)
          logembed.add_field(name='**Member:**', value=f'{member}', inline=False)
          logembed.add_field(name='**Moderator:**', value=f'{ctx.author}', inline=False)
          author = ctx.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          logembed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
      except (AttributeError, KeyError):
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member:discord.Member, *, role:discord.Role):
      if role not in member.roles:
        await ctx.send(f'{ctx.author.mention}, this member does not have this role!')
        return
      if role not in ctx.guild.roles:
        await ctx.send(f'{ctx.author.mention}, I could not find that role, please try again!')
      await member.remove_roles(role)
      embed=discord.Embed(title="Role Removed", color=0x0FFFF)
      embed.add_field(name='**Role Name:**', value=f'{role}', inline=False)
      embed.add_field(name='**Member:**', value=f'{member}', inline=False)
      memberpfp = member.avatar_url
      embed.set_thumbnail(url=memberpfp)
      embed.timestamp = datetime.datetime.utcnow()
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)
      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          await ctx.send(embed=embed)
          logembed=discord.Embed(title="Bot Log", description="Remove Role Command Used", color=0xFFA500)
          logembed.add_field(name='**Role Name:**', value=f'{role}', inline=False)
          logembed.add_field(name='**Member:**', value=f'{member}', inline=False)
          logembed.add_field(name='**Moderator:**', value=f'{ctx.author}', inline=False)
          author = ctx.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          logembed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
      except (AttributeError, KeyError):
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
      embed=discord.Embed(title="Bot Invite", description="Click here -> https://top.gg/bot/830599839623675925 **you WILL GET 404 ERROR! BOT WAITING FOR APPROVAL**", color=0x00FFFF)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    async def support(self, ctx):
      embed=discord.Embed(title="Bot Support", description="Click here -> https://discord.gg/arMVCzHfuf", color=0x00FFFF)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def changenickname(self, ctx, member:discord.Member, *, nick):
      await member.edit(nick=nick)
      embed=discord.Embed(title="Nickname Change", color=0x00FFFF)
      embed.add_field(name='**Member Name:**', value=f'{member}', inline=False)
      embed.add_field(name='**New Nickname:**', value=f'{nick}', inline=False)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      embed.set_thumbnail(url=member.avatar_url)
      embed.timestamp = datetime.datetime.utcnow()
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          await ctx.send(embed=embed)
          logembed=discord.Embed(title="Bot Log", description="Change Nickname Command Used", color=0xFFA500)
          logembed.add_field(name="**Member:**", value=f"{member}", inline=False)
          logembed.add_field(name="**New Nickname:**", value=f"{nick}", inline=False)
          logembed.add_field(name="**Moderator:**", value=f"{ctx.author}", inline=False)
          author = ctx.message.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          logembed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
      except (AttributeError, KeyError):
        await ctx.send(embed=embed)

    @commands.command()
    async def loved(self, ctx):
      await ctx.channel.purge(limit=1)
      embed=discord.Embed(title="Remember that you are loved! :heart: :heart: :heart:", description="Don't forget that!", color=0x00FFFF)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f"{ctx.author}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dm(self, ctx, users: Greedy[User], *, message):
      for user in users:
        await ctx.channel.purge(limit=1)
        try:
          await user.send(message)
        except:
          await ctx.send(f"{ctx.author.mention}, there was an error sending dm's to these users! They may not be accepting dm's.")
          return
        embed=discord.Embed(title="INDIVIDUAL/BULK DM'S", description="Message Delivered!", color=0x00FFFF)
        embed.add_field(name="**Message:**", value=f'{message}', inline=True)
        embed.add_field(name="**User(s):**", value=f'{users.name}', inline=True)
        embed.add_field(name="**Admin:**", value=f'{ctx.author}', inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

      try:
        if log_channel:
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          await ctx.send(embed=embed)
          logembed=discord.Embed(title="Bot Log", description="DM Command Used", color=0xFFA500)
          logembed.add_field(name="**Message:**", value=f"{message}", inline=False)
          logembed.add_field(name="**Member(s):**", value=f"{users}", inline=False)
          logembed.add_field(name="**Admin:**", value=f"{ctx.author}", inline=False)
          author = ctx.message.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          logembed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
      except (AttributeError, KeyError):
        await ctx.send(embed=embed)
        

    @commands.command()
    async def avatar(self, ctx, *, user:discord.Member=None):
      author = ctx.message.author
      if user is None:
        pfp = author.avatar_url
        embed=discord.Embed(description="This is your avatar.", color=0x00FFFF)
        embed.set_author(name=f"{ctx.author}")
        embed.set_image(url=(pfp))
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
      else:
        pfp = user.avatar_url
        embed=discord.Embed(description=f"This is **{user}** avatar.", color=0x00FFFF)
        embed.set_author(name=f"{ctx.author}")
        embed.set_image(url=(pfp))
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def suggest(self, ctx, *, text):
      await ctx.channel.purge(limit=1)
      embed=discord.Embed(title=f"**Suggestion by {ctx.author}**", description=f"Suggestion: ***{text}***", color=0x00FFFF)
      embed.set_footer(text=f"{ctx.guild.name}")
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.timestamp = datetime.datetime.utcnow()
      msg = await ctx.send(embed=embed)
      with open('logchannel.json', 'r', encoding='utf-8') as fp:
        log_channel = json.load(fp)
      
      try:
        if log_channel:
          await msg.add_reaction("👍")
          await msg.add_reaction("👎")
          await msg.add_reaction("😕")
          log_channel = ctx.guild.get_channel(log_channel[str(ctx.guild.id)])
          logembed=discord.Embed(title="Bot Log", description="Suggest Command Used", color=0xFFA500)
          logembed.add_field(name="**Member:**", value=f"{ctx.author}", inline=False)
          logembed.add_field(name="**Suggestion:**", value=f"{text}", inline=False)
          author = ctx.message.author
          pfp = author.avatar_url
          logembed.set_author(name=f"{ctx.author}", icon_url=pfp)
          logembed.timestamp = datetime.datetime.utcnow()
          await log_channel.send(embed=logembed)
      except (AttributeError, KeyError):
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
        await msg.add_reaction("😕")

    @commands.command()
    async def servercount(self, ctx):
      embed=discord.Embed(title="Server Count", description="I'm in " + str(len(self.bot.guilds)) + " servers!", color=0x00FFFF)
      author = ctx.author
      pfp = author.avatar_url
      embed.set_author(name=f"{author.name}", icon_url=pfp)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    async def membercount(self, ctx):
      total = len(ctx.guild.members)
      online = len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members)))
      idle = len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members)))
      dnd = len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members)))
      offline = len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))
      humans = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
      bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
      embed=discord.Embed(title="Member Count", description=f"Total: ***{total}***\nHumans: ***{humans}***\nBots: ***{bots}***\nOnline: ***{online}***\nIdle: ***{idle}***\nDo not Disturb: ***{dnd}***\nOffline: ***{offline}***", color=0x00FFFF)
      author = ctx.author
      pfp = author.avatar_url
      embed.set_author(name=f"{author.name}", icon_url=pfp)
      embed.set_footer(text=f"{ctx.guild.name}")
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, user : discord.Member=None):
      if user is None:
        user = ctx.author
      joined = user.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
      user = user
      author = ctx.author
      pfp = author.avatar_url 
      role_string = ' '.join([r.mention for r in user.roles][1:])
      roles = user.roles
      roles.reverse()
      top_role = roles[0]
      created = user.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
      embed=discord.Embed(title='**Member Info**', color=0x00FFFF)
      embed.add_field(name='**Name:**', value=f'`{user}`', inline=False)
      embed.add_field(name='**ID:**', value=f'`{user.id}`', inline=False)
      embed.add_field(name='**Join Date:**', value=f'`{joined}`', inline=False)
      embed.add_field(name='**Creation Date:**', value=f'`{created}`', inline=False)
      embed.add_field(name='**Roles [{}]:**'.format(len(user.roles)-1), value=role_string, inline=False)
      embed.add_field(name='**Highest Role:**', value=top_role.mention, inline=False)
      embed.set_author(name=f'{author.name}', icon_url=pfp)
      embed.set_thumbnail(url=user.avatar_url)
      embed.set_footer(text=f'{ctx.guild.name}')
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
      author = ctx.author
      pfp = author.avatar_url
      total = len(ctx.guild.members)
      humans = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
      bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
      embed=discord.Embed(title='Server Info', color=0x00FFFF)
      embed.add_field(name='Server Name:', value=f'`{ctx.guild.name}`', inline=False)
      embed.add_field(name='Server ID:', value=f'`{ctx.guild.id}`', inline=False)
      embed.add_field(name='Owner:', value=f'`{ctx.guild.owner}`', inline=False)
      embed.add_field(name='Owner ID:', value=f'`{ctx.guild.owner.id}`', inline=False)
      embed.add_field(name='Server Region:', value=f'`{ctx.guild.region}`', inline=False)
      embed.add_field(name='Server Creation Date:', value=f'`{ctx.guild.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")}`', inline=False)
      embed.add_field(name='Text Channels:', value=f'`{len(ctx.guild.text_channels)} Text Channels`', inline=False)
      embed.add_field(name='Voice Channels:', value=f'`{len(ctx.guild.voice_channels)} Voice Channels`', inline=False)
      embed.add_field(name='Roles:', value=f'`{len(ctx.guild.roles)} Roles`', inline=False)
      embed.add_field(name='Total Members:', value=f'`{total} Members`', inline=False)
      embed.add_field(name='Humans:', value=f'`{humans} Humans`', inline=False)
      embed.add_field(name='Bots:', value=f'`{bots} Bots`', inline=False)
      embed.add_field(name='Boost Count:', value=f'`{ctx.guild.premium_subscription_count} Boosts`', inline=False)
      embed.set_author(name=f'{author.name}', icon_url=pfp)
      embed.set_footer(text=f'{ctx.guild.name}')
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Giveaways')
    async def gcreate(self, ctx, time=None, *, prize=None):
      if time == None:
        await ctx.send(f'{ctx.author.mention}, you need to give the **duration**! An example of a successful command is\n`{get_prefix(self.bot, ctx.message)}gcreate <duration> <prize>`\n\nThe duration can be in (s|m|h|d).')
        return
      if prize == None:
        await ctx.send(f'{ctx.author.mention}, you need to give the **prize**! An example of a successful command is\n`{get_prefix(self.bot, ctx.message)}gcreate <duration> <prize>`')
        return
      try:
        time_convert = {"s":1, "m":60, "h":3600, "d":86400}
        gawtime = int(time[:-1]) * time_convert[time[-1]]
      except:
        await ctx.send(f'{ctx.author.mention}, there was an error converting your duration! Please try again in the right format, (s|m|h|d)')
        return
      embed=discord.Embed(title='🎁 New Giveaway Started! 🎁', description=f"**Prize:** {prize}\n\n**Ends in**: {time}\n\n**From:** {ctx.author.mention}", color=0x1CDEA3)
      embed.set_footer(text=f'React to 🎉 to enter the giveaway!')
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.timestamp = datetime.datetime.utcnow()

      gaw_msg = await ctx.send(embed=embed)
      await gaw_msg.add_reaction("🎉")
      await asyncio.sleep(gawtime)
      new_msg = await ctx.channel.fetch_message(gaw_msg.id)

      user_list = [u for u in await new_msg.reactions[0].users().flatten() if u != self.bot.user]

      if len(user_list) == 0:
        await ctx.send(f"{ctx.author.mention}, no one reacted for the giveaway")
      else:
        winner = random.choice(user_list)

      winnerembed=discord.Embed(title='🎁 Giveaway Ended! 🎁', description=f'**{winner}** won the giveaway for\n**{prize}**!', color=0x1CDEA3)
      winnerembed.set_footer(text=f'Thanks for participating!')
      winnerembed.timestamp = datetime.datetime.utcnow()
      winnerembed.set_thumbnail(url=winner.avatar_url)
      await ctx.send(embed=winnerembed)
      await ctx.send(f'Congrats! {winner.mention}')


    @commands.command()
    @commands.has_role('Giveaways')
    async def reroll(self, ctx, channel: discord.TextChannel, messageid: int):
      try:
        new_msg = await channel.fetch_message(messageid)
      except:
        await ctx.send(f"{ctx.author.mention}, I could not find that ID! Make sure you gave the right channel and right message, then try again.")
        return
      user_list = [u for u in await new_msg.reactions[0].users().flatten() if u != self.bot.user]

      if len(user_list) == 0:
        await ctx.send("No one reacted.")
      else:
        winner = random.choice(user_list)

      await channel.send(f"Congrats! The new winner is: {winner.mention}!")

    @commands.command()
    @commands.has_role('Giveaways')
    async def deletegiveaway(self, ctx, channel: discord.TextChannel, messageid: int):
      try:
        new_msg = await channel.fetch_message(messageid)
      except:
        await ctx.send(f"{ctx.author.mention}, I could not find that ID! Make sure you gave the right channel and right message, then try again.")
        return
            
      await new_msg.delete()

      await channel.send(f"{ctx.author.mention}, that giveaway was deleted! Message ID: {messageid}")

def setup(bot):
    bot.add_cog(Commands(bot))