import discord
import datetime
import DiscordUtils
from discord.ext import commands

music = DiscordUtils.Music()

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
            embed.set_author(name=f"{ctx.author}", icon_url=pfp)
            await ctx.send(embed=embed)

    @commands.command()
    async def play(self, ctx, *, url):
        invc = ctx.author.voice
        botinvc = ctx.guild.me.voice
        if not invc:
            await ctx.send(f'{ctx.author.mention}, You are not in a VC!')
            return
        if invc:
            if not botinvc:
                await ctx.author.voice.channel.connect()
                player = music.get_player(guild_id=ctx.guild.id)
                if not player:
                    player =  music.create_player(ctx, ffmpeg_error_betterfix=True)
                if not ctx.voice_client.is_playing():
                    await player.queue(url, search=True)
                    song = await player.play()
                    await ctx.send(f'Now Playing: `{song.name}`')
            
            if botinvc:
                player = music.get_player(guild_id=ctx.guild.id)
                if not player:
                    player =  music.create_player(ctx, ffmpeg_error_betterfix=True)
                if not ctx.voice_client.is_playing():
                    await player.queue(url, search=True)
                    song = await player.play()
                    await ctx.send(f'Now Playing: `{song.name}`')
                else:
                    song = await player.queue(url, search=True)
                    embed=discord.Embed(title='Song Added to Queue!', description=f'**{song.name}** added!', color=0x00FFFF)
                    author = ctx.message.author
                    pfp = author.avatar_url
                    embed.set_author(name=f"{ctx.author.name}", icon_url=pfp)
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text=f'Added by {ctx.author}')
                    await ctx.send(embed=embed)

    @commands.command()
    async def pause(self, ctx):
        invc = ctx.author.voice
        botinvc = ctx.guild.me.voice
        if not botinvc:
            await ctx.send(f"{ctx.author.mention}, I'm not in a VC!")
            return
        if not invc:
            await ctx.send(f'{ctx.author.mention}, You are not in a VC!')
            return
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        embed=discord.Embed(description='Music Paused!', color=0x00FFFF)
        author = ctx.author
        pfp = author.avatar_url
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=f"{ctx.author.name}", icon_url=pfp)
        embed.set_footer(text=f'Paused by {ctx.author}')
        await ctx.send(embed=embed)

    @commands.command()
    async def resume(self, ctx):
        invc = ctx.author.voice
        botinvc = ctx.guild.me.voice
        if not botinvc:
            await ctx.send(f"{ctx.author.mention}, I'm not in a VC!")
            return
        if not invc:
            await ctx.send(f'{ctx.author.mention}, You are not in a VC!')
            return
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        embed=discord.Embed(description='Music Resumed!', color=0x00FFFF)
        author = ctx.author
        pfp = author.avatar_url
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=f"{ctx.author.name}", icon_url=pfp)
        embed.set_footer(text=f'Resumed by {ctx.author}')
        await ctx.send(embed=embed)

    @commands.command()
    async def skip(self, ctx):
        invc = ctx.author.voice
        botinvc = ctx.guild.me.voice
        if not botinvc:
            await ctx.send(f"{ctx.author.mention}, I'm not in a VC!")
            return
        if not invc:
            await ctx.send(f'{ctx.author.mention}, You are not in a VC!')
            return
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.skip()

    @commands.command()
    async def stop(self, ctx):
        invc = ctx.author.voice
        botinvc = ctx.guild.me.voice
        if not botinvc:
            await ctx.send(f"{ctx.author.mention}, I'm not in a VC!")
            return
        if not invc:
            await ctx.send(f'{ctx.author.mention}, You are not in a VC!')
            return
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.stop()
        embed=discord.Embed(title='Music Stopped!', description=f'`>leave to make bot leave VC`', color=0x00FFFF)
        author = ctx.author
        pfp = author.avatar_url
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=f"{ctx.author.name}", icon_url=pfp)
        embed.set_footer(text=f'Stopped by {ctx.author}')
        await ctx.send(embed=embed)

    @commands.command()
    async def playing(self, ctx):
        invc = ctx.author.voice
        botinvc = ctx.guild.me.voice
        player = music.get_player(guild_id=ctx.guild.id)
        currentsong = player.now_playing()
        if not botinvc:
            await ctx.send(f"{ctx.author.mention}, I'm not in a VC!")
            return
        if not invc:
            await ctx.send(f'{ctx.author.mention}, You are not in a VC!')
            return
        await ctx.send(f'Currently playing: `{currentsong}`')

    @commands.command()
    async def queue(self, ctx):
        invc = ctx.author.voice
        botinvc = ctx.guild.me.voice
        if not botinvc:
            await ctx.send(f"{ctx.author.mention}, I'm not in a VC!")
            return
        if not invc:
            await ctx.send(f'{ctx.author.mention}, You are not in a VC!')
            return
        nextline = " \n"
        player = music.get_player(guild_id=ctx.guild.id)
        await ctx.send(f"{nextline.join([song.name for song in player.current_queue()])}")

def setup(bot):
  bot.add_cog(Music(bot))