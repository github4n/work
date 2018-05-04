#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 11:48
# Author : lixingyun
# Description :
#
# from huomao.money import Money
#
# uid = Money.set_xd(1522,1)
# print(uid)
#
from huomao.common import Common
from huomao.user import User
from huomao.channel import Channel
from huomao.money import MoneyClass

user = User()
channel = Channel()
money = MoneyClass()


uid = money.set_money('1522',1)
print(uid)