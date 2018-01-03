#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/1/2 10:05
# Author : lixingyun
from guess import create, bet, update_status, settlement, change_banker
from common.common import Common
import gevent
from gevent import monkey
import random
import time
import logging

monkey.patch_all()

uids = list(range(60000, 3159))
# for uid in uids:
#     bean = Common.get_money(uid)['bean']
#     xd = Common.get_xd(uid)
#     if bean != 100 or xd !=100:
#         print(uid,bean,xd)
#     print(uid)
#     Common.set_xd(uid, 100000)
#     Common.set_money(uid, 100000,100000)
# exit()

'''对冲竞猜'''


# 下注,个人下注上限
def gamble_bet_bet():
    uid = 1522
    period = create(guess_type='match', play_type='gamble')
    kw = dict(uid=uid, period=period, chose='option_A', coin_type='free_bean', amount=200000)
    events = []
    for i in range(0, 200):
        events.append(gevent.spawn(bet, **kw))
    gevent.joinall(events)


# 下注,锁定
def gamble_bet_locking():
    period = create(guess_type='match', play_type='gamble')
    events = []
    events.append(gevent.spawn(update_status, period, 'locking'))
    for uid in range(3306, 3406):
        kw = dict(uid=uid, period=period, chose='option_A', coin_type='free_bean', amount=100)
        events.append(gevent.spawn(bet, **kw))
    random.shuffle(events)
    gevent.joinall(events)


# 下注,封盘
def gamble_bet_blockade():
    period = create(guess_type='match', play_type='gamble')
    events = []
    events.append(gevent.spawn(update_status, period, 'blockade'))
    for uid in range(6000, 6100):
        kw = dict(uid=uid, period=period, chose='option_A', coin_type='free_bean', amount=100)
        events.append(gevent.spawn(bet, **kw))
    t1 = time.time()
    gevent.joinall(events)
    logging.info('耗时{}'.format(time.time() - t1))


# 下注,结算
def gamble_bet_settlement():
    period = create(guess_type='match', play_type='gamble')
    events = []
    for uid in uids[:10]:
        kw = dict(uid=uid, period=period, chose='option_B', coin_type='free_bean', amount=100)
        events.append(gevent.spawn(bet, **kw))
    events.append(gevent.spawn(settlement, period=period, win_option='option_A'))
    for uid in uids[10:]:
        kw = dict(uid=uid, period=period, chose='option_B', coin_type='free_bean', amount=100)
        events.append(gevent.spawn(bet, **kw))
    t1 = time.time()
    gevent.joinall(events)
    logging.info('耗时{}'.format(time.time() - t1))


# 结算并发
def gamble_settlement_settlement():
    period = create(guess_type='match', play_type='gamble')
    uid = 1522
    bet(uid=uid, period=period, chose='option_A', coin_type='free_bean', amount=100)
    events = []
    for i in range(10):
        events.append(gevent.spawn(settlement, period=period, win_option='option_A'))
    gevent.joinall(events)


'''坐庄竞猜'''


# 下注,超出庄上限
def banker_bet_bet():
    period = create(guess_type='match', play_type='banker')
    bet(uid=1522, period=period, chose='option_B', coin_type='free_bean', amount=100, punter='banker', banker_odds=0.5)
    events = []
    for uid in uids:
        kw = dict(uid=uid, period=period, chose='option_A', coin_type='free_bean', amount=20, punter='buyer')
        events.append(gevent.spawn(bet, **kw))
    gevent.joinall(events)


# 下注,个人下注上限
def banker_bet_bet_person():
    period = create(guess_type='match', play_type='banker')
    bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=100000, punter='banker', banker_odds=0.01)
    events = []
    for uid in uids:
        kw = dict(uid=1522, period=period, chose='option_B', coin_type='free_bean', amount=200000, punter='buyer')
        events.append(gevent.spawn(bet, **kw))
    gevent.joinall(events)


# 下注,撤庄
def banker_bet_changebanker():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        kw = dict(uid=uid, period=period, chose='option_B', coin_type='free_bean', amount=100, punter='buyer')
        events.append(gevent.spawn(bet, **kw))
        if uid == uids[10]:
            events.append(gevent.spawn(change_banker, 1522, period, order_id))
    gevent.joinall(events)
    settlement(period=period, win_option='option_A')


# 下注,修改庄
def banker_bet_changebanker2():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        kw = dict(uid=uid, period=period, chose='option_B', coin_type='free_bean', amount=100, punter='buyer')
        events.append(gevent.spawn(bet, **kw))
        if uid == uids[5]:
            events.append(gevent.spawn(change_banker, 1522, period, order_id, 2, 'change'))
    gevent.joinall(events)
    # settlement(period=period, win_option='option_B')

# settlement(period=2018010393, win_option='option_A')
# banker_bet_changebanker2()
# 下注,锁定
def banker_bet_locking():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        kw = dict(uid=uid, period=period, chose='option_B', coin_type='free_bean', amount=100, punter='buyer')
        events.append(gevent.spawn(bet, **kw))
        if uid == 6010:
            events.append(gevent.spawn(update_status, period, 'locking'))
    gevent.joinall(events)
    settlement(period=period, win_option='option_B')


# 下注,封盘
def banker_bet_blockade():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        kw = dict(uid=uid, period=period, chose='option_B', coin_type='free_bean', amount=100, punter='buyer')
        events.append(gevent.spawn(bet, **kw))
        if uid == 6010:
            events.append(gevent.spawn(update_status, period, 'blockade'))
    gevent.joinall(events)
    settlement(period=period, win_option='option_B')


# 下注,结算
def banker_bet_settlement():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        kw = dict(uid=uid, period=period, chose='option_B', coin_type='free_bean', amount=100, punter='buyer')
        events.append(gevent.spawn(bet, **kw))
        if uid == 6010:
            events.append(gevent.spawn(settlement, period=period, win_option='option_A'))
    gevent.joinall(events)


# 坐庄,个人坐庄上限
def banker_banker_person():
    period = create(guess_type='match', play_type='banker')
    events = []
    for uid in uids:
        kw = dict(uid=1522, period=period, chose='option_B', coin_type='free_bean', amount=100, unter='banker', banker_odds=1)
        events.append(gevent.spawn(bet, **kw))
    gevent.joinall(events)


# 坐庄,撤庄
# 坐庄,修改庄
# 坐庄,锁定
def banker_banker_changebanker():
    period = create(guess_type='match', play_type='banker')
    events = []
    for uid in uids:
        kw = dict(uid=1522, period=period, chose='option_B', coin_type='free_bean', amount=100, unter='banker', banker_odds=1)
        events.append(gevent.spawn(bet, **kw))
        if uid == uids[10]:
            events.append(gevent.spawn(update_status, period, 'locking'))
    gevent.joinall(events)


# 坐庄,封盘
def banker_banker_blockade():
    period = create(guess_type='match', play_type='banker')
    events = []
    for uid in uids:
        kw = dict(uid=1522, period=period, chose='option_B', coin_type='free_bean', amount=100, unter='banker', banker_odds=1)
        events.append(gevent.spawn(bet, **kw))
        if uid == uids[10]:
            events.append(gevent.spawn(update_status, period, 'blockade'))
    gevent.joinall(events)


# 坐庄,结算
def banker_banker_settlement():
    period = create(guess_type='match', play_type='banker')
    events = []
    for uid in uids:
        kw = dict(uid=1522, period=period, chose='option_B', coin_type='free_bean', amount=100, unter='banker', banker_odds=1)
        events.append(gevent.spawn(bet, **kw))
        if uid == uids[10]:
            events.append(gevent.spawn(settlement, period=period, win_option='option_A'))
    gevent.joinall(events)


# 撤庄并发
def banker_changebanker_changebanker():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        events.append(gevent.spawn(change_banker, 1522, period, order_id))
    gevent.joinall(events)
    settlement(period=period, win_option='option_A')


# 撤庄,修改庄
def banker_changebanker_changebanker2():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        events.append(gevent.spawn(change_banker, 1522, period, order_id))
        events.append(gevent.spawn(change_banker, 1522, period, order_id, 2, 'change'))
    gevent.joinall(events)
    settlement(period=period, win_option='option_A')


# 撤庄,锁定
def banker_changebanker_locking():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        events.append(gevent.spawn(change_banker, 1522, period, order_id))
        events.append(gevent.spawn(update_status, period, 'locking'))
    gevent.joinall(events)
    settlement(period=period, win_option='option_A')


# 撤庄,封盘
def banker_changebanker_blockade():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        events.append(gevent.spawn(change_banker, 1522, period, order_id))
        events.append(gevent.spawn(update_status, period, 'blockade'))
    gevent.joinall(events)
    settlement(period=period, win_option='option_A')


# 撤庄,结算
def banker_changebanker_settlement():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        events.append(gevent.spawn(change_banker, 1522, period, order_id))
        events.append(gevent.spawn(settlement, period=period, win_option='option_A'))
    gevent.joinall(events)
    settlement(period=period, win_option='option_A')


# 修改庄并发
def banker_changebanker_new_changebanker():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        events.append(gevent.spawn(change_banker, 1522, period, order_id, 3, 'change'))
        events.append(gevent.spawn(change_banker, 1522, period, order_id, 2, 'change'))
    gevent.joinall(events)
    settlement(period=period, win_option='option_A')


# 修改庄,锁定
def banker_changebanker_new_locking():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        events.append(gevent.spawn(change_banker, 1522, period, order_id, 2, 'change'))
        events.append(gevent.spawn(update_status, period, 'locking'))
    gevent.joinall(events)
    settlement(period=period, win_option='option_A')


# 修改庄,封盘
def banker_changebanker_new_blockade():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        events.append(gevent.spawn(change_banker, 1522, period, order_id, 3, 'change'))
        events.append(gevent.spawn(update_status, period, 'blockade'))
    gevent.joinall(events)
    settlement(period=period, win_option='option_A')


# 修改庄,结算
def banker_changebanker_new_settlement():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    events = []
    for uid in uids:
        events.append(gevent.spawn(change_banker, 1522, period, order_id, 3, 'change'))
        events.append(gevent.spawn(settlement, period=period, win_option='option_A'))
    gevent.joinall(events)
    settlement(period=period, win_option='option_A')


# 结算并发
def settlement_settlement():
    period = create(guess_type='match', play_type='banker')
    order_id = bet(uid=1522, period=period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
    bet(uid=1522, period=period, chose='option_B', coin_type='free_bean', amount=100, punter='buyer')
    events = []
    for uid in uids:
        events.append(gevent.spawn(settlement, period=period, win_option='option_A'))
    gevent.joinall(events)
