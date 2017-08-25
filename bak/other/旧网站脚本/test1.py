import csv
import urllib.request
import urllib
import hashlib
import time
import threading
import json

# 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库

url = 'http://chat.huomaotv.cn/index.php?'


def headers(uid):
    key = 'HUOMAOTV!@#$%^&*137SECRET'
    uid = str(uid)
    ts = str(int(time.time()))
    a = uid + str(ts) + key
    b = a.encode('utf-8')
    token = str(hashlib.md5(b).hexdigest())
    headers = {'Cookie': 'huomaotvhjhdwq_u_ID=' + uid +
               '; huomaotvhjhdwq_u_token=' + token + '; huomaotvhjhdwq_u_ts=' + ts,
               'Connection': 'keep-alive'}
    return headers


# 请求|method:方法名|data:数据|uid:请求的headers|type:请求方式默认get
def request(method, data, requesttype=None, uid=None):
    if requesttype:
        data = urllib.parse.urlencode(data)
        # post数据需要转换bite
        data = data.encode('utf8')
        res = urllib.request.Request(url + method, data, headers(uid))
    else:
        data = urllib.parse.urlencode(data)
        res = urllib.request.Request(url + method + data, headers=headers(uid))
    data = urllib.request.urlopen(res)
    data1 = data.read().decode('utf-8')
    # print(data1[1:-1])
    data2 = json.loads(data1[1:-1])
    print(data2)


reader = csv.reader(open(r'C:\\Users\\lucky\\Desktop\\mtv_chat_log.csv', 'r'))
list0 = ['hhh']
for row in reader:
    s = row[5]
    list0.append(s)
list1 = [list0[1:300], list0[301:600], list0[601:900],
         list0[901:1200], list0[1201:1500], list0[1501:]]
args = [357855, 461250, 357849, 461253, 1506416, 199657]
cid = '3414'


def fy(uid1, n):
    for i in range(0, len(n)):
        data1 = {'data': n[i],
                 'cid': cid,
                 'phone': '1'}
        request('c=live&a=send_msg&', data1, uid=uid1)


threads = []
t1 = threading.Thread(target=fy, args=(args[0], list1[0]))
threads.append(t1)

for t in threads:
    # t.setDaemon(True)
    t.start()
