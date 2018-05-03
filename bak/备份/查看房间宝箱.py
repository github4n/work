import requests
import threading
# from common import cookies

url = 'http://gml.new.huomaotv.com.cn'
res = requests.get(url + '/channels/isHaveTreasure?cid=100')
res = res.json()
print(res)
