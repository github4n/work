# -*- coding:utf-8 -*-
import time
import pymysql
import hashlib
import requests
import redis
from lxml import etree
import threading
import json
import struct
import socket


# 网站url
url = 'http://qa.new.huomaotv.com.cn'
roomid = '100'
domain = '.huomaotv.com.cn'
# url = 'http://www.huomao.com'
# 后台url
adminurl = 'http://qaadmin.new.huomaotv.com.cn'
cookiesadmin = {'huomaotvcheckcode': 'SQJ5', 'adminId': '33',
                'adminAccount': 'root', 'adminNick': 'root',
                'adminUserId': '0', 'adminLoginTime': '1473220408',
                'adminToken': 'bd2c21cb89ada618b16170504ad9f84d'}

userpwd = 'test1234'
# 全局数据库参数设置
host = '192.168.23.14'
user = 'root'
passwd = '123456'
# db = 'hm_money',
port = 3306
redisport = 6379
charset = 'utf8'


# 表参数查询
def hash_table(s, num=32):
    s = ('hm_db_' + s).encode('utf-8')
    m = hashlib.md5()
    m.update(s)
    md5s = m.hexdigest()
    md5ss = int(md5s[1:3], 16) % num
    return str(md5ss)


# 用户cookie生成
def cookies(uid):
    if uid:
        key = 'HUOMAOTV!@#$%^&*137SECRET'
        uid = str(uid)
        ts = str(int(time.time()))
        a = uid + str(ts) + key
        b = a.encode('utf-8')
        token = str(hashlib.md5(b).hexdigest())
        headers = {'user_e100fe70f5705b56db66da43c140237c': uid,
                   'user_6b90717037ae096e2f345fde0c31e11b': token,
                   'user_2c691ee7b8307f7fadc5c2c9349dbd7b': ts}
        return headers
    else:
        return {}


def CookieLogin(uid, driver):
    ts = str(int(time.time()))
    ts2 = str(int(time.time()) + 4320000)
    key = 'HUOMAOTV!@#$%^&*137SECRET'
    # ts = '1478919600'
    # ts2 = '1479363590'
    a = uid + str(ts) + key
    b = a.encode('utf-8')
    token = str(hashlib.md5(b).hexdigest())
    driver.add_cookie({'name': 'user_e100fe70f5705b56db66da43c140237c', 'value': uid, 'expiry': ts2, 'domain': domain})
    driver.add_cookie({'name': 'user_6b90717037ae096e2f345fde0c31e11b', 'value': token, 'expiry': ts2, 'domain': domain})
    driver.add_cookie({'name': 'user_2c691ee7b8307f7fadc5c2c9349dbd7b', 'value': ts, 'expiry': ts2, 'domain': domain})
    driver.add_cookie({'name': 'user_frontloginstat', 'value': '1', 'expiry': ts2, 'domain': domain})
    time.sleep(2)
    driver.refresh()


# 连接聊天室
def connect(cid, uid, url):
    data = requests.post(url + '/chat/getToken?', data={'cid': cid}, cookies=cookies(uid))
    print(data.text)
    data = json.loads(data.text[1:-1])
    data = data['data']
    HOST = data['host']
    PORT = int(data['port'])
    token = data['token']
    # print(HOST, PORT)
    # 定义socket类型，网络通信，TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # 关键代码binascii.a2b_hex
    a = b'{"sys":{"type":"pomelo-flash-tcp","pomelo_version":"0.7.x","version":"0.1.6b"},"user":null}'
    a = struct.pack('!hh' + str(len(a)) + 's', 256, len(a), a)
    print('连接system')
    s.send(a)
    data = s.recv(1024)
    # 发送某东西
    c = b'\x02\x00\x00\x00'
    print('发送某心跳')
    s.send(c)

    b = '\x00\x01 gate.gateHandler.lookupConnector{"channelId":"' + \
        cid + '","userId":' + uid + ',"log":true}'
    b = b.encode('utf-8')
    b = struct.pack('!hh' + str(len(b)) + 's', 1024, len(b), b)
    print('连接负载服务器')
    s.send(b)
    data = s.recv(1024)
    data2 = data.decode('utf-8')
    data3 = data2[6:]
    data3 = json.loads(data3)

    # s.close()
    host2 = data3['host']
    port2 = data3['port']
    # print((host2, port2))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host2, port2))
    # a = struct.pack('!hh' + str(len(a)) + 's', 256, len(a), a)
    print('再次连接system')
    s.send(a)
    data = s.recv(1024)
    e = b'\x02\x00\x00\x00'
    # c = struct.pack('!h', 512)
    print('发送某心跳')
    s.send(e)

    d = '\x00\x02 connector.connectorHandler.login{"channelId":"' + \
        cid + '","token":"' + token + '","userId":' + uid + '}'
    d = d.encode('utf-8')
    d = struct.pack('!hh' + str(len(d)) + 's', 1024, len(d), d)
    print('连接聊天室')
    s.send(d)
    data = s.recv(1024)
    print(data)
    print(time.time())
    while True:
        time.sleep(30)
        s.send(b'\x03\x00\x00\x00')
        print(time.time())


def connects(cid, uids, url):
    threads = []
    for i in uids:
        t = threading.Thread(target=connect, args=(cid, str(i), url))
        threads.append(t)

    for t in threads:
        t.start()


# 用户名查找uid
def finduid(yhm):
    tablname = 'username_' + hash_table(yhm)
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db='hm_user', port=port, charset=charset)
    cur = conn.cursor()
    sql = "SELECT uid FROM %s WHERE username = '%s'" % (tablname, yhm)
    cur.execute(sql)
    data = cur.fetchone()
    if data:
        return data[0]
    else:
        return False


# 设置仙豆
def addxd(uid, xd):
    xd = 0 if not xd else int(xd)
    uid = str(uid)
    r = redis.Redis(host=host, port=redisport, db=0, decode_responses=True)
    # oldxd = r.get('hm_free_bean_' + uid)
    # oldxd = 0 if not oldxd else int(oldxd)
    r.set('hm_free_bean_' + uid, xd)
    return True


# 设置用户猫币猫豆
def addmoney(uid, num1, num2):
    uid = str(str(uid))
    num1 = 0 if not num1 else num1
    num2 = 0 if not num2 else num2
    num1 = float(num1)
    num2 = float(num2)
    tablname = 'money_' + hash_table(uid)
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db='hm_money', port=port, charset=charset)
    cur = conn.cursor()  # 获取一个游标
    sql = "SELECT * FROM %s WHERE uid = %s" % (tablname, uid)
    cur.execute(sql)
    data = cur.fetchone()
    # 判断用户是否存在记录，存在则修改，否则插入数据
    if data:
        sql1 = "SELECT coin,bean FROM %s WHERE uid = %s" % (tablname, uid)
        cur.execute(sql1)
        data = cur.fetchone()
        # sql2 = "UPDATE  %s SET  coin =  %s, bean =  %s WHERE  uid = %s" % (tablname, num1 + float(data[0]), num2 + float(data[0]), uid)
        sql2 = "UPDATE  %s SET  coin =  %s, bean =  %s WHERE  uid = %s" % (tablname, num1, num2, uid)
        cur.execute(sql2)
    else:
        ts = int(time.time())
        sql3 = "INSERT INTO  %s(uid,coin,bean,ts) values(%s,%s,%s,%s)" % (tablname, uid, num1, num2, ts)
        cur.execute(sql3)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


# 绑定手机号
def bdsj(uid):
    url1 = url + '/test/uum/' + str(uid) + '/' + str(15800000000 + int(uid))
    r = requests.get(url1, cookies=cookies(uid))
    if r.status_code == 200:
        return True
    else:
        return False


# 注册用户返回uid,或登录返回uid
def zc(username):
    r = requests.post(url + '/user/lucky_reg', data={'nick_name': username + 'nc', 'user_pwd': userpwd, 'username': username, 'key': 'huomao_lucky'})
    if r.json()['code'] != '100':
        return False
    else:
        return r.json()['data']['uid']


# 申请直播并通过
def sqzb(uid):
    # 判断uid是否是主播
    uid = str(uid)
    r = requests.get(url + '/member/checkUsersIdentify', cookies=cookies(uid))
    if r.json()['data']['isAnchor'] is True:
        return False
    else:
        bdsj(uid)
        time.sleep(1)
        data = {'true_name': '测试号',
                'sex': '1',
                'gid': '97',
                'cred': '4',
                'card_code': '100' + uid,
                'card_pic': 'http://img.new.huomaotv.com.cn/upload/web/images/defaultimgs/0dc10ab4d7bda309e3095298ca689573/20160907110242mnxsySdt.png',
                'qq': '100' + uid,
                'agreement': '1'}
        r = requests.post(url + '/anchor/submitApply', data=data, cookies=cookies(uid), headers={'X-Requested-With': 'XMLHttpRequest'})
        r = requests.get(adminurl + '/anchor/lists', params={'field': 'uid', 'keyword': uid}, cookies=cookiesadmin)
        uidid = etree.HTML(r.text).xpath('//tr[2]/td[1]')[0].text
        r = requests.post(adminurl + '/index.php/anchor/submitVerify', data={'status': '1', 'is_push': '1', 'reason': '', 'id': uidid}, cookies=cookiesadmin)
        return True


# 更新流
def updatestream(stream, rommid):
    conn = pymysql.connect(host='192.168.23.14', user='root',
                           passwd='123456',
                           db='hm_contents', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    r = redis.Redis(host='192.168.23.14', port=6379, db=0)
    cur.execute("UPDATE  hm_channel SET  stream = %s WHERE room_number = %s", (stream, rommid))
    cur.execute("UPDATE  hm_channel SET  is_live = 1 WHERE room_number = %s", rommid)
    cur.execute("SELECT uid from hm_channel  WHERE room_number = %s", rommid)
    data = cur.fetchone()
    print(data)
    r.hset('hm_channel_anchor_' + str(data), 'stream', '"' + stream + '"')
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
