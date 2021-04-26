from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,
                                  f"Haii, Saya adalah **Layanan Asisten Musik.\
                                  \n-Silahkan Tekan /Start Ke @MusicVCGRobot**\
                                  \n 📑 **Rules :**\
                                  \n- Supaya Tidak ❌ Error ❌, Jangan Melakukan Spam Request Lagu.\
                                  \n 👉 **KIRIM LINK UNDANGAN GROUP ATAU NAMA PENGGUNA JIKA ASSISTANT MUSIC TIDAK DAPAT BERGABUNG DENGAN GRUP ANDA.**\
                                  \n ⛑ **Contributors :** @SyndicateTwenty4 & @Devilsangry - **Sponsored :** [⚡Lynx-Userbot⚡](https://kenzo-404.github.io/Lynx-Userbot)\
                                  \n 🚀 Instagram : [Axel](instagram.com/si_axeell) & [Dharma](instagram.com/kadekx._)\n\n")
  return
