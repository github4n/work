#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/10/12 14:43
# Author : lixingyun

# 礼物不丢弃http://gate.huomaotv.com.cn:7172
# 普通达到速率后丢弃http://gate.huomaotv.com.cn:7173

# 全平台 /1/push/all
# 单房间 /1/push/room?rid=

import time
import requests
import json

url = 'http://gate.huomaotv.com.cn:7173/1/push/room?rid=2'
data = {
    "code":"400011",
    "time":"1525948661",
    "platform":"1",
    "join":{
        "user":{
            "name":"1",
            "uid":"1522",
            "avatar":"http://img.new.huomaotv.com.cn/upload/web/images/headimgs/3e53e16551c07c21d8317e3cb3a04e46/20180305152310358_big.jpeg",
            "level":"36"
        },
        "fans":{
            "level":"22",
            "name":"粉丝",
            "cid":"100",
            "rid":"100",
            "rname":"我的直播间",
            "gname":"格斗怀旧",
            "gcmd":"FTG",
            "avatar":"http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_1_normal.png",
            "zb_name":"hm_10000103",
            "is_live":""
        },
        "badge":[
            {
                "bid":"48",
                "name":"绝版感恩徽章",
                "img":"/upload/admin/file/hm/20171117112514UzOykQP3.png",
                "expire":"7222天15小时后过期",
                "click_type":"0",
                "click_url":"",
                "extend":{
                    "height":"20",
                    "width":"80"
                },
                "desc":""
            },
            {
                "bid":"47",
                "name":"感恩徽章",
                "img":"/upload/admin/file/hm/20171117112220sqP5gb28.png",
                "expire":"12天16小时后过期",
                "click_type":"0",
                "click_url":"",
                "extend":{
                    "height":"20",
                    "width":"70"
                },
                "desc":""
            },
            {
                "bid":"36",
                "name":"徽章女神活动啦拉拉",
                "img":"/upload/admin/file/hm/20171031103120vaR826iq.png",
                "expire":"永久",
                "click_type":"0",
                "click_url":"",
                "extend":{
                    "height":"20",
                    "width":"60"
                },
                "desc":"徽章女神活动啦啦啦啊"
            }
        ],
        "channel":{
            "name":"<br>jwdasd",
            "cid":"2",
            "rid":"1",
            "screenType":"2",
            "platType":"1"
        },
        "extend":{
            "is_guard":"0",
            "is_noble":"1",
            "noble_info":{
                "id":"18",
                "uid":"1522",
                "anchor_id":"0",
                "level":"7",
                "type":"1",
                "start_time":"1525769942",
                "end_time":"1528532950",
                "update_time":"1525940950",
                "status":"1"
            },
            "is_zb":"1",
            "is_fg":"0",
            "is_cg":"0"
        }
    }
}

def test():
    res = requests.post(url, json=data, timeout=1)
    print(res.json())


test()

# t1 = time.time()
# for i in range(1, 1000):
#     test()
# t2 = time.time()
# print(t2-t1)
