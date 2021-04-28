from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""⚡ Selamat Datang Di Room Music Robot⚡

Music VCG-ROBOT adalah Project Yang Dirancang Untuk Memutar Sebuah Lagu, Secara Sesederhana Mungkin. Robot ini Dapat Memutar Music Dalam Group Anda Melalui Obrolan Suara Yang Baru Diperkenalkan Oleh Telegram.
Untuk Informasi Terupdate Silahkan Kunjungi @InfoUpdateMusicVCGRobot
Jika Disini Kurang Penjelasan, Silahkan Chat @AssistantMusicVCGRobot

🤔 Bagaimana Cara Menggunakannya ?

Silahkan Tekan Tombol » /help """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "ᴀxᴇʟ ᴀ.ʟ", url="instagram.com/si_axeell")
                  ],
                [
                    InlineKeyboardButton(
                        "ᴅʜᴀʀᴍᴀ", url="instgram.com/kadekx._")
                  ],[
                    InlineKeyboardButton(
                        "❓FAQ Group", url="https://t.me/FSGOpenChat"
                    ),
                    InlineKeyboardButton(
                        "✨Sponsored", url="https://kenzo-404.github.io/Lynx-Userbot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("online") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""⚡ MusicVCG-ROBOT Online ⚡""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❓FAQ Group", url="https://t.me/FSGOpenChat"
                    ),
                    InlineKeyboardButton(
                        "✨Sponsored", url="https://kenzo-404.github.io/Lynx-Userbot"
                    )
                ]
            ]
        )
   )


@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""🚀Music VCG-ROBOT Sedang Online"""
   )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""Menu Bantuan\nDari **MusicVCGRobot**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• BANTUAN •", url="https://t.me/InfoMusicRobot/10")
                ]
            ]
        )
    )


@Client.on_message(filters.command("repo") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""Repository :""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤖 MusicVCGRobot ", url="https://github.com/KENZO-404/MusicVCG-ROBOT")
                ]
            ]
        )
    )

