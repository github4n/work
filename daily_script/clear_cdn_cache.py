import requests

cookies = {'huomaotvcheckcode': 'LR6A', 'adminId': '7', 'adminAccount': 'lxy',
           'adminNick': '%E6%9D%8E%E5%B9%B8%E8%BF%90', 'adminUserId': '1870709',
           'adminLoginTime': '1474620118', 'adminToken': 'deab64750163288434cccfa4f5229ef1'}

# 清除缓存
urls = ['/static/web/smallgame/images/farm/history/bbet' + str(i) + '.png' for i in range(1, 20)]

for url in urls:
    url = 'https://www.huomao.com/' + url
    res = requests.post('http://bii3c.huomao.com/cachemanage/clearCdnCache', cookies=cookies, data={'url': url})
    res = res.json()
    print(res, url)
    requests.get(url)
