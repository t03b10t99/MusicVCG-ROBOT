from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message

from helpers.filters import other_filters, other_filters2
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
async def online(_, message: Message):
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
async def reload(_, message: Message):
      await message.reply_text("""🚀Music VCG-ROBOT Sedang Online"""
      )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def helps(_, message: Message):
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
async def repo(_, message: Message):
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

# MusicVCG-ROBOT Ping and Info System


#START_TIME = datetime.utcnow()
#START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
#TIME_DURATION_UNITS = (
#    ('week', 60 * 60 * 24 * 7),
#    ('day', 60 * 60 * 24),
#    ('hour', 60 * 60),
#    ('min', 60),
#    ('sec', 1)
#)

#self_or_contact_filter = filters.create(
#    lambda
#    _,
#    __,
#    message:
#    (message.from_user and message.from_user.is_contact) or message.outgoing
#)


# https://gist.github.com/borgstrom/936ca741e885a1438c374824efb038b3
#async def _human_time_duration(seconds):
#    if seconds == 0:
#        return 'inf'
#    parts = []
#    for unit, div in TIME_DURATION_UNITS:
#        amount, seconds = divmod(int(seconds), div)
#       if amount > 0:
#            parts.append('{} {}{}'
#                         .format(amount, unit, "" if amount == 1 else "s"))
#    return ', '.join(parts)


#@Client.on_message(filters.text
#                   & self_or_contact_filter
#                   & ~filters.edited
#                   & ~filters.via_bot
#                   & filters.regex(pattern=r'^(playlist)$'))
#@authorized_users_only
#async def ping(_, message: Message):
#    """reply ping with pong and delete both messages"""
#    start = time()
#    m_reply = await message.reply_text("...")
#    delta_ping = time() - start
#    await m_reply.edit_text(
#        f"Ping : `{delta_ping * 1000:.3f} ms`"
#    )


#@Client.on_message(filters.text
#                   & self_or_contact_filter
#                   & ~filters.edited
#                   & ~filters.via_bot
#                   & filters.regex(pattern=r'^(uptime)$'))
#@authorized_users_only
#async def uptime(_, message: Message):
#    """/uptime Reply with readable uptime and ISO 8601 start time"""
#    current_time = datetime.utcnow()
#    uptime_sec = (current_time - START_TIME).total_seconds()
#    uptime = await _human_time_duration(int(uptime_sec))
#    await message.reply_text(
#        f"• Uptime: `{uptime}`\n"
#        f"• Start Time: `{START_TIME_ISO}`"
#    )
