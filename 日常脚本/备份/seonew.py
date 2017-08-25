# -*- coding: utf-8 -*-
import os
# import HTMLParser
from html.parser import HTMLParser
from bottle import template

# 读取html模板信息
html_parser = HTMLParser()
f = open(r'D:\下载\火猫\news.html', 'r', encoding='utf-8')
template_demo = f.read()
filedir = 'D:\下载\火猫\火猫\\'
i = 0
for parent, dirnames, filenames in os.walk(filedir):
    for filename in filenames:
        file = filedir + filename
        f = open(file, 'r')
        bt = filename[:-4]
        nr = f.read()
        name = 'new_{}'.format(i)
        html = template(template_demo, bt=bt, nr=nr)
        filehtml = 'D:\下载\火猫\\test\\' + name + '.html'
        f2 = open(filehtml, 'w', encoding='utf-8')
        f2.write(html)
        f2.close()
        i += 1
        # if i > 10:
        #     break
