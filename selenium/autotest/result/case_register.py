# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import xlrd
import unittest
import time
import pymysql
from pf import *


class register(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        # 数据准备
        self.url = "http://qf.huomaotv.com.cn"
        self.yzm = 'lxy1'
        self.pwd = 'test123456'
        self.file = 'E:\selenium\\autotest\\testcase\data\case_data.xlsx'

    def test_register001(self):
        '登录-用例001(初始化)'
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_link_text('注册').click()
        # 返回placeholder

        def aaa(self):
            try:
                p1 = self.find_element_by_id(
                    'email_login').get_attribute('placeholder')
            except:
                p1 = ''
            try:
                p2 = self.find_element_by_id(
                    'pwd_login').get_attribute('placeholder')
            except:
                p2 = ''
            try:
                p3 = self.find_element_by_id(
                    'pwd_login2').get_attribute('placeholder')
            except:
                p3 = ''
            try:
                p4 = self.find_element_by_id(
                    'vcode_login').get_attribute('placeholder')
            except:
                p4 = ''
            try:
                p5 = self.find_element_by_id(
                    'mobile_login').get_attribute('placeholder')
            except:
                p5 = ''
            return(p1 + p2 + p3 + p4 + p5)
        time.sleep(1)
        # 界面初始化-手机注册
        if aaa(driver) != '请输入11位大陆手机号码密码确认密码请输入验证码请输入验证码':
            self.verificationErrors.insert(0, "界面初始化placeholder错误")
        driver.find_element_by_class_name('user').click()
        time.sleep(1)
        if aaa(driver) != '请输入用户名密码确认密码请输入验证码':
            self.verificationErrors.insert(0, "界面初始化placeholder错误")
        driver.find_element_by_class_name('mail').click()
        time.sleep(1)
        if aaa(driver) != '请输入邮箱密码确认密码请输入验证码':
            self.verificationErrors.insert(0, "界面初始化placeholder错误")

    def test_register002(self):
        '登录-用例002(用户名异常注册)'
        driver = self.driver
        driver.get(self.url)
        # 打开excel读取数据
        data = xlrd.open_workbook(self.file)
        # 获取工作表（通过名称）
        table = data.sheet_by_name('register1')
        for i in range(table.nrows - 1):
            reglogin(driver, 'user', table.cell(i + 1, 0).value,
                     table.cell(i + 1, 1).value, table.cell(i + 1, 2).value,
                     table.cell(i + 1, 3).value)

            # 判断提示
            if divtc(driver) != table.cell(i + 1, 4).value:
                self.verificationErrors.insert(
                    0, divtc(driver) + "错误:数据行号" + str(i + 2))
            time.sleep(1)
            driver.refresh()

    def test_register003(self):
        '注册-用例003(用户名正常注册)'
        driver = self.driver
        driver.get(self.url)
        name = 'test' + str((int(time.time())))
        reglogin(driver, 'user', name, self.pwd, self.pwd, self.yzm)
        # 判断登录
        if not existE(driver, 'xpath',
                      '//*[@id="user_info"]/ul/li[1]/a'):
            self.verificationErrors.insert(0, "用户名注册失败")

    def test_register004(self):
        '注册-用例004(邮箱异常注册)'
        driver = self.driver
        driver.get(self.url)
        # 打开excel读取数据
        datafile = 'E:\selenium\\autotest\\testcase\data\case_data.xlsx'
        data = xlrd.open_workbook(datafile)
        # 获取工作表（通过名称）
        table = data.sheet_by_name('register2')
        for i in range(table.nrows - 1):
            reglogin(driver, 'mail', table.cell(i + 1, 0).value,
                     table.cell(i + 1, 1).value, table.cell(i + 1, 2).value,
                     table.cell(i + 1, 3).value)
            # 判断提示
            if divtc(driver) != table.cell(i + 1, 4).value:
                self.verificationErrors.insert(
                    0, divtc(driver) + "错误:数据行号" + str(i + 2))
            time.sleep(1)
            driver.refresh()

    def test_register005(self):
        '登录-用例005(邮箱正常注册)'
        email_lists = ['@sina.com', '@163.com', '@qq.com',
                       '@126.com', '@vip.sina.com', '@sina.cn',
                       '@hotmail.com', '@gmail.com', '@sohu.com',
                       '@139.com', '@wo.com.cn', '@189.cn', '@21cn.com']
        emailn = str((int(time.time())))
        email_list1 = []
        for email_list in email_lists:
            email_list1.append(emailn + email_list)
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_link_text('注册').click()
        time.sleep(1)
        driver.find_element_by_class_name('mail').click()
        time.sleep(1)
        driver.find_element_by_id('email_login').send_keys(emailn + '@')
        email_list2 = []
        for i in range(0, 13):
            a = driver.find_element_by_xpath(
                '//*[@id="intelligent-regName"]/li[' + str(i + 1) + ']').text
            email_list2.append(a)
        if email_list1 != email_list2:
            self.verificationErrors.insert(0, 'emaillist错误')
        time.sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="intelligent-regName"]/li[1]').click()
        time.sleep(1)
        driver.find_element_by_id('pwd_login').send_keys(self.pwd)
        time.sleep(1)
        driver.find_element_by_id('pwd_login2').send_keys(self.pwd)
        time.sleep(1)
        driver.find_element_by_id('vcode_login').send_keys(self.yzm)
        time.sleep(1)
        driver.find_element_by_id('reg_login').click()
        time.sleep(2)
        # 判断邮箱注册跳转
        if not existE(driver, 'link_text', '登录') or \
           not existE(driver, 'xpath', '/html/body/div[4]/div[2]/a'):
            self.verificationErrors.insert(0, "邮箱注册失败1")
        testemail = emailn + '@sina.com'
        if driver.find_element_by_class_name('success-mail').text != \
                '我们已经向您的邮箱' + testemail + '发送了一封激活邮件，' +\
                '请点击邮件中的链接完成注册！注册成功后，您就可以享受高清赛事直播服务啦！\n立即进入邮箱':
            self.verificationErrors.insert(0, "邮箱注册失败2")
        # 验证邮箱
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='180.150.179.136', user='qa',
                               passwd='fgd@gG513$FD1',
                               db='marstv_www', port=4040, charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        cur.execute(
            "SELECT uid FROM ms_ucenter_members WHERE email = %s", (testemail))
        data = cur.fetchone()
        uid = data[0]
        cur.execute(
            "UPDATE mtv_user SET email_is_check = 1 WHERE uid LIKE %s", uid)
        conn.commit()  # 提交
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        # 邮箱登录
        driver.refresh()
        time.sleep(1)
        login(driver, testemail, self.pwd, self.yzm)
        time.sleep(1)
        # 判断提示
        if not existE(driver, 'xpath',
                      '//*[@id="user_info"]/ul/li[1]/a'):
            self.verificationErrors.insert(0, "正常登录失败")

    # 异常弹框处理
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True

    # 关闭警告以及对得到文本框的处理
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    # 清理结果
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
