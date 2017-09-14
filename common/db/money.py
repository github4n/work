#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/14 12:15
# Author : lixingyun
import sys
sys.path.append('..')
from peewee import *
from common.db.config import DB_CONFIG

database = MySQLDatabase('hm_money', **DB_CONFIG)


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Money(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money'


class MoneyPay(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay'

class MoneyChannelIncome(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income'