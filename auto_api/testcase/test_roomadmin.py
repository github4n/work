#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/8/8 17:24
# Author : lixingyun
import unittest
import sys
import time
import json
sys.path.append('../')
from lib import assert_res, request
from lib2 import redis_inst, generate_room, generate_user

# testdata1 = generate_room('sra')
# testdata2 = generate_room('sra')
# testdata3 = generate_room('sra')
# testdata4 = generate_room('sra')
# generate_user('sra', 7, True)
# exit()
room_data = {'room_number': 984948, 'fz_id': 5084, 'cid': 119445, 'fz_name': 'sra1502948240'}
room_data2 = {'room_number': 360784, 'fz_id': 5085, 'cid': 119446, 'fz_name': 'sra1502948246'}
room_data3 = {'room_number': 913091, 'fz_id': 5086, 'cid': 119447, 'fz_name': 'sra1502948251'}
room_data4 = {'room_number': 780744, 'fz_id': 5087, 'cid': 119448, 'fz_name': 'sra1502948257'}
yh_data = {'user_ids': [5088, 5089, 5090, 5091, 5092, 5093, 5094],
           'user_names': ['sra1502948262', 'sra1502948264', 'sra1502948265', 'sra1502948267', 'sra1502948268', 'sra1502948270', 'sra1502948272']}
fz = room_data['fz_id']
cid = room_data['cid']
yh = yh_data['user_ids']
yh_name = yh_data['user_names']
times = int(time.time())


# 二次验证方法
def ver(user, cid, exp_yz):
    def ver_():
        res_twice = request('msg', user, cid=cid)
        try:
            cmp_dict(exp_yz, res_twice[0])
            return True
        except Exception as e:
            return False

    return ver_


class TestRoomAdmin(unittest.TestCase):
    def test_setroomadmin_01(self):
        '''房主设置普通用户为房管'''
        user = fz
        redis_inst.delete('hm_channel_admin_{}'.format(cid))
        exp = {'code': 200, 'status': True, 'message': '处理成功！'}
        exp_yz = {'code': 200, 'data': {'chat_code': 100001, 'msg_type': 'msg', 'msg_content': {'is_fg': 1}}}
        assert_res(sys._getframe(), 'setroomadmin', user, exp, ver=ver(yh[0], cid, exp_yz), username=yh_name[0])

    def test_setroomadmin_02(self):
        '''房主设置房管为房管'''
        user = room_data2['fz_id']
        redis_inst.set('hm_channel_admin_{}'.format(room_data2['cid']), json.dumps({yh[1]: times}))
        exp = {'code': '266', 'status': False, 'message': '已经是房管'}
        assert_res(sys._getframe(), 'setroomadmin', user, exp, username=yh_name[1])

    def test_setroomadmin_03(self):
        '''房主设置房主为房管'''
        user = fz
        exp = {'code': '4302', 'status': False, 'message': '无法对自己进行设置'}
        assert_res(sys._getframe(), 'setroomadmin', user, exp, username=room_data['fz_name'])

    def test_setroomadmin_04(self):
        '''用户设置用户为房管'''
        user = yh[2]
        exp = {'code': '4302', 'status': False, 'message': '参数错误！'}
        assert_res(sys._getframe(), 'setroomadmin', user, exp, username=yh_name[3])

    def test_setroomadmin_05(self):
        '''房管已达到上限'''
        user = room_data3['fz_id']
        redis_inst.set('hm_channel_admin_{}'.format(room_data3['cid']), json.dumps({i: times for i in range(1, 11)}))
        exp = {'code': '4305', 'status': False, 'message': '房管最多10位'}
        assert_res(sys._getframe(), 'setroomadmin', user, exp, username=yh_name[4])

    def test_delroomadmin_01(self):
        '''用户是房管，取消用户房管'''
        user = room_data4['fz_id']
        cid = room_data4['cid']
        redis_inst.set('hm_channel_admin_{}'.format(cid), json.dumps({yh[5]: times}))
        exp = {'code': '4000', 'status': True, 'message': '处理成功！'}
        exp_yz = {'code': 200, 'data': {'chat_code': 100001, 'msg_type': 'msg', 'msg_content': {'is_fg': 0}}}
        assert_res(sys._getframe(), 'delroomadmin', user, exp, ver=ver(yh[5], cid, exp_yz), username=yh_name[5], uid=yh[5])

    def test_delroomadmin_02(self):
        '''用户不是房管，取消用户房管'''
        user = fz
        exp = {'code': '4000', 'status': True, 'message': '处理成功！'}
        assert_res(sys._getframe(), 'delroomadmin', user, exp, username=yh_name[6], uid=yh[6])


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestRoomAdmin('test_delroomadmin_01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
