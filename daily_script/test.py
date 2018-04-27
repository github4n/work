#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/4/26 18:58
# Author : lixingyun
# Description :
import time
import datetime

now = datetime.datetime.now()
today = datetime.date.today()
start_time = datetime.datetime(today.year, today.month, today.day, 23, 55, 0, 0)
end_time = datetime.datetime(today.year, today.month, today.day, 0, 5, 0, 0)

if now >= start_time or now <= end_time:
    print(start_time, end_time)


