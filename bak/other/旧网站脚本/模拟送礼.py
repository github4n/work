# -*- coding:utf-8 -*-
import urllib
import http.cookiejar
import random
import threading
import time


def login(url, username, password):
    url1 = 'http://' + url + '/index.php?c=ajax&a=user_do'
    postdata1 = urllib.parse.urlencode(
        {'username': username, 'password': password, 'vcode': 'lxy1',
         'state': 'from', 'remember': '1', 'ac': 'login'})
    postdata1 = postdata1.encode('utf-8')
    res1 = urllib.request.urlopen(url1, postdata1)
    # print(bytes.decode(res1.read()))


def sendgift(url, roomid, gift, count, type):

    # print(111)
    # for item in cookie:
    #     print('Name = ' + item.name)
    #     print('Value = ' + item.value)

    # print(222)
    # for item in cookie:
    #     print('Name = ' + item.name)
    #     print('Value = ' + item.value)


    url2 = 'http://' + url + '/index.php?c=live&a=send_msg'
    postdata2 = urllib.parse.urlencode(
        {'msg_type': 'gift', 'data': 'gift', 'pos': gift - 2, 'cid': roomid, 'gift': gift, 't_count': count, 'send_gift_type': type, '_': '1452562574801'})
    postdata2 = postdata2.encode('utf-8')

    res2 = urllib.request.urlopen(url2, postdata2)



    # print(333)
    # for item in cookie:
    #     print('Name = ' + item.name)
    #     print('Value = ' + item.value)
    
    print(bytes.decode(res2.read()))


def gettype(id, count):
    # 设b > a
    dict1 = {
        3: [10, 30],
        4: [15, 30],
        5: [10, 13],
        6: [2, 3],
        7: [0, 0]
    }
    if id in dict1.keys():
        if dict1[id][1] <= 0:
            type = 1
        elif count >= dict1[id][1]:
            type = 2
        elif dict1[id][0] < count < dict1[id][1]:
            type = 2
        elif count <= dict1[id][0]:
            type = 1
    return(type)


def monisl():
    # id = 5  # random.randint(3, 7)
    # count = 2  #
    # count = random.randint(1, 20)
    # url = 'www.huomaotv.com.cn'
    url = 'test-new_gift.huomaotv.com.cn'
    roomid = '115'
    # username = 'testlevel100'
    # username = 'testlevel' + str(random.randint(100, 102))
    # print(username)

    for a in range(220):
        # name = ['test1453188451', 'test1453190084', 'test1453190114']
        # i = random.randint(0, 2)
        # username = name[i]
        username = 'test1453343182'
        cookie = http.cookiejar.CookieJar()
        cjhdr = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(cjhdr)
        urllib.request.install_opener(opener)
        login(url, username, 'test1234')
        count = random.randint(1, 20)
        print(username)
        # id = random.randint(3, 7)
        id = 5
        type = gettype(id, count)
        if id == 5:
            type = 2
        sendgift(url, roomid, id, count, type)
        # id = 4
        # sendgift(url, roomid, id, count, type)
        # id = 5
        # sendgift(url, roomid, id, count, type)
monisl()
# threading.Thread(target=monisl, args=('testlevel100',)).start()
# monisl('testlevel100')
# threads = []
# t1 = threading.Thread(target=monisl, args=('testlevel100',))
# threads.append(t1)
# t2 = threading.Thread(target=monisl, args=('testlevel101',))
# threads.append(t2)
# t3 = threading.Thread(target=monisl, args=('testlevel102',))
# threads.append(t3)
# for t in threads:
# t.setDaemon(True)
#     t.start()
