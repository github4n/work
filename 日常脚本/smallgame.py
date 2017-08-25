# -*- coding: utf-8 -*-
from common import generate_cookies
import requests
import random
import time
import gevent
from gevent import monkey
import logging
monkey.patch_all()
logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S %p',
                    level=logging.INFO,
                    filename='example.log',
                    filemode='w')


def getc():
    try:
        res = requests.post(url1, cookies=generate_cookies(1522))
        # 期数
        period = res.json()['item_maps']['period']
        # 选项集合
        res_items = res.json()['item_maps']['items']
        logging.info('参数{}{}'.format(period, res_items))
        return period, res_items
    except Exception as e:
        logging.exception(e)
        logging.exception(res.text)


def bet1(uid, period, res_items):
    try:
        item = random.choice(list(res_items))
        # item = 'bet14'
        odds = res_items[item]['odds']
        # 期号 赔率 选项 下注额
        data = dict(period=period, odds=odds, item=item,
                    amount=100, cid=cid)
        res = requests.post(url2, data=data, cookies=generate_cookies(uid))
        logging.info('下注{}'.format(data))
        logging.info(res.json())
    except Exception as e:
        logging.exception(e)


def bet2(uid):
    try:
        res = requests.post(url1, cookies=generate_cookies(uid))
        logging.info('join{}'.format(res.json()))
    except Exception as e:
        logging.exception(e)


def test():
    try:
        res = getc()
        t1 = time.time()
        events = [gevent.spawn(bet2, uid) for uid in user]
        gevent.joinall(events)
        logging.info('join时间消耗{}'.format(time.time() - t1))

        t2 = time.time()
        events = [gevent.spawn(bet1, uid, res[0], res[1]) for uid in user]
        gevent.joinall(events)
        logging.info('下注时间消耗{}'.format(time.time() - t2))
    except Exception as e:
        logging.exception(e)


cid = '2'
domain = 'http://lxy.new.huomaotv.com.cn'
# domain = 'http://lxy.new.huomaotv.com.cn'
url1 = domain + '/smallgame/join/xync?cid=2&is_app=0'
url2 = domain + '/smallgame/bet?is_app=0'
user = range(3060, 3160)
# user = (4153, 4153)
# user = [1522 for i in range(1, 100)]
n = 1
while True:
    logging.info('第{}次：'.format(n))
    test()
    time.sleep(10)
#     n = n + 1
# for i in user:
#     set_money(i, 0, 99999999)
