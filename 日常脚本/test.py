#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/13 19:59
# Author : lixingyun
import sys
import json
from  urllib import parse


# from common.common import Common

def form_single_dict(data, key='', ret={}):
    if isinstance(data, dict):
        for key1, value1 in data.items():
            key1s = str(key) + '[' + str(key1) + ']' if key else str(key1)
            if isinstance(value1, dict):
                form_single_dict(value1, key1s)
            else:
                ret[key1s] = value1
        return ret
    else:
        return False


data2 = {
    'guess_type': 'match',  # 竞猜类型,anchor:主播,match:赛事
    'match_id_or_room_number': '4685',  # 比赛ID/房间号
    'play_type': 'gamble',  # 竞猜玩法,对赌:gamble,坐庄:banker
    'title': '赛事对赌竞猜测试',  # 竞猜标题
    'opt_type': 'normal',  # 选项类型 normal,normal_3,normal_4,normal_5,money_line,ball
    'opt_items': {
        1: '选项1',
        2: '选项2'
    }}

data = {
    'bet': {0: {
        'period': '111111',
        'opt_type': 'normal',
        'coin_type': 'free_bean',
        'punter': 'bet',
        'banker_odds': '',
        'chose': {
            0: {'chose': 1, 'amount': 100},
            1: {'chose': 1, 'amount': 100}, },
    }
    },
}

r = form_single_dict(data)
print(r)
