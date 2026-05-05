import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'ping':
        await message.channel.send('pong!')

# Railwayの設定画面で入力する「TOKEN」を読み込む
client.run(os.getenv('MTUwMTE4NTYyMjg4MTM0MTU2Mg.GEDsrz.zhk2pZd69P_-o6aorBSCqEhIIAMxRDrmB6l890'))