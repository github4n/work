import requests
import threading
from common import cookies

url = 'http://gml.new.huomaotv.com.cn'
# res = requests.get(url + '/channels/isHaveTreasure?cid=100')
# res = res.json()
# print(res)


def bx(treasure_key, uid):
    res = requests.get(url + '/chat/getUserZcmBean', params={'cid': 100, 'treasure_key': treasure_key}, cookies=cookies(uid))
    res = res.text
    print(res, uid)


threads = []
treasure_key = 'zcm_bean_list@12095_961_14931152583213_1'
for i in range(3181, 3182):#3181
    t = threading.Thread(target=bx, args=(treasure_key, i))
    threads.append(t)


print('*' * 150)
for t in threads:
    t.start()
