from selenium import webdriver
import unittest
import time
import sys
sys.path.append('..')
from common import url, roomid, CookieLogin, addxd, addmoney, bdsj, zc


class chatroom(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = url
        self.roomid = roomid
        self.driver.get(self.url + '/' + self.roomid)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_chatroom001(self):
        # 通用功能判断，除搜索
        # topbar
        driver = self.driver
        topbar_link1 = driver.find_element_by_class_name("topbar-logo").get_attribute("href")
        if topbar_link1 != self.url + '/':
            self.verificationErrors.append(topbar_link1 + "logo:url错误")
        topbar_link2 = driver.find_element_by_link_text("首页").get_attribute("href")
        if topbar_link2 != self.url + '/':
            self.verificationErrors.append(topbar_link2 + "首页:url错误")
        topbar_link3 = driver.find_element_by_link_text("直播").get_attribute("href")
        if topbar_link3 != self.url + '/channel/all':
            self.verificationErrors.append(topbar_link3 + "直播:url错误")
        topbar_link4 = driver.find_element_by_link_text("分类").get_attribute("href")
        if topbar_link4 != self.url + '/game':
            self.verificationErrors.append(topbar_link4 + "分类:url错误")
        topbar_link5 = driver.find_element_by_class_name("hotgame-bottombox").get_attribute("href")
        # 查看全部
        if topbar_link5 != self.url + '/game':
            self.verificationErrors.append(topbar_link5 + "查看全部:url错误")
        search_kw = driver.find_element_by_id('search_kw').get_attribute('value')
        if search_kw != '搜主播/房间':
            self.verificationErrors.append(search_kw + "搜索提示错误")
        # # 搜索
        # driver.find_element_by_id('search_kw').send_keys('3642')
        # driver.find_element_by_class_name('search-button').click()
        # # 搜索结果判断
        # snum = 0
        # for s in driver.find_elements_by_xpath('//em'):
        #     if s.text == 'dota2测试中9999':
        #         snum = snum + 1
        # if snum == 0:
        #     self.verificationErrors.append(str(snum) + "搜索结果错误")
        # driver.get(self.url + '/' + self.roomid)

        # leftbar
        leftbars = driver.find_element_by_class_name('leftmenu-nav').find_elements_by_tag_name('a')
        if leftbars[0].get_attribute("href") != self.url + '/channel/all':
            self.verificationErrors.append(leftbars[0].get_attribute("href") + "直播:url错误")
            # print(i.get_attribute("href"))
        if leftbars[1].get_attribute("href") != self.url + '/game':
            self.verificationErrors.append(leftbars[1].get_attribute("href") + "分类:url错误")
        # if leftbars[2].get_attribute("href") != self.url + '/subscribe/showUserSubs':
        #     self.verificationErrors.append(leftbars[2].get_attribute("href") + "订阅:url错误")

    def test_chatroom002(self):
        # 未登录状态判断
        driver = self.driver
        # topbar
        # 登录框判断
        try:
            driver.find_element_by_id('login').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("topbar登录框错误")
        # 注册框判断
        try:
            driver.find_element_by_id('register').click()
            time.sleep(1)
            driver.find_element_by_id('register-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("topbar注册框错误")
        # 申请直播判断
        try:
            driver.find_element_by_id('ask-for-live').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("topbar申请直播错误")
        # leftbar判断
        # 登录框判断
        try:
            driver.find_element_by_id('login-btn').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("leftbar登录框错误")
        # 注册框判断
        try:
            driver.find_element_by_id('register-btn').click()
            time.sleep(1)
            driver.find_element_by_id('register-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("leftbar注册框错误")
        # 申请直播判断
        try:
            driver.find_element_by_link_text('申请直播').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("leftbar申请直播错误")
        # 未登录订阅
        try:
            driver.find_element_by_id('leftmenu-l-subscribe').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("leftbar我的订阅错误")
        # 任务
        try:
            driver.find_element_by_id('mission').click()
            driver.find_element_by_id('mission-register').click()
            time.sleep(1)
            driver.find_element_by_id('register-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("任务注册框错误")
        # 签到
        try:
            driver.find_element_by_id('signin').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("签到登录框错误")
        # 领仙豆
        try:
            driver.find_element_by_id('getxd').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("领仙豆登录框错误")
        # 送仙豆
        try:
            driver.find_element_by_id('sendxd').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("送仙豆登录框错误")
        # 送礼物
        try:
            driver.find_element_by_id('gift7').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("送礼物登录框错误")
        # 充值
        try:
            driver.find_element_by_id('pay-md').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("充值登录框错误")
        # 兑换
        try:
            driver.find_element_by_id('change-md').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("兑换登录框错误")
        # 发言
        try:
            driver.find_element_by_id('replay').send_keys('测试')
            driver.find_element_by_id('Countdown').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("发言登录框错误")
        # 举报
        try:
            driver.find_element_by_id('jubao').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("举报登录框错误")
        # 订阅
        try:
            driver.find_element_by_id('subscribe').click()
            time.sleep(1)
            driver.find_element_by_id('login-post')
            driver.find_element_by_class_name('close').click()
        except:
            self.verificationErrors.append("订阅登录框错误")
        time.sleep(2)

    def test_chatroom003(self):
        # 登录用户1
        driver = self.driver
        chatdata1 = '测试'
        username1 = 'test' + str(int(time.time()))
        yh1 = zc(username1)
        bdsj(yh1)
        addxd(yh1, 10000)
        addmoney(yh1, 10000, 10000)
        CookieLogin(yh1, driver)
        # 登录用户2
        driver2 = webdriver.Chrome()
        driver2.get(self.url + '/' + self.roomid)
        driver2.maximize_window()
        username2 = 'test' + str(int(time.time()))
        yh2 = zc(username2)
        CookieLogin(yh2, driver2)
        time.sleep(2)
        # 用户1发言显示
        driver.find_element_by_id('replay').send_keys(chatdata1)
        driver.find_element_by_id('Countdown').click()
        time.sleep(2)
        # 发言自身显示
        chatdata2 = driver.find_element_by_xpath('//*[@id="chat_cont_bx"]/li[2]/p').text
        if chatdata2 != username1 + ' : ' + chatdata1:
            self.verificationErrors.append("发言自身显示错误")
        # 发言其他人显示
        chatdata3 = driver2.find_element_by_xpath('//*[@id="chat_cont_bx"]/li[2]/p').text
        if chatdata3 != username1 + ' : ' + chatdata1:
            self.verificationErrors.append("聊发言其他人显示错误")
        time.sleep(2)
        # 送仙豆
        driver.find_element_by_id('sendxd').click()
        # 送豆自身显示
        chatdata4 = driver.find_element_by_xpath('//*[@id="chat_cont_bx"]/li[3]/p').text
        if chatdata4 != username1 + '：送给主播 X 10':
            self.verificationErrors.append("送豆自身显示错误")
        # 送豆其他人显示
        chatdata5 = driver2.find_element_by_xpath('//*[@id="chat_cont_bx"]/li[3]/p').text
        if chatdata5 != username1 + '：送给主播 X 10':
            self.verificationErrors.append("送豆其他人显示错误")
        # 送礼
        driver.find_element_by_id('gift6').click()
        # 送礼自身显示
        chatdata6 = driver.find_element_by_xpath('//*[@id="chat_cont_bx"]/li[4]/p').text
        chatdata7 = driver.find_element_by_xpath('//*[@class="gift-float pos"]/font[1]').text
        if chatdata6 == username1 + '：送给主播 X 1' and chatdata7 != username1:
            self.verificationErrors.append("送礼自身显示错误")
        # 送礼其他人显示
        chatdata8 = driver2.find_element_by_xpath('//*[@id="chat_cont_bx"]/li[4]/p').text
        chatdata9 = driver.find_element_by_xpath('//*[@class="gift-float pos"]/font[1]').text
        if chatdata8 == username1 + '：送给主播 X 1' and chatdata9 != username1:
            self.verificationErrors.append("送礼其他人显示错误")

    # 清理结果
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


# suite = unittest.TestSuite()
# suite.addTest(chatroom("test_chatroom003"))
# unittest.main()
# defaultTest='suite')
unittest.main()
