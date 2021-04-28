from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,
                                  f"Hai Selamat Datang di Room Chat Music Assistant Robot, Saya adalah Layanan Asisten Musik dari @MusicVCGRobot.\
                                  \n\n• Silahkan Tekan /start Ke @MusicVCGRobot\
                                  \n Dan Jangan Lupa Membaca Rules Dibawah Ini.\
                                  \n\n 📑 **Rules :**\
                                  \n • Supaya Tidak ❌Error, Jangan Melakukan Spam Request Lagu Terlalu Banyak.\
                                  \n\n **Cara Mengundang :** Tambahkan @MusicVCGRobot Terlebih Dahulu, Lalu Jangan Lupa Jadikan Admin. Jika Telah Menjadi Admin, Undang Saya Dengan Cara : \n 1. Ketik /joingroup Lalu Enter. \n 2. Atau Tambahkan @AssistantMusicVCGRobot Secara Manual.\
                                  \n\n **Cara Penggunaan :** Ketik /help di @MusicVCGRobot Lalu Enter, Atau Anda Juga Bisa Ke @InfoMusicRobot.\
                                  \n\n Berikut adalah Pembahasan Mengenai MusicVCGRobot, Untuk Mendapatkan Info Terupdate Silahkan Kunjungi @InfoMusicRobot,\n😊 Sekian dan Terimakasih 🙏\
                                  \n\n ⛑ **Contributors :** [Axel](t.me/SyndicateTwenty4) & [Dharma](t.me/Devilsangry)\
                                  \n **Instagram :** [Axel](instagram.com/si_axeell) & [Dharma](instagram.com/kadekx._)\
                                  \n **Sponsored :** [⚡Lynx-Userbot⚡](https://kenzo-404.github.io/Lynx-Userbot)\
                                  \n **Powered By :** [Federation Super Group](https://t.me/FederationSuperGroup)\n\n")
  return
