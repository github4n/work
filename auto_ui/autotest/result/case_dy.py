# -*- coding:utf-8 -*-
# 订阅
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
import sys
sys.path.append("..")
from public.pf import existE, cleardy, login, cookieLogin, dyfj, zbzt


class dy(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.url = 'http://qf.huomaotv.com.cn/live/4133'
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        # 用户信息
        self.uid = 395417
        self.token = '85f8fdbc9db17992d9f6687d6b519ee3'
        self.ts = 1449645282
        self.lists = [4134, 4135, 4136, 4137, 4138]
        '''
        数据准备：
        test_sub1  395417,e2cc29a7e0751a6f51afb22d4df92772,144964256
        test_sub2
        账号             uid    房间号
        test_sub_zhubo1  395420 4133
        test_sub_zhubo2  395421 4134
        test_sub_zhubo3  395422 4135
        test_sub_zhubo4  395423 4136
        test_sub_zhubo5  395424 4137
        test_sub_zhubo6  395425 4138
        '''

    def test_dy001(self):
        '未登录用户直播间功能检查'
        driver = self.driver
        driver.get(self.url)
        # 未登录无法订阅
        driver.find_element_by_id('subs_btn').click()
        time.sleep(1)
        if existE(driver, 'class_name', 'close'):
            driver.find_element_by_class_name('close').click()
        else:
            self.verificationErrors.insert(0, "订阅错误")

    def test_dy002(self):
        '空订阅及订阅人数'
        cleardy(self.uid)
        # 登录
        driver = self.driver
        driver.get(self.url)
        cookieLogin(self.uid, self.token, self.ts, driver)
        # 空订阅信息判断top
        time.sleep(2)
        dy1 = driver.find_element_by_xpath('//*[@class="hm-user fr"]/li[2]/a')
        ActionChains(driver).move_to_element(dy1).perform()
        time.sleep(2)
        if not existE(driver, 'class_name', 'no-rss'):
            self.verificationErrors.insert(0, "top订阅错误1")
        driver.find_element_by_xpath('//*[@class="more pa"]/a').click()
        time.sleep(1)
        if driver.current_url != \
                'http://qf.huomaotv.com.cn/live_list?from=topbanner':
            self.verificationErrors.insert(0, "top订阅错误2")
        driver.back()
        # 空订阅信息判断left
        dy2 = driver.find_element_by_class_name("icon-mini-rss")
        ActionChains(driver).move_to_element(dy2).perform()
        time.sleep(1)
        if not existE(driver, 'class_name', 'no-rss'):
            self.verificationErrors.insert(0, "left订阅错误1")
        driver.find_element_by_xpath('//*[@id="listrss"]/a').click()
        time.sleep(1)
        if driver.current_url != 'http://qf.huomaotv.com.cn/live_list':
            self.verificationErrors.insert(0, "left订阅错误2")
        driver.back()
        # 订阅人数判断
        a = int(driver.find_element_by_id('subs_bx1').text)
        # 订阅4133房间
        driver.find_element_by_id('subs_btn').click()
        time.sleep(1)
        b = int(driver.find_element_by_id('subs_bx1').text)
        if b != (a + 1):
            self.verificationErrors.insert(0, "订阅数错误1")
        # 取消订阅4133
        driver.find_element_by_id('subs_btn').click()
        c = int(driver.find_element_by_id('subs_bx1').text)
        if c != (b - 1):
            self.verificationErrors.insert(0, "订阅数错误2")

    def test_dy003(self):
        '订阅多房间显示'
        # 订阅5位正在直播
        cleardy(self.uid)
        for list1 in self.lists:
            dyfj(self.uid, list1)
            zbzt(1, list1)
        # 登录
        driver = self.driver
        driver.get(self.url)
        cookieLogin(self.uid, self.token, self.ts, driver)
        driver.get('http://qf.huomaotv.com.cn/member/sub')
        if len(driver.find_elements_by_class_name('VOD')) == 5:
            self.verificationErrors.insert(0, "订阅数错误")


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
