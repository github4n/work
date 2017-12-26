#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/12/26 10:27
# Author : lixingyun

uids = [str(i) for i in range(5524, 5624)]

# for uid in uids:
#     Common.set_money(uid,999999,999999)
#     Common.set_xd(uid, 999999)
# exit()
# 这边的金额表示猫豆和仙豆同时下的金额,预期收益,option_AB表示两个选项的下注,
period_lists = [
    # 结算A
    # 结算A,当选项A有下注,B无下注,单
    {'option_A': {uids[0]: (100, 0)}, 'option_B': None, 'res': 'option_A'},
    # 结算A,当选项A有下注,B无下注,多
    {'option_A': {uids[0]: (100, 0), uids[1]: (100, 0)}, 'option_B': None, 'res': 'option_A'},
    # 结算A,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {uids[0]: (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {uids[0]: (100, -100), uids[1]: (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {uids[0]: (1, 0)}, 'option_B': {uids[1]: (1, -1)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {uids[0]: (1, 9)}, 'option_B': {uids[1]: (10, -10)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {uids[0]: (1, 95)}, 'option_B': {uids[1]: (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {uids[0]: (10, 95)}, 'option_B': {uids[1]: (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {uids[0]: (1000, 950)}, 'option_B': {uids[1]: (1000, -1000)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {uids[0]: (1, 0), uids[1]: (1, 0)}, 'option_B': {'5526': (1, -1), '5527': (1, -1)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {uids[0]: (1, 9), uids[1]: (1, 9)}, 'option_B': {'5526': (10, -10), '5527': (10, -10)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {uids[0]: (1, 95), uids[1]: (1, 95)}, 'option_B': {'5526': (100, -100), '5527': (100, -100)}, 'res': 'option_A'},
    # 结算A,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {uids[0]: (10, 126), uids[1]: (20, 253)}, 'option_B': {'5526': (100, -100), '5527': (300, -300)}, 'res': 'option_A'},
    # 结算B
    # 结算B,当选项A有下注,B无下注,单
    {'option_A': {uids[0]: (100, -100)}, 'option_B': None, 'res': 'option_B'},
    # 结算B,当选项A有下注,B无下注,多
    {'option_A': {uids[0]: (100, -100), uids[1]: (100, -100)}, 'option_B': None, 'res': 'option_B'},
    # 结算B,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {uids[0]: (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {uids[0]: (100, 0), uids[1]: (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {uids[0]: (1, -1)}, 'option_B': {uids[1]: (1, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {uids[0]: (1, -1)}, 'option_B': {uids[1]: (10, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {uids[0]: (1, -1)}, 'option_B': {uids[1]: (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {uids[0]: (10, -10)}, 'option_B': {uids[1]: (100, 9)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {uids[0]: (1000, -1000)}, 'option_B': {uids[1]: (1000, 950)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {uids[0]: (1, -1), uids[1]: (1, -1)}, 'option_B': {'5526': (1, 0), '5527': (1, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {uids[0]: (1, -1), uids[1]: (1, -1)}, 'option_B': {'5526': (10, 0), '5527': (10, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {uids[0]: (1, -1), uids[1]: (1, -1)}, 'option_B': {'5526': (100, 0), '5527': (100, 0)}, 'res': 'option_B'},
    # 结算B,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {uids[0]: (10, -10), uids[1]: (20, -20)}, 'option_B': {'5526': (100, 7), '5527': (300, 21)}, 'res': 'option_B'},
    # 结算:流局
    # 流局,当选项A有下注,B无下注,单
    {'option_A': {uids[0]: (100, 0)}, 'option_B': None, 'res': 'loss'},
    # 流局,当选项A有下注,B无下注,多
    {'option_A': {uids[0]: (100, 0), uids[1]: (100, 0)}, 'option_B': None, 'res': 'loss'},
    # 流局,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {uids[0]: (100, 0)}, 'res': 'loss'},
    # 流局,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {uids[0]: (100, 0), uids[1]: (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {uids[0]: (1, 0)}, 'option_B': {uids[1]: (1, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {uids[0]: (1, 0)}, 'option_B': {uids[1]: (10, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {uids[0]: (1, 0)}, 'option_B': {uids[1]: (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {uids[0]: (10, 0)}, 'option_B': {uids[1]: (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {uids[0]: (1000, 0)}, 'option_B': {uids[1]: (1000, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {uids[0]: (1, 0), uids[1]: (1, 0)}, 'option_B': {'5526': (1, 0), '5527': (1, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {uids[0]: (1, 0), uids[1]: (1, 0)}, 'option_B': {'5526': (10, 0), '5527': (10, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {uids[0]: (1, 0), uids[1]: (1, 0)}, 'option_B': {'5526': (100, 0), '5527': (100, 0)}, 'res': 'loss'},
    # 流局,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {uids[0]: (10, 0), uids[1]: (20, 0)}, 'option_B': {'5526': (100, 0), '5527': (300, 0)}, 'res': 'loss'},
    # 结算:平局
    # 平局,当选项A有下注,B无下注,单
    {'option_A': {uids[0]: (100, 0)}, 'option_B': None, 'res': 'dogfall'},
    # 平局,当选项A有下注,B无下注,多
    {'option_A': {uids[0]: (100, 0), uids[1]: (100, 0)}, 'option_B': None, 'res': 'dogfall'},
    # 平局,当选项B有下注,A无下注,单
    {'option_A': None, 'option_B': {uids[0]: (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项B有下注,A无下注,多
    {'option_A': None, 'option_B': {uids[0]: (100, 0), uids[1]: (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1,B:1
    {'option_A': {uids[0]: (1, 0)}, 'option_B': {uids[1]: (1, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1,B:10
    {'option_A': {uids[0]: (1, 0)}, 'option_B': {uids[1]: (10, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1,B:100
    {'option_A': {uids[0]: (1, 0)}, 'option_B': {uids[1]: (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:10,B:100
    {'option_A': {uids[0]: (10, 0)}, 'option_B': {uids[1]: (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,两个用户,A:1000,B:1000
    {'option_A': {uids[0]: (1000, 0)}, 'option_B': {uids[1]: (1000, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    {'option_A': {uids[0]: (1, 0), uids[1]: (1, 0)}, 'option_B': {'5526': (1, 0), '5527': (1, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    {'option_A': {uids[0]: (1, 0), uids[1]: (1, 0)}, 'option_B': {'5526': (10, 0), '5527': (10, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    {'option_A': {uids[0]: (1, 0), uids[1]: (1, 0)}, 'option_B': {'5526': (100, 0), '5527': (100, 0)}, 'res': 'dogfall'},
    # 平局,当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    {'option_A': {uids[0]: (10, 0), uids[1]: (20, 0)}, 'option_B': {'5526': (100, 0), '5527': (300, 0)}, 'res': 'dogfall'},
]
# 这边的金额表示猫豆和仙豆同时(下注金额,预期收益,赔率),(下注金额,预期收益,实际下注金额)option_AB表示两个选项的下注buyer坐庄banker,
case_lists = [
    # 结算A
    ## 有坐庄无下注时
    # 结算A,当选项A有坐庄,无下注,选项B无坐庄,无下注
    ('1', {'option_A': None, 'option_B': {'banker': [{uids[0]: (100, 0, 1)}]}, 'res': 'option_A'}),
    # 结算A,当选项A有多个坐庄,无下注,选项B无坐庄,无下注
    ('2', {'option_A': None, 'option_B': {'banker': [{uids[0]: (100, 0, 1)}, {uids[1]: (100, 0, 1)}]}, 'res': 'option_A'}),
    # 结算A,当选项A无坐庄,无下注,选项B有坐庄,无下注
    ('3', {'option_A': {'banker': [{uids[0]: (100, 0, 1)}]}, 'option_B': None, 'res': 'option_A'}),
    # 结算A,当选项A无坐庄,无下注,选项B有多个坐庄,无下注
    ('4', {'option_A': {'banker': [{uids[0]: (100, 0, 1)}, {uids[1]: (100, 0, 1)}]}, 'option_B': None, 'res': 'option_A'}),
    # 结算A,当选项A,B都有庄,无下注
    ('5', {'option_A': {'banker': [{uids[0]: (100, 0, 1)}, {uids[1]: (100, 0, 1)}]},
           'option_B': {'banker': [{uids[0]: (100, 0, 1)}, {uids[1]: (100, 0, 1)}]}, 'res': 'option_A'}),
    ## 有坐庄有下注 - 单边有坐庄下注
    # 结算A,当选项A有一个坐庄,有一个下注,选项B无坐庄,无下注
    ('6', {'option_A': {'buyer': [{uids[1]: (10, 94)}]},
           'option_B': {'banker': [{uids[0]: (100, -99, 9.9)}]}, 'res': 'option_A'}),
    # 结算A,当选项A有一个坐庄,有多个下注(未买完),选项B无坐庄,无下注
    ('7', {'option_A': {'buyer': [{uids[1]: (100, 47)}, {uids[2]: (50, 23)}]},
           'option_B': {'banker': [{uids[0]: (100, -75, 0.5)}]}, 'res': 'option_A'}),
    # 结算A,当选项A有一个坐庄,有多个下注(超庄),选项B无坐庄,无下注
    ('8', {'option_A': {'buyer': [{uids[1]: (100, 47)}, {uids[2]: (200, 47, 100)}]},
           'option_B': {'banker': [{uids[0]: (100, -100, 0.5)}]}, 'res': 'option_A'}),
    # 结算A,当选项A有多个坐庄(同用户,同赔率),有一个下注(跨庄),选项B无坐庄,无下注
    ('9', {'option_A': {'buyer': [{uids[1]: (400, 190)}]},
           'option_B': {'banker': [{uids[0]: (100, -200, 0.5)}, {uids[0]: (100, -200, 0.5)}]}, 'res': 'option_A'}),
    # 结算A,当选项A有多个坐庄(不同用户,同赔率),有一个下注(跨庄),选项B无坐庄,无下注
    ('10', {'option_A': {'buyer': [{uids[1]: (400, 90)}]},
            'option_B': {'banker': [{uids[0]: (100, -100, 0.5)}, {uids[1]: (100, 90, 0.5)}]}, 'res': 'option_A'}),
    # 结算A,当选项A有多个坐庄(不同用户,不同赔率),有一个下注(超庄),选项B无坐庄,无下注
    ('11', {'option_A': {'buyer': [{uids[1]: (170, 94, 166)}]},
            'option_B': {'banker': [{uids[0]: (100, 0, 0.5)}, {uids[2]: (100, -100, 0.6)}]}, 'res': 'option_A'}),
    # 结算A,当选项A有多个坐庄,多个下注,选项B无坐庄,无下注
    ('12', {'option_A': {'buyer': [{uids[0]: (100, 57)}, {uids[1]: (100, 37, 66)}, {uids[2]: (100, 47)}]},
            'option_B': {'banker': [{uids[3]: (100, -50, 0.5)}, {uids[4]: (100, -100, 0.6)}]}, 'res': 'option_A'}),
    # 结算A,当选项A无坐庄,无下注,选项B有一个坐庄,有一个下注
    ('13', {'option_A': {'banker': [{uids[0]: (100, 190, 0.5)}]},
            'option_B': {'buyer': [{uids[1]: (200, -200)}]}, 'res': 'option_A'}),
    # 结算A,当选项A无坐庄,无下注,选项B有一个坐庄,有多个下注(未买完)
    ('14', {'option_A': {'banker': [{uids[0]: (100, 142, 0.5)}]},
            'option_B': {'buyer': [{uids[1]: (100, -100)}, {uids[2]: (50, -50)}]}, 'res': 'option_A'}),
    # 结算A,当选项A无坐庄,无下注,选项B有一个坐庄,有多个下注(超庄)
    ('15', {'option_A': {'banker': [{uids[0]: (100, 190, 0.5)}]},
            'option_B': {'buyer': [{uids[1]: (100, -100)}, {uids[2]: (200, -100, 100)}]}, 'res': 'option_A'}),
    # 结算A,当选项A无坐庄,无下注,选项B有多个坐庄(同用户,同赔率),有一个下注(跨庄)
    ('16', {'option_A': {'banker': [{uids[0]: (100, 380, 0.5)}, {uids[0]: (100, 380, 0.5)}]},
            'option_B': {'buyer': [{uids[1]: (400, -400)}]}, 'res': 'option_A'}),
    # 结算A,当选项A无坐庄,无下注,选项B有多个坐庄(不同用户,同赔率),有一个下注(跨庄)
    ('17', {'option_A': {'banker': [{uids[0]: (100, 190, 0.5)}, {uids[1]: (100, -210, 0.5)}]},
            'option_B': {'buyer': [{uids[1]: (400, -210)}]}, 'res': 'option_A'}),
    # 结算A,当选项A无坐庄,无下注,有一个下注(超庄),选项B有多个坐庄(不同用户,不同赔率)
    ('18', {'option_A': {'banker': [{uids[0]: (100, 0, 0.5)}, {uids[2]: (100, 157, 0.6)}]},
            'option_B': {'buyer': [{uids[1]: (170, -166, 166)}]}, 'res': 'option_A'}),
    # 结算A,当选项A无坐庄,无下注,选项B有多个坐庄,多个下注
    ('19', {'option_A': {'banker': [{uids[3]: (100, 95, 0.5)}, {uids[4]: (100, 157, 0.6)}]},
            'option_B': {'buyer': [{uids[0]: (100, -100)}, {uids[1]: (100, -66, 66)}, {uids[2]: (100, -100)}]}, 'res': 'option_A'}),
    ## 有坐庄有下注 - 两边有坐庄下注
    ('20', {'option_A': {'banker': [{uids[0]: (100, 9, 9.9)}, {uids[1]: (100, 19, 5)}, {uids[2]: (100, 190, 0.5)}],
                         'buyer': [{uids[3]: (20, 94, 10)}, {uids[4]: (10, 47)}, {uids[5]: (100, 47, 10)}, {uids[6]: (200, 95)}]},
            'option_B': {'banker': [{uids[7]: (100, -100, 9.9)}, {uids[8]: (100, -100, 5)}, {uids[9]: (100, -100, 0.5)}],
                         'buyer': [{uids[10]: (10, -10, 10)}, {uids[11]: (10, -10)}, {uids[12]: (100, -10, 10)}, {uids[13]: (200, -200)}]},
            'res': 'option_A'}),
]
