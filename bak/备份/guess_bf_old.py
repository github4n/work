import gevent
from gevent import monkey
from multiprocessing import Process
import multiprocessing
monkey.patch_all()
import time
import requests
import grequests
import hashlib
import json
import sys
from  urllib import parse
sys.path.append('../')
from huomao.common import Common

common = Common()

# 默认房间号1，选择主题1，默认仙豆1，坐庄额度1000仙豆，下注额度10，退庄序号pos1，竞猜序号0，选择选项1，赔率默认1,流局默认1
cid = '2'  # 是房间主键
zbuid = '1522'
zzuid = '3866'
xzuid = '3865'
url = 'http://qa.new.huomaotv.com.cn'
s = requests.Session()

# 开盘
def open_guess(cid, uid):
    data = {'cid': cid,
            'first[title]': '测试主题1' + str(int(time.time())),
            'first[choice_1]': '测试主题1选项1',
            'first[choice_2]': '测试主题1选项2',
            'first[type]': '1',
            'second[title]': '测试主题2' + str(int(time.time())),
            'second[choice_1]': '测试主题2选项1',
            'second[choice_2]': '测试主题2选项2',
            'second[type]': '1',
            'third[title]': '测试主题3' + str(int(time.time())),
            'third[choice_1]': '测试主题3选项1',
            'third[choice_2]': '测试主题3选项2',
            'third[type]': '1'}
    res = requests.get(url + '/guess/setGuessSubject', data, cookies=common.generate_cookies(uid))
    data = res.json()
    print('开盘****************:{}'.format(data))
    # 返回订单号
    return data['data']['1']['xd']


# 结束盘口。num序号0，1，2，choice选项1，2. 退庄是3.
def close_guess(cid, uid, choice1='', choice2='', choice3=''):
    data = {'params[0]': choice1,
            'params[1]': choice2,
            'params[2]': choice3,
            'cid': cid}
    res = requests.get(url + '/Guess/setCloseGuess', params=data, cookies=common.generate_cookies(uid))
    print('结束****************:{}'.format(res.json()))


# 坐庄
def banker(cid, order_id, uid, odds='1'):
    data = {'choice_name': '测试主题1选项1',  # 选项名
            'title': '0',  # 竞猜序号
            'cid': cid,  # 房间号
            'odds': odds,  # 赔率
            'money_type': '1',  # 1仙豆 2猫豆
            'order_id': order_id,  # 订单号
            'money': '200',  # 坐庄金额
            'choice': '1'}  # 选项序号
    res = requests.get(url + '/guess/banker', params=data, cookies=common.generate_cookies(uid))
    print('坐庄****************:{}'.format(res.json()))


# 封庄
def back_banker(cid, order_id, uid):
    data = {'title': '0',  # 竞猜序号
            'cid': cid,  # 房间号
            'pos': '1',  # 庄序号
            'money_type': '1',  # 1仙豆 2猫豆
            'order_id': order_id,  # 订单号
            'choice': '1'}  # 选项序号
    res = requests.get(url + '/Guess/backBanker', params=data, cookies=common.generate_cookies(uid))
    print(res.json())


# 下注
def bet(cid, zzuid, xzuid, order_id):
    data = {'choice_title': '测试主题1选项1',  # 选项名
            'title': '0',  # 竞猜序号
            'cid': cid,  # 房间号
            'banker_uid': zzuid,  # 坐庄uid
            'bet_choice': '1',  # 下注选项
            'banker_choice': '1',  # 坐庄选项
            'odds': '1',  # 赔率
            'pos': '0',
            'money_type': '1',  # 1仙豆 2猫豆
            'order_id': order_id,
            'money': '10',  # 下注额
            'bet_index': '3',
            'order_flag': 'false'}  # 选项序号
    # print(parse.urlencode(data))
    # res = requests.get(url + '/Guess/bet', params=data, cookies=huomao.generate_cookies(xzuid))
    s.get('http://qa.new.huomaotv.com.cn/plugs/getCacheTime')
    # print('下注****************:{}'.format(res.json()))



# 下注
def bet2(cid, zzuid, xzuid, order_id):
    data = {'choice_title': '测试主题1选项1',  # 选项名
            'title': '0',  # 竞猜序号
            'cid': cid,  # 房间号
            'banker_uid': zzuid,  # 坐庄uid
            'bet_choice': '1',  # 下注选项
            'banker_choice': '1',  # 坐庄选项
            'odds': '1',  # 赔率
            'pos': '0',
            'money_type': '1',  # 1仙豆 2猫豆
            'order_id': order_id,
            'money': '10',  # 下注额
            'bet_index': '3',
            'order_flag': 'false'}  # 选项序号
    # print(parse.urlencode(data))
    return grequests.get('http://qa.new.huomaotv.com.cn/plugs/getCacheTime')
    # print('下注****************:{}'.format(res.json()))





# 流局
def lj():
    res = requests.get(url + '/guess/timeoutEndGuess')
    print(res.text)


# close_guess(cid, zbuid, '2', '2', '2')
# exit()


# close_guess(cid, zbuid, '1', '1', '1')
# bet(cid, zzuid, xzuid, order_id)

order_id = 1511761916152210
# print(order_id)
# banker(cid, order_id, zzuid, odds='1')
def test1(order_id=order_id):
    events = []
    for i in range(0, 200):
        events.append(gevent.spawn(bet, cid, zzuid, xzuid, order_id))
    gevent.joinall(events)


t1 = time.time()
test1()
print((time.time() - t1))

# t1 = time.time()
# tasks = []
# for i in range(0, 4000):
#     res = bet2(cid, zzuid, xzuid, order_id)
#     tasks.append(res)
# # print((time.time() - t1))
# res = grequests.map(tasks)
# print((time.time() - t1))
# for i in res:
#     print(json.loads(i._content.decode()))



# if __name__ == '__main__':
#     t1 = time.time()
#     order_id = open_guess(cid, zbuid)
#     banker(cid, order_id, zzuid, odds='1')
#     for i in range(0, 8):
#         print(i)
#         p = Process(target=test1, args=(order_id,))
#         # p.daemon = True
#         p.start()
#         p.join()
#     # pool = multiprocessing.Pool(processes=2)
#     # for i in range(0, 2):
#     #     pool.apply_async(test1,(order_id,))
#     # pool.close()
#     # pool.join()
#     print(time.time() - t1)
# # 流局修改redis和请求
# def lj1(cid):
#     r = redis.Redis(host='192.168.23.14', port=6379, db=0)
#     data = r.get('hm_subject_guess_' + cid)
#     data1 = data.decode('utf-8')
#     data2 = json.loads(data1)
#     data3 = int(data2[0]['addtime'])
#     data2[0]['addtime'] = str(data3 - 21800)
#     r.set('hm_subject_guess_' + cid, json.dumps(data2))


# case1:结束，坐庄并发
# case2：结束，封庄并发
# case3：结束，下注并发**************************
# case4:结束并发
# case5:坐庄，流盘并发 暂时却流盘redis逻辑
# case6:封庄并发
# case7:封庄,流盘并发 暂时却流盘redis逻辑
# case8：封庄,封盘并发
# case9:下注并发 (大量数据超过坐庄额度)
# case10：下注,流盘并发
# case11：流盘并发,不太会发生
# case12: 结束和流盘并发
