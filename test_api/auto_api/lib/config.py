#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 16:37:48
# @Author  : lixingyun


import time

# 请求的域名
domain_web = 'http://qa.new.huomaotv.com.cn'
domain_api = 'http://qaapi.new.huomaotv.com.cn'
# uid
UID = 1522
# 超管
super_uid = '1870709'

case_file = 'test_case.xlsx'
# 测试报告数据
report_data = {'report_res': [],
               'test_sum': 0,
               'test_success': 0,
               'test_failed': 0,
               'test_date': time.strftime("%Y-%m-%d %X", time.localtime())}
