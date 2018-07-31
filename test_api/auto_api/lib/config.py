#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 16:37:48
# @Author  : lixingyun

import os
import time
import logging
from huomao.config import ADMIN_COOKIES

# 请求的域名
domain_web = 'http://qa.new.huomaotv.com.cn'
domain_api = 'http://qaapi.new.huomaotv.com.cn'
domain_admin = 'http://qaadmin.new.huomaotv.com.cn'
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

# 获取文件的当前路径（绝对路径）
huomao_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
log_path = os.path.join(huomao_path, 'test_api.log')

# 创建文件处理器
handler = logging.FileHandler(log_path)

# 创建formatter
formatter = logging.Formatter('%(asctime)s %(filename)10s [line:%(lineno)5d] %(name)10s %(levelname)s %(message)s')
# Formatter绑定在Handler上
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

# 创建logger记录器实例
logger_test_api = logging.getLogger('test_api')
logger_test_api.setLevel(logging.DEBUG)

# Handler绑定在logger上
logger_test_api.addHandler(handler)
