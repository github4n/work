#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/13 19:57
# Author : lixingyun
import sys

sys.path.append('..')
from peewee import *
from common.db.config import DB_CONFIG

database = MySQLDatabase('hm_user', **DB_CONFIG)


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class UserName(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username'


class Userbase(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase'
        primary_key = False


class Userinfo(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo'