from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Follow the instructions: https://telegra.ph/file/f446eb266510b3b6ee3c3.mp4"
    await message.reply_text(helptxt)
