# -*- coding:utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
import sys
sys.path.append("..")
from public import pf
# import HTMLTestRunner


class zt(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.url = "http://www.huomaotv.com.cn"
        self.base_url = self.url + "/index.php?c=huodong&a=new_ts4"
        self.home_url = \
            "http://www.huomaotv.com/?from=topbanner?from=topbanner"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    # 未登录用户页面功能检查
    def test_nologin(self):
        u"""未登录用户页面功能检查"""
        driver = self.driver
    # 进入首页
        driver.get(self.base_url)
    # 点击火猫logo
        driver.find_element_by_xpath('//*[@id="header"]/h1/a').click()
        time.sleep(2)
        if driver.current_url != self.home_url:
            self.verificationErrors.insert(0, driver.current_url+"url错误")
        driver.back()
    # 点击首页
        driver.find_element_by_link_text("首页").click()
        time.sleep(2)
        if driver.current_url != self.home_url:
            self.verificationErrors.insert(0, driver.current_url+"url错误")
        driver.back()
    # 点击直播
        time.sleep(1)
        driver.find_element_by_link_text("直播").click()
        time.sleep(1)
        if driver.current_url != self.url + \
                "/channel/all?from=topbanner?from=topbanner":
            self.verificationErrors.insert(0, driver.current_url+"url错误")
        driver.back()
    # 点击游戏
        driver.find_element_by_link_text("游戏").click()
        time.sleep(2)
        if driver.current_url != self.url + \
                "/game?from=topbanner?from=topbanner":
            self.verificationErrors.insert(0, driver.current_url+"url错误")
        driver.back()
    # 点击游戏下拉框
        a = driver.find_element_by_link_text("游戏")
        ActionChains(driver).move_to_element(a).perform()
        time.sleep(3)
        driver.find_element_by_xpath(
            '//*[@id="header"]/ul/li[3]/div/a').click()
        time.sleep(2)
        if driver.current_url != self.url + \
                "/game?from=topbanner?from=topbanner":
            self.verificationErrors.insert(0, driver.current_url+"url错误")
        driver.back()
    # 搜索
        driver.find_element_by_id('search_kw').send_keys(666)
        driver.find_element_by_xpath('//*[@id="search_frm"]/button').click()
    # 页面重新加载后需要等待时间
        time.sleep(2)
        try:
            driver.find_element_by_partial_link_text('推荐').click()
        except:
            self.verificationErrors.insert(0, "搜索结果页面显示错误")
        time.sleep(2)
        driver.get(self.base_url)
    # 提示登录弹框
        arr_links = ['登录', '注册', '申请直播', '任务', '签到', '登陆领仙豆', '立即登录']
        for arr_link in arr_links:
            driver.find_element_by_link_text(arr_link).click()
            time.sleep(1)
            driver.find_element_by_class_name('close').click()
            time.sleep(1)
    # 仙豆选择
        driver.find_element_by_id('xw_zs').click()
        time.sleep(1)
        driver.find_element_by_link_text('10').click()
        time.sleep(1)
        driver.find_element_by_class_name('close').click()
    # 发送
        time.sleep(1)
        driver.find_element_by_id('chat_btn').click()
        time.sleep(1)
        driver.find_element_by_class_name('close').click()
        time.sleep(2)
    # 页面底部链接（暂时无判断）
        arr_footers = ['关于我们', '招贤纳士', '问题反馈', '帮助中心', '在线客服']
        for arr_footer in arr_footers:
            driver.find_element_by_link_text(arr_footer).click()
            time.sleep(2)
            driver.switch_to_window(driver.window_handles[0])

    # 登录用户(未绑定手机或者邮箱)
    def test_loginnoie(self):
        """登录用户页面功能检查"""
        print('666')
        driver = self.driver
        driver.get(self.base_url)
        # 插入cookie登录
        pf.cookie_login(357849, 'a3d2069c05db53d6dde9d526b7697f1e',
                        1447663698, driver)

        driver.find_element_by_class_name('btn_login').click
        self.verificationErrors.insert(0, "xxx错误")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

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
