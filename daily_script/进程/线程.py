#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/10/23 10:50
# Author : lixingyun
import threading
import time
import sys
import requests


# print(sys.getcheckinterval())

def fun(*args):
    time.sleep(2)

t1 = time.time()

threads = []

threads.append(threading.Thread(target=fun, args=()))  # 创建线程,添加到线程组
threads.append(threading.Thread(target=fun, args=()))  # 创建线程,添加到线程组

for t in threads:
    t.setDaemon(True)  # 设置为守护线程,不用等待守护线程,主线程就可以退出
    t.start()
for t in threads:
    t.join()  # 在子线程完成运行之前，这个子线程的父线程将一直被阻塞

print(time.time()-t1)