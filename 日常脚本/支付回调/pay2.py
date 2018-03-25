#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/1/25 11:48
# Author : lixingyun
# 回调接口测试
# 高汇通 爱农  支付宝 微信 苹果 京东 快钱
import requests
import hashlib
import base64
from  urllib import parse

url = 'http://lxy.new.huomaotv.com.cn/NotifyPayment/callbackNotify/tmall'
# Shop=10001&PorductId=catCoin&Account=18101920938&OrderNo=20180320_1266602633&Amount=50&Signature=eb1eb83930e8e2ac0e37f0082f8a0b75

data = {
    'Shop':'10001',
    'PorductId':'catCoin',
    'Account':'15800091111',
    'OrderNo':'20180320_126610424',
    'Amount':'20000',
    # 'Signature':'eb1eb83930e8e2ac0e37f0082f8a0b75'
}

salt = '^&*%(*GIUGJ'
sgin = data['Account'] + data['Amount']+data['PorductId']+data['Shop']+data['OrderNo']+salt
m = hashlib.md5()
m.update(sgin.encode('utf-8'))
sgin = m.hexdigest()
data['Signature'] = sgin
print(data)
res = requests.post(url, data=data)
print(res.json())
