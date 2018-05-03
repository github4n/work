#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/4/17 17:53
# Author : lixingyun
# Description : 测试贵族功能
from gevent import monkey
monkey.patch_all()
import gevent


events = [gevent.spawn(f, url, data, uid) for uid in uids]
gevent.joinall(events)