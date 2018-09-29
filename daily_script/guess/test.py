#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/7 15:55
# Author : lixingyun
# Description :
import requests
import time
from huomao.common import Common, REDIS_INST
from huomao.money import MoneyClass

from guess import create, banker, bet,settlement,Calculation
#
# REDIS_INST.delete('hm_new_guess_active_recharge_joins_tag')
# exit()

period = create()
banker(uid=1522, period=period, coin_type='cat_bean', amount=500000)
banker(uid=1522, period=period, coin_type='cat_bean', amount=500000,chose=2)




bet(35499, period=period, coin_type='cat_bean', punter='buyer',
    chose={  # 下注选项
        0: {'chose': 1, 'amount': 1000, 'now_odds': 2},
        1: {'chose': 2, 'amount': 1000, 'now_odds': 2},

    }, )


bet(35499, period=period, coin_type='cat_bean', punter='buyer',
    chose={  # 下注选项
        0: {'chose': 1, 'amount': 2000, 'now_odds': 2}

    }, )


bet(35499, period=period, coin_type='cat_bean', punter='buyer',
    chose={  # 下注选项
        0: {'chose': 2, 'amount': 2000, 'now_odds': 2}
    }, )




time.sleep(2)

settlement(period=period,win_option=1)

Calculation()



# item = 1000
# uid = 35482
#
# MoneyClass.set_money(uid, item / 1000, 0)
#
# REDIS_INST.delete('hm_new_guess_active_recharge_joins_tag')
# url = 'http://lxy.new.huomaotv.com.cn/badgeexchange/exchangePay?room_number=0&refer=web'
# url = 'http://lxy.new.huomaotv.com.cn/Smallgame/exchangePay?room_number=0&refer=web'
# ret = requests.post(url, data=dict(item=item), cookies=Common.generate_cookies(uid))
# print(ret.text)



# jt = REDIS_INST.get('hm_zcm_key1537459200')
# zt = REDIS_INST.set('hm_zcm_key1537372800', jt)
# REDIS_INST.delete('hm_zcm_key1537459200')