#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/7/12 16:47
# Author : lixingyun
# Description :

import gevent
from gevent import monkey, pool

monkey.patch_all()
import requests
import time
import hashlib
from huomao.common import REDIS_INST
from huomao.user import User



t1 = time.time()
events = []
for i in range(5524, 5674):
    events.append(gevent.spawn(User.create_noble, 34088, level=1, month=1,cid=2))

gevent.joinall(events)

print(time.time() - t1)
