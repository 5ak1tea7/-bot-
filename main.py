import discord
import os
from flask import Flask
from threading import Thread

# --- Flaskで簡単なWebページを作る ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ------------------------------

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user: return
    if message.content == 'いよりちゃーん？':
        await message.channel.send('うあ！わらわは生きておるぞ！')

# Flaskを起動
keep_alive()
# Botを起動
client.run(os.getenv('DISCORD_TOKEN'))
