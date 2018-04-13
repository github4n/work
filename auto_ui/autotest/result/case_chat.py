# -*- coding:utf-8 -*-
# 聊天室
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
import sys
sys.path.append("..")
from public.pf import existE, cleardy, login, cookieLogin, dyfj, zbzt


class chat(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.url = 'http://qf.huomaotv.com.cn'
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        # 用户信息
        self.roomid = 4133

    def test_chat001(self):
        '未登录用户'
        driver = self.driver
        driver.get(self.url + '/live/' + str(self.roomid))
        driver.maximize_window()
        time.sleep(1)
        # 聊天框显示
        a = driver.find_element_by_class_name('phone-tips').text
        if a != '登录后即可发言，立即登录':
            self.verificationErrors.insert(0, "错误")
        try:
            driver.find_element_by_link_text('立即登录').click()
            time.sleep(1)
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.insert(0, "错误")

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
