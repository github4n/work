#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 16:06
# Author : lixingyun
# Description :
import redis
from .db.money import Money, MoneyPay, MoneyChannelIncome
from .common import REDIS_INST


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
            return Money.create(uid=uid, coin=coin, bean=bean, ts=timestamp)

    # 获取用户余额
    @staticmethod
    def get_money(uid):
        money = Money.select().where(Money.uid == uid).first()
        return {'coin': money.coin, 'bean': money.bean}
