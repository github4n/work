#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/8/11 10:08
# Author : lixingyun
import sqlite3

conn = sqlite3.connect('mysite_db.sqlite3')
cursor = conn.cursor()
# a = [118, 258, 277, 365, 366, 509, 822, 842, 855, 858, 919, 961, 1081, 1108, 1150, 1151, 1188, 1189, 1209, 1257, 1259, 1282]
a = 118
sql1 = 'select * from release_pre where id = {}'.format(a)
sql2 = 'select * from release_log where id = {}'.format(a)
cursor.execute(sql1)
values = cursor.fetchall()
print(values)
cursor.execute(sql2)
values = cursor.fetchall()
print(values)
# for value in values:
#     a.append(value[0])
#
#     print(a)