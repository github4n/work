#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/4/17 17:53
# Author : lixingyun
# Description : 测试贵族功能 不验证每月返还功能,未测试已折扣月份升级，续费

import time
import requests
import logging
from nose_parameterized import parameterized
import unittest
from huomao.money import MoneyClass
from huomao.user import User
from huomao.bag import Bag
from ..lib.lib import req
from ..lib.config import domain_web
from decimal import *


def new_name_func(func, num, p):
    return func.__name__ + '_' + str(num + 1)


# 用户状态，原月数，原等级，是否赠送，折扣，开通月数，开通等级
cases = [
    ('first', 0, 0, 0, 0, 1, 1),
    ('first', 0, 0, 0, 1, 1, 1),
    ('first', 0, 0, 1, 0, 1, 1),
    ('first', 0, 0, 1, 1, 1, 1),
    ('first', 0, 0, 0, 0, 2, 2),
    ('first', 0, 0, 0, 1, 2, 2),
    ('first', 0, 0, 1, 0, 2, 2),
    ('first', 0, 0, 1, 1, 2, 2),
    # ('unexpired', 1, 2),
    # ('expired_protect', 1, 2),
    # ('expired', 1, 2),
]


class TestNoble(unittest.TestCase):
    # 创建用户
    def create_user(self):
        uid = User.reg('noble')
        logging.info('注册用户UID：{}'.format(uid))
        User.bd_sj(uid)
        MoneyClass.set_money(uid, 9000000)
        return uid

    # 二次验证方法创建，续费，升级
    def validate(self, _type='create'):
        discount = self.discount and Decimal(str(self.discount)) or 1
        print(discount)
        # 贵族等级：开通价格0，续费价格1，返还猫币2，主播提成3，增加经验4
        noble_data = {
            1: [66, 30, 30, Decimal('13.2'), 0],
            2: [500, 300, 300, 100, 1000],
            3: [1500, 1000, 1000, 300, 3000],
            4: [5000, 3000, 3000, 1000, 7500],
            5: [15000, 10000, 10000, 3000, 15000],
            6: [40000, 30000, 30000, 6000, 20000],
            7: [120000, 100000, 100000, 12000, 30000]
        }
        level = self.data['level']
        month = self.data['month']
        old_level = hasattr(self, 'old_level') and self.old_level
        old_month = hasattr(self, 'old_month') and self.old_month
        # 获取赠送者用户的猫币，贵族猫币，平台经验
        buyer_uid = self.user
        buyer_coin = MoneyClass.get_money(buyer_uid)['coin']
        buyer_noble_coin = MoneyClass.get_noble_coin(buyer_uid)
        buyer_exp = User.get_experience(buyer_uid)[0]

        # 获取被赠送者的猫币，贵族猫币，平台经验
        to_uid = self.data.get('to_uid')
        if to_uid:
            to_uid_coin = MoneyClass.get_money(to_uid)['coin']
            to_uid_noble_coin = MoneyClass.get_noble_coin(to_uid)
            to_uid_exp = User.get_experience(to_uid)[0]

        def _ver():
            noble_profit = get_noble_exp = get_noble_money = pay_money = False
            if to_uid:
                # 赠送模式
                # 判断增送者猫币
                buyer_coin_new = MoneyClass.get_money(buyer_uid)['coin']
                if _type == 'create' or _type == 'upgrade':
                    # 开通/升级 首月原价,其他优惠价
                    pay_money = (noble_data[level][0] * 1 + noble_data[level][1] * (month - 1)) * discount
                elif _type == 'renew' or _type == 'protect_create':
                    # 续费/续费保护期购买 只花费折扣价格
                    pay_money = noble_data[level][1] * month * discount
                if buyer_coin != buyer_coin_new + pay_money:
                    logging.error('赠送者-猫币错误{}:{}'.format(buyer_coin, buyer_coin_new))
                    return False
                # 判断赠送者贵族猫币
                buyer_noble_coin_new = MoneyClass.get_noble_coin(buyer_uid)
                if buyer_noble_coin != buyer_noble_coin_new:
                    logging.error('赠送者贵族猫币错误{}:{}'.format(buyer_noble_coin, buyer_noble_coin_new))
                    return False
                # 判断赠送者平台经验
                buyer_exp_new = User.get_experience(buyer_uid)[0]
                if buyer_exp != buyer_exp_new:
                    logging.error('赠送者平台经验错误{}:{}'.format(buyer_exp, buyer_exp_new))
                    return False
                # 判断被增送者猫币
                to_uid_coin_new = MoneyClass.get_money(to_uid)['coin']
                if to_uid_coin != to_uid_coin_new:
                    logging.error('被赠送者猫币错误{}:{}'.format(to_uid_coin, to_uid_coin_new))
                    return False
                # 判断被增送贵族猫币
                to_uid_noble_coin_new = MoneyClass.get_noble_coin(to_uid)
                if _type == 'create' or _type == 'protect_create':
                    # 开通/续费保护期 获得一个月
                    get_noble_money = noble_data[level][2] * discount
                elif _type == 'renew':
                    # 续费 不获得
                    get_noble_money = 0
                elif _type == 'upgrade':
                    # 返还第一个月和之前月份未给的
                    get_noble_money = noble_data[level][2] * discount + noble_data[old_level][2] * (old_month - 1)
                if to_uid_noble_coin != to_uid_noble_coin_new - get_noble_money:
                    logging.error('被赠送者贵族猫币错误{}:{}'.format(to_uid_noble_coin, to_uid_noble_coin_new))
                    return False

                # 判断被增送平台经验
                to_uid_exp_new = User.get_experience(to_uid)[0]
                if _type == 'create' or _type == 'protect_create':
                    # 开通/续费保护期购买 获得一个月
                    get_noble_exp = noble_data[level][4] * discount
                elif _type == 'renew':
                    # 续费不获得平台经验
                    get_noble_exp = 0
                elif _type == 'upgrade':
                    # 返还第一个月和之前月份未给的
                    get_noble_exp = noble_data[level][4] * discount + noble_data[old_level][4] * (old_month - 1)
                if to_uid_exp != to_uid_exp_new - get_noble_exp:
                    logging.error('普通-平台经验错误{}:{}'.format(to_uid_exp, to_uid_exp_new))
                    return False

                # 判断主播提成
                profit = User.find_noble_anchor_profit(to_uid, pay_money)
                if _type == 'create' or _type == 'upgrade':
                    # 开通/升级 获得一个月
                    noble_profit = noble_data[level][3] * discount
                elif _type == 'renew' or _type == 'protect_create':
                    # 续费/续费保护期  不获得主播提成
                    noble_profit = 0
                if profit != noble_profit:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            else:
                # 普通模式
                buyer_coin_new = MoneyClass.get_money(buyer_uid)['coin']
                if _type == 'create' or _type == 'upgrade':
                    # 开通/升级 首月原价,其他优惠价
                    pay_money = (noble_data[level][0] * 1 + noble_data[level][1] * (month - 1)) * discount
                elif _type == 'renew' or _type == 'protect_create':
                    # 续费/续费保护期购买 只花费折扣价格
                    pay_money = noble_data[level][1] * month * discount
                if buyer_coin != buyer_coin_new + pay_money:
                    logging.error('普通-猫币错误{}:{}'.format(buyer_coin, buyer_coin_new))
                    return False
                # 判断贵族猫币
                buyer_noble_coin_new = MoneyClass.get_noble_coin(buyer_uid)
                if _type == 'create' or _type == 'protect_create':
                    # 开通/续费保护期购买 获得一个月
                    get_noble_money = noble_data[level][2] * discount
                elif _type == 'renew':
                    # 续费 不获得
                    get_noble_money = 0
                elif _type == 'upgrade':
                    # 返还第一个月和之前月份未给的
                    get_noble_money = noble_data[level][2] * discount + noble_data[old_level][2] * (old_month - 1)
                if buyer_noble_coin != buyer_noble_coin_new - get_noble_money:
                    logging.error('普通-贵族猫币错误{}:{}'.format(buyer_noble_coin, buyer_noble_coin_new))
                    return False
                # 判断平台经验
                buyer_exp_new = User.get_experience(buyer_uid)[0]
                if _type == 'create' or _type == 'protect_create':
                    # 开通/续费保护期购买 获得一个月
                    get_noble_exp = noble_data[level][4] * discount
                elif _type == 'renew':
                    # 续费不获得平台经验
                    get_noble_exp = 0
                elif _type == 'upgrade':
                    # 返还第一个月和之前月份未给的
                    get_noble_exp = noble_data[level][4] * discount + noble_data[old_level][4] * (old_month - 1)
                if buyer_exp != buyer_exp_new - get_noble_exp:
                    logging.error('普通-平台经验错误{}:{}:{}'.format(buyer_exp, buyer_exp_new, get_noble_exp))
                    return False
                # 判断主播提成
                profit = User.find_noble_anchor_profit(buyer_uid, pay_money)
                if _type == 'create' or _type == 'upgrade':
                    # 开通/升级 获得一个月
                    noble_profit = noble_data[level][3] * discount
                elif _type == 'renew' or _type == 'protect_create':
                    # 续费/续费保护期  不获得主播提成
                    noble_profit = 0
                if profit != noble_profit:
                    logging.error('普通-主播提成错误{}:{}'.format(noble_profit, profit))
                    return False
            return True

        return _ver

    def setUp(self):
        # 接口信息
        self.name = '贵族'
        self.method = 'get'
        # 默认请求数据 type:0体验1充值2赠送
        self.data = dict(level=1, cid=14, month=1, type=1, to_uid='')
        self.url = '/noble/createNoble'
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}

    '''参数必填检验'''

    def test_0_1(self):
        '''参数必填检验-未登录'''
        self.user = ''
        self.exp_res = {'code': 201, 'msg': '还没登录', 'data': ''}

    def test_0_2(self):
        '''参数必填检验-level参数'''
        self.user = 1522
        self.data.pop('level')
        self.exp_res = {'msg': 'level不存在', 'code': 201, 'data': ''}

    def test_0_3(self):
        '''参数必填检验-level参数'''
        self.user = 1522
        self.data['level'] = 0
        self.exp_res = {'msg': 'level不存在', 'code': 201, 'data': ''}

    def test_0_4(self):
        '''参数必填检验-level参数'''
        self.user = 1522
        self.data['level'] = 8
        self.exp_res = {'msg': 'level不存在', 'code': 201, 'data': ''}

    def test_0_5(self):
        '''参数必填检验-level参数'''
        self.user = 1522
        self.data['level'] = -1
        self.exp_res = {'msg': 'level不存在', 'code': 201, 'data': ''}

    def test_0_6(self):
        '''参数必填检验-month参数'''
        self.user = 1522
        self.data.pop('month')
        self.exp_res = dict(code=201)

    def test_0_7(self):
        '''参数必填检验-month参数'''
        self.user = 1522
        self.data['month'] = 0
        self.exp_res = dict(code=201)

    def test_0_8(self):
        '''参数必填检验-month参数'''
        self.user = 1522
        self.data['month'] = -1
        self.exp_res = dict(code=201)

    def test_0_9(self):
        '''参数必填检验-month参数'''
        self.user = 1522
        self.data['month'] = 13
        self.exp_res = dict(code=201)

    def test_0_10(self):
        '''参数必填检验-type参数'''
        self.user = 1522
        self.data.pop('type')
        self.exp_res = dict(code=201)

    @parameterized.expand(cases, name_func=new_name_func)
    def test(self, *args):
        if args[0] == 'first':
            # 是否打折
            self.discount = args[-3] and 0.8
            # 开通参数
            self.data['level'] = args[-1]
            self.data['month'] = args[-2]
            # 创建购买用户
            self.user = self.create_user()
            self.discount and Bag.add_bag(self.user, bag=90001)
            # 是否赠送
            if args[3]:
                self.data['to_uid'] = self.create_user()
                self.data['type'] = 2
            # 验证
            self.ver = self.validate()

    '''用户首次开通贵族'''

    def test_1_1(self):
        '''1级1个月'''
        self.user = self.create_user()
        self.data['level'] = 1
        self.ver = self.validate()

    def test_1_1_eight(self):
        '''1级1个月'''
        self.user = self.create_user(True)
        self.data['level'] = 1
        self.ver = self.validate('create', 0.8)

    def test_1_1_give(self):
        '''被赠送1级1个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 1
        self.data['type'] = 2
        self.ver = self.validate()

    def test_1_1_give_eight(self):
        '''被赠送1级1个月'''
        # 赠送者
        self.user = self.create_user(True)
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 1
        self.data['type'] = 2
        self.ver = self.validate('create', 0.8)

    def test_1_2(self):
        '''2级2个月'''
        self.user = self.create_user()
        self.data['level'] = 2
        self.data['month'] = 2
        self.ver = self.validate()

    def test_1_2_eight(self):
        '''2级2个月'''
        self.user = self.create_user(True)
        self.data['level'] = 2
        self.data['month'] = 2
        self.ver = self.validate('create', 0.8)

    def test_1_2_give(self):
        '''被赠送2级2个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 2
        self.data['month'] = 2
        self.data['type'] = 2
        self.ver = self.validate()

    def test_1_2_give_eight(self):
        '''被赠送2级2个月'''
        # 赠送者
        self.user = self.create_user(True)
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 2
        self.data['month'] = 2
        self.data['type'] = 2
        self.ver = self.validate('create', 0.8)

    def test_1_5(self):
        '''3级3个月'''
        self.user = self.create_user()
        self.data['level'] = 3
        self.data['month'] = 3
        self.ver = self.validate()

    def test_1_6(self):
        '''被赠送3级3个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 3
        self.data['month'] = 3
        self.data['type'] = 2
        self.ver = self.validate()

    def test_1_7(self):
        '''4级6个月'''
        self.user = self.create_user()
        self.data['level'] = 4
        self.data['month'] = 6
        self.ver = self.validate()

    def test_1_8(self):
        '''被赠送4级6个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 4
        self.data['month'] = 6
        self.data['type'] = 2
        self.ver = self.validate()

    def test_1_9(self):
        '''5级9个月'''
        self.user = self.create_user()
        self.data['level'] = 5
        self.data['month'] = 9
        self.ver = self.validate()

    def test_1_10(self):
        '''被赠送5级9个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 5
        self.data['month'] = 9
        self.data['type'] = 2
        self.ver = self.validate()

    def test_1_11(self):
        '''6级12个月'''
        self.user = self.create_user()
        self.data['level'] = 6
        self.data['month'] = 12
        self.ver = self.validate()

    def test_1_12(self):
        '''被赠送6级12个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 6
        self.data['month'] = 12
        self.data['type'] = 2
        self.ver = self.validate()

    def test_1_13(self):
        '''7级5个月'''
        self.user = self.create_user()
        self.data['level'] = 7
        self.data['month'] = 5
        self.ver = self.validate()

    def test_1_14(self):
        '''被赠送7级5个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 7
        self.data['month'] = 5
        self.data['type'] = 2
        self.ver = self.validate()

    '''用户已开通未过期'''

    def test_2_1(self):
        '''已1级1个月开通1级1个月--相当于续费'''
        self.user = self.create_user()
        self.old_level = 1
        self.old_month = 1
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 1
        self.ver = self.validate('renew')

    def test_2_2(self):
        '''已1级1个月被赠送1级1个月--相当于续费'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 1
        self.old_month = 1
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 1
        self.data['type'] = 2
        self.ver = self.validate('renew')

    def test_2_3(self):
        '''已1级1个月开通2级2个月--相当于升级'''
        self.user = self.create_user()
        self.old_level = 1
        self.old_month = 1
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 2
        self.data['month'] = 2
        self.ver = self.validate('upgrade')

    def test_2_4(self):
        '''已1级1个月被赠送2级2个月--相当于升级'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 1
        self.old_month = 1
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 2
        self.data['month'] = 2
        self.data['type'] = 2
        self.ver = self.validate('upgrade')

    def test_2_5(self):
        '''已1级1个月开通7级12个月--相当于升级'''
        self.user = self.create_user()
        self.old_level = 1
        self.old_month = 1
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 7
        self.data['month'] = 12
        self.ver = self.validate('upgrade')

    def test_2_6(self):
        '''已1级1个月被赠送7级12个月--相当于升级'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 1
        self.old_month = 1
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 7
        self.data['month'] = 12
        self.data['type'] = 2
        self.ver = self.validate('upgrade')

    def test_2_7(self):
        '''已2级2个月开通1级12个月'''
        self.user = self.create_user()
        self.old_level = 2
        self.old_month = 2
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 1
        self.data['month'] = 12
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_8(self):
        '''已2级2个月被赠送1级12个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 2
        self.old_month = 2
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 1
        self.data['month'] = 12
        self.data['type'] = 2
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_9(self):
        '''已2级2个月开通2级6个月--相当于续费'''
        self.user = self.create_user()
        self.old_level = 2
        self.old_month = 2
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 2
        self.data['month'] = 6
        self.ver = self.validate('renew')

    def test_2_10(self):
        '''已2级2个月被赠送2级6个月--相当于续费'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 2
        self.old_month = 2
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 2
        self.data['month'] = 6
        self.data['type'] = 2
        self.ver = self.validate('renew')

    def test_2_11(self):
        '''已2级3个月开通3级3个月--相当于升级'''
        self.user = self.create_user()
        self.old_level = 2
        self.old_month = 3
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 3
        self.data['month'] = 3
        self.ver = self.validate('upgrade')

    def test_2_12(self):
        '''已2级3个月被赠送3级3个月--相当于升级'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 2
        self.old_month = 3
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 3
        self.data['month'] = 3
        self.data['type'] = 2
        self.ver = self.validate('upgrade')

    def test_2_13(self):
        '''已3级2个月开通2级12个月'''
        self.user = self.create_user()
        self.old_level = 3
        self.old_month = 2
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 2
        self.data['month'] = 12
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_14(self):
        '''已3级2个月被赠送2级12个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 3
        self.old_month = 2
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 2
        self.data['month'] = 12
        self.data['type'] = 2
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_15(self):
        '''已3级2个月开通3级6个月--相当于续费'''
        self.user = self.create_user()
        self.old_level = 3
        self.old_month = 2
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 3
        self.data['month'] = 6
        self.ver = self.validate('renew')

    def test_2_16(self):
        '''已3级2个月被赠送3级6个月--相当于续费'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 3
        self.old_month = 2
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 3
        self.data['month'] = 6
        self.data['type'] = 2
        self.ver = self.validate('renew')

    def test_2_17(self):
        '''已3级3个月开通5级3个月--相当于升级'''
        self.user = self.create_user()
        self.old_level = 3
        self.old_month = 3
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 5
        self.data['month'] = 3
        self.ver = self.validate('upgrade')

    def test_2_18(self):
        '''已3级3个月被赠送5级3个月--相当于升级'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 3
        self.old_month = 3
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 5
        self.data['month'] = 3
        self.data['type'] = 2
        self.ver = self.validate('upgrade')

    def test_2_19(self):
        '''已4级2个月开通3级12个月'''
        self.user = self.create_user()
        self.old_level = 4
        self.old_month = 2
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 3
        self.data['month'] = 12
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_20(self):
        '''已4级2个月被赠送3级12个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 4
        self.old_month = 2
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 3
        self.data['month'] = 12
        self.data['type'] = 2
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_21(self):
        '''已4级4个月开通4级6个月--相当于续费'''
        self.user = self.create_user()
        self.old_level = 4
        self.old_month = 4
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 4
        self.data['month'] = 6
        self.ver = self.validate('renew')

    def test_2_22(self):
        '''已4级4个月被赠送4级6个月--相当于续费'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 4
        self.old_month = 4
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 4
        self.data['month'] = 6
        self.data['type'] = 2
        self.ver = self.validate('renew')

    def test_2_23(self):
        '''已4级3个月开通6级2个月--相当于升级'''
        self.user = self.create_user()
        self.old_level = 4
        self.old_month = 3
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 6
        self.data['month'] = 3
        self.ver = self.validate('upgrade')

    def test_2_24(self):
        '''已4级3个月被赠送6级2个月--相当于升级'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 3
        self.old_month = 3
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 5
        self.data['month'] = 3
        self.data['type'] = 2
        self.ver = self.validate('upgrade')

    def test_2_25(self):
        '''已5级2个月开通3级12个月'''
        self.user = self.create_user()
        self.old_level = 5
        self.old_month = 2
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 3
        self.data['month'] = 12
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_26(self):
        '''已5级2个月被赠送3级12个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 5
        self.old_month = 2
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 3
        self.data['month'] = 12
        self.data['type'] = 2
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_27(self):
        '''已5级4个月开通5级1个月--相当于续费'''
        self.user = self.create_user()
        self.old_level = 5
        self.old_month = 4
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 5
        self.data['month'] = 1
        self.ver = self.validate('renew')

    def test_2_28(self):
        '''已5级4个月被赠送5级1个月--相当于续费'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 5
        self.old_month = 4
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 5
        self.data['month'] = 1
        self.data['type'] = 2
        self.ver = self.validate('renew')

    def test_2_29(self):
        '''已5级3个月开通7级1个月--相当于升级'''
        self.user = self.create_user()
        self.old_level = 5
        self.old_month = 3
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 7
        self.data['month'] = 1
        self.ver = self.validate('upgrade')

    def test_2_30(self):
        '''已5级3个月被赠送7级1个月--相当于升级'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 5
        self.old_month = 3
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 7
        self.data['month'] = 1
        self.data['type'] = 2
        self.ver = self.validate('upgrade')

    def test_2_31(self):
        '''已6级2个月开通2级1个月'''
        self.user = self.create_user()
        self.old_level = 6
        self.old_month = 2
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 2
        self.data['month'] = 1
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_32(self):
        '''已6级2个月被赠送2级1个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 6
        self.old_month = 2
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 2
        self.data['month'] = 1
        self.data['type'] = 2
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_33(self):
        '''已6级4个月开通6级2个月--相当于续费'''
        self.user = self.create_user()
        self.old_level = 6
        self.old_month = 4
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 6
        self.data['month'] = 2
        self.ver = self.validate('renew')

    def test_2_34(self):
        '''已6级4个月被赠送6级2个月--相当于续费'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 6
        self.old_month = 4
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 6
        self.data['month'] = 2
        self.data['type'] = 2
        self.ver = self.validate('renew')

    def test_2_35(self):
        '''已6级3个月开通7级2个月--相当于升级'''
        self.user = self.create_user()
        self.old_level = 6
        self.old_month = 3
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 7
        self.data['month'] = 2
        self.ver = self.validate('upgrade')

    def test_2_36(self):
        '''已6级3个月被赠送7级2个月--相当于升级'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 6
        self.old_month = 3
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 7
        self.data['month'] = 2
        self.data['type'] = 2
        self.ver = self.validate('upgrade')

    def test_2_37(self):
        '''已7级1个月开通6级12个月'''
        self.user = self.create_user()
        self.old_level = 7
        self.old_month = 1
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 6
        self.data['month'] = 12
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_38(self):
        '''已7级1个月被赠送6级12个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 7
        self.old_month = 1
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 6
        self.data['month'] = 12
        self.data['type'] = 2
        self.exp_res = {'code': 201, 'data': '', 'msg': '已经是该贵族了'}

    def test_2_39(self):
        '''已7级4个月开通7级12个月--相当于续费'''
        self.user = self.create_user()
        self.old_level = 7
        self.old_month = 4
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 7
        self.data['month'] = 12
        self.ver = self.validate('renew')

    def test_2_40(self):
        '''已7级4个月被赠送7级12个月--相当于续费'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        self.old_level = 7
        self.old_month = 4
        User.create_noble(self.data['to_uid'], level=self.old_level, month=self.old_month)
        self.data['level'] = 7
        self.data['month'] = 12
        self.data['type'] = 2
        self.ver = self.validate('renew')

    '''用户开通过在保护期'''

    def test_3_1(self):
        '''用户2级在保护期开通1级1月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=2)
        User.set_noble_expire(self.user)
        self.data['level'] = 1
        self.data['month'] = 1
        self.ver = self.validate('protect_create')

    def test_3_2(self):
        '''用户2级在保护期被开通1级1月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=2)
        User.set_noble_expire(self.data['to_uid'])
        self.data['level'] = 1
        self.data['month'] = 1
        self.data['type'] = 2
        self.ver = self.validate('protect_create')

    def test_3_3(self):
        '''用户3级在保护期开通3级3月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=3)
        User.set_noble_expire(self.user)
        self.data['level'] = 3
        self.data['month'] = 3
        self.ver = self.validate('protect_create')

    def test_3_4(self):
        '''用户3级在保护期被开通3级3月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=3)
        User.set_noble_expire(self.data['to_uid'])
        self.data['level'] = 3
        self.data['month'] = 3
        self.data['type'] = 2
        self.ver = self.validate('protect_create')

    def test_3_5(self):
        '''用4级在保护期开通5级6月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=4)
        User.set_noble_expire(self.user)
        self.data['level'] = 5
        self.data['month'] = 6
        self.ver = self.validate('protect_create')

    def test_3_6(self):
        '''用户4级在保护期被开通5级6月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=4)
        User.set_noble_expire(self.data['to_uid'])
        self.data['level'] = 5
        self.data['month'] = 6
        self.data['type'] = 2
        self.ver = self.validate('protect_create')

    def test_3_7(self):
        '''用5级在保护期开通2级6月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=5)
        User.set_noble_expire(self.user)
        self.data['level'] = 2
        self.data['month'] = 6
        self.ver = self.validate('protect_create')

    def test_3_8(self):
        '''用户5级在保护期被开通2级6月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=5)
        User.set_noble_expire(self.data['to_uid'])
        self.data['level'] = 2
        self.data['month'] = 6
        self.data['type'] = 2
        self.ver = self.validate('protect_create')

    def test_3_9(self):
        '''用6级在保护期开通7级2月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=6)
        User.set_noble_expire(self.user)
        self.data['level'] = 7
        self.data['month'] = 2
        self.ver = self.validate('protect_create')

    def test_3_10(self):
        '''用户6级在保护期被开通7级2月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=6)
        User.set_noble_expire(self.data['to_uid'])
        self.data['level'] = 7
        self.data['month'] = 2
        self.data['type'] = 2
        self.ver = self.validate('protect_create')

    def test_3_11(self):
        '''用7级在保护期开通7级1月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=7)
        User.set_noble_expire(self.user)
        self.data['level'] = 7
        self.data['month'] = 1
        self.ver = self.validate('protect_create')

    def test_3_12(self):
        '''用户7级在保护期被开通7级1月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=7)
        User.set_noble_expire(self.data['to_uid'])
        self.data['level'] = 7
        self.data['month'] = 1
        self.data['type'] = 2
        self.ver = self.validate('protect_create')

    def test_3_13(self):
        '''用1级在保护期开通7级10月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=1)
        User.set_noble_expire(self.user)
        self.data['level'] = 7
        self.data['month'] = 10
        self.ver = self.validate('protect_create')

    def test_3_14(self):
        '''用户1级在保护期被开通7级10月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=1)
        User.set_noble_expire(self.data['to_uid'])
        self.data['level'] = 7
        self.data['month'] = 10
        self.data['type'] = 2
        self.ver = self.validate('protect_create')

    '''用户开通过已过保护期'''

    def test_4_1(self):
        '''用户2级在已过保护期开通1级1月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=2)
        User.set_noble_expire(self.user, 50)
        self.data['level'] = 1
        self.data['month'] = 1
        self.ver = self.validate('create')

    def test_4_2(self):
        '''用户2级已过保护期被开通1级1月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=2)
        User.set_noble_expire(self.data['to_uid'], 50)
        self.data['level'] = 1
        self.data['month'] = 1
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_3(self):
        '''用户3级已过保护期开通3级3月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=3)
        User.set_noble_expire(self.user, 50)
        self.data['level'] = 3
        self.data['month'] = 3
        self.ver = self.validate('create')

    def test_4_4(self):
        '''用户3级已过保护期被开通3级3月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=3)
        User.set_noble_expire(self.data['to_uid'], 50)
        self.data['level'] = 3
        self.data['month'] = 3
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_5(self):
        '''用4级已过保护期开通5级6月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=4)
        User.set_noble_expire(self.user, 50)
        self.data['level'] = 5
        self.data['month'] = 6
        self.ver = self.validate('create')

    def test_4_6(self):
        '''用户4级已过保护期被开通5级6月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=4)
        User.set_noble_expire(self.data['to_uid'], 50)
        self.data['level'] = 5
        self.data['month'] = 6
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_7(self):
        '''用5级已过保护期开通2级6月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=5)
        User.set_noble_expire(self.user, 50)
        self.data['level'] = 2
        self.data['month'] = 6
        self.ver = self.validate('create')

    def test_4_8(self):
        '''用户5级已过保护期被开通2级6月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=5)
        User.set_noble_expire(self.data['to_uid'], 50)
        self.data['level'] = 2
        self.data['month'] = 6
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_9(self):
        '''用6级已过保护期开通7级2月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=6)
        User.set_noble_expire(self.user, 50)
        self.data['level'] = 7
        self.data['month'] = 2
        self.ver = self.validate('create')

    def test_4_10(self):
        '''用户6级已过保护期被开通7级2月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=6)
        User.set_noble_expire(self.data['to_uid'], 50)
        self.data['level'] = 7
        self.data['month'] = 2
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_11(self):
        '''用7级已过保护期开通7级1月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=7)
        User.set_noble_expire(self.user, 50)
        self.data['level'] = 7
        self.data['month'] = 1
        self.ver = self.validate('create')

    def test_4_12(self):
        '''用户7级已过保护期被开通7级1月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=7)
        User.set_noble_expire(self.data['to_uid'], 50)
        self.data['level'] = 7
        self.data['month'] = 1
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_13(self):
        '''用1级已过保护期开通7级10月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=1)
        User.set_noble_expire(self.user, 50)
        self.data['level'] = 7
        self.data['month'] = 10
        self.ver = self.validate('create')

    def test_4_14(self):
        '''用户1级已过保护期被开通7级10月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=1)
        User.set_noble_expire(self.data['to_uid'], 50)
        self.data['level'] = 7
        self.data['month'] = 10
        self.data['type'] = 2
        self.ver = self.validate('create')

    def tearDown(self):
        # 比较结果
        req(self)
