import discord
from discord import User
from discord.ext import commands
import random
import requests
import json
import asyncio
import datetime
from discord.ext.commands import Bot, Greedy

def get_logchannel(bot, message):
    with open('logchannel.json', 'r') as fp:
        log_channel = json.load(fp)
    try:
        return log_channel[str(message.guild.id)]
    except KeyError:
        return "`No log channel is set!`"
def get_welcomechannel(bot, message):
    with open('welcomechannel.json', 'r') as fp:
        welcomechannel = json.load(fp)
    try:
        return welcomechannel[str(message.guild.id)]
    except KeyError:
        return "`No welcome channel is set!`"

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, input=None):

        def get_prefix(bot, message):
            with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)
            return prefixes[str(message.guild.id)]

        mainembed=discord.Embed(title="Bottato Help", description="Hello! Here, you can get help from lots of useful links and info! **By using Bottato, you agree to the Terms & Conditions**", color=0x00FFFF)
        mainembed.add_field(name='⚙️ | **Bot Setup/Config:**', value=f'`{get_prefix(self.bot, ctx.message)}help config`', inline=True)
        mainembed.add_field(name='⚔️ | **Moderation:**', value=f'`{get_prefix(self.bot, ctx.message)}help moderation`', inline=True)
        mainembed.add_field(name='🏓 | **Fun:**', value=f'`{get_prefix(self.bot, ctx.message)}help fun`', inline=True)
        mainembed.add_field(name='💰 | **Economy:**', value=f'`{get_prefix(self.bot, ctx.message)}help economy`', inline=True)
        mainembed.add_field(name='🎲 | **Minigames:**', value=f'`{get_prefix(self.bot, ctx.message)}help minigames`', inline=True)
        mainembed.add_field(name='🎉 | **Giveaways:**', value=f'`{get_prefix(self.bot, ctx.message)}help giveaways`', inline=True)
        mainembed.add_field(name='🔗 | **Links:**', value=f'`{get_prefix(self.bot, ctx.message)}help links`', inline=True)
        mainembed.add_field(name="**Current Prefix**", value=f'The **CURRENT** prefix for this server is `{get_prefix(self.bot, ctx.message)}`', inline=False)
        mainembed.timestamp = datetime.datetime.utcnow()
        mainembed.set_footer(text='Support Server : https://discord.gg/arMVCzHfuf')
        mainembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/830599839623675925/7e5e5152a2490e6d3e89dd09f2f33a99.webp?size=1024")

        setupconfigembed=discord.Embed(title='Setup/Config Help', description='Here, you can get help for setting me up for your server!', color=0x00FFFF)
        setupconfigembed.add_field(name='**Change Prefix Command:**', value=f'`{get_prefix(self.bot, ctx.message)}changeprefix [prefix]`', inline=False)
        setupconfigembed.add_field(name='**Set Welcome Channel Command:**', value=f'`{get_prefix(self.bot, ctx.message)}setwelcomechannel [channel]`', inline=False)
        setupconfigembed.add_field(name='**Set Logging Channel Command:**', value=f'`{get_prefix(self.bot, ctx.message)}setlogchannel [channel]`', inline=False)
        setupconfigembed.add_field(name="Current Prefix:", value=f'The current prefix for this server is `{get_prefix(self.bot, ctx.message)}`', inline=False)
        if get_logchannel != None:
            setupconfigembed.add_field(name="Current Log Channel:", value=f"`{get_logchannel(self.bot, ctx.message)}`", inline=False)     
        if get_welcomechannel != None:
            setupconfigembed.add_field(name="Current Welcome Channel:", value=f"`{get_welcomechannel(self.bot, ctx.message)}`", inline=False)
        setupconfigembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/830599839623675925/7e5e5152a2490e6d3e89dd09f2f33a99.webp?size=1024")
        setupconfigembed.timestamp = datetime.datetime.utcnow()

        moderationembed=discord.Embed(title='Moderation Help', description='Here, you can get help for moderation commands!', color=0x00FFFF)
        moderationembed.add_field(name='Clear/Purge Messages:', value=f'`{get_prefix(self.bot, ctx.message)}clear [amount]`', inline=True)
        moderationembed.add_field(name='**Warn:**', value=f'`{get_prefix(self.bot, ctx.message)}warn [member] [reason]`\n`{get_prefix(self.bot, ctx.message)}warns [member]`\n`{get_prefix(self.bot, ctx.message)}removewarns [member] [amount]`', inline=True)
        moderationembed.add_field(name='**Kick:**', value=f'`{get_prefix(self.bot, ctx.message)}kick [member] [reason]`', inline=True)
        moderationembed.add_field(name='**Ban:**', value=f'`{get_prefix(self.bot, ctx.message)}ban [member] [reason]`', inline=True)
        moderationembed.add_field(name='**Mute:**', value=f'`{get_prefix(self.bot, ctx.message)}mute [member] [reason]`', inline=True)
        moderationembed.add_field(name='**Temp. Mute:**', value=f'`{get_prefix(self.bot, ctx.message)}tempmute [member] [duration in seconds] [reason]`', inline=True)
        moderationembed.add_field(name='**Unmute:**', value=f'`{get_prefix(self.bot, ctx.message)}unmute [member]`', inline=True)
        moderationembed.add_field(name='**Change Nickname:**', value=f'`{get_prefix(self.bot, ctx.message)}changenickname [member] [nickname]`', inline=True)
        moderationembed.add_field(name='**Give Role:**', value=f'`{get_prefix(self.bot, ctx.message)}giverole [member] [role]`', inline=True)
        moderationembed.add_field(name='**Remove Role:**', value=f'`{get_prefix(self.bot, ctx.message)}removerole [member] [role]`', inline=True)
        moderationembed.add_field(name='**Lock Channel:**', value=f'`{get_prefix(self.bot, ctx.message)}lockchannel`', inline=True)
        moderationembed.add_field(name='**Warn:**', value=f'`{get_prefix(self.bot, ctx.message)}unlockchannel`', inline=True)
        moderationembed.add_field(name='**Slowmode:**', value=f'`{get_prefix(self.bot, ctx.message)}slowmode [duration in seconds]`', inline=True)
        moderationembed.add_field(name='**DM:**', value=f'`{get_prefix(self.bot, ctx.message)}dm [member(s)] [message]`', inline=True)
        moderationembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/830599839623675925/7e5e5152a2490e6d3e89dd09f2f33a99.webp?size=1024")
        moderationembed.timestamp = datetime.datetime.utcnow()

        funembed=discord.Embed(title='Fun Help', description='Here, you can get help for fun commands!', color=0x00FFFF)
        funembed.add_field(name='**Random Fact:**', value=f'`{get_prefix(self.bot, ctx.message)}fact`', inline=False)
        funembed.add_field(name='**Random Quote:**', value=f'`{get_prefix(self.bot, ctx.message)}quote`', inline=False)
        funembed.add_field(name='**Bot Ping:**', value=f'`{get_prefix(self.bot, ctx.message)}ping`', inline=False)
        funembed.add_field(name='**Random Fact:**', value=f'`{get_prefix(self.bot, ctx.message)}fact`', inline=False)
        funembed.add_field(name='**Random Dog Pic:**', value=f'`{get_prefix(self.bot, ctx.message)}dog`', inline=False)
        funembed.add_field(name='**Random Cat Pic:**', value=f'`{get_prefix(self.bot, ctx.message)}cat`', inline=False)
        funembed.add_field(name='**Dead Chat:**', value=f'`{get_prefix(self.bot, ctx.message)}deadchat`', inline=False)
        funembed.add_field(name='**Love Message:**', value=f'`{get_prefix(self.bot, ctx.message)}loved`', inline=False)
        funembed.add_field(name='**Avatar:**', value=f'`{get_prefix(self.bot, ctx.message)}avatar [member]`', inline=False)
        funembed.add_field(name='**Suggest:**', value=f'`{get_prefix(self.bot, ctx.message)}suggest [suggestion]`', inline=False)
        funembed.add_field(name='**Userinfo:**', value=f'`{get_prefix(self.bot, ctx.message)}userinfo [member]`', inline=False)
        funembed.add_field(name='**Membercount:**', value=f'`{get_prefix(self.bot, ctx.message)}membercount`', inline=False)
        funembed.add_field(name='**Servercount:**', value=f'`{get_prefix(self.bot, ctx.message)}servercount`', inline=False)
        funembed.add_field(name='**Server Info:**', value=f'`{get_prefix(self.bot, ctx.message)}serverinfo`', inline=False)
        funembed.add_field(name='**Bot Invite:**', value=f'`{get_prefix(self.bot, ctx.message)}invite`', inline=False)
        funembed.add_field(name='**Support:**', value=f'`{get_prefix(self.bot, ctx.message)}support`', inline=False)
        funembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/830599839623675925/7e5e5152a2490e6d3e89dd09f2f33a99.webp?size=1024")
        funembed.timestamp = datetime.datetime.utcnow()

        economyembed=discord.Embed(title='Economy Help', description='Here, you can get help for economy commands!', color=0x00FFFF)
        economyembed.add_field(name='**Work:**', value=f'`{get_prefix(self.bot, ctx.message)}work`', inline=False)
        economyembed.add_field(name='**Beg:**', value=f'`{get_prefix(self.bot, ctx.message)}beg`', inline=False)
        economyembed.add_field(name='**Balance:**', value=f'`{get_prefix(self.bot, ctx.message)}bal [member]`', inline=False)
        economyembed.add_field(name='**Give:**', value=f'`{get_prefix(self.bot, ctx.message)}give [member] [amount]`', inline=False)
        economyembed.add_field(name='**Deposit:**', value=f'`{get_prefix(self.bot, ctx.message)}deposit [amount]`', inline=False)
        economyembed.add_field(name='**Withdraw:**', value=f'`{get_prefix(self.bot, ctx.message)}withdraw`', inline=False)
        economyembed.add_field(name='**Add Coins:**', value=f'`{get_prefix(self.bot, ctx.message)}addcoins [member] [amount]` ADMIN ONLY!', inline=False)
        economyembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/830599839623675925/7e5e5152a2490e6d3e89dd09f2f33a99.webp?size=1024")
        economyembed.timestamp = datetime.datetime.utcnow()

        minigamesembed=discord.Embed(title='Minigames Help', description='Here, you can get help for minigame commands!', color=0x00FFFF)
        minigamesembed.add_field(name='**Guess the Number:**', value=f'`{get_prefix(self.bot, ctx.message)}numbergame`', inline=False)
        minigamesembed.add_field(name='**Rock, Paper, Scissors:**', value=f'`{get_prefix(self.bot, ctx.message)}rps`', inline=False)
        minigamesembed.add_field(name='**Akinator:**', value=f'`{get_prefix(self.bot, ctx.message)}akinator`', inline=False)
        minigamesembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/830599839623675925/7e5e5152a2490e6d3e89dd09f2f33a99.webp?size=1024")
        minigamesembed.timestamp = datetime.datetime.utcnow()

        giveawaysembed=discord.Embed(title='Giveaways Help', description='Here, you can get help for giveaway commands!', color=0x00FFFF)
        giveawaysembed.add_field(name='**Create Giveaway:**', value=f'`{get_prefix(self.bot, ctx.message)}gcreate [duration] [prize]`\n\nAn example of a correct command is..\n\n`{get_prefix(self.bot, ctx.message)}gcreate 7d Discord Nitro Classic for 1 Month`', inline=False)
        giveawaysembed.add_field(name='**Reroll Giveaway:**', value=f'`{get_prefix(self.bot, ctx.message)}reroll [channel] [message id]`', inline=False)
        giveawaysembed.add_field(name='**Delete Giveaway:**', value=f'`{get_prefix(self.bot, ctx.message)}deletegiveaway [channel] [message id]`', inline=False)
        giveawaysembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/830599839623675925/7e5e5152a2490e6d3e89dd09f2f33a99.webp?size=1024")
        giveawaysembed.timestamp = datetime.datetime.utcnow()

        linksembed=discord.Embed(title='Links Help', description='Here, you can access import links to websites and more!', color=0x00FFFF)
        linksembed.add_field(name="**Website:**", value='https://bit.ly/3okQzMh', inline=False)
        linksembed.add_field(name="**All Commands Page:**", value='https://bit.ly/33N0TTY', inline=False)
        linksembed.add_field(name="**Terms & Conditions:**", value='https://bit.ly/3yEYs48', inline=False)
        linksembed.add_field(name="**Support Server:**", value='https://discord.gg/arMVCzHfuf', inline=False)
        linksembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/830599839623675925/7e5e5152a2490e6d3e89dd09f2f33a99.webp?size=1024")
        linksembed.timestamp = datetime.datetime.utcnow()

        if input == None:
            await ctx.send(embed=mainembed)
        if input == 'config':
            await ctx.send(embed=setupconfigembed)
        if input == 'moderation':
            await ctx.send(embed=moderationembed)
        if input == 'fun':
            await ctx.send(embed=funembed)
        if input == 'economy':
            await ctx.send(embed=economyembed)
        if input == 'minigames':
            await ctx.send(embed=minigamesembed)
        if input == 'giveaways':
            await ctx.send(embed=giveawaysembed)
        if input == 'links':
            await ctx.send(embed=linksembed)

def setup(bot):
    bot.add_cog(Help(bot))