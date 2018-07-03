#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 11:48
# Author : lixingyun
# Description :
import requests
from huomao.common import Common
from huomao.user import User
# version = 640
#
# urls_config = [
#     'poletest.js',
#     'https://www.huomao.com/static/web/js/live_draw.js',
#     ''
# ]
#
# for url in urls_config:
#     'https://www.huomao.com/static/web/js/{}?v={}'.format(url, version)
#
#
Common.clear_cdn_cache('https://www.huomao.com/static/web/css/common.css?v=662')
# Common.clear_cdn_cache('https://www.huomao.com/static/web/js/live_draw.js?v=640')
#
# User.create_noble(5260, level=7, month=1, cid=13)
#
#
# exit()
# for uid in range(5260, 5261):
#
#     requests.get('http://lxy.new.huomaotv.com.cn/chatnew/sendGift?pos=2&cid=13&gift=8&t_count=1&isbag=0',cookies=Common.generate_cookies(uid))
