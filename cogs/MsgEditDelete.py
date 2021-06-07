import discord
import datetime
import json
from discord.ext import commands

class MsgEditDelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
      if before.guild.id == 730922649144000602:
        if before.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

        try:
          if log_channel:
            log_channel = before.guild.get_channel(log_channel[str(before.guild.id)])
            logembed=discord.Embed(title="Message Edited", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {before.author.name} • Message ID : {before.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Before:', value=before.content + "\u200b", inline=False)
            logembed.add_field(name="After:", value=after.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=before.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=before.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if before.guild.id == 742027175628242954:
        if before.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

        try:
          if log_channel:
            log_channel = before.guild.get_channel(log_channel[str(before.guild.id)])
            logembed=discord.Embed(title="Message Edited", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {before.author.name} • Message ID : {before.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Before:', value=before.content + "\u200b", inline=False)
            logembed.add_field(name="After:", value=after.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=before.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=before.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if before.guild.id == 757014581984886856:
        if before.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

        try:
          if log_channel:
            log_channel = before.guild.get_channel(log_channel[str(before.guild.id)])
            logembed=discord.Embed(title="Message Edited", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {before.author.name} • Message ID : {before.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Before:', value=before.content + "\u200b", inline=False)
            logembed.add_field(name="After:", value=after.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=before.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=before.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if before.guild.id == 774425673841901578:
        if before.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

        try:
          if log_channel:
            log_channel = before.guild.get_channel(log_channel[str(before.guild.id)])
            logembed=discord.Embed(title="Message Edited", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {before.author.name} • Message ID : {before.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Before:', value=before.content + "\u200b", inline=False)
            logembed.add_field(name="After:", value=after.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=before.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=before.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if before.guild.id == 811362696456437770:
        if before.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

        try:
          if log_channel:
            log_channel = before.guild.get_channel(log_channel[str(before.guild.id)])
            logembed=discord.Embed(title="Message Edited", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {before.author.name} • Message ID : {before.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Before:', value=before.content + "\u200b", inline=False)
            logembed.add_field(name="After:", value=after.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=before.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=before.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if before.guild.id == 821556171735040020:
        if before.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

        try:
          if log_channel:
            log_channel = before.guild.get_channel(log_channel[str(before.guild.id)])
            logembed=discord.Embed(title="Message Edited", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {before.author.name} • Message ID : {before.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Before:', value=before.content + "\u200b", inline=False)
            logembed.add_field(name="After:", value=after.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=before.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=before.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if before.guild.id == 836412234673815590:
        if before.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

        try:
          if log_channel:
            log_channel = before.guild.get_channel(log_channel[str(before.guild.id)])
            logembed=discord.Embed(title="Message Edited", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {before.author.name} • Message ID : {before.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Before:', value=before.content + "\u200b", inline=False)
            logembed.add_field(name="After:", value=after.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=before.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=before.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if before.guild.id == 847085861761187850:
        if before.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)

        try:
          if log_channel:
            log_channel = before.guild.get_channel(log_channel[str(before.guild.id)])
            logembed=discord.Embed(title="Message Edited", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {before.author.name} • Message ID : {before.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Before:', value=before.content + "\u200b", inline=False)
            logembed.add_field(name="After:", value=after.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=before.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=before.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

    @commands.Cog.listener()
    async def on_message_delete(self, message):
      if message.guild.id == 730922649144000602:
        if message.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)
        
        try:
          if log_channel:
            log_channel = message.guild.get_channel(log_channel[str(message.guild.id)])
            logembed=discord.Embed(title="Message Deleted", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {message.author.name} • Message ID : {message.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Message:', value=message.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=message.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=message.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if message.guild.id == 742027175628242954:
        if message.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)
        
        try:
          if log_channel:
            log_channel = message.guild.get_channel(log_channel[str(message.guild.id)])
            logembed=discord.Embed(title="Message Deleted", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {message.author.name} • Message ID : {message.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Message:', value=message.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=message.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=message.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if message.guild.id == 757014581984886856:
        if message.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)
        
        try:
          if log_channel:
            log_channel = message.guild.get_channel(log_channel[str(message.guild.id)])
            logembed=discord.Embed(title="Message Deleted", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {message.author.name} • Message ID : {message.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Message:', value=message.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=message.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=message.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if message.guild.id == 774425673841901578:
        if message.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)
        
        try:
          if log_channel:
            log_channel = message.guild.get_channel(log_channel[str(message.guild.id)])
            logembed=discord.Embed(title="Message Deleted", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {message.author.name} • Message ID : {message.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Message:', value=message.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=message.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=message.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if message.guild.id == 811362696456437770:
        if message.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)
        
        try:
          if log_channel:
            log_channel = message.guild.get_channel(log_channel[str(message.guild.id)])
            logembed=discord.Embed(title="Message Deleted", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {message.author.name} • Message ID : {message.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Message:', value=message.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=message.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=message.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if message.guild.id == 821556171735040020:
        if message.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)
        
        try:
          if log_channel:
            log_channel = message.guild.get_channel(log_channel[str(message.guild.id)])
            logembed=discord.Embed(title="Message Deleted", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {message.author.name} • Message ID : {message.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Message:', value=message.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=message.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=message.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if message.guild.id == 836412234673815590:
        if message.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)
        
        try:
          if log_channel:
            log_channel = message.guild.get_channel(log_channel[str(message.guild.id)])
            logembed=discord.Embed(title="Message Deleted", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {message.author.name} • Message ID : {message.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Message:', value=message.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=message.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=message.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

      if message.guild.id == 847085861761187850:
        if message.author.bot:
          return
        with open('logchannel.json', 'r', encoding='utf-8') as fp:
          log_channel = json.load(fp)
        
        try:
          if log_channel:
            log_channel = message.guild.get_channel(log_channel[str(message.guild.id)])
            logembed=discord.Embed(title="Message Deleted", color=0x00FFFF)
            logembed.set_footer(text=f"Member : {message.author.name} • Message ID : {message.id}")
            logembed.timestamp = datetime.datetime.utcnow()
            logembed.add_field(name='Message:', value=message.content + "\u200b", inline=False)
            logembed.add_field(name="Channel:", value=message.channel.name + "\u200b", inline=False)
            logembed.set_thumbnail(url=message.author.avatar_url)
            await log_channel.send(embed=logembed)
          else:
            pass
        except (AttributeError, KeyError):
          pass

def setup(bot):
  bot.add_cog(MsgEditDelete(bot))