import urllib.request
from lxml import etree
import json
import os
import time


def fwq():
    for i in range(1, 4):
        res = urllib.request.urlopen("http://www.ishadowsocks.net/")
        selector = etree.HTML(res.read())
        a = selector.xpath('//*[@id="free"]/div/div[2]/div[%s]/h4' % i)
        s = []
        for j in range(0, 3):
            x = (a[j].text).split(':')[1]
            if x:
                s.append(x)
            else:
                s = []
        if s:
            return s

fwq = fwq()
file = r'E:\ss\gui-config.json'
file_object = open(file)
data = file_object.read()
s = json.loads(data)
configs = s['configs']
configs[0]['server'] = fwq[0].upper()
configs[0]['server_port'] = fwq[1]
configs[0]['password'] = fwq[2]
print(s)
json.dump(s, open(file, 'w'))
file_object.close()
time.sleep(1)
os.startfile(r"E:\ss\Shadowsocks.exe")

