import common
import  requests
#
data ={'channel':11,
       'content':'2',
       'notice':'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
       'province':19,
       'city':268,
       'gid':32 }
r = requests.post('http://lxy.new.huomaotv.com.cn/myroom/editRoomInfo',data=data,cookies=common.generate_cookies(1522), headers={'X-Requested-With': 'XMLHttpRequest'})
print(r.text)
