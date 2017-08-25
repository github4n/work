from gevent import monkey
monkey.patch_all()
import gevent
import requests
import time
import threading
import asyncio
import random
import aiohttp
from common import generate_cookies, set_money

a = 0
n = 0
m = 0
def generate_fun(fun_type=False):
    async def request_async(url, data={}, uid=False):
        async with aiohttp.request('GET', url, params=data, cookies=generate_cookies(uid)) as response:
            try:
                res = await response.json()
                print(res)
            except Exception as e:
                pass

    def request(url, data={}, uid=False):
        res = requests.get(url, params=data, cookies=generate_cookies(uid))
        try:
            print(res.json())
        except:
            print(res.text)
    if fun_type:
        return request_async
    else:
        return request


def run(run_type, f, uids, url, data={}):
    start = time.time()
    if run_type == 'gevent':
        events = [gevent.spawn(f, url, data, uid) for uid in uids]
        gevent.joinall(events)
    elif run_type == 'async':
        event_loop = asyncio.get_event_loop()
        tasks = [f(url, data, uid) for uid in uids]
        event_loop.run_until_complete(asyncio.gather(*tasks))
    elif run_type == 'thread':
        threads = []
        for uid in uids:
            threads.append(threading.Thread(target=f, args=(url, data, uid,)))
        for t in threads:
            t.setDaemon(True)
            t.start()
        for t in threads:
            t.join()
    print('耗时: {}'.format(time.time() - start))


domain = 'http://lxy.new.huomaotv.com.cn'
ti7_url = '/ti7/seckill?time=1501469340'
gift_url = '/chatnew/sendGift'
gift_data = {'msg_type': 'gift',
             'data': 'gift',
             'pos': 1,
             'cid': 15,
             'gift': 5,
             't_count': 1,
             'msg_send_type': 'gift'}
msg_url = '/chatnew/msg'
msg_data = {'data': '测试弹幕',
            'cid': 2,
            'color_barrage': 1,
            'guard_barrage': '',
            'isAdminPrivateChat': ''}


uids = range(5253, 5263)
# uids = [1522]*200
url = domain + gift_url
# url = 'http://wanjn.new.huomaotv.com.cn/abcdef/abcdef.json?cur_page=web_channeldetailnew&cid=985'
data = gift_data
# for uid in uids:
#     set_money(uid, 999999, 999999)
# exit()

cids = [x for x in range(10, 21)] + [2]
# cids = [29]
for cid in cids:
    gifts = [7,8]
    data['cid'] = cid #random.choice(cids)
    data['gift'] =random.choice(gifts)
    run('gevent', generate_fun(), uids, url, data)
# while True:
#     run('gevent', generate_fun(), uids, url, data)
#     time.sleep(10)
    # time.sleep(2)
# run('async', generate_fun(True), uids, url, data)
# run('thread', generate_fun(), uids, url, data)
