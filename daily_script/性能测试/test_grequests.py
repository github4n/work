#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/7/13 11:10
# Author : lixingyun
# Description :
import grequests
import time

url = 'http://qa.new.huomaotv.com.cn/'
t1 = time.time()
total_rqs = 10

rs = [grequests.get(url) for i in range(total_rqs)]
rets = grequests.map(rs, size=None)

print(time.time() - t1)

# for ret in rets:
#     print(ret.text)
