
# 登录：c=ajax&a=user_do
# 猜时间 subject_guess_3435
# http://www.huomaotv.com.cn/index.php?c=Crontab&a=flow_Bureau
# 17717305559 12345678  select111 test123456
# -*- coding:utf-8 -*-
import hashlib
import urllib
import time
import json

url1 = 'http://test-new_guess.huomaotv.com.cn/index.php?'


# 计算订单下注存放哪各表
def jsddh(ddh):
    x = 'guess_user_' + str(ddh)
    a = x.encode('utf-8')
    b = hashlib.md5(a).hexdigest()
    print(int(b[1:3], 16) % 32)


# cookie计算
def cookie(uid):
    key = 'HUOMAOTV!@#$%^&*137SECRET'
    ts = str(time.time())
    a = uid + str(ts) + key
    b = a.encode('utf-8')
    token = str(hashlib.md5(b).hexdigest())
    cookie1 = [('Cookie', 'huomaotvhjhdwq_u_ID=' + uid + '; huomaotvhjhdwq_u_token=' + token + '; huomaotvhjhdwq_u_ts=' + ts),
               ('Referer', 'http://www.huomaotv.com.cn/live/1704'),
               ('Connection', 'keep-alive'),
               ('User-Agent',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'),
               ('Content-Type', 'application/x-www-form-urlencoded'),
               ('Host', 'www.huomaotv.com.cn'),
               ('Origin', 'http://www.huomaotv.com.cn')]
    return cookie1


def aa(cookie, data, type1='get'):
    url1 = 'http://test-new_guess.huomaotv.com.cn/index.php?'
    # url1 = 'http://www.huomaotv.com.cn/index.php?'
    opener = urllib.request.build_opener()
    # opener.addheaders.append(cookie)
    opener.addheaders = cookie
    if type1 == 'get':
        url = url1 + urllib.parse.urlencode(data)
        res = opener.open(url)
        # data1 = bytes.decode(res.read())
        data1 = res.read().decode('utf-8')
        data2 = json.loads(data1[1:-1])
        print(data2)
    else:
        url = url1 + type1
        postdata = urllib.parse.urlencode(data)
        postdata = postdata.encode('utf-8')
        res = opener.open(url, postdata)
        data1 = res.read().decode('utf-8')
        data2 = json.loads(data1[1:-1])
        print(data2)
