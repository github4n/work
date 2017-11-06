#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/13 19:59
# Author : lixingyun
import sys
sys.path.append('../..')
from common.db.money import Money
from common.common import Common
from common.db.contents import HmChannel,HmGag
import redis

r = redis.Redis(host='10.10.23.12', port=6379, db=0, decode_responses=True)

res = r.keys('*hm_channel_views*')
for k in res:
    r.delete(k)
# print(res)