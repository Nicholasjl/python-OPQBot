import json
import pdb
import re
import logging
import time
import httpx
import asyncio
from Config import *

async def send(ToQQ,Content,sendToType=1,atUser=0, sendMsgType='TextMsg',groupid=0):
    #好友私聊
    data={}
    data['sendToType'] = sendToType
    data['toUser']= ToQQ
    data['sendMsgType']=sendMsgType
    data['content']=Content
    data['groupid']=0
    data['atUser']=atUser
    
    async with httpx.AsyncClient() as client:
        await client.post(webApi+'/v1/LuaApiCaller?funcname=SendMsg&qq='+robotQQ,json=data)
    
    
async def zan(QQ):
    #QQ名片赞
    data={}
    data['UserID']=QQ
    with httpx.AsyncClient() as client:
        await client.post(webApi+'/v1/LuaApiCaller?funcname=QQZan&timeout=10&qq='+robotQQ,json=data)

async def sendPic(ToQQ, Content, imageUrl, atUser = 0, sendToType = 1):
    #发送图片信息
    data={}
    data['sendToType'] = sendToType
    data['toUser']= ToQQ
    data['sendMsgType']="PicMsg"
    data['content']=Content
    data['picBase64Buf']=''
    data["groupid"] = GroupId
    data['fileMd5']=''
    data['atUser']=atUser
    data['picUrl']=imageUrl
    
    with httpx.AsyncClient() as client:
        await client.post(webApi+'/v1/LuaApiCaller?funcname=SendMsg&timeout=10&qq='+robotQQ,json=data)

async def sendVoice(ToQQ, VoiceUrl, sendToType = 1,Grou69pId = 0):
    data={}
    data['sendToType'] = sendToType
    data['toUser']= ToQQ
    data['sendMsgType']="VoiceMsg"
    data['content'] = ""
    data["groupid"] = GroupId
    data['atUser']=0
    data['voiceBase64Buf']=''
    data['voiceUrl']=imageUrl
    
    with httpx.AsyncClient() as client:
        await client.post(webApi+'/v1/LuaApiCaller?funcname=SendMsg&timeout=10&qq='+robotQQ,json=data)


async def sendGroup(ToQQG, Content, atuser=0, sendMsgType='TextMsg', groupid=0):
    #发送群消息
    await send(ToQQG, Content, 2, atuser, sendMsgType, groupid)

async def sendGroupPic(ToQQG, Content, imageUrl, atUser = 0):
    return await sendPic(ToQQG, Content, imageUrl, atUser,sendToType = 2)

async def sendGroupVoice(ToQQG, VoiceUrl):
    return await sendVoice(ToQQG, VoiceUrl,sendToType = 2)

async def sendFromGroup(ToQQ,Content,groupid=0,atUser=0, sendMsgType='TextMsg'):
    return await send(ToQQ,Content,groupid,sendToType=3,atUser=0, sendMsgType='TextMsg')