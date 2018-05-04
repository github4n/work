#!/usr/bin/env python
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
from config import superuid

'''数据准备'''
# Common.generate_room('msg', 1)
# Common.generate_user('msg', 11)
# Common.generate_user('msg', 1, False)
# exit()
room = {'fg': {0: {'name': 'msg1510038173', 'uid': '5586'}},
        'anchor': {'name': 'msg1510038168', 'uid': '5585'},
        'room': {'cid': '119486', 'rid': '775105'}}

user = {0: {'name': 'msg1510038174', 'uid': '5587'},
        1: {'name': 'msg1510038175', 'uid': '5588'},
        2: {'name': 'msg1510038177', 'uid': '5589'},
        3: {'name': 'msg1510038178', 'uid': '5590'},
        4: {'name': 'msg1510038180', 'uid': '5591'},
        5: {'name': 'msg1510038181', 'uid': '5592'},
        6: {'name': 'msg1510038183', 'uid': '5593'},
        7: {'name': 'msg1510038184', 'uid': '5594'},
        8: {'name': 'msg1510038186', 'uid': '5595'},
        9: {'name': 'msg1510038187', 'uid': '5596'},
        10: {'name': 'msg1510038189', 'uid': '5597'}}

user2 = {0: {'name': 'msg1510038190', 'uid': '5598'}}


class TestMsg(unittest.TestCase):
    def setUp(self):
        # 接口信息
        self.name = '发言'
        self.url = '/chatnew/msg'
        self.method = 'get'
        # 默认预期
        self.exp_res = {'code': 200, 'status': True, 'data': {}}
        # 默认报错信息
        self.info = ''
        # 默认登录用户
        self.user = ''
        # 默认请求数据
        self.data = {
            'data': '测试弹幕',
            'cid': room['room']['cid'],
            # 'color_barrage': '',
            # 'guard_barrage': '',
            # 'isAdminPrivateChat': '',
            # 'is_hotWord': '',
        }

    '''基础功能判断'''

    def test_msg_api_01(self):
        '''未登录发言'''
        self.exp_res = {'data': {'uid': 0}, 'message': '未登陆', 'code': '101', 'status': 0}

    def test_msg_api_02(self):
        '''发言为空'''
        self.exp_res = {'code': 202, 'status': False, 'message': '消息不能为空'}
        self.user = user[0]['uid']
        self.data['data'] = ''

    def test_msg_api_03(self):
        '''普通用户弹幕'''
        self.user = user[1]['uid']

    def test_msg_api_04(self):
        '''字数限制'''
        self.exp_res = self.exp_res_api = {'code': 206, 'status': False, 'message': '您的发言已超出字符限制了~'}
        self.user = user[2]['uid']
        self.data['data'] = '01234567890123456789012345678901234567890123456789'

    def test_msg_api_05(self):
        '''敏感词'''
        self.exp_res = self.exp_res_api = {'code': 271, 'status': False, 'message': '发言包含敏感词，请重新输入'}
        self.user = user[3]['uid']
        self.data['data'] = '习近平'

    def test_msg_api_06(self):
        '''发言间隔'''
        self.exp_res = {'status': False, 'code': 204, 'message': '你发言太快！'}
        self.user = user[4]['uid']
        # 设置发言时间,服务器时间和本地时间有误差
        Common.REDIS_INST.set('hm_chat_{}'.format(self.user), int(time.time()) + 10)

    def test_msg_api_07(self):
        '''未绑定手机'''
        self.exp_res = {'code': 2031, 'status': False, 'message': '绑定手机号即可发言'}
        self.user = user2[0]['uid']

    def test_msg_api_08(self):
        '''注册时间'''
        self.exp_res = {'code': 2018, 'status': False, 'message': '您刚来,还得2分钟才能发言~'}
        self.user = user[5]['uid']
        # 删除房间发言限制
        key = 'hm_chat_limit_admin_{}'.format(room['room']['cid'])
        Common.REDIS_INST.delete(key)
        # 设置用户注册时间
        user_info_key = 'hm_{}'.format(self.user)
        user_info = json.loads(Common.REDIS_INST.get(user_info_key))
        user_info['regtime'] = int(time.time())
        Common.REDIS_INST.set(user_info_key, json.dumps(user_info))
        # 设置房间发言限制
        Common.REDIS_INST.hset(key, 'regTime', '120')

    def test_msg_api_09(self):
        '''用户被禁言'''
        self.exp_res = {'status': False, 'code': 203, 'message': '抱歉,您已被禁言!详情请咨询客服!'}
        self.user = user[6]['uid']
        Common.gag(self.user, room['anchor']['uid'], room['room']['cid'])

    '''角色功能判断'''

    def test_msg_api_10(self):
        '''房管'''
        self.user = room['fg'][0]['uid']

    def test_msg_api_11(self):
        '''房主'''
        self.user = room['anchor']['uid']

    @unittest.skip('')
    def test_msg_api_12(self):
        '''超管'''
        self.exp_res = ''
        self.user = superuid

    '''彩色弹幕逻辑'''

    def test_msg_api_13(self):
        '''弹幕卡足，余额足时，发言彩色弹幕'''
        self.user = user[7]['uid']
        self.data['color_barrage'] = 1
        # 删除弹幕卡,设置用户
        Common.del_dmk(self.user)
        Common.set_money(self.user, 0)
        # 二次验证函数
        self.ver = lambda: Common.get_dmk(self.user) == 0 and Common.get_money(self.user)['coin'] == 1
        # 添加用户弹幕卡和货币
        Common.add_dmk(self.user)
        Common.set_money(self.user, 1)

    # def test_msg_api_14(self):
    #     '''弹幕卡足，余额不足时，发言彩色弹幕'''
    #     self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}
    #     self.user = user_ids[8]
    #     self.data['color_barrage'] = 1
    #     Common.del_dmk(self.user)
    #     # 二次验证函数
    #     self.ver = lambda: Common.get_dmk(self.user) == 0
    #     # 添加用户弹幕卡
    #     Common.add_dmk(self.user)
    #
    # def test_msg_api_15(self):
    #     '''弹幕卡不足，余额足时，发言彩色弹幕'''
    #     self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}
    #     self.user = user_ids[9]
    #     self.data['color_barrage'] = 1
    #     Common.del_dmk(self.user)
    #     # 二次验证函数
    #     self.ver = lambda: Common.get_money(self.user)['coin'] == 0
    #     Common.set_money(self.user, 1)
    #
    # def test_msg_api_16(self):
    #     '''弹幕卡不足，余额不足时，发言彩色弹幕'''
    #     self.exp_res = {'code': 2032, 'status': False, 'message': '余额不足'}
    #     self.user = user_ids[10]
    #     self.data['color_barrage'] = 1
    #
    # def test_msg_api_17(self):
    #     '''弹幕卡消耗顺序'''
    #     self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '1', 'msg': '测试弹幕'}}}
    #     self.user = user_ids[14]
    #     self.data['color_barrage'] = 1
    #     Common.del_dmk(self.user)
    #
    #     dmk_time = int(time.time())
    #     expire_time1 = dmk_time + 100
    #     expire_time2 = dmk_time + 200
    #     Common.add_dmk(self.user, expire_time=expire_time1)
    #     Common.add_dmk(self.user, expire_time=expire_time2)
    #     # 二次验证函数
    #     self.ver = lambda: Common.get_time_dmk(self.user, expire_time1) == 0
    '''粉丝'''

    def test_msg_api_14(self):
        '''粉丝返回判断'''
        self.user = user[8]['uid']
        # 设置用户粉丝等级
        key = 'hm_loveliness_fan_lv_news_{}_{}'.format(self.user, room['room']['cid'])
        Common.REDIS_INST.set(key, 25)

    '''徽章'''

    def test_msg_api_15(self):
        '''徽章返回'''
        self.user = user[9]['uid']
        key = 'hm_member_adorn_badge:{}'.format(self.user)
        Common.REDIS_INST.hset(key, 'bid:1', '{"bid":1,"gettime":' + str(int(time.time())) + ',"owntime":1440,"currentstat":3}')

    '''守护'''

    def test_msg_api_16(self):
        '''守护返回'''
        self.user = user[10]['uid']
        self.data['guard_barrage'] = 1

    def tearDown(self):
        # 比较结果
        assert_res(self)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMsg('test_msg_api_16'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
