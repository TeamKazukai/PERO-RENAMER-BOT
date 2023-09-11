import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Dxbot
from config import Config



Bot = Client(

           "Bixby",

           bot_token=Config.BOT_TOKEN,

           api_id=Config.API_ID,

           api_hash=Config.API_HASH,

           plugins=dict(root='plugins'))
           

if Config.PYROGRAM_SESSION:
    apps = [Dxbot,Bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    Bot.run()
