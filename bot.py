from pyrogram import Client, filters
import requests
import random
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  
from myrogram import notJoin , forceMe

TOKEN = os.environ.get("6513400749:AAFfrC2JmGltLcQJGfO41GKEgu2RlRWHoxs", "")

API_ID = int(os.environ.get("25105744", ))

API_HASH = os.environ.get("0ca4154111e7b0f99e9929710faa3f25", "")

app = Client("anime-gen", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

regex_photo = ["waifu","neko"]
pht = random.choice(regex_photo)
url = f"https://api.waifu.pics/sfw/{pht}"
      
@app.on_callback_query()
async def handle_query(client, query):
    if query.data == "again":
     response = requests.get(url).json()
     up = response['url']
     if up:
      but = [[InlineKeyboardButton("Generate again ✨", callback_data=f'again')],
             [InlineKeyboardButton("Source Code 🌺", url=f'https://github.com/prime-hritu/Anime-Generator-Bot')]]
      markup = InlineKeyboardMarkup(but)
      await query.message.reply_photo(up,caption="**@AIanimeGenBot**",reply_markup=markup)
     else:
      await query.message.reply("Request failed try /again")
    		
@app.on_message(filters.private)
def get_waifu(client, message):
    res = forceMe(message.chat.id)
    if res == "no":
      return notJoin(client,message)
    response = requests.get(url).json()
    up = response['url']
    if up:
        button = [[InlineKeyboardButton("Generate again ✨", callback_data=f'again')],
                  [InlineKeyboardButton("Source Code 🌺", url=f'https://github.com/prime-hritu/Anime-Generator-Bot')]]
        markup = InlineKeyboardMarkup(button)
        message.reply_photo(up,caption="**@AIanimeGenBot**",reply_markup=markup)
    else:
        message.reply("Request failed try /again")
        
app.run()
