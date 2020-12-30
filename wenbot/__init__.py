import discord

client = discord.Client()


@client.event
async def on_message(message):
    if 'wen' in str(message.content).lower() or 'digg' in str(message.content).lower():
        await message.channel.send('soon:tm:')


client.run('NzkzODYxODMxMTk4MjQ0ODg1.X-ybcQ.X534wTsDpiGjBCJjMuj_Dto1g4w')
