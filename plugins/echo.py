from Control import on_command
from Message import send, sendGroup
@on_command("ECHO")
async def echo(message):
    
    if(message.isGroup):
        await sendGroup(message.FromQQG, message.Content)
    else :
        await send(message.FromQQ, message.Content)