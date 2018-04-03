import requests
import gevent
from gevent import monkey

monkey.patch_all()
from common.common import Common



def test():
    res = requests.get('http://lxy.new.huomaotv.com.cn/chatnew/sendGift?cid=119396&gift=18&t_count=99&isbag=1', cookies=Common.generate_cookies(5702))
    try:
        print(res.json())
    except:
        print(res.text)


events = [gevent.spawn(test) for i in range(50)]
gevent.joinall(events)