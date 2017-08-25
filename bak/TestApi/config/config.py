import os
import time

# 参数开始位置
argbegin = 3
# 用例标题索引
titleindex = 2
# 用例开始索引
casebegin = 3
# 测试用例路径
filepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\config'
# 测试结果路径
resfilepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\result'
# 接口域名
url = 'http://qa.new.huomaotv.com.cn'
# html报告地址
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
resulthtml = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\result\\' + now + 'result.html'

# 测试用例，结果集路径
excel_cases = []
excel_results = []
for name in os.listdir(filepath):
    if name.endswith('.xlsx'):
        # 生成excel文件的绝对路径
        excel_case = os.path.join(filepath, name)
        excel_cases.append(excel_case)
        excel_result = os.path.join(resfilepath, now + 'result' + name)
        excel_results.append(excel_result)
