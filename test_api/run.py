#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 16:37:15
# @Author  : lixingyun
import unittest
from auto_api.test_case.web_noble import TestNoble


suite = unittest.TestSuite()
suite.addTest(TestNoble('test_2_1'))
runner = unittest.TextTestRunner()
runner.run(suite)


# pattern = '*_noble'
# test_dir = './auto_api/test_case'
# print(test_dir)
# filename = './{}result.html'.format(int(time.time()))
# fp = open(filename, "wb")
# discover = unittest.defaultTestLoader.discover(test_dir, pattern=pattern)
# print(discover)
# HTML测试报告
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp)
# runner.run(discover)
# 普通报告
# runner = unittest.TextTestRunner()
# runner.run(discover)
# 协程执行
# events = []
# for testsuites in discover:
#     for testsuite in testsuites:
#         for test in testsuite:
#             events.append(gevent.spawn(runner.run, test))
# gevent.joinall(events)
# if report:
#     generate_report()


