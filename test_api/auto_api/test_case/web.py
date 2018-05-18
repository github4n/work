#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/18 14:53
# Author : lixingyun
# Description :

import unittest
from nose_parameterized import parameterized
import requests
from ..lib.config import UID
from ..lib.lib import req

cases = [
    # 首页
    ('/plugs/getCacheTime', dict(code='100')),
    ('/user/checkUserLoginStat', dict(code='100')),
    ('/member/checkUsersIdentify', dict(code='110')),
    ('/money/getUserMoney', dict(code=200)),
    ('/member/retUserLVinfo', dict(code='130')),
    ('/abcde/abcde.json?cur_page=web_channellist&cid=0&gid=0&labelID=0', dict(code='180')),
    ('/ajax/get_outdoor?cid=2&callback=', dict(anchorUid='1522')),
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


def new_name_func(func, num, p):
    return func.__name__ + '_' + str(num + 1)


class TestWeb(unittest.TestCase):
    @parameterized.expand(cases, name_func=new_name_func)
    def test(self, *args):
        # 接口信息
        self.name = 'WEB'
        self.url = args[0]
        self.method = 'get'
        # 默认报错信息
        # self.info = ''
        # 默认登录用户
        self.user = UID
        # 默认请求数据
        self.data = dict()
        self.exp_res = args[1]
        req(self)

