# 死链查询，还缺ajax和其他链接
from lxml import etree
import time
import requests
domainurl = 'http://www.huomao.com'
# url = 'http://www.huomao.com'
urls = ['http://www.huomao.com',
        'http://www.huomao.com/channel/all',
        'http://www.huomao.com/game'
        ]


def geturl(url):
    r = requests.get(url)
    hrefs = etree.HTML(r.text).xpath('//a')
    hrefs2 = []
    for href in hrefs:
        try:
            if href.attrib['href'][0:17] == 'http://www.huomao':
                hrefs2.append(href.attrib['href'])
            elif href.attrib['href'][0:4] == 'java' or href.attrib['href'][0:4] == '#':
                continue
            elif href.attrib['href'][0:1] == '/':
                hrefs2.append(domainurl + href.attrib['href'])
            elif href.attrib['href'][0:4] != 'http':
                hrefs2.append(domainurl + '/' + href.attrib['href'])
        except:
                pass
    return hrefs2


hrefs = []
for url in urls:
    hrefs.extend(geturl(url))

# 去重
hrefs = list(set(hrefs))

for href in hrefs:
    time1 = time.time()
    r = requests.get(href)
    time2 = time.time()
    time3 = time2 - time1
    if r.status_code != 200:
        print(r.status_code, href, '耗时' + str(time3))
print('链接一共' + str(len(hrefs)))
