#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/8/17 9:16
# Author : lixingyun
# python -m pwiz -e mysql -H 10.10.23.15  -u huomao -P huomao  hm_contents > db.py
from peewee import *

database = MySQLDatabase('hm_contents', **{'user': 'huomao', 'password': 'huomao', 'host': '10.10.23.15'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database




