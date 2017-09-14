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
from common.db.user import Userbase, Userinfo
from common.db.money import Money, MoneyPay, MoneyChannelIncome
from common.db.contents import HmChannel, HmGag, HmLoveliness

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

# redis配置
REDIS_HOST = 'db.huomaotv.com.cn'
REDIS_PORT = 6379
# 数据库配置
DB_HOST = '10.10.23.15'
DB_USER = 'huomao'
DB_PASSWD = 'huomao'
DB_PORT = 3306
DB_CONFIG = {'host': DB_HOST, 'user': DB_USER, 'password': DB_PASSWD}
# 用户默认密码
USER_PWD = '1'
timestamp = int(time.time())
run_date = time.localtime()
run_date_year = run_date.tm_year
run_date_month = run_date.tm_mon

REDIS_KEYS = {
    'fans':
        [
            'hm_loveliness_fan_lv_news_{uid}_{cid}',  # 房间粉丝等级
            'hm_level_six_{uid}',  # 用户是否首次6级
            'hm_level_first_{uid}',  # 用户是否首次1级
            'hm_level_first_channel_{cid}_{uid}',  # 用户房间首次1级
            'hm_fans_platform_{uid}',  #
            'hm_more_six_platform_list_{uid}',  #
            'hm_XIAN_1000_GIFT'  # 是否送爱心已得到粉丝值
        ],
    'subscribe': 'hm_users_subscribe_channels{uid}'
}


class Common():
    def __init__(self, *args, **kwargs):
        # redis连接
        self.REDIS_INST = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

    def execute_sql(self, db, sql):
        # 数据库连接
        MYSQL_INST = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, port=DB_PORT, db=db, charset='utf8')
        cur = MYSQL_INST.cursor()
        cur.execute(sql)
        data = cur.fetchone()
        cur.close()
        MYSQL_INST.commit()
        MYSQL_INST.close()
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
    def find_uid(self, username):
        u = Userbase.select(Userbase.uid).where(Userbase.name == username).first()
        if u:
            return {'code': 100, 'status': True, 'msg': u.uid}
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
    def set_money(self, uid, coin=0, bean=0):
        coin = 0 if not coin else coin
        bean = 0 if not bean else bean
        money = Money.select().where(Money.uid == uid).first()
        # 判断用户是否存在记录，存在则修改，否则插入数据
        if money:
            return Money.update(coin=coin, bean=bean).where(Money.uid == uid).execute()
        else:
            return Money.create(uid=uid, coin=coin, bean=bean, ts=timestamp)

    # 获取用户余额
    def get_money(self, uid):
        money = Money.select().where(Money.uid == uid).first()
        return {'coin': money.coin, 'bean': money.bean}

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
            uid = r.json()['data']['uid']
            return {'code': 100, 'status': True, 'msg': '成功\tuid:{}\t密码:1'.format(uid), 'uid': uid}

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
                channel = HmChannel.select().where(HmChannel.uid == uid).first()
                data = [channel.id, channel.room_number]
                return {'code': 100, 'status': True, 'msg': '申请成功\tcid:{}\t房间号:{}'.format(data[0], data[1]), 'data': data}
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
            # 更新表
            HmChannel.update(stream=stream).where(HmChannel.room_number == room_xx).execute()
            # 获取主播uid
            channel = HmChannel.select().where(HmChannel.room_number == room_xx).first()
            self.REDIS_INST.hset('hm_channel_anchor_{}'.format(channel.uid), 'stream', '"' + stream + '"')
            return {'code': 100, 'status': True, 'msg': '成功'}
        except:
            return {'code': 900, 'status': False, 'msg': '失败'}

    # 修改密码
    def update_password(self, uid, password):
        # 生产密码
        uid = str(uid)
        m = hashlib.md5()
        m.update(str(password).encode('utf-8'))
        newpassword = m.hexdigest()
        # 更新表
        Userinfo.update(password=newpassword).where(Userinfo.uid == uid).execute()
        # 更新redis
        data = json.loads(self.REDIS_INST.get('hm_' + uid))
        data['password'] = newpassword
        self.REDIS_INST.set('hm_' + uid, json.dumps(data))

    # 修改房间类型0普通，1横板娱乐，2竖版娱乐
    def update_roomlx(self, room_number, status):
        if room_number and status or status == '0':
            channel = HmChannel.select().where(HmChannel.room_number == room_number).first()
            uid = channel.uid
            cid = channel.id
            if status == '0':
                HmChannel.update(is_entertainment='no').where(HmChannel.room_number == room_number).execute()
                self.REDIS_INST.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('no'))
            elif status == '1':
                HmChannel.update(is_entertainment='yes').where(HmChannel.room_number == room_number).execute()
                self.REDIS_INST.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps('yes'))
                self.REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 1)  # 2手机 1PC
            elif status == '2':
                HmChannel.update(is_entertainment='yes').where(HmChannel.room_number == room_number).execute()
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
            name = self.generate_name(casename)
            names.append(name)
            uid = self.zc(name)['uid']
            self.bd_sj(uid)
            uids.append(uid)
            time.sleep(1)
        res = self.sq_zb(uids[0])['data']
        cid = res[0]
        room_number = res[1]
        for i in range(0, fg):
            requests.post(URL + '/myroom/setRoomAdministrator', data={'username': names[i + 1]}, cookies=self.generate_cookies(uids[0]))
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
            name = self.generate_name(casename)
            names.append(name)
            uid = self.zc(name)['uid']
            if phone:
                self.bd_sj(uid)
            uids.append(uid)
            time.sleep(1)
        data = {'user_ids': uids, 'user_names': names}
        logging.debug(data)
        return data

    # 初始化禁言数据
    def init_gag(self, user_data, room_data):
        HmGag.delete().where(1 == 1).execute()
        fz = room_data.get('fz_id', 0)
        fg = room_data.get('fg_id', 0)
        users = user_data.get('user_ids', 0)
        users.append(fz)
        users.extend(fg)
        for user in users:
            redis_inst.delete('hm_gag_user_{}'.format(user))
        redis_inst.delete('hm_gag_channel_{}'.format(room_data.get('cid', 0)))

    # 获取经验值
    def get_experience(self, uid):
        u = Userbase.select().where(Userbase.uid == uid).first()
        return u.get_experience, u.anchor_experience

    # 获取送礼记录
    def get_money_pay(self, uid):
        return MoneyPay.select().where(MoneyPay.uid == uid).count()

    # 获取收礼记录
    def get_money_income(self, uid, type=0):
        if type == 1:
            m = MoneyChannelIncome.delete().where(MoneyChannelIncome.uid == uid).execute()
        elif type == 2:
            m = MoneyChannelIncome.select().where(MoneyChannelIncome.uid == uid).first()
            m = m.money
        else:
            m = MoneyChannelIncome.select().where(MoneyChannelIncome.uid == uid).count()
        return m

    # 获取/修改/删除粉丝值
    def loveliness(self, type, uid, cid=0, score=0):
        if type == 'get':
            res = HmLoveliness.select().where(HmLoveliness.uid == uid and HmLoveliness.cid == cid).first().score
        elif type == 'set':
            print(333)
            res = HmLoveliness.update(score=score).where(HmLoveliness.uid == uid and HmLoveliness.cid == cid).execute()
        elif type == 'del':
            res = HmLoveliness.delete().where(HmLoveliness.uid == uid).execute()
            print(res)
        else:
            res = False
        return res

    # 初始化粉丝
    def init_fans(self, uid, cid):
        self.loveliness('del', uid)
        fan_keys = REDIS_KEYS['fans']
        # print(fan_keys[0:6])
        for key in fan_keys[0:6]:
            # print(key.format_map({'uid': uid, 'cid': cid}))
            self.REDIS_INST.delete(key.format_map({'uid': uid, 'cid': cid}))
        # 删除已获取爱心粉丝值用户
        key = REDIS_KEYS['fans'][6]
        data = json.loads(self.REDIS_INST.get(key))
        uids = data.get(str(cid))
        if uids:
            if uid in uids:
                index = uids.index(str(uid))
                print(index)
                uids.pop(index)
                self.REDIS_INST.set(key, json.dumps(data))

    def subscribe(self, uid):
        key = REDIS_KEYS['subscribe'].format_map({'uid': uid})
        subscribe_data = self.REDIS_INST.get(key)
        subscribe_data = json.loads(subscribe_data)
        data = {}
        for i in range(1, 211):
            data[i] = []
        subscribe_data['subsList'] = data
        self.REDIS_INST.set(key, json.dumps(subscribe_data))
