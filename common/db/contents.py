#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/8/17 9:16
# Author : lixingyun
# python -m pwiz -e mysql -H 10.10.23.15  -u huomao -P huomao  hm_contents > db.py
import sys

sys.path.append('..')
from peewee import *
from common.db.config import DB_CONFIG

database = MySQLDatabase('hm_contents', **DB_CONFIG)


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class HmChannel(BaseModel):
    addtime = IntegerField()
    channel = CharField()
    content = TextField(null=True)
    del_time = IntegerField(null=True)
    entertainment_time = IntegerField(null=True)
    event_endtime = IntegerField(null=True)
    event_starttime = IntegerField(null=True)
    gid = IntegerField(index=True)
    high_status = IntegerField(null=True)
    image = CharField(null=True)
    is_del = IntegerField(index=True, null=True)
    is_entertainment = CharField(null=True)
    is_event = CharField(null=True)
    is_high = IntegerField()
    is_index = IntegerField(index=True, null=True)
    is_index_live = IntegerField()
    is_index_top = IntegerField(null=True)
    is_index_type = IntegerField()
    is_live = IntegerField(index=True, null=True)
    is_push = IntegerField(null=True)
    is_replay = IntegerField()
    is_sign = IntegerField(index=True)
    is_sub = IntegerField()
    is_tuijian = IntegerField(null=True)
    is_zhuanma = CharField(null=True)
    live_last_start_time = IntegerField(null=True)
    logo = CharField(null=True)
    note = CharField()
    opusername = CharField(null=True)
    percent = CharField()
    room_number = IntegerField(index=True)
    roomadmin_num = IntegerField(null=True)
    sh_zt = IntegerField(index=True, null=True)
    status = IntegerField(index=True)
    stream = CharField(index=True)
    stream_key = CharField(null=True)
    superstar_info = TextField(null=True)
    tag = CharField(index=True)
    tel = CharField(null=True)
    tj_pic = CharField(null=True)
    tj_title = CharField(null=True)
    uid = IntegerField()
    updatetime = IntegerField(null=True)
    username = CharField(null=True)
    views = IntegerField()

    class Meta:
        db_table = 'hm_channel'


class HmGag(BaseModel):
    addtime = IntegerField()
    ban_uid = IntegerField()
    channel = CharField(null=True)
    cid = IntegerField()
    is_root = IntegerField()
    mname = CharField()
    node = CharField(null=True)
    status = IntegerField(null=True)
    type = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_gag'


class HmLoveliness(BaseModel):
    cid = IntegerField(index=True)
    is_sel = IntegerField()
    other_uid = IntegerField(index=True)
    score = IntegerField()
    settime = IntegerField()
    type = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_loveliness'
        indexes = (
            (('uid', 'score'), False),
        )
