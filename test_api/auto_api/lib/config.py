#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 16:37:48
# @Author  : lixingyun


import time
import logging

logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S %p',
                    level=logging.INFO,
                    # filename='test.log',
                    filemode='w')
# 请求的域名
domain_web = 'http://lxy.new.huomaotv.com.cn'
domain_api = 'http://lxyapi.new.huomaotv.com.cn'
# 超管
super_uid = '1870709'

# domain = 'https://www.huomao.com/'
# 测试用例路径
# if platform.system() == 'Linux':
#     case_file = os.path.dirname(os.path.abspath(__file__)) + '/test_case.xlsx'
# else:
#     case_file = os.path.dirname(os.path.abspath(__file__)) + '\\test_case.xlsx'
case_file = 'test_case.xlsx'
# 测试报告数据
report_data = {'report_res': [],
               'test_sum': 0,
               'test_success': 0,
               'test_failed': 0,
               'test_date': time.strftime("%Y-%m-%d %X", time.localtime())}
# 接口信息
interface = {
    'admingag': {'name': '超管禁言',
                 'url': 'myroom/addUserGag',
                 'method': 'post',
                 'data': {'cid': '',
                          'uid': 1,
                          'user_uid': '',
                          'gag_type': 24,
                          'nickname': '',
                          'text': ''
                          },
                 },
    'admindelgag': {'name': '超管禁言',
                    'url': 'myroom/delGagForSuper',
                    'method': 'post',
                    'data': {'cid': 0,
                             'uid': '',
                             'user_uid': 1,
                             'gag_type': 24,
                             'nickname': '',
                             'text': ''
                             },
                    },
}
