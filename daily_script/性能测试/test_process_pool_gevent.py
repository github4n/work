#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/7/13 15:07
# Author : lixingyun
# Description :
import grequests
import time
from multiprocessing import Process, cpu_count, Pool
import os

url = 'http://qa.new.huomaotv.com.cn/'


def process_start(i):
    print(i)
    print('子进程{}'.format(os.getpid()))
    # rs = [grequests.get(url) for i in range(100)]
    # grequests.map(rs)


if __name__ == '__main__':
    print('父进程:{}'.format(os.getpid()))
    t1 = time.time()
    pool = Pool(processes=8)
    for i in range(8):
        pool.apply_async(process_start,(i,))
    pool.close()
    pool.join()
    print(time.time() - t1)

    # total_cores = cpu_count()
    # jobs = []
    # t1 = time.time()
    # for i in range(total_cores):
    #     p = Process(target=process_start, args=())
    #     p.start()
    #     jobs.append(p)
    # for job in jobs:
    #     job.join()
    # print(time.time() - t1)
