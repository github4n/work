#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/6/28 15:37
# Author : lixingyun
# Description :
import requests
from lxml import etree
from ..lib.config import domain_admin
from huomao.config import ADMIN_COOKIES

admin_cases = ['/channel/getChannelList']
other_links = ['#', '/eventTreasures/index', '/treasureSends/index','/guess/index','/guessuser/index']

ret = requests.get(domain_admin, cookies=ADMIN_COOKIES).text
links = etree.HTML(ret).xpath('//a')
for link in links:
    href = link.get('href')
    if href not in other_links:
        admin_cases.append(href.strip()) # 去除首尾空额
