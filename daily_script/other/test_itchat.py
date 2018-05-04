#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/1/30 11:09
# Author : lixingyun
# from huomao.huomao import Common
#
#
# keys = Common.REDIS_INST.keys('*hm_EVERYDAYRECHARGE*')
#
# for key in keys:
#     Common.REDIS_INST.delete(key)
import itchat
import time
import requests

# itchat.auto_login(hotReload=True)


# #想给谁发信息，先查找到这个朋友
# users = itchat.get_friends()
# print(type(users))
# for user in users:
#     # print(user)
#     print(user['NickName'],user['UserName'])
# exit()
# toUserName_qq = itchat.search_friends(nickName='圈圈')[0]['UserName']
# ret3 = itchat.send('现在的时间是:' + time.asctime(time.localtime(time.time())), toUserName=toUserName_qq)  #
# print(ret3)


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : '4b81a06558f04e2f941f932d7a071f4f',
        'info'   : msg,
        # 'userid' : 'test1111111sss111',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply


itchat.auto_login(hotReload=False)
itchat.run()
