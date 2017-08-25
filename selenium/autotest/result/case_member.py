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
from public.pf import login, regnamef, config


class member(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        config1 = config()
        self.url = config1.url
        self.messurl = self.url + '/member/mess'
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        # 用户信息
        self.roomid = 4133

    def test_member001(self):
        ''

        driver = self.driver
        driver.get(self.url)
        # driver.maximize_window()
        time.sleep(1)
        regnamef()
        driver.get(self.messurl)

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
