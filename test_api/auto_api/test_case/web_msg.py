#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 18:27:48
# @Author  : lixingyun
# @notice  :
import unittest
import time
from ..lib.lib import req
from ..lib.config import UID,logger_test_api
from huomao.user import User
from huomao.common import Common, REDIS_INST
from huomao.bag import Bag
from huomao.money import MoneyClass

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
anchor = '5555'
cid = '119484'
rid = '580535'


# user = {
#     0: {'uid': '5567', 'name': 'msg1509962184'},
#     1: {'uid': '5568', 'name': 'msg1509962186'},
#     2: {'uid': '5569', 'name': 'msg1509962188'},
#     3: {'uid': '5570', 'name': 'msg1509962189'},
#     4: {'uid': '5571', 'name': 'msg1509962191'},
#     5: {'uid': '5572', 'name': 'msg1509962192'},
#     6: {'uid': '5573', 'name': 'msg1509962194'},
#     7: {'uid': '5574', 'name': 'msg1509962195'},
#     8: {'uid': '5575', 'name': 'msg1509962196'},
#     9: {'uid': '5576', 'name': 'msg1509962198'},
#     10: {'uid': '5580', 'name': 'msg1510022720'}
# }

# user2 = {0: {'name': 'msg1509964415', 'uid': '5578'}}


class TestMsg(unittest.TestCase):
    # 创建用户
    def create_user(self, phone=True):
        uid = User.reg('noble')
        logger_test_api.info(f'注册用户UID：{uid}')
        if phone:
            User.bd_sj(uid)
        return uid

    def setUp(self):
        # 接口信息
        self.name = '发言'
        self.url = '/chatnew/msg'
        self.method = 'get'
        # 默认报错信息
        self.info = ''
        # 默认登录用户
        self.user = UID
        # 默认请求数据
        self.data = dict(data='测试弹幕', cid=cid)

    '''参数必填检验'''

    def test_01(self):
        '''参数必填检验-未登录发言'''
        self.user = ''
        self.exp_res = {'status': False, 'code': '101', 'data': [], 'message': '未登录'}

    def test_02(self):
        '''参数必填检验-未传data'''
        self.exp_res = {'code': '202', 'status': False, 'message': '消息不能为空'}
        self.data['data'] = ''

    def test_03(self):
        '''参数必填检验-未传cid'''
        self.exp_res = {'code': '1001', 'status': False, 'message': '房间不存在'}
        self.data['cid'] = ''

    '''业务-发言内容'''

    def test_04(self):
        '''业务-发言内容'''
        self.exp_res = {'code': 200, 'data': {'barrage': {'msg': self.data['data']}}}
        self.user = self.create_user()

    '''业务-字数限制'''

    def test_05(self):
        '''业务-字数限制'''
        self.exp_res = {'code': '206', 'status': False, 'message': '您的发言已超出字符限制了~'}
        self.user = self.create_user()
        self.data['data'] = '01234567890123456789012345678901234567890123456789'

    # '''业务-敏感词'''
    #
    # def test_06(self):
    #     '''业务-敏感词'''
    #     self.exp_res = self.exp_res_api = {'code': '271', 'status': False, 'message': '发言包含敏感词，请重新输入'}
    #     self.user = user[3]['uid']
    #     self.data['data'] = '习近平'

    '''业务-发言间隔判断'''

    def test_07(self):
        '''业务-发言间隔'''
        self.exp_res = {'status': False, 'code': '204', 'message': '你发言太快！'}
        self.user = self.create_user()
        User.set_chat_time(self.user)

    '''业务-未绑定手机判断'''

    def test_08(self):
        '''业务-未绑定手机'''
        self.exp_res = {'code': '2031', 'status': False, 'message': '绑定手机号即可发言'}
        self.user = self.create_user(False)

    # '''业务-注册时间判断'''
    #
    # def test_msg_09(self):
    #     '''业务-注册时间判断'''
    #     self.exp_res = {'code': '2018', 'status': False, 'message': '您刚来,还得2分钟才能发言~'}
    #     self.user = user[5]['uid']
    #     # 设置用户注册时间
    #     user_info_key = 'hm_{}'.format(self.user)
    #     user_info = json.loads(REDIS_INST.get(user_info_key))
    #     user_info['regtime'] = int(time.time())
    #     REDIS_INST.set(user_info_key, json.dumps(user_info))
    #     # 设置房间发言限制
    #     key = 'hm_chat_limit_admin_{}'.format(cid)
    #     REDIS_INST.hset(key, 'regTime', '120')

    '''业务-用户被禁言'''

    def test_10(self):
        '''业务-用户被禁言'''
        self.exp_res = {'status': False, 'code': '203', 'message': '抱歉,您已被禁言!详情请咨询客服!'}
        self.user = self.create_user()
        Common.gag(self.user, anchor, cid)

    '''业务-角色功能判断'''

    def test_11(self):
        '''业务-角色功能判断-房管'''
        self.exp_res = {'code': 200, 'data': {'extend': {'is_fg': '1'}}}
        self.user = self.create_user()
        User.set_fg(cid, self.user)

    def test_12(self):
        '''业务-角色功能判断-房主'''
        self.exp_res = {'code': 200, 'data': {'extend': {'is_zb': '1'}}}
        self.user = anchor

    # @unittest.skip('')
    # def test_msg_12(self):
    #     '''业务-角色功能判断-超管'''
    #     self.exp_res = ''
    #     self.user = superuid

    '''业务-彩色弹幕逻辑'''
    # @unittest.skip('主从同步20s太坑')
    def test_13(self):
        '''业务-彩色弹幕'''
        self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}
        self.user = self.create_user()
        # 添加用户弹幕卡和货币
        Bag.add_bag(self.user)
        MoneyClass.set_money(self.user, 10)
        self.data['color_barrage'] = 1

        # 二次验证函数
        self.ver = lambda: Bag.get_dmk(self.user) == 0 and MoneyClass.get_money(self.user)['coin'] == 10

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
    def test_14(self):
        '''弹幕卡不足，余额足时，发言彩色弹幕'''
        self.exp_res = {'code': 200, 'data': {'barrage': {'type': '300', 'color': '#e24040', 'num': '0', 'msg': '测试弹幕'}}}
        self.user = self.create_user()
        self.data['color_barrage'] = 1
        MoneyClass.set_money(self.user, 1)
        # 二次验证函数
        self.ver = lambda: MoneyClass.get_money(self.user)['coin'] == 0

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

    def test_15(self):
        '''业务-图标-粉丝'''
        self.exp_res = {'code': 200, 'data': {'fans': {'cid': cid,
                                                       'level': '25', 'name': '粉丝'}}}
        self.user = self.create_user()
        # 设置用户粉丝等级
        User.set_fs_level(self.user, cid)

    def test_16(self):
        '''业务-图标-徽章'''
        self.exp_res = {'code': 200, 'data': {'badge': [{'bid': '1', }]}}
        self.user = self.create_user()
        User.set_badge(self.user)

    def tearDown(self):
        # 比较结果
        req(self)
