#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/6/14 14:14
# Author : lixingyun
# Description :
import requests
from huomao.common import Common
import gevent
from gevent import monkey
monkey.patch_all()




url = 'http://lxy.new.huomaotv.com.cn/eventBox/getEventTreasure?treasure_id=315&cid=2'

def test(uid):
    ret = requests.get(url, cookies=Common.generate_cookies(uid)).json()
    print(ret,uid)



events = []
uids = range(5253,5263)

for uid in uids:
    event = gevent.spawn(test, uid)
    events.append(event)
gevent.joinall(events)

