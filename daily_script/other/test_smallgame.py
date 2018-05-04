#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/13 19:59
# Author : lixingyun
import sys
import requests
import json
from  urllib import parse

from huomao.common import Common

data = {'is_opened': 1,
        'open_time': 1524041486,
        'time': 1524041578,
        'cash': 50,
        'is_signed': 1,
        'data': {'1': {'signed': 2},
                 '2': {'signed': 2},
                 '3': {'signed': 2},
                 '4': {'signed': 2},
                 '5': {'signed': 2},
                 '6': {'signed': 2},
                 '7': {'signed': 2}} }
test_list = []
for i in range(1):
    # p = json.loads(Common.REDIS_INST.get('hm_new_Signs12:1522'))
    # print(p)
    Common.REDIS_INST.set('hm_new_Signs12:1522', json.dumps(data))
    # ret = requests.get('http://lxy.new.huomaotv.com.cn/Sign/done', cookies=Common.generate_cookies(1522))
    # test_list.append(ret.json()['data']['cash'])
# sum = 0
# for i in set(test_list):
#     sum = sum + i * test_list.count(i)
# print(sum / 10)
