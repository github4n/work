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
    # 添加道具
    @staticmethod
    def add_bag(uid, bag=2, **kw):
        t = int(time.time())
        add_time = kw.get('add_time', t)
        expire_time = kw.get('expire_time', t + 100000)
        num = kw.get('num', 1)
        if bag in [90002, 90003, 90004, 90005, 90006, 90007, 90008, 90009, 90010, 90012, 90013, 90014, 90015, 90016, 90017]:
            type = 4
        elif bag in [90018, 90019, 90020] or bag // 10000 == 8:
            type = 6
        elif bag == 90011:  # 全站弹幕喇叭
            type = 5
        elif bag == 90001:  # 八折卡
            type = 3
        else:
            type = 1  # 礼物
        UserBag.create(uid=uid, get_way='admin_33', bag=bag, add_time=add_time, expire_time=expire_time, num=num, type=type,
                       total=num)
        # time.sleep(10)
        # 线下从库有延迟
        return

    # 获取弹幕卡
    @staticmethod
    def get_dmk(uid, bag_id=100001):
        # u = UserBag.select(fn.Sum(UserBag.num).alias('nums')).where((UserBag.uid == uid) & (UserBag.bag == 100001)).first()
        u = UserBag.raw(f'/*master*/select sum(num) as nums from user_bag where uid = {uid} and bag_id={bag_id}').execute()
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

    # 获取背包某道具数量
    @staticmethod
    def get_bag(uid, bag_id=100001):
        # u = UserBag.select(fn.Sum(UserBag.num).alias('nums')).where((UserBag.uid == uid) & (UserBag.bag == 100001)).first()
        u = UserBag.raw(f'/*master*/select sum(num) as nums from user_bag where uid = {uid} and bag_id={bag_id}').execute()
        ret = u.cursor._rows[0][0]
        logger_huomao.info(f'{uid}道具数量{ret}')
        return ret
