from Control import on_command
from Message import send, sendGroup
@on_command("ECHO")
def echo(message):
    if(message.isGroup):
        sendGroup(message.FromQQG, message.Content)
    else :
        send(message.FromQQ, message.Content)