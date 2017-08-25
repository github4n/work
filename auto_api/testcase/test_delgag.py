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
import time

# generate_room('gag', 10)
# generate_user('gag', 13, True)
# exit()

room_data = {'cid': 119450,
             'fg_name': ['gag1503019261', 'gag1503019263', 'gag1503019264', 'gag1503019266', 'gag1503019267', 'gag1503019269', 'gag1503019271',
                         'gag1503019273',
                         'gag1503019274', 'gag1503019276'], 'fg_id': [5102, 5103, 5104, 5105, 5106, 5107, 5108, 5109, 5110, 5111], 'fz_id': 5101,
             'fz_name': 'gag1503019260', 'room_number': 870041}
user_data = {'user_names': ['gag1503019282', 'gag1503019284', 'gag1503019286', 'gag1503019288', 'gag1503019289', 'gag1503019291', 'gag1503019292',
                            'gag1503019294', 'gag1503019296', 'gag1503019298', 'gag1503019299', 'gag1503019301', 'gag1503019302'],
             'user_ids': [5112, 5113, 5114, 5115, 5116, 5117, 5118, 5119, 5120, 5121, 5122, 5123, 5124]}
fz = room_data['fz_id']
fg = room_data['fg_id']
cid = room_data['cid']
users = user_data['user_ids']

# 初始化禁言数据
init_gag(users, cid)

# 数据准备
# 房管禁言用户
for i in range(1, 5):
    request('gag', fg[0], cid=cid, uid=users[i])
# 房主禁言用户
for i in range(5, 8):
    request('gag', fz, cid=cid, uid=users[i])
# 超管禁言用户
for i in range(8, 11):
    request('admingag', superuid, cid=cid, uid=users[i])
# 房主禁言房管
for i in range(2, 5):
    request('gag', fz, cid=cid, uid=fg[i])
# 超管禁言房管
for i in range(5, 8):
    request('admingag', superuid, cid=cid, user_uid=fg[i])
# 超管禁言房主
request('admingag', superuid, cid=cid, user_uid=fz)


# 二次验证方法
def ver(user, exp_f=1):
    def ver_():
        if exp_f == 1:
            exp_f_yz = {'code': 203, 'status': False, 'message': '抱歉，您已被禁言！如有疑问，请咨询客服。'}
        else:
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


exp_t = {'code': 4000, 'status': True, 'message': '处理成功！'}
exp_f1 = {'code': '2018', 'status': False, 'data': [], 'message': '没有权限'}
exp_f2 = {'code': '4426', 'status': False, 'message': '您的权限不够,因不是您禁言的用户'}
exp_f3 = {'code': '4424', 'status': False, 'message': '处理失败'}
exp_f4 = {'code': '4302', 'status': False, 'message': '参数错误！'}


class TestDelgag(unittest.TestCase):
    '''普通用户yh[i]被房管1禁言'''

    def test_gag_01(self):
        '''普通用户取消禁言已被房管禁言的用户'''
        uid = users[1]
        assert_res(sys._getframe(), 'delgag', users[0], exp_f1, ver=ver(uid), cid=cid, uid=uid)

    def test_gag_02(self):
        '''房管自己取消禁言已被自己禁言的用户'''
        uid = users[2]
        assert_res(sys._getframe(), 'delgag', fg[0], exp_t, ver=ver(uid, 2), cid=cid, uid=uid)

    def test_gag_03(self):
        '''房管2取消禁言已被房管1禁言的用户'''
        uid = users[3]
        assert_res(sys._getframe(), 'delgag', fg[1], exp_f2, ver=ver(uid), cid=cid, uid=uid)

    def test_gag_04(self):
        '''房主取消禁言已被房管1禁言的用户'''
        uid = users[4]
        assert_res(sys._getframe(), 'delgag', fz, exp_t, ver=ver(uid, 2), cid=cid, uid=uid)

    '''普通用户yh[i]被房主禁言'''

    def test_gag_05(self):
        '''用户取消已被房主禁言的用户'''
        uid = users[5]
        assert_res(sys._getframe(), 'delgag', users[0], exp_f1, cid=cid, uid=uid)

    def test_gag_06(self):
        '''房管1取消禁言房主禁言的用户'''
        uid = users[6]
        assert_res(sys._getframe(), 'delgag', fg[0], exp_f2, cid=cid, uid=uid)

    def test_gag_07(self):
        '''房主取消禁言房主禁言的用户'''
        uid = users[7]
        assert_res(sys._getframe(), 'delgag', fz, exp_t, ver=ver(uid, 2), cid=cid, uid=uid)

    '''普通用户yh[i]被超管禁言'''

    def test_gag_08(self):
        '''用户取消已被超管禁言的用户'''
        uid = users[8]
        assert_res(sys._getframe(), 'delgag', users[0], exp_f1, cid=cid, uid=uid)

    def test_gag_09(self):
        '''房管1取消禁言超管禁言的用户'''
        uid = users[9]
        assert_res(sys._getframe(), 'delgag', fg[0], exp_f3, cid=cid, uid=uid)

    def test_gag_10(self):
        '''房主取消禁言超管禁言的用户'''
        uid = users[10]
        assert_res(sys._getframe(), 'delgag', fz, exp_f3, cid=cid, uid=uid)

    '''房管被房主禁言'''

    def test_gag_11(self):
        '''用户取消已被房主禁言的房管'''
        uid = fg[2]
        assert_res(sys._getframe(), 'delgag', users[0], exp_f1, cid=cid, uid=uid)

    def test_gag_12(self):
        '''房管2取消禁言房主禁言的房管'''
        uid = fg[3]
        assert_res(sys._getframe(), 'delgag', fg[0], exp_f2, cid=cid, uid=uid)

    def test_gag_13(self):
        '''房主取消禁言房主禁言的房管'''
        uid = fg[4]
        assert_res(sys._getframe(), 'delgag', fz, exp_t, ver=ver(uid, 2), cid=cid, uid=uid)

    '''房管被超管禁言'''

    def test_gag_14(self):
        '''用户取消已被超管禁言的房管'''
        uid = fg[5]
        assert_res(sys._getframe(), 'delgag', users[0], exp_f1, cid=cid, uid=uid)

    def test_gag_15(self):
        '''房管1取消禁言超管禁言的房管'''
        uid = fg[6]
        assert_res(sys._getframe(), 'delgag', fg[0], exp_f3, cid=cid, uid=uid)

    def test_gag_16(self):
        '''房主取消禁言超管禁言的房管'''
        uid = fg[7]
        assert_res(sys._getframe(), 'delgag', fz, exp_f3, cid=cid, uid=uid)

    '''房主被超管禁言'''

    def test_gag_17(self):
        '''用户取消已被超管禁言的房主'''
        uid = fz
        assert_res(sys._getframe(), 'delgag', users[0], exp_f1, cid=cid, uid=uid)

    def test_gag_18(self):
        '''房管1取消禁言超管禁言的房主'''
        uid = fz
        assert_res(sys._getframe(), 'delgag', fg[0], exp_f3, cid=cid, uid=uid)

    def test_gag_19(self):
        '''房主取消禁言超管禁言的房主'''
        uid = fz
        assert_res(sys._getframe(), 'delgag', fz, exp_f4, cid=cid, uid=uid)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestDelgag('test_gag_02'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
