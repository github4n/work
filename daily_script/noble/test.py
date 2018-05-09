#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/4/17 17:53
# Author : lixingyun
# Description : 测试贵族功能
import requests
import unittest
from huomao.common import Common

URL = 'http://lxy.new.huomaotv.com.cn/'


class TestNoble(unittest.TestCase):
    def setUp(self):
        self.data = dict(level=0, cid=0, month=0, type=0)
        self.url = URL + 'noble/createNoble'

    def test_1(self):
        self.cookies = Common.generate_cookies('')
        ret = requests.post(self.url, data=self.data, cookies=self.cookies).json()
        print(ret)

    def test_2(self):
        self.cookies = Common.generate_cookies('')
        ret = requests.post(self.url, data=self.data, cookies=self.cookies).json()
        print(ret)


if __name__ == '__main__':
    # 执行文件下所有用例
    # unittest.main()
    # 执行指定类下的所有用例
    # suite = unittest.TestSuite(unittest.makeSuite(TestNoble))
    # 执行单个用例
    suite = unittest.TestSuite()
    suite.addTest(TestNoble('test_2'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # test_dir = './'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='guess.py')
    # for i in discover:
    #     print(i)
