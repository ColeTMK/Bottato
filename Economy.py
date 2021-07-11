import discord
from discord.ext import commands
import json
import datetime
import random

async def get_bank_data():
	    with open("bank.json", "r") as f:
		    users = json.load(f)
		    return users

async def update_bank(user, change=0, mode="wallet"):
      users = await get_bank_data()

      users[str(user.id)][mode] += change

      with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)

      bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
      return bal

async def open_account(user):
      users = await get_bank_data()

      if str(user.id) in users:
        return False

      else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
        
      with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)
        return True

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['bal'])
    async def balance(self, ctx, member: discord.Member = None):
      if not member:
        member = ctx.author
        await open_account(member)

      users = await get_bank_data()
      user = member

      wallet_amount = users[str(user.id)]["wallet"]
      bank_amount = users[str(user.id)]["bank"]

      embed = discord.Embed(title=f"{member.name}'s Balance", color=0x00FFFF)
      embed.add_field(name="**Wallet:**", value=f"{wallet_amount} Tato Coins", inline=False)
      embed.add_field(name="**Bank:**", value=f"{bank_amount} Tato Coins", inline=False)
      embed.set_thumbnail(url=user.avatar_url)
      embed.set_footer(
      text="Your total amount is saved across all servers that I'm in!")
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)


    @commands.cooldown(1, 3600, commands.BucketType.user)
    @commands.command()
    async def work(self, ctx):
      member = ctx.author
      await open_account(member)

      users = await get_bank_data()
      user = member
      money = random.randrange(10,50)
      jobtitles = ['Twitch Streamer', 'Youtuber', 'Content Creator', 'Maid', 'Cook', 'Teacher', 'Veteran', 'Receptionist', 'Librarian', 'Software Engineer', 'Teller', '911 Dispatcher', 'Financial Advisor', 'Nurse', 'Surgeon', 'Police Officer']
      job = random.choice(jobtitles)
      users[str(user.id)]["bank"] += money

      with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)

      embed = discord.Embed(title="Work (Earn 10-50 Tato Coins)",
	                      description=f"{ctx.author} went to work!",
	                      color=0x00FFFF)
      embed.add_field(name="**Your Job:**", value=f"{job}", inline=False)
      embed.add_field(name="**You Earned:**",
	                value=f"{money} Tato Coins",
	                inline=False)
      embed.set_thumbnail(url=user.avatar_url)
      embed.set_footer(text="Your total amount is saved across all servers that I'm in!")
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    async def withdraw(self, ctx, amount=None):
      await open_account(ctx.author)

      if amount == None:
        await ctx.send(f"{ctx.author.mention}, Please enter the amount that you want to withdraw!")
        return

      bal = await update_bank(ctx.author)
      users = await get_bank_data()
      bal = users[str(ctx.author.id)]["bank"]
      amount = int(amount)

      if amount < 1:
        await ctx.send(f"{ctx.author.mention}, Your withdraw amount needs to be larger than 0!")
        return
      elif amount > bal:
        await ctx.send(f"{ctx.author.mention}, You do not have enough Tato Coins in your bank to do this!")
        return
      elif amount <= bal:
        await update_bank(ctx.author, amount, "wallet")
        await update_bank(ctx.author,-1*amount, "bank")
        await ctx.send(f"{ctx.author.mention}, You just withdrew `{amount}` Tato Coins from your bank and into your wallet!")

    @commands.command()
    async def deposit(self, ctx, amount=None):
      await open_account(ctx.author)

      if amount == None:
        await ctx.send(f"{ctx.author.mention}, Please enter the amount that you want to withdraw!")
        return

      bal = await update_bank(ctx.author)
      users = await get_bank_data()
      bal = users[str(ctx.author.id)]["wallet"]
      amount = int(amount)

      if amount < 1:
        await ctx.send(f"{ctx.author.mention}, Your deposit amount needs to be larger than 0!")
        return
      if amount > bal:
        await ctx.send(f"{ctx.author.mention}, You do not have enough money in your wallet to do this!")
        return

      await update_bank(ctx.author,-1*amount,"wallet")
      await update_bank(ctx.author,amount,"bank")

      await ctx.send(f"{ctx.author.mention}, You just deposited `{amount}` Tato Coins into your bank!")

    @commands.command()
    async def give(self, ctx, member : discord.Member, amount=None):
      await open_account(ctx.author)
      await open_account(member)

      if amount is None:
        await ctx.send(f"{ctx.author.mention}, Please enter the amount that you want to give!")
        return

      users = await get_bank_data()
      bal = users[str(ctx.author.id)]["wallet"]

      amount = int(amount)

      if amount < 1:
        await ctx.send(f"{ctx.author.mention}, Your amount needs to be larger than 0!")
        return
      elif amount > bal:
        await ctx.send(f"{ctx.author.mention}, You do not have enough money in your wallet to do this!")
        return
      elif amount <= bal:
        await update_bank(ctx.author,-1*amount, "wallet")
        await update_bank(member, amount, "wallet")
        await ctx.send(f"{ctx.author.mention}, You just gave `{amount}` Tato Coins to {member.name}!")

    @commands.cooldown(1, 3600, commands.BucketType.user)
    @commands.command()
    async def beg(self, ctx):
      member = ctx.author
      await open_account(member)

      users = await get_bank_data()
      user = member
      money = random.randrange(0, 25)
      users[str(user.id)]["bank"] += money

      with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)

      embed = discord.Embed(title="Beg (Earn 0-25 Tato Coins)", description=f"{ctx.author} wants to beg! :sob:", color=0x00FFFF)
      embed.add_field(name="**You Earned:**", value=f"{money} Tato Coins", inline=False)
      embed.set_thumbnail(url=user.avatar_url)
      embed.set_footer(text="Your total amount is saved across all servers that I'm in!")
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addcoins(self, ctx, member : discord.Member, amount=None):
      await open_account(member)

      if amount is None:
        await ctx.send(f"{ctx.author.mention}, Please enter the amount that you want to add to the account!")
        return

      amount = int(amount)

      if amount < 1:
        await ctx.send(f"{ctx.author.mention}, Your amount needs to be larger than 0!")
        return
      await update_bank(member, amount, "wallet")
      await ctx.send(f"{ctx.author.mention}, You just added `{amount}` Tato Coins to {member.name}'s account!")

def setup(bot):
    bot.add_cog(Economy(bot))