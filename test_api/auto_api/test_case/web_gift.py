#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/8/14 14:17
# Author : lixingyun
'''
1.全站横幅,单房间横幅无法判断
2.无平台升级提示
3.未判断守护用户
4.
'''
import time
import logging
import unittest
from ..lib.lib import req
from ..lib.config import UID
from huomao.user import User
from huomao.money import MoneyClass

'''数据准备'''
anchor = '5602'
cid = '119488'
# 礼物配置
gift = {'gift_id': '51',
        'word': 'send',
        'name': 'APITEST1',
        'bp': {'tx_frame': {'height': '15960',
                            'num': '38',
                            'time': '4'},
               'hf_time': '10',
               'count': '3',
               },
        'fan_exp': 1000,
        'mb': 1,
        }


class TestGift(unittest.TestCase):
    # 创建用户
    def create_user(self):
        uid = User.reg('noble')
        logging.info('注册用户UID：{}'.format(uid))
        User.bd_sj(uid)
        return uid

    def setUp(self):
        # 接口信息
        self.name = '送礼'
        self.url = '/chatnew/sendGift'
        self.method = 'get'
        # 默认报错信息
        # self.info = ''
        # 默认登录用户
        self.user = UID
        # 默认请求数据
        self.data = dict(cid=cid, gift=gift['gift_id'], t_count=1)
        self.exp_res = dict(code='1001', status=False, message='房间不存在')

    '''参数必填检验'''

    def test_gift_01(self):
        '''参数必填检验-无cid参数'''
        self.data['cid'] = ''
        self.exp_res = dict(code='1001', status=False, message='房间不存在')

    def test_gift_02(self):
        '''参数必填检验-无t_count参数'''
        self.data['t_count'] = ''
        self.exp_res = dict(code='1001', status=False, message='请选择数量')

    def test_gift_03(self):
        '''参数必填检验-未登录'''
        self.user = ''
        self.exp_res = dict(code='101', status=False, message='未登录')

    '''业务-角色'''

    def test_gift_04(self):
        '''业务-角色-房主'''
        self.user = anchor
        self.exp_res = dict(code='219', status=False, message='自己不能给自己送礼物')

    def test_gift_05(self):
        '''业务-角色-房管'''
        self.user = self.create_user()
        MoneyClass.set_money(self.user, 1)
        User.set_fg(cid, self.user)
        self.exp_res = dict(code=200, status=True, data=dict(extend=dict(is_fg='1')))

    def test_gift_06(self):
        '''业务-角色-粉丝'''
        self.user = self.create_user()
        MoneyClass.set_money(self.user, 1)
        User.set_fs_level(self.user, cid)
        self.exp_res = {'code': 200, 'data': {'fans': {'cid': cid, 'level': '25', 'name': '粉丝'}}}

    '''业务-显示图标'''

    def test_gift_07(self):
        '''业务-显示图标-徽章'''
        self.exp_res = {'code': 200, 'data': {'badge': [{'bid': '1', }]}}
        self.user = self.create_user()
        User.set_badge(self.user)
        MoneyClass.set_money(self.user, 1)

    '''业务-赠送爱心'''

    def test_gift_08(self):
        '''业务-赠送爱心-用户赠送爱心不足'''
        self.exp_res = {'message': '您剩余的仙豆数量不足！', 'status': False, 'code': '118'}
        self.user = self.create_user()
        self.data['gift'] = 0

    def test_gift_09(self):
        '''业务-赠送爱心-用户赠送爱心增加经验主播增加仙能'''
        self.user = self.create_user()
        self.data['gift'] = 0
        self.exp_res = {'status': True, 'code': 200}
        MoneyClass.set_xd(self.user, 1000)
        # 获取用户平台经验,主播仙能
        user_experience = User.get_experience(self.user)[0]
        anchor_experience = User.get_experience(anchor)[1]
        self.ver = lambda: User.get_experience(self.user)[0] == user_experience + 1000 and \
                           User.get_experience(anchor)[1] == anchor_experience + 1000

    '''业务-礼物配置'''

    def test_gift_11(self):
        '''业务-礼物配置-礼物未启用'''
        self.exp_res = {'status': False, 'message': '礼物未激活', 'code': '211'}
        self.user = self.create_user()
        self.data['gift'] = 1
        MoneyClass.set_money(self.user, 1)

    def test_gift_12(self):
        '''业务-礼物配置-道具名称,id,赠送语'''
        self.exp_res = {'status': True, 'code': 200,
                        'data': {'gift': {'word': gift['word'], 'send_count': '1', 'gift_id': gift['gift_id'], 'name': gift['name'],
                                          'resource_path': 'http://img.new.huomaotv.com.cn/'}}}
        self.user = self.create_user()
        MoneyClass.set_money(self.user, 1)

    def test_gift_13(self):
        '''业务-礼物配置-连击'''
        self.exp_res = {'status': True, 'code': 200, 'data': {'gift': {'current_count': '1', 'before_count': '0', 'repeat': {'img': ''}, }}}
        self.user = self.create_user()
        MoneyClass.set_money(self.user, 1)

    def test_gift_14(self):
        '''业务-礼物配置-霸屏特效,横幅'''
        self.exp_res = {
            'status': True,
            'code': 200,
            'data': {
                'gift': {
                    'screen_effect': {
                        'effect': '',
                        'frame': {
                            'time': gift['bp']['tx_frame']['time'],
                            'height': gift['bp']['tx_frame']['height'],
                            'num': gift['bp']['tx_frame']['num'],
                            'img': ''
                        }
                    },
                    'screen_hf': {
                        'time': gift['bp']['hf_time']
                    }
                }
            }
        }
        self.user = self.create_user()
        self.data['t_count'] = gift['bp']['count']
        MoneyClass.set_money(self.user, 10, 1000)

    '''业务-粉丝值'''

    def test_gift_15(self):
        '''业务-粉丝值'''
        self.exp_res = {'status': True, 'code': 200, 'data': {}}
        self.user = self.create_user()
        MoneyClass.set_money(self.user, 1)
        get_loveliness = User.loveliness('get', self.user, cid)
        self.ver = lambda: User.loveliness('get', self.user, cid) == get_loveliness + gift['fan_exp']

    '''业务-余额'''

    def test_gift_16(self):
        '''业务-余额不足'''
        self.exp_res = {'message': '余额不足', 'status': False, 'code': '2032'}
        self.user = self.create_user()

    def test_gift_17(self):
        '''业务-余额足够'''
        self.exp_res = {'status': True, 'code': 200}
        self.user = self.create_user()
        MoneyClass.set_money(self.user, 1)
        get_money = MoneyClass.get_money(self.user)['coin']
        self.ver = lambda: MoneyClass.get_money(self.user)['coin'] == get_money - gift['mb']

    '''业务-送礼记录'''

    def test_gift_18(self):
        '''业务-送礼记录'''
        self.exp_res = {'status': True, 'code': 200, 'data': {}}
        self.user = self.create_user()
        MoneyClass.set_money(self.user, 1)
        send_gift_count = MoneyClass.get_money_pay(self.user, cid)
        self.ver = lambda: MoneyClass.get_money_pay(self.user, cid) == send_gift_count + 1

    '''业务-收礼记录'''

    def test_gift_19(self):
        '''业务-收礼记录,礼物中无宝箱'''
        self.exp_res = {'status': True, 'code': 200, 'data': {}}
        self.user = self.create_user()
        MoneyClass.set_money(self.user, 1)

        # 收礼记录
        get_gift_count = MoneyClass.money_income('count', anchor, self.user)
        self.ver = lambda: MoneyClass.money_income('count', anchor, self.user) == get_gift_count + 1

    def test_gift_20(self):
        '''业务-收礼记录,礼物中有宝箱'''
        self.exp_res = {'status': True, 'code': 200, 'data': {}}
        self.user = self.create_user()
        self.data['gift'] = '52'
        MoneyClass.set_money(self.user, 4)

        # 收礼记录,及收礼金额
        get_gift_count = MoneyClass.money_income('count', anchor, self.user)
        self.ver = lambda: MoneyClass.money_income('count', anchor, self.user) == get_gift_count + 1 and \
                           MoneyClass.money_income('get', anchor, self.user) == 2

    def tearDown(self):
        # 比较结果
        req(self)
