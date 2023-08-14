# This example requires the 'message_content' intent.

import discord # Import the discord module
from dotenv import load_dotenv # Import the dotenv module
import os # Import the os module

intents = discord.Intents.default() # Create intents object
intents.message_content = True # Subscribe to the message_content intent

client = discord.Client(intents=intents) # Create an instance of a Client, and pass it your intents


@client.event 
async def on_ready(): # When the bot is ready
    print(f'We have logged in as {client.user}')  # Print the bot's username


@client.event 
async def on_message(message): # When the bot sees a message in the server
    if str(client.user.id) in message.content: # If the bot is mentioned
        if 'goat' in message.content.lower(): # If the message contains 'goat'
            await message.channel.send('Mao Zedong is the Goat!') # Send a message in the same channel
        if 'help' in message.content.lower(): # If the message contains 'help'
            await message.channel.send('In order to prompt the bot, be sure to mention it with the "@" mention symbol. \n\nUtilize the following functions:\n* If you wish to know who the GOAT is, include "goat" in your message, or use the command "!goat"') # Send a message in the same channel

load_dotenv() # Load the .env file  
client.run(os.environ.get("TOKEN"))  # Run the bot with the token