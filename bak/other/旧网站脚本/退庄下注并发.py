import urllib
import urllib.request
import threading
import public
import time
# subject_guess_banker_list_3435_145941102134353220' . $cid . '_' . $order_id . '_' . $type;
# 下注cookie testjc9
cookie1 = public.cookie('343533')
# 退庄cookie testjc2
cookie2 = public.cookie('343517')
# 下注数据
data1 = {'c': 'NewGuess',
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
         'order_id': 146001376434353220,
         'money': 10,
         'bet_index': 3,
         '_': 1458635932794,
         }
# 退庄数据
data2 = {'c': 'NewGuess',
         'a': 'backBanker',
         'cid': 3435,								# 房间号
         'order_id': 146001376434353220,				# 订单号
         'pos': 0,
         'choice': 1,								# 选项序号
         'index': 2,								# 仙豆1  猫豆2
         'title': 0,  								# 主题序号
         '_': 1458616231343,
         }
# 多线程并发
# threads = []
# for i in range(0, 10):
#     t = threading.Thread(target=public.aa, args=(cookie1, data1,))
#     threads.append(t)
# # 退庄
# y = threading.Thread(target=public.aa, args=(cookie2, data2,))
# threads.append(y)

# for t in threads:
#     # t.setDaemon(True)
#     t.start()
public.aa(cookie1, data1,)
time.sleep(1)
public.aa(cookie2, data2,)
