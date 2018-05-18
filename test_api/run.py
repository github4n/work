#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 16:37:15
# @Author  : lixingyun
import unittest
import datetime
import sys
import os
from auto_api.lib import HTMLTestRunner
from auto_api.lib.lib import report_data
# from auto_api.test_case.web_noble import TestNoble
from auto_api.test_case.web_gift import TestGift
# from auto_api.test_case.web_msg import TestMsg
# from auto_api.test_case.web import TestWeb


# 获取文件的当前路径（绝对路径）
cur_path = os.path.dirname(os.path.realpath(__file__))
filename = cur_path + '/result/{}.html'.format(datetime.datetime.now().strftime('%b_%d_%Y_%H_%M_%S'))
fp = open(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp)
# 全部执行
unittest.main(testRunner=runner, exit=False)
# print(1) if report_data.get('test_failed') == 0 else print(0)

# 执行单个class
# suite = unittest.makeSuite(TestWeb)
# print(dir(suite))
# print(suite._tests)

# 执行单个类单个用例  #test_1_4
# suite = unittest.TestSuite()
# suite.addTest(TestWeb('test_1'))
# runner = unittest.TextTestRunner()
# runner.run(suite)
