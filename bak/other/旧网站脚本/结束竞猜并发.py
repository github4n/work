import urllib
import urllib.request
import threading
import public

# 结束竞猜uid
cookie1 = public.cookie('343518')
data1 = {'c': 'NewGuess',
         'a': 'closeGuess',
         'cid': 3435,
         'params[0]': 1,
         '_': 1458616231343,
         }


cookie2 = public.cookie('343536')
data2 = {'c': 'NewGuess',
         'a': 'banker',
         'choice_title': 111,
         'title': 0,
         'cid': 3435,
         'odds': 1,
         'money_type': 2,
         'order_id': 145870451734353210,
         'money': 1000,
         'choice': 1,
         '_': 1458701495645
         }
         

threads = []

for i in range(0, 1):
    t = threading.Thread(target=public.aa, args=(cookie2, data2,))
    threads.append(t)
y = threading.Thread(target=public.aa, args=(cookie1, data1,))
threads.append(y)
for t in threads:
    # t.setDaemon(True)
    t.start()
