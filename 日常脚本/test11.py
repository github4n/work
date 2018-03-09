import requests
import gevent
from gevent import monkey
monkey.patch_all()
from common.common import Common

data = {
    'type':2,
    'day':0,
}
def test():
    res = requests.get('http://lxy.new.huomaotv.com.cn/active_file/Springfestival/userClickRegister',params=data,cookies=Common.generate_cookies(5726))
    print(res.json())


events = [gevent.spawn(test) for i in range(400)]
gevent.joinall(events)