#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 16:06
# Author : lixingyun
# Description :
import redis
import time
from .db.money import Money
from .db.noble_coin import NobleCoin
from .common import REDIS_INST
from .db.money import MoneyPay, MoneyChannelIncome
from .config import mon_last_time,mon_first_time,logger_huomao
from peewee import fn



class MoneyClass():
    # 设置仙豆
    @staticmethod
    def set_xd(uid, xd):
        xd = 0 if not xd else xd
        return REDIS_INST.set('hm_free_bean_{}'.format(uid), int(xd) if xd else 0)

    # 获取仙豆
    @staticmethod
    def get_xd(uid):
        return int(REDIS_INST.get('hm_free_bean_{}'.format(uid)))

    # 设置用户猫币，猫豆
    @staticmethod
    def set_money(uid, coin=0, bean=0):
        coin = 0 if not coin else coin
        bean = 0 if not bean else bean
        money = Money.select().where(Money.uid == uid).first()
        # 判断用户是否存在记录，存在则修改，否则插入数据
        if money:
            return Money.update(coin=coin, bean=bean).where(Money.uid == uid).execute()
        else:
            return Money.create(uid=uid, coin=coin, bean=bean, ts=str(int(time.time())))

    # 设置用户贵族猫币
    @staticmethod
    def set_noble_coin(uid, noble_coin=0, ts=str(int(time.time()))):
        noble_coin = noble_coin if noble_coin else 0
        noble = NobleCoin.select().where(NobleCoin.uid == uid).first()
        # 判断用户是否存在记录，存在则修改，否则插入数据
        if noble:
            return NobleCoin.update(coin=noble_coin, ts=ts).where(NobleCoin.uid == uid).execute()
        else:
            return NobleCoin.create(uid=uid, coin=noble_coin, ts=ts)

    # 获取用户余额
    @staticmethod
    def get_money(uid):
        money = Money.select().where(Money.uid == uid).first()
        ret = {'coin': money.coin, 'bean': money.bean}
        logger_huomao.info(ret)
        return ret

    # 获取用户贵族余额
    @staticmethod
    def get_noble_coin(uid):
        noble = NobleCoin.select().where(NobleCoin.uid == uid).first()
        return noble.coin if noble else 0

    # 获取用户猫币，贵族猫币
    @staticmethod
    def get_coin(uid):
        noble = NobleCoin.select().where(NobleCoin.uid == uid).first()
        money = Money.select().where(Money.uid == uid).first()
        return (money.coin, noble.coin)

    # 获取送礼记录
    @staticmethod
    def get_money_pay(uid, cid):
        count = MoneyPay.select(fn.COUNT(1).alias('nums')).where((MoneyPay.uid == uid) & (MoneyPay.other_cid == cid) & (MoneyPay.ts < mon_last_time)& (MoneyPay.ts > mon_first_time)).first()
        return count.nums

    # 获取收礼记录
    @staticmethod
    def money_income(type, uid, user_id=0):
        m = 0
        if type == 'del':
            m = MoneyChannelIncome.delete().where(MoneyChannelIncome.uid == uid).execute()
        elif type == 'get':
            m = MoneyChannelIncome.select().where((MoneyChannelIncome.uid == uid) & (MoneyChannelIncome.addtime < mon_last_time) & (
                MoneyChannelIncome.other_uid == user_id)).first()
            m = m.money
        elif type == 'count':
            m = MoneyChannelIncome.select(fn.COUNT(1).alias('nums')).where((MoneyChannelIncome.uid == uid) & (MoneyChannelIncome.addtime < mon_last_time) & (
                MoneyChannelIncome.other_uid == user_id)).first().nums
        return m