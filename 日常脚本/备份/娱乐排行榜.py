import threading
import requests
import time
import hashlib
import random
import asyncio
import aiohttp
import time


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


def sl(pos, cid, gift, t_count, url, uid):
    datax = {'msg_type': 'gift',
             'data': 'gift',
             'pos': pos,
             'cid': cid,
             'gift': gift,
             't_count': t_count,
             'msg_send_type': 'gift'}
    aa = requests.get(url + '/chat/sendMsg?',
                      params=datax, cookies=cookies(uid))
    print(aa.text + uid)


# url = 'http://lxy.new.huomaotv.com.cn/member/sendFreeBean'
# url = 'https://lxy.huomao.tv/chat/sendMsg'
url = 'http://cs.lierenjingji.cn/ice/cat_trade.php'
cid = '100'
uid = '1512'

# 普通方式
# for i in range(10, 13):
#     print(sl('1', cid, '8', 1, url, uid))

# 多线程
# threads = []
# for i in range(10, 221):
#     cid = 100
#     uid = str(1412 + i)
#     t = threading.Thread(target=sl, args=('1', cid, '8', 1, url, uid))
#     threads.append(t)

# for t in threads:
#     t.start()

# 协程
NUMBERS = range(1, 2)
# URL = 'https://www.huomao.com/plugs/getCacheTime'
params = {'device': 'pc',
          'id': 1016,
          'user_id': 1006176,
          'user': '',
          'mobile_no': '',
          'ip_addr': '',
          'desc': '50Q币,QQ号码:55',
          'money': 60000,
          'name': '50Q币',
          'timestamp': 1491036230189}

# data1 = {'cid':'3642', 'cuid':'357855'}

# help(aiohttp.request)
cookies1 = dict(JSESSIONID='792C39E03BD03777FA70134DEF60262B')

async def fetch_async(uid):
    async with aiohttp.request('POST', url, data=params, cookies=cookies1) as r:
        data = await r.text()
    return data 



start = time.time()
event_loop = asyncio.get_event_loop()
tasks = [fetch_async(uid) for uid in NUMBERS]
results = event_loop.run_until_complete(asyncio.gather(*tasks))

for uid, result in zip(NUMBERS, results):
    print('fetch({}) = {}'.format(uid, result))

print('Use asyncio+aiohttp cost: {}'.format(time.time() - start))
