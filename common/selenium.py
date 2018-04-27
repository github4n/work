#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/4/13 14:34
# Author : lixingyun
import time

URL = 'http://qa.new.huomaotv.com.cn/'


def CookieLogin(uid, driver):
    ts = str(int(time.time()))
    ts2 = str(int(time.time()) + 4320000)
    key = 'HUOMAOTV!@#$%^&*137SECRET'
    # ts = '1478919600'
    # ts2 = '1479363590'
    a = uid + str(ts) + key
    b = a.encode('utf-8')
    token = str(hashlib.md5(b).hexdigest())
    driver.add_cookie({'name': 'user_e100fe70f5705b56db66da43c140237c', 'value': uid, 'expiry': ts2, 'domain': domain})
    driver.add_cookie({'name': 'user_6b90717037ae096e2f345fde0c31e11b', 'value': token, 'expiry': ts2, 'domain': domain})
    driver.add_cookie({'name': 'user_2c691ee7b8307f7fadc5c2c9349dbd7b', 'value': ts, 'expiry': ts2, 'domain': domain})
    driver.add_cookie({'name': 'user_frontloginstat', 'value': '1', 'expiry': ts2, 'domain': domain})
    time.sleep(2)
    driver.refresh()