#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 16:37:15
# @Author  : lixingyun
import unittest
import datetime
import os
from auto_api.lib import HTMLTestRunner
from auto_api.test_case.web_noble import TestNoble
from auto_api.test_case.web_gift import TestGift

# 全部执行
# unittest.main()
# 执行单个class
# suite = unittest.makeSuite(TestNoble)

# 执行单个类单个用例  #test_1_4
suite = unittest.TestSuite()
# for i in range(1,15):
#     suite.addTest(TestNoble('test_4_{}'.format(i)))
suite.addTest(TestGift('test_gift_5'))
runner = unittest.TextTestRunner()
# filename = './result/{}.html'.format(datetime.datetime.now().strftime('%b_%d_%Y_%H_%M_%S'))
# fp = open(filename, "wb")
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp)

runner.run(suite)
