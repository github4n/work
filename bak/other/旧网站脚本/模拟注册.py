import urllib
import http.cookiejar
import time
import pymysql

host = '180.150.179.136'
user = 'qa'
passwd = 'fgd@gG513$FD1'
db1 = 'marstv_www'
db2 = 'marstv_money_pay'
port = 4040
charset = 'utf8'


def regnamef(tv_email):
    cookie = http.cookiejar.CookieJar()
    cjhdr = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cjhdr)
    urllib.request.install_opener(opener)
    url = "http://www.huomaotv.com.cn/index.php?c=ajax&a=new_user_do"
    postdata = urllib.parse.urlencode(
        {'tv_email': tv_email, 'tv_pwd': 'test1234',
         'tv_name': '', 'tv_vcode': 'lxy1',
         'tv_agr': 1, 'state': 'vcode', 'ac': 'username'})
    postdata = postdata.encode('utf-8')
    res = urllib.request.urlopen(url, postdata)
    dict1 = eval(bytes.decode(res.read()))
    if dict1['msg'] == '1':
        print('注册成功')
    else:
        print('注册失败')
    print(cookie)


def jq(testemail):
    conn1 = pymysql.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db1,
        port=port,
        charset=charset)
    cur1 = conn1.cursor()  # 获取一个游标
    cur1.execute(
        "SELECT uid FROM ms_ucenter_members WHERE username = %s", (testemail))
    data = cur1.fetchone()
    uid = data[0]
    print(uid)
    cur1.execute(
        "UPDATE ms_ucenter_members SET mobile = 111 WHERE uid LIKE %s", uid)
    cur1.execute(
        "UPDATE mtv_user_credits_list SET credits_2 = 999999 WHERE uid LIKE %s", uid)
    conn1.commit()  # 提交
    cur1.close()  # 关闭游标
    conn1.close()  # 释放数据库资源
    conn2 = pymysql.connect(
         host=host,
         user=user,
         passwd=passwd,
         db=db2,
         port=port,
         charset=charset)
    cur2 = conn2.cursor()  # 获取一个游标
    cur2.execute(
         "INSERT INTO mtv_money(mid, uid, money_one_total, money_one_get, money_one_pay, money_two_total, money_two_get, money_two_pay, pay_status, status, addtime, updatetime, note) VALUES (NULL, %s, '0.00', '99999999', '1097.20', '22237360', '99999999', '10000', '1', '1', '1436968570', '1449125447', '减少M币')", uid)
    conn2.commit()  # 提交
    cur2.close()  # 关闭游标
    conn2.close()  # 释放数据库资源

name = 'test' + str(int(time.time()))
# name = 'testjc12'
print(name)
regnamef(name)

# jq(name)
'''
UPDATE  `marstv_www`.`ms_ucenter_members` SET  `mobile` =  '666' WHERE  `ms_ucenter_members`.`uid` =343537;
INSERT INTO `marstv_money_pay`.`mtv_money` (`mid`, `uid`, `money_one_total`, `money_one_get`, `money_one_pay`, `money_two_total`, `money_two_get`, `money_two_pay`, `pay_status`, `status`, `addtime`, `updatetime`, `note`) VALUES (NULL, '343537', '0', '10000', '0', '0', '10000', '0', '1', '1', '1436968570', '1449125447', '减少M币');
UPDATE  `marstv_www`.`mtv_user_credits_list` SET  `credits_2` =  '500000' WHERE  `mtv_user_credits_list`.`uid` =343537;
'''