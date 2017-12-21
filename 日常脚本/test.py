#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/13 19:59
# Author : lixingyun
import sys
from  urllib import parse
sys.path.append('../')
from common.common import Common
from gevent import monkey
data ={'uid':461250,
       'cid':1,
       'time':1513843380,
       'data':'222',
       # 'ver':1000,
       # 'refer':'ios',
       # 'post_data':1,
       # 'pf_ver':'11.0.3',
       # 'mp_openid':'317f6bf302d88824ba07e88b9309289c',
       # 'fr':'applestore',
       # 'expires_time':1510302832,
       # 'an':126,
       # 'access_token':'252d74d74a6d7d440750e4036c16f53b',
       }
token = Common.encrypt(data)
print(token)


