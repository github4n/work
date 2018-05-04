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
from huomao.selenium import URL, CookieLogin


class ChatRoom(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = URL + '100'
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.username = 'test' + str(int(time.time()))
        # self.uid = Common.register()

    # 发言
    def test_chat_room1(self):
        uid = Common.register(self.username)['uid']
        uid2 = Common.register(self.username + '1')['uid']
        Common.bd_sj(uid)
        Common.set_money(uid, 9999, 9999)
        Common.set_xd(uid, 9999)
        # 登录用户1
        driver = self.driver
        driver.execute_script('window.hmh5.changePlayer.changePlayerType(false);')
        CookieLogin(uid, driver)
        # 登录用户2
        driver2 = webdriver.Chrome()
        driver2.get(self.url)
        driver2.maximize_window()
        driver2.execute_script('window.hmh5.changePlayer.changePlayerType(false);')
        CookieLogin(1522, driver2)
        # 用户1发言显示
        chat_data = self.username
        driver.find_element(By.ID, 'replay').send_keys(chat_data)
        driver.find_element(By.ID, 'Countdown').click()
        time.sleep(2)
        # 发言自身显示
        msgs = []
        for element in driver.find_elements(By.CLASS_NAME, 'msg'):
            text = element.find_element(By.CLASS_NAME, 'message').text
            msgs.append(text)
        self.assertIn(chat_data, msgs, '发言自身显示error')
        # 发言其他人显示
        msgs2 = []
        for element in driver2.find_elements(By.CLASS_NAME, 'msg'):
            text = element.find_element(By.CLASS_NAME, 'message').text
            msgs2.append(text)
        self.assertIn(chat_data, msgs2, '发言其他人显示error')
        time.sleep(2)
        # 送仙豆
        driver.find_element(By.CLASS_NAME, 'sendxd').click()
        # 送豆自身显示
        beans = []
        for element in driver.find_elements(By.CLASS_NAME, 'beans'):
            text = element.find_element(By.CLASS_NAME, 'username').text
            beans.append(text)
        self.assertIn(self.username + 'nc', beans, '送豆自身显示error')
        # 送豆其他人显示
        beans2 = []
        for element in driver.find_elements(By.CLASS_NAME, 'beans'):
            text = element.find_element(By.CLASS_NAME, 'username').text
            beans2.append(text)
        self.assertIn(self.username + 'nc', beans2, '送豆其他人显示error')
        # 送礼
        driver.find_element(By.XPATH, '//*[@id="newgift"]/li[1]').click()
        # 送礼自身显示
        gifts = []
        for element in driver.find_elements(By.CLASS_NAME, 'gift'):
            text = element.find_element(By.CLASS_NAME, 'username').text
            gifts.append(text)
        self.assertIn(self.username + 'nc', gifts, '送礼自身显示error')
        # 送礼其他人显示
        gifts2 = []
        for element in driver.find_elements(By.CLASS_NAME, 'gift'):
            text = element.find_element(By.CLASS_NAME, 'username').text
            gifts2.append(text)
        self.assertIn(self.username + 'nc', gifts2, '送礼其他人显示error')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ChatRoom("test_chat_room1"))
    unittest.main(defaultTest='suite')
    # unittest.main()
