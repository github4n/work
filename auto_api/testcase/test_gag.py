#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 18:27:48
# @Author  : lixingyun
import unittest
from nose_parameterized import parameterized
import sys
import logging

sys.path.append('../')
from lib import assert_res, request, cmp_dict
from lib2 import generate_room, generate_user, init_gag
from config import superuid, report_data, interface

# generate_room('gag', 3)
# generate_user('gag', 10, True)
# exit()
room_data = {'room_number': 641900, 'fz_name': 'gag1503044661', 'fg_name': ['gag1503044663', 'gag1503044665', 'gag1503044666'], 'fz_id': 5130,
             'cid': 119451, 'fg_id': [5131, 5132, 5133]}
user_data = {'user_names': ['gag1503044672', 'gag1503044673', 'gag1503044675', 'gag1503044677', 'gag1503044678', 'gag1503044680', 'gag1503044682',
                            'gag1503044683', 'gag1503044685', 'gag1503044687'],
             'user_ids': [5134, 5135, 5136, 5137, 5138, 5139, 5140, 5141, 5142, 5143]}

fz = room_data['fz_id']
fg = room_data['fg_id']
cid = room_data['cid']
users = user_data['user_ids']

exp_t = {'code': 4000, 'status': True, 'message': '处理成功！'}
exp_f1 = {'code': '2018', 'status': False, 'data': [], 'message': '没有权限'}
exp_f2 = {'code': '4302', 'status': False, 'message': '参数错误！'}
exp_f3 = {'code': '4418', 'status': False, 'message': '您无权对本房间房管进行禁言'}
exp_f4 = {'code': '4417', 'status': False, 'message': '您无权对本房间主播进行禁言'}
exp_f5 = {'code': '4416', 'status': False, 'message': '您无权对超管进行禁言'}
exp_f6 = {'code': '4421', 'status': False, 'message': '已被禁言'}
exp_f_yz = {'code': 203, 'message': '抱歉，您已被禁言！如有疑问，请咨询客服。', 'status': False}


# 初始化禁言数据
init_gag(users,cid)
# 数据准备
# 房管禁言用户
for i in range(3, 8):
    request('gag', fg[0], cid=cid, uid=users[i])
# 房主禁言用户
for i in range(8, 10):
    request('gag', fz, cid=cid, uid=users[i])

# 二次验证方法
def ver(user):
    def ver_():
        res_twice = request('msg', user, cid=cid)
        logging.debug(res_twice)
        try:
            cmp_dict(exp_f_yz, res_twice[0])
            return True
        except Exception as e:
            logging.debug(e)
            return False

    return ver_


class TestGag(unittest.TestCase):
    '''普通用户禁言'''

    def test_gag_01(self):
        '''普通用户禁言普通用户'''
        user = users[0]
        assert_res(sys._getframe(), 'gag', user, exp_f1, cid=cid, uid=users[1])

    def test_gag_02(self):
        '''普通用户禁言房管'''
        user = users[0]
        assert_res(sys._getframe(), 'gag', user, exp_f1, cid=cid, uid=fg[0])

    def test_gag_03(self):
        '''普通用户禁言房主'''
        user = users[0]
        assert_res(sys._getframe(), 'gag', user, exp_f1, cid=cid, uid=fz)

    def test_gag_04(self):
        '''普通用户禁言超管'''
        user = users[0]
        assert_res(sys._getframe(), 'gag', user, exp_f1, cid=cid, uid=superuid)

    '''房管禁言'''

    def test_gag_05(self):
        '''房管禁言普通用户'''
        user = fg[0]
        assert_res(sys._getframe(), 'gag', user, exp_t, ver=ver(users[1]), cid=cid, uid=users[1])

    def test_gag_06(self):
        '''房管禁言房管'''
        user = fg[0]
        assert_res(sys._getframe(), 'gag', user, exp_f3, cid=cid, uid=fg[1])

    def test_gag_07(self):
        '''房管禁言房主'''
        user = fg[0]
        assert_res(sys._getframe(), 'gag', user, exp_f4, cid=cid, uid=fz)

    def test_gag_08(self):
        '''房管禁言超管'''
        user = fg[0]
        assert_res(sys._getframe(), 'gag', user, exp_f5, cid=cid, uid=superuid)

    '''房主禁言'''

    def test_gag_09(self):
        '''房主禁言普通用户'''
        user = fz
        assert_res(sys._getframe(), 'gag', user, exp_t, ver=ver(users[2]), cid=cid, uid=users[2])

    def test_gag_10(self):
        '''房主禁言房管'''
        user = fz
        assert_res(sys._getframe(), 'gag', user, exp_t, ver=ver(fg[2]), cid=cid, uid=fg[2])

    def test_gag_11(self):
        '''房主禁言房主'''
        user = fz
        assert_res(sys._getframe(), 'gag', user, exp_f2, cid=cid, uid=fz)

    def test_gag_12(self):
        '''房主禁言超管'''
        user = fz
        assert_res(sys._getframe(), 'gag', user, exp_f5, cid=cid, uid=superuid)

    '''已被禁言用户,再被其他用户禁言操作'''

    def test_gag_13(self):
        '''用户已被房管1,24h禁言,再被房管1,永久禁言'''
        user = fg[0]
        assert_res(sys._getframe(), 'gag', user, exp_t, status=0, cid=cid, uid=users[3])

    def test_gag_14(self):
        '''用户已被房管1,24h禁言，不能被房管2禁言操作'''
        user = fg[1]
        assert_res(sys._getframe(), 'gag', user, exp_f6, cid=cid, uid=users[4])

    def test_gag_15(self):
        '''用户已被房管1,24h禁言,被房管2,永久禁言'''
        user = fg[1]
        assert_res(sys._getframe(), 'gag', user, exp_f6, status=0, cid=cid, uid=users[5])

    def test_gag_16(self):
        '''已被房管1禁言用户,被房主,24h禁言'''
        user = fz
        assert_res(sys._getframe(), 'gag', user, exp_t, cid=cid, uid=users[6])

    def test_gag_17(self):
        '''已被房管1禁言用户,被房主永久禁言'''
        user = fz
        assert_res(sys._getframe(), 'gag', user, exp_t, status=0, cid=cid, uid=users[7])

    def test_gag_18(self):
        '''已被房主禁言用户,被房管1,24h禁言'''
        user = fg[0]
        assert_res(sys._getframe(), 'gag', user, exp_f6, cid=cid, uid=users[8])

    def test_gag_19(self):
        '''已被房主禁言用户,被房管1,永久禁言'''
        user = fg[0]
        assert_res(sys._getframe(), 'gag', user, exp_f6, status=0, cid=cid, uid=users[9])


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestGag('test_gag_18'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
