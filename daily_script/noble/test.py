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

cid = '13'
rid ='13'
url = 'http://gate.huomaotv.com.cn:7173/1/push/room?rid='+cid

nick_name = "t1stnoble{}nc".format(random.randint(1, 10000))
join_data = {
    "platform":"1",
    "join":{
        "channel":{
            "name":"<br>jwdasd",
            "screenType":"2",
            "cid":cid,
            "platType":"1",
            "rid":"1"
        },
        "user":{
            "name":"WWWWWWWWWWWWWW",
            "uid":"1522",
            "level":"7",
            "avatar":"http://img.new.huomaotv.com.cn/upload/web/images/headimgs/8e90d32205c4a00fc365c983cb9153a1/20180525152459875_big.jpeg"
        },
        "badge":[
            {
                "bid":"9",
                "img":"/upload/admin/file/hm/20171026172931ZjFciXCs.png",
                "desc":"9",
                "expire":"永久",
                "name":"富豪3",
                "click_url":"15213",
                "click_type":"2",
                "extend":{
                    "height":"20",
                    "width":"98"
                }
            },
            {
                "bid":"48",
                "img":"/upload/admin/file/hm/20171117112514UzOykQP3.png",
                "desc":"",
                "expire":"7207天17小时后过期",
                "name":"绝版感恩徽章",
                "click_url":"",
                "click_type":"0",
                "extend":{
                    "height":"20",
                    "width":"80"
                }
            },
            {
                "bid":"36",
                "img":"/upload/admin/file/hm/20171031103120vaR826iq.png",
                "desc":"徽章女神活动啦啦啦啊",
                "expire":"永久",
                "name":"徽章女神活动啦拉拉",
                "click_url":"",
                "click_type":"0",
                "extend":{
                    "height":"20",
                    "width":"60"
                }
            }
        ],
        "fans":{
            "is_live":"0",
            "zb_name":"WWWWWWWWWWWWWW",
            "gname":"",
            "level":"20",
            "rid":"1",
            "avatar":"",
            "name":"不要哦",
            "cid":cid,
            "gcmd":"",
            "rname":""
        },
        "extend":{
            "is_noble":"1",
            "is_fg":"0",
            "noble_info":{
                "update_time":"1527168091",
                "level":"7",
                "anchor_id":"0",
                "uid":"1522",
                "end_time":"1751444950",
                "status":"1",
                "id":"18",
                "type":"1",
                "start_time":"1525769942"
            },
            "is_zb":"1",
            "is_cg":"0",
            "is_guard":"0"
        }
    },
    "time":"1527236072",
    "code":"400011"
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
            "cid": cid,
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
            "cid": cid,
            "rid": rid,
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
            "cid": cid,
            "rid": rid,
            "screenType": "2",
            "platType": "1"
        },
        "anchor": {
            "avatar": "http://img.new.huomaotv.com.cn/upload/web/images/headimgs/3e53e16551c07c21d8317e3cb3a04e46/20180305152310358_normal.jpeg",
            "name": "哈哈哈哈哈哈哈",
            "uid": "5257"
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
kt_data_3 = {
    "code":"800004",
    "time":"1527737834",
    "platform":"1",
    "noble":{
        "screen_hf":{
            "img":"static/web/nobility/img/jm_sc_3.png",
            "time":"150",
            "m_time":"30"
        },
        "screen_effect":{
            "effect":"static/web/nobility/img/xlz_3.gif",
            "frame":{
                "height":"21000",
                "img":"static/web/nobility/img/xlz_3.png",
                "num":"50",
                "time":"5"
            }
        },
        "bannerWords":{
            "isTarget":"1",
            "targetUrl":"2",
            "img":{
                "head":"static/web/images/playerguizu/big/guizu_zi.png",
                "background":"static/web/images/playerguizu/banner/zi/down.png",
                "head_background":"static/web/images/playerguizu/banner/zi/left.png",
                "mid_background":"static/web/images/playerguizu/banner/zi/center.png",
                "tail_background":"static/web/images/playerguizu/banner/zi/right.png",
                "resource_path":"http://img.new.huomaotv.com.cn/"
            },
            "text":[
                {
                    "text":"t_n3834n",
                    "color":"#FFF262"
                },
                {
                    "text":"在",
                    "color":"#FFFFFF"
                },
                {
                    "text":"WWWWmingzi",
                    "color":"#FFF262"
                },
                {
                    "text":"的直播间开通了",
                    "color":"#FFFFFF"
                },
                {
                    "text":"子爵",
                    "color":"#FFF262"
                },
                {
                    "text":"立即围观>",
                    "color":"#FFFFFF"
                }
            ],
            "channelType":{
                "type":"1",
                "screenType":"2"
            },
            "rid":rid
        },
        "noble_info":{
            "uid":"27063",
            "level":"3",
            "type":"1",
            "status":"1"
        },
        "user":{
            "name":"t_n3834n",
            "uid":"27063",
            "avatar":"http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_0_big.png"
        },
        "cid":cid,
        "is_xf":"",
        "resource_path":"http://img.new.huomaotv.com.cn/"
    }
}
kt_data_4 = {
    "code": "800004",
    "time": "1526367178",
    "platform": "1",
    "noble": {
        "screen_hf": {
            "img": "static/web/nobility/img/jm_sc_4.png",
            "time": "20"
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
                    "text": 'sssssssss',
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
            "rid": rid
        },
        "noble_info": {
            "uid": "23650",
            "level": "4",
            "type": "1",
            "status": "1"
        },
        "user": {
            "name": 'sssssssss',
            "uid": "23650",
            "avatar": "http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_3_big.png"
        },
        "cid": cid,
        "is_xf": "",
        "resource_path": "http://img.new.huomaotv.com.cn/"
    }
}
kt_data_1 = {
    "code":"400011",
    "time":"1527586094",
    "platform":"1",
    "join":{
        "user":{
            "name":"t_n3786n",
            "uid":"27010",
            "avatar":"http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_0_big.png",
            "level":"0"
        },
        "fans":{

        },
        "badge":[

        ],
        "channel":{
            "name":"<br>jwdasd",
            "cid":cid,
            "rid":"1",
            "screenType":"2",
            "platType":"1"
        },
        "extend":{
            "is_guard":"0",
            "is_noble":"1",
            "noble_info":{
                "anchor_id":"5257",
                "start_time":"1527586054",
                "end_time":"1530201599",
                "update_time":"1527586054",
                "type":"1",
                "level":"1",
                "uid":"27010",
                "status":"1"
            },
            "is_zb":"0",
            "is_fg":"0",
            "is_cg":"0"
        }
    }
}
kt_data_5 = {
    "code": "800004",
    "time": "1527063967",
    "platform": "1",
    "noble": {
        "screen_hf": {
            "img": "static/web/nobility/img/jm_sc_5.png",
            "time": "20",
            "m_time": "45"
        },
        "screen_effect": {
            "effect": "static/web/nobility/img/xlz_5.gif",
            "frame": {
                "height": "21000",
                "img": "static/web/nobility/img/xlz_5.png",
                "num": "50",
                "time": "5"
            }
        },
        "bannerWords": {
            "isTarget": "1",
            "targetUrl": "2",
            "img": {
                "head": "static/web/images/playerguizu/big/guizu_gong.png",
                "background": "static/web/images/playerguizu/banner/gong/down.png",
                "head_background": "static/web/images/playerguizu/banner/gong/left.png",
                "mid_background": "static/web/images/playerguizu/banner/gong/center.png",
                "tail_background": "static/web/images/playerguizu/banner/gong/right.png",
                "resource_path": "http://img.new.huomaotv.com.cn/"
            },
            "text": [
                {
                    "text": "t_n3243nc",
                    "color": "#FFF262"
                },
                {
                    "text": "在",
                    "color": "#FFFFFF"
                },
                {
                    "text": "WWWWWWWWWWW",
                    "color": "#FFF262"
                },
                {
                    "text": "的直播间续费了",
                    "color": "#FFFFFF"
                },
                {
                    "text": "公爵",
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
            "uid": "26302",
            "level": "5",
            "type": "1",
            "status": "1"
        },
        "user": {
            "name": "t_n3243nc",
            "uid": "26302",
            "avatar": "http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_1_big.png"
        },
        "cid": cid,
        "is_xf": "1",
        "resource_path": "http://img.new.huomaotv.com.cn/"
    }
}
kt_data_6 = {
    "code": "800004",
    "time": "1527065049",
    "platform": "1",
    "noble": {
        "screen_hf": {
            "img": "static/web/nobility/img/jm_sc_6.png",
            "time": "20",
            "m_time": "50"
        },
        "screen_effect": {
            "effect": "static/web/nobility/img/xlz_6.gif",
            "frame": {
                "height": "21000",
                "img": "static/web/nobility/img/xlz_6.png",
                # "img": "static/web/nobility/img/min_xlz_6.png",
                "num": "50",
                "time": "5"
            }
        },
        "bannerWords": {
            "isTarget": "1",
            "targetUrl": "2",
            "img": {
                "head": "static/web/images/playerguizu/big/guizu_wang.png",
                "background": "static/web/images/playerguizu/banner/guo/down.png",
                "head_background": "static/web/images/playerguizu/banner/guo/left.png",
                "mid_background": "static/web/images/playerguizu/banner/guo/center.png",
                "tail_background": "static/web/images/playerguizu/banner/guo/right.png",
                "resource_path": "http://img.new.huomaotv.com.cn/"
            },
            "text": [
                {
                    "text": "t_n3246nc",
                    "color": "#FFF262"
                },
                {
                    "text": "在",
                    "color": "#FFFFFF"
                },
                {
                    "text": "WWWWWWWWWWW",
                    "color": "#FFF262"
                },
                {
                    "text": "的直播间开通了",
                    "color": "#FFFFFF"
                },
                {
                    "text": "国王",
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
            "uid": "26307",
            "level": "6",
            "type": "1",
            "status": "1"
        },
        "user": {
            "name": "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "uid": "26307",
            "avatar": "http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_3_big.png"
        },
        "cid": cid,
        "is_xf": "",
        "resource_path": "http://img.new.huomaotv.com.cn/"
    }
}
kt_data_7 = {
    "code": "800004",
    "time": "1527064149",
    "platform": "1",
    "noble": {
        "screen_hf": {
            "img": "static/web/nobility/img/jm_sc_7.png",
            "time": "20",
            "m_time": "60"
        },
        "screen_effect": {
            "effect": "static/web/nobility/img/xlz_7.gif",
            "frame": {
                "height": "21000",
                "img": "static/web/nobility/img/xlz_7.png",
                "num": "50",
                "time": "5"
            }
        },
        "bannerWords": {
            "isTarget": "1",
            "targetUrl": "2",
            "img": {
                "head": "static/web/images/playerguizu/big/guizu_di.png",
                "background": "static/web/images/playerguizu/banner/huang/down.png",
                "head_background": "static/web/images/playerguizu/banner/huang/left.png",
                "mid_background": "static/web/images/playerguizu/banner/huang/center.png",
                "tail_background": "static/web/images/playerguizu/banner/huang/right.png",
                "resource_path": "http://img.new.huomaotv.com.cn/"
            },
            "text": [
                {
                    "text": "t_n3243nc",
                    "color": "#FFF262"
                },
                {
                    "text": "在",
                    "color": "#FFFFFF"
                },
                {
                    "text": "WWWWWWWWWWW",
                    "color": "#FFF262"
                },
                {
                    "text": "的直播间续费了",
                    "color": "#FFFFFF"
                },
                {
                    "text": "皇帝",
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
            "rid": rid
        },
        "noble_info": {
            "uid": "26302",
            "level": "7",
            "type": "1",
            "status": "1"
        },
        "user": {
            "name": "t_n3243nc",
            "uid": "26302",
            "avatar": "http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_1_big.png"
        },
        "cid": cid,
        "is_xf": "1",
        "resource_path": "http://img.new.huomaotv.com.cn/"
    }
}

# 纯粉丝
data_400001 = {
    "code":"400001",
    "time":"1527576152",
    "platform":"1",
    "join":{
        "user":{
            "name":"t_n3780n",
            "uid":"27003",
            "avatar":"http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_3_big.png",
            "level":"0"
        },
        "fans":{
            "level":"25",
            "name":"不要哦",
            "cid":cid,
            "rid":"1",
            "rname":"<br>jwdasd",
            "gname":"QQ飞车",
            "gcmd":"QQfeiche",
            "avatar":"http://img.new.huomaotv.com.cn/upload/web/images/headimgs/031020510d6a488829d6e5e1ef3e7a8b/20180529101818562_normal.jpeg",
            "zb_name":"WWWWWWWWWWWWWWW",
            "is_live":"1"
        },
        "badge":[

        ],
        "channel":{
            "name":"<br>jwdasd",
            "cid":cid,
            "rid":"1",
            "screenType":"2",
            "platType":"1"
        },
        "extend":{
            "is_guard":"0",
            "is_noble":"0",
            "noble_info":{

            },
            "is_zb":"0",
            "is_fg":"0",
            "is_cg":"0"
        }
    }
}
# 粉丝加贵族
data_400011 = {
    "code":"400011",
    "time":"1527576698",
    "platform":"1",
    "join":{
        "user":{
            "name":"t_n3780n",
            "uid":"27003",
            "avatar":"http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_3_big.png",
            "level":"22"
        },
        "fans":{
            "level":"18",
            "name":"不要哦",
            "cid":cid,
            "rid":"1",
            "rname":"",
            "gname":"",
            "gcmd":"",
            "avatar":"",
            "zb_name":"WWWWWWWWWWWWWWW",
            "is_live":"0"
        },
        "badge":[

        ],
        "channel":{
            "name":"<br>jwdasd",
            "cid":cid,
            "rid":"1",
            "screenType":"2",
            "platType":"1"
        },
        "extend":{
            "is_guard":"0",
            "is_noble":"1",
            "noble_info":{
                "anchor_id":"1522",
                "start_time":"1527576677",
                "end_time":"1530201599",
                "update_time":"1527576677",
                "type":"1",
                "level":"7",
                "uid":"27003",
                "status":"1"
            },
            "is_zb":"0",
            "is_fg":"0",
            "is_cg":"0"
        }
    }
}
# 纯贵族
data_={
    "code":"400011",
    "time":"1527576838",
    "platform":"1",
    "join":{
        "user":{
            "name":"t_n3782n",
            "uid":"27005",
            "avatar":"http://img.new.huomaotv.com.cn/static/web/images/default_headimg/default_head_3_big.png",
            "level":"22"
        },
        "fans":{

        },
        "badge":[

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
                "anchor_id":"5257",
                "start_time":"1527576829",
                "end_time":"1535385599",
                "update_time":"1527576829",
                "type":"1",
                "level":"7",
                "uid":"27005",
                "status":"1"
            },
            "is_zb":"0",
            "is_fg":"0",
            "is_cg":"0"
        }
    }
}

def test(data):
    res = requests.post(url, json=data, timeout=1)
    print(res.json())




print(1533139199 - 1533052800)
# test(kt_data_7)
# test(kt_data_6)
#
# test(gift_data)