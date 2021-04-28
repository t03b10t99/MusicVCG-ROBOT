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
/plays <Link Youtube / Direct> - Untuk Memutar lagu lewat link YouTube atau Lagu biasa (Sudah di Download)
/playlist - Untuk Menampilkan Daftar Putar Lagu.
/song <Judul Lagu> - Untuk Mendownload Lagu di YouTube.
/video atau /vsong <Judul Lagu> - Untuk Mendownload Video di YouTube Secara Detail.
/deezer <Judul Lagu> - Untuk Mendownload Lagu Dari Deezer.
/saavn <Judul Lagu> - Untuk Mendownload Lagu Dari Website Saavn.
/search <Judul Lagu> - Untuk Mencari Video di YouTube Secara Detail.
/current - Untuk Mengecek Antrian dan Juga Siapa yang Me-Request Lagu Tersebut.
/player - Untuk Memudahkan Anda Dalam Mengelola Robot.

• Berikut Adalah Perintah Untuk Admin Group :

/pause - Untuk Menjeda Pemutaran Lagu.
/resume - Untuk Melanjutkan Pemutaran Lagu Yang Telah Dipause.
/skip - Untuk Menloncati Pemutaran Lagu ke Lagu Berikutnya.
/end - Untuk Memberhentikan Pemutaran Lagu.
/joingroup - Untuk Mengundang Asisten Music ke Obrolan Suara.
/leavegroup - Untuk Menendang Asisten Music dari Obrolan Suara.
/adminreset - Untuk Memperbarui Admin List.
/admincache - Untuk Me-Refresh Cache Admin Pada Robot.""")
