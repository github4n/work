import time


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
