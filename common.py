# -*- coding:utf-8 -*-
import time
import pymysql
import hashlib
import requests
import redis
import json
from lxml import etree


# 网站url
url = 'http://qa.new.huomaotv.com.cn'
url_api = 'http://qaapi.new.huomaotv.com.cn'
domain = '.huomaotv.com.cn'
# url = 'http://www.huomao.com'
# 后台url
adminurl = 'http://qaadmin.new.huomaotv.com.cn'
# 后台cookies
cookiesadmin = {'huomaotvcheckcode': 'SQJ5', 'adminId': '33',
                'adminAccount': 'root', 'adminNick': 'root',
                'adminUserId': '0', 'adminLoginTime': '1473220408',
                'adminToken': 'bd2c21cb89ada618b16170504ad9f84d'}
# 线上后台cookies
cookiesadmin_online = {'huomaotvcheckcode': 'LR6A', 'adminId': '7', 'adminAccount': 'lxy',
                       'adminNick': '%E6%9D%8E%E5%B9%B8%E8%BF%90', 'adminUserId': '1870709',
                       'adminLoginTime': '1474620118', 'adminToken': 'deab64750163288434cccfa4f5229ef1'}

# 用户默认密码
userpwd = '1'
# 全局数据库参数设置
host = 'db.huomaotv.com.cn'
user = 'root'
passwd = '123456'
# db = 'hm_money',
port = 3306
redisport = 6379
charset = 'utf8'
redis_inst = redis.Redis(host=host, port=redisport, db=0, decode_responses=True)
mysql_inst = pymysql.connect(host=host, user=user, passwd=passwd, port=port, charset=charset)


# res = redis_inst.get('hm_qixi_active_sign:1522')
# print(res)
# sign = json.loads(res)
# sign['signInfo']={"20170820":True,"20170819":True,"20170818":True,"20170817":True,"20170821":True,"20170822":True}
# sign['continuitySign']=6
# # sign['continue_three'] = 'open'
# redis_inst.set('hm_qixi_active_sign:1522',json.dumps(sign))
# for key in redis_inst.keys('*seed*'):
#     redis_inst.delete(key)

# 分表参数查询
def hash_table(s, num=32):
    s = ('hm_db_' + str(s)).encode('utf-8')
    m = hashlib.md5()
    m.update(s)
    md5s = m.hexdigest()
    md5ss = int(md5s[1:3], 16) % num
    return str(md5ss)
# print(hash_table('1282'))

# 用户cookie生成


def generate_cookies(uid):
    if uid:
        key = 'HUOMAOTV!@#$%^&*137SECRET'
        uid = str(uid)
        ts = str(int(time.time()))
        a = uid + str(ts) + key
        b = a.encode('utf-8')
        token = str(hashlib.md5(b).hexdigest())
        cookies = {'user_e100fe70f5705b56db66da43c140237c': uid,
                   'user_6b90717037ae096e2f345fde0c31e11b': token,
                   'user_2c691ee7b8307f7fadc5c2c9349dbd7b': ts}
        return cookies
    else:
        return {}


# 输入uid或用户名返回uid
def find_uid(name):
    if name is None:
        return False
    elif name.isdigit():
        return name
    else:
        tablname = 'username_' + hash_table(name)
        conn = pymysql.connect(host=host, user=user, passwd=passwd, db='hm_user', port=port, charset=charset)
        cur = conn.cursor()
        sql = "SELECT uid FROM %s WHERE username = '%s'" % (tablname, name)
        cur.execute(sql)
        data = cur.fetchone()
        if data:
            return data[0]
        else:
            return False
        conn.close()


# 设置仙豆
def set_xd(uid, xd):
    xd = 0 if not xd else int(xd)
    uid = str(uid)
    r = redis.Redis(host=host, port=redisport, db=0, decode_responses=True)
    r.set('hm_free_bean_' + uid, xd)
    return True


# 设置用户猫币猫豆
def set_money(uid, num1, num2):
    uid = str(str(uid))
    num1 = 0 if not num1 else num1
    num2 = 0 if not num2 else num2
    num1 = float(num1)
    num2 = float(num2)
    tablname = 'money_' + hash_table(uid)
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db='hm_money', port=port, charset=charset)
    cur = conn.cursor()  # 获取一个游标
    sql = "SELECT * FROM %s WHERE uid = %s" % (tablname, uid)
    cur.execute(sql)
    data = cur.fetchone()
    # 判断用户是否存在记录，存在则修改，否则插入数据
    if data:
        sql1 = "SELECT coin,bean FROM %s WHERE uid = %s" % (tablname, uid)
        cur.execute(sql1)
        data = cur.fetchone()
        # sql2 = "UPDATE  %s SET  coin =  %s, bean =  %s WHERE  uid = %s" % (tablname, num1 + float(data[0]), num2 + float(data[0]), uid)
        sql2 = "UPDATE  %s SET  coin =  %s, bean =  %s WHERE  uid = %s" % (tablname, num1, num2, uid)
        cur.execute(sql2)
    else:
        ts = int(time.time())
        sql3 = "INSERT INTO  %s(uid,coin,bean,ts) values(%s,%s,%s,%s)" % (tablname, uid, num1, num2, ts)
        cur.execute(sql3)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源

set_money(1523, 999999, 999999)

# 绑定手机号
def bd_sj(uid):
    url1 = url + '/test/uum/' + str(uid) + '/' + str(15800000000 + int(uid))
    r = requests.get(url1, cookies=generate_cookies(uid))
    if r.status_code == 200:
        return True
    else:
        return False


# 注册用户返回uid,或登录返回uid
def zc(username):
    r = requests.post(url + '/user/lucky_reg', data={'nick_name': username + 'nc', 'user_pwd': userpwd, 'username': username, 'key': 'huomao_lucky'})
    if r.json()['code'] != '100':
        return False
    else:
        return r.json()['data']['uid']


# 申请直播并通过
def sq_zb(uid):
    # 判断uid是否是主播
    if uid:
        uid = str(uid)
        r = requests.get(url + '/member/checkUsersIdentify', cookies=generate_cookies(uid))
        if r.json()['data']['isAnchor'] is True:
            return False
        else:
            bd_sj(uid)
            time.sleep(1)
            data = {'true_name': '测试号',
                    'sex': '1',
                    'gid': '97',
                    'cred': '4',
                    'card_code': '100' + uid,
                    'card_pic': 'http://img.new.huomaotv.com.cn/upload/web/images/defaultimgs/0dc10ab4d7bda309e3095298ca689573/20160907110242mnxsySdt.png',
                    'qq': '100' + uid,
                    'agreement': '1'}
            r = requests.post(url + '/anchor/submitApply', data=data, cookies=generate_cookies(uid), headers={'X-Requested-With': 'XMLHttpRequest'})
            r = requests.get(adminurl + '/anchor/lists', params={'field': 'uid', 'keyword': uid}, cookies=cookiesadmin)
            uidid = etree.HTML(r.text).xpath('//tr[2]/td[1]')[0].text
            r = requests.post(adminurl + '/index.php/anchor/submitVerify', data={'status': '1', 'is_push': '1', 'reason': '', 'id': uidid}, cookies=cookiesadmin)
            return True
    else:
        return False


# 更新流
def update_stream(room_number_online, room_number_offine):
    # 返回线上流dict
    if room_number_online and room_number_offine:
        res = requests.get('http://bii3c.huomao.com/outlink/stream', cookies=cookiesadmin_online)
        contentTree = etree.HTML(res.text)
        lennum = contentTree.xpath('//tr')
        streamdict = {}
        for i in range(2, len(lennum) + 1):
            i = str(i)
            room_number = contentTree.xpath('//tr[' + i + ']/td[1]/a/text()')
            stream = contentTree.xpath(u'//tr[' + i + ']/td[3]/a/text()')
            streamdict[room_number[0]] = stream[0]
        # 修改线下库和redis
        try:
            stream = streamdict[str(room_number_online)]
        except:
            return {'code': 2, 'msg': '线上房间流未直播或房间存在'}
        conn = pymysql.connect(host=host, user='root',
                               passwd='123456',
                               db='hm_contents', port=3306, charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        r = redis.Redis(host=host, port=6379, db=0)
        cur.execute("UPDATE  hm_channel SET  stream = %s WHERE room_number = %s", (stream, room_number_offine))
        cur.execute("SELECT uid from hm_channel  WHERE room_number = %s", room_number_offine)
        data = cur.fetchone()
        r.hset('hm_channel_anchor_' + str(data[0]), 'stream', '"' + stream + '"')
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return {'code': 0, 'msg': '成功'}
    else:
        return {'code': 1, 'msg': '请输入房间号'}


def phone_fy(cid, data, uid):
    if cid and data and uid:
        data = {'cid': cid,
                'data': data,
                # 'msg_level': 'channel',
                # 'msg_send_type': 'msg',
                # 'msg_type': 'msg',
                'uid': uid,
                }
        res = requests.post(url_api + '/user/sendmsg', data=data)
        if res.json()['code'] == 200:
            return True
        else:
            return False
    else:
        return False


def phone_sl(cid, uid, t_count, pos, gift):
    if cid and uid and t_count and pos and gift:
        data = {'cid': cid,
                # 'msg_level': 'channel',
                # 'an': '91',
                'msg_type': 'gift',
                'uid': uid,
                't_count': t_count,
                'pos': pos,
                'gift': gift,
                # 'data': 'gift',
                # 'ver': '1000',
                # 'time': '1494915960',
                # 'refer': 'ios',
                # 'pf_ver': '10.3.1',
                # 'mp_openid': '30322db7b86a97e3955eb6185fadfd16',
                # 'fr': 'applestore',
                # 'expires_time': '1494906790',
                # 'access_token': 'dd40e45af533f3d26d3b0c6ae42d983d',
                # 'token': '8e4b87a4d40bf03fd93a4a1135c11dc5'
                }
        print(data)
        res = requests.get(url_api + '/user/sendGift', params=data)
        print(res.json())
        if res.json()['code'] == 200:
            return True
        else:
            return False
    else:
        return False


def phone_sd(cid, uid):
    if cid and uid:
        data = {'cid': cid,
                'cuid': 1,
                'freebean_num': '10',
                'uid': uid,
                }
        res = requests.post(url_api + '/user/sendFreeBean', data=data)
        if res.json()['code'] == '110':
            return True
        else:
            return False
    else:
        return False


def updatestat(cids, stat):
    if cids and stat:
        cids = str(cids)
        cids = cids.split(",")
        for cid in cids:
            if cid:
                data = {'is_live': stat,
                        'cid': cids,
                        }
                requests.get(url + '/plugs/updateRoomLiveStat', params=data)
        return True
    else:
        return False


# 修改密码
def update_password(uid, password):
    uid = str(uid)
    m = hashlib.md5()
    m.update(str(password).encode('utf-8'))
    newpassword = m.hexdigest()
    tablname = 'userinfo_' + hash_table(uid)
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db='hm_user', port=port, charset=charset)
    cur = conn.cursor()  # 获取一个游标
    sql = "UPDATE {} SET password = '{}' WHERE uid = {}".format(tablname, newpassword, uid)
    cur.execute(sql)
    conn.commit()
    r = redis.Redis(host=host, port=redisport, db=0, decode_responses=True)
    data = json.loads(r.get('hm_' + uid))
    data['password'] = newpassword
    r.set('hm_' + uid, json.dumps(data))


# 修改房间类型0普通，1横板娱乐，2竖版娱乐
def update_roomlx(room_number, status):
    r = redis.Redis(host=host, port=redisport, db=0, decode_responses=True)
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db='hm_contents', port=port, charset=charset)
    cur = conn.cursor()  # 获取一个游标
    cur.execute("SELECT uid,id from hm_channel  WHERE room_number = %s", room_number)
    data = cur.fetchone()
    uid = data[0]
    cid = data[1]
    if status == 0:
        sql = "UPDATE hm_channel SET is_entertainment='{}' WHERE room_number = {}".format('no', room_number)
        cur.execute(sql)
        conn.commit()
        r.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('no'))
        return True
    elif status == 1:
        sql = "UPDATE hm_channel SET is_entertainment='{}' WHERE room_number = {}".format('yes', room_number)
        cur.execute(sql)
        conn.commit()
        r.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('yes'))
        r.set('hm_pushstream_type_{}'.format(cid), 1)  # 2手机 1PC
        return True
    elif status == 2:
        sql = "UPDATE hm_channel SET is_entertainment='{}' WHERE room_number = {}".format('yes', room_number)
        cur.execute(sql)
        conn.commit()
        r.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('yes'))
        r.set('hm_pushstream_type_{}'.format(cid), 2)  # 2手机 1PC
        r.set('hm_mobile_screenType_outdoor_{}'.format(cid), 2)  # 2竖屏 1横屏
        return True
    else:
        return False
