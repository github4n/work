import urllib
import urllib.request
import threading
import public
# 主播结束cookie testjc8
cookie1 = public.cookie('343532')
data1 = {'c': 'NewGuess',
         'a': 'closeGuess',
         'cid': 3435,
         'params[0]': 1,
         '_': 1459414035019
         }
# 坐庄 cookie testjc2
cookie2 = public.cookie('343517')
data2 = {'c': 'NewGuess',
         'a': 'banker',
         'choice_title': 222,
         'title': 0,
         'cid': 3435,
         'odds': 1,
         'money_type': 2,
         'order_id': 146008001834353220,
         'money': 1000,
         'choice': 1,
         '_': 1460015127466
         }
# 退庄数据cookie testjc2
cookie4 = public.cookie('343517')
data4 = {'c': 'NewGuess',
         'a': 'backBanker',
         'cid': 3435,                               # 房间号
         'order_id': 146008528734353220,                # 订单号
         'pos': 0,
         'choice': 1,                               # 选项序号
         'index': 2,                                # 仙豆1  猫豆2
         'title': 0,                                # 主题序号
         '_': 1458616231343,
         }

# 下注cookie testjc9
cookie3 = public.cookie('343533')
data3 = {'c': 'NewGuess',
         'a': 'bet',
         'choice_title': '333',
         'title': 0,
         'cid': 3435,
         'banker_uid': 343517,
         'bet_choice': 2,
         'banker_choice': 1,
         'odds': 1,
         'pos': 0,
         'money_type': 2,
         'order_id': 146001987634353220,
         'money': 10,
         'bet_index': 3,
         '_': 1458635932794,
         }


threads = []
for i in range(0, 1):
    t = threading.Thread(target=public.aa, args=(cookie4, data4,))
    threads.append(t)
    y = threading.Thread(target=public.aa, args=(cookie1, data1,))
threads.append(y)


for t in threads:
    # t.setDaemon(True)
    t.start()
