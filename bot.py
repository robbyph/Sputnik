# This example requires the 'message_content' intent.

import discord # Import the discord module
from dotenv import load_dotenv # Import the dotenv module
import os # Import the os module
from discord.ext import commands
import json as jason
import datetime
import asyncio

intents = discord.Intents.default() # Create intents object
intents.message_content = True # Subscribe to the message_content intent

# client = discord.Client(intents=intents) # Create an instance of a Client, and pass it your intents
bot = commands.Bot(command_prefix='!', intents=intents) # Create an instance of a Bot, and pass it your intents

@bot.event 
async def on_ready(): # When the bot is ready
    print(f'We have logged in as {bot.user}')  # Print the bot's username

'''
@bot.event 
async def on_message(message): # When the bot sees a message in the server
    if str(bot.user.id) in message.content: # If the bot is mentioned
        if 'goat' in message.content.lower(): # If the message contains 'goat'
            await message.channel.send('Mao Zedong is the Goat!') # Send a message in the same channel
        if 'help' in message.content.lower(): # If the message contains 'help'
            await message.channel.send('In order to prompt the bot, be sure to mention it with the "@" mention symbol. \n\nUtilize the following functions:\n* If you wish to know who the GOAT is, include "goat" in your message, or use the command "!goat"') # Send a message in the same channel
    
    await bot.process_commands(message)

'''

async def check_for_birthday(self):
    await self.wait_until_ready()
    now = datetime.datetime.now()
    curmonth = now.month
    curday = now.day
    
    while not self.is_closed():
        with open('birthdays.json', 'r') as f:
            var = jason.load(f)
            for member in var:
                if member['month'] == curmonth:
                    if member['day'] == curday:
                        try:
                            await bot.get_user(member).send("Happy birthday!")
                        except:
                            pass
                        success = False
                        index = 0
                        while not success:
                            try:
                                await guild.channels[index].send(f"Happy birthday to <@{member}>!")
                            except discord.Forbidden:
                                                    index += 1
                            except AttributeError:
                                index += 1
                            except IndexError:
                                # if the server has no channels, doesn't let the bot talk, or all vc/categories
                                pass
                            else:
                                success = True
        await asyncio.sleep(86400) # task runs every day

@bot.command()
async def ping(ctx):
    '''Check if bot is working.'''
    await ctx.channel.send("Long live Josef Stalin! I am here!")

@bot.command()
async def setbirthday(ctx):
    '''Set a birthday.'''
    member = ctx.message.author.id
    await ctx.send("What is your birthday? Please use MM/DD format.")
    def check(user):
        print(str(user.author.name) == str(ctx.message.author) and str(user.channel.name) == str(ctx.message.channel))
        return str(user.author.name) == str(ctx.message.author) and str(user.channel.name) == str(ctx.message.channel)
    msg = await bot.wait_for('message', check=check)
    try: # Check if date is valid
        list = msg.split("/")
        if list[0] > 13 or list[0] < 1: # Check if month is valid
            print('1') # Debugging
            await ctx.send("Invalid date.") # Send error message     
            await ctx.send("Aborting...")
            return
        else:
            pass
            
        if list[0] in (1, 3, 5, 7, 8, 10, 12): # Check if day is valid for month (31 days)
            if list[1] > 31 or list[1] < 1:
                print('2')
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        elif list[0] in (4, 6, 9, 11): # Check if day is valid for month (30 days) 
            if list[1] > 30 or list[1] < 1: 
                print('3')
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        elif list[0] == 2:  # Check if day is valid for month (28 days)
            if list[1] > 29 or list[1] < 1:
                print('4')
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        else: # If month is invalid
            print('5')
            await ctx.send("Invalid date.")
            await ctx.send("Aborting...")
            return
    except: # If date is invalid
        print('6')
        await ctx.send("Invalid date.")
        await ctx.send("Aborting...")
        return
    
    list = msg.split("/")
    month = list[0]
    day = list[1]
    
    
    
    with open('./birthdays.json', 'r+') as f:
        var = jason.load(f)
        var[member] = {'month': month, 'day': day}
        jason.dump(var, f, indent=4)

if __name__ == "__main__":
    load_dotenv() # Load the .env file  
    bot.run(os.environ.get("TOKEN"))  # Run the bot with the token
    self.bg_task = self.loop.create_task(self.check_for_birthday())