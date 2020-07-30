from pyrogram import Client, Filters, StopPropagation, ContinuePropagation, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto


@Client.on_callback_query()
async def darkmode(c, m):
    cb_data = m.data
    if cb_data.startswith("d||"):
        filename = cb_data.split("||")[-1].strip(".png")

        print(cb_data)
        light_button = InlineKeyboardMarkup([
            [InlineKeyboardButton("Light Mode ☀️", callback_data=f"l||{filename}")], ])

        darkimage = InputMediaPhoto(
            media=f"{filename}_dark.png",
        )
        await m.edit_message_media(media=darkimage, reply_markup=light_button)

    elif cb_data.startswith("l||"):
        filename = cb_data.split("||")[-1].strip("_dark.png")
        dark_button = InlineKeyboardMarkup([
            [InlineKeyboardButton("Darkmode 🌜", callback_data=f"d||{filename}")], ])

        darkimage = InputMediaPhoto(
            media=f"{filename}.png",
        )
        await m.edit_message_media(media=darkimage, reply_markup=dark_button)
    else:
        raise ContinuePropagation
