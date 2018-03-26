#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/12/6 11:39
# Author : lixingyun
# 竞猜分为 赛事/主播  对冲/坐庄 仙豆/猫豆
# 本脚本主要测试结算功能,无下注,坐庄时结算手动测试,超庄时,不同用户不同赔率时跨庄
import unittest
from nose_parameterized import parameterized
import requests
import time
import logging
from guess_case import banker_case_lists, gamble_case_lists
from common.common import Common
import json
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
        'guess_type': 'match',  # 竞猜类型,anchor:主播,match:赛事
        'match_id_or_room_number': '4685',  # 比赛ID/房间号
        'play_type': 'gamble',  # 竞猜玩法,对赌:gamble,坐庄:banker
        'title': '赛事对赌竞猜测试',  # 竞猜标题
        'opt_type': 'normal',  # 选项类型 normal,normal_3,normal_4,normal_5,money_line,ball
        # 'opt_items':['选项1','选项2'],
        # 'opt_items':{'选项1','选项2'},
        'opt_items[1]': '选项1',  # 选项1
        'opt_items[2]': '选项2',  # 选项2
        'expire': str(int(time.time()))  # 竞猜封盘时间
    }
    for key in kw:
        if key in data:
            data[key] = kw.get(key)
    res = requests.post(ADMIN_URL + '/guessnew/create_save', data=data, cookies=ADMIN_COOKIES)
    try:
        period = res.json()['period']
        logging.info('开盘{},{}'.format(period, res.json()))
        return period
    except:
        logging.error(res.text)


# 更新状态
def update_status(period, status):
    # res = requests.post(ADMIN_URL + '/guessnew/update_status', data=dict(period=period, status=status), cookies=ADMIN_COOKIES)
    res = requests.post(ADMIN_URL + '/guessnew/update_status/' + str(period) + '/' + str(status), cookies=ADMIN_COOKIES)
    logging.info('{}:{}'.format(status, res.json()))
    # return period


# 普通下注,坐庄,下注
def bet(uid, **kw):
    data = {
        'period': '',  # 期号
        'opt_type': 'normal',  # 选项类型 normal,normal_3,normal_4,normal_5,money_line,ball
        'chose': [
            {'chose':'1','amount':'100'},
            {'chose':'2','amount':'100'},
        ],  # 下注选项
        'coin_type': 'free_bean',  # 货币类型仙豆free_bean,猫豆cat_bean
        'punter': 'bet',  # bet:普通下注,'banker':坐庄, 'buyer':买庄
        'banker_odds': '',  # 赔率
    }
    for key in kw:
        if key in data:
            data[key] = kw.get(key)

    res = requests.get(URL + '/guessnew/bet', params=data, cookies=Common.generate_cookies(uid))
    try:
        res = res.json()
        res_info = '用户{}'.format(uid) + '操作类型{punter}:期号{period}选项{chose}货币类型{coin_type}赔率{banker_odds}返回'.format_map(data) + str(res)
        logging.info(res_info)
        logging.info(data)
        if data['punter'] == 'banker' and res['status'] == 'success':
            return res['data']['banker']['order_id']
    except ValueError:
        logging.info(res.text)


# 修改庄
def change_banker(uid, period, id, banker_odds='', type_='revoke'):
    data = {
        'period': period,  # 期号
        'id': id,
        'banker_odds': banker_odds,
    }
    res = requests.get(URL + '/guessnew/changeBanker/' + type_, params=data, cookies=Common.generate_cookies(uid))
    if type_ == 'revoke':
        logging.info('撤庄{}'.format(res.json()))
    else:
        logging.info('修改庄{}'.format(res.json()))


# 结算
def settlement(**kw):
    data = {
        'cid': '',  # 房间号
        'period': '',  # 期号
        'win_option': ''  # 开奖结果option_A,option_B,loss流局,dogfall平局
    }
    for key in kw:
        if key in data:
            data[key] = kw.get(key)
    res = requests.post(ADMIN_URL + '/guessnew/settlement', data=data, cookies=ADMIN_COOKIES)
    try:
        res1 = requests.get(URL + '/crontab/guessNewCalculation')
        logging.info('计算' + res1.text)
        res2 = requests.get(URL + '/crontab/guessNewSettlement')
        logging.info('结算' + res2.text)
    except:
        logging.info('超时')
    logging.info('结算选项:{}结果:{}'.format(data['win_option'], res.json()))


def new_name_func(func, num, p):
    # base_name = func.__name__
    # name_suffix = "_%s" % (num, )
    # if len(p.args) > 0 and isinstance(p.args[0], str):
    #     name_suffix += "_" + parameterized.to_safe_name(p.args[0])
    # return base_name + name_suffix
    return func.__name__ + '_' + p.args[0]


# 赛事竞猜,对冲竞猜
class TestGuessGamble(unittest.TestCase):
    @parameterized.expand(gamble_case_lists, name_func=new_name_func)
    def test(self, name, kw):
        logging.info('用例:' + name + '开始')
        # 开盘
        period = create(guess_type='match', play_type='gamble')
        # 下注
        data = []
        for uid, value in kw.items():
            # 获取用户的货币信息,预期货币信息
            xd = Common.get_xd(uid)  # 获取仙豆
            md = Common.get_money(uid)['bean']  # 获取猫豆
            yq = value['ret']
            data.append((uid, xd, md, yq))
            value.pop('ret')
            # 计算用户下注
            choses = []
            for chose, amount in value.items():
                choses.append({'chose': chose, 'amount': amount})
            bet(uid=uid, period=period, chose=choses, coin_type='free_bean')
            # self.assertEqual(Common.get_xd(uid), xd - amount, '仙豆未扣除')
            bet(uid=uid, period=period, chose=choses, coin_type='cat_bean')
            # self.assertEqual(Common.get_money(uid)['bean'], md - amount, '猫豆未扣除')
        # 结算
        if 'A' in name:
            option = '1'
        elif 'B' in name:
            option = '2'
        elif 'L' in name:
            option = 'loss'
        else:
            option = 'dogfall'
        # 结算
        # settlement(period=period, win_option=option)
        # 验证结果
        for uid, xd, md, exp in data:
            self.assertEqual(Common.get_xd(uid), xd + exp, '仙豆结算错误')
            self.assertEqual(Common.get_money(uid)['bean'], md + exp, '猫豆结算错误')
        logging.info('用例:' + name + '结束')


# 赛事竞猜,坐庄竞猜
class TestGuessBanker(unittest.TestCase):
    @parameterized.expand(banker_case_lists, name_func=new_name_func)
    def test(self, name, kw):
        logging.info('用例:' + name + '开始')
        # 开盘
        period = create(guess_type='match', play_type='banker')
        # 用户先循环坐庄再下注
        punters = ['banker', 'buyer']
        data = {}
        for punter in punters:
            for key, value in kw.items():
                if value is not None and key in ['option_A', 'option_B']:
                    for punter_type, users in value.items():
                        if punter_type == punter:
                            for user in users:
                                for uid, amounts in user.items():
                                    xd = Common.get_xd(uid)  # 获取仙豆
                                    md = Common.get_money(uid)['bean']  # 获取猫豆
                                    # 获取首次用户的货币信息,预期货币信息,第二次读取不更新
                                    if not data.get(uid):
                                        data[uid] = (xd, md, amounts[1])
                                    if punter == 'banker':
                                        bet(uid=uid, period=period, chose=key, coin_type='free_bean', amount=amounts[0], punter=punter,
                                            banker_odds=amounts[2])
                                        self.assertEqual(Common.get_xd(uid), xd - amounts[0], '仙豆未扣除')
                                        bet(uid=uid, period=period, chose=key, coin_type='cat_bean', amount=amounts[0], punter=punter,
                                            banker_odds=amounts[2])
                                        self.assertEqual(Common.get_money(uid)['bean'], md - amounts[0], '猫豆未扣除')
                                    elif punter == 'buyer' and len(amounts) == 3:
                                        bet(uid=uid, period=period, chose=key, coin_type='free_bean', amount=amounts[0], punter=punter)
                                        self.assertEqual(Common.get_xd(uid), xd - amounts[2], '仙豆未扣除')
                                        bet(uid=uid, period=period, chose=key, coin_type='cat_bean', amount=amounts[0], punter=punter)
                                        self.assertEqual(Common.get_money(uid)['bean'], md - amounts[2], '猫豆未扣除')
                                    else:
                                        bet(uid=uid, period=period, chose=key, coin_type='free_bean', amount=amounts[0], punter=punter)
                                        self.assertEqual(Common.get_xd(uid), xd - amounts[0], '仙豆未扣除')
                                        bet(uid=uid, period=period, chose=key, coin_type='cat_bean', amount=amounts[0], punter=punter)
                                        self.assertEqual(Common.get_money(uid)['bean'], md - amounts[0], '猫豆未扣除')

        # 结算
        if 'A' in name:
            option = 'option_A'
        elif 'B' in name:
            option = 'option_B'
        elif 'L' in name:
            option = 'loss'
        else:
            option = 'dogfall'
        settlement(period=period, win_option=option)
        # 验证结果
        for uid, (xd, md, exp) in data.items():
            self.assertEqual(Common.get_xd(uid), xd + exp, '仙豆结算错误{}'.format(uid))
            self.assertEqual(Common.get_money(uid)['bean'], md + exp, '猫豆结算错误{}'.format(uid))
        logging.info('用例:' + name + '结束')


if __name__ == '__main__':
    # 执行文件下所有用例
    # unittest.main()
    # 执行指定类下的所有用例
    # suite = unittest.TestSuite(unittest.makeSuite(TestGuessGamble))
    # 执行单个用例
    suite = unittest.TestSuite()
    suite.addTest(TestGuessGamble('test_A1'))
    runner = unittest.TextTestRunner()
    runner.run(suite)





# test_dir = './'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='guess.py')
# for i in discover:
#     print(i)
