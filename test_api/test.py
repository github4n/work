#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/31 19:25
# Author : lixingyun
# Description :
from huomao.common import Common
from time import time
import requests

# STREAM_REFRESH_API_EXPIRE = 10


url = 'http://test1.api.huomao.com/channels/channelDetail'
# url = 'http://lxyapi.new.huomaotv.com.cn/channels/channelDetail'
data = dict(
    refer='android',
    cid=9418,
    expires_time=1527757747,
    post_data=1,
    time=1528181184,
    uid=27064,
    now_time=int(time()),
    an=67,
    ver='dev2.4',
)
ret = requests.get(url, params=Common.encrypt(data)).json()
print(ret)

# refer=android
# cid=9418&
# expires_time=1527757747
# post_data=1
# refer=android
# time=1528181184
# uid=27064
# now_time=1528181186
# an=67
# ver=dev2.4

# access_token=fbf65d280611a711e70f2dc05290c667
# mp_openid=3bfe295bc944a0b293974be9ffaa9fa9
# token=b8a3df89f6ca7903afea1195e83b1e0a
