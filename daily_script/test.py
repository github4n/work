#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 11:48
# Author : lixingyun
# Description :
import requests
from lxml import etree

for page in range(1,22):

    url = f'http://www.huomao188.com/api/user/bag/570/list.do?rel=user_bag&data=loading&_=1534335901535&page={page}'

    cookies = {
        'JSESSIONID':'4A4A8A4BCFDD10CCEBE08C5670D4E7FA',
    }

    ret = requests.get(url,cookies=cookies)
    ret = ret.json()['datas']['list']

    for key in ret:
        print(f"{key['id']},{key['name']},{key['value']},{key['rarity']['tag']}")
