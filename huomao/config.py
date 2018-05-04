#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 14:35
# Author : lixingyun
# Description :
import configparser
import os
import time
import calendar

# 获取文件的当前路径（绝对路径）
cur_path = os.path.dirname(os.path.realpath(__file__))
# 获取config.ini的路径
config_path = os.path.join(cur_path, 'config.ini')
conf = configparser.ConfigParser()
# 读取配置
conf.read(config_path)
# 网站url
URL = conf.get('urls', 'URL')
URL_API = conf.get('urls', 'URL_API')
DOMAIN = conf.get('urls', 'DOMAIN')
# 线上地址
URL_ONLINE = conf.get('urls', 'URL_ONLINE')
ADMIN_URL_ONLINE = conf.get('urls', 'ADMIN_URL_ONLINE')
# 后台url
ADMIN_URL = conf.get('urls', 'ADMIN_URL')
# 后台cookies
ADMIN_COOKIES = {
    'huomaotvcheckcode': 'SQJ5',
    'adminId': '33',
    'adminAccount': 'root',
    'adminNick': 'root',
    'adminUserId': '0',
    'adminLoginTime': '1473220408',
    'adminToken': 'bd2c21cb89ada618b16170504ad9f84d'
}
# 线上后台cookies
ADMIN_COOKIES_ONLINE = {
    'adminId': '7',
    'adminAccount': 'lxy',
    'adminNick': '%E6%9D%8E%E5%B9%B8%E8%BF%90',
    'adminUserId': '1870709',
    'adminLoginTime': '1504756354',
    'adminToken': '66897400739a15c9c6453a6e68b71e1d'
}
# redis配置
REDIS_CONFIG = {}
for (key, value) in conf.items('redis'):
    REDIS_CONFIG[key] = value
REDIS_CONFIG2 = {}
for (key, value) in conf.items('redis2'):
    REDIS_CONFIG2[key] = value

timestamp = int(time.time())
run_date = time.localtime()
run_date_year = run_date.tm_year
run_date_month = run_date.tm_mon
days = calendar.monthrange(run_date_year, run_date_month)[1]
mon_last_time = time.mktime((run_date_year, run_date_month, days, 23, 59, 59, 0, 0, 0))

REDIS_KEYS = {
    'fans':
        [
            'hm_loveliness_fan_lv_news_{uid}_{cid}',  # 房间粉丝等级
            'hm_level_first_channel_{cid}_{uid}',  # 用户房间首次1级
            'hm_level_six_{uid}',  # 用户是否首次6级
            'hm_level_first_{uid}',  # 用户是否首次1级
            'hm_fans_platform_{uid}',  #
            'hm_more_six_platform_list_{uid}',  #
            'hm_XIAN_1000_GIFT'  # 是否送爱心已得到粉丝值
        ],
    'subscribe': 'hm_users_subscribe_channels{uid}'
}
