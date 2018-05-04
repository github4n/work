#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/10/30 15:27
# Author : lixingyun
from peewee import *
from .config import DB_CONFIG

database = MySQLDatabase('hm_user_bag', **DB_CONFIG)


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class UserBag(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )


class UserBagUseRecord(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record'
        indexes = (
            (('uid', 'type'), False),
        )
