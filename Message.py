import json
import pdb
import re
import logging
import time
import requests
from Config import *

def send(ToQQ,Content,sendToType=1,atUser=0, sendMsgType='TextMsg',groupid=0):
    #好友私聊
    tmp={}
    tmp['sendToType'] = sendToType
    tmp['toUser']= ToQQ
    tmp['sendMsgType']=sendMsgType
    tmp['content']=Content
    tmp['groupid']=0
    tmp['atUser']=atUser
    data = json.dumps(tmp)
    
    requests.post(webApi+'/v1/LuaApiCaller?funcname=SendMsg&qq='+robotQQ,data=data)
def zan(QQ):
    #QQ名片赞
    tmp={}
    tmp['UserID']=QQ
    data = json.dumps(tmp)
    requests.post(webApi+'/v1/LuaApiCaller?funcname=QQZan&timeout=10&qq='+robotQQ,data=data)
def sendPic(ToQQ, Content, imageUrl, atUser = 0, sendToType = 1):
    #发送图片信息
    tmp={}
    tmp['sendToType'] = sendToType
    tmp['toUser']= ToQQ
    tmp['sendMsgType']="PicMsg"
    tmp['content']=Content
    tmp['picBase64Buf']=''
    tmp["groupid"] = GroupId
    tmp['fileMd5']=''
    tmp['atUser']=atUser
    tmp['picUrl']=imageUrl
    data = json.dumps(tmp)
    #print(data)
    requests.post(webApi+'/v1/LuaApiCaller?funcname=SendMsg&timeout=10&qq='+robotQQ,data=data).text

def sendVoice(ToQQ, VoiceUrl, sendToType = 1,Grou69pId = 0):
    tmp={}
    tmp['sendToType'] = sendToType
    tmp['toUser']= ToQQ
    tmp['sendMsgType']="VoiceMsg"
    tmp['content'] = ""
    tmp["groupid"] = GroupId
    tmp['atUser']=0
    tmp['voiceBase64Buf']=''
    tmp['voiceUrl']=imageUrl
    data = json.dumps(tmp)
    requests.post(webApi+'/v1/LuaApiCaller?funcname=SendMsg&timeout=10&qq='+robotQQ,data=data).text


def sendGroup(ToQQG, Content, atuser=0, sendMsgType='TextMsg', groupid=0):
    #发送群消息
    send(ToQQG, Content, 2, atuser, sendMsgType, groupid)

def sendGroupPic(ToQQG, Content, imageUrl, atUser = 0):
    return sendPic(ToQQG, Content, imageUrl, atUser,sendToType = 2)

def sendGroupVoice(ToQQG, VoiceUrl):
    return sendVoice(ToQQG, VoiceUrl,sendToType = 2)

def sendFromGroup(ToQQ,Content,groupid=0,atUser=0, sendMsgType='TextMsg'):
    send(ToQQ,Content,groupid,sendToType=3,atUser=0, sendMsgType='TextMsg')