#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/4/20 15:52
# Author : lixingyun
# Description :
from common.common import Common

for i in range(101):
    name = 'tuyu' + str(i)
    try:
        uid = Common.register(name)['uid']
        print(uid)
        Common.bd_sj(uid)
        Common.set_money(uid,999999,999999)
        Common.set_xd(uid, 99999999)
    except  Exception:
        print(Exception)
