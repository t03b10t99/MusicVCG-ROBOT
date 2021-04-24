from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,f"Haii, Saya adalah **Layanan Asisten Musik.\n -Silahkan Ketik /Start Ke @MusicVCGRobot**\n\n 📑 **Rules :**\n   - Supaya Tidak Error, Jangan Melakukan Spam Request Lagu. \n\n 👉 **KIRIM LINK UNDANGAN GRUP ATAU NAMA PENGGUNA JIKA ASSISTANT MUSIC TIDAK DAPAT BERGABUNG DENGAN GRUP ANDA.**\n\n ⛑ **Created by :** @SyndicateTwenty4 - **Sponsored :** [⚡Lynx-Userbot⚡](https://kenzo-404.github.io/Lynx-Userbot)\n\n")
  return
