from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
import sys
import configparser
import os

sys.path.append('..')
from huomao.common import Common
from huomao.selenium import URL,CookieLogin


class LoginRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = URL + 'channel/all'
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.username = 'test' + str(int(time.time()))
        # self.uid = Common.register()

    # 注册
    def test_login_register1(self):
        # 获取文件的当前路径（绝对路径）
        cur_path = os.path.dirname(os.path.realpath(__file__))
        # 获取config.ini的路径
        config_path = os.path.join(cur_path, 'config.ini')
        conf = configparser.ConfigParser()
        # 读取配置
        conf.read(config_path)
        mobile = conf.get('config', 'mobile')
        # 设置配置
        conf.set('config', 'mobile', str(int(mobile) + 1))
        # 写入配置
        with open(config_path, 'w') as fw:
            conf.write(fw)
        # 添加验证码
        Common.add_mobile_yzm(mobile)
        driver = self.driver
        driver.find_element(By.ID, 'register-btn').click()
        driver.find_element(By.NAME, 'mobile').send_keys(mobile)
        driver.find_element(By.NAME, 'nick_name').send_keys(self.username)
        driver.find_element(By.ID, 'user_pwd_jia').click()
        driver.find_element(By.NAME, 'user_pwd').send_keys('test1234')
        driver.find_element(By.NAME, 'mobile_code').send_keys('123456')
        driver.find_element(By.ID, 'register-post').click()
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'leftmenu-nickname'), self.username), '没注册成功')

    # 手机验证码登录
    def test_login_register2(self):
        uid = Common.register(self.username)['uid']
        mobile = Common.bd_sj(uid)['mobile']
        Common.add_mobile_yzm(mobile)
        driver = self.driver
        driver.find_element(By.ID, 'login-btn').click()
        driver.find_element(By.NAME, 'mobile').send_keys(mobile)
        driver.find_element(By.NAME, 'mobile_code').send_keys('123456')
        driver.find_element(By.ID, 'login-post').click()
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'leftmenu-nickname'), self.username), '没登陆')

    # # 账号密码登录
    # def test_login_register3(self):
    #     Common.register(self.username)
    #     driver = self.driver
    #     driver.find_element(By.ID, 'login-btn').click()
    #     time.sleep(1)
    #     driver.find_element(By.CLASS_NAME, 'login-tab0').click()
    #     driver.find_element(By.NAME, 'username').send_keys(self.username)
    #     driver.find_element(By.ID, 'user_pwd_jia').click()
    #     driver.find_element(By.NAME, 'user_pwd').send_keys('1')
    #     driver.find_element(By.ID, 'login-post').click()
    #     WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'leftmenu-nickname'), self.username), '没登陆')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginRegister("test_login_register1"))
    unittest.main(defaultTest='suite')
    # unittest.main()
