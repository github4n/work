#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 10:49:33
# @Author  : lixingyun
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
# 线上地址
URL_ONLINE = 'https://www.huomao.com'
ADMIN_URL_ONLINE = 'http://bii3c.huomao.com'
# 后台url
ADMIN_URL = 'http://qaadmin.new.huomaotv.com.cn'
# 后台cookies
ADMIN_COOKIES = {'huomaotvcheckcode': 'SQJ5', 'adminId': '33', 'adminAccount': 'root', 'adminNick': 'root', 'adminUserId': '0',
                 'adminLoginTime': '1473220408', 'adminToken': 'bd2c21cb89ada618b16170504ad9f84d'}
# 线上后台cookies
ADMIN_COOKIES_ONLINE = {'adminId': '7', 'adminAccount': 'lxy', 'adminNick': '%E6%9D%8E%E5%B9%B8%E8%BF%90',
                        'adminUserId': '1870709', 'adminLoginTime': '1504756354', 'adminToken': '66897400739a15c9c6453a6e68b71e1d'}

# 用户默认密码
USER_PWD = '1'
# 数据库配置
DB_HOST = 'db.huomaotv.com.cn'
DB_USER = 'root'
DB_PASSWD = '123456'
DB_PORT = 3306
# redis配置
REDIS_HOST = 'db.huomaotv.com.cn'
REDIS_PORT = 6379


class Common():
    def __init__(self, *args, **kwargs):
        # redis连接
        self.REDIS_INST = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
        self._conn()

    def _conn(self):
        try:
            # 数据库连接
            self.MYSQL_INST = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, port=DB_PORT, charset='utf8')
            return True
        except:
            return False

    def execute_sql(self, db, sql):
        try:
            self.MYSQL_INST.ping()
        except Exception as e:
            print('数据库重连中{}'.format(e))
            self._conn()
        self.MYSQL_INST.select_db(db)
        cur = self.MYSQL_INST.cursor()
        cur.execute(sql)
        data = cur.fetchone()
        cur.close()
        self.MYSQL_INST.commit()
        return data

    # hash分表查询
    def hash_table(self, s, num=32):
        s = ('hm_db_{}'.format(s)).encode('utf-8')
        m = hashlib.md5()
        m.update(s)
        md5s = m.hexdigest()
        md5ss = int(md5s[1:3], 16) % num
        return str(md5ss)

    # 用户cookie生成
    @staticmethod
    def generate_cookies(uid):
        key = 'HUOMAOTV!@#$%^&*137SECRET'
        uid = str(uid)
        ts = str(int(time.time()))
        b = (uid + ts + key).encode('utf-8')
        token = str(hashlib.md5(b).hexdigest())
        cookies = {'user_e100fe70f5705b56db66da43c140237c': uid,
                   'user_6b90717037ae096e2f345fde0c31e11b': token,
                   'user_2c691ee7b8307f7fadc5c2c9349dbd7b': ts}
        return cookies

    # 查找UID
    def find_uid(self, name):
        tb_name = 'username_' + self.hash_table(name)
        sql = 'SELECT uid FROM {} WHERE username = "{}"'.format(tb_name, name)
        data = self.execute_sql('hm_user', sql)
        if data:
            return {'code': 100, 'status': True, 'msg': data[0]}
        else:
            return {'code': 101, 'status': False, 'msg': '没找到'}

    # 设置仙豆
    def set_xd(self, uid, xd):
        xd = 0 if not xd else xd
        return self.REDIS_INST.set('hm_free_bean_{}'.format(uid), int(xd) if xd else 0)

    # 获取仙豆
    def get_xd(self, uid):
        return self.REDIS_INST.get('hm_free_bean_{}'.format(uid))

    # 设置用户猫币，猫豆
    def set_money(self, uid, coin, bean):
        coin = 0 if not coin else coin
        bean = 0 if not bean else bean
        tb_name = 'money_' + self.hash_table(uid)
        sql = 'SELECT coin,bean FROM {} WHERE uid = {}'.format(tb_name, uid)
        data = self.execute_sql('hm_money', sql)
        # 判断用户是否存在记录，存在则修改，否则插入数据
        if data is not None:
            # sql1 = 'SELECT coin,bean FROM {} WHERE uid = {}'.format(tablname, uid)
            # sql2 = "UPDATE  %s SET  coin =  %s, bean =  %s WHERE  uid = %s" % (tablname, num1 + float(data[0]), num2 + float(data[0]), uid)
            sql_update = 'UPDATE {} SET coin = {}, bean = {} WHERE uid = {}'.format(tb_name, coin, bean, uid)
            return self.execute_sql('hm_money', sql_update)
        else:
            sql_insert = "INSERT INTO  {}(uid,coin,bean,ts) values({},{},{},{})".format(tb_name, uid, coin, bean, int(time.time()))
            return self.execute_sql('hm_money', sql_insert)

    # 获取用户余额
    def get_money(self, uid):
        tb_name = 'money_' + self.hash_table(uid)
        sql = 'SELECT coin,bean FROM {} WHERE uid = {}'.format(tb_name, uid)
        data = self.execute_sql('hm_money', sql)
        return {'coin': data[0], 'bean': data[1]}

    # 添加弹幕卡
    def add_dmk(self, uid, add_time=int(time.time()), expire_time=int(time.time()) + 10000, num=1):
        sql = "INSERT INTO user_bag_{} values(NULL,{},'{}',{},{},{},{},{},{})".format(self.hash_table(uid), uid, 'admin_33', 100001, add_time,
                                                                                      expire_time,
                                                                                      num, 2, num)
        return self.execute_sql('hm_user_bag', sql)

    # 获取弹幕卡
    def get_dmk(self, uid):
        sql = "SELECT sum(num) FROM user_bag_{} WHERE uid={} and expire_time >{} and bag_id=100001 ".format(self.hash_table(uid), uid,
                                                                                                            int(time.time()))
        return self.execute_sql('hm_user_bag', sql)[0]

    # 删除弹幕卡
    def del_dmk(self, uid):
        sql = "DELETE FROM user_bag_{} WHERE uid={}".format(self.hash_table(uid), uid)
        return self.execute_sql('hm_user_bag', sql)

    # 绑定手机号
    def bd_sj(self, uid):
        if uid:
            url1 = URL + '/test/uum/' + str(uid) + '/' + str(15800000000 + int(uid))
            res = requests.get(url1, cookies=self.generate_cookies(uid))
            if res.status_code == 200:
                return {'code': 100, 'status': True, 'msg': '绑定手机号成功'}
            else:
                return {'code': 901, 'status': False, 'msg': '绑定手机号失败'}
        else:
            return {'code': 902, 'status': False, 'msg': '绑定手机号失败'}

    # 注册用户返回uid,或登录返回uid
    def zc(self, username):
        r = requests.post(URL + '/user/lucky_reg',
                          data={'nick_name': username, 'user_pwd': USER_PWD, 'username': username, 'key': 'huomao_lucky'})
        if r.json()['code'] != '100':
            return {'code': 900, 'status': False, 'msg': '注册失败'}
        else:
            return {'code': 100, 'status': True, 'msg': '成功\tuid:{}\t密码:1'.format(r.json()['data']['uid'])}


    # 申请直播并通过
    def sq_zb(self, uid):
        # 判断uid是否是主播
        if uid:
            uid = str(uid)
            res = requests.get(URL + '/member/checkUsersIdentify', cookies=self.generate_cookies(uid))
            if res.json()['data']['isAnchor'] is True:
                return {'code': 900, 'status': False, 'msg': '已是主播'}
            else:
                self.bd_sj(uid)
                time.sleep(1)
                data = {'true_name': '测试号',
                        'sex': '1',
                        'gid': '97',
                        'cred': '4',
                        'card_code': '100' + uid,
                        'card_pic': 'http://img.new.huomaotv.com.cn/upload/web/images/defaultimgs/0dc10ab4d7bda309e3095298ca689573/20160907110242mnxsySdt.png',
                        'qq': '100' + uid,
                        'agreement': '1'}
                res = requests.post(URL + '/anchor/submitApply', data=data, cookies=self.generate_cookies(uid),
                                    headers={'X-Requested-With': 'XMLHttpRequest'})
                res = requests.get(ADMIN_URL + '/anchor/lists', params={'field': 'uid', 'keyword': uid}, cookies=ADMIN_COOKIES)
                uidid = etree.HTML(res.text).xpath('//tr[2]/td[1]')[0].text
                res = requests.post(ADMIN_URL + '/index.php/anchor/submitVerify',
                                    data={'status': '1', 'is_push': '1', 'reason': '', 'id': uidid}, cookies=ADMIN_COOKIES)

                sql = "SELECT id,room_number FROM hm_channel WHERE uid = '{}'".format(uid)
                data = self.execute_sql('hm_contents', sql)
                return {'code': 100, 'status': True, 'msg': '申请成功\tcid:{}\t房间号:{}'.format(data[0],data[1])}
        else:
            return {'code': 901, 'status': False, 'msg': '申请失败'}

    # 更新房间状态
    def update_stat(self, cids, stat):
        if cids and stat:
            cids = str(cids)
            cids = cids.split(",")
            for cid in cids:
                if cid:
                    data = {'is_live': stat,
                            'cid': cids,
                            }
                    requests.get(URL + '/plugs/updateRoomLiveStat', params=data)
            return {'code': 100, 'status': True, 'msg': '修改成功'}
        else:
            return {'code': 101, 'status': False, 'msg': '修改失败'}

    # 线上流同步线下
    def update_stream(self, room_xs, room_xx):
        try:
            res = requests.post(ADMIN_URL_ONLINE + '/channel/getChannelList', data={'keyWord': 'roomNum', 'keyContent': room_xs, 'page': 1},
                                cookies=ADMIN_COOKIES)
            stream = etree.HTML(res.text).xpath('//*[@id="matchTable"]/tr[2]/td[2]')[0].text
            print(stream)
            r = self.execute_sql('hm_contents', "UPDATE  hm_channel SET  stream = '{}' WHERE room_number = {}".format(stream, room_xx))
            print(r)
            anchor = self.execute_sql('hm_contents', "SELECT uid from hm_channel  WHERE room_number = {}".format(room_xx))[0]
            print(anchor)
            self.REDIS_INST.hset('hm_channel_anchor_{}'.format(anchor), 'stream', '"' + stream + '"')
            return {'code': 100, 'status': True, 'msg': '成功'}
        except:
            return {'code': 900, 'status': False, 'msg': '失败'}

    # 修改密码
    def update_password(self, uid, password):
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
    def update_roomlx(self, room_number, status):
        if room_number and status or status == '0':
            data = self.execute_sql('hm_contents', "SELECT uid,id from hm_channel  WHERE room_number = {}".format(room_number))
            uid = data[0]
            cid = data[1]
            if status == '0':
                sql = "UPDATE hm_channel SET is_entertainment='{}' WHERE room_number = {}".format('no', room_number)
                self.execute_sql('hm_contents', sql)
                self.REDIS_INST.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('no'))
            elif status == '1':
                sql = "UPDATE hm_channel SET is_entertainment='{}' WHERE room_number = {}".format('yes', room_number)
                self.execute_sql('hm_contents', sql)
                self.REDIS_INST.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('yes'))
                self.REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 1)  # 2手机 1PC
            elif status == '2':
                sql = "UPDATE hm_channel SET is_entertainment='{}' WHERE room_number = {}".format('yes', room_number)
                self.execute_sql('hm_contents', sql)
                self.REDIS_INST.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('yes'))
                self.REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 2)  # 2手机 1PC
                self.REDIS_INST.set('hm_mobile_screenType_outdoor_{}'.format(cid), 2)  # 2竖屏 1横屏
            else:
                return {'code': 101, 'status': False, 'msg': '修改失败'}
            return {'code': 100, 'status': True, 'msg': '修改成功'}
        else:
            return {'code': 102, 'status': False, 'msg': '修改失败'}

    def generate_name(self, casename):
        return '{}{}'.format(casename, int(time.time()))

    # 测试数据生成 1个房间，房主，房管fg数默认0
    def generate_room(self, casename, fg=0):
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

    def generate_user(self, casename, user=1, phone=False):
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
    def init_gag(self, user_data, room_data):
        mysql_inst.select_db('hm_contents')
        cur = mysql_inst.cursor()
        cur.execute('truncate hm_gag')
        mysql_inst.commit()
        fz = room_data.get('fz_id', 0)
        fg = room_data.get('fg_id', 0)
        users = user_data.get('user_ids', 0)
        users.append(fz)
        users.extend(fg)
        for user in users:
            redis_inst.delete('hm_gag_user_{}'.format(user))
        redis_inst.delete('hm_gag_channel_{}'.format(room_data.get('cid', 0)))
