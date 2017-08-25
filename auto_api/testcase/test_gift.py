#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/8/14 14:17
# Author : lixingyun
import unittest
import sys
sys.path.append('../')
from lib import assert_res, generate_report, request, cmp_dict, name_func_new
from lib2 import mysql_inst, redis_inst, generate_room, generate_user, add_dmk, del_dmk, set_money, get_money, get_dmk, hash_table
from config import superuid
import time
import json


'''数据准备'''


# generate_room('gift')
# generate_user('gift', 20, True)
# generate_user('gift', 1)
# exit()

class TestGift(unittest.TestCase):
    '''基础功能判断'''

    def test_gift_01(self):
        '''普通用户弹幕'''
        user = user_ids[1]
        exp = {'code': 200, 'data': {'chat_code': 100001, 'msg_type': 'msg'}}
        assert_res(sys._getframe(), 'msg', user, exp, cid=cid)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestGift('test_gift_01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    generate_report()
