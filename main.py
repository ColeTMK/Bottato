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
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '>'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)

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
  statuses = [f'{len(set(bot.get_all_members()))} members and {len(bot.guilds)} servers!', f'>help for help!', 'ping me for server prefix']


  displaying = cycle(statuses)

  running = True

  while running:
    current_status = next(displaying)
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=current_status ,type=3))
    await asyncio.sleep(45)

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

@bot.event
async def on_message(message):
  def get_prefix(message):
        with open('prefixes.json', 'r') as f:
          prefixes = json.load(f)
          return prefixes[str(message.guild.id)]
  if message.content == "<@!830599839623675925>":
    await message.channel.send(f"My prefix for this server is `{get_prefix(message)}`")
  
  await bot.process_commands(message)

@bot.command()
async def cole(ctx):
  embed=discord.Embed(title='Opening a Ticket for Curse Word List Change', description='If you want to open a ticket to change the Curse Word List for your server, do these steps.', color=0x00FFFF)
  embed.add_field(name='Step-1', value='Run `{ulitimate bot prefix}serverinfo` in your server.', inline=False)
  embed.add_field(name='Step-2', value='Click **:envelope_with_arrow: Create ticket** below the Ticket Tool embed.', inline=False)
  embed.add_field(name='Step-3', value='Say you want to change the curse word list in your server AND send a screenshot of the server info embed. (this is to verify that you are the owner of the server that your trying to change the curse word list in!)', inline=False)
  embed.add_field(name='Step-4', value='Wait for assistance by an Admin!', inline=False)
  embed.set_image(url='https://i.stack.imgur.com/9Q7xb.png')
  await ctx.send(embed=embed)

bot.load_extension('AutoMod')
bot.load_extension('Commands')
bot.load_extension('Games')
bot.load_extension('Economy')
bot.load_extension('ErrorHandlers')
bot.load_extension('MsgEditDelete')
bot.load_extension('Warns')
bot.load_extension('Welcome')
#bot.load_extension('Music')

bot.run('ODMwNTk5ODM5NjIzNjc1OTI1.YHJCYQ.kzMTlKbjNzSmw2cXtc96JVmEiTc')