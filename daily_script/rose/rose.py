#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/3/8 14:16
# Author : lixingyun
import unittest
from nose_parameterized import parameterized
import requests
from gevent import monkey
import gevent
import time
import logging
from huomao.common import Common
monkey.patch_all()
DOMAIN = 'http://lxy.dev.rose.live'


class TestPrivateShow(unittest.TestCase):
    def setUp(self):
        pass

    def test(self,i):
        res = requests.get(DOMAIN + self.url, params = self.data, cookies = Common.generate_cookies(i))
        Common.try_json(res.text)


    def test1(self):
        self.url = '/PrivateShow/joinShow'
        self.data = {}
        # 主播房间号
        self.data['cid'] = '10'
        res = requests.get(DOMAIN + self.url, params=self.data, cookies=Common.generate_cookies(5253)).text
        Common.try_json(res)

    def test11(self):
        self.url = '/PrivateShow/joinShow'
        self.data = {}
        # 主播房间号
        self.data['cid'] = '10'
        events = []
        for i in range(5524, 5624):
            events.append(gevent.spawn(self.test,i))
        gevent.joinall(events)

    def test2(self):
        self.url = '/PrivateShow/endShowByAll'
        self.data = {}
        # 主播房间号
        self.data['cid'] = '10'
        res = requests.get(DOMAIN + self.url, params=self.data, cookies=Common.generate_cookies(1522)).text
        Common.try_json(res)

    def test3(self):
        self.url = '/PrivateShow/endShowByUid'
        self.data = {}
        # 主播房间号
        self.data['cid'] = '10'
        res = requests.get(DOMAIN + self.url, params=self.data, cookies=Common.generate_cookies(1522)).text
        Common.try_json(res)

    def test4(self):
        self.url = '/PrivateShow/changeStatus'
        self.data = {}
        # 主播房间号
        self.data['cid'] = '14'
        res = requests.get(DOMAIN + self.url, params=self.data, cookies=Common.generate_cookies(1522)).text
        Common.try_json(res)

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestPrivateShow('test2'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
