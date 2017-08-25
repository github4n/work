# update:20161121 17:35
import requests
import pymysql
import random
from lxml import etree
import redis
nlist = []
cookies = {'huomaotvcheckcode': 'LR6A', 'adminId': '7', 'adminAccount': 'lxy',
           'adminNick': '%E6%9D%8E%E5%B9%B8%E8%BF%90', 'adminUserId': '1870709',
           'adminLoginTime': '1474620118', 'adminToken': 'deab64750163288434cccfa4f5229ef1'}

# cids = [2, 830, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 ,22, 61, 8685, 10235, 14740]
# for cid in cids:
#   res = requests.post('http://lxyadmin.new.huomaotv.com.cn/channel/updataChannelRedis', cookies=cookies, data={'cid':cid})
#   res = res.json()
#   print(res)

# 清除缓存
urls = ['static/web/css/live-yz-h.css', 'static/web/css/live-yz.css', 'static/web/huodong/js/live.ui.js', 'static/web/js/common.js', 'static/web/js/live.ui.js']
for url in urls:
    url = 'https://www.huomao.com/' + url + '?v=177'
    res = requests.post('http://bii3c.huomao.com/cachemanage/clearCdnCache', cookies=cookies, data={'url': url})
    res = res.json()
    print(res, url)
