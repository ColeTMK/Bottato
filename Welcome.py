import discord
import json
from discord.ext import commands
import datetime

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
      embed=discord.Embed(description=f'**Welcome {member.name}!**\nMake sure to read our rules and verify if needed. Have a great time :D', color=0x00FFFF)
      embed.timestamp = datetime.datetime.utcnow()
      pfp = member.avatar_url
      embed.set_author(name=f'{member} joined!', icon_url=pfp)
      memberpfp = member.avatar_url
      embed.set_thumbnail(url=memberpfp)
      with open('welcomechannel.json', 'r', encoding='utf-8') as fp:
        get_channel = json.load(fp)

        try:
            if get_channel:
                channel = member.guild.get_channel(get_channel[str(member.guild.id)])
                await channel.send(embed=embed)
                await member.send(f'Thanks for joining **{member.guild.name}**! Make sure to read our rules and verify if needed.')
            else:
                await member.send(f'Thanks for joining **{member.guild.name}**! Make sure to read our rules and verify if needed.')
        except (AttributeError, KeyError):
            await member.send(f'Thanks for joining **{member.guild.name}**! Make sure to read our rules and verify if needed.')

def setup(bot):
    bot.add_cog(Welcome(bot))