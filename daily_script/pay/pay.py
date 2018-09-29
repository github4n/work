#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/1/25 11:48
# Author : lixingyun
# 回调接口测试
# 已支持：支付宝  待支持：微信 苹果 京东 快钱
import requests
import hashlib
import base64
from  urllib import parse


def data_filter(data):
    if isinstance(data, dict):
        if data.get('sign'):
            data.pop('sign')
    return data


# WEB支付宝回调pay_mode=1， money 单位元，float
def alipay(trade_id, money):
    url = 'http://lxy.new.huomaotv.com.cn/test/testpay'
    data = {
        'type': 'alipay',
        'out_trade_no': trade_id,  # 商户订单号
        'trade_no': '27394723947293749',  # 支付宝交易号
        'trade_status': 'TRADE_FINISHED',  # 交易状态
        'total_amount': money,  # 交易金额 int float str
        'notify_id': '9ESDJFJS23749ASDFJAS12341',  # 通知校验ID
        'notify_time': '201606121539',  # 通知的发送时间
        'buyer_logon_id': 'AJSDJF238492839',  # 买家支付宝帐号
    }
    res = requests.post(url, data=data)
    print(res.text)


# WEB微信回调pay_mode=2， money 单位分，int
def wxpay(trade_id, money):
    url = 'http://lxy.new.huomaotv.com.cn/test/testpay'
    data = {
        'type': 'weixin',
        'out_trade_no': trade_id,  # 商户订单号
        'transaction_id': '2',  # 微信交易号
        'total_fee': money*100,  # 交易金额  注意类型
        'sign': '',  # 通知校验ID
        'time_end': '',  # 通知的发送时间
        'openid': '',  # 买家支付宝帐号
    }
    res = requests.post(url, data=data)
    print(res.text)


# WEB微信公众号回调pay_mode=2， money 单位分，int
def wxgzhpay(trade_id, money):
    url = 'http://lxy.new.huomaotv.com.cn/test/testpay'
    data = {
        'type': 'wxgzh',
        'out_trade_no': trade_id,  # 商户订单号
        'total_fee': money,  # 交易金额  注意类型
        'transaction_id': '',
        'sign': '',
        'time_end': '',
        'openid': '',
    }
    res = requests.post(url, data=data)
    print(res.text)


# WEBqqgame回调pay_mode=2， money 单位元，int
def qqgamepay(trade_id, money):
    url = 'http://lxy.new.huomaotv.com.cn/test/testpay'
    data = {
        'type': 'qqgame',
        'out_trade_no': trade_id,  # 商户订单号
        'trade_no': '',
        'total_fee': money,
        'notify_id': '',
        'notify_time': '',
        'buyer_email': '',
        'trade_status': 'TRADE_FINISHED',

    }
    res = requests.post(url, data=data)
    print(res.text)


# WEB 快钱回调，money 单位分，int
def kqpay(trade_id, money):
    url = 'http://lxy.new.huomaotv.com.cn/test/testpay'
    data = {
        'type': 'kuaiqian',
        'orderId': trade_id,  # 商户订单号
        'dealId': '',
        'orderAmount': money,
        'payAmount': money,
        'payResult': '10',

    }
    res = requests.post(url, data=data)
    print(res.text)


# WEB 京东回调，money 单位分，int
def jdpay(trade_id, money):
    url = 'http://lxy.new.huomaotv.com.cn/test/testpay'
    data = {
        'type': 'jd',
        'out_trade_no': trade_id,  # 商户订单号
        'transaction_id': '',
        'total_fee': money,
        'sign': '',
        'tranTime': '',
        'openid': '',
        'note': '',
    }
    res = requests.post(url, data=data)
    print(res.text)


# 苹果回掉pay_mode=2， money 单位元，int,固定金额 6：4，18：13，50：35，98：68，328：225，518：362，30：20，298：205，798：548，1598：1097
def applepay(trade_id, money):
    url = 'http://lxy.new.huomaotv.com.cn/test/testpay'
    data = {
        'type': 'apple',
        'out_trade_no': trade_id,  # 商户订单号
        'trade_no': '',  # 交易号
        'time_end': '',  # 通知的发送时间
    }
    res = requests.post(url, data=data)
    print(res.text)


# WEB 天猫回调，money 单位分，int
def tmallpay(trade_id, money):
    url = 'http://lxy.new.huomaotv.com.cn/NotifyPayment/callbackNotify/tmall'
    data = {
        'Shop': '10001',
        'PorductId': 'catCoin',
        'Account': '15800022799',
        'OrderNo': trade_id,
        'Amount': money,  # 注意浮点型
    }
    salt = '^&*%(*GIUGJ'
    sgin = data['Account'] + str(data['Amount']) + data['PorductId'] + data['Shop'] + str(data['OrderNo']) + salt
    m = hashlib.md5()
    m.update(sgin.encode('utf-8'))
    sgin = m.hexdigest()
    data['Signature'] = sgin
    print(data)
    res = requests.post(url, data=data)
    print(res.json())


# wxpay(2018050209463215229773399, 2800)
wxpay(20180928192623354996498011, 100)