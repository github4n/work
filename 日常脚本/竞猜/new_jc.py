#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/12/6 11:39
# Author : lixingyun
# 竞猜分为 赛事/主播  对冲/坐庄 仙豆/猫豆
# 本脚本主要测试结算功能,无下注,坐庄时结算手动测试
import unittest
from nose_parameterized import parameterized
import requests
import time
import logging
from common.common import Common

logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S %p',
                    level=logging.INFO,
                    # filename='example.log',
                    filemode='w')

URL = 'http://lxy.new.huomaotv.com.cn'
# 后台url
ADMIN_URL = 'http://lxyadmin.new.huomaotv.com.cn'
# 后台cookies
ADMIN_COOKIES = {'huomaotvcheckcode': 'SQJ5', 'adminId': '33', 'adminAccount': 'root',
                 'adminNick': 'root', 'adminUserId': '0', 'adminLoginTime': '1473220408',
                 'adminToken': 'bd2c21cb89ada618b16170504ad9f84d'}


# 创建盘口
def create(**kw):
    data = {
        'guess_type': 'not_anchor',  # 竞猜类型,anchor:主播,其他:赛事
        'match_id_or_room_number': '4685',  # 比赛ID/房间号
        'play_type': 'gamble',  # 竞猜玩法,对赌:gamble,坐庄:banker
        'title': '赛事对赌竞猜测试',  # 竞猜标题
        'option_A': '选项A',  # 选项A
        'option_B': '选项B',  # 选项B
        'expire': str(int(time.time()))  # 竞猜封盘时间
    }
    for key in kw:
        if key in data:
            data[key] = kw.get(key)
    # res = requests.post(ADMIN_URL+'/guessnew/create_save', data=data, cookies=ADMIN_COOKIES)
    # logging.info(res.json())
    period = '盘口ID:123456'
    logging.info(period)
    logging.info('开盘')
    return period


# 下注
def bet(uid, **kw):
    data = {
        'period': '',  # 期号
        'chose': 'option_A',  # 竞猜选项option_A, option_B
        'coin_type': 'free_bean',  # 货币类型仙豆free_bean,猫豆cat_bean
        'amount': 100  # 下注金额
    }
    for key in kw:
        if key in data:
            data[key] = kw.get(key)
    # res = requests.get(URL + '/guessnew/bet', param=data, cookies=Common.generate_cookies(uid))
    # logging.info(res.json())
    logging.info('用户{}'.format(uid) + '下注:期号{period}选项{chose}货币类型{coin_type}下注额{amount}'.format_map(data))


# 结算
def settlement(**kw):
    data = {
        'cid': '2',  # 房间号
        'period': '',  # 期号
        'win_option': 'option_A'  # 开奖结果option_A,option_B,loss流局,dogfall平局
    }
    for key in kw:
        if key in data:
            data[key] = kw.get(key)
    # res = requests.post(ADMIN_URL+'/guessnew/create_save', data=data, cookies=ADMIN_COOKIES)
    # logging.info(res.json())
    logging.info('结算')


# 格式化测试数据
def format_data(period_lists):
    case_lists = []
    for i in period_lists:
        list_dict = []
        list_dict.append(i)
        tuple_dict = tuple(list_dict)
        case_lists.append(tuple_dict)
    return case_lists

    # logging.info(case_lists)


# 这边的金额表示猫豆和仙豆同时下的金额,预期收益,option_AB表示两个选项的下注,
period_lists = [
    # 结算A
    # 结算A,当选项A有下注,B无下注,单
    {'option_A': {'5524': (100, 0)}, 'option_B': None, 'res': 'option_A'},
    # 结算A,当选项A有下注,B无下注,多
    {'option_A': {'5524': (100, 0), '5525': (100, 0)}, 'option_B': None, 'res': 'option_A'},
    # 结算A,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {'5524': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {'5524': (100, -100), '5525': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (1, -1)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {'5524': (1, 9)}, 'option_B': {'5525': (10, -10)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {'5524': (1, 95)}, 'option_B': {'5525': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {'5524': (10, 95)}, 'option_B': {'5525': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {'5524': (1000, 950)}, 'option_B': {'5525': (1000, -1000)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (1, -1), '5527': (1, -1)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {'5524': (1, 9), '5525': (1, 9)}, 'option_B': {'5526': (10, -10), '5527': (10, -10)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {'5524': (1, 95), '5525': (1, 95)}, 'option_B': {'5526': (100, -100), '5527': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {'5524': (10, 126), '5525': (20, 253)}, 'option_B': {'5526': (100, -100), '5527': (300, -300)}, 'res': 'option_A'},
    # 结算B
    # 结算B,当选项A有下注,B无下注,单
    {'option_A': {'5524': (100, -100)}, 'option_B': None, 'res': 'option_B'},
    # 结算B,当选项A有下注,B无下注,多
    {'option_A': {'5524': (100, -100), '5525': (100, -100)}, 'option_B': None, 'res': 'option_B'},
    # 结算B,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {'5524': (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {'5524': (100, 0), '5525': (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {'5524': (1, -1)}, 'option_B': {'5525': (1, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {'5524': (1, -1)}, 'option_B': {'5525': (10, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {'5524': (1, -1)}, 'option_B': {'5525': (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {'5524': (10, -10)}, 'option_B': {'5525': (100, 9)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {'5524': (1000, -1000)}, 'option_B': {'5525': (1000, 950)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {'5524': (1, -1), '5525': (1, -1)}, 'option_B': {'5526': (1, 0), '5527': (1, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {'5524': (1, -1), '5525': (1, -1)}, 'option_B': {'5526': (10, 0), '5527': (10, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {'5524': (1, -1), '5525': (1, -1)}, 'option_B': {'5526': (100, 0), '5527': (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {'5524': (10, -10), '5525': (20, -20)}, 'option_B': {'5526': (100, 7), '5527': (300, 21)}, 'res': 'option_B'},
    # 结算:流局
    # 流局,当选项A有下注,B无下注,单
    {'option_A': {'5524': (100, 0)}, 'option_B': None, 'res': 'loss'},
    # 流局,当选项A有下注,B无下注,多
    {'option_A': {'5524': (100, 0), '5525': (100, 0)}, 'option_B': None, 'res': 'loss'},
    # 流局,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {'5524': (100, 0)}, 'res': 'loss'},
    # 流局,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {'5524': (100, 0), '5525': (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (1, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (10, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {'5524': (10, 0)}, 'option_B': {'5525': (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {'5524': (1000, 0)}, 'option_B': {'5525': (1000, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (1, 0), '5527': (1, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (10, 0), '5527': (10, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (100, 0), '5527': (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {'5524': (10, 0), '5525': (20, 0)}, 'option_B': {'5526': (100, 0), '5527': (300, 0)}, 'res': 'loss'},
    # 结算:平局
    # 平局,当选项A有下注,B无下注,单
    {'option_A': {'5524': (100, 0)}, 'option_B': None, 'res': 'dogfall'},
    # 平局,当选项A有下注,B无下注,多
    {'option_A': {'5524': (100, 0), '5525': (100, 0)}, 'option_B': None, 'res': 'dogfall'},
    # 平局,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {'5524': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {'5524': (100, 0), '5525': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (1, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (10, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {'5524': (10, 0)}, 'option_B': {'5525': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {'5524': (1000, 0)}, 'option_B': {'5525': (1000, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (1, 0), '5527': (1, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (10, 0), '5527': (10, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (100, 0), '5527': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {'5524': (10, 0), '5525': (20, 0)}, 'option_B': {'5526': (100, 0), '5527': (300, 0)}, 'res': 'dogfall'},
]

'''赛事竞猜,对冲竞猜'''


class TestGuess(unittest.TestCase):
    case_lists = format_data(period_lists)
    def setUp(self):
        pass

    @parameterized.expand(case_lists)
    def test(self, kw):
        # 开盘
        period = create()
        # 下注
        data = []
        for key, value in kw.items():
            if value is not None and (key == 'option_A' or key == 'option_B'):
                # 用户循环下注
                for uid, amounts in value.items():
                    xd = Common.get_xd(uid)  # 获取仙豆
                    md = Common.get_money(uid)['bean']  # 获取猫豆
                    # 获取用户的货币信息,预期货币信息
                    data.append((uid, xd, md, amounts[1]))
                    bet(uid=uid, period=period, chose=key, coin_type='free_bean', amount=amounts[0])
                    # self.assertEqual(Common.get_xd(uid), xd - amount, '仙豆未扣除')
                    bet(uid=uid, period=period, chose=key, coin_type='cat_bean', amount=amounts[0])
                    # self.assertEqual(Common.get_money(uid)['bean'], md - amount, '猫豆未扣除')
        # 结算
        settlement(period=period, option=kw['res'])
        # 验证结果
        for uid, xd, md, exp in data:
            self.assertEqual(Common.get_xd(uid), xd + exp, '仙豆结算错误')
            self.assertEqual(Common.get_money(uid)['bean'], md + exp, '猫豆结算错误')

    def tearDown(self):
        pass


period_lists2 = [
    # 结算A
    # 结算A,当选项A有下注,B无下注,单
    {'option_A': {'5524': (100, 0)}, 'option_B': None, 'res': 'option_A'},
    # 结算A,当选项A有下注,B无下注,多
    {'option_A': {'5524': (100, 0), '5525': (100, 0)}, 'option_B': None, 'res': 'option_A'},
    # 结算A,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {'5524': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {'5524': (100, -100), '5525': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (1, -1)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {'5524': (1, 9)}, 'option_B': {'5525': (10, -10)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {'5524': (1, 95)}, 'option_B': {'5525': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {'5524': (10, 95)}, 'option_B': {'5525': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {'5524': (1000, 950)}, 'option_B': {'5525': (1000, -1000)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (1, -1), '5527': (1, -1)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {'5524': (1, 9), '5525': (1, 9)}, 'option_B': {'5526': (10, -10), '5527': (10, -10)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {'5524': (1, 95), '5525': (1, 95)}, 'option_B': {'5526': (100, -100), '5527': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {'5524': (10, 126), '5525': (20, 253)}, 'option_B': {'5526': (100, -100), '5527': (300, -300)}, 'res': 'option_A'},
    # 结算B
    # 结算B,当选项A有下注,B无下注,单
    {'option_A': {'5524': (100, -100)}, 'option_B': None, 'res': 'option_B'},
    # 结算B,当选项A有下注,B无下注,多
    {'option_A': {'5524': (100, -100), '5525': (100, -100)}, 'option_B': None, 'res': 'option_B'},
    # 结算B,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {'5524': (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {'5524': (100, 0), '5525': (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {'5524': (1, -1)}, 'option_B': {'5525': (1, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {'5524': (1, -1)}, 'option_B': {'5525': (10, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {'5524': (1, -1)}, 'option_B': {'5525': (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {'5524': (10, -10)}, 'option_B': {'5525': (100, 9)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {'5524': (1000, -1000)}, 'option_B': {'5525': (1000, 950)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {'5524': (1, -1), '5525': (1, -1)}, 'option_B': {'5526': (1, 0), '5527': (1, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {'5524': (1, -1), '5525': (1, -1)}, 'option_B': {'5526': (10, 0), '5527': (10, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {'5524': (1, -1), '5525': (1, -1)}, 'option_B': {'5526': (100, 0), '5527': (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {'5524': (10, -10), '5525': (20, -20)}, 'option_B': {'5526': (100, 7), '5527': (300, 21)}, 'res': 'option_B'},
    # 结算:流局
    # 流局,当选项A有下注,B无下注,单
    {'option_A': {'5524': (100, 0)}, 'option_B': None, 'res': 'loss'},
    # 流局,当选项A有下注,B无下注,多
    {'option_A': {'5524': (100, 0), '5525': (100, 0)}, 'option_B': None, 'res': 'loss'},
    # 流局,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {'5524': (100, 0)}, 'res': 'loss'},
    # 流局,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {'5524': (100, 0), '5525': (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (1, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (10, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {'5524': (10, 0)}, 'option_B': {'5525': (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {'5524': (1000, 0)}, 'option_B': {'5525': (1000, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (1, 0), '5527': (1, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (10, 0), '5527': (10, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (100, 0), '5527': (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {'5524': (10, 0), '5525': (20, 0)}, 'option_B': {'5526': (100, 0), '5527': (300, 0)}, 'res': 'loss'},
    # 结算:平局
    # 平局,当选项A有下注,B无下注,单
    {'option_A': {'5524': (100, 0)}, 'option_B': None, 'res': 'dogfall'},
    # 平局,当选项A有下注,B无下注,多
    {'option_A': {'5524': (100, 0), '5525': (100, 0)}, 'option_B': None, 'res': 'dogfall'},
    # 平局,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {'5524': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {'5524': (100, 0), '5525': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (1, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (10, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {'5524': (1, 0)}, 'option_B': {'5525': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {'5524': (10, 0)}, 'option_B': {'5525': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {'5524': (1000, 0)}, 'option_B': {'5525': (1000, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (1, 0), '5527': (1, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (10, 0), '5527': (10, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {'5524': (1, 0), '5525': (1, 0)}, 'option_B': {'5526': (100, 0), '5527': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {'5524': (10, 0), '5525': (20, 0)}, 'option_B': {'5526': (100, 0), '5527': (300, 0)}, 'res': 'dogfall'},
]

'''赛事竞猜,坐庄竞猜'''


class TestGuess1(unittest.TestCase):
    case_lists = format_data(period_lists)
    def setUp(self):
        pass

    @parameterized.expand(case_lists)
    def test(self, kw):
        # 开盘
        period = create()
        # 下注
        data = []
        for key, value in kw.items():
            if value is not None and (key == 'option_A' or key == 'option_B'):
                # 用户循环下注
                for uid, amounts in value.items():
                    xd = Common.get_xd(uid)  # 获取仙豆
                    md = Common.get_money(uid)['bean']  # 获取猫豆
                    # 获取用户的货币信息,预期货币信息
                    data.append((uid, xd, md, amounts[1]))
                    bet(uid=uid, period=period, chose=key, coin_type='free_bean', amount=amounts[0])
                    # self.assertEqual(Common.get_xd(uid), xd - amount, '仙豆未扣除')
                    bet(uid=uid, period=period, chose=key, coin_type='cat_bean', amount=amounts[0])
                    # self.assertEqual(Common.get_money(uid)['bean'], md - amount, '猫豆未扣除')
        # 结算
        settlement(period=period, option=kw['res'])
        # 验证结果
        for uid, xd, md, exp in data:
            self.assertEqual(Common.get_xd(uid), xd + exp, '仙豆结算错误')
            self.assertEqual(Common.get_money(uid)['bean'], md + exp, '猫豆结算错误')

    def tearDown(self):
        pass



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestGuess('test_9'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

# unittest.main()

# test_dir = './'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='new_jc.py')
# for i in discover:
#     print(i)
