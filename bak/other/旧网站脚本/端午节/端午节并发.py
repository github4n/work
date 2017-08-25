import pymysql
import urllib.request
import urllib.parse
import hashlib
import time
import json
import threading
# 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
uid = 342911
url = 'http://tuyu.huomaotv.com.cn/index.php?c=Dragon&a=achieve_beans'


def headers(uid):
    key = 'HUOMAOTV!@#$%^&*137SECRET'
    uid = str(uid)
    ts = str(time.time())
    a = uid + str(ts) + key
    b = a.encode('utf-8')
    token = str(hashlib.md5(b).hexdigest())
    headers = {'Cookie': 'huomaotvhjhdwq_u_ID=' + uid +
               '; huomaotvhjhdwq_u_token=' + token + '; huomaotvhjhdwq_u_ts=' + ts,
               'Connection': 'keep-alive'}
    return headers


def aa():
    res = urllib.request.Request(url, None, headers(342911))
    data = urllib.request.urlopen(res)
    data1 = data.read().decode('utf-8')
    print(data1) 


threads = []
for i in range(0, 1000):
    t = threading.Thread(target=aa, args=())
    threads.append(t)

for t in threads:
    # t.setDaemon(True)
    t.start()