from selenium import webdriver
import unittest
import time
import requests
import sys
sys.path.append('..')
from common import url, CookieLogin, userpwd, zc


class user(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = url
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.username = 'test' + str(int(time.time()))
        self.yh = zc(self.username)

    def test_user001(self):
        # 基本信息
        driver = self.driver
        username = self.username
        CookieLogin(self.yh, driver)
        driver.get(self.url + '/member/showMemberInfo')
        time.sleep(2)
        # 昵称和用户名
        nickname1 = driver.find_element_by_xpath('//*[@class="userinfo"]/dl[1]/dd/span').text
        username1 = driver.find_element_by_xpath('//*[@class="userinfo"]/dl[2]/dd').text
        leftnickname1 = driver.find_element_by_class_name('leftmenu-nickname').text
        if nickname1 != username or username1 != username or leftnickname1 != username:
            self.verificationErrors.append("昵称显示错误|用户名显示错误1")
        # 修改昵称
        driver.find_element_by_id('member-changenickname').click()
        usernameupdate = 'test' + str(int(time.time()))
        driver.find_element_by_name('nick_name').clear()
        driver.find_element_by_name('nick_name').send_keys(usernameupdate)
        driver.find_element_by_id('send-nickname').click()
        time.sleep(2)
        # 第一次修改完以后判断昵称
        nickname2 = driver.find_element_by_xpath('//*[@class="userinfo"]/dl[1]/dd/span').text
        username2 = driver.find_element_by_xpath('//*[@class="userinfo"]/dl[2]/dd').text
        leftnickname2 = driver.find_element_by_class_name('leftmenu-nickname').text
        if nickname2 != usernameupdate or username2 != username or leftnickname2 != usernameupdate:
            self.verificationErrors.append("昵称显示错误|用户名显示错误2")
        # 第二次修改昵称判断
        driver.find_element_by_id('member-changenickname').click()
        usernameupdate2 = 'test' + str(int(time.time()))
        driver.find_element_by_name('nick_name').clear()
        driver.find_element_by_name('nick_name').send_keys(usernameupdate2)
        driver.find_element_by_id('send-nickname').click()
        time.sleep(2)
        nick_name_error = driver.find_element_by_xpath('//*[@id="nick_name-error"]/span').text
        if nick_name_error != '昵称7天以内只能修改一次哦！':
            self.verificationErrors.append("昵称修改限制错误")
        driver.find_element_by_class_name('close').click()

    def test_user002(self):
        # 修改密码
        driver = self.driver
        CookieLogin(self.yh, driver)
        userpwd2 = userpwd + 't'
        driver.get(self.url + '/member/showMemberInfo')
        driver.find_element_by_id('member-changepwd').click()
        driver.find_element_by_name('old_pwd').send_keys(userpwd)
        driver.find_element_by_name('user_pwd').send_keys(userpwd2)
        driver.find_element_by_name('confirm_pwd').send_keys(userpwd2)
        driver.find_element_by_id('change-password').click()
        time.sleep(1)
        alert = driver.switch_to_alert()
        if alert.text != '修改密码成功，请重新登录！':
            self.verificationErrors.append("alert错误")
        alert.accept()
        # 无法验证密码正确性

    def test_user003(self):
        # 绑定邮箱、手机
        driver = self.driver
        CookieLogin(self.yh, driver)
        driver.get(self.url + '/member/showMemberInfo')
        link1 = driver.find_element_by_xpath('//*[@class="email"]/a').get_attribute('href')
        link2 = driver.find_element_by_xpath('//*[@class="phone"]/a').get_attribute('href')
        if link1 != self.url + '/member/showUpdateEmail' and link2 != self.url + '/member/showUpdateMobile':
            self.verificationErrors.append('绑定邮箱手机url错误')

    # def test_user004(self):
    #     # 充值
    #     driver = self.driver
    #     CookieLogin(self.yh, driver)
    #     driver.get(self.url + '/member/showMemberInfo')
    #     # 充值，默认选择10，支付宝
    #     driver.find_element_by_id('pay-md').click()
    #     if driver.find_element_by_xpath('//*[@id="choice-money"]/a[1]').get_attribute('class') != 'active':
    #         self.verificationErrors.append("选择错误1")
    #     if driver.find_element_by_id('alipay').get_attribute('class') != 'active':
    #         self.verificationErrors.append("选择错误2")
    #     driver.find_element_by_id('pay-now').click()
    #     driver.switch_to_window(driver.window_handles[1])
    #     if driver.find_element_by_xpath('//*[@id="J_qrPayArea"]/div[1]/div[2]').text != '10.00':
    #         self.verificationErrors.append("充值错误1")
    #     driver.switch_to_window(driver.window_handles[0])
    #     driver.find_element_by_id('pay-md').click()
    #     driver.find_element_by_id('weixin').click()
    #     driver.find_element_by_id('pay-now').click()
    #     driver.switch_to_window(driver.window_handles[2])
    #     if driver.find_element_by_xpath('//*[@class="pay-topbox"]/em').text != '10.00元':
    #         self.verificationErrors.append("充值错误2")

    # 清理结果
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


# suite = unittest.TestSuite()
# suite.addTest(user("test_user001"))
# unittest.main(defaultTest='suite')
