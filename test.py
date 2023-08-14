# This example requires the 'message_content' intent.

import discord # Import the discord module

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

client.run('MTE0MDA2MjIzMTI4MzkwMDQ4Nw.GHm7ho.BfgWwqJgXVdZgFtMVla665S435yWE7Fm77YXaw')  # Run the bot with the token