#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 10:49:33
# @Author  : lixingyun
# 注册用户返回uid,或登录返回uid
import time
import pymysql
import hashlib
import requests
import redis
import json
import logging
from lxml import etree

# 网站url
URL = 'http://qa.new.huomaotv.com.cn'
URL_API = 'http://qaapi.new.huomaotv.com.cn'
DOMAIN = '.huomaotv.com.cn'
# 后台url
ADMIN_URL = 'http://qaadmin.new.huomaotv.com.cn'
# 后台cookies
ADMIN_COOKIES = {'huomaotvcheckcode': 'SQJ5', 'adminId': '33','adminAccount': 'root', 'adminNick': 'root','adminUserId': '0', 'adminLoginTime': '1473220408','adminToken': 'bd2c21cb89ada618b16170504ad9f84d'}
# 线上后台cookies
ADMIN_COOKIES_ONLINE = {'huomaotvcheckcode': 'LR6A', 'adminId': '7', 'adminAccount': 'lxy','adminNick': '%E6%9D%8E%E5%B9%B8%E8%BF%90', 'adminUserId': '1870709','adminLoginTime': '1474620118', 'adminToken': 'deab64750163288434cccfa4f5229ef1'}
# 用户默认密码
userpwd = '1'
# 数据库配置
DB_HOST = 'db.huomaotv.com.cn'
DB_USER = 'root'
DB_PASSWD = '123456'
DB_PORT = 3306
# redis配置
REDIS_HOST = 'db.huomaotv.com.cn'
REDIS_PORT = 6379
# 数据库连接
MYSQL_INST = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, port=DB_PORT, charset='utf8')
# redis连接
REDIS_INST = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

# 分表参数查询
def hash_table(s, num=32):
    s = ('hm_db_{}'.format(s)).encode('utf-8')
    m = hashlib.md5()
    m.update(s)
    md5s = m.hexdigest()
    md5ss = int(md5s[1:3], 16) % num
    return str(md5ss)


#用户cookie生成
def generate_cookies(uid):
    if uid:
        key = 'HUOMAOTV!@#$%^&*137SECRET'
        uid = str(uid)
        ts = str(int(time.time()))
        b = (uid + ts + key).encode('utf-8')
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
        mysql_inst.select_db('hm_user')
        cur = mysql_inst.cursor()
        sql = "SELECT uid FROM %s WHERE username = '%s'" % (tablname, name)
        cur.execute(sql)
        data = cur.fetchone()
        cur.close()
        if data:
            return data[0]
        else:
            return False


# 设置仙豆
def set_xd(uid, xd):
    xd = 0 if not xd else int(xd)
    uid = str(uid)
    r.set('hm_free_bean_' + uid, xd)
    return True


# 获取仙豆
def get_xd(uid):
    res = r.get('hm_free_bean_{}'.format(uid))
    return res


# 设置用户猫币猫豆
def set_money(uid, num1=0, num2=0):
    uid = str(uid)
    tablname = 'money_' + hash_table(uid)
    mysql_inst.select_db('hm_money')
    cur = mysql_inst.cursor()  # 获取一个游标
    sql = "SELECT coin,bean FROM %s WHERE uid = %s" % (tablname, uid)
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
    mysql_inst.commit()
    cur.close()  # 关闭游标


# 获取用户余额
def get_money(uid, type='coin'):
    uid = str(uid)
    tablname = 'money_' + hash_table(uid)
    mysql_inst.select_db('hm_money')
    cur = mysql_inst.cursor()  # 获取一个游标
    sql = "SELECT coin,bean FROM %s WHERE uid = %s" % (tablname, uid)
    cur.execute(sql)
    data = cur.fetchone()
    cur.close()
    if data:
        if type=='coin':
            return data[0]
        else:
            return data[1]
    else:
        return False


# 添加弹幕卡
def add_dmk(uid, add_time=int(time.time()), expire_time=int(time.time()) + 10000, num=1):
    mysql_inst.select_db('hm_user_bag')
    cur = mysql_inst.cursor()
    sql = "INSERT INTO  user_bag_{} values(NULL,{},'{}',{},{},{},{},{},{})".format(hash_table(uid), uid, 'admin_33', 100001, add_time, expire_time,
                                                                                   num, 2, num)
    cur.execute(sql)
    mysql_inst.commit()
    cur.close()


# 获取弹幕卡
def get_dmk(uid):
    mysql_inst.select_db('hm_user_bag')
    cur = mysql_inst.cursor()
    sql = "SELECT sum(num) FROM user_bag_{} WHERE uid={} and expire_time >{}".format(hash_table(uid), uid, int(time.time()))
    cur.execute(sql)
    mysql_inst.commit()
    data = cur.fetchone()[0]  # cur.fetchall()
    cur.close()
    return data


# 删除弹幕卡
def del_dmk(uid):
    mysql_inst.select_db('hm_user_bag')
    cur = mysql_inst.cursor()
    sql = "DELETE FROM user_bag_{} WHERE uid={}".format(hash_table(uid), uid)
    cur.execute(sql)
    mysql_inst.commit()
    cur.close()


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
    r = requests.post(url + '/user/lucky_reg',
                      data={'nick_name': username, 'user_pwd': userpwd, 'username': username, 'key': 'huomao_lucky'})
    if r.json()['code'] != '100':
        return False
    else:
        return r.json()['data']['uid']


# 申请直播并通过
def sq_zb(uid):
    # 判断uid是否是主播
    if uid:
        uid = str(uid)
        res = requests.get(url + '/member/checkUsersIdentify', cookies=generate_cookies(uid))
        if res.json()['data']['isAnchor'] is True:
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
            res = requests.post(url + '/anchor/submitApply', data=data, cookies=generate_cookies(uid),
                              headers={'X-Requested-With': 'XMLHttpRequest'})
            res = requests.get(adminurl + '/anchor/lists', params={'field': 'uid', 'keyword': uid}, cookies=cookiesadmin)
            uidid = etree.HTML(res.text).xpath('//tr[2]/td[1]')[0].text
            res = requests.post(adminurl + '/index.php/anchor/submitVerify',
                              data={'status': '1', 'is_push': '1', 'reason': '', 'id': uidid}, cookies=cookiesadmin)
            mysql_inst.select_db('hm_contents')
            cur = mysql_inst.cursor()
            sql = "SELECT id,room_number FROM hm_channel WHERE uid = '%s'" % (uid)
            cur.execute(sql)
            data = cur.fetchone()
            cur.close()
            mysql_inst.commit()
            return data
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
    cur = mysql_inst.cursor()  # 获取一个游标
    sql = "UPDATE {} SET password = '{}' WHERE uid = {}".format(tablname, newpassword, uid)
    cur.execute(sql)
    mysql_inst.commit()
    data = json.loads(r.get('hm_' + uid))
    data['password'] = newpassword
    r.set('hm_' + uid, json.dumps(data))


# 修改房间类型0普通，1横板娱乐，2竖版娱乐
def update_roomlx(room_number, status):
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db='hm_contents', port=port, charset=charset)
    cur = mysql_inst.cursor()  # 获取一个游标
    cur.execute("SELECT uid,id from hm_channel  WHERE room_number = %s", room_number)
    data = cur.fetchone()
    uid = data[0]
    cid = data[1]
    if status == 0:
        sql = "UPDATE hm_channel SET is_entertainment='{}' WHERE room_number = {}".format('no', room_number)
        cur.execute(sql)
        mysql_inst.commit()
        r.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('no'))
        return True
    elif status == 1:
        sql = "UPDATE hm_channel SET is_entertainment='{}' WHERE room_number = {}".format('yes', room_number)
        cur.execute(sql)
        mysql_inst.commit()
        r.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('yes'))
        r.set('hm_pushstream_type_{}'.format(cid), 1)  # 2手机 1PC
        return True
    elif status == 2:
        sql = "UPDATE hm_channel SET is_entertainment='{}' WHERE room_number = {}".format('yes', room_number)
        cur.execute(sql)
        mysql_inst.commit()
        r.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('yes'))
        r.set('hm_pushstream_type_{}'.format(cid), 2)  # 2手机 1PC
        r.set('hm_mobile_screenType_outdoor_{}'.format(cid), 2)  # 2竖屏 1横屏
        return True
    else:
        return False


def generate_name(casename):
    return '{}{}'.format(casename, int(time.time()))


# 测试数据生成 1个房间，房主，房管fg数默认0
def generate_room(casename, fg=0):
    uids = []
    names = []
    for i in range(0, fg + 1):
        name = generate_name(casename)
        names.append(name)
        uid = zc(name)
        bd_sj(uid)
        uids.append(uid)
        time.sleep(1)
    res = sq_zb(uids[0])
    cid = res[0]
    room_number = res[1]
    for i in range(0, fg):
        requests.post(url + '/myroom/setRoomAdministrator', data={'username': names[i + 1]}, cookies=generate_cookies(uids[0]))
    if fg > 0:
        data = {'fz_id': uids[0], 'fz_name': names[0],
                'fg_id': uids[1:], 'fg_name': names[1:],
                'cid': cid, 'room_number': room_number}
    elif fg == 0:
        data = {'fz_id': uids[0], 'fz_name': names[0],
                'cid': cid, 'room_number': room_number}
    else:
        data = False
    logging.debug(data)
    return data


def generate_user(casename, user=1, phone=False):
    uids = []
    names = []
    for i in range(0, user):
        name = generate_name(casename)
        names.append(name)
        uid = zc(name)
        if phone:
            bd_sj(uid)
        uids.append(uid)
        time.sleep(1)
    data = {'user_ids': uids, 'user_names': names}
    logging.debug(data)
    return data

# 初始化禁言数据
def init_gag(user_data, room_data):
    mysql_inst.select_db('hm_contents')
    cur = mysql_inst.cursor()
    cur.execute('truncate hm_gag')
    mysql_inst.commit()
    fz = room_data.get('fz_id',0)
    fg = room_data.get('fg_id',0)
    users = user_data.get('user_ids',0)
    users.append(fz)
    users.extend(fg)
    for user in users:
        redis_inst.delete('hm_gag_user_{}'.format(user))
    redis_inst.delete('hm_gag_channel_{}'.format(room_data.get('cid',0)))

