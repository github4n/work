#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/8/14 14:17
# Author : lixingyun
'''
1.全站横幅无法判断
2.无平台升级提示
3.未判断守护用户
4.
'''
import unittest
import sys

sys.path.append('../')
from lib import *
from common.common import Common
# from config import *
import time
import json

'''数据准备'''
common = Common()
# common.generate_room('gift', 1)
# common.generate_user('gift', 20, True)
# exit()
# generate_user('gift', 20, True)
# generate_user('gift', 1)
# exit()
room_data = {'cid': 119465, 'fz_name': 'gift1505185802', 'fg_id': [5386], 'fz_id': 5385, 'fg_name': ['gift1505185803'], 'room_number': 461811}
user_data = {
    'user_names': ['gift1504855086', 'gift1504855088', 'gift1504855089', 'gift1504855091', 'gift1504855093', 'gift1504855094', 'gift1504855096',
                   'gift1504855097', 'gift1504855099', 'gift1504855101', 'gift1504855102', 'gift1504855105', 'gift1504855107', 'gift1504855108',
                   'gift1504855110', 'gift1504855111', 'gift1504855114', 'gift1504855115', 'gift1504855117', 'gift1504855118'],
    'user_ids': [5336, 5337, 5338, 5339, 5340, 5341, 5342, 5343, 5344, 5345, 5346, 5347, 5348, 5349, 5350, 5351, 5352, 5353, 5354, 5355]}

anchor = room_data['fz_id']
fg = room_data['fg_id']
cid = room_data['cid']
user_ids = user_data['user_ids']
exp_dict = interface['gift']['exp_dict']


class TestGift(unittest.TestCase):
    '''基本-赠送人'''

    def test_gift_01(self):
        '''基本-赠送人-房主'''
        assert_res(sys._getframe(), 'gift', anchor, exp_dict['anchor'], cid=cid)

    def test_gift_02(self):
        '''基本-赠送人-房管'''
        user = fg[0]
        common.set_money(user, 1000)
        exp = {'status': True, 'code': 200, 'data': {'extend': {'is_fg': '1', 'is_zb': '0', 'is_guard': '0'}}}
        assert_res(sys._getframe(), 'gift', fg[0], exp, cid=cid, gift=48)

    def test_gift_03(self):
        '''基本-赠送人-粉丝-首次获取粉丝'''
        pass

    def test_gift_04(self):
        '''基本-赠送人-粉丝-首次6级'''
        pass


    '''赠送爱心'''

    def test_gift_101(self):
        '''用户赠送爱心不足'''
        assert_res(sys._getframe(), 'gift', user_ids[0], exp_dict['insufficient_xd'], cid=cid)

    def test_gift_102(self):
        '''用户赠送爱心增加经验'''
        user = user_ids[1]
        common.set_xd(user_ids[1], 1000)
        # 获取用户平台经验,主播仙能
        user_experience = common.get_experience(user)[0]
        anchor_experience = common.get_experience(anchor)[1]

        def ver():
            user_experience2 = common.get_experience(user)[0]
            anchor_experience2 = common.get_experience(anchor)[1]
            if user_experience2 == user_experience + 1000 and anchor_experience2 == anchor_experience + 1000:
                return True
            else:
                return False

        assert_res(sys._getframe(), 'gift', user, {}, ver=ver, cid=cid)

        common.set_xd(user, 0)

    '''礼物特效'''

    def test_gift_103(self):
        '''礼物未启用'''
        user = user_ids[2]
        common.set_money(user, 1000)
        assert_res(sys._getframe(), 'gift', user, exp_dict['not_active'], cid=cid, gift=47)

    def test_gift_104(self):
        '''礼物已启用,无特效,收礼记录,送礼记录,粉丝值,赠送语,余额,判断'''
        user = user_ids[3]
        common.set_money(user, 1, 1000)
        exp = {'status': True, 'code': 200, 'data': {'gift': {'word': 'send', 'send_count': '1', 'gift_id': '48', 'name': '脚本测试礼物48(勿修改)',
                                                              'resource_path': 'http://img.new.huomaotv.com.cn/'}}}
        # 获取送礼和收礼记录,粉丝值,余额
        send_gift_count1 = common.get_money_pay(user)
        get_gift_count1 = common.get_money_income(anchor)
        get_loveliness1 = common.get_loveliness(user, cid)
        get_money1 = common.get_money(user)['coin']

        def ver():
            send_gift_count2 = common.get_money_pay(user)
            get_gift_count2 = common.get_money_income(anchor)
            get_loveliness2 = common.get_loveliness(user, cid)
            get_money2 = common.get_money(user)['coin']
            if send_gift_count2 == send_gift_count1 + 1 and get_gift_count2 == get_gift_count1 + 1 and get_loveliness2 == get_loveliness1 + 2000 and get_money2 == get_money1 - 1:
                return True
            else:
                return False

        assert_res(sys._getframe(), 'gift', user, exp, ver=ver, cid=cid, gift=48)

    def test_gift_105(self):
        '''连击'''
        user = user_ids[4]
        common.set_money(user, 1, 1000)
        num_key = 'hm_add_new_gift_num_{}_{}_{}'.format(user, 49, cid)
        common.REDIS_INST.delete(num_key)
        exp = {'status': True, 'code': 200, 'data': {'gift': {'current_count': '1', 'before_count': '0', 'repeat': {'img': ''}, }}}
        assert_res(sys._getframe(), 'gift', user, exp, cid=cid, gift=49)

    def test_gift_106(self):
        '''霸屏特效,横幅'''
        user = user_ids[5]
        common.set_money(user, 10, 1000)
        exp = {'status': True, 'code': 200, 'data': {
            'gift': {'screen_effect': {'effect': '', 'frame': {'time': '4', 'height': '15960', 'num': '38', 'img': ''}},
                     'screen_hf': {'time': '10'}}}}
        assert_res(sys._getframe(), 'gift', user, exp, cid=cid, gift=49, t_count=3)

    def test_gift_107(self):
        '''单房间弹幕横幅'''
        user = user_ids[6]
        common.set_money(user, 10, 1000)
        exp = {'status': True, 'code': 200, 'data': {'gift': {'barrage': {'effect': '', 'img': ''}}}}
        assert_res(sys._getframe(), 'gift', user, exp, cid=cid, gift=49, t_count=5)

    def test_gift_108(self):
        '''全房间弹幕横幅, 有宝箱,有宝箱礼物'''
        user = user_ids[7]
        common.set_money(user, 10)
        common.get_money_income(anchor, 1)

        # 判断收礼扣除宝箱礼物金额
        def ver():
            money = common.get_money_income(anchor, 2)
            return True if money == 8.00 else False

        exp = {'status': True, 'code': 200, 'data': {'gift': {'barrage': {'effect': '', 'img': ''}}}}
        assert_res(sys._getframe(), 'gift', user, exp, ver=ver, cid=cid, gift=50)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestGift('test_gift_02'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
