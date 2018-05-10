#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/4/17 17:53
# Author : lixingyun
# Description : 测试贵族功能 不验证每月返还功能

import time
import requests
import logging
import unittest
from huomao.money import MoneyClass
from huomao.user import User
from ..lib.lib import assert_res
from ..lib.config import domain_web


class TestNoble(unittest.TestCase):
    # 创建用户
    def create_user(self):
        user = User()
        uid = user.reg()
        logging.info('注册用户UID：{}'.format(uid))
        user.bd_sj(uid)
        MoneyClass.set_money(uid, 9000000)
        return uid

    # 二次验证方法创建，续费，升级
    def validate(self, _type='create'):
        # 贵族等级：开通价格0，续费价格1，返还猫币2，主播提成3，增加经验4
        noble_data = {
            1: [66, 30, 30, 13.2, 0],
            2: [500, 300, 300, 100, 1000],
            3: [1500, 1000, 1000, 300, 3000],
            4: [5000, 3000, 3000, 1000, 7500],
            5: [15000, 10000, 10000, 3000, 15000],
            6: [40000, 30000, 30000, 6000, 20000],
            7: [120000, 100000, 100000, 12000, 30000]
        }
        level = self.data['level']
        month = self.data['month']
        old_level = self.old_level if hasattr(self, 'old_level') else False
        old_month = self.old_month if hasattr(self, 'old_month') else False
        # 获取用户的猫币，贵族猫币，平台经验
        uid = self.user
        coin = MoneyClass.get_money(self.user)['coin']
        noble_coin = MoneyClass.get_noble_coin(self.user)
        exp = User.get_experience(self.user)[0]
        # 获取被赠送者的猫币，贵族猫币，平台经验
        to_uid = self.data['to_uid']
        if to_uid:
            to_uid_coin = MoneyClass.get_money(to_uid)['coin']
            to_uid_noble_coin = MoneyClass.get_noble_coin(to_uid)
            to_uid_exp = User.get_experience(to_uid)[0]

        def _ver_create():
            if not to_uid:
                # 普通模式
                # 判断猫币
                coin1 = MoneyClass.get_money(uid)['coin']
                if coin != coin1 + noble_data[level][0] * 1 + noble_data[level][1] * (month - 1):
                    logging.error('普通-猫币错误{}:{}'.format(coin, coin1))
                    return False
                # 判断贵族猫币
                noble_coin1 = MoneyClass.get_noble_coin(uid)
                if noble_coin != noble_coin1 - noble_data[level][2]:
                    logging.error('普通-贵族猫币错误{}:{}'.format(noble_coin, noble_coin1))
                    return False
                # 判断平台经验
                exp1 = User.get_experience(uid)[0]
                if exp != exp1 - noble_data[level][4]:
                    logging.error('普通-平台经验错误{}:{}'.format(exp, exp1))
                    return False
                # 判断主播提成
                profit = User.find_noble_anchor_profit(uid)
                if profit != noble_data[level][3]:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            else:
                # 赠送模式
                # 判断增送者猫币
                coin1 = MoneyClass.get_money(uid)['coin']
                if coin != coin1 + noble_data[level][0] * 1 + noble_data[level][1] * (month - 1):
                    logging.error('赠送者猫币错误{}:{}'.format(coin, coin1))
                    return False
                # 判断赠送者贵族猫币
                noble_coin1 = MoneyClass.get_noble_coin(uid)
                if noble_coin != noble_coin1:
                    logging.error('赠送者贵族猫币错误{}:{}'.format(noble_coin, noble_coin1))
                    return False
                # 判断赠送者平台经验
                exp1 = User.get_experience(uid)[0]
                if exp != exp1:
                    logging.error('赠送者平台经验错误{}:{}'.format(exp, exp1))
                    return False
                # 判断被增送者猫币
                coin2 = MoneyClass.get_money(to_uid)['coin']
                if to_uid_coin != coin2:
                    logging.error('被赠送者猫币错误{}:{}'.format(to_uid_coin, coin2))
                    return False
                # 判断被赠送者贵族猫币
                noble_coin2 = MoneyClass.get_noble_coin(to_uid)
                if to_uid_noble_coin != noble_coin2 - noble_data[level][2]:
                    logging.error('被赠送者贵族猫币错误{}:{}'.format(to_uid_noble_coin, noble_coin2))
                    return False
                # 判断被赠送者平台经验
                exp2 = User.get_experience(to_uid)[0]
                if to_uid_exp != exp2 - noble_data[level][4]:
                    logging.error('被赠送者平台经验错误{}:{}'.format(to_uid_exp, exp2))
                    return False
                # 判断主播提成
                profit = User.find_noble_anchor_profit(to_uid)
                if profit != noble_data[level][3]:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            return True

        def _ver_renew():
            if not to_uid:
                # 普通模式
                # 判断猫币-续费只花费折扣价格
                coin1 = MoneyClass.get_money(uid)['coin']
                if coin != coin1 + noble_data[level][1] * month:
                    logging.error('普通-猫币错误{}:{}'.format(coin, coin1))
                    return False
                # 判断贵族猫币-续费不获得贵族猫币
                noble_coin1 = MoneyClass.get_noble_coin(uid)
                if noble_coin != noble_coin1:
                    logging.error('普通-贵族猫币错误{}:{}'.format(noble_coin, noble_coin1))
                    return False
                # 判断平台经验-续费不获得平台经验
                exp1 = User.get_experience(uid)[0]
                if exp != exp1:
                    logging.error('普通-平台经验错误{}:{}'.format(exp, exp1))
                    return False
                # 判断主播提成-续费不获得主播提成
                profit = User.find_noble_anchor_profit(uid, noble_data[level][1] * month)
                if profit:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            else:
                # 赠送模式
                # 判断增送者猫币-续费只花费折扣价格
                coin1 = MoneyClass.get_money(uid)['coin']
                if coin != coin1 + noble_data[level][1] * month:
                    logging.error('赠送者猫币错误{}:{}'.format(coin, coin1))
                    return False
                # 判断赠送者贵族猫币-续费不获得贵族猫币
                noble_coin1 = MoneyClass.get_noble_coin(uid)
                if noble_coin != noble_coin1:
                    logging.error('赠送者贵族猫币错误{}:{}'.format(noble_coin, noble_coin1))
                    return False
                # 判断赠送者平台经验-续费不获得平台经验
                exp1 = User.get_experience(uid)[0]
                if exp != exp1:
                    logging.error('赠送者平台经验错误{}:{}'.format(exp, exp1))
                    return False
                # 判断被增送者猫币-续费不获得猫币
                coin2 = MoneyClass.get_money(to_uid)['coin']
                if to_uid_coin != coin2:
                    logging.error('被赠送者猫币错误{}:{}'.format(to_uid_coin, coin2))
                    return False
                # 判断被赠送者贵族猫币-续费不获得贵族猫币
                noble_coin2 = MoneyClass.get_noble_coin(to_uid)
                if to_uid_noble_coin != noble_coin2:
                    logging.error('被赠送者贵族猫币错误{}:{}'.format(to_uid_noble_coin, noble_coin2))
                    return False
                # 判断被赠送者平台经验-续费不获得平台经验
                exp2 = User.get_experience(to_uid)[0]
                if to_uid_exp != exp2:
                    logging.error('被赠送者平台经验错误{}:{}'.format(to_uid_exp, exp2))
                    return False
                # 判断主播提成-续费不获得主播提成
                profit = User.find_noble_anchor_profit(to_uid, noble_data[level][1] * month)
                if profit:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            return True

        def _ver_upgrade():
            if not to_uid:
                # 普通模式
                # 判断猫币 - 相当于重新购买
                coin1 = MoneyClass.get_money(uid)['coin']
                pay_money = noble_data[level][0] * 1 + noble_data[level][1] * (month - 1)
                if coin != coin1 + pay_money:
                    logging.error('普通-猫币错误{}:{}:{}'.format(coin, coin1, pay_money))
                    return False
                # 判断贵族猫币-返还第一个月和之前月份未给的
                noble_coin1 = MoneyClass.get_noble_coin(uid)
                if noble_coin != noble_coin1 - noble_data[level][2] - noble_data[old_level][2] * (old_month - 1):
                    logging.error('普通-贵族猫币错误{}:{}'.format(noble_coin, noble_coin1))
                    return False
                # 判断平台经验 返还第一个月和之前月份未给的
                exp1 = User.get_experience(uid)[0]
                if exp != exp1 - noble_data[level][4] - noble_data[old_level][4] * (old_month - 1):
                    logging.error('普通-平台经验错误{}:{}'.format(exp, exp1))
                    return False
                # 判断主播提成-返还一个月
                profit = User.find_noble_anchor_profit(uid, pay_money)
                if profit != noble_data[level][3]:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            else:
                # 赠送模式
                # 判断增送者猫币- 相当于重新购买
                coin1 = MoneyClass.get_money(uid)['coin']
                pay_money = noble_data[level][0] * 1 + noble_data[level][1] * (month - 1)
                if coin != coin1 + pay_money:
                    logging.error('赠送者猫币错误{}:{}:{}'.format(coin, coin1, pay_money))
                    return False
                # 判断赠送者贵族猫币 - 不变
                noble_coin1 = MoneyClass.get_noble_coin(uid)
                if noble_coin != noble_coin1:
                    logging.error('赠送者贵族猫币错误{}:{}'.format(noble_coin, noble_coin1))
                    return False
                # 判断赠送者平台经验 - 不变
                exp1 = User.get_experience(uid)[0]
                if exp != exp1:
                    logging.error('赠送者平台经验错误{}:{}'.format(exp, exp1))
                    return False
                # 判断被增送者猫币-不变
                coin2 = MoneyClass.get_money(to_uid)['coin']
                if to_uid_coin != coin2:
                    logging.error('被赠送者猫币错误{}:{}'.format(to_uid_coin, coin2))
                    return False
                # 判断被赠送者贵族猫币-返还第一个月和之前月份未给的
                noble_coin2 = MoneyClass.get_noble_coin(to_uid)
                if to_uid_noble_coin != noble_coin2 - noble_data[level][2] - noble_data[old_level][2] * (old_month - 1):
                    logging.error('被赠送者贵族猫币错误{}:{}'.format(to_uid_noble_coin, noble_coin2))
                    return False
                # 判断被赠送者平台经验-返还第一个月和之前月份未给的
                exp2 = User.get_experience(to_uid)[0]
                if to_uid_exp != exp2 - noble_data[level][4] - noble_data[old_level][4] * (old_month - 1):
                    logging.error('被赠送者平台经验错误{}:{}'.format(to_uid_exp, exp2))
                    return False
                # 判断主播提成-返还一个月
                profit = User.find_noble_anchor_profit(to_uid, pay_money)
                if profit != noble_data[level][3]:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            return True

        def _ver_protect_create():
            if not to_uid:
                # 普通模式
                # 判断猫币-续费保护期只花费折扣价格
                coin1 = MoneyClass.get_money(uid)['coin']
                if coin != coin1 + noble_data[level][1] * month:
                    logging.error('普通-猫币错误{}:{}'.format(coin, coin1))
                    return False
                # 判断贵族猫币-续费保护期获得首月贵族猫币
                noble_coin1 = MoneyClass.get_noble_coin(uid)
                if noble_coin != noble_coin1 - noble_data[level][2]:
                    logging.error('普通-贵族猫币错误{}:{}'.format(noble_coin, noble_coin1))
                    return False
                # 判断平台经验-续费保护期获得首月平台经验
                exp1 = User.get_experience(uid)[0]
                if exp != exp1 - noble_data[level][4]:
                    logging.error('普通-平台经验错误{}:{}'.format(exp, exp1))
                    return False
                # 判断主播提成-续费保护期不获得主播提成
                profit = User.find_noble_anchor_profit(uid, noble_data[level][1] * month)
                if profit:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            else:
                # 赠送模式
                # 判断增送者猫币-续费保护期只花费折扣价格
                coin1 = MoneyClass.get_money(uid)['coin']
                if coin != coin1 + noble_data[level][1] * month:
                    logging.error('赠送者猫币错误{}:{}'.format(coin, coin1))
                    return False
                # 判断赠送者贵族猫币-续费不获得贵族猫币
                noble_coin1 = MoneyClass.get_noble_coin(uid)
                if noble_coin != noble_coin1:
                    logging.error('赠送者贵族猫币错误{}:{}'.format(noble_coin, noble_coin1))
                    return False
                # 判断赠送者平台经验-续费不获得平台经验
                exp1 = User.get_experience(uid)[0]
                if exp != exp1:
                    logging.error('赠送者平台经验错误{}:{}'.format(exp, exp1))
                    return False
                # 判断被增送者猫币-续费不获得猫币
                coin2 = MoneyClass.get_money(to_uid)['coin']
                if to_uid_coin != coin2:
                    logging.error('被赠送者猫币错误{}:{}'.format(to_uid_coin, coin2))
                    return False
                # 判断被赠送者贵族猫币-续费保护期获得首月贵族猫币
                noble_coin2 = MoneyClass.get_noble_coin(to_uid)
                if to_uid_noble_coin != noble_coin2 - noble_data[level][2]:
                    logging.error('被赠送者贵族猫币错误{}:{}'.format(to_uid_noble_coin, noble_coin2))
                    return False
                # 判断被赠送者平台经验-续费保护期获得首月平台经验
                exp2 = User.get_experience(to_uid)[0]
                if to_uid_exp != exp2 - noble_data[level][4]:
                    logging.error('被赠送者平台经验错误{}:{}'.format(to_uid_exp, exp2))
                    return False
                # 判断主播提成-续费不获得主播提成
                profit = User.find_noble_anchor_profit(to_uid, noble_data[level][1] * month)
                if profit:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            return True

        if _type == 'create':
            return _ver_create
        elif _type == 'renew':
            return _ver_renew
        elif _type == 'upgrade':
            return _ver_upgrade
        elif _type == 'protect_create':
            return _ver_protect_create
        else:
            return False

    def setUp(self):
        # 接口信息
        self.name = '贵族'
        self.method = 'get'
        # 默认请求数据 type:0体验1充值2赠送
        self.data = dict(level=1, cid=2, month=1, type=1, to_uid='')
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
        self.exp_res = {'data': '', 'code': 201, 'msg': 'month不存在'}

    def test_0_7(self):
        '''参数必填检验-month参数'''
        self.user = 1522
        self.data['month'] = 0
        self.exp_res = {'data': '', 'code': 201, 'msg': 'month不存在'}

    def test_0_8(self):
        '''参数必填检验-month参数'''
        self.user = 1522
        self.data['month'] = -1
        self.exp_res = {'data': '', 'code': 201, 'msg': 'month不存在'}

    def test_0_9(self):
        '''参数必填检验-month参数'''
        self.user = 1522
        self.data['month'] = 13
        self.exp_res = {'data': '', 'code': 201, 'msg': 'month不存在'}

    def test_0_10(self):
        '''参数必填检验-type参数'''
        self.user = 1522
        self.data.pop('type')
        self.exp_res = {'code': 201, 'msg': 'type不存在', 'data': ''}

    '''用户首次开通贵族'''

    def test_1_1(self):
        '''1级1个月'''
        self.user = self.create_user()
        self.data['level'] = 1
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
        self.ver = self.validate()

    def test_1_2(self):
        '''被赠送1级1个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 1
        self.data['type'] = 2
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
        self.ver = self.validate()

    def test_1_3(self):
        '''2级2个月'''
        self.user = self.create_user()
        self.data['level'] = 2
        self.data['month'] = 2
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
        self.ver = self.validate()

    def test_1_4(self):
        '''被赠送2级2个月'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送着
        self.data['to_uid'] = self.create_user()
        self.data['level'] = 2
        self.data['month'] = 2
        self.data['type'] = 2
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
        self.ver = self.validate()

    def test_1_5(self):
        '''3级3个月'''
        self.user = self.create_user()
        self.data['level'] = 3
        self.data['month'] = 3
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
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
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
        self.ver = self.validate()

    def test_1_7(self):
        '''4级6个月'''
        self.user = self.create_user()
        self.data['level'] = 4
        self.data['month'] = 6
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
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
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
        self.ver = self.validate()

    def test_1_9(self):
        '''5级9个月'''
        self.user = self.create_user()
        self.data['level'] = 5
        self.data['month'] = 9
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
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
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
        self.ver = self.validate()

    def test_1_11(self):
        '''6级12个月'''
        self.user = self.create_user()
        self.data['level'] = 6
        self.data['month'] = 12
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
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
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
        self.ver = self.validate()

    def test_1_13(self):
        '''7级5个月'''
        self.user = self.create_user()
        self.data['level'] = 7
        self.data['month'] = 5
        self.exp_res = {'code': 200, 'data': None, 'msg': '成功'}
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
        self.data['level'] = 7
        self.data['month'] = 10
        self.data['type'] = 2
        self.ver = self.validate('protect_create')

    '''用户开通过已过保护期'''

    def test_4_1(self):
        '''用户2级在已过保护期开通1级1月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=2)
        User.set_noble_expire(self.user, False)
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
        self.data['level'] = 1
        self.data['month'] = 1
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_3(self):
        '''用户3级已过保护期开通3级3月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=3)
        User.set_noble_expire(self.user)
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
        self.data['level'] = 3
        self.data['month'] = 3
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_5(self):
        '''用4级已过保护期开通5级6月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=4)
        User.set_noble_expire(self.user)
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
        self.data['level'] = 5
        self.data['month'] = 6
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_7(self):
        '''用5级已过保护期开通2级6月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=5)
        User.set_noble_expire(self.user)
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
        self.data['level'] = 2
        self.data['month'] = 6
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_9(self):
        '''用6级已过保护期开通7级2月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=6)
        User.set_noble_expire(self.user)
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
        self.data['level'] = 7
        self.data['month'] = 2
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_11(self):
        '''用7级已过保护期开通7级1月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=7)
        User.set_noble_expire(self.user)
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
        self.data['level'] = 7
        self.data['month'] = 1
        self.data['type'] = 2
        self.ver = self.validate('create')

    def test_4_13(self):
        '''用1级已过保护期开通7级10月'''
        self.user = self.create_user()
        User.create_noble(self.user, level=1)
        User.set_noble_expire(self.user)
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
        self.data['level'] = 7
        self.data['month'] = 10
        self.data['type'] = 2
        self.ver = self.validate('create')

    def tearDown(self):
        # 比较结果
        assert_res(self)
