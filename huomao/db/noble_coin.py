#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/14 12:15
# Author : lixingyun
from peewee import *
from .config import DB_CONFIG

database = MySQLDatabase('hm_noble_coin', **DB_CONFIG)


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class NobleCoin(BaseModel):
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'noble_coin'

