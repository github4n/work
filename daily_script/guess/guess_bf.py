#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/1/2 10:05
# Author : lixingyun
from guess import create, bet, update_status, settlement, change_banker
from huomao.common import Common
import gevent
from gevent import monkey
import random
import time
import logging

monkey.patch_all()


class TestGuess():
    def __init__(self, play_type, uids):
        self.period = create(guess_type='match', play_type=play_type)
        self.uids = uids
        self.uid = 1522

    def add(self):
        for uid in self.uids:
            Common.set_xd(uid, 100000)
            Common.set_money(uid, 100000, 100000)

    def get_m(self):
        res = {}
        uids = self.uids
        uids.append(self.uid)
        for uid in uids:
            xd = Common.get_xd(uid)
            md = Common.get_money(uid)['bean']
            res[uid] = (xd, md)
        return res

    def cmp(self, res1, res2):
        for key in res1:
            if key in res2:
                if res1[key] != res2[key]:
                    print(key, res1[key], res2[key])

    def test(self):
        for uid in self.uids:
            bean = Common.get_money(uid)['bean']
            xd = Common.get_xd(uid)
            if bean != 100 or xd != 100:
                print(uid, bean, xd)

    '''对赌竞猜'''

    # 下注,货币上限/个人下注上限
    def gamble_bet_bet(self):
        Common.set_xd(self.uid, 1200000)
        Common.set_money(self.uid, 0, 1200000)
        kw = dict(uid=self.uid, period=self.period, chose='option_A', coin_type='cat_bean', amount=200000)
        events = []
        for i in self.uids:
            events.append(gevent.spawn(bet, **kw))
        gevent.joinall(events)

    # 下注,锁定,封盘,结算
    def gamble_bet_status(self):
        events = []
        for uid in self.uids:
            kw = dict(uid=uid, period=self.period, chose='option_B', coin_type='free_bean', amount=100)
            events.append(gevent.spawn(bet, **kw))
            if uid == uids[5]:
                events.append(gevent.spawn(update_status, self.period, 'locking'))  # blockade封盘
                # events.append(gevent.spawn(settlement, period=self.period, win_option='option_B')) # 结算
        gevent.joinall(events)

    # 结算并发
    def gamble_settlement_settlement(self):
        Common.set_xd(self.uid, 200)
        Common.set_money(self.uid, 0, 200)
        Common.set_xd(1523, 200)
        Common.set_money(1523, 0, 200)
        bet(uid=self.uid, period=self.period, chose='option_A', coin_type='free_bean', amount=100)
        bet(uid=1523, period=self.period, chose='option_B', coin_type='free_bean', amount=100)
        events = []
        for i in self.uids:
            events.append(gevent.spawn(settlement, period=self.period, win_option='option_B'))
        gevent.joinall(events)

    '''坐庄竞猜'''

    # 下注,超出庄上限
    def banker_bet_bet(self):
        bet(uid=self.uid, period=self.period, chose='option_A', coin_type='free_bean', amount=100, punter='banker', banker_odds=0.5)
        events = []
        for uid in self.uids:
            kw = dict(uid=uid, period=self.period, chose='option_B', coin_type='free_bean', amount=20, punter='buyer')
            events.append(gevent.spawn(bet, **kw))
        gevent.joinall(events)

    # 下注,个人下注上限
    def banker_bet_bet_person(self):
        bet(uid=self.uid, period=self.period, chose='option_A', coin_type='cat_bean', amount=100000, punter='banker', banker_odds=0.01)
        events = []
        for i in self.uids:
            kw = dict(uid=self.uid, period=self.period, chose='option_B', coin_type='cat_bean', amount=200000, punter='buyer')
            events.append(gevent.spawn(bet, **kw))
        gevent.joinall(events)

    # 下注,撤庄,修改庄
    def banker_bet_change_banker(self):
        res1 = self.get_m()
        order_id = bet(uid=self.uid, period=self.period, chose='option_A', coin_type='cat_bean', amount=10000, punter='banker', banker_odds=1)
        events = []
        for uid in self.uids:
            kw = dict(uid=uid, period=self.period, chose='option_B', coin_type='cat_bean', amount=100, punter='buyer')
            events.append(gevent.spawn(bet, **kw))
            if uid == self.uids[5]:
                events.append(gevent.spawn(change_banker, self.uid, self.period, order_id))  # 撤庄
                # events.append(gevent.spawn(change_banker, self.uid, self.period, order_id, 2, 'change')) # 修改庄
        gevent.joinall(events)
        settlement(period=self.period, win_option='option_A')
        res2 = self.get_m()
        self.cmp(res1, res2)

    # 下注,锁定,封盘,结算
    def banker_bet_status(self):
        res1 = self.get_m()
        order_id = bet(uid=self.uid, period=self.period, chose='option_A', coin_type='free_bean', amount=10000, punter='banker', banker_odds=1)
        events = []
        for uid in self.uids:
            kw = dict(uid=uid, period=self.period, chose='option_B', coin_type='free_bean', amount=100, punter='buyer')
            events.append(gevent.spawn(bet, **kw))
            if uid == self.uids[5]:
                # events.append(gevent.spawn(settlement, period=self.period, win_option='option_A')) # 结算
                events.append(gevent.spawn(update_status, self.period, 'locking'))  # blockade封盘 locking锁定
        gevent.joinall(events)
        settlement(period=self.period, win_option='option_B')
        res2 = self.get_m()
        self.cmp(res1, res2)

    # 坐庄,个人坐庄上限
    def banker_banker_person(self):
        res1 = self.get_m()
        events = []
        for i in uids:
            kw = dict(uid=1522, period=self.period, chose='option_B', coin_type='cat_bean', amount=2000000, punter='banker', banker_odds=1)
            events.append(gevent.spawn(bet, **kw))
        gevent.joinall(events)
        res2 = self.get_m()
        self.cmp(res1, res2)

    # 坐庄,撤庄,修改庄没必要
    # 坐庄,锁定和封盘,结算
    def banker_banker_status(self):
        res1 = self.get_m()
        events = []
        for uid in self.uids:
            kw = dict(uid=uid, period=self.period, chose='option_B', coin_type='free_bean', amount=100, punter='banker', banker_odds=1)
            events.append(gevent.spawn(bet, **kw))
            if uid == self.uids[5]:
                events.append(gevent.spawn(settlement, period=self.period, win_option='option_B'))  # 结算
                # events.append(gevent.spawn(update_status, self.period, 'blockade')) #blockade封盘 locking锁定
        gevent.joinall(events)
        # settlement(period=self.period, win_option='option_B')
        res2 = self.get_m()
        self.cmp(res1, res2)

    # 撤庄并发
    def banker_change_banker_change_banker(self):
        res1 = self.get_m()
        order_id = bet(uid=self.uid, period=self.period, chose='option_B', coin_type='free_bean', amount=100, punter='banker', banker_odds=1)
        events = []
        for i in self.uids:
            events.append(gevent.spawn(change_banker, self.uid, self.period, order_id))
        gevent.joinall(events)
        # settlement(period=self.period, win_option='option_B')
        res2 = self.get_m()
        self.cmp(res1, res2)

    # 撤庄,修改庄
    def banker_change_banker_change_banker2(self):
        res1 = self.get_m()
        order_id = bet(uid=self.uid, period=self.period, chose='option_B', coin_type='free_bean', amount=100, punter='banker', banker_odds=1)
        events = []
        for i in self.uids:
            events.append(gevent.spawn(change_banker, self.uid, self.period, order_id, 2, 'change'))
            events.append(gevent.spawn(change_banker, self.uid, self.period, order_id))
        gevent.joinall(events)
        settlement(period=self.period, win_option='option_B')
        res2 = self.get_m()
        self.cmp(res1, res2)

    # 撤庄,锁定,封盘,结算
    def banker_change_banker_status(self):
        res1 = self.get_m()
        order_id = bet(uid=self.uid, period=self.period, chose='option_B', coin_type='cat_bean', amount=100, punter='banker', banker_odds=1)
        events = []
        events.append(gevent.spawn(change_banker, self.uid, self.period, order_id))
        # events.append(gevent.spawn(update_status, self.period, 'blockade'))  # blockade #封盘 locking锁定
        events.append(gevent.spawn(settlement, period=self.period, win_option='option_A'))  # 结算
        gevent.joinall(events)
        settlement(period=self.period, win_option='option_B')
        res2 = self.get_m()
        self.cmp(res1, res2)

    # 修改庄并发
    def banker_change_banker_new(self):
        res1 = self.get_m()
        order_id = bet(uid=self.uid, period=self.period, chose='option_B', coin_type='cat_bean', amount=100, punter='banker', banker_odds=1)
        events = []
        events.append(gevent.spawn(change_banker, self.uid, self.period, order_id, 3, 'change'))
        events.append(gevent.spawn(change_banker, self.uid, self.period, order_id, 2, 'change'))
        gevent.joinall(events)
        settlement(period=self.period, win_option='option_A')
        res2 = self.get_m()
        self.cmp(res1, res2)

    # 修改庄,锁定,封盘,结算
    def banker_changebanker_new_status(self):
        res1 = self.get_m()
        order_id = bet(uid=self.uid, period=self.period, chose='option_B', coin_type='cat_bean', amount=100, punter='banker', banker_odds=1)
        events = []
        events.append(gevent.spawn(change_banker, self.uid, self.period, order_id, 2, 'change'))
        # events.append(gevent.spawn(update_status, self.period, 'blockade'))  # blockade #封盘 locking锁定
        events.append(gevent.spawn(settlement, period=self.period, win_option='option_A'))  # 结算
        gevent.joinall(events)
        # settlement(period=self.period, win_option='option_B')
        res2 = self.get_m()
        self.cmp(res1, res2)

    # 结算并发
    def banker_settlement(self):
        res1 = self.get_m()
        order_id = bet(uid=self.uid, period=self.period, chose='option_B', coin_type='free_bean', amount=100, punter='banker', banker_odds=1)
        bet(uid=self.uid, period=self.period, chose='option_A', coin_type='free_bean', amount=100, punter='buyer')
        events = []
        for i in uids:
            events.append(gevent.spawn(settlement, period=self.period, win_option='option_B'))
        gevent.joinall(events)
        res2 = self.get_m()
        self.cmp(res1, res2)


uids = list(range(6000, 6200))
test = TestGuess('banker', uids)
test.banker_settlement()
