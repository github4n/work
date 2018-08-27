#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/7/24 13:54
# Author : lixingyun
# Description :
import requests


data = {
    "code":"600004",
    "time":"1535357787",
    "platform":"1",
    "payCallbackNotify":{
        "msg_type":"payCallbackNotify",
        "msg_content":{
            "uid":"1522",
            "payType":"success",
            "type":"callbackAlipayService",
            "money":"520"
        }
    }
}


ret = requests.post('http://gate.huomaotv.com.cn:7172/1/push?uid=1522',json=data)

print(ret.text)

