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
import random

url = 'http://gate.huomaotv.com.cn:7173/1/push/room?rid=2'


def test(i):
    nick_name = "t1stnoble{}nc".format(random.randint(1, 10000))
    join_data = {
        "code": "400011",
        "time": "1525948661",
        "platform": "1",
        "join": {
            "user": {
                "name": nick_name,
                "uid": "1522",
                "avatar": "http://img.new.huomaotv.com.cn/upload/web/images/headimgs/3e53e16551c07c21d8317e3cb3a04e46/20180305152310358_big.jpeg",
                "level": "36"
            },
            "fans": {
                "level": "22",
                "name": "粉丝",
                "cid": "100",
                "rid": "100",
                "rname": "我的直播间",
                "gname": "格斗怀旧",
                "gcmd": "FTG",
                "avatar": "http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_1_normal.png",
                "zb_name": "hm_10000103",
                "is_live": ""
            },
            "badge": [
                {
                    "bid": "48",
                    "name": "绝版感恩徽章",
                    "img": "/upload/admin/file/hm/20171117112514UzOykQP3.png",
                    "expire": "7222天15小时后过期",
                    "click_type": "0",
                    "click_url": "",
                    "extend": {
                        "height": "20",
                        "width": "80"
                    },
                    "desc": ""
                },
                {
                    "bid": "47",
                    "name": "感恩徽章",
                    "img": "/upload/admin/file/hm/20171117112220sqP5gb28.png",
                    "expire": "12天16小时后过期",
                    "click_type": "0",
                    "click_url": "",
                    "extend": {
                        "height": "20",
                        "width": "70"
                    },
                    "desc": ""
                },
                {
                    "bid": "36",
                    "name": "徽章女神活动啦拉拉",
                    "img": "/upload/admin/file/hm/20171031103120vaR826iq.png",
                    "expire": "永久",
                    "click_type": "0",
                    "click_url": "",
                    "extend": {
                        "height": "20",
                        "width": "60"
                    },
                    "desc": "徽章女神活动啦啦啦啊"
                }
            ],
            "channel": {
                "name": "<br>jwdasd",
                "cid": "2",
                "rid": "1",
                "screenType": "2",
                "platType": "1"
            },
            "extend": {
                "is_guard": "0",
                "is_noble": "1",
                "noble_info": {
                    "id": "18",
                    "uid": "1522",
                    "anchor_id": "0",
                    "level": str(random.randint(4, 7)),
                    "type": "1",
                    "start_time": "1525769942",
                    "end_time": "1528532950",
                    "update_time": "1525940950",
                    "status": "1"
                },
                "is_zb": "1",
                "is_fg": "0",
                "is_cg": "0"
            }
        }
    }
    msg_data = {
        "code": "100001",
        "time": "1526364744",
        "platform": "1",
        "speak": {
            "user": {
                "name": nick_name,
                "uid": "23650",
                "avatar": "http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_3_big.png",
                "level": "7"
            },
            "fans": {

            },
            "badge": [

            ],
            "channel": {
                "name": "<br>jwdasd",
                "cid": "2",
                "rid": "1",
                "screenType": "2",
                "platType": "1"
            },
            "extend": {
                "is_guard": "0",
                "is_noble": "1",
                "noble_info": {
                    "id": "664",
                    "uid": "23650",
                    "anchor_id": "0",
                    "level": str(random.randint(4, 7)),
                    "type": "1",
                    "start_time": "1526357039",
                    "end_time": "1531583999",
                    "update_time": "1526357049",
                    "status": "1"
                },
                "is_zb": "0",
                "is_fg": "0",
                "is_cg": "0"
            },
            "barrage": {
                "type": "600",
                "msg": "testmsg{}".format(random.randint(1, 10000)),
                "color": "",
                "num": "0"
            }
        }
    }
    gift_data = {
        "code": "300002",
        "time": "1526366306",
        "platform": "1",
        "gift": {
            "user": {
                "name": nick_name,
                "uid": str(random.randint(1, 10000)),
                "avatar": "http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_3_big.png",
                "level": "7"
            },
            "fans": {
                "level": "3",
                "name": "不要哦",
                "cid": "2",
                "rid": "1",
                "rname": "",
                "gname": "",
                "gcmd": "",
                "avatar": "",
                "zb_name": "哈哈哈哈哈哈哈",
                "is_live": "0"
            },
            "badge": [

            ],
            "channel": {
                "name": "<br>jwdasd",
                "cid": "2",
                "rid": "1",
                "screenType": "2",
                "platType": "1"
            },
            "anchor": {
                "avatar": "http://img.new.huomaotv.com.cn/upload/web/images/headimgs/3e53e16551c07c21d8317e3cb3a04e46/20180305152310358_normal.jpeg",
                "name": "哈哈哈哈哈哈哈",
                "uid": "1522"
            },
            "extend": {
                "is_guard": "0",
                "is_noble": "1",
                "noble_info": {
                    "id": "664",
                    "uid": "23650",
                    "anchor_id": "0",
                    "level": "2",
                    "type": "1",
                    "start_time": "1526357039",
                    "end_time": "1531583999",
                    "update_time": "1526357049",
                    "status": "1"
                },
                "is_zb": "0",
                "is_fg": "0",
                "is_cg": "0"
            },
            "gift": {
                "gift_id": "8",
                "name": "招财猫520",
                "before_count": "1",
                "current_count": "2",
                "send_count": "1",
                "resource_path": "http://img.new.huomaotv.com.cn/",
                "img": "/static/web/images/gift/20161213144247VMo1FpYb.png",
                "effect": "/upload/web/images/gift/20170420193626FwuYDEkl.gif",
                "word": "送了",
                "screen_effect": {
                    "effect": "/upload/web/images/gift/20170420193626FwuYDEkl1.gif",
                    "frame": {
                        "img": "/upload/web/images/gift/20170425153955jradcF2M.png",
                        "num": "30",
                        "time": "3",
                        "height": "12600"
                    }
                },
                "screen_hf": {
                    "img": "/upload/web/images/gift/20170420193626FwuYDEkl.png",
                    "time": "10"
                },
                "barrage": {
                    "img": "/upload/web/images/gift/20171226180453z8BeTcqo.png",
                    "effect": "/upload/web/images/gift/20170316175309oiBEgV9u.swf",
                    "effect_mobile": "/upload/web/images/gift/20180111191138z9P2EH5r.gif",
                    "mobile_dm_hf": "/upload/web/images/gift/20180111191138z9P2EH5r.png",
                    "head_background": "/upload/web/images/gift/20180209154319iZ5jQ4u2.png",
                    "mid_background": "/upload/web/images/gift/20180209154319iZ5jQ4u21.png",
                    "tail_background": "/upload/web/images/gift/20180209154319iZ5jQ4u22.png"
                },
                "bannerWords": {
                    "isTarget": "1",
                    "targetUrl": "2",
                    "img": {
                        "resource_path": "http://img.new.huomaotv.com.cn/",
                        "head": "/upload/web/images/gift/20180111191138z9P2EH5r.gif",
                        "background": "/upload/web/images/gift/20180111191138z9P2EH5r.png",
                        "head_background": "/upload/web/images/gift/20180209154319iZ5jQ4u2.png",
                        "mid_background": "/upload/web/images/gift/20180209154319iZ5jQ4u21.png",
                        "tail_background": "/upload/web/images/gift/20180209154319iZ5jQ4u22.png"
                    },
                    "text": [
                        {
                            "text": nick_name,
                            "color": "#F8E81C"
                        },
                        {
                            "text": "送了",
                            "color": "#FFFFFF"
                        },
                        {
                            "text": "哈哈哈哈哈哈哈",
                            "color": "#F8E81C"
                        },
                        {
                            "text": "招财猫520 × 1",
                            "color": "#FFFFFF"
                        }
                    ],
                    "channelType": {
                        "type": "1",
                        "screenType": "2"
                    }
                }
            }
        }
    }
    kt_data = {
        "code": "800004",
        "time": "1526367178",
        "platform": "1",
        "noble": {
            "screen_hf": {
                "img": "static/web/nobility/img/jm_sc_4.png",
                "time": "10"
            },
            "screen_effect": {
                "effect": "static/web/nobility/img/xlz_4.gif",
                "frame": {
                    "height": "21000",
                    "img": "static/web/nobility/img/xlz_4.png",
                    "num": "50",
                    "time": "5"
                }
            },
            "bannerWords": {
                "isTarget": "1",
                "targetUrl": "2",
                "img": {
                    "head": "static/web/images/playerguizu/big/guizu_bo.png",
                    "background": "upload/web/images/gift/20171226180453z8BeTcqo.png",
                    "head_background": "static/web/images/playerguizu/banner/bo/left.png",
                    "mid_background": "static/web/images/playerguizu/banner/bo/center.png",
                    "tail_background": "static/web/images/playerguizu/banner/bo/right.png",
                    "resource_path": "http://img.new.huomaotv.com.cn/"
                },
                "text": [
                    {
                        "text": nick_name,
                        "color": "#FFF262"
                    },
                    {
                        "text": "在",
                        "color": "#FFFFFF"
                    },
                    {
                        "text": "哈哈哈哈哈哈哈",
                        "color": "#FFF262"
                    },
                    {
                        "text": "的直播间开通了",
                        "color": "#FFFFFF"
                    },
                    {
                        "text": "伯爵",
                        "color": "#FFF262"
                    },
                    {
                        "text": "立即围观>",
                        "color": "#FFFFFF"
                    }
                ],
                "channelType": {
                    "type": "1",
                    "screenType": "2"
                },
                "rid": "1"
            },
            "noble_info": {
                "uid": "23650",
                "level": "4",
                "type": "1",
                "status": "1"
            },
            "user": {
                "name": nick_name,
                "uid": "23650",
                "avatar": "http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_3_big.png"
            },
            "cid": "2",
            "is_xf": "",
            "resource_path": "http://img.new.huomaotv.com.cn/"
        }
    }
    data = []
    data.append(join_data)
    data.append(msg_data)
    data.append(gift_data)
    data.append(kt_data)
    res = requests.post(url, json=data[i], timeout=1)
    print(res.json())


for i in range(2):
    test(3)
    test(2)
    t = random.random()
    print(t)
    # time.sleep(4)
# while True:
#     test()
#     time.sleep(0.5)
