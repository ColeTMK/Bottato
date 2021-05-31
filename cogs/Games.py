from discord.ext import commands
import random
import asyncio

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx):
      rpsGame = ['rock', 'paper', 'scissors']
      await ctx.send(f"Rock, paper, or scissors? Choose wisely...")
 
      def check(msg):
       return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame
 
      user_choice = (await self.bot.wait_for('message', check=check)).content
 
      comp_choice = random.choice(rpsGame)
      if user_choice == 'rock':
        if comp_choice == 'rock':
           await ctx.send(f'Well, that was weird. We tied.\nI choose: {comp_choice}')
        elif comp_choice == 'paper':
           await ctx.send(f'Nice try, but I won that time!!\nI choose: {comp_choice}')
        elif comp_choice == 'scissors':
           await ctx.send(f"Aw, you beat me. It won't happen again!\nI choose: {comp_choice}")
 
      if user_choice == 'Rock':
        if comp_choice == 'rock':
          await ctx.send(f'Well, that was weird. We tied.\nI choose: {comp_choice}')
        elif comp_choice == 'paper':
           await ctx.send(f'Nice try, but I won that time!!\nI choose: {comp_choice}')
        elif comp_choice == 'scissors':
           await ctx.send(f"Aw, you beat me. It won't happen again!\nI choose: {comp_choice}")
 
      if user_choice == 'paper':
        if comp_choice == 'rock':
          await ctx.send(f'Fair game!! Watch out next time though MUWAHAHAHA!\nI choose: {comp_choice}')
        elif comp_choice == 'paper':
           await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nI choose: {comp_choice}')
        elif comp_choice == 'scissors':
           await ctx.send(f"HAHAHHA you noob!\nI choose: {comp_choice}")
 
      if user_choice == 'Paper':
         if comp_choice == 'rock':
           await ctx.send(f'Fair game!! Watch out next time though MUWAHAHAHA!\nI choose: {comp_choice}')
         elif comp_choice == 'paper':
           await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nI choose: {comp_choice}')
         elif comp_choice == 'scissors':
           await ctx.send(f"Aw man, you actually managed to beat me.\nI choose: {comp_choice}")
 
      if user_choice == 'scissors':
        if comp_choice == 'rock':
           await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nI choose: {comp_choice}')
        elif comp_choice == 'paper':
           await ctx.send(f'Bruh. >: |\nI choose: {comp_choice}')
        elif comp_choice == 'scissors':
           await ctx.send(f"Oh well, we tied.\nI choose: {comp_choice}")
        
      if user_choice == 'Scissors':
        if comp_choice == 'rock':
           await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nI choose: {comp_choice}')
        elif comp_choice == 'paper':
           await ctx.send(f'Bruh. >: |\nI choose: {comp_choice}')
        elif comp_choice == 'scissors':
           await ctx.send(f"Oh well, we tied.\nI choose: {comp_choice}")
 
    @commands.command()
    async def numbergame(self, ctx):
      channel = ctx.channel
      await channel.send("Guess the number from 0-100 by writing the number in this channel!")
 
      number = random.randint(1,100)
 
      def check(m):
        return m.content.isdigit() and m.channel == channel and m.author == ctx.author
  
      while True:
        try:
            msg = await self.bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return await channel.send(f"{ctx.author.mention}, You are late to guess!")
        
        guess = int(msg.content)
        if guess == number:
            return await channel.send(f"Correct answer! {ctx.author.mention}")
        elif guess > number:
            await channel.send(f"{ctx.author.mention}, Your guess was too high!")
        elif guess < number:
            await channel.send(f"{ctx.author.mention}, Your guess was too low!")

def setup(bot):
  bot.add_cog(Games(bot))