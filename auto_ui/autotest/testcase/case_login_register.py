from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
import sys

sys.path.append('..')
from common.common import Common
from common.selenium import URL


class login_register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = URL + 'channel/all'
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.username = 'test' + str(int(time.time()))
        # self.uid = Common.register()

    def test_login_register001(self):
        # 注册-用户名注册
        driver = self.driver
        driver.find_element(By.ID, 'register-btn').click()
        driver.find_element(By.ID, 'met-username').click()
        driver.find_element(By.NAME, 'username').send_keys(self.username)
        driver.find_element(By.NAME, 'nick_name').send_keys(self.username)
        driver.find_element(By.ID, 'user_pwd_jia').click()
        driver.find_element(By.NAME, 'user_pwd').send_keys('test1234')
        driver.find_element(By.ID, 'confirm_pwd_jia').click()
        driver.find_element(By.NAME, 'confirm_pwd').send_keys('test1234')
        driver.find_element(By.ID, 'register-post').click()
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'leftmenu-nickname'), self.username), '没注册成功')

    def test_login_register002(self):
        # 登录
        Common.register(self.username)
        driver = self.driver
        driver.find_element(By.ID, 'login-btn').click()
        driver.find_element(By.NAME, 'username').send_keys(self.username)
        driver.find_element(By.ID, 'user_pwd_jia').click()
        driver.find_element(By.NAME, 'user_pwd').send_keys('1')
        driver.find_element(By.ID, 'login-post').click()
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'leftmenu-nickname'), self.username), '没登陆')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(login_register("test_login_register002"))
    unittest.main(defaultTest='suite')
    # unittest.main()
