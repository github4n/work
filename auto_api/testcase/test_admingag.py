#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-04 17:07:44
# @Author  : lixingyun
import sys
sys.path.append('../')
import unittest
import logging
from lib import assert_res, request, cmp_dict
from lib2 import generate_room, generate_user, init_gag
from config import superuid, report_data, interface

# generate_room('ag', 1)
# generate_user('ag', 1, True)
# exit()

room_data = {'fg_id': [5146], 'fg_name': ['gag1503056806'], 'fz_id': 5145, 'room_number': 124072, 'fz_name': 'gag1503056804', 'cid': 119452}
user_data = {'user_ids': [5147], 'user_names': ['gag1503056812']}
fz = room_data['fz_id']
fg = room_data['fg_id']
cid = room_data['cid']
users = user_data['user_ids']

# 初始化禁言数据
init_gag(users, cid)

# 数据准备
# 房管已被房主禁言
request('gag', fz, uid=fg[0])

exp_t = {'code': 4000, 'status': True, 'message': '处理成功！', 'data': {'title': '全平台24小时禁言'}}
exp_t2 = {'code': 4000, 'status': True, 'message': '处理成功！', 'data': {'title': '全平台禁言'}}
exp_f1 = {'status': False, 'message': '没有权限', 'code': '2018', 'data': []}


# 二次验证方法
def ver(user):
    def ver_():
        exp_f_yz = {'code': 203, 'status': False, 'message': '抱歉，您已被禁言！如有疑问，请咨询客服。'}
        res_twice = request('msg', user, cid=cid)
        logging.debug(res_twice)
        try:
            cmp_dict(exp_f_yz, res_twice[0])
            return True
        except Exception as e:
            logging.debug(e)
            return False

    return ver_


class Test_Admingag(unittest.TestCase):
    def test_admingag_01(self):
        '''非超管用户禁言超管'''
        assert_res(sys._getframe(), 'admingag', users[0], '', cid=cid, user_uid=superuid)

    def test_admingag_02(self):
        '''超管禁言普通用户'''
        uid = users[0]
        assert_res(sys._getframe(), 'admingag', superuid, exp_t2, ver=ver(uid), cid=cid, user_uid=uid, gag_type=0)

    def test_admingag_03(self):
        '''超管禁言房主'''
        uid = fz
        assert_res(sys._getframe(), 'admingag', superuid, exp_t, ver=ver(uid), cid=cid, user_uid=uid)

    def test_admingag_04(self):
        '''房管已被普通禁言，超管再禁言'''
        uid = fg[0]
        assert_res(sys._getframe(), 'admingag', superuid, exp_t2, ver=ver(uid), cid=cid, user_uid=uid, gag_type=0)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_Admingag('test_admingag_04'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
