from itertools import cycle
import discord
from discord.ext import commands
import json
import datetime
import asyncio

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
  print('Bot is connected to:')
  for server in bot.guilds:
    print(server.name, server.id)
  embed=discord.Embed(title="Bot Restart", color=0x00FFFF)
  embed.timestamp = datetime.datetime.utcnow()
  await channel.send(embed=embed)
  statuses = [f'{len(set(bot.get_all_members()))} members and {len(bot.guilds)} servers!', f'>help for help!']


  displaying = cycle(statuses)

  running = True

  while running:
    current_status = next(displaying)
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=current_status ,type=3))
    await asyncio.sleep(60)

@bot.command()
async def toggle(ctx, *, command):
  if ctx.author.id == 467715040087244800:
    command = bot.get_command(command)

    if command is None:
        await ctx.send(f'{ctx.author.mention}, I cannot find that command! Please try again.')
        return

    else:
        command.enabled = not command.enabled
        ternary = "enabled" if command.enabled else "disabled"
        await ctx.send(f"I have {ternary} the {command.qualified_name} command!")
  else:
    return

bot.load_extension('AutoMod')
bot.load_extension('Commands')
bot.load_extension('Games')
bot.load_extension('Economy')
bot.load_extension('ErrorHandlers')
bot.load_extension('MsgEditDelete')
bot.load_extension('Warns')
bot.load_extension('Welcome')

bot.run('ODMwNTk5ODM5NjIzNjc1OTI1.YHJCYQ.kzMTlKbjNzSmw2cXtc96JVmEiTc')