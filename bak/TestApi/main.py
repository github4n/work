# -*- coding: utf-8 -*-
# ****************************************************************
# main.py
# Author     : LUCKY
# Version    : 1.0
# Date       : 2016-05-04
# Description: 测试组装，用例执行入口
# ****************************************************************
import unittest
from lib.testframe import create_excel
from lib import HTMLTestRunner
from config.config import excel_cases, excel_results, argbegin, titleindex, casebegin, url, resulthtml


class tes(unittest.TestCase):

    def setUp(self):
        pass

    def test_test1(self):
        c = create_excel(excel_cases[0], excel_results[0], argbegin, titleindex, casebegin, url)
        res = c.assertres()

        self.assertEqual(res[2], 0, res[3])

    def test_test2(self):
        c = create_excel(excel_cases[1], excel_results[1], argbegin, titleindex, casebegin, url)
        c.assertres()
        print(c.assertres())

    def test_test3(self):
        self.assertEqual(1, 2)

    def tearDown(self):
        pass


fp = open(resulthtml, "wb")
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')

# 运行测试用例
suite = unittest.TestSuite()
suite.addTest(tes("test_test1"))
suite.addTest(tes("test_test2"))
# runner = unittest.TextTestRunner()
runner.run(suite)

