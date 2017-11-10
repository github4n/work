#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 16:37:48
# @Author  : lixingyun

import requests
from  urllib import parse
import json
import xlsxwriter
from config import domain_web,domain_api, interface,report_data
import logging
import unittest
import HTMLTestRunner
import time
import gevent
from gevent import monkey
from common.common import Common

monkey.patch_all()


# 比较dict
def cmp_dict(dict1, dict2):
    if dict1 == '':
        return True
    assert type(dict1) == type(dict2), "type: '{}' != '{}'".format(type(dict1), type(dict2))
    if isinstance(dict1, dict):
        for key in dict1:
            assert key in dict2, "{} not in{}".format(key, dict2)
            cmp_dict(dict1[key], dict2[key])
    elif isinstance(dict1, list):
        for dict1_list, dict2_list in zip(dict1, dict2):
            cmp_dict(dict1_list, dict2_list)
    else:
        assert dict1 == dict2, "value: '{}' != '{}'".format(dict1, dict2)


# 请求返回接口信息
def request(self):
    # 获取接口信息
    url = self.url
    method = self.method
    data = self.data
    name = self.name
    # 判断环境
    if 'api' not in self._testMethodName:
        cookies = Common.generate_cookies(self.user)
        domain = domain_web
    else:
        data['uid'] = self.user
        cookies = {}
        domain = domain_api

    self.resquest_url = domain + url + '?' + parse.urlencode(data)

    logging.info('请求数据:{}\n{}'.format(data, self.resquest_url))

    # 判断请求方式
    headers = {'X-Requested-With': 'XMLHttpRequest'}
    if method == 'get':
        res = requests.get(domain + url, params=data, cookies=cookies, headers=headers)
    elif method == 'post':
        res = requests.post(domain + url, data=data, cookies=cookies, headers=headers)
    else:
        logging.error('请求方式BUG')
    try:
        real_res = res.json()
    except Exception:
        try:
            real_res = json.loads(res.text[1:-1])
        except Exception:
            real_res = res.text
    # logging.debug('数据准备{}'.format(real_res))
    return [real_res, url, method, name, str(data)]


# 首次验证并生成测试报告数据
def assert_res(self):
    exp_res = self.exp_res
    report_data['test_sum'] += 1
    # 实际结果判断方式
    res = request(self)
    real_res = res[0]
    # logging.debug('预期:{}\t实际:{}\t数据:{}'.format(exp_res, real_res, res[4]))
    # 判断请求结果是否包含预期结果
    try:
        cmp_dict(exp_res, real_res)
        report_data['test_success'] += 1
        result = True
        bz = ''
        logging.info('{}验证成功'.format(self._testMethodName))
    except Exception as e:
        result = False
        bz = str(e)
        report_data['test_failed'] += 1
        self.info = '用例{},失败:{}\n\n预期:{}\n\n实际:{}\n\n实际json:{}'.format(self._testMethodDoc, e, exp_res, real_res, json.dumps(real_res))
        # logging.error(self.info)
        self.assertTrue(False, self.info)
    if result and hasattr(self, 'ver'):
        if self.ver():
            logging.info('二次验证成功')
        else:
            result = '二次验证失败'
            logging.error('二次验证失败')
            self.assertTrue(False, '二次验证失败')
    # 把结果添加到报告list中
    res = {"case_id": self._testMethodName,
           "case_des": self._testMethodDoc,
           "name": res[3],
           "method": res[2],
           "url": res[1],
           "user": self.user,
           "data": res[4],
           "exp_res": str(exp_res),
           "real_res": str(real_res),
           "result": result,
           "bz": bz}
    report_data['report_res'].append(res)
    return real_res


# 如何执行测试用例
def exec_case(datas, run_type={}):
    case = []
    if isinstance(datas, dict):
        if run_type == {}:
            for key, value in datas.items():
                case.extend(value)
        else:
            # 遍历两个dict
            for key1, value1 in datas.items():
                for key2, value2 in run_type.items():
                    # 当key相同，根据val2来取val1的值,val2为空取全部，否则取对应的
                    if key1 == key2:
                        if value2 == []:
                            case.extend(value1)
                        else:
                            for i in value2:
                                case.append(value1[i])
        return case
    else:
        return False


def generate_report():
    # 新建excel
    workbook = xlsxwriter.Workbook('report.xlsx')
    # 新建两个sheet
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")

    # 设置列行的宽高
    worksheet.set_column("A:A", 15)
    worksheet.set_column("B:E", 20)

    for i in range(1, 6):
        worksheet.set_row(i, 30)

    define_format_H1 = workbook.add_format({'bold': True,
                                            'font_size': 18,
                                            'border': 1,
                                            'align': "center"})
    define_format_H2 = workbook.add_format({'bold': True,
                                            'font_size': 14,
                                            'border': 1,
                                            'align': "center",
                                            'bg_color': "blue",
                                            'color': "#ffffff"})
    format_center = workbook.add_format({'align': 'center',
                                         'valign': 'vcenter',
                                         'border': 1})
    format_center2 = workbook.add_format({
        'bold': True,
        'font_size': 18,
        'align': 'center',
        'valign': 'vcenter',
        'bg_color': 'blue',
        'font_color': '#ffffff'
    })
    # Create a new Chart object.
    worksheet.merge_range('A1:E1', '测试报告总概况', define_format_H1)
    worksheet.merge_range('A2:E2', '测试概括', define_format_H2)
    data = {
        'A3': '项目名称', 'A4': '接口版本', 'A5': '脚本语言', 'A6': '测试网络',
        'B3': '接口测试', 'B4': 'v1.0', 'B5': 'WEB', 'B6': 'wifi',
        'C3': '接口总数', 'C4': '通过总数', 'C5': '失败总数', 'C6': '测试日期',
        'D3': report_data['test_sum'], 'D4': report_data['test_success'], 'D5': report_data['test_failed'],
        'D6': report_data['test_date'],
        'E3': '分数'
    }
    for key, value in data.items():
        worksheet.write(key, value, format_center)
    worksheet.merge_range('E4:E6', '60', format_center)
    # 图表
    chart = workbook.add_chart({'type': 'pie'})
    chart.add_series({
        'name': '接口测试统计',  # ['Sheet1', 0, 2]
        'categories': [worksheet.name, 3, 2, 4, 2],  # 选项说明（行列） [worksheet.name, 3, 2, 4, 2] '=测试总况!$C$4:$C$5'
        'values': [worksheet.name, 3, 3, 4, 3],  # 选项值 [worksheet.name, 3, 3, 4, 3]'=测试总况!$D$4:$D$5'
    })
    # chart.set_title({'name': '接口测试统计333'})
    chart.set_style(10)
    worksheet.insert_chart('A9', chart, {'x_offset': 25, 'y_offset': 10})
    # sheet2设置
    # 设置列行的宽高
    worksheet2.set_column("A:B", 16)
    worksheet2.set_column("C:F", 8)
    worksheet2.set_column("G:I", 48)
    worksheet2.set_column("J:K", 16)

    # for i in range(1, 8):
    #     worksheet.set_row(i, 30)

    worksheet2.merge_range('A1:K1', '测试详情', format_center2)
    data2 = {
        'A2': '用例ID', 'B2': '用例描述', 'C2': '接口名称', 'D2': '请求方式', 'E2': 'URL', 'F2': '登录用户UID', 'G2': '参数', 'H2': '预期值', 'I2': '实际值',
        'J2': '测试结果', 'K2': '备注'
    }
    for key, value in data2.items():
        worksheet2.write(key, value, format_center)
    report_data['report_res'].sort(key=lambda k: (k.get('case_id', 0)))
    for item in report_data['report_res']:
        excel1 = {'A': item["case_id"], 'B': item["case_des"], 'C': item["name"], 'D': item["method"],
                  'E': item["url"], 'F': item["user"],
                  'G': item["data"], 'H': item["exp_res"], 'I': item["real_res"], 'J': item["result"],
                  'K': item['bz']}
        for key, value in excel1.items():
            worksheet2.write(key + str(report_data['report_res'].index(item) + 3), value)
    workbook.close()


def run_case(pattern='*.py'):
    test_dir = './testcase'
    filename = './result/{}result.html'.format(int(time.time()))
    fp = open(filename, "wb")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern=pattern)
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp)
    # 运行测试用例
    runner.run(discover)
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


def name_func_new(func, num, p):
    base_name = func.__name__
    # base_name
    name_suffix = "_%s" % (num + 1,)
    # name_suffix = ''
    # if len(p.args) > 0 and isinstance(p.args[0], str):
    #     name_suffix += "_" + parameterized.to_safe_name(p.args[0])
    return base_name + name_suffix
    # print(base_name)
    # return base_name

# # 从excel获取测试数据openpyxl 起始位置1, 1
# def get_data(case_file):
#     try:
#         # 打开excel到内存
#         wb = load_workbook(case_file)
#     except Exception as e:
#         logging.error('打开excel错误:{}'.format(e))
#         return False
#     datadict = {}
#     for sheet in wb.worksheets:
#         try:
#             # 获取接口参数
#             interface_data = json.loads(sheet.cell(row=1, column=2).value)
#             name = interface_data['name']
#             url = interface_data['url']
#             method = interface_data['method']
#             num = int(interface_data['num'])
#             logging.debug('接口参数{}'.format(interface_data))
#         except Exception as e:
#             logging.error('接口参数读取错误:{}'.format(e))
#             return False
#         # 请求数据
#         datas = []
#         # 从第三行开始循环读取excel行
#         for row in range(3, sheet.max_row + 1):
#             if sheet.cell(row=row, column=3).value == 'Y':
#                 # 用例ID 第1列
#                 caseid = sheet.cell(row=row, column=1).value
#                 # 描述
#                 casedes = sheet.cell(row=row, column=2).value
#                 # 用户 第4列
#                 user = sheet.cell(row=row, column=4).value
#                 # 预期结果 第num+5列
#                 try:
#                     exp_res = json.loads(sheet.cell(row=row, column=num + 5).value)
#                 except Exception as e:
#                     logging.error('预期结果读取错误:行数{}'.format(row))
#                     return False
#                 # 请求数据
#                 data = {}
#                 for i in range(num):
#                     # 第二行参数：第i行。第五个列数开始循环
#                     data[sheet.cell(row=2, column=5 + i).value] = sheet.cell(row=row, column=5 + i).value if sheet.cell(row=row, column=5 + i).value else ''
#                 datas.append((caseid, casedes, name, url, method, user, data, exp_res))
#         logging.debug('{}用例数据:{}'.format(sheet.title, json.dumps(datas)))
#         datadict[sheet.title] = datas
#     logging.debug('全部用例数据:{}'.format(json.dumps(datadict)))
#     return datadict
