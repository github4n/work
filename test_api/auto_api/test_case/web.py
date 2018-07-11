#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/18 14:53
# Author : lixingyun
# Description :

import unittest
from time import time
from parameterized import parameterized
from huomao.common import Common
from ..lib.config import UID
from ..lib.lib import req
from .web_data import admin_cases


def new_name_func(func, num, p):
    return func.__name__ + '_' + str(num + 1)


cases = [
    # 首页
    ('/plugs/getCacheTime', dict(code='100')),
    ('/user/checkUserLoginStat', dict(code='100')),
    ('/member/checkUsersIdentify', dict(code='110')),
    ('/money/getUserMoney', dict(code=200)),
    ('/member/retUserLVinfo', dict(code='130')),
    ('/abcde/abcde.json?cur_page=web_channellist&cid=0&gid=0&labelID=0', dict(code='180')),
    ('/ajax/get_outdoor?cid=2', dict(anchorUid='1522')),
    ('/ajax/getAnchorGiftByMon.json?anchor_uid=1522', dict(code=100)),
    ('/eventcenter/getThirdMatchGuessList.json', dict(code=101)),
    ('/eventcenter/getThirdMatchGuessList.json', dict(code=101)),
    ('/abcde/abcde.json?cur_page=web_index', dict(code='180')),
    ('/plugs/getHotWords', dict(code=200)),
    # 列表页
    ('/channels/tabChannels.json', dict(code='120')),
    ('/channels/channel.json?page=1&game_url_rule=all', dict(code=100)),
    ('/Popup/show', dict(code=200)),
]


class TestWeb(unittest.TestCase):
    @parameterized.expand(cases, name_func=new_name_func)
    def test(self, *args):
        # 接口信息
        self.domain = 'http://www.huomao.com'
        self.name = 'WEB'
        self.url = args[0]
        self.method = 'get'
        # 默认登录用户
        self.user = UID
        # 默认请求数据
        self.data = dict()
        self.exp_res = args[1]
        req(self)




class TestAdmin(unittest.TestCase):
    @parameterized.expand(admin_cases, name_func=new_name_func)
    def test_admin(self, *args):
        # 接口信息
        self.name = 'ADMIN'
        self.url = args[0]
        self.method = 'get'
        # 默认登录用户
        self.user = UID
        # 默认请求数据
        self.data = dict()
        self.exp_res = ''
        req(self)


cases_api = [
    ('/channels/channelDetail', dict(refer='android',
                                     cid=9418,
                                     expires_time=1527757747,
                                     post_data=1,
                                     time=1528181184,
                                     uid=27064,
                                     now_time=int(time()) + 100,
                                     an=67,
                                     ver='dev2.4', ), dict(code='100'))
]


class TestApi(unittest.TestCase):
    @parameterized.expand(cases_api, name_func=new_name_func)
    def test_api(self, *args):
        # 接口信息
        self.domain = 'http://test1.api.huomao.com'
        self.name = 'API'
        self.url = args[0]
        self.method = 'get'
        # 默认登录用户
        self.user = UID
        # 默认请求数据
        self.data = args[1]
        self.exp_res = args[2]
        req(self)
