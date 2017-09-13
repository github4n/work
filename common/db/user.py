#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/13 19:57
# Author : lixingyun

from peewee import *

database = MySQLDatabase('hm_user', **{'user': 'huomao', 'host': '10.10.23.15', 'password': 'huomao'})

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
