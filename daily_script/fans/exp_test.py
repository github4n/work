#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/9/5 14:39
# Author : lixingyun
# Description :
from huomao.user import User
from huomao.common import Common
from huomao.bag import Bag
import requests

fans_config = {
    1: [6000, 10, 1000],
    2: [7000, 10, 2500],
    3: [10000, 10, 2500],
    4: [16000, 10, 2500],
    5: [28000, 10, 2500],
    6: [48000, 15, 3000],
    7: [70000, 15, 3000],
    8: [94000, 15, 3000],
    9: [120000, 15, 3000],
    10: [150000, 15, 3000],
    11: [200000, 30, 4000],
    12: [300000, 30, 4000],
    13: [450000, 30, 4000],
    14: [650000, 30, 4000],
    15: [900000, 30, 4000],
    16: [1200000, 50, 5000],
    17: [1800000, 50, 5000],
    18: [3000000, 50, 5000],
    19: [4800000, 50, 7200],
    20: [7200000, 50, 9600],
    21: [10200000, 100, 12000],
    22: [30000000, 100, 79200],
    23: [60000000, 100, 120000],
    24: [100000000, 100, 160000],
    25: [150000000, 100, 200000],
    26: [220000000, 100, 280000],
    27: [310000000, 100, 360000],
    28: [420000000, 100, 440000],
    29: [550000000, 100, 520000],
    30: [700000000, 100, 600000],
}

uids = list(range(5524,5554))

# 测试各等级每日礼包
for i in fans_config.keys():
    # 创建用户
    uid = User.reg('fans')
    # uid = uids[i-1]
    # 设置粉丝值
    User.loveliness('set', uid, 2, fans_config[i][0])
    # 判断等级,每日礼包数量
    ret = requests.post('http://lxy.new.huomaotv.com.cn/chatnew/joinMsg',
                        data=dict(cid=2, anchor_id=1522, is_yule=0),
                        cookies=Common.generate_cookies(uid)).json()
    if int(ret['data']['fans']['level']) == i and Bag.get_bag(uid,20) == fans_config[i][1]:
        print(uid,int(ret['data']['fans']['level']), i, Bag.get_bag(uid, 20), fans_config[i][1], '测试ok')
    else:
        print(uid,int(ret['data']['fans']['level']), i, Bag.get_bag(uid, 20), fans_config[i][1], '测试fail')
    # 测试衰减脚本
    requests.get('http://lxy.new.huomaotv.com.cn/crontab/fansAttenuation')
    scores = User.loveliness('get',uid,2)
    if scores == fans_config[i][0] - fans_config[i][2]:
        print(scores,fans_config[i][0],fans_config[i][2],'测试OK')
    else:
        print(scores, fans_config[i][0], fans_config[i][2], '测试F')