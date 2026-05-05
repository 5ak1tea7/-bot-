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
# Ping送信
    if message.content == 'いよりちゃーん？':
        await message.channel.send('うあ！わらわは生きておるぞ！')
#　性癖ガチャ
    elif message.content == 'せいへきがちゃ':
        import random
        seiheki = random.randint(1,3)
        if seiheki == 1:
            await message.channel.send('もしかして...わらわか？(1)')
        else:
            if seiheki == 2:
                await message.channel.send('あーっ...お主、ロリ好きじゃろ。(2)')
            else:
                if seiheki == 3:
                    await message.channel.send('お主...ふたなりが好きなのか？(3)')
                else:
                    await message.channel.send('おかしいのう...こんなの知らんわい...(Err:存在しない出目です。)')

# Flaskを起動
keep_alive()
# Botを起動
client.run(os.getenv('DISCORD_TOKEN'))
