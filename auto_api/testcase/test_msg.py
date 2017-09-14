#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 18:27:48
# @Author  : lixingyun
import unittest
import sys

sys.path.append('../')
from lib import assert_res, generate_report, request, cmp_dict, name_func_new
from common.common import Common
from config import superuid, interface
import time
import json

'''
注意：
1.禁言在gag中判断,房管在roomadmin判断
2.5还有问题
'''
common = Common()
'''数据准备'''
# generate_room('msg')
# generate_user('msg', 20, True)
# generate_user('msg', 1)
# exit()
room_data = {'fz_name': 'msg1502360487', 'cid': 119398, 'fz_id': 4973, 'room_number': 787403}
room_data2 = {'fz_id': 4995, 'fz_name': 'msg1502430222', 'cid': 119399, 'room_number': 664753}
user_data = {
    'user_ids': [4997, 4998, 4999, 5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 5016, 5017]}
fz = room_data['fz_id']
cid = room_data['cid']
cid2 = room_data2['cid']
user_ids = user_data['user_ids']
exp_dict = interface['msg']['exp_dict']
redis_inst = common.REDIS_INST


class TestMsg(unittest.TestCase):
    '''基础功能判断'''

    @unittest.skip('')
    def test_msg_01(self):
        '''未登录发言'''
        assert_res(sys._getframe(), 'msg', '', '')

    def test_msg_02(self):
        '''发言为空'''
        assert_res(sys._getframe(), 'msg', user_ids[0], exp_dict['null'], cid=cid, data='')

    def test_msg_03(self):
        '''普通用户弹幕'''
        assert_res(sys._getframe(), 'msg', user_ids[1], exp_dict['normal'], cid=cid)

    def test_msg_04(self):
        '''字数限制'''
        length_data = '01234567890123456789012345678901234567890123456789'
        assert_res(sys._getframe(), 'msg', user_ids[2], exp_dict['length'], cid=cid, data=length_data)

    def test_msg_05(self):
        '''敏感词'''
        assert_res(sys._getframe(), 'msg', user_ids[3], exp_dict['sensitive_words'], cid=cid, data='习近平')

    def test_msg_06(self):
        '''发言间隔'''
        user = user_ids[4]
        request('msg', user, cid=cid)
        assert_res(sys._getframe(), 'msg', user, exp_dict['time'], cid=cid)

    def test_msg_07(self):
        '''未绑定手机'''
        assert_res(sys._getframe(), 'msg', user_ids[-1], exp_dict['no_phone'], cid=cid)

    def test_msg_08(self):
        '''注册时间'''
        user = user_ids[5]
        # 设置用户注册时间
        regtime = int(time.time())
        user_info_key = 'hm_{}'.format(user)
        user_info = json.loads(redis_inst.get(user_info_key))
        user_info['regtime'] = regtime
        redis_inst.set(user_info_key, json.dumps(user_info))
        # 设置房间发言限制
        redis_inst.hset('hm_chat_limit_admin_{}'.format(cid2), 'regTime', '120')
        exp = {'code': 2018, 'status': False, 'message': '您刚来,还得2分钟才能发言~'}
        assert_res(sys._getframe(), 'msg', user, exp, cid=cid2)

    '''角色功能判断'''

    def test_msg_09(self):
        '''房主'''
        assert_res(sys._getframe(), 'msg', fz, exp_dict['fz'], cid=cid)

    @unittest.skip('')
    def test_msg_10(self):
        '''超管'''
        exp = {'code': 206, 'status': False, 'message': '敏感词'}
        assert_res(sys._getframe(), 'msg', superuid, exp, cid=cid)

    '''彩色弹幕逻辑'''

    def test_msg_11(self):
        '''弹幕卡足，余额足时，发言彩色弹幕'''
        user = user_ids[6]
        common.add_dmk(user)
        common.set_money(user, 1)
        exp = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}

        def ver():
            return common.get_dmk(user) == 0 and common.get_money(user)['coin'] == 1

        assert_res(sys._getframe(), 'msg', user, exp, ver=ver, color_barrage=1, cid=cid)

        common.del_dmk(user)

    def test_msg_12(self):
        '''弹幕卡足，余额不足时，发言彩色弹幕'''
        user = user_ids[7]
        common.add_dmk(user)
        exp = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}

        def ver():
            return common.get_dmk(user) == 0

        assert_res(sys._getframe(), 'msg', user, exp, ver=ver, color_barrage=1, cid=cid)
        common.del_dmk(user)

    def test_msg_13(self):
        '''弹幕卡不足，余额足时，发言彩色弹幕'''
        user = user_ids[8]
        common.set_money(user, 1)
        exp = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}

        def ver():
            return common.get_money(user)['coin'] == 0

        assert_res(sys._getframe(), 'msg', user, exp, ver=ver, color_barrage=1, cid=cid)
        common.del_dmk(user)

    def test_msg_14(self):
        '''弹幕卡不足，余额不足时，发言彩色弹幕'''
        user = user_ids[9]
        exp = {'code': 2032, 'status': False, 'message': '余额不足'}
        assert_res(sys._getframe(), 'msg', user, exp, color_barrage=1, cid=cid)

    def test_msg_15(self):
        '''弹幕卡消耗顺序'''
        user = user_ids[10]
        dmk_time = int(time.time())
        expire_time1 = dmk_time + 100
        expire_time2 = dmk_time + 200
        common.add_dmk(user, expire_time=expire_time1)
        common.add_dmk(user, expire_time=expire_time2)
        exp = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '1', 'msg': '测试弹幕'}}}

        def ver():
            sql = "SELECT num FROM user_bag_{} WHERE uid={} and expire_time ={}".format(common.hash_table(user), user, expire_time1)
            data = common.execute_sql('hm_user_bag', sql)
            if data[0] == 0:
                return True

        assert_res(sys._getframe(), 'msg', user, exp, ver=ver, color_barrage=1, cid=cid)
        common.del_dmk(user)


# # 粉丝逻辑
# # 徽章逻辑
# def test_msg017(self):
#     case_des = '守护王子'
#     user = '4188'
#     self.data['cid'] = 119298
#     self.data['guard_barrage'] = 1
#     exp_res = {'code': 200, 'data': {'chat_code': 100001, 'msg_type': 'msg', 'msg_content': {'is_guard': 1, 'guard_barrage': {'type': 2}, 'guardInfo': {'uid': '4188', 'type': 2, 'knight_expire': 0, 'prince_expire': 1531618943}}}}
#     assert_res(sys._getframe().f_code.co_name, case_des, self.name, self.url, self.method, user, self.data, exp_res)
#
# def test_msg018(self):
#     case_des = '守护骑士'
#     user = '4196'
#     self.data['cid'] = 119298
#     self.data['guard_barrage'] = 1
#     exp_res = {'code': 200, 'data': {'chat_code': 100001, 'msg_type': 'msg', 'msg_content': {'is_guard': 1, 'guard_barrage': {'type': 1}, 'guardInfo': {'uid': '4196', 'type': 1, 'knight_expire': 1531988363, 'prince_expire': 0}}}}
#     assert_res(sys._getframe().f_code.co_name, case_des, self.name, self.url, self.method, user, self.data, exp_res)
#
# @unittest.skip('')
# def test_msg019(self):
#     case_des = '守护王子弹幕数量不足'
#     user = '4192'
#     self.data['cid'] = 119298
#     self.data['guard_barrage'] = 1
#     exp_res = {'code': 3002, 'status': False, 'message': '守护弹幕已经用光'}
#     assert_res(sys._getframe().f_code.co_name, case_des, self.name, self.url, self.method, user, self.data, exp_res)
#
# @unittest.skip('')
# def test_msg020(self):
#     case_des = '守护骑士弹幕数量不足'
#     user = '4193'
#     self.data['cid'] = 119298
#     self.data['guard_barrage'] = 1
#     exp_res = {'code': 3002, 'status': False, 'message': '守护弹幕已经用光'}
#     assert_res(sys._getframe().f_code.co_name, case_des, self.name, self.url, self.method, user, self.data, exp_res)
#
# @unittest.skip('')
# def test_msg021(self):
#     case_des = '守护王子过期'
#     user = '4190'
#     self.data['cid'] = 119298
#     self.data['guard_barrage'] = 1
#     exp_res = {}
#     assert_res(sys._getframe().f_code.co_name, case_des, self.name, self.url, self.method, user, self.data, exp_res)
#
# @unittest.skip('')
# def test_msg022(self):
#     case_des = '守护骑士过期'
#     user = '4191'
#     self.data['cid'] = 119298
#     self.data['guard_barrage'] = 1
#     exp_res = {}
#     assert_res(sys._getframe().f_code.co_name, case_des, self.name, self.url, self.method, user, self.data, exp_res)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMsg('test_msg_15'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
