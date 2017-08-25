# -*- coding:utf-8 -*-
import unittest
import time
import HTMLTestRunner
import os

if __name__ == "__main__":
    # 用例目录
    filepath = os.getcwd()
    listcase = filepath + r'\testcase'

    def creatsuitel():
        testunit = unittest.TestSuite()
        # discover 方法,加载目录下testcase
        discover = unittest.defaultTestLoader.discover(
            listcase,
            pattern='case2*.py',
            top_level_dir=None
        )
        # discover 方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discover:
            print(test_suite)
            for test_case in test_suite:
                testunit.addTests(test_case)
                # print(testunit)
        return testunit

    alltestnames = creatsuitel()
    print(alltestnames)
    # 取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 定义个报告存放路径，支持相对路径
    filename = filepath + '\\result\\' + now + 'result.html'
    fp = open(filename, "wb")

    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')

    # 运行测试用例
    runner.run(alltestnames)
