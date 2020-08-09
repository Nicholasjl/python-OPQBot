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

sio = socketio.Client()
#log文件处理
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=0)
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
def beat():
    while(1):
        sio.emit('GetWebConn',robotQQ)
        time.sleep(60)

@sio.event
def connect():
    logging.info('connected to server')
    sio.emit('GetWebConn',robotQQ)#取得当前已经登录的QQ链接
    beat() #心跳包，保持对服务器的连接

@sio.on('OnGroupMsgs')
def OnGroupMsgs(message):
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
    message.ToQQ 
    '''
    
    try:
        plugin_list[message.Content.split()[0].upper()](message)
    except:
        plugin_list["else"](message)

@sio.on('OnFriendMsgs')
def OnFriendMsgs(message):
    ''' 监听好友消息 '''
    
    message = Mess(message)
    if weakCommand != []:
        if message.Content[0] in weakCommand:
            message.Content = message.Content[1:]
        else:
            return
    try:
        plugin_list[message.Content.split()[0].upper()](message)
    except:
        plugin_list["else"](message)
@sio.on('OnEvents')
def OnEvents(message):
    ''' 监听相关事件'''
    pass 
# ----------------------------------------------------- 
def main():
    try:
        sio.connect(webApi,transports=['websocket'])
        #pdb.set_trace() #这是断点
        sio.wait()
    except BaseException as e:
        logging.info(e)


if __name__ == '__main__':
   main()
   logging.info("exit")
