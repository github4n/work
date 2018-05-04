#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/12/29 10:45
# Author : lixingyun
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 18:27:48
# @Author  : lixingyun
# @notice  :
import unittest
import sys
import time
import json

sys.path.append('../')
from lib import assert_res
from huomao.common import Common
from config import super_uid

'''数据准备'''


# Common.generate_room('msg', 1)
# Common.generate_user('msg', 1)
# Common.generate_user('msg', 1, False)
# exit()


class TestGuessUserCreate(unittest.TestCase):
    def setUp(self):
        # 接口信息
        self.name = '用户创建盘口'
        self.url = '/guessnew/create'
        self.method = 'post'
        # 默认报错信息
        self.info = ''
        # 默认登录用户
        self.user = ''
        # 默认请求数据
        self.data = {'cid': 2,
                     'items[0][match_id_or_room_number]': '4685',
                     'items[0][play_type]': 'gamble',
                     'items[0][title]': '赛事对赌竞猜测试',
                     'items[0][option_A]': '选项A',
                     'items[0][option_B]': '选项B',
                     'items[0][expire]': str(int(time.time()))}

    '''参数必填检验'''

    def test_1(self):
        '''参数必填检验-未登录发言'''
        self.exp_res = {'status': False, 'code': '101', 'data': [], 'message': '未登录'}
        self.user = '1522'

    def tearDown(self):
        # 比较结果
        assert_res(self)


class TestGuessUserBet(unittest.TestCase):
    def setUp(self):
        # 接口信息
        self.name = '用户下注,坐庄,买庄'
        self.url = '/guessnew/bet'
        self.method = 'get'
        # 默认报错信息
        self.info = ''
        # 默认登录用户
        self.user = ''
        # 默认请求数据
        self.data = {
            'period': '',  # 期号
            'chose': 'option_A',  # 竞猜选项option_A, option_B
            'coin_type': 'free_bean',  # 货币类型仙豆free_bean,猫豆cat_bean
            'amount': 100,  # 下注金额
            'punter': 'bet',  # bet:普通下注,'banker':坐庄, 'buyer':买庄
            'banker_odds': '',  # 赔率
        }

    '''参数必填检验'''

    def test_guess_user_bet_bet_01(self):
        '''参数必填检验-未登录发言'''
        self.exp_res = {'status': False, 'code': '101', 'data': [], 'message': '未登录'}
        self.user = '1522'

    def tearDown(self):
        # 比较结果
        assert_res(self)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestGuessUserCreate('test_1'))
    runner = unittest.TextTestRunner()
    runner.run(suite)