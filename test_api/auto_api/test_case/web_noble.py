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

    # 二次验证方法开通
    def validate(self):
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

        def _ver():
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

        return _ver

    # 二次验证方法续费
    def validate_renew(self):
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

        def _ver():
            if not to_uid:
                # 普通模式
                # 判断猫币
                coin1 = MoneyClass.get_money(uid)['coin']
                if coin != coin1 + noble_data[level][1] * month:
                    logging.error('普通-猫币错误{}:{}'.format(coin, coin1))
                    return False
                # 判断贵族猫币
                noble_coin1 = MoneyClass.get_noble_coin(uid)
                if noble_coin != noble_coin1:
                    logging.error('普通-贵族猫币错误{}:{}'.format(noble_coin, noble_coin1))
                    return False
                # 判断平台经验
                exp1 = User.get_experience(uid)[0]
                if exp != exp1:
                    logging.error('普通-平台经验错误{}:{}'.format(exp, exp1))
                    return False
                # 判断主播提成
                profit = User.find_noble_anchor_profit(uid, noble_data[level][1] * month)
                if profit:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            else:
                # 赠送模式
                # 判断增送者猫币
                coin1 = MoneyClass.get_money(uid)['coin']
                if coin != coin1 + noble_data[level][1] * month:
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
                if to_uid_noble_coin != noble_coin2:
                    logging.error('被赠送者贵族猫币错误{}:{}'.format(to_uid_noble_coin, noble_coin2))
                    return False
                # 判断被赠送者平台经验
                exp2 = User.get_experience(to_uid)[0]
                if to_uid_exp != exp2:
                    logging.error('被赠送者平台经验错误{}:{}'.format(to_uid_exp, exp2))
                    return False
                # 判断主播提成
                profit = User.find_noble_anchor_profit(to_uid, noble_data[level][1] * month)
                if profit:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            return True

        return _ver

    # 二次验证方法升级
    def validate_upgrade(self):
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
        old_level = self.old_level
        old_month = self.old_month
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

        def _ver():
            if not to_uid:
                # 普通模式
                # 判断猫币
                coin1 = MoneyClass.get_money(uid)['coin']
                pay_money = noble_data[level][0] * 1 + noble_data[level][1] * (month - 1)
                if coin != coin1 + pay_money:
                    logging.error('普通-猫币错误{}:{}:{}'.format(coin, coin1, pay_money))
                    return False
                # 判断贵族猫币  返还第一个月和之前月份未给的
                noble_coin1 = MoneyClass.get_noble_coin(uid)
                if noble_coin != noble_coin1 - noble_data[level][2] - noble_data[old_level][2] * (old_month - 1):
                    logging.error('普通-贵族猫币错误{}:{}'.format(noble_coin, noble_coin1))
                    return False
                # 判断平台经验 返还第一个月和之前月份未给的
                exp1 = User.get_experience(uid)[0]
                if exp != exp1 - noble_data[level][4] - noble_data[old_level][4] * (old_month - 1):
                    logging.error('普通-平台经验错误{}:{}'.format(exp, exp1))
                    return False
                # 判断主播提成
                profit = User.find_noble_anchor_profit(uid, pay_money)
                if profit != noble_data[level][3]:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            else:
                # 赠送模式
                # 判断增送者猫币
                coin1 = MoneyClass.get_money(uid)['coin']
                if coin != coin1 + noble_data[level][1] * month:
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
                if to_uid_noble_coin != noble_coin2:
                    logging.error('被赠送者贵族猫币错误{}:{}'.format(to_uid_noble_coin, noble_coin2))
                    return False
                # 判断被赠送者平台经验
                exp2 = User.get_experience(to_uid)[0]
                if to_uid_exp != exp2:
                    logging.error('被赠送者平台经验错误{}:{}'.format(to_uid_exp, exp2))
                    return False
                # 判断主播提成
                profit = User.find_noble_anchor_profit(to_uid, noble_data[level][1] * month)
                if profit != noble_data[level][3]:
                    logging.error('普通-主播提成错误{}'.format(profit))
                    return False
            return True

        return _ver

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
        User.create_noble(self.user, level=1)
        self.data['level'] = 1
        self.ver = self.validate_renew()

    def test_2_2(self):
        '''已1级1个月被赠送1级1个月--相当于续费'''
        # 赠送者
        self.user = self.create_user()
        # 被赠送者
        self.data['to_uid'] = self.create_user()
        User.create_noble(self.data['to_uid'], level=1)
        self.data['level'] = 1
        self.data['type'] = 2
        self.ver = self.validate_renew()

    def test_2_3(self):
        '''已1级1个月开通2级2个月--相当于升级'''
        self.user = self.create_user()
        User.create_noble(self.user, level=1)
        self.data['level'] = 2
        self.data['month'] = 2
        self.ver = self.validate_upgrade()

    def test_2_66(self):
        '''已2级2个月开通4级4个月--相当于升级'''
        self.user = self.create_user()
        self.old_level = 2
        self.old_month = 2
        User.create_noble(self.user, level=self.old_level, month=self.old_month)
        self.data['level'] = 4
        self.data['month'] = 4
        self.ver = self.validate_upgrade()

    def tearDown(self):
        # 比较结果
        assert_res(self)
