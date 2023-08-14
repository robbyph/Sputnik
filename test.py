# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message): # When the bot sees a message in the server
    if str(client.user.id) in message.content: # If the bot is mentioned
        if 'goat' in message.content: # If the message contains 'goat'
            await message.channel.send('Mao Zedong is the Goat!') # Send a message in the same channel

client.run('MTE0MDA2MjIzMTI4MzkwMDQ4Nw.GHm7ho.BfgWwqJgXVdZgFtMVla665S435yWE7Fm77YXaw')
