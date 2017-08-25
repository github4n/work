from selenium import webdriver
import unittest
import time
import sys
sys.path.append('..')
from common import CookieLogin, zc, addxd, bdsj, addmoney, url, roomid


class task(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(url + '/' + roomid)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_task001(self):
        # 送豆功能
        yh = zc('test' + str(int(time.time())))
        driver = self.driver
        CookieLogin(yh, driver)
        time.sleep(1)
        # 仙豆不足，点击送豆
        driver.find_element_by_id('sendxd').click()
        time.sleep(1)
        if driver.find_element_by_xpath('//*[@class="tlayer-bx"]/div[2]').text != '您剩余的仙豆数量不足！':
            self.verificationErrors.append("送豆错误1")
        driver.find_element_by_class_name('close').click()
        addxd(yh, 100)
        driver.refresh()
        time.sleep(1)
        driver.find_element_by_id('sendxd').click()
        time.sleep(1)
        if driver.find_element_by_class_name('xiandou-num').text != '90':
            self.verificationErrors.append("送豆错误2")
        time.sleep(1)

    def test_task002(self):
        # 礼物
        yhm = 'test' + str(int(time.time()))
        yh = zc(yhm)
        driver = self.driver
        CookieLogin(yh, driver)
        time.sleep(1)
        # 未绑定，余额不足
        driver.find_element_by_id('axxd').click()
        driver.find_element_by_class_name('close').click()
        time.sleep(1)
        driver.find_element_by_id('gift3').click()
        time.sleep(1)
        driver.find_element_by_class_name('close').click()
        # 已绑定，余额不足
        bdsj(yh)
        driver.refresh()
        time.sleep(1)
        driver.find_element_by_id('gift3').click()
        time.sleep(5)
        if driver.find_element_by_xpath('//*[@id="zfb-paybox"]/div[1]/span[1]/em').text != yhm:
            self.verificationErrors.append("礼物错误1")
        text1 = driver.find_element_by_xpath('//*[@id="zfb-paybox"]/div[1]/span[3]/em').text
        text2 = driver.find_element_by_xpath('//*[@id="zfb-paybox"]/div[1]/span[4]/em').text
        if text1 != '1' or text2 != '1':
            self.verificationErrors.append("礼物错误2")
        driver.find_element_by_id('wx-nav').click()
        time.sleep(5)
        if driver.find_element_by_xpath('//*[@id="wx-paybox"]/div[1]/span[1]/em').text != yhm:
            self.verificationErrors.append("礼物错误3")
        text1 = driver.find_element_by_xpath('//*[@id="wx-paybox"]/div[1]/span[3]/em').text
        text2 = driver.find_element_by_xpath('//*[@id="wx-paybox"]/div[1]/span[4]/em').text
        if text1 != '1' or text2 != '1':
            self.verificationErrors.append("礼物错误4")
        # time.sleep(200000)
        # 已绑定，余额足
        addxd(yh, 10000)
        addmoney(yh, 1000, 1000)
        driver.refresh()
        time.sleep(1)
        driver.find_element_by_id('gift4').click()
        time.sleep(0.5)
        try:
            driver.find_element_by_xpath('//*[@class="gift-scroll-div"]/div[1]')
        except:
            self.verificationErrors.append("礼物错误5")
        if driver.find_element_by_class_name('catcoin-num') != '990.1' or driver.find_element_by_class_name('catbean-num') != '1000':
            self.verificationErrors.append("礼物错误6")

    # 清理结果
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


suite = unittest.TestSuite()
suite.addTest(task("test_task001"))
unittest.main(defaultTest='suite')
