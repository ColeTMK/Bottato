import discord
import datetime
import DiscordUtils
from discord.ext import commands

music = DiscordUtils.Music()

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
      invc = ctx.author.voice
      botinvc = ctx.guild.me.voice
      if botinvc:
          await ctx.send(f"{ctx.author.mention}, I'm already in a VC!")
          return
      if invc:
        await ctx.author.voice.channel.connect()
        embed=discord.Embed(description='Joined VC!', color=0x00FFFF)
        author = ctx.author
        pfp = author.avatar_url
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=f"{ctx.author.name}", icon_url=pfp)
        await ctx.send(embed=embed)
      if not invc:
        await ctx.send(f'{ctx.author.mention}, You need to be in a VC so I can join!')
        return

    @commands.command()
    async def leave(self, ctx):
        invc = ctx.author.voice
        botinvc = ctx.guild.me.voice
        if not botinvc:
            await ctx.send(f"{ctx.author.mention}, I'm not in a VC!")
            return
        if not invc:
            await ctx.send(f'{ctx.author.mention}, You are not in a VC!')
            return
        else:
            await ctx.guild.voice_client.disconnect() 
            embed=discord.Embed(description='Left VC!', color=0x00FFFF)
            author = ctx.author
            pfp = author.avatar_url
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_author(name=f"{ctx.author.name}", icon_url=pfp)
            await ctx.send(embed=embed)

    @commands.command()
    async def play(self, ctx, *, url):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            player =  music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            await ctx.send(f'Now Playing: `{song.name}`')
        else:
            song = await player.queue(url, search=True)
            await ctx.send(f'{ctx.author.mention}, `{song.name}` has been added to the queue!')


def setup(bot):
  bot.add_cog(Music(bot))