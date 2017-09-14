#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/13 19:59
# Author : lixingyun
import sys
sys.path.append('../..')
from common.db.money import Money
from common.common import Common
from common.db.contents import HmChannel,HmGag
# from db import config
# u = Money.select().where(Money.uid=='1522').first()
# u = Userbase.select().where(Userbase.name=='')
# print(u.uid)

# channel = HmChannel.select().where(HmChannel.uid=='1522').first()
# print(channel)

HmGag.delete().where(1==1).execute()