#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/7/12 16:47
# Author : lixingyun
# Description :

import gevent
from gevent import monkey, pool

monkey.patch_all()
import requests
import time
import hashlib
from huomao.common import REDIS_INST


def generate_cookies(uid):
    key = 'HUOMAOTV!@#$%^&*137SECRET'
    uid = str(uid)
    ts = str(int(time.time()))
    b = (uid + ts + key).encode('utf-8')
    token = str(hashlib.md5(b).hexdigest())
    cookies = {'user_e100fe70f5705b56db66da43c140237c': uid,
               'user_6b90717037ae096e2f345fde0c31e11b': token,
               'user_2c691ee7b8307f7fadc5c2c9349dbd7b': ts}
    return cookies


def test(uid):
    ret = requests.get('http://lxy.new.huomaotv.com.cn/ti8/receivePartake', cookies=generate_cookies(uid))
    print(ret.json(),uid)


t1 = time.time()
events = []
for i in range(5524, 5534):
    # REDIS_INST.hset('hm_ti8_task_barrage_roulette_time:2018-08-07', i, 5)
    events.append(gevent.spawn(test, i))

gevent.joinall(events)

print(time.time() - t1)
