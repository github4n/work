# -*- coding:utf-8 -*-
from selenium import webdriver
import xlrd
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import sys
sys.path.append("..")
from public.pf import existE, divtc, login


class login(unittest.TestCase):

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
        self.file = 'E:\selenium\\autotest\\testcase\data\case_data.xlsx'
        self.yzm = 'lxy1'

    def test_login001(self):
        '登录-用例001(初始化)'
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_link_text('登录').click()
        time.sleep(1)
        # 界面初始化
        p1 = driver.find_element_by_id(
            'email_login').get_attribute('placeholder')
        p2 = driver.find_element_by_id(
            'pwd_login').get_attribute('placeholder')
        p3 = driver.find_element_by_id(
            'vcode_login').get_attribute('placeholder')
        if p1 != '用户名/邮箱/手机号' or p2 != '请输入密码' or p3 != '请输入验证码':
            self.verificationErrors.insert(0, "界面初始化placeholder错误")
        # 点击后placeholder消失
        driver.find_element_by_id('email_login').click()
        time.sleep(1)
        p4 = driver.find_element_by_id(
            'email_login').get_attribute('placeholder')
        driver.find_element_by_id('pwd_login').click()
        time.sleep(1)
        p5 = driver.find_element_by_id(
            'pwd_login').get_attribute('placeholder')
        driver.find_element_by_id('vcode_login').click()
        time.sleep(1)
        p6 = driver.find_element_by_id(
            'vcode_login').get_attribute('placeholder')
        if p4 != '' or p5 != '' or p6 != '':
            self.verificationErrors.insert(0, p4 + p5 + p6 + "点击placeholder错误")

        # 第三方登录
        if not existE(driver, 'class_name', 'qq-login') or \
                not existE(driver, 'class_name', 'wanmei-login'):
            self.verificationErrors.insert(0, "第三方登录错误")
        # 快速注册
        driver.find_element_by_link_text('快速注册>>').click()
        if not existE(driver, 'link_text', '立即登录>>'):
            self.verificationErrors.insert(0, "快速注册错误")
        driver.find_element_by_link_text('立即登录>>').click()
        time.sleep(1)
        # 下次自动登录
        if not driver.find_element_by_id('remember_me')\
                .get_attribute('checked'):
            self.verificationErrors.insert(0, "下次自动登陆错误")
        # 忘记密码
        driver.find_element_by_class_name('forgetpwd').click()
        time.sleep(1)
        wjmm = '/html/body/div[6]/div[1]/h2'
        if driver.find_element_by_xpath(wjmm).text != '忘记密码':
            self.verificationErrors.insert(0, "忘记密码错误")

    def test_login002(self):
        '登录-用例002(异常登录)'
        # webdriver不识别display为none的元素
        driver = self.driver
        driver.get(self.url)
        # 打开excel读取数据
        data = xlrd.open_workbook(self.file)
        # 获取工作表（通过名称）
        table = data.sheet_by_name('login1')
        for i in range(table.nrows - 1):
            login(driver, table.cell(i + 1, 0).value,
                   table.cell(i + 1, 1).value, table.cell(i + 1, 2).value)
            # 判断提示
            if divtc(driver) != table.cell(i + 1, 3).value:
                self.verificationErrors.insert(
                    0, divtc(driver) + "错误:数据行号" + str(i + 2))
            time.sleep(1)
            driver.refresh()
        # 其它异常判断
        # 邮箱未验证
        login(driver, 'login001@sina.com', 'login001', self.yzm)
        if not existE(driver, 'xpath', "//div[@class='form-l exp']"):
            self.verificationErrors.insert(0, "邮箱未验证错误")

    def test_login003(self):
        '登录-用例003(正常登录)'
        driver = self.driver
        driver.get(self.url)
        data = xlrd.open_workbook(self.file)
        # 获取工作表（通过名称）
        table = data.sheet_by_name('login2')
        for i in range(table.nrows - 1):
            login(driver, table.cell(i + 1, 0).value,
                   table.cell(i + 1, 1).value, table.cell(i + 1, 2).value)
            time.sleep(1)
            # 判断提示
            if not existE(driver, 'xpath', '//*[@id="user_info"]/ul/li[1]/a'):
                self.verificationErrors.insert(0, "正常登录失败")
            driver.delete_all_cookies()
            driver.refresh()

    # 安全机制无法做
    # def test_login004(self):
        # '登录-用例004(第三方登录)'
        # driver.find_element_by_link_text('登录').click()
        # print(driver.current_window_handle)
        # time.sleep(1)
        # driver.find_element_by_class_name('qq-login').click()
        # time.sleep(1)
        # a = driver.window_handles
        # print(a)
        # driver.switch_to_window(a[1])
        # print(driver.current_window_handle)
        # time.sleep(3)
        # b = driver.find_element_by_class_name('switch_btn_focus').text
        # print(b)
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
