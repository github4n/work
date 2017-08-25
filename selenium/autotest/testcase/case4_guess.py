from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
import time
import requests
import sys
sys.path.append('..')
from common import CookieLogin, cookies, addmoney, addxd

url = 'http://qa.new.huomaotv.com.cn/'
roomid = '1'
cid = '2'
fzuid = '1522'
zzuid = '1412'
xzuid = '1413'
ts = str(int(time.time()))


# 结束所有盘口。num序号0，1，2，choice选项1，2,3封盘,4流局
def js(cid, fzuid, xx1='1', xx2='1', xx3='1'):
    data = {'params[0]': xx1,
            'params[1]': xx2,
            'params[2]': xx3,
            'cid': cid}
    res = requests.get(url + '/Guess/setCloseGuess?', params=data, cookies=cookies(fzuid))
    # print(res.text)
    time.sleep(5)


def kp(cid, fzuid, ts):
    # 开盘前先结束盘口
    js(cid, fzuid)
    data = {'cid': cid,
            'first[title]': '测试主题1' + ts,
            'first[choice_1]': '主题1选项1',
            'first[choice_2]': '主题1选项2',
            'first[type]': '1',
            'second[title]': '测试主题2' + ts,
            'second[choice_1]': '主题2选项1',
            'second[choice_2]': '主题2选项2',
            'second[type]': '1',
            'third[title]': '测试主题3' + ts,
            'third[choice_1]': '主题3选项1',
            'third[choice_2]': '主题3选项2',
            'third[type]': '1'}
    res = requests.get(url + '/guess/setGuessSubject', data, cookies=cookies(fzuid))
    # print(res.json()['data']['1']['xd'], res.json()['data']['2']['xd'], res.json()['data']['3']['xd'])
    # 获取订单号


def zzui(driver, odds, money, xx, moneytype):  # xx 1,2 moneytype 1猫豆 2仙豆
    driver.find_element_by_id('guess2').click()
    time.sleep(1)
    driver.find_element_by_id('guess-2-box').find_element_by_class_name('guess-zz').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@class="jc_bank_11"]/i[' + xx + ']').click()
    driver.find_element_by_xpath('//*[@class="jc_bank_22"]/input').send_keys(odds)
    driver.find_element_by_xpath('//*[@class="jc_bank_33"]/i[' + moneytype + ']').click()
    driver.find_element_by_xpath('//*[@class="jc_bank_44"]/input').send_keys(money)
    driver.find_element_by_id('sub_banker').click()
    time.sleep(2)


def xzui(driver, money, xx):  # xx 仙豆1,2,猫豆3,4
    driver.find_element_by_id('guess2').click()
    time.sleep(1)
    driver.find_element_by_id('guess-2-box').find_element_by_id('bet_' + xx).click()
    time.sleep(1)
    driver.find_element_by_id('bet_money').clear()
    time.sleep(1)
    driver.find_element_by_id('bet_money').send_keys(money)
    time.sleep(1)
    i = 0
    while i < 10:
        if driver.find_element_by_id('bet_money').text == money:
            break
        else:
            driver.find_element_by_id('bet_money').clear()
            time.sleep(1)
            driver.find_element_by_id('bet_money').send_keys(money)
            i = i + 1
    time.sleep(1)
    driver.find_element_by_id('sub_bet_guess').click()
    time.sleep(1)


class login_register(unittest.TestCase):

    def setUp(self):
        self.url = url + roomid
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver1 = webdriver.Chrome()
        self.driver1.implicitly_wait(10)
        self.driver1.get(self.url)
        self.driver1.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_register001(self):
        # 开盘
        # 登陆账号
        js(cid, fzuid)
        driver = self.driver
        driver1 = self.driver1
        CookieLogin(fzuid, driver)
        CookieLogin(zzuid, driver1)
        # 房主开盘-输入值和推送
        time.sleep(1)
        driver.find_element_by_class_name('zhubo-guess').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@class="jc_setup_01"]/input[1]').clear()
        driver.find_element_by_xpath('//*[@class="jc_setup_01"]/input[1]').send_keys('竞猜主题1' + ts)
        driver.find_element_by_xpath('//*[@class="jc_setup_01"]/input[2]').clear()
        driver.find_element_by_xpath('//*[@class="jc_setup_01"]/input[2]').send_keys('主题1选项1')
        driver.find_element_by_xpath('//*[@class="jc_setup_01"]/input[3]').clear()
        driver.find_element_by_xpath('//*[@class="jc_setup_01"]/input[3]').send_keys('主题1选项2')
        driver.find_element_by_xpath('//*[@class="jc_setup_02"]/input[1]').clear()
        driver.find_element_by_xpath('//*[@class="jc_setup_02"]/input[1]').send_keys('竞猜主题2' + ts)
        driver.find_element_by_xpath('//*[@class="jc_setup_02"]/input[2]').clear()
        driver.find_element_by_xpath('//*[@class="jc_setup_02"]/input[2]').send_keys('主题2选项1')
        driver.find_element_by_xpath('//*[@class="jc_setup_02"]/input[3]').clear()
        driver.find_element_by_xpath('//*[@class="jc_setup_02"]/input[3]').send_keys('主题2选项2')
        driver.find_element_by_xpath('//*[@class="jc_setup_03"]/input[1]').clear()
        driver.find_element_by_xpath('//*[@class="jc_setup_03"]/input[1]').send_keys('竞猜主题3' + ts)
        driver.find_element_by_xpath('//*[@class="jc_setup_03"]/input[2]').clear()
        driver.find_element_by_xpath('//*[@class="jc_setup_03"]/input[2]').send_keys('主题3选项1')
        driver.find_element_by_xpath('//*[@class="jc_setup_03"]/input[3]').clear()
        driver.find_element_by_xpath('//*[@class="jc_setup_03"]/input[3]').send_keys('主题3选项2')
        driver.find_element_by_id('sub_start_guess').click()
        time.sleep(1)
        # 其他用户判断推送
        driver1.find_element_by_id('guess1').click()
        if driver1.find_element_by_xpath('//*[@id="guess-1-box"]/div[2]/span[2]').text != '进行中':
            self.verificationErrors.append("开盘推送错误")
        time.sleep(1)
        driver1.find_element_by_id('guess2').click()
        if driver1.find_element_by_xpath('//*[@id="guess-2-box"]/div[2]/span[2]').text != '进行中':
            self.verificationErrors.append("开盘推送错误")
        time.sleep(1)
        driver1.find_element_by_id('guess3').click()
        if driver1.find_element_by_xpath('//*[@id="guess-3-box"]/div[2]/span[2]').text != '进行中':
            self.verificationErrors.append("开盘推送错误")

    def test_login_register002(self):
        # 坐庄，选项1-猫豆，庄赢
        # 开盘，设置账号货币状态
        kp(cid, fzuid, ts)
        # addxd()
        addmoney(zzuid, 0, 2000)
        addmoney(xzuid, 0, 2000)
        driver1 = self.driver1
        CookieLogin(xzuid, driver1)
        # 坐庄
        driver = self.driver
        CookieLogin(zzuid, driver)
        time.sleep(5)
        zzui(driver, '1', '1000', '1', '1')
        zzui(driver, '2', '1000', '1', '1')
        # 下注结束盘口
        time.sleep(2)
        xzui(driver1, '1500', '3')
        driver1.find_element_by_xpath('//*[@class="tlayer-bx"]/div[3]/a[2]').click()
        js(cid, fzuid, xx2='2')
        # 坐庄记录查询
        driver.get(url + 'member/guess')
        time.sleep(1)
        Select(driver.find_element_by_id('guess_money')).select_by_value('2')
        Select(driver.find_element_by_id('guess_type')).select_by_value('2')
        driver.find_element_by_id('submit').click()
        # 坐庄记录首条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '赢', '主题2选项1', '猫豆', '1000', '500', '+485']:
            self.verificationErrors.append("坐庄数据错误1" + str(guess_rows))
        # 坐庄记录第二条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '赢', '主题2选项1', '猫豆', '1000', '1000', '+970']:
            self.verificationErrors.append("坐庄数据错误2" + str(guess_rows))
        # 坐庄站内信查询
        driver.get(url + 'member/showMessage')
        if driver.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[3]/li/span').text != '3455':
            self.verificationErrors.append("坐庄结算错误")
        time.sleep(1)
        # 坐庄站内信首条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的坐庄:主题2选项1, 结果是:赢, 盈亏:猫豆+485':
            self.verificationErrors.append("坐庄站内信数据错误1" + text1)
        # 坐庄站内信第二条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的坐庄:主题2选项1, 结果是:赢, 盈亏:猫豆+970':
            self.verificationErrors.append("坐庄站内信数据错误2" + text2)
        # 下注数据查询
        driver1.get(url + 'member/guess')
        time.sleep(1)
        Select(driver1.find_element_by_id('guess_money')).select_by_value('2')
        Select(driver1.find_element_by_id('guess_type')).select_by_value('1')
        driver1.find_element_by_id('submit').click()
        # 首条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '输', '主题2选项1', '猫豆', '1000', '-1000']:
            self.verificationErrors.append("下注数据错误1" + str(guess_rows))
        # 第二条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '输', '主题2选项1', '猫豆', '500', '-500']:
            self.verificationErrors.append("下注数据错误2" + str(guess_rows))
        # 下注站内信查询
        driver1.get(url + 'member/showMessage')
        time.sleep(1)
        if driver1.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[3]/li/span').text != '500':
            self.verificationErrors.append("下注结算错误")
        # 下注站内信首条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的下注:主题2选项1, 结果是:输, 盈亏:猫豆-1000':
            self.verificationErrors.append("下注站内信数据错误1" + text1)
        # 下注站内信第二条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的下注:主题2选项1, 结果是:输, 盈亏:猫豆-500':
            self.verificationErrors.append("下注站内信数据错误2" + text2)
        time.sleep(2)

    def test_login_register003(self):
        # 坐庄，选项1-猫豆，庄输
        # 开盘，设置账号货币状态
        kp(cid, fzuid, ts)
        # addxd()
        addmoney(zzuid, 0, 2000)
        addmoney(xzuid, 0, 2000)
        driver1 = self.driver1
        CookieLogin(xzuid, driver1)
        # 坐庄
        driver = self.driver
        CookieLogin(zzuid, driver)
        time.sleep(5)
        zzui(driver, '1', '1000', '1', '1')
        zzui(driver, '2', '1000', '1', '1')
        # 下注结束盘口
        time.sleep(2)
        xzui(driver1, '1500', '3')
        driver1.find_element_by_xpath('//*[@class="tlayer-bx"]/div[3]/a[2]').click()
        js(cid, fzuid, xx2='1')
        # 坐庄记录查询
        driver.get(url + 'member/guess')
        time.sleep(1)
        Select(driver.find_element_by_id('guess_money')).select_by_value('2')
        Select(driver.find_element_by_id('guess_type')).select_by_value('2')
        driver.find_element_by_id('submit').click()
        # 坐庄记录首条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '输', '主题2选项1', '猫豆', '1000', '500', '-1000']:
            self.verificationErrors.append("坐庄数据错误1" + str(guess_rows))
        # 坐庄记录第二条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '输', '主题2选项1', '猫豆', '1000', '1000', '-1000']:
            self.verificationErrors.append("坐庄数据错误2" + str(guess_rows))
        # 坐庄站内信查询
        driver.get(url + 'member/showMessage')
        if driver.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[3]/li/span').text != '0':
            self.verificationErrors.append("坐庄结算错误")
        time.sleep(1)
        # 坐庄站内信首条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的坐庄:主题2选项1, 结果是:输, 盈亏:猫豆-1000':
            self.verificationErrors.append("坐庄站内信数据错误1" + text1)
        # 坐庄站内信第二条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的坐庄:主题2选项1, 结果是:输, 盈亏:猫豆-1000':
            self.verificationErrors.append("坐庄站内信数据错误2" + text2)
        # 下注数据查询
        driver1.get(url + 'member/guess')
        time.sleep(1)
        Select(driver1.find_element_by_id('guess_money')).select_by_value('2')
        Select(driver1.find_element_by_id('guess_type')).select_by_value('1')
        driver1.find_element_by_id('submit').click()
        # 首条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '赢', '主题2选项1', '猫豆', '1000', '+970']:
            self.verificationErrors.append("下注数据错误1" + str(guess_rows))
        # 第二条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '赢', '主题2选项1', '猫豆', '500', '+970']:
            self.verificationErrors.append("下注数据错误2" + str(guess_rows))
        # 下注站内信查询
        driver1.get(url + 'member/showMessage')
        time.sleep(1)
        if driver1.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[3]/li/span').text != '3940':
            self.verificationErrors.append("下注结算错误")
        # 下注站内信首条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的下注:主题2选项1, 结果是:赢, 盈亏:猫豆+970':
            self.verificationErrors.append("下注站内信数据错误1" + text1)
        # 下注站内信第二条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的下注:主题2选项1, 结果是:赢, 盈亏:猫豆+970':
            self.verificationErrors.append("下注站内信数据错误2" + text2)

    def test_login_register004(self):
        # 坐庄，选项2-猫豆，庄赢
        # 开盘，设置账号货币状态
        kp(cid, fzuid, ts)
        # addxd()
        addmoney(zzuid, 0, 2000)
        addmoney(xzuid, 0, 2000)
        driver1 = self.driver1
        CookieLogin(xzuid, driver1)
        # 坐庄
        driver = self.driver
        CookieLogin(zzuid, driver)
        time.sleep(5)
        zzui(driver, '1', '1000', '2', '1')
        zzui(driver, '2', '1000', '2', '1')
        # 下注结束盘口
        time.sleep(2)
        xzui(driver1, '1500', '4')
        driver1.find_element_by_xpath('//*[@class="tlayer-bx"]/div[3]/a[2]').click()
        js(cid, fzuid, xx2='1')
        # 坐庄记录查询
        driver.get(url + 'member/guess')
        time.sleep(1)
        Select(driver.find_element_by_id('guess_money')).select_by_value('2')
        Select(driver.find_element_by_id('guess_type')).select_by_value('2')
        driver.find_element_by_id('submit').click()
        # 坐庄记录首条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '赢', '主题2选项2', '猫豆', '1000', '500', '+485']:
            self.verificationErrors.append("坐庄数据错误1" + str(guess_rows))
        # 坐庄记录第二条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '赢', '主题2选项2', '猫豆', '1000', '1000', '+970']:
            self.verificationErrors.append("坐庄数据错误2" + str(guess_rows))
        # 坐庄站内信查询
        driver.get(url + 'member/showMessage')
        if driver.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[3]/li/span').text != '3455':
            self.verificationErrors.append("坐庄结算错误")
        time.sleep(1)
        # 坐庄站内信首条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的坐庄:主题2选项2, 结果是:赢, 盈亏:猫豆+485':
            self.verificationErrors.append("坐庄站内信数据错误1" + text1)
        # 坐庄站内信第二条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的坐庄:主题2选项2, 结果是:赢, 盈亏:猫豆+970':
            self.verificationErrors.append("坐庄站内信数据错误2" + text2)
        # 下注数据查询
        driver1.get(url + 'member/guess')
        time.sleep(1)
        Select(driver1.find_element_by_id('guess_money')).select_by_value('2')
        Select(driver1.find_element_by_id('guess_type')).select_by_value('1')
        driver1.find_element_by_id('submit').click()
        # 首条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '输', '主题2选项2', '猫豆', '1000', '-1000']:
            self.verificationErrors.append("下注数据错误1" + str(guess_rows))
        # 第二条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '输', '主题2选项2', '猫豆', '500', '-500']:
            self.verificationErrors.append("下注数据错误2" + str(guess_rows))
        # 下注站内信查询
        driver1.get(url + 'member/showMessage')
        time.sleep(1)
        if driver1.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[3]/li/span').text != '500':
            self.verificationErrors.append("下注结算错误")
        # 下注站内信首条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的下注:主题2选项2, 结果是:输, 盈亏:猫豆-1000':
            self.verificationErrors.append("下注站内信数据错误1" + text1)
        # 下注站内信第二条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的下注:主题2选项2, 结果是:输, 盈亏:猫豆-500':
            self.verificationErrors.append("下注站内信数据错误2" + text2)
        time.sleep(2)

    def test_login_register005(self):
        # 坐庄，选项2-猫豆，庄输
        # 开盘，设置账号货币状态
        kp(cid, fzuid, ts)
        # addxd()
        addmoney(zzuid, 0, 2000)
        addmoney(xzuid, 0, 2000)
        driver1 = self.driver1
        CookieLogin(xzuid, driver1)
        # 坐庄
        driver = self.driver
        CookieLogin(zzuid, driver)
        time.sleep(5)
        zzui(driver, '1', '1000', '2', '1')
        zzui(driver, '2', '1000', '2', '1')
        # 下注结束盘口
        time.sleep(2)
        xzui(driver1, '1500', '4')
        driver1.find_element_by_xpath('//*[@class="tlayer-bx"]/div[3]/a[2]').click()
        js(cid, fzuid, xx2='2')
        # 坐庄记录查询
        driver.get(url + 'member/guess')
        time.sleep(1)
        Select(driver.find_element_by_id('guess_money')).select_by_value('2')
        Select(driver.find_element_by_id('guess_type')).select_by_value('2')
        driver.find_element_by_id('submit').click()
        # 坐庄记录首条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '输', '主题2选项2', '猫豆', '1000', '500', '-1000']:
            self.verificationErrors.append("坐庄数据错误1" + str(guess_rows))
        # 坐庄记录第二条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '输', '主题2选项2', '猫豆', '1000', '1000', '-1000']:
            self.verificationErrors.append("坐庄数据错误2" + str(guess_rows))
        # 坐庄站内信查询
        driver.get(url + 'member/showMessage')
        if driver.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[3]/li/span').text != '0':
            self.verificationErrors.append("坐庄结算错误")
        time.sleep(1)
        # 坐庄站内信首条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的坐庄:主题2选项2, 结果是:输, 盈亏:猫豆-1000':
            self.verificationErrors.append("坐庄站内信数据错误1" + text1)
        # 坐庄站内信第二条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的坐庄:主题2选项2, 结果是:输, 盈亏:猫豆-1000':
            self.verificationErrors.append("坐庄站内信数据错误2" + text2)
        # 下注数据查询
        driver1.get(url + 'member/guess')
        time.sleep(1)
        Select(driver1.find_element_by_id('guess_money')).select_by_value('2')
        Select(driver1.find_element_by_id('guess_type')).select_by_value('1')
        driver1.find_element_by_id('submit').click()
        # 首条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '赢', '主题2选项2', '猫豆', '1000', '+970']:
            self.verificationErrors.append("下注数据错误1" + str(guess_rows))
        # 第二条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '赢', '主题2选项2', '猫豆', '500', '+970']:
            self.verificationErrors.append("下注数据错误2" + str(guess_rows))
        # 下注站内信查询
        driver1.get(url + 'member/showMessage')
        time.sleep(1)
        if driver1.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[3]/li/span').text != '3940':
            self.verificationErrors.append("下注结算错误")
        # 下注站内信首条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的下注:主题2选项2, 结果是:赢, 盈亏:猫豆+970':
            self.verificationErrors.append("下注站内信数据错误1" + text1)
        # 下注站内信第二条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的下注:主题2选项2, 结果是:赢, 盈亏:猫豆+970':
            self.verificationErrors.append("下注站内信数据错误2" + text2)

    def test_login_register006(self):
        # 坐庄，选项1-仙豆，庄赢
        # 开盘，设置账号货币状态
        kp(cid, fzuid, ts)
        # addxd()
        addxd(zzuid, 2000)
        addxd(xzuid, 2000)
        driver1 = self.driver1
        CookieLogin(xzuid, driver1)
        # 坐庄
        driver = self.driver
        CookieLogin(zzuid, driver)
        time.sleep(5)
        zzui(driver, '1', '1000', '1', '2')
        zzui(driver, '2', '1000', '1', '2')
        # 下注结束盘口
        time.sleep(2)
        xzui(driver1, '1500', '1')
        driver1.find_element_by_xpath('//*[@class="tlayer-bx"]/div[3]/a[2]').click()
        js(cid, fzuid, xx2='2')
        # 坐庄记录查询
        driver.get(url + 'member/guess')
        time.sleep(1)
        Select(driver.find_element_by_id('guess_money')).select_by_value('1')
        Select(driver.find_element_by_id('guess_type')).select_by_value('2')
        driver.find_element_by_id('submit').click()
        # 坐庄记录首条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '赢', '主题2选项1', '仙豆', '1000', '500', '+485']:
            self.verificationErrors.append("坐庄数据错误1" + str(guess_rows))
        # 坐庄记录第二条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '赢', '主题2选项1', '仙豆', '1000', '1000', '+970']:
            self.verificationErrors.append("坐庄数据错误2" + str(guess_rows))
        # 坐庄站内信查询
        driver.get(url + 'member/showMessage')
        if driver.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[1]/li/span').text != '3455':
            self.verificationErrors.append("坐庄结算错误")
        time.sleep(1)
        # 坐庄站内信首条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的坐庄:主题2选项1, 结果是:赢, 盈亏:仙豆+485':
            self.verificationErrors.append("坐庄站内信数据错误1" + text1)
        # 坐庄站内信第二条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的坐庄:主题2选项1, 结果是:赢, 盈亏:仙豆+970':
            self.verificationErrors.append("坐庄站内信数据错误2" + text2)
        # 下注数据查询
        driver1.get(url + 'member/guess')
        time.sleep(1)
        Select(driver1.find_element_by_id('guess_money')).select_by_value('1')
        Select(driver1.find_element_by_id('guess_type')).select_by_value('1')
        driver1.find_element_by_id('submit').click()
        # 首条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '输', '主题2选项1', '仙豆', '1000', '-1000']:
            self.verificationErrors.append("下注数据错误1" + str(guess_rows))
        # 第二条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '输', '主题2选项1', '仙豆', '500', '-500']:
            self.verificationErrors.append("下注数据错误2" + str(guess_rows))
        # 下注站内信查询
        driver1.get(url + 'member/showMessage')
        time.sleep(1)
        if driver1.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[1]/li/span').text != '500':
            self.verificationErrors.append("下注结算错误")
        # 下注站内信首条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的下注:主题2选项1, 结果是:输, 盈亏:仙豆-1000':
            self.verificationErrors.append("下注站内信数据错误1" + text1)
        # 下注站内信第二条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的下注:主题2选项1, 结果是:输, 盈亏:仙豆-500':
            self.verificationErrors.append("下注站内信数据错误2" + text2)
        time.sleep(2)

    def test_login_register007(self):
        # 坐庄，选项1-仙豆，庄输
        # 开盘，设置账号货币状态
        kp(cid, fzuid, ts)
        # addxd()
        addxd(zzuid, 2000)
        addxd(xzuid, 2000)
        driver1 = self.driver1
        CookieLogin(xzuid, driver1)
        # 坐庄
        driver = self.driver
        CookieLogin(zzuid, driver)
        time.sleep(5)
        zzui(driver, '1', '1000', '1', '2')
        zzui(driver, '2', '1000', '1', '2')
        # 下注结束盘口
        time.sleep(2)
        xzui(driver1, '1500', '1')
        driver1.find_element_by_xpath('//*[@class="tlayer-bx"]/div[3]/a[2]').click()
        js(cid, fzuid, xx2='1')
        # 坐庄记录查询
        driver.get(url + 'member/guess')
        time.sleep(1)
        Select(driver.find_element_by_id('guess_money')).select_by_value('1')
        Select(driver.find_element_by_id('guess_type')).select_by_value('2')
        driver.find_element_by_id('submit').click()
        # 坐庄记录首条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '输', '主题2选项1', '仙豆', '1000', '500', '-1000']:
            self.verificationErrors.append("坐庄数据错误1" + str(guess_rows))
        # 坐庄记录第二条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '输', '主题2选项1', '仙豆', '1000', '1000', '-1000']:
            self.verificationErrors.append("坐庄数据错误2" + str(guess_rows))
        # 坐庄站内信查询
        driver.get(url + 'member/showMessage')
        if driver.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[1]/li/span').text != '0':
            self.verificationErrors.append("坐庄结算错误")
        time.sleep(1)
        # 坐庄站内信首条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的坐庄:主题2选项1, 结果是:输, 盈亏:仙豆-1000':
            self.verificationErrors.append("坐庄站内信数据错误1" + text1)
        # 坐庄站内信第二条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的坐庄:主题2选项1, 结果是:输, 盈亏:仙豆-1000':
            self.verificationErrors.append("坐庄站内信数据错误2" + text2)
        # 下注数据查询
        driver1.get(url + 'member/guess')
        time.sleep(1)
        Select(driver1.find_element_by_id('guess_money')).select_by_value('1')
        Select(driver1.find_element_by_id('guess_type')).select_by_value('1')
        driver1.find_element_by_id('submit').click()
        # 首条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '赢', '主题2选项1', '仙豆', '1000', '+970']:
            self.verificationErrors.append("下注数据错误1" + str(guess_rows))
        # 第二条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '赢', '主题2选项1', '仙豆', '500', '+970']:
            self.verificationErrors.append("下注数据错误2" + str(guess_rows))
        # 下注站内信查询
        driver1.get(url + 'member/showMessage')
        time.sleep(1)
        if driver1.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[1]/li/span').text != '3940':
            self.verificationErrors.append("下注结算错误")
        # 下注站内信首条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的下注:主题2选项1, 结果是:赢, 盈亏:仙豆+970':
            self.verificationErrors.append("下注站内信数据错误1" + text1)
        # 下注站内信第二条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的下注:主题2选项1, 结果是:赢, 盈亏:仙豆+970':
            self.verificationErrors.append("下注站内信数据错误2" + text2)

    def test_login_register008(self):
        # 坐庄，选项2-仙豆，庄赢
        # 开盘，设置账号货币状态
        kp(cid, fzuid, ts)
        # addxd()
        addxd(zzuid, 2000)
        addxd(xzuid, 2000)
        driver1 = self.driver1
        CookieLogin(xzuid, driver1)
        # 坐庄
        driver = self.driver
        CookieLogin(zzuid, driver)
        time.sleep(5)
        zzui(driver, '1', '1000', '2', '2')
        zzui(driver, '2', '1000', '2', '2')
        # 下注结束盘口
        time.sleep(2)
        xzui(driver1, '1500', '2')
        driver1.find_element_by_xpath('//*[@class="tlayer-bx"]/div[3]/a[2]').click()
        js(cid, fzuid, xx2='1')
        # 坐庄记录查询
        driver.get(url + 'member/guess')
        time.sleep(1)
        Select(driver.find_element_by_id('guess_money')).select_by_value('1')
        Select(driver.find_element_by_id('guess_type')).select_by_value('2')
        driver.find_element_by_id('submit').click()
        # 坐庄记录首条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '赢', '主题2选项2', '仙豆', '1000', '500', '+485']:
            self.verificationErrors.append("坐庄数据错误1" + str(guess_rows))
        # 坐庄记录第二条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '赢', '主题2选项2', '仙豆', '1000', '1000', '+970']:
            self.verificationErrors.append("坐庄数据错误2" + str(guess_rows))
        # 坐庄站内信查询
        driver.get(url + 'member/showMessage')
        if driver.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[1]/li/span').text != '3455':
            self.verificationErrors.append("坐庄结算错误")
        time.sleep(1)
        # 坐庄站内信首条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的坐庄:主题2选项2, 结果是:赢, 盈亏:仙豆+485':
            self.verificationErrors.append("坐庄站内信数据错误1" + text1)
        # 坐庄站内信第二条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的坐庄:主题2选项2, 结果是:赢, 盈亏:仙豆+970':
            self.verificationErrors.append("坐庄站内信数据错误2" + text2)
        # 下注数据查询
        driver1.get(url + 'member/guess')
        time.sleep(1)
        Select(driver1.find_element_by_id('guess_money')).select_by_value('1')
        Select(driver1.find_element_by_id('guess_type')).select_by_value('1')
        driver1.find_element_by_id('submit').click()
        # 首条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '输', '主题2选项2', '仙豆', '1000', '-1000']:
            self.verificationErrors.append("下注数据错误1" + str(guess_rows))
        # 第二条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '输', '主题2选项2', '仙豆', '500', '-500']:
            self.verificationErrors.append("下注数据错误2" + str(guess_rows))
        # 下注站内信查询
        driver1.get(url + 'member/showMessage')
        time.sleep(1)
        if driver1.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[1]/li/span').text != '500':
            self.verificationErrors.append("下注结算错误")
        # 下注站内信首条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的下注:主题2选项2, 结果是:输, 盈亏:仙豆-1000':
            self.verificationErrors.append("下注站内信数据错误1" + text1)
        # 下注站内信第二条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项1, 你的下注:主题2选项2, 结果是:输, 盈亏:仙豆-500':
            self.verificationErrors.append("下注站内信数据错误2" + text2)
        time.sleep(2)

    def test_login_register009(self):
        # 坐庄，选项2-仙豆，庄输
        # 开盘，设置账号货币状态
        kp(cid, fzuid, ts)
        # addxd()
        addxd(zzuid, 2000)
        addxd(xzuid, 2000)
        driver1 = self.driver1
        CookieLogin(xzuid, driver1)
        # 坐庄
        driver = self.driver
        CookieLogin(zzuid, driver)
        time.sleep(5)
        zzui(driver, '1', '1000', '2', '2')
        zzui(driver, '2', '1000', '2', '2')
        # 下注结束盘口
        time.sleep(2)
        xzui(driver1, '1500', '2')
        driver1.find_element_by_xpath('//*[@class="tlayer-bx"]/div[3]/a[2]').click()
        js(cid, fzuid, xx2='2')
        # 坐庄记录查询
        driver.get(url + 'member/guess')
        time.sleep(1)
        Select(driver.find_element_by_id('guess_money')).select_by_value('1')
        Select(driver.find_element_by_id('guess_type')).select_by_value('2')
        driver.find_element_by_id('submit').click()
        # 坐庄记录首条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '输', '主题2选项2', '仙豆', '1000', '500', '-1000']:
            self.verificationErrors.append("坐庄数据错误1" + str(guess_rows))
        # 坐庄记录第二条记录判断
        guess_rows = []
        for guess_row in driver.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '输', '主题2选项2', '仙豆', '1000', '1000', '-1000']:
            self.verificationErrors.append("坐庄数据错误2" + str(guess_rows))
        # 坐庄站内信查询
        driver.get(url + 'member/showMessage')
        if driver.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[1]/li/span').text != '0':
            self.verificationErrors.append("坐庄结算错误")
        time.sleep(1)
        # 坐庄站内信首条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的坐庄:主题2选项2, 结果是:输, 盈亏:仙豆-1000':
            self.verificationErrors.append("坐庄站内信数据错误1" + text1)
        # 坐庄站内信第二条记录判断
        driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的坐庄:主题2选项2, 结果是:输, 盈亏:仙豆-1000':
            self.verificationErrors.append("坐庄站内信数据错误2" + text2)
        # 下注数据查询
        driver1.get(url + 'member/guess')
        time.sleep(1)
        Select(driver1.find_element_by_id('guess_money')).select_by_value('1')
        Select(driver1.find_element_by_id('guess_type')).select_by_value('1')
        driver1.find_element_by_id('submit').click()
        # 首条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[2]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '1', '赢', '主题2选项2', '仙豆', '1000', '+970']:
            self.verificationErrors.append("下注数据错误1" + str(guess_rows))
        # 第二条记录判断
        guess_rows = []
        for guess_row in driver1.find_elements_by_xpath('//*[@class="table-bigbox"]/table/tbody/tr[3]/td'):
            guess_rows.append(guess_row.text)
        if guess_rows[1:] != ['1', '测试主题2' + ts, '2', '赢', '主题2选项2', '仙豆', '500', '+970']:
            self.verificationErrors.append("下注数据错误2" + str(guess_rows))
        # 下注站内信查询
        driver1.get(url + 'member/showMessage')
        time.sleep(1)
        if driver1.find_element_by_xpath('//*[@id="leftmenu-l"]/div[1]/div[2]/ul/a[1]/li/span').text != '3940':
            self.verificationErrors.append("下注结算错误")
        # 下注站内信首条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[2]/td[3]/a').click()
        text1 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[3]/td').text
        if text1 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的下注:主题2选项2, 结果是:赢, 盈亏:仙豆+970':
            self.verificationErrors.append("下注站内信数据错误1" + text1)
        # 下注站内信第二条记录判断
        driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[4]/td[3]/a').click()
        text2 = driver1.find_element_by_xpath('//*[@id="message-add"]/tbody/tr[5]/td').text
        if text2 != '你的竞猜房间:我的直播间, 房间ID:1, 主题:测试主题2' + ts + ', 主播选项:主题2选项2, 你的下注:主题2选项2, 结果是:赢, 盈亏:仙豆+970':
            self.verificationErrors.append("下注站内信数据错误2" + text2)

    def tearDown(self):
        self.driver.quit()
        self.driver1.quit()
        self.assertEqual([], self.verificationErrors)


suite = unittest.TestSuite()
suite.addTest(login_register("test_login_register003"))
suite.addTest(login_register("test_login_register008"))
suite.addTest(login_register("test_login_register009"))
unittest.main(defaultTest='suite')
# unittest.main()
# 插入cookie登录
# 插入cookie登录