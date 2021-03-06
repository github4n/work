#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/4/17 17:53
# Author : lixingyun
# Description : 测试贵族功能 不验证每月返还功能,未测试已折扣月份升级，续费,未测试体验贵族

import time
import requests
import logging
from nose_parameterized import parameterized
import unittest
from huomao.money import MoneyClass
from huomao.user import User
from huomao.bag import Bag
from ..lib.lib import req
from ..lib.config import domain_web, logger_test_api
from decimal import *


def new_name_func(func, num, p):
    return func.__name__ + '_' + str(num + 1)


# 用户状态，原等级,原月数，是否赠送，是否打折，开通等级,开通月数,         体验贵族等级,体验贵族天数
cases_first = [
    # 用户首次开通贵族1
    ('first', 0, 0, 0, 0, 1, 1),
    ('first', 0, 0, 0, 8, 1, 1),
    ('first', 0, 0, 0, {'level': 1, 'discount': 0.1, 'month': 1}, 1, 1),
    ('first', 0, 0, 1, 0, 1, 1),
    ('first', 0, 0, 1, 8, 1, 1),

    ('first', 0, 0, 0, 0, 2, 2),
    ('first', 0, 0, 0, 8, 2, 2),
    ('first', 0, 0, 0, {'level': 2, 'discount': 2, 'month': 2}, 2, 2),
    ('first', 0, 0, 1, 0, 2, 2),
    ('first', 0, 0, 1, 8, 2, 2),

    ('first', 0, 0, 0, 0, 3, 3),
    ('first', 0, 0, 0, 8, 3, 3),
    ('first', 0, 0, 0, {'level': 3, 'discount': 3.2, 'month': 3}, 3, 3),
    ('first', 0, 0, 1, 0, 3, 3),
    ('first', 0, 0, 1, 8, 3, 3),

    ('first', 0, 0, 0, 0, 4, 6),
    ('first', 0, 0, 0, 8, 4, 6),
    ('first', 0, 0, 0, {'level': 4, 'discount': 4, 'month': 6}, 4, 6),
    ('first', 0, 0, 1, 0, 4, 6),
    ('first', 0, 0, 1, 8, 4, 6),

    ('first', 0, 0, 0, 0, 5, 9),
    ('first', 0, 0, 0, 8, 5, 9),
    ('first', 0, 0, 0, {'level': 5, 'discount': 1.5, 'month': 9}, 5, 9),
    ('first', 0, 0, 1, 0, 5, 9),
    ('first', 0, 0, 1, 8, 5, 9),

    ('first', 0, 0, 0, 0, 6, 12),
    ('first', 0, 0, 0, 8, 6, 12),
    ('first', 0, 0, 0, {'level': 6, 'discount': 6, 'month': 12}, 6, 12),
    ('first', 0, 0, 1, 0, 6, 12),
    ('first', 0, 0, 1, 8, 6, 12),

    ('first', 0, 0, 0, 0, 7, 5),
    ('first', 0, 0, 0, 8, 7, 5),
    ('first', 0, 0, 0, {'level': 7, 'discount': 9.9, 'month': 5}, 7, 5),
    ('first', 0, 0, 1, 0, 7, 5),
    ('first', 0, 0, 1, 8, 7, 5),

    # 免开通卡.....
    ('first', 0, 0, 0, {'level': 1, 'discount': 10, 'month': 1, 'card': 90018}, 1, 1),
    ('first', 0, 0, 0, {'level': 4, 'discount': 10, 'month': 1, 'card': 90019}, 4, 1),
    ('first', 0, 0, 0, {'level': 5, 'discount': 10, 'month': 1, 'card': 90020}, 5, 1),

]

cases_unexpired = [

    ('unexpired', 1, 1, 0, {'level': 1, 'discount': 10, 'month': 1, 'card': 90018}, 1, 1),
    ('unexpired', 1, 1, 0, {'level': 4, 'discount': 10, 'month': 1, 'card': 90019}, 4, 1),

    # 用户已开通未过期
    ('unexpired', 1, 1, 0, 0, 1, 1),
    ('unexpired', 1, 1, 0, 8, 1, 1),
    ('unexpired', 1, 1, 0, {'level': 1, 'discount': 0.1, 'month': 1}, 1, 1),
    ('unexpired', 1, 1, 1, 0, 1, 1),
    ('unexpired', 1, 1, 1, 8, 1, 1),

    ('unexpired', 1, 1, 0, 0, 7, 12),
    ('unexpired', 1, 1, 0, 8, 7, 12),
    ('unexpired', 1, 1, 0, {'level': 7, 'discount': 1.1, 'month': 12}, 7, 12),
    ('unexpired', 1, 1, 1, 0, 7, 12),
    ('unexpired', 1, 1, 1, 8, 7, 12),

    ('unexpired', 2, 3, 0, 0, 3, 3),
    ('unexpired', 2, 3, 0, 8, 3, 3),
    ('unexpired', 1, 1, 0, {'level': 3, 'discount': 4.1, 'month': 3}, 3, 3),
    ('unexpired', 2, 3, 1, 0, 3, 3),
    ('unexpired', 2, 3, 1, 8, 3, 3),

    ('unexpired', 3, 2, 0, 0, 2, 12),
    ('unexpired', 3, 2, 0, 8, 2, 12),
    ('unexpired', 3, 2, 0, {'level': 2, 'discount': 5.1, 'month': 12}, 2, 12),
    ('unexpired', 3, 2, 1, 0, 2, 12),
    ('unexpired', 3, 2, 1, 8, 2, 12),

    ('unexpired', 4, 4, 0, 0, 4, 6),
    ('unexpired', 4, 4, 0, 8, 4, 6),
    ('unexpired', 4, 4, 0, {'level': 4, 'discount': 8.1, 'month': 6}, 4, 6),
    ('unexpired', 4, 4, 1, 0, 4, 6),
    ('unexpired', 4, 4, 1, 8, 4, 6),

    ('unexpired', 5, 3, 0, 0, 7, 1),
    ('unexpired', 5, 3, 0, 8, 7, 1),
    ('unexpired', 5, 3, 0, {'level': 7, 'discount': 9.1, 'month': 1}, 7, 1),
    ('unexpired', 5, 3, 1, 0, 7, 1),
    ('unexpired', 5, 3, 1, 8, 7, 1),

    ('unexpired', 6, 3, 0, 0, 5, 2),
    ('unexpired', 6, 3, 0, 8, 5, 2),
    ('unexpired', 6, 3, 0, {'level': 5, 'discount': 9.1, 'month': 2}, 5, 2),
    ('unexpired', 6, 3, 1, 0, 5, 2),
    ('unexpired', 6, 3, 1, 8, 5, 2),

    ('unexpired', 7, 4, 0, 0, 7, 12),
    ('unexpired', 7, 4, 0, 8, 7, 12),
    ('unexpired', 7, 4, 0, {'level': 7, 'discount': 9.1, 'month': 12}, 7, 12),
    ('unexpired', 7, 4, 1, 0, 7, 12),
    ('unexpired', 7, 4, 1, 8, 7, 12),

    ('unexpired', 7, 3, 0, 0, 6, 2),
    ('unexpired', 7, 3, 0, 8, 6, 2),
    ('unexpired', 7, 3, 0, {'level': 6, 'discount': 9.1, 'month': 2}, 6, 2),
    ('unexpired', 7, 3, 1, 0, 6, 2),
    ('unexpired', 7, 3, 1, 8, 6, 2),
]
cases_expired_protect = [
    ('expired_protect', 1, 1, 0, {'level': 1, 'discount': 10, 'month': 1, 'card': 90018}, 1, 1),
    ('expired_protect', 1, 1, 0, {'level': 4, 'discount': 10, 'month': 1, 'card': 90019}, 4, 1),
    # 用户开通过在保护期
    ('expired_protect', 1, 1, 0, 0, 7, 10),
    ('expired_protect', 1, 1, 0, 8, 7, 10),
    ('expired_protect', 1, 1, 0, {'level': 7, 'discount': 0.1, 'month': 10}, 7, 10),
    ('expired_protect', 1, 1, 1, 0, 7, 10),
    ('expired_protect', 1, 1, 1, 8, 7, 10),

    ('expired_protect', 2, 1, 0, 0, 1, 1),
    ('expired_protect', 2, 1, 0, 8, 1, 1),
    ('expired_protect', 2, 1, 0, {'level': 1, 'discount': 1.1, 'month': 1}, 1, 1), # bug
    ('expired_protect', 2, 1, 1, 0, 1, 1),
    ('expired_protect', 2, 1, 1, 8, 1, 1),

    ('expired_protect', 3, 1, 0, 0, 3, 3),
    ('expired_protect', 3, 1, 0, 8, 3, 3),
    ('expired_protect', 3, 1, 0, {'level': 3, 'discount': 2.1, 'month': 3}, 3, 3),
    ('expired_protect', 3, 1, 1, 0, 3, 3),
    ('expired_protect', 3, 1, 1, 8, 3, 3),

    ('expired_protect', 4, 1, 0, 0, 5, 3),
    ('expired_protect', 4, 1, 0, 8, 5, 3),
    ('expired_protect', 4, 1, 0, {'level': 5, 'discount': 5.1, 'month': 3}, 5, 3),
    ('expired_protect', 4, 1, 1, 0, 5, 3),
    ('expired_protect', 4, 1, 1, 8, 5, 3),

    ('expired_protect', 5, 1, 0, 0, 2, 6),
    ('expired_protect', 5, 1, 0, 8, 2, 6),
    ('expired_protect', 5, 1, 0, {'level': 2, 'discount': 6.1, 'month': 6}, 2, 6),
    ('expired_protect', 5, 1, 1, 0, 2, 6),
    ('expired_protect', 5, 1, 1, 8, 2, 6),

    ('expired_protect', 6, 1, 0, 0, 7, 2),
    ('expired_protect', 6, 1, 0, 8, 7, 2),
    ('expired_protect', 6, 1, 0, {'level': 7, 'discount': 7.1, 'month': 2}, 7, 2),
    ('expired_protect', 6, 1, 1, 0, 7, 2),
    ('expired_protect', 6, 1, 1, 8, 7, 2),

    ('expired_protect', 7, 1, 0, 0, 7, 1),
    ('expired_protect', 7, 1, 0, 8, 7, 1),
    ('expired_protect', 7, 1, 0, {'level': 7, 'discount': 8, 'month': 1}, 7, 1),
    ('expired_protect', 7, 1, 1, 0, 7, 1),
    ('expired_protect', 7, 1, 1, 8, 7, 1),

]

cases_expired = [
    ('expired', 1, 1, 0, {'level': 1, 'discount': 10, 'month': 1, 'card': 90018}, 1, 1),
    ('expired', 1, 1, 0, {'level': 4, 'discount': 10, 'month': 1, 'card': 90019}, 4, 1),
    # 用户开通过已过保护期

    ('expired', 1, 1, 0, 0, 7, 10),
    ('expired', 1, 1, 0, 8, 7, 10),
    ('expired', 1, 1, 0, {'level': 7, 'discount': 0.1, 'month': 10}, 7, 10),
    ('expired', 1, 1, 1, 0, 7, 10),
    ('expired', 1, 1, 1, 8, 7, 10),

    ('expired', 2, 1, 0, 0, 1, 1),
    ('expired', 2, 1, 0, 8, 1, 1),
    ('expired', 2, 1, 0, {'level': 1, 'discount': 1.1, 'month': 1}, 1, 1),
    ('expired', 2, 1, 1, 0, 1, 1),
    ('expired', 2, 1, 1, 8, 1, 1),

    ('expired', 3, 1, 0, 0, 3, 3),
    ('expired', 3, 1, 0, 8, 3, 3),
    ('expired', 3, 1, 0, {'level': 3, 'discount': 8.1, 'month': 3}, 3, 3),
    ('expired', 3, 1, 1, 0, 3, 3),
    ('expired', 3, 1, 1, 8, 3, 3),

    ('expired', 4, 1, 0, 0, 5, 3),  # 145
    ('expired', 4, 1, 0, 8, 5, 3),
    ('expired', 4, 1, 0, {'level': 5, 'discount': 9.1, 'month': 3}, 5, 3),
    ('expired', 4, 1, 1, 0, 5, 3),
    ('expired', 4, 1, 1, 8, 5, 3),

    ('expired', 5, 1, 0, 0, 2, 6),  # 149
    ('expired', 5, 1, 0, 8, 2, 6),
    ('expired', 5, 1, 0, {'level': 2, 'discount': 6.1, 'month': 6}, 2, 6),
    ('expired', 5, 1, 1, 0, 2, 6),
    ('expired', 5, 1, 1, 8, 2, 6),

    ('expired', 6, 1, 0, 0, 7, 2),  # 153
    ('expired', 6, 1, 0, 8, 7, 2),
    ('expired', 6, 1, 0, {'level': 7, 'discount': 6.1, 'month': 2}, 7, 2),
    ('expired', 6, 1, 1, 0, 7, 2),
    ('expired', 6, 1, 1, 8, 7, 2),

    ('expired', 7, 1, 0, 0, 7, 1),  # 157
    ('expired', 7, 1, 0, 8, 7, 1),
    ('expired', 7, 1, 0, {'level': 7, 'discount': 1, 'month': 1}, 7, 1),
    ('expired', 7, 1, 1, 0, 7, 1),
    ('expired', 7, 1, 1, 8, 7, 1),

]

cases = cases_first   + cases_unexpired + cases_expired_protect + cases_expired
# cases = cases_expired


class TestNoble(unittest.TestCase):
    # 创建用户
    def create_user(self):
        uid = User.reg('noble')
        logger_test_api.info(f'注册用户UID：{uid}')
        User.bd_sj(uid)
        MoneyClass.set_money(uid, 9000000)
        return uid

    # 二次验证方法创建，续费，升级
    def validate(self, _type='create'):
        # discount = self.discount and Decimal(str(self.discount)) or 1
        discount = isinstance(self.discount, dict) and self.discount['discount'] * 10 / 100 or self.discount * 10 / 100
        # 贵族等级：开通价格0，续费价格1，返还猫币2，主播提成3，增加经验4,喇叭5
        noble_data = {
            1: [66, 30, 30, 13.2, 0, 0],
            2: [500, 300, 300, 100, 50000, 0],
            3: [1500, 1000, 1000, 300, 125000, 0],
            4: [5000, 3000, 3000, 1000, 500000, 5],
            5: [15000, 10000, 10000, 3000, 1250000, 8],
            6: [40000, 30000, 30000, 6000, 2500000, 15],
            7: [120000, 100000, 100000, 12000, 5000000, 30]
        }
        level = isinstance(self.discount, dict) and self.discount['level'] or self.data['level']
        month = isinstance(self.discount, dict) and self.discount['month'] or self.data['month']
        old_level = hasattr(self, 'old_level') and self.old_level
        old_month = hasattr(self, 'old_month') and self.old_month
        # 获取赠送者用户的猫币，贵族猫币，平台经验
        buyer_uid = self.user
        buyer_coin = MoneyClass.get_money(buyer_uid)['coin']
        buyer_noble_coin = MoneyClass.get_noble_coin(buyer_uid)
        buyer_exp = User.get_experience(buyer_uid)[0]
        buyer_lb = Bag.get_dmk(buyer_uid, 90011)

        # 获取被赠送者的猫币，贵族猫币，平台经验
        to_uid = self.data.get('to_uid')
        if to_uid:
            to_uid_coin = MoneyClass.get_money(to_uid)['coin']
            to_uid_noble_coin = MoneyClass.get_noble_coin(to_uid)
            to_uid_exp = User.get_experience(to_uid)[0]
            to_uid_lb = Bag.get_dmk(to_uid, 90011)

        def _ver():
            noble_profit = get_noble_exp = get_noble_money = pay_money = False
            if to_uid:
                # A 赠送模式
                # 1  判断增送者猫币
                buyer_coin_new = MoneyClass.get_money(buyer_uid)['coin']
                if _type == 'create' or _type == 'upgrade' or (_type == 'protect_create' and level != old_level):
                    # 开通/升级 首月原价,其他优惠价
                    pay_money = (noble_data[level][0] * 1 + noble_data[level][1] * (month - 1)) * discount
                elif _type == 'renew' or (_type == 'protect_create' and level == old_level):
                    # 续费/续费保护期购买 只花费折扣价格
                    pay_money = noble_data[level][1] * month * discount
                if buyer_coin != buyer_coin_new + pay_money:
                    logger_test_api.error(f'赠送者-猫币错误{buyer_coin}:{buyer_coin_new}')
                    return False
                # 2 判断赠送者贵族猫币
                buyer_noble_coin_new = MoneyClass.get_noble_coin(buyer_uid)
                if buyer_noble_coin != buyer_noble_coin_new:
                    logger_test_api.error(f'赠送者贵族猫币错误{buyer_noble_coin}:{buyer_noble_coin_new}')
                    return False
                # 3 判断赠送者平台经验
                buyer_exp_new = User.get_experience(buyer_uid)[0]
                if buyer_exp != buyer_exp_new:
                    logger_test_api.error(f'赠送者平台经验错误{buyer_exp}:{buyer_exp_new}')
                    return False
                # 判断赠送者喇叭
                buyer_lb_new = Bag.get_dmk(buyer_uid, 90011)
                if buyer_lb != buyer_lb_new:
                    logger_test_api.error(f'赠送者喇叭错误{buyer_lb}:{buyer_lb_new}')
                    return False
                # 4 判断被增送者猫币
                to_uid_coin_new = MoneyClass.get_money(to_uid)['coin']
                if to_uid_coin != to_uid_coin_new:
                    logger_test_api.error(f'被赠送者猫币错误{to_uid_coin}:{to_uid_coin_new}')
                    return False
                # 5 判断被增送贵族猫币,平台经验,喇叭
                to_uid_noble_coin_new = MoneyClass.get_noble_coin(to_uid)
                to_uid_exp_new = User.get_experience(to_uid)[0]
                to_uid_lb_new = Bag.get_dmk(to_uid, 90011)

                get_noble_money = noble_data[level][2] * discount * month
                get_noble_exp = noble_data[level][4] * discount * month
                get_noble_lb = noble_data[level][5] * month
                # if _type == 'create' or _type == 'protect_create':
                #     # 开通/续费保护期 获得一个月
                #     get_noble_money = noble_data[level][2] * discount
                #     get_noble_exp = noble_data[level][4] * discount
                # elif _type == 'renew':
                #     # 续费 不获得
                #     get_noble_money = 0
                #     get_noble_exp = 0
                # elif _type == 'upgrade':
                #     # 返还第一个月和之前月份未给的
                #     get_noble_money = noble_data[level][2] * discount + noble_data[old_level][2] * (old_month - 1)
                #     get_noble_exp = noble_data[level][4] * discount + noble_data[old_level][4] * (old_month - 1)
                if to_uid_noble_coin != to_uid_noble_coin_new - get_noble_money:
                    logger_test_api.error(f'被赠送者贵族猫币错误{to_uid_noble_coin}:{to_uid_noble_coin_new}')
                    return False
                if to_uid_exp != to_uid_exp_new - get_noble_exp:
                    logger_test_api.error(f'普通-平台经验错误{to_uid_exp}:{to_uid_exp_new}:{get_noble_exp}')
                    return False
                if to_uid_lb != to_uid_lb_new - get_noble_lb:
                    logger_test_api.error(f'普通-喇叭错误{to_uid_lb}!={to_uid_lb_new}-{get_noble_lb}')
                    return False

                # 判断主播提成
                profit = User.find_noble_anchor_profit(to_uid, pay_money)
                if _type == 'create' or _type == 'upgrade' or (_type == 'protect_create' and level != old_level):
                    # 开通/升级 获得一个月
                    noble_profit = noble_data[level][3] * 10 / 10 * discount
                elif _type == 'renew' or (_type == 'protect_create' and level == old_level):
                    # 续费/续费保护期  不获得主播提成
                    noble_profit = 0
                if profit != noble_profit:
                    logger_test_api.error(f'普通-主播提成错误{profit}')
                    return False
            else:
                # B 普通模式
                # 1 判断花费猫币
                buyer_coin_new = MoneyClass.get_money(buyer_uid)['coin']
                if _type == 'create' or _type == 'upgrade' or (_type == 'protect_create' and level != old_level):
                    # 开通/升级/续费保护不同等级 首月原价,其他优惠价
                    pay_money = (noble_data[level][0] * 1 + noble_data[level][1] * (month - 1)) * discount
                elif _type == 'renew' or (_type == 'protect_create' and level == old_level):
                    # 续费/续费保护相同等级购买 只花费折扣价格
                    pay_money = noble_data[level][1] * month * discount
                if buyer_coin != buyer_coin_new + pay_money:
                    logger_test_api.error(f'普通-猫币错误{buyer_coin}:{buyer_coin_new}:{pay_money}')
                    return False
                # 2 判断贵族猫币,平台经验,喇叭数量
                buyer_lb_new = Bag.get_dmk(buyer_uid, 90011)
                buyer_noble_coin_new = MoneyClass.get_noble_coin(buyer_uid)
                buyer_exp_new = User.get_experience(buyer_uid)[0]

                # 新逻辑 开通/续费/升级/续费保护期购买 获得所有
                get_noble_money = noble_data[level][2] * discount * month
                get_noble_exp = noble_data[level][4] * discount * month
                get_noble_lb = noble_data[level][5] * month  # 喇叭不打折

                #   if _type == 'create' or _type == 'protect_create' :
                #     # 开通/续费保护期购买 获得一个月
                #     get_noble_money = noble_data[level][2] * discount
                #     get_noble_exp = noble_data[level][4] * discount
                # elif _type == 'renew':
                #     # 续费 不获得
                #     get_noble_money = 0
                #     get_noble_exp = 0
                # elif _type == 'upgrade':
                #     # 返还第一个月和之前月份未给的
                #     get_noble_money = noble_data[level][2] * discount + noble_data[old_level][2] * (old_month - 1)
                #     get_noble_exp = noble_data[level][4] * discount + noble_data[old_level][4] * (old_month - 1)
                #
                if buyer_noble_coin != buyer_noble_coin_new - get_noble_money:
                    logger_test_api.error(f'普通-贵族猫币错误{buyer_noble_coin}:{buyer_noble_coin_new}')
                    return False

                if buyer_exp != buyer_exp_new - get_noble_exp:
                    logger_test_api.error(f'普通-平台经验错误{buyer_exp}:{buyer_exp_new}:{get_noble_exp}')
                    return False

                if buyer_lb != buyer_lb_new - get_noble_lb:
                    logger_test_api.error(f'普通-喇叭错误{buyer_lb}!={buyer_lb_new}-{get_noble_lb}')
                    return False

                # 3 判断主播提成
                profit = User.find_noble_anchor_profit(buyer_uid, pay_money)
                if _type == 'create' or _type == 'upgrade' or (_type == 'protect_create' and level != old_level):
                    # 开通/升级 获得一个月
                    noble_profit = round(noble_data[level][3] * 10 / 10 * discount, 2)
                elif _type == 'renew' or (_type == 'protect_create' and level == old_level):
                    # 续费/续费保护期  不获得主播提成
                    noble_profit = 0
                if profit != noble_profit:
                    logger_test_api.error(f'普通-主播提成错误{noble_profit}:{profit}')
                    return False

            return True

        return _ver

    def setUp(self):
        # 接口信息
        self.name = '贵族'
        self.method = 'post'
        # 默认请求数据 type:0体验1充值2赠送
        self.data = dict(level=1, cid=14, month=1, type=1, to_uid='')
        self.url = '/noble/createNoble'
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}

    @parameterized.expand(cases, name_func=new_name_func)
    def test(self, *args):
        logger_test_api.info(args)
        # 开通参数
        self.data['month'] = args[-1]
        self.data['level'] = args[-2]
        self.old_level = args[1]
        self.old_month = args[2]
        # 创建购买用户
        self.user = self.create_user()
        # 是否赠送，创建用户贵族
        if args[3]:
            self.data['to_uid'] = self.create_user()
            self.data['type'] = 2
            if args[0] != 'first':
                # 是首次开通,不用预先开通用户贵族
                User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
            if args[0] == 'expired_protect':
                User.set_noble_expire(self.data['to_uid'])
            elif args[0] == 'expired':
                User.set_noble_expire(self.data['to_uid'], 50)
        else:
            if args[0] != 'first':
                User.create_noble(self.user, level=self.old_level, month=self.old_month)
            if args[0] == 'expired_protect':
                User.set_noble_expire(self.user)
            elif args[0] == 'expired':
                User.set_noble_expire(self.user, 50)

        # 通用8折皇帝，国王不打折,指定打折卡,添加打折卡
        self.discount = args[-3]
        if isinstance(self.discount, dict):
            # 添加打折卡
            use_level = self.discount['level']
            discount = self.discount['discount']
            open_month = self.discount['month']
            if discount < 10:
                self.data['card'] = User.add_noble_card(self.user, use_level, discount, open_month)
            else:
                Bag.add_bag(self.user, self.discount['card'])
                self.data['card'] = self.discount['card']
        elif self.discount > 0 and self.data['level'] <= 5:
            Bag.add_bag(self.user, bag=90001)
        else:
            self.discount = 10
        # 验证
        if isinstance(args[4], dict) and args[4].get('card'):
            if self.old_level == self.data['level'] and args[0] == 'unexpired':
                self.exp_res = {'code': 201, 'data': ''}
            else:
                self.ver = self.validate('renew')
        elif args[0] == 'expired_protect':
            self.ver = self.validate('protect_create')
        elif args[0] == 'expired':
            self.ver = self.validate('create')
        elif args[0] == 'unexpired':
            # 验证
            if self.old_level == self.data['level']:
                self.ver = self.validate('renew')
            elif self.old_level < self.data['level']:
                self.ver = self.validate('upgrade')
            else:
                self.exp_res = {'code': 201, 'data': ''}
        else:
            self.ver = self.validate()

    '''参数必填检验'''

    # def test_0_1(self):
    #     '''参数必填检验-未登录'''
    #     self.user = ''
    #     self.exp_res = {'code': 201, 'msg': '还没登录', 'data': ''}
    #
    # def test_0_2(self):
    #     '''参数必填检验-level参数'''
    #     self.user = 1522
    #     self.data.pop('level')
    #     self.exp_res = {'msg': 'level不存在', 'code': 201, 'data': ''}
    #
    # def test_0_3(self):
    #     '''参数必填检验-level参数'''
    #     self.user = 1522
    #     self.data['level'] = 0
    #     self.exp_res = {'msg': 'level不存在', 'code': 201, 'data': ''}
    #
    # def test_0_4(self):
    #     '''参数必填检验-level参数'''
    #     self.user = 1522
    #     self.data['level'] = 8
    #     self.exp_res = {'msg': 'level不存在', 'code': 201, 'data': ''}
    #
    # def test_0_5(self):
    #     '''参数必填检验-level参数'''
    #     self.user = 1522
    #     self.data['level'] = -1
    #     self.exp_res = {'msg': 'level不存在', 'code': 201, 'data': ''}
    #
    # def test_0_6(self):
    #     '''参数必填检验-month参数'''
    #     self.user = 1522
    #     self.data.pop('month')
    #     self.exp_res = dict(code=201)
    #
    # def test_0_7(self):
    #     '''参数必填检验-month参数'''
    #     self.user = 1522
    #     self.data['month'] = 0
    #     self.exp_res = dict(code=201)
    #
    # def test_0_8(self):
    #     '''参数必填检验-month参数'''
    #     self.user = 1522
    #     self.data['month'] = -1
    #     self.exp_res = dict(code=201)
    #
    # def test_0_9(self):
    #     '''参数必填检验-month参数'''
    #     self.user = 1522
    #     self.data['month'] = 13
    #     self.exp_res = dict(code=201)
    #
    # def test_0_10(self):
    #     '''参数必填检验-type参数'''
    #     self.user = 1522
    #     self.data.pop('type')
    #     self.exp_res = dict(code=201)

    def tearDown(self):
        # 比较结果
        req(self)
        # pass
