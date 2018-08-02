#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 16:52
# Author : lixingyun
# Description :
import time
from peewee import fn
from .db.user_bag import UserBag
from .config import logger_huomao


class Bag():
    # 添加弹幕卡
    @staticmethod
    def add_bag(uid, **kw):
        t = int(time.time())
        add_time = kw.get('add_time', t)
        expire_time = kw.get('expire_time', t + 100000)
        num = kw.get('num', 1)
        bag = kw.get('bag', 100001)
        UserBag.create(uid=uid, get_way='admin_33', bag=bag, add_time=add_time, expire_time=expire_time, num=num, type=2, total=num)
        # time.sleep(10)
        # 线下从库有延迟
        return

    # 获取弹幕卡
    @staticmethod
    def get_dmk(uid):
        # u = UserBag.select(fn.Sum(UserBag.num).alias('nums')).where((UserBag.uid == uid) & (UserBag.bag == 100001)).first()
        u = UserBag.raw(f'/*master*/select sum(num) as nums from user_bag where uid = {uid} and bag_id=100001').execute()
        ret = u.cursor._rows[0][0]
        logger_huomao.info(f'{uid}弹幕卡数量{ret}')
        return ret

    # 获取用户特定时间弹幕卡数量
    @staticmethod
    def get_time_dmk(uid, dmk_time):
        u = UserBag.select(fn.Sum(UserBag.num).alias('nums')).where((UserBag.uid == uid) & (UserBag.expire_time == dmk_time)).first()
        return u.nums

    # 删除弹幕卡
    @staticmethod
    def del_dmk(uid):
        UserBag.delete().where(UserBag.uid == uid).execute()
