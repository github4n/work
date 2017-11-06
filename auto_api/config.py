#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 16:37:48
# @Author  : lixingyun


import time
import logging

ENVIRONMENT = 'test'
logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S %p',
                    level=logging.INFO,
                    # filename='test.log',
                    filemode='w')
# 请求的域名
domain_web = 'http://lxy.new.huomaotv.com.cn'
domain_api = 'http://lxyapi.new.huomaotv.com.cn'
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
                     'url_api': '/chatnew/msg',
                     'method': 'post',
                     'data': {
                         'data': '测试弹幕',
                         'cid': 2,
                         'color_barrage': '',
                         'guard_barrage': '',
                         'isAdminPrivateChat': '',
                         'is_hotWord': '',
                     },
                     'exp_dict': {
                         'unlogin': {'status': False, 'code': '101', 'data': [], 'message': '未登录'},
                         'null': {'code': 202, 'status': False, 'message': '消息不能为空'},
                         'normal': {'code': 200, 'data': {}},
                         'length': {'code': 206, 'status': False, 'message': '您的发言已超出字符限制了~'},
                         'sensitive_words': {'code': 271, 'status': False, 'message': '发言包含敏感词，请重新输入'},
                         'time': {'status': False, 'code': 204, 'message': '你发言太快！'},
                         'no_phone': {'code': 2031, 'status': False, 'message': '绑定手机号即可发言'},
                         'fz': {'code': 200, 'data': {'extend': {'is_zb': '1'}}},
                     },
                     },
             'gift': {'name': '送礼',
                      'url': '/chatnew/sendGift',
                      'method': 'get',
                      'data': {'cid': 2,
                               'gift': 0,
                               't_count': 1,
                               'isbag': 0
                               },
                      'exp_dict': {
                          'insufficient_xd': {'message': '您剩余的仙豆数量不足！', 'status': False, 'code': 118},
                          'not_active': {'status': False, 'message': '礼物未激活', 'code': 211},
                          'anchor': {'status': False, 'code': 219, 'message': '自己不能给自己送礼物'},

                      },
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
