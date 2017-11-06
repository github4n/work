#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 18:27:48
# @Author  : lixingyun
# @notice  : 禁言在gag中判断
import unittest
import sys

sys.path.append('../')
from lib import assert_res, generate_report, cmp_dict, name_func_new
from common.common import Common
from config import superuid
import time
import json

'''数据准备'''
# Common.generate_room('msg', 1)
# Common.generate_user('msg', 20, True)
# Common.generate_user('msg', 1)
# exit()
room_data = {'fz_name': 'msg1509679530', 'fg_id': [5540], 'fz_id': 5539, 'room_number': 755038, 'cid': 119479, 'fg_name': ['msg1509679532']}
room_data2 = {'fz_id': 4995, 'fz_name': 'msg1502430222', 'cid': 119399, 'room_number': 664753}
user_data = {
    'user_ids': [4997, 4998, 4999, 5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 5016, 5017]}
anchor = room_data['fz_id']
fg = room_data['fg_id'][0]
cid = room_data['cid']
cid2 = room_data2['cid']
user_ids = user_data['user_ids']
redis_inst = Common.REDIS_INST

exp_dict = {
    'unlogin': {'status': False, 'code': '101', 'data': [], 'message': '未登录'},
    'null': {'code': 202, 'status': False, 'message': '消息不能为空'},
    'normal': {'code': 200, 'data': {}},
    'length': {'code': 206, 'status': False, 'message': '您的发言已超出字符限制了~'},
    'sensitive_words': {'code': 271, 'status': False, 'message': '发言包含敏感词，请重新输入'},
    'time': {'status': False, 'code': 204, 'message': '你发言太快！'},
    'no_phone': {'code': 2031, 'status': False, 'message': '绑定手机号即可发言'},
    'fz': {'code': 200, 'data': {'extend': {'is_zb': '1'}}},
    'fg': {'code': 200, 'data': {'extend': {'is_fg': '1'}}},
    'gag': {'status': False, 'code': 203, 'message': '抱歉,您已被禁言!详情请咨询客服!'},
}


class TestMsg(unittest.TestCase):
    def setUp(self):
        # 接口信息
        self.name = '发言'
        self.url = '/chatnew/msg'
        self.method = 'post'
        self.data = {
            'data': '测试弹幕',
            'cid': cid,
            'color_barrage': '',
            'guard_barrage': '',
            'isAdminPrivateChat': '',
            'is_hotWord': '',
        }

    '''基础功能判断'''

    def test_msg_01(self):
        '''未登录发言'''
        self.exp_res = exp_dict['unlogin']
        self.user = ''
        assert_res(self)

    def test_msg_02(self):
        '''发言为空'''
        self.exp_res = exp_dict['null']
        self.user = user_ids[0]
        self.data['data'] = ''
        assert_res(self)

    def test_msg_03(self):
        '''普通用户弹幕'''
        self.exp_res = exp_dict['normal']
        self.user = user_ids[1]
        assert_res(self)

    def test_msg_04(self):
        '''字数限制'''
        self.exp_res = exp_dict['length']
        self.user = user_ids[2]
        self.data['data'] = '01234567890123456789012345678901234567890123456789'
        assert_res(self)

    def test_msg_05(self):
        '''敏感词'''
        self.exp_res = exp_dict['sensitive_words']
        self.user = user_ids[3]
        self.data['data'] = '习近平'
        assert_res(self)

    def test_msg_06(self):
        '''发言间隔'''
        self.exp_res = exp_dict['time']
        self.user = user_ids[4]
        # 设置发言时间,服务器时间和本地时间有误差
        redis_inst.set('hm_chat_{}'.format(self.user), int(time.time()))
        assert_res(self)

    def test_msg_07(self):
        '''未绑定手机'''
        self.exp_res = exp_dict['no_phone']
        self.user = user_ids[-1]
        assert_res(self)

    def test_msg_08(self):
        '''注册时间'''
        self.exp_res = {'code': 2018, 'status': False, 'message': '您刚来,还得2分钟才能发言~'}
        self.user = user_ids[5]
        self.data['cid'] = cid2
        # 设置用户注册时间
        regtime = int(time.time())
        user_info_key = 'hm_{}'.format(self.user)
        user_info = json.loads(redis_inst.get(user_info_key))
        user_info['regtime'] = regtime
        redis_inst.set(user_info_key, json.dumps(user_info))
        # 设置房间cid2发言限制
        redis_inst.hset('hm_chat_limit_admin_{}'.format(cid2), 'regTime', '120')
        assert_res(self)

    def test_msg_09(self):
        '''用户被禁言'''
        self.exp_res = exp_dict['gag']
        self.user = user_ids[6]
        Common.gag(self.user, anchor, cid)
        assert_res(self)

    '''角色功能判断'''

    def test_msg_10(self):
        '''房管'''
        self.exp_res = exp_dict['fg']
        self.user = fg
        assert_res(self)

    def test_msg_11(self):
        '''房主'''
        self.exp_res = exp_dict['fz']
        self.user = anchor
        assert_res(self)

    @unittest.skip('')
    def test_msg_12(self):
        '''超管'''
        self.exp_res = ''
        self.user = superuid
        assert_res(self)

    '''彩色弹幕逻辑'''

    def test_msg_13(self):
        '''弹幕卡足，余额足时，发言彩色弹幕'''
        self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}
        self.user = user_ids[7]
        self.data['color_barrage'] = 1
        # 二次验证函数
        self.ver = lambda: Common.get_dmk(self.user) == 0 and Common.get_money(self.user)['coin'] == 1
        # 添加用户弹幕卡和货币
        Common.add_dmk(self.user)
        Common.set_money(self.user, 1)
        assert_res(self)
        Common.del_dmk(self.user)

    def test_msg_14(self):
        '''弹幕卡足，余额不足时，发言彩色弹幕'''
        self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}
        self.user = user_ids[8]
        self.data['color_barrage'] = 1
        # 二次验证函数
        self.ver = lambda: Common.get_dmk(self.user) == 0
        # 添加用户弹幕卡
        Common.add_dmk(self.user)
        assert_res(self)
        Common.del_dmk(self.user)

    def test_msg_15(self):
        '''弹幕卡不足，余额足时，发言彩色弹幕'''
        self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}
        self.user = user_ids[9]
        self.data['color_barrage'] = 1
        # 二次验证函数
        self.ver = lambda: Common.get_money(self.user)['coin'] == 0
        Common.set_money(self.user, 1)
        assert_res(self)
        Common.del_dmk(self.user)

    def test_msg_16(self):
        '''弹幕卡不足，余额不足时，发言彩色弹幕'''
        self.exp_res = {'code': 2032, 'status': False, 'message': '余额不足'}
        self.user = user_ids[10]
        self.data['color_barrage'] = 1
        assert_res(self)

    def test_msg_17(self):
        '''弹幕卡消耗顺序'''
        self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '1', 'msg': '测试弹幕'}}}
        self.user = 1522
        self.data['color_barrage'] = 1
        dmk_time = int(time.time())
        expire_time1 = dmk_time + 100
        expire_time2 = dmk_time + 200
        Common.add_dmk(self.user, expire_time=expire_time1)
        Common.add_dmk(self.user, expire_time=expire_time2)
        # 二次验证函数
        self.ver = lambda: Common.get_time_dmk(self.user, expire_time1) == 0
        assert_res(self)
        Common.del_dmk(self.user)

    '''粉丝逻辑'''

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
    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMsg('test_msg_14'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
