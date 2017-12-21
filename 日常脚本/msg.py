#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/10/12 14:43
# Author : lixingyun

# 礼物不丢弃http://gate.huomaotv.com.cn:7172
# 普通达到速率后丢弃http://gate.huomaotv.com.cn:7173

# 全平台 /1/push/all
# 单房间 /1/push/room?rid=

import time
import requests
import json

url = 'http://gate.huomao.com:7172' + '/1/push/room?rid=' + '2'
data = {
    'time': '1507793926',
    'platform': '1',
    'code': '100001',
    'speak':
        {
            'badge': [],
            'fans':
                {
                    'is_live': '1',
                    'avatar': 'http://img.new.huomaotv.com.cn/upload/web/images/headimgs/cfb3d65969e7768350ab33b8ad3d36ae/20170823171927312_normal.jpeg',
                    'gname': '娱乐星秀',
                    'cid': '11',
                    'name': '粉丝',
                    'level': '16',
                    'gcmd': 'ylxx',
                    'rname': 'WWWWWWWWWWWWWWWW',
                    'rid': '11',
                    'zb_name': 'testroom11nc'
                },
            'channel':
                {
                    'name': '哈哈哈11',
                    'screenType': '2',
                    'platType': '1',
                    'rid': '1',
                    'cid': '2'
                },
            'barrage':
                {
                    'type': '100',
                    'msg': '测试',
                    'color': '',
                    'num': '0'
                },
            'extend':
                {
                    'is_guard': '0',
                    'is_fg': '0',
                    'is_zb': '0'
                },
            'user':
                {
                    'name': '哈哈哈%',
                    'level': '3',
                    'avatar': 'http://img.new.huomaotv.com.cn/upload/web/images/headimgs/cfb3d65969e7768350ab33b8ad3d36ae/20170823172044543_normal.jpeg',
                    'uid': '5257'
                }
        }
}
def test():
    res = requests.post(url, json=data,timeout=1)
    print(res.json())

t1 = time.time()
for i in range(1, 2):
    test()
t2 = time.time()
print(t2-t1)

