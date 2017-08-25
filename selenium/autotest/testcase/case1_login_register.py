from selenium import webdriver
import unittest
import time
import sys
sys.path.append('..')
from common import url, CookieLogin, zc


class login_register(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = url
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.uid = zc('test' + str(int(time.time())))

    def test_login_register001(self):
        # 未登录用户注册，有极验暂时不做破解
        driver = self.driver
        driver.find_element_by_id('register').click()
        time.sleep(1)
        driver.find_element_by_class_name('mobile').send_keys('15801899659')
        time.sleep(1)
        driver.find_element_by_name('nick_name').send_keys('nick_name')
        time.sleep(1)
        driver.find_element_by_id('user_pwd_jia').click()
        time.sleep(1)
        driver.find_element_by_name('user_pwd').send_keys('user_pwd')
        time.sleep(1)
        driver.find_element_by_id('confirm_pwd_jia').click()
        time.sleep(1)
        driver.find_element_by_name('confirm_pwd').send_keys('confirm_pwd')
        time.sleep(1)
        driver.find_element_by_name('mobile_code').send_keys('666666')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@class="gt_holder float"]')
        driver.find_element_by_id('register-post').click()

    def test_login_register002(self):
        # 未登录用户登录，有极验暂时不做破解
        driver = self.driver
        driver.find_element_by_id('login').click()
        time.sleep(1)
        driver.find_element_by_name('username').send_keys('username')
        time.sleep(1)
        driver.find_element_by_id('user_pwd_jia').click()
        time.sleep(1)
        driver.find_element_by_name('user_pwd').send_keys('user_pwd')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@class="gt_holder float"]')
        driver.find_element_by_id('login-post').click()

    def test_login_register003(self):
        # 退出登录
        driver = self.driver
        CookieLogin(self.uid, driver)
        js = "$('.topbar-userimg ul').css('opacity','1');$('.topbar-userimg ul').css('visibility','visible');"
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_id('logout').click()
        time.sleep(2)
        driver.find_element_by_id('login').click()
        time.sleep(2)

    def test_login_register004(self):
        # QQ登录,线下预发布无法登陆
        if url == 'http://www.huomao.com':
            driver = self.driver
            driver.find_element_by_id('login').click()
            time.sleep(1)
            driver.find_element_by_id('met-qq').click()
            time.sleep(1)
            windows = driver.window_handles
            driver.switch_to_window(windows[1])
            time.sleep(2)
            driver.switch_to_frame('ptlogin_iframe')
            time.sleep(2)
            driver.find_element_by_id('switcher_plogin').click()
            time.sleep(2)
            driver.find_element_by_id('u').send_keys('1991555314')
            time.sleep(1)
            driver.find_element_by_id('p').send_keys('qq445566')
            time.sleep(1)
            driver.find_element_by_id('login_button').click()
            time.sleep(5)
            driver.switch_to_window(windows[0])
        else:
            pass


    # def test_login_register005(self):
    #     # 退出登录
    #     driver = self.driver
    #     CookieLogin('1522', driver)
    #     time.sleep(100000)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


# suite = unittest.TestSuite()
# suite.addTest(login_register("test_login_register003"))
# unittest.main(defaultTest='suite')
# unittest.main()
