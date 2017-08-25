import urllib
import http.cookiejar
from lxml import etree

url = 'www.huomaotv.com.cn'


def htsqzb():
    def make_cookie(name, value):
        return http.cookiejar.Cookie(
            version=0,
            name=name,
            value=value,
            port=None,
            port_specified=False,
            domain="www.huomaotv.com.cn",
            domain_specified=True,
            domain_initial_dot=False,
            path="/",
            path_specified=True,
            secure=False,
            expires=None,
            discard=False,
            comment=None,
            comment_url=None,
            rest=None
        )
    # 声明一个CookieJar对象实例来保存cookie a0hp22opqu2k954vbkp34ullo2
    cookie = http.cookiejar.CookieJar()
    cookie.set_cookie(make_cookie("PHPSESSID", 'qfq1m43mpbk1nh2sagjb8pphp6'))
    cjhdr = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cjhdr)
    urllib.request.install_opener(opener)
    url2 = "http://" + url + "/admin33/umember/zhubo.php?act=lists"
    res2 = urllib.request.urlopen(url2)
    content = bytes.decode(res2.read())
    tree = etree.HTML(content)
    hyperlinks = tree.xpath(u'//*[@class="tb_list"][1]/td[1]')
    id = hyperlinks[0].text
    url1 = "http://" + url + "/admin33/umember/zhubo.php?act=edit"
    postdata = urllib.parse.urlencode(
        {'id': id, 'act': 'change', 'status': '1'})
    postdata = postdata.encode('utf-8')
    res = urllib.request.urlopen(url1, postdata)


def login(url, username, password):
    url1 = 'http://' + url + '/index.php?c=ajax&a=user_do'
    postdata1 = urllib.parse.urlencode(
        {'username': username, 'password': password, 'vcode': 'lxy1',
         'state': 'from', 'remember': '1', 'ac': 'login'})
    postdata1 = postdata1.encode('utf-8')
    res1 = urllib.request.urlopen(url1, postdata1)



def sqzb(url, username, password):
    cookie = http.cookiejar.CookieJar()
    cjhdr = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cjhdr)
    urllib.request.install_opener(opener)
    login(url, username, password)
    url2 = 'http://' + url + '/managent/live_apply_add'
    postdata2 = urllib.parse.urlencode(
        {'true_name': '1', 'sex': '1', 'cred': '1', 'id_card': '1', 'card_pic': '/upload/idcard_img/2016-01-18/569ca78fe1f42.png', 'phone': 111, 'yzm': '验证码', 'qq': '1', 'gid': '23'})
    postdata2 = postdata2.encode('utf-8')
    res2 = urllib.request.urlopen(url2, postdata2)
    print(res2)


sqzb(url,'testjc8','test1234')
htsqzb()
