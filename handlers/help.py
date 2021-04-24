from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("help") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""• Berikut Perintah Untuk Member Dalam Grup :
/play <Judul Lagu>  - Untuk Memutar Lagu Yang Anda Minta Melalui Youtube.
/dplay <Judul Lagu>  - Untuk Memutar Lagu Yang Anda Minta Melalui Deezer.
/playlist - Untuk Menampilkan Daftar Putar Lagu.
/song <Judul Lagu> - Untuk Mendownload Lagu di YouTube.
/video <Judul Lagu> - Untuk Mendownload Video di YouTube Secara Detail.
/deezer <Judul Lagu> - Untuk Mendownload Lagu Dari Deezer.
/saavn <Judul Lagu> - Untuk Mendownload Lagu Dari Website Saavn.
/search <Judul Lagu> - Untuk Mencari Video di YouTube Secara Detail.
• Berikut Perintah Untuk Admin Dalam Group :
/pause - Untuk Menjeda Pemutaran Lagu.
/resume - Untuk Melanjutkan Pemutaran Lagu Yang Telah Dipause.
/skip - Untuk Menloncati Pemutaran Lagu ke Lagu Berikutnya.
/end - Untuk Memberhentikan Pemutaran Lagu.
/userbotjoin - Untuk Mengundang Asisten Music ke Obrolan Suara.
/admincache - Untuk Memperbarui Admin List.""",
