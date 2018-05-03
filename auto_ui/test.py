#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/3 13:40
# Author : lixingyun
# Description :
import configparser
import os

# 获取文件的当前路径（绝对路径）
cur_path = os.path.dirname(os.path.realpath(__file__))
# 获取config.ini的路径
config_path = os.path.join(cur_path, 'config.ini')
conf = configparser.ConfigParser()
conf.read(config_path)
mobile = conf.get('config','mobile')
conf.set('config', 'mobile', str(int(mobile) + 1))

with open(config_path, 'w') as fw:
    conf.write(fw)

print(type(mobile))