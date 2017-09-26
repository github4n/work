import gevent
from gevent import monkey
monkey.patch_all()
import time
import requests
import hashlib

# 默认房间号1，选择主题1，默认仙豆1，坐庄额度1000仙豆，下注额度10，退庄序号pos1，竞猜序号0，选择选项1，赔率默认1,流局默认1
cid = '2'  # 是房间主键
zbuid = '1522'
zzuid = '3866'
xzuid = '3865'
url = 'http://qa.new.huomaotv.com.cn'


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

# 开盘


def kp(cid, uid):
    data = {'cid': cid,
            'first[title]': '测试主题1' + str(int(time.time())),
            'first[choice_1]': '主题1选项1',
            'first[choice_2]': '主题1选项2',
            'first[type]': '1',
            'second[title]': '测试主题2' + str(int(time.time())),
            'second[choice_1]': '主题1选项1',
            'second[choice_2]': '主题1选项2',
            'second[type]': '1',
            'third[title]': '测试主题3' + str(int(time.time())),
            'third[choice_1]': '主题1选项1',
            'third[choice_2]': '主题1选项2',
            'third[type]': '1'}
    res = requests.get('http://qa.new.huomaotv.com.cn/guess/setGuessSubject', data, cookies=cookies(uid))
    data = res.json()
    print('开盘****************:{}'.format(data))
    # 返回订单号
    return data['data']['1']['md']


# 结束盘口。num序号0，1，2，choice选项1，2


def js(cid, zbuid):
    data = {'params[0]': '1',
            'params[2]': '1',
            'params[1]': '1',
            'cid': cid}
    res = requests.get(url + '/Guess/setCloseGuess?', params=data, cookies=cookies(zbuid))
    print('结束****************:{}'.format(res.json()))


# 坐庄
def zz(cid, order_id, zzuid, odds='1'):
    data = {'choice_name': '主题1选项1',  # 选项名
            'title': '0',  # 竞猜序号
            'cid': cid,  # 房间号
            'odds': odds,  # 赔率
            'money_type': '2',  # 1仙豆 2猫豆
            'order_id': order_id,  # 订单号
            'money': '1000',  # 坐庄金额
            'choice': '1'}  # 选项序号
    res = requests.get(url + '/guess/banker?', params=data, cookies=cookies(zzuid))
    print('坐庄****************:{}'.format(res.json()))


# 封庄
def fz(cid, order_id, zzuid):
    data = {'title': '0',  # 竞猜序号
            'cid': cid,  # 房间号
            'pos': '1',  # 庄序号
            'money_type': '1',  # 1仙豆 2猫豆
            'order_id': order_id,  # 订单号
            'choice': '1'}  # 选项序号
    res = requests.get(url + '/Guess/backBanker?', params=data, cookies=cookies(zzuid))
    print(res.json())


# 下注
def xz(cid, zzuid, xzuid, order_id):
    data = {'choice_title': '主题1选项1',  # 选项名
            'title': '0',  # 竞猜序号
            'cid': cid,  # 房间号
            'banker_uid': zzuid,  # 坐庄uid
            'bet_choice': '1',  # 下注选项
            'banker_choice': '1',  # 坐庄选项
            'odds': '1',  # 赔率
            'pos': '0',
            'money_type': '2',  # 1仙豆 2猫豆
            'order_id': order_id,
            'money': '10',  # 下注额
            'bet_index': '3',
            'order_flag': 'false'}  # 选项序号
    res = requests.get(url + '/Guess/bet?', params=data, cookies=cookies(xzuid))
    print('下注****************:{}'.format(res.json()))


def phonejc(uid):
    phoneurl = 'http://lxyapi.new.huomaotv.com.cn/user/bet'
    phonedata = {
        'uid': uid,
        'title': 2,
        'time': 1483950180,
        'refer': 'ios',
        'pos': 0,
        'order_id': 1483950019152222,
        'odds': 1,
        'mp_openid': 'd31f177be1a2347bd6eea7932442b663',
        'money_type': 2,
        'money': 10,
        'cid': 2,
        'bet_index': 3,
        'bet_choice': 1,
        'banker_uid': 1412,
        'banker_choice': 1,
        'choice_title': 2,
    }

    res = requests.get(phoneurl, params=phonedata)
    print(res.json())


# # 封盘。num序号0，1，2，choice3是封盘(cid, zzuid, xzuid, order_id)
# def fp(cid, zbuid):
#     data = {'params[0]': '3',
#             'params[2]': '3',
#             'params[1]': '3',
#             'cid': cid}
#     common.request('/Guess/setCloseGuess?', data, uid=zbuid)


# # 流局修改redis和请求
# def lj1(cid):
#     r = redis.Redis(host='192.168.23.14', port=6379, db=0)
#     data = r.get('hm_subject_guess_' + cid)
#     data1 = data.decode('utf-8')
#     data2 = json.loads(data1)
#     data3 = int(data2[0]['addtime'])
#     data2[0]['addtime'] = str(data3 - 21800)
#     r.set('hm_subject_guess_' + cid, json.dumps(data2))


# def lj2():
#     res = urllib.request.Request(common.url + '/guess/timeoutEndGuess')
#     data = urllib.request.urlopen(res)
#     data1 = data.read().decode('utf-8')
#     print(data1)


# # case1:结束，坐庄并发
# def case1():
#     js(cid, zbuid)
#     order_id = kp(cid, zbuid)
#     # print('表地址' + order_id)
#     threads = []
#     t1 = threading.Thread(target=js, args=(cid, zbuid))
#     for i in range(1, 500):
#         t2 = threading.Thread(target=zz, args=(cid, order_id, zzuid))
#         threads.append(t2)
#     threads.append(t1)
#     print('*' * 150)
#     for t in threads:
#         t.start()
# # case1()
# # js(cid, zbuid)
# # case2：结束，封庄并发


# def case2():
#     js(cid, zbuid)
#     order_id = kp(cid, zbuid)
#     zz(cid, order_id, zzuid)
#     time.sleep(2)
#     threads = []
#     t1 = threading.Thread(target=js, args=(cid, zbuid))
#     threads.append(t1)
#     for i in range(1, 2):
#         t2 = threading.Thread(target=fz, args=(cid, order_id, zzuid))
#         threads.append(t2)
#     print('*' * 150)
#     for t in threads:
#         t.start()
# # case2()


# # case3：结束，下注并发**************************
def case3():
    js(cid, zbuid)
    order_id = kp(cid, zbuid)
    zz(cid, order_id, zzuid)
    t1 = time.time()
    events = []
    events.extend([gevent.spawn(js, cid, zbuid) for i in range(0, 200)])
    events.extend(gevent.spawn(xz, cid, zzuid, xzuid, order_id) for i in range(0, 200))

    # events.extend(gevent.spawn(xz, cid, zzuid, xzuid, order_id) for i in range(0, 500))
    gevent.joinall(events)
    print('时间消耗{}'.format(time.time() - t1))


# case3()
js(2, 1522)
# # case4:结束并发
# def case4():
#     js(cid, zbuid)
#     order_id = kp(cid, zbuid)
#     zz(cid, order_id, zzuid)
#     xz(cid, zzuid, xzuid, order_id)
#     threads = []
#     t1 = threading.Thread(target=js, args=(cid, zbuid))
#     t2 = threading.Thread(target=js, args=(cid, zbuid))
#     threads.append(t1)
#     threads.append(t2)
#     print('*' * 150)
#     for t in threads:
#         t.start()
# #case4()


# # case5:坐庄，流盘并发 暂时却流盘redis逻辑
# def case5():
#     js(cid, zbuid)
#     order_id = kp(cid, zbuid)
#     lj1(cid)
#     threads = []
#     t1 = threading.Thread(target=lj2, args=())
#     for i in range(1, 2):
#         t2 = threading.Thread(target=zz, args=(cid, order_id, zzuid))
#         threads.append(t2)
#     threads.append(t1)
#     print('*' * 150)
#     for t in threads:
#         t.start()
# #case5()

# # case6:封庄并发
# def case6():
#     js(cid, zbuid)
#     order_id = kp(cid, zbuid)
#     zz(cid, order_id, zzuid)
#     time.sleep(2)
#     threads = []
#     for i in range(1, 30):
#         t1 = threading.Thread(target=fz, args=(cid, order_id, zzuid))
#         threads.append(t1)
#     print('*' * 150)
#     for t in threads:
#         t.start()

# # case7:封庄,流盘并发 暂时却流盘redis逻辑
# def case7():
#     js(cid, zbuid)
#     order_id = kp(cid, zbuid)
#     zz(cid, order_id, zzuid)
#     lj1(cid)
#     time.sleep(2)
#     threads = []
#     for i in range(1, 2):
#         t1 = threading.Thread(target=fz, args=(cid, order_id, zzuid))
#         threads.append(t1)
#     t2 = threading.Thread(target=lj2, args=())
#     threads.append(t2)
#     print('*' * 150)
#     for t in threads:
#         t.start()


# # case8：封庄,封盘并发
# def case8():
#     js(cid, zbuid)
#     order_id = kp(cid, zbuid)
#     zz(cid, order_id, zzuid)
#     time.sleep(2)
#     threads = []
#     t1 = threading.Thread(target=fz, args=(cid, order_id, zzuid))
#     t2 = threading.Thread(target=fp, args=(cid, zbuid))
#     threads.append(t1)
#     threads.append(t2)
#     print('*' * 150)
#     for t in threads:
#         t.start()
#     js(cid, zbuid)


# # case9:下注并发 (大量数据超过坐庄额度)
# def case9():
#     js(cid, zbuid)
#     order_id = kp(cid, zbuid)
#     zz(cid, order_id, zzuid)
#     threads = []
#     for x in range(1, 1000):
#         t1 = threading.Thread(target=xz, args=(cid, zzuid, xzuid, order_id))
#         threads.append(t1)
#     print('*' * 150)
#     for t in threads:
#         t.start()


# # case10：下注,流盘并发
# def case10():
#     js(cid, zbuid)
#     order_id = kp(cid, zbuid)
#     zz(cid, order_id, zzuid)
#     lj1(cid)
#     time.sleep(2)
#     threads = []
#     for i in range(1, 2):
#         t1 = threading.Thread(target=xz, args=(cid, zzuid, xzuid, order_id))
#         threads.append(t1)
#     t2 = threading.Thread(target=lj2, args=())
#     threads.append(t2)
#     print('*' * 150)
#     for t in threads:
#         t.start()
# # case10()

# # case11：流盘并发,不太会发生
# # case12: 结束和流盘并发
# def case12():
#     js(cid, zbuid)
#     order_id = kp(cid, zbuid)
#     zz(cid, order_id, zzuid)
#     xz(cid, zzuid, xzuid, order_id)
#     # lj1(cid)
#     threads = []
#     t1 = threading.Thread(target=js, args=(cid, zbuid))
#     # t2 = threading.Thread(target=lj2, args=())
#     threads.append(t1)
#     # threads.append(t2)
#     print('*' * 150)
#     for t in threads:
#         t.start()
# while  True:
#     case12()
