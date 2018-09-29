#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/7/24 13:54
# Author : lixingyun
# Description :
from huomao.user import User
from huomao.bag import Bag
from decimal import *
import requests
from huomao.common import Common, REDIS_INST
from huomao.money import MoneyClass
import time
# Bag.add_bag(1522,90001)

# User.add_noble_card(34052, 3, 2, 1)


#
# t = Bag.get_dmk(1522,90011)


item = 1000
uid = 35482

MoneyClass.set_money(uid, item / 1000, 0)

REDIS_INST.delete('hm_new_guess_active_recharge_joins_tag')
# url = 'http://lxy.new.huomaotv.com.cn/badgeexchange/exchangePay?room_number=0&refer=web'
url = 'http://lxy.new.huomaotv.com.cn/Smallgame/exchangePay?room_number=0&refer=web'
ret = requests.post(url, data=dict(item=item), cookies=Common.generate_cookies(uid))
print(ret.text)
