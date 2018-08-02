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







t1 = time.time()
events = []
for i in range(5524, 5534):
    events.append(gevent.spawn(test, i))

gevent.joinall(events)

print(time.time() - t1)
