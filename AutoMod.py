import discord
import json
import datetime
import asyncio
from discord.ext import commands

def get_prefix(bot, message):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)
	return prefixes[str(message.guild.id)]

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        curseWord = ['shit', 'asshole', 'fuck', 'bitch', 'cunt', 'nigger', 'faggot', 'fag', 'nigga', 'dick', 'cock', 'pussy', 'hoe']
        msg_content = message.content.lower()  

        if any(word in msg_content for word in curseWord):
            if message.channel.type == discord.ChannelType.private:
                return
            if message.author.id == 330988962162147329: #johnny
                return
            if message.author.id == 261578097978114050: #devvy
                return
            if message.author.id == 467715040087244800: #me
                return
            if message.author.guild_permissions.administrator:
                return
            if message.author.guild_permissions.manage_messages:
                return
            if message.guild.id == 859603774669979648: #ghost's server
                return

            await message.delete()
            embed=discord.Embed(title="Swear Word", description=f"{message.author.mention}, Hey! Those words arent allowed here! Please refrain from saying this again!", color=0x00FFFF)
            embed.timestamp = datetime.datetime.utcnow()
            author = message.author
            pfp = author.avatar_url
            embed.set_author(name=f"{author.name}", icon_url=pfp)
            await message.channel.send(embed=embed)
            dmembed=discord.Embed(title="AutoMod", description="You were caught saying a bad word! Please refrain from saying this again!", color=0x00FFFF)
            dmembed.add_field(name="**Message:**", value=f"{msg_content}", inline=False)
            pfp = author.avatar_url
            dmembed.add_field(name="**Server:**", value=f"{message.guild.name}", inline=False)
            dmembed.set_author(name=f"{author.name}", icon_url=pfp)
            dmembed.timestamp = datetime.datetime.utcnow()
            with open('logchannel.json', 'r', encoding='utf-8') as fp:
                log_channel = json.load(fp)

            try:
                await message.author.send(embed=dmembed)
            except:
                pass #ignore error if DM are closed
            try:
                if log_channel:
                    log_channel = message.guild.get_channel(log_channel[str(message.guild.id)])
                    logembed=discord.Embed(title="Bot Log", description="Bad Word Said", color=0x00FFFF)
                    logembed.add_field(name="**Message:**", value=f"{msg_content}", inline=False)
                    logembed.add_field(name="**Member:**", value=f"{message.author.name}", inline=False)
                    author = message.author
                    pfp = author.avatar_url
                    logembed.set_author(name=f"{author}", icon_url=pfp)
                    logembed.timestamp = datetime.datetime.utcnow()
                    await log_channel.send(embed=logembed)
            except (AttributeError, KeyError):
                pass

        if isinstance(message.channel, discord.DMChannel):
            if message.content == '>help':
                embed=discord.Embed(title="Ultimate Bot Help", description="Hello! Here, you can get help from lots of useful links and info!", color=0x00FFFF)
                embed.add_field(name="**Website**", value='https://bit.ly/3okQzMh', inline=False)
                embed.add_field(name="**All Commands Page**", value='https://bit.ly/33N0TTY', inline=False)
                embed.add_field(name="**Terms & Conditions:**", value='https://bit.ly/3yEYs48', inline=False)
                embed.add_field(name="**Support Server:**", value='https://discord.gg/arMVCzHfuf', inline=False)
                embed.add_field(name="**Moderator Commands**", value='`clear` `warn` `kick` `ban` `mute` `tempmute` `unmute` `unlock/lockchannel` `give/removerole` `slowmode` `setlogchannel` `setwelcomechannel`', inline=False)
                embed.add_field(name="**Admin Commands**", value='`dm` `changeprefix` `addcoins`', inline=False)
                embed.add_field(name="**Fun Commands**", value='`fact` `quote` `ping` `deadchat` `loved` `pfp` `numbergame` `rps` `suggest` `userinfo` `serverinfo` `membercount` `servercount` `invite`', inline=False)
                embed.add_field(name="**Economy**", value='`balance` `work` `beg` `give` `deposit` `withdraw`', inline=False)
                embed.add_field(name="**AutoMod**", value='*Members that have admin and/or manage messages perms are bypassed by AutoMod!* Click this link to see what words will get deleted -> https://bit.ly/33N0TTY **IF YOU WANT THE LIST CHANGED FOR YOUR SERVER, JOIN https://discord.gg/arMVCzHfuf**', inline=False)
                embed.add_field(name="**Message Edit/Delete Events**", value='If a message gets Deleted or Edited, the bot will log it in the log channel that is set.', inline=False)
                embed.add_field(name="**Prefix Info**", value='My **DEFAULT** prefix is `>` To change, type `>changeprefix {prefix}`', inline=False)
                embed.add_field(name="**Current Prefix**", value=f'The **CURRENT** prefix for this server is `{get_prefix(self.bot, ctx.message)}`', inline=False)
                embed.timestamp = datetime.datetime.utcnow()
                await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(AutoMod(bot))