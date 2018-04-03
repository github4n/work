#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/13 19:59
# Author : lixingyun
import sys
import json
from  urllib import parse


from common.common import Common
Common.REDIS_INST2.hset('hm_channel_views:962', 'is_live', 1)
ret = Common.REDIS_INST2.hgetall('hm_channel_views:962')




print(ret)