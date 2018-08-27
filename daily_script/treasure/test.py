#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/6/14 14:14
# Author : lixingyun
# Description :
import gevent
from gevent import monkey

monkey.patch_all()
import requests
from huomao.common import Common
import time
import random
import threading

uid = 18398171#357855
ip_pool = ['219.141.153.41:80']


def test(cid):
    while 1:
        try:
            ret = requests.get(f'http://www.huomao.com/eventBox/isHaveEventTreasure?cid={cid}',
                               cookies=Common.generate_cookies(uid),
                               proxies={'http': random.choice(ip_pool)}).json()
            print(ret)
            if ret['status']:
                print(ret)
                treasure_id = ret['data']['id']
                open_time = int(ret['data']['open_time'])
                time.sleep(open_time)
                for i in range(10):
                    ret = requests.get(f'http://www.huomao.com/EventBox/getEventTreasure?treasure_id={treasure_id}&cid={cid}',
                                       cookies=Common.generate_cookies(uid),
                                       proxies={'http': random.choice(ip_pool)})
                    print(ret.json())
                time.sleep(0.2)
            time.sleep(100)
            time.sleep(random.randint(20, 40))
        except:
            print('error')


events = []
cids = [3039, 10661, 3041, 3042, 888]

for cid in cids:
    event = gevent.spawn(test, cid)
    events.append(event)
gevent.joinall(events)
