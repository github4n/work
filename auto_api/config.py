#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 16:37:48
# @Author  : lixingyun


import time
import logging

ENVIRONMENT = 'test'
logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S %p',
                    level=logging.DEBUG,
                    # filename='test.log',
                    filemode='w')
# 请求的域名
domain = 'http://qa.new.huomaotv.com.cn/'
# domain = 'https://www.huomao.com/'
# 测试用例路径
# if platform.system() == 'Linux':
#     case_file = os.path.dirname(os.path.abspath(__file__)) + '/testcase.xlsx'
# else:
#     case_file = os.path.dirname(os.path.abspath(__file__)) + '\\testcase.xlsx'
case_file = 'testcase.xlsx'
# 测试报告数据
report_data = {'report_res': [],
               'test_sum': 0,
               'test_success': 0,
               'test_failed': 0,
               'test_date': time.strftime("%Y-%m-%d %X", time.localtime())}

# 超管
superuid = '1870709'

# 接口信息
interface = {'msg': {'name': '发言',
                     'url': '/chatnew/msg',
                     'method': 'post',
                     'data': {'data': '测试弹幕',
                              'cid': 2,
                              'color_barrage': '',
                              'guard_barrage': '',
                              'isAdminPrivateChat': ''
                              }
                     },
             'gift': {'name': '送礼',
                     'url': '/chatnew/sendGift',
                     'method': 'get',
                     'data': {'cid': 2,
                              'gift': '',
                              't_count': 1,
                              'isbag': 0
                              }
                     },
             'gag': {'name': '禁言',
                     'url': '/myroom/setCommChannelGag',
                     'method': 'post',
                     'data': {'cid': '',  # 房间ID
                              'uid': '',  # 禁言用户ID
                              'status': 24,
                              'nickname': '',
                              'text': ''
                              },
                     },
             'delgag': {'name': '取消禁言',
                        'url': '/myroom/delCommUserGag',
                        'method': 'post',
                        'data': {'cid': '',  # 房间ID
                                 'uid': '',  # 禁言用户ID
                                 'status': '',
                                 'nickname': '',
                                 'text': ''
                                 },
                        },
             'admingag': {'name': '超管禁言',
                          'url': 'myroom/addUserGag',
                          'method': 'post',
                          'data': {'cid': '',
                                   'uid': superuid,
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
                                      'user_uid': superuid,
                                      'gag_type': 24,
                                      'nickname': '',
                                      'text': ''
                                      },
                             },
             'setroomadmin': {'name': '设置房管',
                              'url': 'myroom/setRoomAdministrator',
                              'method': 'post',
                              'data': {'uid': '',
                                       'username': ''
                                       }
                              },
             'delroomadmin': {'name': '设置房管',
                              'url': 'myroom/delRoomAdministrator',
                              'method': 'post',
                              'data': {'uid': '',
                                       'username': ''
                                       }
                              },
             }
