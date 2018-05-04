#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-31 10:52:35
# @Author  : lixingyun

import requests
from huomao.common import Common
import time
import gevent
from gevent import monkey
monkey.patch_all()


i=0
j=0
url = 'http://lxy.new.huomaotv.com.cn/memberpay/get_qr_url?&money=20&gift_id=12&source=%E7%9B%B4%E6%92%AD%E9%97%B4&room=1'
for a in range(100):
    res = requests.get(url,cookies=Common.generate_cookies(1522))
    if 'qr_weixin' in res.json()['payUrl']['wx_url']:
        i+=1
    elif 'tonglian?pay_type=wx' in res.json()['payUrl']['wx_url']:
        j+=1
    else:
        print(res.json()['payUrl'])
print(i,j)
# qr_alipay tonglian?pay_type=alipay  qr_weixin tonglian?pay_type=wx