#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 16:52
# Author : lixingyun
# Description :
import time
from peewee import fn
from .db.user_bag import UserBag


class Bag():
    # 添加弹幕卡
    @staticmethod
    def add_dmk(uid, add_time=int(time.time()), expire_time=int(time.time()) + 10000, num=1):
        UserBag.create(uid=uid, get_way='admin_33', bag=100001, add_time=add_time, expire_time=expire_time, num=num, type=2, total=num)
        return

    # 获取弹幕卡
    @staticmethod
    def get_dmk(uid):
        u = UserBag.select(fn.Sum(UserBag.num)).where(
            (UserBag.uid == uid) & (UserBag.bag == 100001)).first()
        return u.num

    # 获取用户特定时间弹幕卡数量
    @staticmethod
    def get_time_dmk(uid, dmk_time):
        u = UserBag.select(fn.Sum(UserBag.num)).where((UserBag.uid == uid) & (UserBag.expire_time == dmk_time)).first()
        return u.num

    # 删除弹幕卡
    @staticmethod
    def del_dmk(uid):
        UserBag.delete().where(UserBag.uid == uid).execute()