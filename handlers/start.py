from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""⚡ Selamat Datang Di Room Music Robot⚡
Music VCG-ROBOT adalah Project Yang Dirancang Untuk Memutar Sebuah Lagu, Secara Sesederhana Mungkin, Music Dalam Group anda melalui obrolan suara yang baru diperkenalkan oleh Telegram.
🤔 Bagaimana Cara Menggunakannya ? 
Silahkan Tekan Tombol » /help """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "My Instagram", url="https://www.instagram.com/si_axeell")
                  ],[
                    InlineKeyboardButton(
                        "FAQ Group", url="https://t.me/FSGOpenChat"
                    ),
                    InlineKeyboardButton(
                        "Sponsored", url="https://kenzo-404.github.io/Lynx-Userbot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⚡ Music VCG-ROBOT Sedang Online ⚡**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "FAQ Group", url="https://t.me/FSGOpenChat"
                    ),
                    InlineKeyboardButton(
                        "Sponsored", url="https://kenzo-404.github.io/Lynx-Userbot"
                    )
                ]
            ]
        )
   )


@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""🚀 **Music VCG-ROBOT Sedang Online**""")

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""• Berikut Adalah Perintah Untuk Member Group :

/play <Judul Lagu>  - Untuk Memutar Lagu Yang Anda Minta Melalui Youtube.
/dplay <Judul Lagu>  - Untuk Memutar Lagu Yang Anda Minta Melalui Deezer.
/playlist - Untuk Menampilkan Daftar Putar Lagu.
/song <Judul Lagu> - Untuk Mendownload Lagu di YouTube.
/video <Judul Lagu> - Untuk Mendownload Video di YouTube Secara Detail.
/deezer <Judul Lagu> - Untuk Mendownload Lagu Dari Deezer.
/saavn <Judul Lagu> - Untuk Mendownload Lagu Dari Website Saavn.
/search <Judul Lagu> - Untuk Mencari Video di YouTube Secara Detail.

• Berikut Adalah Perintah Untuk Admin Group :

/pause - Untuk Menjeda Pemutaran Lagu.
/resume - Untuk Melanjutkan Pemutaran Lagu Yang Telah Dipause.
/skip - Untuk Menloncati Pemutaran Lagu ke Lagu Berikutnya.
/end - Untuk Memberhentikan Pemutaran Lagu.
/userbotjoin - Untuk Mengundang Asisten Music ke Obrolan Suara.
/admincache - Untuk Memperbarui Admin List.""")
