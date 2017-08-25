import pymysql
import urllib.request
import urllib.parse
import hashlib
import time
import json
# 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
uid = 342911
url = 'http://tuyu.huomaotv.com.cn/index.php?c=Dragon&a=achieve_beans'


def headers(uid):
    key = 'HUOMAOTV!@#$%^&*137SECRET'
    uid = str(uid)
    ts = str(time.time())
    a = uid + str(ts) + key
    b = a.encode('utf-8')
    token = str(hashlib.md5(b).hexdigest())
    headers = {'Cookie': 'huomaotvhjhdwq_u_ID=' + uid +
               '; huomaotvhjhdwq_u_token=' + token + '; huomaotvhjhdwq_u_ts=' + ts,
               'Connection': 'keep-alive'}
    return headers


def dwj():
    conn = pymysql.connect(host='192.168.23.11', user='marstv',
                           passwd='marstv123',
                           db='marstv_money_pay', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = "UPDATE  mtv_dw_money_bill SET  is_achieve =  0 WHERE  uid = %s" % uid
    sql1 = "DELETE FROM mtv_dw_money_bill  WHERE  uid = %s and type = 2" % uid
    sql2 = "UPDATE mtv_dw_money_log  SET  two_gear_get = 0 WHERE uid = %s" % uid
    sql3 = "UPDATE mtv_dw_money_log  SET  one_gear_get = 0 WHERE uid = %s" % uid
    sql4 = "UPDATE mtv_dw_money_log  SET  three_gear_get = 0 WHERE uid = %s" % uid
    sql5 = "UPDATE mtv_dw_money_log  SET  four_gear_get = 0 WHERE uid = %s" % uid
    cur.execute(sql)
    cur.execute(sql1)
    cur.execute(sql2)
    cur.execute(sql3)
    cur.execute(sql4)
    cur.execute(sql5)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源

    # res = urllib.request.Request(url, None, headers(342911))
    # data = urllib.request.urlopen(res)
    # data1 = data.read().decode('utf-8')
    # data2 = json.loads(data1[1:-1])
    # #print(data2)
    # return data2['c']['num']
dwj()
# a = b = c = d = 0
# for i in range(0, 100):
#     s = dwj()
#     if s == 369:
#         a += 1
#     elif s == 488:
#         b += 1
#     elif s == 588:
#         c += 1
#     elif s == 666:
#         d += 1
#     e = a + b + c + d
# a = a / e
# b = b / e
# c = c / e
# d = d / e
# print('369'+str(a))
# print('488出现几率'+str(b))
# print('588出现几率'+str(c))
# print('666出现几率'+str(d))
