#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-31 10:52:35
# @Author  : lixingyun

import requests
from common import generate_cookies
import time
import gevent
from gevent import monkey
monkey.patch_all()


url = 'http://lxy.new.huomaotv.com.cn/csgo/lottery'

r_list = []


def f(uid):
    r = requests.get(url, cookies=generate_cookies(uid))
    try:
        r_list.append(r.json()['data']['goods_name'] + str(r.json()['data']['unit']))
    except Exception as e:
        print(e)
        pass


t1 = time.time()
events = [gevent.spawn(f, i) for i in range(3060, 3560)]
gevent.joinall(events)
print('时间消耗{}'.format(time.time() - t1))
print(r_list)
r_set = set(r_list)
len_r = len(r_list)
for i in r_set:
    print('{}概率：{}'.format(i, r_list.count(i) / len_r))
