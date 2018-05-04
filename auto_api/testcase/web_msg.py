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
from config import super_uid

'''数据准备'''
# Common.generate_room('msg', 1)
# Common.generate_user('msg', 1)
# Common.generate_user('msg', 1, False)
# exit()
room = {
    'room': {
        'rid': '580535',
        'cid': '119484'
    },
    'fg': {
        0: {
            'name': 'msg1509961646',
            'uid': '5556'
        }
    },
    'anchor': {
        'name': 'msg1509961641',
        'uid': '5555'
    }
}
anchor = room['anchor']['uid']
cid = room['room']['cid']
user = {
    0: {'uid': '5567', 'name': 'msg1509962184'},
    1: {'uid': '5568', 'name': 'msg1509962186'},
    2: {'uid': '5569', 'name': 'msg1509962188'},
    3: {'uid': '5570', 'name': 'msg1509962189'},
    4: {'uid': '5571', 'name': 'msg1509962191'},
    5: {'uid': '5572', 'name': 'msg1509962192'},
    6: {'uid': '5573', 'name': 'msg1509962194'},
    7: {'uid': '5574', 'name': 'msg1509962195'},
    8: {'uid': '5575', 'name': 'msg1509962196'},
    9: {'uid': '5576', 'name': 'msg1509962198'},
    10: {'uid': '5580', 'name': 'msg1510022720'}
}

user2 = {0: {'name': 'msg1509964415', 'uid': '5578'}}


class TestMsg(unittest.TestCase):
    def setUp(self):
        # 接口信息
        self.name = '发言'
        self.url = '/chatnew/msg'
        self.method = 'get'
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

    '''参数必填检验'''

    def test_msg_01(self):
        '''参数必填检验-未登录发言'''
        self.exp_res = {'status': False, 'code': '101', 'data': [], 'message': '未登录'}

    def test_msg_02(self):
        '''参数必填检验-未传data'''
        self.exp_res = {'code': '202', 'status': False, 'message': '消息不能为空'}
        self.user = user[0]['uid']
        self.data['data'] = ''

    def test_msg_03(self):
        '''参数必填检验-未传cid'''
        self.exp_res = {'code': '1001', 'status': False, 'message': '房间不存在'}
        self.user = user[0]['uid']
        self.data['cid'] = ''

    '''业务-发言内容'''

    def test_msg_04(self):
        '''业务-发言内容'''
        self.exp_res = {'code': 200, 'data': {'barrage': {'msg': self.data['data']}}}
        self.user = user[1]['uid']

    '''业务-字数限制'''

    def test_msg_05(self):
        '''业务-字数限制'''
        self.exp_res = self.exp_res_api = {'code': '206', 'status': False, 'message': '您的发言已超出字符限制了~'}
        self.user = user[2]['uid']
        self.data['data'] = '01234567890123456789012345678901234567890123456789'

    '''业务-敏感词'''

    def test_msg_06(self):
        '''业务-敏感词'''
        self.exp_res = self.exp_res_api = {'code': '271', 'status': False, 'message': '发言包含敏感词，请重新输入'}
        self.user = user[3]['uid']
        self.data['data'] = '习近平'

    '''业务-发言间隔判断'''

    def test_msg_07(self):
        '''业务-发言间隔'''
        self.exp_res = {'status': False, 'code': '204', 'message': '你发言太快！'}
        self.user = user[4]['uid']
        # 设置发言时间,服务器时间和本地时间有误差,所以用服务器时间
        msg_time = Common.get_linux_time()
        Common.REDIS_INST.set('hm_chat_{}'.format(self.user), msg_time)

    '''业务-未绑定手机判断'''

    def test_msg_08(self):
        '''业务-未绑定手机'''
        self.exp_res = {'code': '2031', 'status': False, 'message': '绑定手机号即可发言'}
        self.user = user2[0]['uid']

    '''业务-注册时间判断'''

    def test_msg_09(self):
        '''业务-注册时间判断'''
        self.exp_res = {'code': '2018', 'status': False, 'message': '您刚来,还得2分钟才能发言~'}
        self.user = user[5]['uid']
        # 设置用户注册时间
        user_info_key = 'hm_{}'.format(self.user)
        user_info = json.loads(Common.REDIS_INST.get(user_info_key))
        user_info['regtime'] = int(time.time())
        Common.REDIS_INST.set(user_info_key, json.dumps(user_info))
        # 设置房间发言限制
        key = 'hm_chat_limit_admin_{}'.format(cid)
        Common.REDIS_INST.hset(key, 'regTime', '120')

    '''业务-用户被禁言'''

    def test_msg_10(self):
        '''业务-用户被禁言'''
        self.exp_res = {'status': False, 'code': '203', 'message': '抱歉,您已被禁言!详情请咨询客服!'}
        self.user = user[6]['uid']
        Common.gag(self.user, room['anchor']['uid'], room['room']['cid'])

    '''业务-角色功能判断'''

    def test_msg_11(self):
        '''业务-角色功能判断-房管'''
        self.exp_res = {'code': 200, 'data': {'extend': {'is_fg': '1'}}}
        self.user = room['fg'][0]['uid']

    def test_msg_12(self):
        '''业务-角色功能判断-房主'''
        self.exp_res = {'code': 200, 'data': {'extend': {'is_zb': '1'}}}
        self.user = room['anchor']['uid']

    # @unittest.skip('')
    # def test_msg_12(self):
    #     '''业务-角色功能判断-超管'''
    #     self.exp_res = ''
    #     self.user = superuid

    '''业务-彩色弹幕逻辑'''

    def test_msg_13(self):
        '''业务-彩色弹幕'''
        self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}
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

    # def test_msg_14(self):
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
    # def test_msg_15(self):
    #     '''弹幕卡不足，余额足时，发言彩色弹幕'''
    #     self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}
    #     self.user = user_ids[9]
    #     self.data['color_barrage'] = 1
    #     Common.del_dmk(self.user)
    #     # 二次验证函数
    #     self.ver = lambda: Common.get_money(self.user)['coin'] == 0
    #     Common.set_money(self.user, 1)
    #
    # def test_msg_16(self):
    #     '''弹幕卡不足，余额不足时，发言彩色弹幕'''
    #     self.exp_res = {'code': 2032, 'status': False, 'message': '余额不足'}
    #     self.user = user_ids[10]
    #     self.data['color_barrage'] = 1
    #
    # def test_msg_17(self):
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
    '''业务-图标'''

    def test_msg_14(self):
        '''业务-图标-粉丝'''
        self.exp_res = {'code': 200, 'data': {'fans': {'cid': room['room']['cid'],
                                                       'zb_name': room['anchor']['name'],
                                                       'rid': room['room']['rid'],
                                                       'level': '25', 'name': '粉丝'}}}
        self.user = user[8]['uid']
        # 设置用户粉丝等级
        key = 'hm_loveliness_fan_lv_news_{}_{}'.format(self.user, room['room']['cid'])
        Common.REDIS_INST.set(key, 25)

    def test_msg_15(self):
        '''业务-图标-徽章'''
        self.exp_res = {'code': 200, 'data': {'badge': [{'bid': '1', }]}}
        self.user = user[9]['uid']
        key = 'hm_member_adorn_badge:{}'.format(self.user)
        Common.REDIS_INST.hset(key, 'bid:1', '{"bid":1,"gettime":' + str(int(time.time())) + ',"owntime":1440,"currentstat":3}')

    def test_msg_16(self):
        '''业务-图标-守护'''
        self.exp_res = {'code': 200, 'data': {'extend': {'is_guard': '2'}, 'barrage': {'type': '200'}}}
        self.user = user[10]['uid']
        self.data['guard_barrage'] = 1

    def tearDown(self):
        # 比较结果
        assert_res(self)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMsg('test_msg_11'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
