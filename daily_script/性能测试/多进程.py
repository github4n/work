#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/8/1 9:50
# Author : lixingyun
# Description :
import time
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor
from test import test_requests


start = time.time()
pool = ProcessPoolExecutor()
results = list(pool.map(test_requests, ))
end = time.time()
print(end - start)

# from multiprocessing import Pool, cpu_count
# import os, time, random

#
# print(cpu_count())
# exit()
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
