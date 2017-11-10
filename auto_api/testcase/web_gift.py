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
import unittest
import sys
import time
import json

sys.path.append('../')
from lib import *
from common.common import Common

# from config import *

'''数据准备'''
# Common.generate_room('gift', 1)
# Common.generate_user('gift', 20)
# exit()
room = {'fg': {0: {'name': 'gift1510039356', 'uid': '5603'}},
        'room': {'rid': '497373', 'cid': '119488'},
        'anchor': {'name': 'gift1510039347', 'uid': '5602'}}
anchor = room['anchor']['uid']
cid = room['room']['cid']
user = {0: {'name': 'gift1510039357', 'uid': '5604'},
        1: {'name': 'gift1510039358', 'uid': '5605'},
        2: {'name': 'gift1510039360', 'uid': '5606'},
        3: {'name': 'gift1510039361', 'uid': '5607'},
        4: {'name': 'gift1510039363', 'uid': '5608'},
        5: {'name': 'gift1510039364', 'uid': '5609'},
        6: {'name': 'gift1510039366', 'uid': '5610'},
        7: {'name': 'gift1510039368', 'uid': '5611'},
        8: {'name': 'gift1510039369', 'uid': '5612'},
        9: {'name': 'gift1510039371', 'uid': '5613'},
        10: {'name': 'gift1510039372', 'uid': '5614'},
        11: {'name': 'gift1510039374', 'uid': '5615'},
        12: {'name': 'gift1510039375', 'uid': '5616'},
        13: {'name': 'gift1510039377', 'uid': '5617'},
        14: {'name': 'gift1510039379', 'uid': '5618'},
        15: {'name': 'gift1510039380', 'uid': '5619'},
        16: {'name': 'gift1510039382', 'uid': '5620'},
        17: {'name': 'gift1510039384', 'uid': '5621'},
        18: {'name': 'gift1510039385', 'uid': '5622'},
        19: {'name': 'gift1510039387', 'uid': '5623'}}
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

    def setUp(self):
        # 接口信息
        self.name = '送礼'
        self.url = '/chatnew/sendGift'
        self.method = 'get'
        # 默认报错信息
        self.info = ''
        # 默认登录用户
        self.user = ''
        # 默认请求数据
        self.data = {
            'cid': cid,
            'gift': gift['gift_id'],
            't_count': '1',
            # 'isbag': ''
        }

    '''参数必填检验'''

    def test_gift_01(self):
        '''参数必填检验-无cid参数'''
        self.user = user[0]['uid']
        self.data['cid'] = ''
        self.exp_res = {'message': '房间不存在', 'code': 1001, 'status': False}

    def test_gift_02(self):
        '''参数必填检验-无t_count参数'''
        self.user = user[0]['uid']
        self.data['t_count'] = ''
        self.exp_res = {'status': False, 'code': 1001, 'message': '请选择数量'}

    def test_gift_03(self):
        '''参数必填检验-未登录'''
        self.exp_res = {'status': False, 'code': '101', 'data': [], 'message': '未登录'}

    '''业务-角色'''

    def test_gift_04(self):
        '''业务-角色-房主'''
        self.user = anchor
        self.exp_res = {'status': False, 'code': 219, 'message': '自己不能给自己送礼物'}

    def test_gift_05(self):
        '''业务-角色-房管'''
        self.user = room['fg'][0]['uid']
        self.exp_res = {'status': True, 'code': 200, 'data': {'extend': {'is_fg': '1', 'is_zb': '0', 'is_guard': '0'}}}
        Common.set_money(self.user, 1)

    def test_gift_06(self):
        '''业务-角色-粉丝'''
        self.user = user[0]['uid']
        self.exp_res = {'code': 200, 'data': {'fans': {'cid': room['room']['cid'],
                                                       'zb_name': room['anchor']['name'],
                                                       'rid': room['room']['rid'],
                                                       'level': '25', 'name': '粉丝'}}}
        Common.set_money(self.user, 1)
        key = 'hm_loveliness_fan_lv_news_{}_{}'.format(self.user, room['room']['cid'])
        Common.REDIS_INST.set(key, 25)

    # def test_gift_03(self):
    #     '''基本-赠送人-粉丝-首次获取粉丝'''
    #     pass
    #
    # def test_gift_04(self):
    #     '''基本-赠送人-粉丝-首次6级'''
    #     pass
    '''业务-显示图标'''

    def test_gift_07(self):
        '''业务-显示图标-徽章'''
        self.exp_res = {'code': 200, 'data': {'badge': [{'bid': '1', }]}}
        self.user = user[1]['uid']
        key = 'hm_member_adorn_badge:{}'.format(self.user)
        Common.REDIS_INST.hset(key, 'bid:1', '{"bid":1,"gettime":' + str(int(time.time())) + ',"owntime":1440,"currentstat":3}')
        Common.set_money(self.user, 1)

    def test_gift_08(self):
        '''业务-显示图标-守护'''
        self.exp_res = {'code': 200, 'data': {'extend': {'is_guard': '2'}}}
        self.user = user[2]['uid']
        self.data['guard_barrage'] = 1
        Common.set_money(self.user, 1)

    '''业务-赠送爱心'''

    def test_gift_09(self):
        '''业务-赠送爱心-用户赠送爱心不足'''
        self.exp_res = {'message': '您剩余的仙豆数量不足！', 'status': False, 'code': 118}
        self.user = user[3]['uid']
        self.data['gift'] = 0

    def test_gift_10(self):
        '''业务-赠送爱心-用户赠送爱心增加经验主播增加仙能'''
        self.user = user[4]['uid']
        self.data['gift'] = 0
        self.exp_res = {'status': True, 'code': 200, 'data': {}}
        Common.set_xd(self.user, 1000)
        # 获取用户平台经验,主播仙能
        user_experience = Common.get_experience(self.user)[0]
        anchor_experience = Common.get_experience(room['anchor']['uid'])[1]
        self.ver = lambda: Common.get_experience(self.user)[0] == user_experience + 1000 and \
                           Common.get_experience(room['anchor']['uid'])[1] == anchor_experience + 1000

    '''业务-礼物配置'''

    def test_gift_11(self):
        '''业务-礼物配置-礼物未启用'''
        self.exp_res = {'status': False, 'message': '礼物未激活', 'code': 211}
        self.user = user[5]['uid']
        self.data['gift'] = 1
        Common.set_money(self.user, 1)

    def test_gift_12(self):
        '''业务-礼物配置-道具名称,id,赠送语'''
        self.exp_res = {'status': True, 'code': 200,
                        'data': {'gift': {'word': gift['word'], 'send_count': '1', 'gift_id': gift['gift_id'], 'name': gift['name'],
                                          'resource_path': 'http://img.new.huomaotv.com.cn/'}}}
        self.user = user[6]['uid']
        Common.set_money(self.user, 1)


    def test_gift_13(self):
        '''业务-礼物配置-连击'''
        self.exp_res = {'status': True, 'code': 200, 'data': {'gift': {'current_count': '1', 'before_count': '0', 'repeat': {'img': ''}, }}}
        self.user = user[8]['uid']
        Common.set_money(self.user, 1)
        # 删除连击key
        key = 'hm_add_new_gift_num_{}_{}_{}'.format(self.user, gift['gift_id'], cid)
        Common.REDIS_INST.delete(key)

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
        self.user = user[9]['uid']
        self.data['t_count'] = gift['bp']['count']
        Common.set_money(self.user, 10, 1000)

    '''业务-粉丝值'''

    def test_gift_15(self):
        '''业务-粉丝值'''
        self.exp_res = {'status': True, 'code': 200, 'data': {}}
        self.user = user[10]['uid']
        Common.set_money(self.user, 1)
        get_loveliness = Common.loveliness('get', '5614', cid)
        self.ver = lambda: Common.loveliness('get', self.user, cid) == get_loveliness + gift['fan_exp']

    '''业务-余额'''

    def test_gift_16(self):
        '''业务-余额不足'''
        self.exp_res = {'message': '余额不足', 'status': False, 'code': 2032}
        self.user = user[11]['uid']

    def test_gift_17(self):
        '''业务-余额足够'''
        self.exp_res = {'status': True, 'code': 200, 'data': {}}
        self.user = user[12]['uid']
        Common.set_money(self.user, 1)
        get_money = Common.get_money(self.user)['coin']
        self.ver = lambda: Common.get_money(self.user)['coin'] == get_money - gift['mb']

    '''业务-送礼记录'''

    def test_gift_18(self):
        '''业务-送礼记录'''
        self.exp_res = {'status': True, 'code': 200, 'data': {}}
        self.user = user[13]['uid']
        Common.set_money(self.user, 1)
        send_gift_count = Common.get_money_pay(self.user, cid)
        self.ver = lambda: Common.get_money_pay(self.user, cid) == send_gift_count + 1

    '''业务-收礼记录'''

    def test_gift_19(self):
        '''业务-收礼记录,礼物中无宝箱'''
        self.exp_res = {'status': True, 'code': 200, 'data': {}}
        self.user = user[14]['uid']
        Common.set_money(self.user, 1)

        # 收礼记录
        get_gift_count = Common.money_income('count', anchor, self.user)
        self.ver = lambda: Common.money_income('count', anchor, self.user) == get_gift_count + 1

    def test_gift_20(self):
        '''业务-收礼记录,礼物中有宝箱'''
        self.exp_res = {'status': True, 'code': 200, 'data': {}}
        self.user = user[15]['uid']
        self.data['gift'] = '52'
        Common.set_money(self.user, 4)

        # 收礼记录,及收礼金额
        get_gift_count = Common.money_income('count', anchor, self.user)
        self.ver = lambda: Common.money_income('count', anchor, self.user) == get_gift_count + 1 and \
                           Common.money_income('get', anchor, self.user) == 2

    def tearDown(self):
        # 比较结果
        assert_res(self)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestGift('test_gift_21'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
