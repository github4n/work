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

url = 'http://lxy.new.huomaotv.com.cn/notifypay/ainongScanNotify'
data = {
    'merOrderId': 2018012515132315223989298,  # 商户订单号
    'respCode': 1001,  # 交易状态
    'txnAmt': 1000,  # 交易金额
    'succTime': 0,  # 通知的发送时间
    'merId': 0  # 没有支付宝或者微信账号，只有我们的商户号
}

parse.urlencode(data)

an_key = '4d5WeuWgPszzAMhzDgpDYA5s4vKfmWZW'
sgin = ''
for key in sorted(data.keys()):
    sgin = sgin + key + '=' + str(data[key]) + '&'

sgin = sgin[:-1] + an_key
sgin = hashlib.md5(sgin.encode('utf-8')).digest()
sgin = (base64.b64encode(sgin)).decode('utf-8')

data['signature'] = sgin

res = requests.post(url, data=data)
print(res.text)
