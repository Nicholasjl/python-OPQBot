#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from Control import on_command
from Message import send, sendGroup

@on_command("COC")
async def COC(message):
    
    try:
        num =int( message.Content.split()[-1])
    except:
        num = 1
    characteristics = ''
    for i in range(num):
        temp = ''
        sta = [Roll3d6(), Roll3d6(), Roll2d66(), Roll3d6(), Roll3d6(), Roll2d66(), Roll3d6(), Roll2d66(), Roll3d6()]
        sum = 0
        for nu in sta:
            sum += nu
        temp += "力量:" + str(sta[0]) + " 体质:" + str(sta[1]) + " 体型:" + str(sta[2]) + " 敏捷:" + str(sta[3])
        temp += " 容貌:" + str(sta[4]) + " 智力:" + str(sta[5]) + " 意志:" + str(sta[6]) + " 教育:" + str(sta[7])
        temp += " 幸运:" + str(sta[8]) + " 总计:" + str(sum)
        characteristics += temp + '\n'
    characteristics = characteristics[:-1]
    output = characteristics
    if(message.isGroup):
        sendGroup(message.FromQQG, output)
    else :
        send(message.FromQQ, output)
    
def Roll2d66():
    return (random.randint(1, 6) + random.randint(1, 6) + 6) * 5
def Roll3d6():
    return (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 5
def onPlug(bot):
    if not hasattr(bot, 'helpinfo'):
        bot.helpinfo = {}
    bot.helpinfo['coc7'] = [['个数'],bot.Momona_text['helpinfo_coc7']]
def onUnplug(bot):
    del bot.helpinfo['coc7']
