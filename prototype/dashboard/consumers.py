import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group('streams').add(message.reply_channel)

def ws_disconnect(message):
    Group('streams').discard(message.reply_channel)

