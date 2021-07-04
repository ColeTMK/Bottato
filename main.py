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

    with open('serverlist.json', 'r') as f:
        serverlist = json.load(f)

    serverlist[str(guild.id)] = str(guild.owner.id)

    with open('serverlist.json', 'w') as f:
        json.dump(serverlist, f, indent=4)

    guildowner = guild.owner
    embed=discord.Embed(title='Thanks for inviting me! Please read below for important info.', description=f'ColeTMK#1234 is really appreciated by you that you invited Ultimate Bot to {guild.name}! Please read some info that can be very helpful for you, your mods, and members!', color=0x00FFFF)
    embed.add_field(name='Prefix Info:', value='The DEFAULT prefix that is set for your server is `>`, owner/admins can change this by a simple command! `>changeprefix {prefix}` If you ever forget the prefix for your server, you can just mention me!', inline=False)
    embed.add_field(name='AutoMod Info:', value='AutoMod (Swear Word Filter) is automatically enabled for your server! If you wish to have this disabled or/ banned words change, join the Ultimate Bot Support Server -> https://discord.gg/arMVCzHfuf. To see what words are in the filter, click here -> https://bit.ly/33N0TTY.', inline=False)
    embed.add_field(name='Moderator/Admin Commands:', value='Ultimate Bot has useful commands for you, your admins, and your mods. They include...\n`clear` `ban` `kick` `mute` `tempmute` `unmute` `lockchannel` `unlockchannel` `changenickname` `warn` `warns` `removewarns` `giverole` `removerole`', inline=False)
    embed.add_field(name='Economy:', value='Ultimate Bot has an Economy feature! Commands for this are,\n`work` `beg` `givecoins` `deposit` `withdraw` Admin Only: `addcoins`', inline=False)
    embed.add_field(name='Miscellaneous Commands:', value='Utimate Bot features some commands that members can use and interact with! Some include,\n`rps` `numbergame` `suggest` `pfp` `quote` `fact` These are NOT all of them!', inline=False)
    embed.add_field(name='Welcoming/Leaving:', value='Ultimate Bot can welcome new members that join! Also, when a member leaves! To setup this, type `>setwelcomechannel {channel}` OR `{changedprefix}setwelcomechannel {channel}`', inline=False)
    embed.add_field(name='Logging:', value='Ultimate Bot features logging features! Things that can be logged are `Member Join` `Member Leave` `Message Delete` `Message Edit`', inline=False)
    embed.add_field(name='All Commands/Features:', value='To see ALL my commands and features, click here -> https://bit.ly/33N0TTY', inline=False)
    embed.set_footer(text=f'If your experience any issues with me or want to change the curse word list, please join the support server! https://discord.gg/arMVCzHfuf | Thanks for inviting me to {guild.name}!')
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/-geI64yQFa9oSJQIQrMIsdcvU5F0R53h1L85MUhtjLc/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/830599839623675925/e3628ef58491a80705d745caec06d47d.webp?width=788&height=788")
    try:
      await guildowner.send(embed=embed)
    except:
      pass

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
  channel = bot.get_channel(848722304069926993)
  print('The bot is online!')
  print('Bot is connected to:')
  for server in bot.guilds:
    print(server.name, server.id)
  embed=discord.Embed(title="Bot Restart", color=0x00FFFF)
  embed.timestamp = datetime.datetime.utcnow()
  await channel.send(embed=embed)
  statuses = [f'{len(set(bot.get_all_members()))} members and {len(bot.guilds)} servers!', f'>help for help!', 'Ping me for server prefix!', 'Made my ColeTMK#1234']


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
  embed.add_field(name='Step-2', value='Take a Screenshot that includes the `Guild ID`, `Owner Name`, and the `Owner ID`', inline=False)
  embed.add_field(name='Step-2', value='Click **:envelope_with_arrow: Create ticket** below the Ticket Tool embed.', inline=False)
  embed.add_field(name='Step-3', value='Say you want to change the curse word list in your server AND send the screenshot you took. (this is to verify that you are the owner of the server that your trying to change the curse word list in!)', inline=False)
  embed.add_field(name='Step-4', value='Wait for assistance by an Admin!', inline=False)
  embed.set_image(url='https://i.stack.imgur.com/HCGv7.png')
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