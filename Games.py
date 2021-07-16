import discord
from discord.ext import commands
import random
import asyncio
import datetime
import akinator as ak

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

    @commands.command()
    async def akinator(self, ctx):
        intro=discord.Embed(title="Akinator",description=f"Hello {ctx.author.mention}! Welcome to Akinator!\n\n**Game starting! Please wait...**",color=0xFFFF00)
        intro.set_thumbnail(url="https://en.akinator.com/bundles/elokencesite/images/akinator.png?v93")
        intro.timestamp = datetime.datetime.utcnow()
        intro.set_footer(text="Think about a real or fictional character. It can be from a TV show, movie, book, what not! I will try to guess who it is!")
        bye=discord.Embed(title="Akinator",description="Bye, "+ctx.author.mention,color=0xFFFF00)
        bye.set_footer(text="Akinator out!")
        bye.timestamp = datetime.datetime.utcnow()
        bye.set_thumbnail(url="https://i.pinimg.com/originals/28/fc/0b/28fc0b88d8ded3bb8f89cb23b3e9aa7b.png")
        intromsg = await ctx.send(embed=intro)
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y","n","p","b","yes","no","probably","idk","back"]
        try:
            aki = ak.Akinator()
            q = aki.start_game()
            while aki.progression <= 80:
                question=discord.Embed(title=f"Question for {ctx.author}",description=q,color=0xFFFF00)
                ques=["https://i.imgflip.com/uojn8.jpg","https://ih1.redbubble.net/image.297680471.0027/flat,750x1000,075,f.u1.jpg"]
                question.set_thumbnail(url=ques[random.randint(0,1)])
                question.timestamp = datetime.datetime.utcnow()
                question.set_footer(text="Your answer: (y/n/p/idk/b)")
                question_sent=await ctx.send(embed=question)
                try:
                    msg = await self.bot.wait_for("message", check=check , timeout=30)
                except asyncio.TimeoutError:
                    await question_sent.delete()
                    await ctx.send(f"{ctx.author.mention}, you took too long to respond!")
                    return
                await question_sent.delete()
                await msg.delete()
                if msg.content.lower() in ["b","back"]:
                    try:
                        q=aki.back()
                    except ak.CantGoBackAnyFurther:
                        await ctx.send(f"{ctx.author.mention}, I can't go back any futhur!")
                        continue
                else:
                    try:
                        q = aki.answer(msg.content.lower())
                    except ak.InvalidAnswerError as e:
                        await ctx.send(e)
                        continue
            aki.win()
            answer=discord.Embed(title=aki.first_guess['name'], description=aki.first_guess['description'],color=0xFFFF00)
            answer.set_thumbnail(url=aki.first_guess['absolute_picture_path'])
            answer.set_image(url=aki.first_guess['absolute_picture_path'])
            answer.set_footer(text="Was I correct? (y/n)")
            answer.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=answer)
            try:
                correct = await self.bot.wait_for("message", check=check ,timeout=30)
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention}, you took too long to respond!")
                return
            if correct.content.lower() == "y":
                yes=discord.Embed(title="YAYYY!",description='Epik poggers moment XD', color=0xFFFF00)
                yes.set_thumbnail(url="https://i.pinimg.com/originals/ae/aa/d7/aeaad720bd3c42b095c9a6788ac2df9a.png")
                yes.set_footer(text=f'Thanks for playing {ctx.author.name}!')
                yes.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=yes)
                await intromsg.delete()
            else:
                no=discord.Embed(title="Oh Noo!", description='I tried to think as hard as I could :sob:', color=0xFFFF00)
                no.set_thumbnail(url="https://i.pinimg.com/originals/0a/8c/12/0a8c1218eeaadf5cfe90140e32558e64.png")
                no.set_footer(text=f'Thanks for playing {ctx.author.name}!')
                no.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=no)
                await intromsg.delete()
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    async def eightball(self, ctx, *, question):
      responses = [
        'Certainly!',
        'Not likely.',
        '100%',
        'Thats too personal.',
        'Very positive.',
        'Impossible!',
        '50/50 chance.',
        'Ask you mom.',
        'I dont really know.',
        'Maybe.',
        'Yes.',
        'No.',
        'Im sure!',
        'Im really not sure.']
      answer = random.choice(responses)
      embed=discord.Embed(title='8-Ball', color=0xFFFF00)
      embed.add_field(name='Question:', value=question, inline=False)
      embed.add_field(name='Answer:', value=answer, inline=False)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Games(bot))