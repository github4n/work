#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/11 14:42
# Author : lixingyun
# Description :
from huomao.user import User,Userbase
from huomao.money import MoneyClass
from huomao.bag import Bag
from huomao.selenium import URL,CookieLogin
from selenium import webdriver
from huomao.common import REDIS_INST,Common


# Userbase.update(get_experience=0).where(Userbase.uid == '1522').execute()


# User.update_nick_name('22693'
#
# ,'运维的锅')ㅤㅤㅤㅤㅤㅤㅤ
# User.set_badge(5257,48)

u = User()
uid = u.reg('noble')
u.bd_sj(uid)
MoneyClass.set_money(uid, 5000000)
# User.create_noble(uid, level=7, month=1,cid=13)
# User.set_noble_expire(uid, 30)
# Bag.add_bag(uid,bag=90001)

#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get('http://qa.new.huomaotv.com.cn/1')
# driver.maximize_window()
# CookieLogin(uid,driver)
# driver.get('http://qa.new.huomaotv.com.cn/memberpay/noblePay')

# 非贵族
# 房主 t_n3247(26311)  1225388   粉丝0-1 徽章 0-3
#


# 贵族
# 房主 1
# 房管 t_n3249（26450） 粉丝0-1 徽章 0-3



