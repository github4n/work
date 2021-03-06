#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 16:37:15
# @Author  : lixingyun
import unittest
import datetime
import logging
import sys
import os
from auto_api.lib import HTMLTestRunner
from auto_api.lib.lib import report_data

# from auto_api.test_case.web_noble import TestNoble
# from auto_api.test_case.web_gift import TestGift
# from auto_api.test_case.web_msg import TestMsg
# from auto_api.test_case.web import TestWeb
# from auto_api.test_case.web import TestAdmin
# from auto_api.test_case.web import TestApi
from auto_api.test_case.web_noble import TestNoble


def run_all():
    # 获取文件的当前路径（绝对路径）
    cur_path = os.path.dirname(os.path.realpath(__file__))
    filename = cur_path + f"/result/{datetime.datetime.now().strftime('%b_%d_%Y_%H_%M_%S')}.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp)
    # runner = unittest.TextTestRunner()
    # 全部执行
    unittest.main(testRunner=runner, exit=False)
    report_data.get('test_failed') == 0 and print(0)

# run_all()
# exit()
# 执行单个class
# suite = unittest.makeSuite(TestWeb)
# print(dir(suite))
# print(suite._tests)

# 执行单个类单个用例  #test_1_4

# for i in range(1,165):
#     suite.addTest(TestNoble('test_{}'.format(i)))
# suite = unittest.TestSuite()
# for i in range(1,11):
#     suite.addTest(TestNoble(f'test_{i}'))
# suite.addTest(TestNoble('test_1'))
#
suite = unittest.makeSuite(TestNoble)
runner = unittest.TextTestRunner()
runner.run(suite)
