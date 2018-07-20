#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/7 15:55
# Author : lixingyun
# Description :

import gevent
from gevent import monkey
monkey.patch_all()
import requests
from huomao.common import Common


x = Common.hash_table(18256430)
print(x)
exit()
def test():
    ret = requests.post('http://qa.new.huomaotv.com.cn/active_file/WorldCup/KickTheBall',data=dict(cid=2,type=1),cookies=Common.generate_cookies(1522))
    print(ret.json())

events = []
for i in range(0, 200):
    events.append(gevent.spawn(test,))
gevent.joinall(events)