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
from guess_case import gamble_case_lists
from common.common import Common
from urllib import parse
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
    Calculation()
    data = {
        'guess_type': 'match',  # 竞猜类型,anchor:主播,match:赛事
        'match_id_or_room_number': '4685',  # 比赛ID/房间号
        'play_type': 'gamble',  # 竞猜玩法,对赌:gamble,坐庄:banker
        'title': '赛事对赌竞猜测试',  # 竞猜标题
        'opt_type': 'normal',  # 选项类型 normal,normal_3,normal_4,normal_5,money_line,ball
        'opt_items': {
            1: '选项1',
            2: '选项2'
        },
        'expire': str(int(time.time())),  # 竞猜封盘时间
        'note': '',  # ??
    }
    for key, value in kw.items():
        data['key'] = value
    post_data = Common.form_single_dict(data)
    ret = requests.post(ADMIN_URL + '/guessnew/create_save', data=post_data, cookies=ADMIN_COOKIES).text
    try:
        ret = json.loads(ret)
        logging.info('开盘{},{}'.format(ret['period'], ret))
        return ret['period']
    except:
        logging.error(ret)


# 更新状态
def update_status(period, status):
    # res = requests.post(ADMIN_URL + '/guessnew/update_status', data=dict(period=period, status=status), cookies=ADMIN_COOKIES)
    res = requests.post(ADMIN_URL + '/guessnew/update_status/' + str(period) + '/' + str(status), cookies=ADMIN_COOKIES)
    logging.info('{}:{}'.format(status, res.json()))
    # return period


# 对冲下注,坐庄下注
def bet(uid, **kw):
    data = {
        'bet': {
            0: {
                'period': '111111',  # 期号
                'opt_type': 'normal',  # 选项类型 normal,normal_3,normal_4,normal_5,money_line,ball
                'coin_type': 'free_bean',  # 货币类型仙豆free_bean,猫豆cat_bean
                'punter': 'bet',  # bet:普通下注,'banker':坐庄, 'buyer':买庄
                'chose': {  # 下注选项
                    0: {'chose': 1, 'amount': 100},
                    1: {'chose': 1, 'amount': 100},
                },
            },
        }
    }

    for key, value in kw.items():
        data['bet'][0][key] = value
    post_data = Common.form_single_dict(data)
    res = requests.post(URL + '/guessnew/betMore', data=post_data, cookies=Common.generate_cookies(uid))
    ret = requests.get(URL + '/crontab/doBetTask').text
    logging.info('下注队列执行结果：{}'.format(ret))
    try:
        res = res.json()
        res_info = '用户{}下注：数据{}返回{}'.format(uid, data, res)
        logging.info(res_info)
    except ValueError:
        logging.info(res.text)


# 坐庄
def banker(uid, **kw):
    data = {
        'period': '111111',  # 期号
        'opt_type': 'normal',  # 选项类型 normal,normal_3,normal_4,normal_5,money_line,ball
        'coin_type': 'free_bean',  # 货币类型仙豆free_bean,猫豆cat_bean
        'punter': 'banker',  # bet:普通下注,'banker':坐庄, 'buyer':买庄
        'banker_odds': '',  # 赔率
        'chose': {  # 下注选项
            0: {'chose': 1, 'amount': 100},
            1: {'chose': 1, 'amount': 100},
        },
    }
    post_data = Common.form_single_dict(data)
    res = requests.post(URL + '/guessnew/banker', data=post_data, cookies=Common.generate_cookies(uid))
    try:
        res = res.json()
        res_info = '用户{}数据{}返回{}'.format(uid, data, res)
        logging.info(res_info)
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
    logging.info('结算选项:{}结果:{}'.format(data['win_option'], res.json()))
    Calculation()


# 计算
def Calculation():
    try:
        res1 = requests.get(URL + '/crontab/guessNewCalculation')
        # logging.info('结算 - 计算' + res1.text)
        res2 = requests.get(URL + '/crontab/guessNewSettlement')
        # logging.info('结算 - 结算' + res2.text)
    except:
        logging.info('结算超时')


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
        for res in [1, 2, -1, -2]:
            logging.info('用例:{}结算选项{}开始'.format(name, res) + '*' * 80)
            # 开盘
            period = create(guess_type='match', play_type='gamble')
            # 下注
            data = []
            for uid, value in kw.items():
                # 获取用户的货币信息,预期货币信息
                xd = Common.get_xd(uid)  # 获取仙豆
                md = Common.get_money(uid)['bean']  # 获取猫豆
                if res == 1:
                    exp = value['ret'][0]
                elif res == 2:
                    exp = value['ret'][1]
                else:
                    exp = value['ret'][2]
                data.append((uid, xd, md, exp))
                # 计算用户下注
                choses = {}
                for chose, amount in value.items():
                    if chose != 'ret':
                        i = 0
                        choses[i] = {'chose': chose, 'amount': amount}
                        i = i + 1
                        bet(uid, period=period, coin_type='free_bean', chose=choses)
                        # self.assertEqual(Common.get_xd(uid), xd - amount, '仙豆未扣除')
                        bet(uid, period=period, coin_type='cat_bean', chose=choses)
                        # self.assertEqual(Common.get_money(uid)['bean'], md - amount, '猫豆未扣除')
            # 结算
            settlement(period=period, win_option=res)
            # 验证结果
            for uid, xd, md, exp in data:
                self.assertEqual(Common.get_xd(uid), xd + exp, uid + '仙豆结算错误')
                self.assertEqual(Common.get_money(uid)['bean'], md + exp, uid + '猫豆结算错误')
        logging.info('用例:' + name + '结束')


banker_case_lists = []


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
    suite.addTest(TestGuessGamble('test_13'))
    runner = unittest.TextTestRunner()
    runner.run(suite)





# test_dir = './'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='guess.py')
# for i in discover:
#     print(i)
