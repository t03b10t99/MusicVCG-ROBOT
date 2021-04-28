from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("help") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
              reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Info Help •", url="https://t.me/InfoMusicRobot/10")
                ]
            ]
        )
   )
