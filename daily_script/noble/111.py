#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/17 17:36
# Author : lixingyun
# Description :

import requests
import time

while True:
    requests.get('http://test.new.huomaotv.com.cn/crontab/addNobleSubscribe')
    time.sleep(1)
