import os
import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'memer' in message.content:
        await message.channel.send('shut the fuck up\nplease shut the fuck up')

client.run(os.environ['DISCORD_TOKEN'])