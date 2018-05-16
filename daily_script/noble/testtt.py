#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/11 14:42
# Author : lixingyun
# Description :
from huomao.user import User
from huomao.money import MoneyClass
from huomao.common import REDIS_INST, Common

# name = ['noble{}'.format(i) for i in range(1,8)]
# for i in name:
#     u = User()
#     uid = u.find_uid(i)['msg']
#     print(uid)
# try:
#     uid = u.register('noble{}'.format(i))['uid']
#     u.bd_sj(uid)
# except:
#     pass
# MoneyClass.set_money(uid,9999999)
# User.create_noble(uid, level=i)
for i in range(1, 2):
    u = User()
    uid = u.reg('noble')
    print(uid)
    u.bd_sj(uid)
    MoneyClass.set_money(uid, 1200000)
    User.create_noble(uid,  level=7)
    User.set_noble_expire(uid, 40)

# username = ['hmjsf{}'.format(i) for i in range(1,100)]
# for i in username:
#     uid = User.find_uid(i)['msg']
#     key_username = 'hm_user_name_redis_prefix:{}'.format(Common.md5(i))
#     REDIS_INST.set(key_username, uid)
