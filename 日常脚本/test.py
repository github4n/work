#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/13 19:59
# Author : lixingyun
import sys
import json
from  urllib import parse

sys.path.append('../')
from common.common import Common

# a = Common.hash_table(1522)
data = {'8': 0, '9': 0, '10': 1, '11': 1,
        '12': 0, '13': 1, '14': 1, '15': 1,
        '16': 0, '17': 1, '18': 1, '19': 1,
        '20': 0, '21': 0, '22': 0}
# r = Common.REDIS_INST.set('hm_springfestival:user:register:5724', json.dumps(data))
r = Common.REDIS_INST.delete('hm_springfestival:user:register:5724')
print(r)
