#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/4/26 13:51
# Author : lixingyun
# Description : 活动自动截图

from selenium import webdriver
import time
import datetime
import requests
import itchat

itchat.auto_login(hotReload=True)
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get('https://www.huomao.com/active/firstDayPay')
driver.execute_script('var x=document.documentElement.scrollTop=2100;')


def send_wx(pic_file):
    toUserName_hp = itchat.search_friends(nickName='宏鹏')[0]['UserName']
    ret1 = itchat.send('现在的时间是:' + time.asctime(time.localtime(time.time())), toUserName=toUserName_hp)  #
    print(ret1)
    ret2 = itchat.send("@fil@%s" % pic_file, toUserName=toUserName_hp)  #
    print(ret2)


while True:
    now = datetime.datetime.now()
    today = datetime.date.today()
    start_time = datetime.datetime(today.year, today.month, today.day, 23, 55, 0, 0)
    end_time = datetime.datetime(today.year, today.month, today.day, 0, 5, 0, 0)
    if now >= start_time or now <= end_time:
        try:
            pic_file = 'C:\\Users\\Admin\\Desktop\\pic{}.png'.format(int(time.time()))
            driver.save_screenshot(pic_file)
            driver.refresh()
            send_wx(pic_file)
            ret = requests.get('https://www.huomao.com/active_file/EveryRecharge/getRank')
            print(ret.json())
        except:
            pass
    else:
        print('还没到时间',now)
    time.sleep(60)
