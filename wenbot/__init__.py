import discord
import os

client = discord.Client()


@client.event
async def on_message(message):
    if 'wen' in str(message.content).lower() or 'digg' in str(message.content).lower():
        await message.channel.send('soon:tm:')

token = os.getenv('DISCORD')
client.run(token)
