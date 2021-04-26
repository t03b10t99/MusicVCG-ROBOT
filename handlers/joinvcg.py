import asyncio
import os
from datetime import datetime, timedelt
from pyrogram import Client, filter
from callsmusic.callsmusic import client as USER
from helpers.filters import command, other_filters, other_filters2, self_or_contact_filter
from helpers.vc import mcp


async def current_vc_filter(client: USER, message: Message):
    group_call = mcp.group_call
    if not group_call.is_connected:
        return False
    chat_id = int("-100" + str(group_call.full_chat.id))
    if message.chat.id == chat_id:
        return True
    return False


@Client.on_message(other_filters & self_or_contact_filter & filters.regex & filters.command(["joinvcg"]))
@authorized_users_only
@errors
async def join_group_call(client: USER, message: Message):
    group_call = mcp.group_call
    group_call.client = client
    if group_call.is_connected:
        await message.reply_text(f"Successfully Joined a Voice Chat.")
        return
    await group_call.start(message.chat.id)
    await message.delete()
