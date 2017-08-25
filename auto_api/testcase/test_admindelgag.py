#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/8/7 9:49
# Author : lixingyun

import sys

sys.path.append('../')
import unittest
import logging
from lib import assert_res, request, cmp_dict
from lib2 import generate_room, generate_user, init_gag
from config import superuid, report_data, interface

# generate_room('adg', 1)
# generate_user('adg', 2, True)
# exit()

room_data = {'room_number': 152633, 'fg_id': [5149], 'fz_name': 'adg1503058347', 'cid': 119453, 'fz_id': 5148, 'fg_name': ['adg1503058348']}
user_data = {'user_names': ['adg1503058354', 'adg1503058355'], 'user_ids': [5150, 5151]}
fz = room_data['fz_id']
fg = room_data['fg_id']
cid = room_data['cid']
users = user_data['user_ids']

# 初始化禁言数据
init_gag(user_data, room_data)
# exit()
# 数据准备
# 用户被超管管禁言
request('admingag', superuid, user_uid=users[1])
# 房主被超管禁言
request('admingag', superuid, user_uid=fz, gag_type=0)

exp_t = {'code': 4000, 'status': True, 'message': '处理成功！', 'data': {'title': '取消全平台24小时禁言'}}
exp_t2 = {'code': 4000, 'status': True, 'message': '处理成功！', 'data': {'title': '取消全平台禁言'}}
exp_f1 = {'code': '4302', 'status': False, 'data': [], 'message': '没有权限'}


# 二次验证方法
def ver(user):
    def ver_():
        exp_f_yz = {'code': 200}
        res_twice = request('msg', user, cid=cid)
        logging.debug(res_twice)
        try:
            cmp_dict(exp_f_yz, res_twice[0])
            return True
        except Exception as e:
            logging.debug(e)
            return False

    return ver_


class Test_Admindelgag(unittest.TestCase):
    def test_admindelgag_01(self):
        '''非超管用户取消禁言用户'''
        assert_res(sys._getframe(), 'admindelgag', users[0], exp_f1, cid=0, uid=users[1])

    def test_admindelgag_02(self):
        '''超管取消用户24h禁言'''
        uid = users[1]
        assert_res(sys._getframe(), 'admindelgag', superuid, exp_t, ver=ver(uid), cid=0, uid=uid)

    def test_admindelgag_03(self):
        '''超管取消房主永久禁言'''
        uid = fz
        assert_res(sys._getframe(), 'admindelgag', superuid, exp_t2, ver=ver(uid), cid=0, uid=uid, gag_type=0)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_Admindelgag('test_admindelgag_01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
