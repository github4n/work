#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/9 13:26
# Author : lixingyun
# Description :

from peewee import *
from ..config import DB_CONFIG

database = MySQLDatabase('hm_noble', **DB_CONFIG)


class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class HmNobleInfo(BaseModel):
    anchor = IntegerField(db_column='anchor_id', index=True)
    end_time = IntegerField(index=True)
    level = IntegerField(index=True)
    start_time = IntegerField(index=True)
    type = IntegerField(index=True)
    uid = IntegerField(index=True)
    update_time = IntegerField()

    class Meta:
        db_table = 'hm_noble_info'

class HmNobleRecord(BaseModel):
    anchor = IntegerField(db_column='anchor_id', index=True, null=True)
    anchor_profit = DecimalField(null=True)
    end_time = IntegerField(index=True)
    level = IntegerField()
    day_num = IntegerField()
    op_time = IntegerField()
    op_username = CharField()
    open_type = IntegerField()
    pay_money = DecimalField(null=True)
    send_uid = IntegerField(null=True)
    start_time = IntegerField()
    type = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_record'

class HmNobleUser(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user'

