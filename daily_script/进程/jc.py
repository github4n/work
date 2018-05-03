#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/11/28 10:17
# Author : lixingyun
import multiprocessing
import gevent
import time
import tornado
from threadpool import ThreadPool, makeRequests
from tornado.httpclient import AsyncHTTPClient
from multiprocessing import Process, Manager

process_num = 20  # 进程数
gevent_num = 200  # 协程数

url = "http://qa.new.huomaotv.com.cn/plugs/getCacheTime"


def asynchronous(url):
    try:
        threads = []
        for i in range(gevent_num):
            threads.append(gevent.spawn(request_url, url))
        gevent.joinall(threads)
    except Exception as e:
        pass


def request_url(url):
    http_client = AsyncHTTPClient()
    # global sum
    # sum.value += 1
    http_client.fetch(url, callback=handle_request)
    # time.sleep(1)
    # print " count: " + str(sum.value) + " cur process: " + str(os.getpid()) + " cur thread: " + str(threading.current_thread)
    global loop
    loop = tornado.ioloop.IOLoop.instance()
    if loop._running is False:
        loop.start()


def handle_request(response):
    # print "current site: " + str(response.effective_url) + " , request  time: " + str(
    #     getattr(response, "request_time", "000"))
    loop.stop()


if __name__ == '__main__':
    sum = Manager().Value('count', 0)
    starttime = time.time()
    pool = multiprocessing.Pool(processes=process_num)
    for i in range(process_num):
        pool.apply_async(asynchronous, (url,))
    pool.close()
    pool.join()
    print(sum.value)
    print("cost time: " + str(time.time() - starttime))
