import os
from datetime import datetime
from pyrogram.types import Message
from pytgcalls import GroupCall
from callsmusic.callsmusic import client as USER
from pyrogram.types import Chat, Message, User

class MusicPlayer(object):
    def __init__(self):
        self.group_call = GroupCall(None, path_to_log_file='')
        self.chat_id = None
        self.start_time = None
        self.playlist = []
        self.msg = {}


    async def update_start_time(self, reset=False):
        self.start_time = (
            None if reset
            else datetime.utcnow().replace(microsecond=0)
        )


    async def send_text(self, text):
        group_call = self.group_call
        client = group_call.client
        chat_id = self.chat_id
        message = await client.send_message(
            chat_id,
            text,
            disable_web_page_preview=True,
            disable_notification=True
        )
        return message


mcp = MusicPlayer()


# Pytgcalls Handlers

@mcp.group_call.on_network_status_changed
async def network_status_changed_handler(gc: GroupCall, is_connected: bool):
    if is_connected:
        mcp.chat_id = int("-100" + str(gc.full_chat.id))
        await mcp.send_text(f"My Assistant Joined The Voice Chat")
    else:
        await mcp.send_text(f"My Assistant Left The Voice Chat")
        mcp.chat_id = None


@mcp.group_call.on_playout_ended
async def playout_ended_handler(client: USER, message: Message):
    await mcp.skip_current_playing()
