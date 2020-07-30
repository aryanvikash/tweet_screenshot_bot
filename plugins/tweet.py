from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
from twitter_ss_func import twitter

import time


@Client.on_message(Filters.regex(r"^https:\/\/(mobile.)?twitter.com\/(.+)\/status\/"), group=-2)
async def start(client, m):
    print("ss plugin")
    url = m.text.strip()
    random_fname = str(m.from_user.id)+str(time.strftime("%Y%m%d-%H%M%S"))
    tw = twitter(url, random_fname)
    try:
        filename = tw.light_ss()
        tw.dark_ss()
    finally:
        tw.close()

    dark_button = InlineKeyboardMarkup([
        [InlineKeyboardButton("Darkmode 🌜", callback_data=f"d||{filename}")],


    ])
    print("file", filename)
    try:
        await m.reply_photo(filename, reply_markup=dark_button)
    except Exception as e :
        await m.reply_text("Error while uploading")
        print(e)

    raise StopPropagation
