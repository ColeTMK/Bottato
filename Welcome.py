import discord
import json
from discord.ext import commands
import datetime

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setwelcomemessage(self, ctx, *, message):
      with open('welcomemessage.json', 'r', encoding='utf-8') as fp:
        get_message = json.load(fp)

        try:
          get_message[str(ctx.guild.id)] = message
        except KeyError:
          new = {str(ctx.guild.id): message}
          get_message.update(new)

      embed=discord.Embed(title="Welcome Message Set", color=0x00FFFF)
      embed.add_field(name="**Message:**", value=f"{message}", inline=True)
      embed.add_field(name="**Moderator:**", value=f"{ctx.author.name}", inline=True)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)
      await ctx.author.send(f"You just set the welcome message for **{ctx.guild.name}** to *{message}* !")

      with open('welcomemessage.json', 'w', encoding='utf-8') as fpp:
        json.dump(get_message, fpp, indent=2)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def setwelcomechannel(self, ctx, channel: discord.TextChannel):
      with open('welcomechannel.json', 'r', encoding='utf-8') as fp:
        get_wchannel = json.load(fp)

      try:
        get_wchannel[str(ctx.guild.id)] = channel.id
      except KeyError:
        new = {str(ctx.guild.id): channel.id}
        get_wchannel.update(new)

      embed=discord.Embed(title="Welcome Channel Set", color=0x00FFFF)
      embed.add_field(name="**Channel Name:**", value=f"{channel}", inline=True)
      embed.add_field(name="**Moderator:**", value=f"{ctx.author.name}", inline=True)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)
      await ctx.author.send(f"You just set the welcome channel for **{ctx.guild.name}** to *{channel}* !")

      with open('welcomechannel.json', 'w', encoding='utf-8') as fpp:
        json.dump(get_wchannel, fpp, indent=2)

    @commands.Cog.listener()
    async def on_member_join(self, member):
      def get_message():
        with open('welcomemessage.json', 'r') as fp:
          get_message = json.load(fp)
      def get_wchannel(guild):
        with open('welcomechannel.json', 'r') as fp:
          get_wchannel = json.load(fp)
          try:
            return get_wchannel[str(guild.id)]
          except KeyError:
            return
      embed=discord.Embed(title=f'{member} joined!', description=get_message(), color=0x00FFFF)
      embed.timestamp = datetime.datetime.utcnow()
      pfp = member.avatar_url
      embed.set_author(name=f"{member}", icon_url=pfp)
      memberpfp = member.avatar_url
      embed.set_thumbnail(url=memberpfp)
      try:
        if get_wchannel(member.guild) is not None:
          await get_wchannel(member.guild).send(embed=embed)
      except KeyError:
        return

def setup(bot):
    bot.add_cog(Welcome(bot))