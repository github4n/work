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

