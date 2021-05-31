import discord
import os
from discord.ext import commands
import json
import datetime
from keep_alive import keep_alive

def get_prefix(bot, message):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)
	return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=(get_prefix), intents=discord.Intents.all(), case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '>'#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@bot.event
async def on_ready():
  channel = bot.get_channel(848722304069926993)
  print('The bot is online!')
  await bot.change_presence(
    activity=discord.Activity(type=discord.ActivityType.watching, name="Youtube Videos"))
  print('Bot is connected to:')
  for server in bot.guilds:
    print(server.name, server.id)
  embed=discord.Embed(title="Bot Restart", color=0x00FFFF)
  embed.timestamp = datetime.datetime.utcnow()
  await channel.send(embed=embed)

bot.load_extension('cogs.AutoMod')
bot.load_extension('cogs.Commands')
bot.load_extension('cogs.Games')
bot.load_extension('cogs.Economy')

keep_alive()

bot.run(os.getenv('TOKEN'))