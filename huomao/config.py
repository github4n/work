#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 14:35
# Author : lixingyun
# Description :
import os
import time
import calendar
import logging

# 获取文件的当前路径（绝对路径）
huomao_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(huomao_path, 'huomao.log')
# logging 配置
# logging.basicConfig(format='%(asctime)s %(filename)10s [line:%(lineno)5d]  %(levelname)s %(message)s',
#                     datefmt='%Y/%m/%d %I:%M:%S %p',
#                     level=logging.DEBUG,
#                     filename=log_path,
#                     filemode='a')
# 创建流处理器
# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)

# 创建文件处理器
handler = logging.FileHandler(log_path)

# 创建formatter
formatter = logging.Formatter('%(asctime)s %(filename)10s [line:%(lineno)5d] %(name)10s %(levelname)s %(message)s')
# Formatter绑定在Handler上
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

# 创建logger记录器实例
logger_huomao = logging.getLogger('huomao')
logger_huomao.setLevel(logging.DEBUG)
# Handler绑定在logger上
logger_huomao.addHandler(handler)

# 获取peewee日志
logger_peewee = logging.getLogger('peewee')
logger_peewee.setLevel(logging.DEBUG)
logger_peewee.addHandler(handler)

# 数据库配置
DB_CONFIG = {'host': '10.10.23.15', 'user': 'huomao', 'password': 'huomao', 'port': 3306}
DB_CONFIG2 = {'host': '10.10.23.15', 'user': 'huomao', 'password': 'huomao', 'port': 3307}
# redis配置
REDIS_CONFIG = {'host': 'db.huomaotv.com.cn', 'port': 6379}
REDIS_CONFIG2 = {'host': '10.10.23.12', 'port': 6379}

# 网站url
URL = 'http://qa.new.huomaotv.com.cn'
URL_API = 'http://qa.new.huomaotv.com.cn'
DOMAIN = '.huomaotv.com.cn'
# 线上地址
URL_ONLINE = 'https://www.huomao.com'
ADMIN_URL_ONLINE = 'http://bii3c.huomao.com'
# 后台url
ADMIN_URL = 'http://qaadmin.new.huomaotv.com.cn'
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

timestamp = int(time.time())
run_date = time.localtime()
run_date_year = run_date.tm_year
run_date_month = run_date.tm_mon
days = calendar.monthrange(run_date_year, run_date_month)[1]
mon_last_time = time.mktime((run_date_year, run_date_month, days, 23, 59, 59, 0, 0, 0))
mon_first_time = time.mktime((run_date_year, run_date_month, 1, 0, 0, 0, 0, 0, 0))

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
