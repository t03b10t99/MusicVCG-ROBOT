from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["joinvc"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Tambahkan Saya Sebagai Admin Terlebih Dahulu.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "MusicVCG-ROBOT"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Assistant Music Sudah Berada di Obrolan.</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>Mohon Maaf, User {user.first_name} Tidak Bergabung Dalam Group. Pastikan User Tidak Di Banned Dalam Group Ini."
            "\n\nAtau Tambahkan Robot Dan Assistant Music Secara Manual kedalan Group Anda dan Coba Lagi.</b>",
        )
        return
    await message.reply_text(
            "<b>Assistant Music Baru Saja Bergabung Dengan Obrolan.</b>",
        )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"**@MusicVCGRobot Tidak Dapat Keluar Dari Grup, Mungkin Karena Floodwaits.**"
            "\n\n**Mohon Kick Secara Manual.**",
        )
        return
