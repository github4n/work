#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/3/8 14:16
# Author : lixingyun
import unittest
from nose_parameterized import parameterized
import requests
import time
import logging
from common.common import Common

DOMAIN = 'http://lxy.dev.rose.live'


class TestPrivateShow(unittest.TestCase):
    def setUp(self):
        self.url = '/PrivateShow/joinShow'
        self.data = {}
        # 主播房间号
        self.data['cid'] = '10'
        # 参加模式 1 私聊 2群聊
        self.data['showModel'] = '1'

    def test(self):
        res = requests.get(DOMAIN + self.url, params=self.data,cookies=Common.generate_cookies(1522)).text
        Common.try_json(res)

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestPrivateShow('test'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
