from itertools import cycle
import discord
from discord.ext import commands
import json
import datetime
import asyncio
import time

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

    with open('serverlist.json', 'r') as f:
        serverlist = json.load(f)

    serverlist[str(guild.id)] = str(guild.owner.id)

    with open('serverlist.json', 'w') as f:
        json.dump(serverlist, f, indent=4)

    guildowner = guild.owner
    embed=discord.Embed(title='Thanks for inviting me! Please read below for important info.', description=f'ColeTMK#1234 is really appreciated by you that you invited Bottato to **{guild.name}**! Please read some info that can be very helpful for you, your mods, and members!\n\nThe DEFAULT prefix for your server is `>` This can be changed by the command `>changeprefix [prefix`', color=0x00FFFF)
    
    embed.set_footer(text=f'If your experience any issues with me, please join the support server! https://discord.gg/arMVCzHfuf | Thanks for inviting me to **{guild.name}**!')
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/830599839623675925/7e5e5152a2490e6d3e89dd09f2f33a99.webp?size=1024")
    try:
      await guildowner.send(embed=embed)
    except:
      pass

    cole = bot.get_user(467715040087244800)
    total = len(guild.members)
    humans = len(list(filter(lambda m: not m.bot, guild.members)))
    bots = len(list(filter(lambda m: m.bot, guild.members)))
    embed=discord.Embed(title='New Server Join!', color=0x00FFFF)
    embed.add_field(name='Server Name:', value=f'`{guild.name}`', inline=False)
    embed.add_field(name='Server ID:', value=f'`{guild.id}`', inline=False)
    embed.add_field(name='Owner:', value=f'`{guild.owner}`', inline=False)
    embed.add_field(name='Owner ID:', value=f'`{guild.owner.id}`', inline=False)
    embed.add_field(name='Server Region:', value=f'`{guild.region}`', inline=False)
    embed.add_field(name='Server Creation Date:', value=f'`{guild.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")}`', inline=False)
    embed.add_field(name='Text Channels:', value=f'`{len(guild.text_channels)} Text Channels`', inline=False)
    embed.add_field(name='Voice Channels:', value=f'`{len(guild.voice_channels)} Voice Channels`', inline=False)
    embed.add_field(name='Roles:', value=f'`{len(guild.roles)} Roles`', inline=False)
    embed.add_field(name='Total Members:', value=f'`{total} Members`', inline=False)
    embed.add_field(name='Humans:', value=f'`{humans} Humans`', inline=False)
    embed.add_field(name='Bots:', value=f'`{bots} Bots`', inline=False)
    embed.add_field(name='Boost Count:', value=f'`{guild.premium_subscription_count} Boosts`', inline=False)
    await cole.send(embed=embed)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)

    with open('serverlist.json', 'r') as f:
        serverlist = json.load(f)

    serverlist.pop(str(guild.id))

    with open('serverlist.json', 'w') as f:
        json.dump(serverlist, f, indent=4)

    with open('logchannel.json', 'r') as f:
        logchannel = json.load(f)

    logchannel.pop(str(guild.id))

    with open('logchannel.json', 'w') as f:
        json.dump(logchannel, f, indent=4)

    with open('welcomechannel.json', 'r') as f:
        welcomechannel = json.load(f)

    welcomechannel.pop(str(guild.id))

    with open('welcomechannel.json', 'w') as f:
        json.dump(welcomechannel, f, indent=4)

@bot.event
async def on_ready():
  global startTime
  startTime = time.time()
  channel = bot.get_channel(848722304069926993)
  print('The bot is online!')
  print('Bot is connected to:')
  for server in bot.guilds:
    print(server.name, server.id)
  embed=discord.Embed(title="Bot Restart", color=0x00FFFF)
  embed.timestamp = datetime.datetime.utcnow()
  await channel.send(embed=embed)
  statuses = [f'{len(set(bot.get_all_members()))} Members & {len(bot.guilds)} Servers!', 'Ping Me For Server Prefix!', 'Made by ColeTMK#1234']


  displaying = cycle(statuses)

  running = True

  while running:
    current_status = next(displaying)
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=current_status ,type=3))
    await asyncio.sleep(45)

@bot.command()
async def uptime(ctx):
  uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
  embed=discord.Embed(title='Bottato Uptime', description=f'Uptime: {uptime}', color=0x00FFFF)
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.send(embed=embed)

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

bot.load_extension('AutoMod')
bot.load_extension('Commands')
bot.load_extension('Games')
bot.load_extension('Economy')
bot.load_extension('ErrorHandlers')
bot.load_extension('MsgEditDelete')
bot.load_extension('Warns')
bot.load_extension('Welcome')
bot.load_extension('Help')
#bot.load_extension('Music')

bot.run('ODMwNTk5ODM5NjIzNjc1OTI1.YHJCYQ.6AKH-DuIrLs-AL07LZPY9vqTeoI')