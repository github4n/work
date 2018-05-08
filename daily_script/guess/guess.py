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
import sys
from guess_case import gamble_case_lists, banker_case_lists
from huomao.common import Common
from huomao.money import MoneyClass
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


# 后台创建盘口
def create(**kw):
    Calculation()
    data = {
        'guess_type': 'match',  # 竞猜类型,anchor:主播,match:赛事
        'match_id_or_room_number': '3',  # 比赛ID/房间号
        'play_type': 'gamble',  # 竞猜玩法,对赌:gamble,坐庄:banker
        'title': '赛事竞猜测试',  # 竞猜标题
        'opt_type': '200001',  # 选项类型
        'opt_items': {
            1: '选项1',
            2: '选项2'
        },
        'expire': str(int(time.time())),  # 竞猜封盘时间
        'note': 'test' + str(int(time.time())),  # ??
    }
    for key, value in kw.items():
        data[key] = value
    post_data = Common.form_single_dict(data)
    ret = requests.post(ADMIN_URL + '/guessnew/create_save', data=post_data, cookies=ADMIN_COOKIES).text
    try:
        ret = json.loads(ret)
        logging.info('开盘{},{}'.format(ret['period'], ret))
        return ret['period']
    except:
        logging.error(ret)


# 后台锁定盘口
def lock(period):
    ret = requests.post(ADMIN_URL + '/guessnew/update_status/{}/locking'.format(period), cookies=ADMIN_COOKIES).json()
    logging.info('锁定结果：{}'.format(ret))
    return ret


# 后台封盘blockade
def blockade(period):
    ret = requests.post(ADMIN_URL + '/guessnew/update_status/{}/blockade'.format(period), cookies=ADMIN_COOKIES).json()
    logging.info('封盘结果：{}'.format(ret))
    return ret


# 后台结算
def settlement(**kw):
    data = {
        'cid': 2,  # 房间号
        'period': '',  # 期号
        'win_option': 1  # 开奖结果option_A,option_B,loss流局,dogfall平局
    }
    for key in kw:
        if key in data:
            data[key] = kw.get(key)
    res = requests.post(ADMIN_URL + '/guessnew/settlement', data=data, cookies=ADMIN_COOKIES)
    logging.info('结算选项:{}结果:{}'.format(data['win_option'], res.json()))
    Calculation()


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
                'opt_type': 200001,  # 选项类型
                'coin_type': 'free_bean',  # 货币类型仙豆free_bean,猫豆cat_bean
                'punter': 'bet',  # bet:普通下注,'banker':坐庄, 'buyer':买庄
                'chose': {  # 下注选项
                    0: {'chose': 1, 'amount': 100, 'now_odds': 0},
                    1: {'chose': 1, 'amount': 100, 'now_odds': 0},
                },
            },
        }
    }
    for key, value in kw.items():
        data['bet'][0][key] = value
    post_data = Common.form_single_dict(data)
    requests.post(URL + '/guessnew/betMore', data=post_data, cookies=Common.generate_cookies(uid))
    # 轮询
    for i in range(30):
        ret = requests.get(URL + '/guessnew/bettingRes', cookies=Common.generate_cookies(uid)).text
        if Common.is_json(ret):
            ret = json.loads(ret)
            if ret['code'] == 0:
                res_info = '用户{}下注成功：数据{}返回{}'.format(uid, data, ret)
                logging.info(res_info)
                return ret
            else:
                res_info = '用户{}下注失败：数据{}返回{}'.format(uid, data, ret)
                logging.info(res_info)
        else:
            logging.error(ret)
            return False
        time.sleep(1)
    return False
    # ret = requests.get(URL + '/crontab/doBetTask').text
    # logging.info('下注队列执行结果：{}'.format(ret))
    # time.sleep(2)


# 坐庄
def banker(uid, **kw):
    data = {
        'period': '111111',  # 期号
        'opt_type': 200001,  # 选项类型 normal,normal_3,normal_4,normal_5,money_line,ball
        'coin_type': 'free_bean',  # 货币类型仙豆free_bean,猫豆cat_bean
        'punter': 'banker',  # bet:普通下注,'banker':坐庄, 'buyer':买庄
        'banker_odds': 2,  # 赔率
        'chose': 1,  # 坐庄选项
        'amount': 1000,
        'third_id': 0,
    }
    for key, value in kw.items():
        data[key] = value
    post_data = Common.form_single_dict(data)
    res = requests.post(URL + '/guessnew/banker', data=post_data, cookies=Common.generate_cookies(uid))
    try:
        res = res.json()
        res_info = '用户{}坐庄数据\n{}返回{}\n'.format(uid, data, res)
        logging.info(res_info)
        if res['status'] == 'success':
            return res['data']['banker']['order_id']
    except ValueError:
        logging.error(res.text)
        return False


# 修改庄
def change_banker(uid, period, id, banker_odds='', type_='revoke'):
    data = {
        'period': period,  # 期号
        'id': id,
        'banker_odds': banker_odds,
    }
    res = requests.post(URL + '/guessnew/changeBanker/' + type_, data=data, cookies=Common.generate_cookies(uid))
    if type_ == 'revoke':
        logging.info('撤庄{}'.format(res.json()))
    else:
        logging.info('修改庄{}'.format(res.json()))
    return res.json()


# 计算
def Calculation():
    try:
        res1 = requests.get(URL + '/crontab/guessNewCalculation')
        logging.info('结算 - 计算' + res1.text)
        res2 = requests.get(URL + '/crontab/guessNewSettlement')
        logging.info('结算 - 结算' + res2.text)
    except:
        logging.info('结算超时')


def new_name_func(func, num, p):
    # base_name = func.__name__
    # name_suffix = "_%s" % (num, )
    # if len(p.args) > 0 and isinstance(p.args[0], str):
    #     name_suffix += "_" + parameterized.to_safe_name(p.args[0])
    # return base_name + name_suffix
    return func.__name__ + '_' + str(num + 1)


# 赛事竞猜,对冲竞猜
class TestGuessGamble(unittest.TestCase):
    @parameterized.expand(gamble_case_lists, name_func=new_name_func)
    def test(self, *args):
        name = self._testMethodName
        for res in [1, 2, -1, -2]:
            logging.info('用例:{}结算选项{}开始'.format(name, res) + '*' * 80)
            # 开盘
            period = create(guess_type='match', play_type='gamble')
            # 下注
            money_data = []
            for data in args:
                # 获取用户的货币信息,预期货币信息
                uid = data['uid']
                xd = MoneyClass.get_xd(uid)  # 获取仙豆
                md = MoneyClass.get_money(uid)['bean']  # 获取猫豆
                if res == 1:
                    exp = data['ret'][0]
                elif res == 2:
                    exp = data['ret'][1]
                else:
                    exp = data['ret'][2]
                money_data.append((uid, xd, md, exp))
                # 计算用户下注
                choses = {}
                for chose, amount in data.items():
                    if chose != 'ret' and chose != 'uid':
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
            for uid, xd, md, exp in money_data:
                self.assertEqual(MoneyClass.get_xd(uid), xd + exp, uid + '仙豆结算错误')
                self.assertEqual(MoneyClass.get_money(uid)['bean'], md + exp, uid + '猫豆结算错误')
        logging.info('用例:' + name + '结束')


# 赛事竞猜,坐庄竞猜
class TestGuessBanker(unittest.TestCase):
    @parameterized.expand(banker_case_lists, name_func=new_name_func)
    def test(self, *args):
        name = self._testMethodName
        for res in [1, 2, -1, -2]:
            logging.info('用例:{}结算选项{}开始'.format(name, res) + '*' * 80)
            # 开盘
            period = create(guess_type='match', play_type='banker')
            # 下注
            money_data = []
            for data in args:
                # 获取用户的货币信息,预期货币信息
                uid = data['uid']
                xd = MoneyClass.get_xd(uid)  # 获取仙豆
                md = MoneyClass.get_money(uid)['bean']  # 获取猫豆
                if res == 1:
                    exp = data['ret'][0]
                elif res == 2:
                    exp = data['ret'][1]
                else:
                    exp = data['ret'][2]
                money_data.append((uid, xd, md, exp))
                # 首先坐庄
                banker_data_list = data.get('banker')
                if banker_data_list and isinstance(banker_data_list, list):
                    for banker_data in banker_data_list:
                        for chose, amount in banker_data.items():
                            banker(data['uid'], period=period, coin_type='free_bean', chose=chose, amount=amount[0], banker_odds=amount[1])
                            banker(data['uid'], period=period, coin_type='cat_bean', chose=chose, amount=amount[0], banker_odds=amount[1])
                elif banker_data_list:
                    for chose, amount in banker_data_list.items():
                        banker(data['uid'], period=period, coin_type='free_bean', chose=chose, amount=amount[0], banker_odds=amount[1])
                        banker(data['uid'], period=period, coin_type='cat_bean', chose=chose, amount=amount[0], banker_odds=amount[1])
                # 下注
                buyer_data = data.get('buyer')
                if buyer_data:
                    choses = {}
                    for chose, amounts in buyer_data.items():
                        amount = amounts[0]
                        now_odds = amounts[1]
                        r_amount = amounts[2] if len(amounts) == 3 else amount
                        i = 0
                        choses[i] = {'chose': chose, 'amount': amount, 'now_odds': now_odds}
                        i = i + 1
                        bet(data['uid'], period=period, coin_type='free_bean', punter='buyer', chose=choses)
                        self.assertEqual(MoneyClass.get_xd(uid), xd - r_amount, uid + '仙豆未扣除')
                        bet(data['uid'], period=period, coin_type='cat_bean', punter='buyer', chose=choses)
                        self.assertEqual(MoneyClass.get_money(uid)['bean'], md - r_amount, uid + '猫豆未扣除')
            # 结算
            settlement(period=period, win_option=res)
            # 验证结果
            for uid, xd, md, exp in money_data:
                self.assertEqual(MoneyClass.get_xd(uid), xd + exp, uid + '仙豆结算错误')
                self.assertEqual(MoneyClass.get_money(uid)['bean'], md + exp, uid + '猫豆结算错误')
            logging.info('用例:{}结算选项{}结束'.format(name, res) + '*' * 80)


# 竞猜状态测试
class TestGuessStatus(unittest.TestCase):
    # 竞猜中:状态下的用户操作 坐庄,下注,撤庄,撤庄
    def test_1(self):
        # 开盘
        period = create(guess_type='match', play_type='banker')
        # 坐庄
        order_id = banker(uid=5524, coin_type='free_bean', period=period)
        # 下注
        bet(uid=5525, period=period, coin_type='free_bean', punter='buyer', chose={0: {'chose': 1, 'amount': 100, 'now_odds': 2}})
        # 撤庄
        ret = change_banker(5524, period, order_id)
        self.assertEqual(ret['data']['refund'], 900)

    # 锁定中:状态下的用户操作 坐庄,下注,撤庄,撤庄
    def test_2(self):
        # 开盘
        period = create(guess_type='match', play_type='banker')
        # 坐庄
        order_id = banker(uid=5524, coin_type='free_bean', period=period)
        lock(period)
        # 下注
        bet(uid=5525, period=period, coin_type='free_bean', punter='buyer', chose={0: {'chose': 1, 'amount': 100, 'now_odds': 2}, })
        # 坐庄
        banker(uid=5526, coin_type='free_bean', period=period)
        # 撤庄
        ret = change_banker(5524, period, order_id)

    # 封盘中:状态下的用户操作 坐庄,下注,撤庄,撤庄
    def test_3(self):
        # 开盘
        period = create(guess_type='match', play_type='banker')
        # 坐庄
        order_id = banker(uid=5524, coin_type='free_bean', period=period)
        blockade(period)
        # 下注
        bet(uid=5525, period=period, coin_type='free_bean', punter='buyer', chose={0: {'chose': 1, 'amount': 100, 'now_odds': 2}, })
        # 坐庄
        banker(uid=5526, coin_type='free_bean', period=period)
        # 撤庄
        ret = change_banker(5524, period, order_id)

    # 结算中:状态下的用户操作 坐庄,下注,撤庄,撤庄
    def test_4(self):
        # 开盘
        period = create(guess_type='match', play_type='banker')
        # 坐庄
        order_id = banker(uid=5524, coin_type='free_bean', period=period)
        settlement(period=period)
        # 下注
        bet(uid=5525, period=period, coin_type='free_bean', punter='buyer', chose={0: {'chose': 1, 'amount': 100, 'now_odds': 2}, })
        # 坐庄
        banker(uid=5526, coin_type='free_bean', period=period)
        # 撤庄
        ret = change_banker(5524, period, order_id)

    # 已结算:状态下的用户操作 坐庄,下注,撤庄,撤庄
    def test_5(self):
        # 开盘
        period = create(guess_type='match', play_type='banker')
        # 坐庄
        order_id = banker(uid=5524, coin_type='free_bean', period=period)
        settlement(period=period)
        Calculation()
        # 下注
        bet(uid=5525, period=period, coin_type='free_bean', punter='buyer', chose={0: {'chose': 1, 'amount': 100, 'now_odds': 2}, })
        # 坐庄
        banker(uid=5526, coin_type='free_bean', period=period)
        # 撤庄
        ret = change_banker(5524, period, order_id)


if __name__ == '__main__':
    # 执行文件下所有用例
    # unittest.main()
    # 执行指定类下的所有用例
    # suite = unittest.TestSuite(unittest.makeSuite(TestGuessBanker))
    # 执行单个用例
    suite = unittest.TestSuite()
    suite.addTest(TestGuessStatus('test_5'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # test_dir = './'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='guess.py')
    # for i in discover:
    #     print(i)
