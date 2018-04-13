#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/2/1 17:12
# Author : lixingyun
from common.common import Common
import requests
import random

for i in range(1):
    try:
        cid = 14#random.randint(20, 100)
        t_count = random.randint(100, 200)
        uid = random.randint(7000,7100)
        res = requests.get('http://lxy.new.huomaotv.com.cn/chatnew/sendGift',params=dict(cid=cid,gift=8,t_count=t_count),cookies=Common.generate_cookies(uid))
        print(res.json())
    except:
        print(666)