import discord
import os
import time
import requests
from flask import Flask
from threading import Thread

# --- Flaskで簡単なWebページを作る ---
app = Flask('')

@app.route('/')

# 5分おきに起こす奴
def ping_self():
    while True:
        try:
            requests.get("https://iyorichiyan.onrender.com")
        except:
            pass
        time.sleep(300)

def start_ping():
    t = Thread(target=ping_self)
    t.start()

def home():
    return "Bot is alive!"

def run():
# Renderが指定するポート（PORT）を読み込む。なければ8080を使う。
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

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



#↓ここから弄ってOKゾーン↓
@client.event
async def on_message(message):
    if message.author == client.user: return
# Ping送信
    if message.content == 'いよりちゃーん？':
        await message.channel.send('うあ！わらわは生きておるぞ！')
#　性癖ガチャ
# 出目追加方法
#　1,randintの最大値を変更する
# 2,最後のelse(エラー出目)のawaitの行を範囲選択し、次の行にコピペする。
# ここにコピペ
# 3,一番デカい出目から、以下の構文をコピーする。(elseの後の:の上にawaitのaが来るように)
'''
if seiheki == N:
    await message.channel.send('')
else:
'''
# 4,オリジナルの出目を作る
# 5,エラー出目をelseの:の下にawaitの1文字目のaが来るように貼りなおす。
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
#↑ここまで弄ってOKゾーン↑



# Flask（Webサーバー）を別スレッドで起動
if __name__ == "__main__":
    keep_alive()
    
    # トークンがない場合にエラーを出すようにする
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        print("ERROR: DISCORD_TOKEN is not set in Environment Variables!")
    else:
        client.run(token)
