#coding=utf-8
import socketio
import json
import requests
import pdb
import re
import logging
import time
import socket
from Message import *
from Control import plugin_list
import plugins 
from Config import *
import asyncio
loop = asyncio.get_event_loop()
sio = socketio.AsyncClient()
#log文件处理
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=40)
class GMess:
    #QQ群消息类型
    def __init__(self,message):
        #print(message1)
        tmp1 = message
        tmp2 = tmp1['CurrentPacket']
        message1 = tmp2['Data']
        self.FromQQG = message1['FromGroupId'] #来源QQ群
        self.QQGName = message1['FromGroupName'] #来源QQ群昵称
        self.FromQQ = message1['FromUserId'] #来源QQ
        self.FromQQName = message1['FromNickName'] #来源QQ名称
        self.Content = message1['Content'] #消息内容
        self.isGroup = True
class Mess:
    def __init__(self,message):
        tmp1 = message
        tmp2 = tmp1['CurrentPacket']
        message1 = tmp2['Data']
        self.isGroup = False
        self.FromQQ = message1['FromUin']
        self.ToQQ = message1['ToUin']
        self.Content = message1['Content']
# standard Python

# SocketIO Client
#sio = socketio.AsyncClient(logger=True, engineio_logger=True)


# ----------------------------------------------------- 
# Socketio
# ----------------------------------------------------- 
async def beat():
    while(1):
        await sio.emit('GetWebConn',robotQQ)
        await sio.sleep(60)

@sio.event
async def connect():
    logging.info('connected to server')
    await sio.emit('GetWebConn',robotQQ)#取得当前已经登录的QQ链接
    await beat() #心跳包，保持对服务器的连接

@sio.on('OnGroupMsgs')
async def OnGroupMsgs(message):
    ''' 监听群组消息'''
    
    message = GMess(message)
    if weakCommand != []:
        if message.Content[0] in weakCommand:
            message.Content = message.Content[1:]
        else:
            return
    '''
    message.FromQQ 消息来源
    message.QQGName 来源QQ群昵称
    message.FromQQG 来源QQ群
    message.FromNickName 来源QQ昵称
    message.Content 消息内容
    message.ToQQ 自己的QQ
    '''
    
    try:
        await plugin_list[message.Content.split()[0].upper()](message)
    except:
        await plugin_list["else"](message)

@sio.on('OnFriendMsgs')
async def OnFriendMsgs(message):
    ''' 监听好友消息 '''
    
    message = Mess(message)
    if weakCommand != []:
        if message.Content[0] in weakCommand:
            message.Content = message.Content[1:]
        else:
            return
    try:
        await plugin_list[message.Content.split()[0].upper()](message)
    except:
        await plugin_list["else"](message)
@sio.on('OnEvents')
async def OnEvents(message):
    ''' 监听相关事件'''
    pass 
# ----------------------------------------------------- 
async def main():
    try:
        
        await sio.connect(webApi,transports=['websocket'])
        #pdb.set_trace() #这是断点
        await sio.wait()
    except KeyboardInterrupt as e:
        await sio.disconnect()
        logging.info(e)


if __name__ == '__main__':
   loop.run_until_complete(main())
