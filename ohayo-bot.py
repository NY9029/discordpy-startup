#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "NzM3MzUwODQxOTI5MDM5OTY0.Xx8FfA.1JaStKX54_Crps1WzXncADdAhyI" #トークン
CHANNEL_ID = 737349336110858242 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '02:47':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('夜ちぇる～ん☆')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
