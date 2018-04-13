from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
import requests
import sys
sys.path.append('..')
from public.common import CookieLogin, zc, szxd, bdsj, szmoney, url, roomid, userpwd, bdsj, bdyx
# , configs


class task(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(url + '/' + roomid)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_task001(self):
        # 订阅任务
        yh = zc('test' + str(int(time.time())))
        driver = self.driver
        CookieLogin(yh, driver)
        # 默认完成任务
        if driver.find_element_by_xpath('//*[@id="mission"]/em').text != '1':
            self.verificationErrors.append("默认完成任务错误")
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        # 点击订阅
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[6]/a').click()
        try:
            driver.find_element_by_xpath('//*[@id="subscribe-tcbox"]/img')
        except:
            self.verificationErrors.append("订阅任务错误1")
        driver.find_element_by_id('mission').click()
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        if driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[6]/span').text != '(0/2)':
            self.verificationErrors.append("订阅任务错误2")
        # 订阅任务完成1
        driver.find_element_by_id('subscribe').click()
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        if driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[6]/span').text != '(1/2)':
            self.verificationErrors.append("订阅任务错误3")
        # 订阅任务完成2
        driver.find_element_by_id('has-subscribe').click()
        driver.find_element_by_id('subscribe').click()
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        if driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[6]/span').text != '(2/2)':
            self.verificationErrors.append("订阅任务错误4")
        # 领取仙豆
        if driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[6]/a').text != '领取':
            self.verificationErrors.append("订阅任务错误5")
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[6]/a').click()
        if driver.find_element_by_xpath('//*[@class="tlayer-bx"]/div[2]').text != '绑定手机或邮箱后就能领取仙豆哦~':
            self.verificationErrors.append("订阅任务错误6")
        href = driver.find_element_by_xpath('//*[@class="other-close"]/a').get_attribute('href')
        target = driver.find_element_by_xpath('//*[@class="other-close"]/a').get_attribute('target')
        text = driver.find_element_by_xpath('//*[@class="other-close"]/a').text
        if href != url + '/member/showMemberInfo' or target != '_blank' or text != '去绑定':
            self.verificationErrors.append("订阅任务错误7")
        driver.find_element_by_class_name('close').click()
        # 领仙豆绑定手机
        bdsj(yh)
        driver.refresh()
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[6]/a').click()
        time.sleep(1)
        if driver.find_element_by_class_name('xiandou-num').text != '20':
            self.verificationErrors.append("订阅任务错误8")
        driver.find_element_by_class_name('confirm-button').click()

    def test_task002(self):
        # 注册任务
        yh = zc('test' + str(int(time.time())))
        driver = self.driver
        CookieLogin(yh, driver)
        # 默认完成注册任务
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        if driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[1]/span').text != '(1/1)':
            self.verificationErrors.append("注册任务错误1")
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[1]/a').click()
        if driver.find_element_by_xpath('//*[@class="tlayer-bx"]/div[2]').text != '绑定手机或邮箱后就能领取仙豆哦~':
            self.verificationErrors.append("注册任务错误2")
        driver.find_element_by_class_name('close').click()
        bdsj(yh)
        driver.refresh()
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[1]/a').click()
        time.sleep(1)
        if driver.find_element_by_class_name('xiandou-num').text != '200':
            self.verificationErrors.append("注册任务错误3")
        driver.find_element_by_class_name('confirm-button').click()
        time.sleep(1)

    def test_task003(self):
        # 发言任务
        yh = zc('test' + str(int(time.time())))
        driver = self.driver
        CookieLogin(yh, driver)
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[4]/a').click()
        time.sleep(1)
        driver.find_element_by_id('chat-tc-close').click()
        for i in range(1, 4):
            driver.find_element_by_id('replay').send_keys('666')
            time.sleep(1)
            driver.find_element_by_id('Countdown').click()
            time.sleep(1)
            driver.find_element_by_id('mission').click()
            time.sleep(3)
            if driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[4]/span').text != '(%s/3)' % i:
                self.verificationErrors.append("发言任务错误%s" % i)
        if driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[4]/a').text != '领取':
            self.verificationErrors.append("发言任务错误4")
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[4]/a').click()
        time.sleep(1)
        driver.find_element_by_class_name('close').click()
        bdsj(yh)
        driver.refresh()
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[4]/a').click()
        time.sleep(1)
        if driver.find_element_by_class_name('xiandou-num').text != '20':
            self.verificationErrors.append("发言任务错误5")
        driver.find_element_by_class_name('confirm-button').click()
        time.sleep(1)

    def test_task004(self):
        # 送豆任务
        yh = zc('test' + str(int(time.time())))
        szxd(yh, 100)
        driver = self.driver
        CookieLogin(yh, driver)
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[5]/a').click()
        time.sleep(1)
        driver.find_element_by_id('sendxd-tcbox').click()
        for i in range(1, 3):
            driver.find_element_by_id('sendxd').click()
            time.sleep(1)
            driver.find_element_by_id('mission').click()
            time.sleep(3)
            if driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[5]/span').text != '(%s/2)' % i:
                self.verificationErrors.append("送豆任务错误%s" % i)
        if driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[5]/a').text != '领取':
            self.verificationErrors.append("送豆任务错误3")
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[5]/a').click()
        time.sleep(1)
        driver.find_element_by_class_name('close').click()
        bdyx(yh)
        driver.refresh()
        driver.find_element_by_id('mission').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="mission-box"]/ul/li[5]/a').click()
        time.sleep(2)
        if driver.find_element_by_class_name('xiandou-num').text != '100':
            self.verificationErrors.append("送豆任务错误4")
        driver.find_element_by_class_name('confirm-button').click()
        time.sleep(1)

    def test_task005(self):
        # 签到
        yh = zc('test' + str(int(time.time())))
        driver = self.driver
        CookieLogin(yh, driver)
        time.sleep(1)
        if driver.find_element_by_xpath('//*[@id="signin"]/p').text != '签到':
            self.verificationErrors.append("签到错误1")
        driver.find_element_by_id('signin').click()
        time.sleep(1)
        driver.find_element_by_class_name('close').click()
        bdsj(yh)
        driver.refresh()
        time.sleep(1)
        driver.find_element_by_id('signin').click()
        day = time.localtime(time.time()).tm_mday
        if driver.find_element_by_xpath('//*[@class="signmon-righttop-box"]/div[%s]' % (day + 11)).get_attribute('class') != 'rili2 active last':
            self.verificationErrors.append("签到错误4")
        if driver.find_element_by_xpath('//*[@id="signin"]/p').text != '已签到':
            self.verificationErrors.append("签到错误2")
        if driver.find_element_by_class_name('xiandou-num').text != '10':
            self.verificationErrors.append("签到错误3")

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


suite = unittest.TestSuite()
suite.addTest(task("test_task100"))
unittest.main(defaultTest='suite')
