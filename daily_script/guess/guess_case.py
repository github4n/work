#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/12/26 10:27
# Author : lixingyun

uids = [str(i) for i in range(5524, 5624)]

# for uid in uids:
#     Common.set_money(uid,999999,999999)
#     Common.set_xd(uid, 999999)
# exit()
# 用例ID,{用户:下注选项,结果1,2,loss,dog时的预期}
gamble_case_lists = [
    # 1.当选项1有下注,2无下注,单
    (
        {'uid': uids[0], '1': 100, 'ret': [0, -100, 0]},
    ),
    # 2.当选项1有下注,2无下注,多
    (
        {'uid': uids[0], '1': 100, 'ret': [0, -100, 0]},
        {'uid': uids[1], '1': 100, 'ret': [0, -100, 0]}
    ),
    # 3.当选项2有下注,1无下注,单
    (
        {'uid': uids[0], '2': 100, 'ret': [-100, 0, 0]},
    ),
    # 4.当选项2有下注,1无下注,多
    (
        {'uid': uids[0], '2': 100, 'ret': [-100, 0, 0]},
        {'uid': uids[1], '2': 100, 'ret': [-100, 0, 0]}
    ),
    # 5.当选项12都有下注,两个用户,1:1,1:1
    (
        {'uid': uids[0], '1': 1, 'ret': [0, -1, 0]},
        {'uid': uids[1], '2': 1, 'ret': [-1, 0, 0]}
    ),
    # 6.当选项12都有下注,两个用户,1:1,1:10
    (
        {'uid': uids[0], '1': 1, 'ret': [9, -1, 0]},
        {'uid': uids[1], '2': 10, 'ret': [-10, 0, 0]}
    ),
    # 7.当选项12都有下注,两个用户,1:1,2:100
    (
        {'uid': uids[0], '1': 1, 'ret': [95, -1, 0]},
        {'uid': uids[1], '2': 100, 'ret': [-100, 0, 0]}
    ),
    # 8.当选项12都有下注,两个用户,1:10,2:100
    (
        {'uid': uids[0], '1': 10, 'ret': [95, -10, 0]},
        {'uid': uids[1], '2': 100, 'ret': [-100, 9, 0]}
    ),
    # 9.当选项12都有下注,两个用户,1:1000,2:1000
    (
        {'uid': uids[0], '1': 1000, 'ret': [950, -1000, 0]},
        {'uid': uids[1], '2': 1000, 'ret': [-1000, 950, 0]}
    ),
    # 10.当选项12都有下注,多个用户,A1:1,A2:1,B1:1,B2:1
    (
        {'uid': uids[0], '1': 1, 'ret': [0, -1, 0]},
        {'uid': uids[1], '1': 1, 'ret': [0, -1, 0]},
        {'uid': uids[2], '2': 1, 'ret': [-1, 0, 0]},
        {'uid': uids[3], '2': 1, 'ret': [-1, 0, 0]}
    ),
    # 11.当选项AB都有下注,多个用户,A1:1,A2:1,B1:10,B2:10
    (
        {'uid': uids[0], '1': 1, 'ret': [9, -1, 0]},
        {'uid': uids[1], '1': 1, 'ret': [9, -1, 0]},
        {'uid': uids[2], '2': 10, 'ret': [-10, 0, 0]},
        {'uid': uids[3], '2': 10, 'ret': [-10, 0, 0]}
    ),
    # 12.当选项AB都有下注,多个用户,A1:1,A2:1,B1:100,B2:100
    (
        {'uid': uids[0], '1': 1, 'ret': [95, -1, 0]},
        {'uid': uids[1], '1': 1, 'ret': [95, -1, 0]},
        {'uid': uids[2], '2': 100, 'ret': [-100, 0, 0]},
        {'uid': uids[3], '2': 100, 'ret': [-100, 0, 0]}
    ),
    # 13.当选项AB都有下注,多个用户,A1:10,A2:20,B1:100,B2:300
    (
        {'uid': uids[0], '1': 10, 'ret': [126, -10, 0]},
        {'uid': uids[1], '1': 20, 'ret': [253, -20, 0]},
        {'uid': uids[2], '2': 100, 'ret': [-100, 7, 0]},
        {'uid': uids[3], '2': 300, 'ret': [-300, 21, 0]}
    ),
]
# 用例ID,{用户:banker(选项,下注,赔率)坐庄buyer(选项,下注额,实际额)下注,ret:1,2,loss/dog时的预期}
banker_case_lists = [
    # 结算A
    ## 有坐庄无下注时
    # 1.当选项1有坐庄,无下注,选项2无坐庄,无下注
    (
        {'uid': uids[0], 'banker': {'1': [100, 2]}, 'ret': [0, 0, 0]},
    ),
    # 2.当选项1有多个坐庄,无下注,选项2无坐庄,无下注
    (
        {'uid': uids[0], 'banker': {'1': [100, 2]}, 'ret': [0, 0, 0]},
        {'uid': uids[1], 'banker': {'1': [100, 2]}, 'ret': [0, 0, 0]},
    ),
    # 3.当选项1无坐庄,无下注,选项2有坐庄,无下注
    (
        {'uid': uids[0], 'banker': {'2': [100, 2]}, 'ret': [0, 0, 0]},
    ),
    # 4.当选项1无坐庄,无下注,选项2有多个坐庄,无下注
    (
        {'uid': uids[0], 'banker': {'2': [100, 2]}, 'ret': [0, 0, 0]},
        {'uid': uids[1], 'banker': {'2': [100, 2]}, 'ret': [0, 0, 0]},
    ),
    # 5.当选项1,2都有庄,无下注
    (
        {'uid': uids[0], 'banker': {'1': [100, 2], '2': [100, 2]}, 'ret': [0, 0, 0]},
        {'uid': uids[1], 'banker': {'1': [100, 2], '2': [100, 2]}, 'ret': [0, 0, 0]},
    ),
    ## 有坐庄有下注 - 单边有坐庄下注
    # 6.当选项1有一个坐庄,有一个下注,选项2无坐庄,无下注
    (
        {'uid': uids[0], 'banker': {'1': [100, 10.9]}, 'ret': [-99, 9, 0]},
        {'uid': uids[1], 'buyer': {'1': [10, 10.9]}, 'ret': [94, -10, 0]},
    ),
    # 7.当选项1有一个坐庄,有多个下注(未买完),选项2无坐庄,无下注
    (
        {'uid': uids[0], 'banker': {'1': [100, 1.5]}, 'ret': [-75, 142, 0]},
        {'uid': uids[1], 'buyer': {'1': [100, 1.5]}, 'ret': [47, -100, 0]},
        {'uid': uids[2], 'buyer': {'1': [50, 1.5]}, 'ret': [23, -50, 0]},
    ),
    # 8.当选项1有一个坐庄,有多个下注(超庄),选项2无坐庄,无下注
    (
        {'uid': uids[0], 'banker': {'1': [100, 1.5]}, 'ret': [-100, 190, 0]},
        {'uid': uids[1], 'buyer': {'1': [100, 1.5]}, 'ret': [47, -100, 0]},
        {'uid': uids[2], 'buyer': {'1': [200, 1.5, 100]}, 'ret': [47, -100, 0]},
    ),
    # 9.当选项1有多个坐庄(同用户,同赔率),有一个下注(跨庄),选项2无坐庄,无下注
    (
        {'uid': uids[0], 'banker': [{'1': [100, 1.5]}, {'1': [100, 1.5]}], 'ret': [-200, 380, 0]},
        {'uid': uids[1], 'buyer': {'1': [400, 1.5]}, 'ret': [190, -400, 0]},
    ),
    # 10.当选项1有多个坐庄(不同用户,同赔率),有一个下注(跨庄),选项2无坐庄,无下注
    (
        {'uid': uids[0], 'banker': {'1': [100, 1.5]}, 'ret': [-100, 190, 0]},
        {'uid': uids[1], 'banker': {'1': [100, 1.5]}, 'ret': [-100, 190, 0]},
        {'uid': uids[2], 'buyer': {'1': [400, 1.5]}, 'ret': [190, -400, 0]},
    ),
    # 11.当选项1有多个坐庄(不同用户,不同赔率),有一个下注(超庄),选项2无坐庄,无下注
    (
        {'uid': uids[0], 'banker': {'1': [100, 1.5]}, 'ret': [0, 0, 0]},
        {'uid': uids[1], 'banker': {'1': [100, 1.6]}, 'ret': [-100, 157, 0]},
        {'uid': uids[2], 'buyer': {'1': [170, 1.6, 166]}, 'ret': [94, -166, 0]},
    ),
    # 12.当选项1有多个坐庄,多个下注,选项2无坐庄,无下注
    (
        {'uid': uids[0], 'banker': {'1': [100, 1.5]}, 'ret': [-50, 95, 0]},
        {'uid': uids[1], 'banker': {'1': [100, 1.6]}, 'ret': [-100, 157, 0]},
        {'uid': uids[2], 'buyer': {'1': [100, 1.6]}, 'ret': [57, -100, 0]},
        {'uid': uids[3], 'buyer': {'1': [100, 1.6, 66]}, 'ret': [37, -66, 0]},
        {'uid': uids[4], 'buyer': {'1': [100, 1.5]}, 'ret': [47, -100, 0]},
    ),
    # 13.当选项1无坐庄,无下注,选项2有一个坐庄,有一个下注
    (
        {'uid': uids[0], 'banker': {'2': [100, 1.5]}, 'ret': [190, -100, 0]},
        {'uid': uids[1], 'buyer': {'2': [200, 1.5]}, 'ret': [-200, 95, 0]},
    ),
    # 14.当选项1无坐庄,无下注,选项2有一个坐庄,有多个下注(未买完)
    (
        {'uid': uids[0], 'banker': {'2': [100, 1.5]}, 'ret': [142, -75, 0]},
        {'uid': uids[1], 'buyer': {'2': [100, 1.5]}, 'ret': [-100, 47, 0]},
        {'uid': uids[2], 'buyer': {'2': [50, 1.5]}, 'ret': [-50, 23, 0]},
    ),

    # 15.当选项1无坐庄,无下注,选项2有一个坐庄,有多个下注(超庄)
    (
        {'uid': uids[0], 'banker': {'2': [100, 1.5]}, 'ret': [190, -100, 0]},
        {'uid': uids[1], 'buyer': {'2': [100, 1.5]}, 'ret': [-100, 47, 0]},
        {'uid': uids[2], 'buyer': {'2': [200, 1.5, 100]}, 'ret': [-100, 47, 0]},
    ),
    # 16.当选项1无坐庄,无下注,选项2有多个坐庄(同用户,同赔率),有一个下注(跨庄)
    (
        {'uid': uids[0], 'banker': [{'2': [100, 1.5]}, {'2': [100, 1.5]}], 'ret': [380, -200, 0]},
        {'uid': uids[1], 'buyer': {'2': [400, 1.5]}, 'ret': [-400, 190, 0]},
    ),
    # 17.当选项A无坐庄,无下注,选项B有多个坐庄(不同用户,同赔率),有一个下注(跨庄)
    (
        {'uid': uids[0], 'banker': {'2': [100, 1.5]}, 'ret': [190, -100, 0]},
        {'uid': uids[1], 'banker': {'2': [100, 1.5]}, 'ret': [190, -100, 0]},
        {'uid': uids[2], 'buyer': {'2': [400, 1.5]}, 'ret': [-400, 190, 0]},
    ),
    # 18.当选项1无坐庄,无下注,有一个下注(超庄),选项2有多个坐庄(不同用户,不同赔率)
    (
        {'uid': uids[0], 'banker': {'2': [100, 1.5]}, 'ret': [0, 0, 0]},
        {'uid': uids[1], 'banker': {'2': [100, 1.6]}, 'ret': [157, -100, 0]},
        {'uid': uids[2], 'buyer': {'2': [170, 1.6, 166]}, 'ret': [-166, 94, 0]},
    ),
    # 19.当选项1无坐庄,无下注,选项2有多个坐庄,多个下注
    (
        {'uid': uids[0], 'banker': {'2': [100, 10.9]}, 'ret': [9, -99, 0]},
        {'uid': uids[1], 'banker': {'2': [100, 1.6]}, 'ret': [157, -100, 0]},
        {'uid': uids[2], 'buyer': {'2': [10, 10.9]}, 'ret': [-10, 94, 0]},
        {'uid': uids[3], 'buyer': {'2': [100, 1.6]}, 'ret': [-100, 57, 0]},
        {'uid': uids[4], 'buyer': {'2': [100, 1.6, 66]}, 'ret': [-66, 37, 0]},
    ),
    ## 20.有坐庄有下注 - 两边有坐庄下注
    (

        {'uid': uids[0], 'banker': {'1': [100, 10.9]}, 'ret': [-99, 9, 0]},
        {'uid': uids[1], 'banker': {'1': [100, 6]}, 'ret': [-100, 19, 0]},
        {'uid': uids[2], 'banker': {'1': [100, 1.5]}, 'ret': [-100, 190, 0]},

        {'uid': uids[3], 'banker': {'2': [100, 10.9]}, 'ret': [9, -99, 0]},
        {'uid': uids[4], 'banker': {'2': [100, 6]}, 'ret': [19, -100, 0]},
        {'uid': uids[5], 'banker': {'2': [100, 1.5]}, 'ret': [190, -100, 0]},

        {'uid': uids[6], 'buyer': {'1': [20, 10.9, 10]}, 'ret': [94, -10, 0]},
        {'uid': uids[7], 'buyer': {'1': [10, 6]}, 'ret': [47, -10, 0]},
        {'uid': uids[8], 'buyer': {'1': [100, 1.5, 10]}, 'ret': [47, -10, 0]},
        {'uid': uids[9], 'buyer': {'1': [200, 1.5]}, 'ret': [95, -200, 0]},

        {'uid': uids[10], 'buyer': {'2': [11, 10.9, 10]}, 'ret': [-10, 94, 0]},
        {'uid': uids[11], 'buyer': {'2': [10, 6]}, 'ret': [-10, 47, 0]},
        {'uid': uids[12], 'buyer': {'2': [100, 1.5, 10]}, 'ret': [-10, 47, 0]},
        {'uid': uids[13], 'buyer': {'2': [200, 1.5]}, 'ret': [-200, 95, 0]},

    ),

]
