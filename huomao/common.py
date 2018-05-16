#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 10:49:33
# @Author  : lixingyun
import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
import time
import hashlib
import requests
import paramiko
import redis
import json
import logging
from urllib import parse
from .db.user import Userbase
from .db.money import MoneyPay, MoneyChannelIncome
from .db.contents import HmGag, HmLoveliness
from .config import URL, REDIS_CONFIG, REDIS_CONFIG2

# redis连接
REDIS_INST = redis.Redis(**REDIS_CONFIG, db=0, decode_responses=True)
REDIS_INST2 = redis.Redis(**REDIS_CONFIG2, db=0, decode_responses=True)


class Common():
    def __init__(self, *args, **kwargs):
        pass

    # 连接linux服务器
    @staticmethod
    def connect():
        'this is use the paramiko connect the host,return conn'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            #        ssh.connect(host,username='root',allow_agent=True,look_for_keys=True)
            ssh.connect('10.10.23.14', username='lxy', password='lxy', allow_agent=True)
            return ssh
        except:
            return None

    @staticmethod
    # 获取linux服务器时间
    def get_linux_time():
        ssh = Common.connect()
        stdin, stdout, stderr = ssh.exec_command('date +%s')
        return int(stdout.read().decode())

    # 移动端加密方式
    @staticmethod
    def encrypt(data):
        SECRET_KEY_MOBILE = "EU*T*)*(#23ssdfd"
        value = ''
        for key in sorted(data.keys(), reverse=True):
            value += str(data[key])
        m = hashlib.md5()
        value = (value + SECRET_KEY_MOBILE).encode('utf-8')
        m.update(value)
        md5s = m.hexdigest()
        datas = parse.urlencode(data)
        return '?' + datas + '&token=' + md5s

    # md5
    @staticmethod
    def md5(data):
        s = str(data).encode('utf-8')
        m = hashlib.md5()
        m.update(s)
        md5s = m.hexdigest()
        return md5s

    # 多层字典转单层form
    @staticmethod
    def form_single_dict(data, key='', ret={}):
        if isinstance(data, dict):
            for key1, value1 in data.items():
                key1s = str(key) + '[' + str(key1) + ']' if key else str(key1)
                if isinstance(value1, dict):
                    Common.form_single_dict(value1, key1s)
                else:
                    ret[key1s] = value1
            return ret
        else:
            return False

    # hash分表查询
    @staticmethod
    def hash_table(s, num=32):
        md5s = Common.md5('hm_db_{}'.format(s))
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

    # 添加手机验证码
    @staticmethod
    def add_mobile_yzm(mobile, yzm=123456):
        REDIS_INST.set('hm_plugs_mobile_post_{}'.format(mobile), yzm, 1800)

    @staticmethod
    def generate_name(casename):
        return '{}{}'.format(casename, int(time.time()))

    # 测试数据生成 1个房间，房主，房管fg数默认0
    @staticmethod
    def generate_room(casename, fg=0):
        # 生成主播和房间
        anchor_name = Common.generate_name(casename)
        anchor_uid = Common.zc(anchor_name)['uid']
        Common.bd_sj(anchor_uid)
        res = Common.sq_zb(anchor_uid)['data']
        cid = str(res[0])
        rid = str(res[1])

        data = {
            'room': {
                'cid': cid,
                'rid': rid
            },
            'anchor': {
                'uid': anchor_uid,
                'name': anchor_name
            },
            'fg': {}
        }

        # 生成房管
        for i in range(0, fg):
            name = Common.generate_name(casename)
            uid = Common.zc(name)['uid']
            Common.bd_sj(uid)
            requests.post(URL + '/myroom/setRoomAdministrator', data={'username': name}, cookies=Common.generate_cookies(anchor_uid))
            data['fg'][i] = {'uid': uid, 'name': name}
            time.sleep(1)

        logging.info(data)
        return data

    @staticmethod
    def generate_user(casename, user=1, phone=True):
        data = {}
        for i in range(0, user):
            name = Common.generate_name(casename)
            uid = Common.zc(name)['uid']
            data[i] = {'uid': uid, 'name': name}
            if phone:
                Common.bd_sj(uid)
            time.sleep(1)
        logging.info(data)
        return data

    @staticmethod
    def send_msg(uid, cid):
        data = dict(cid=cid, uid=uid, data='测试')
        res = requests.get(URL + '/chatnew/msg', params=data, cookies=Common.generate_cookies(uid))
        return res.json()

    @staticmethod
    def gag(uid, ban_uid, cid, status=0):
        if status == -1:
            data = dict(cid=cid, uid=ban_uid, user_uid=uid, gag_type='24', text='测试')
            res = requests.get(URL + '/myroom/addUserGag', params=data, cookies=Common.generate_cookies(ban_uid))
            logging.info(res.json())
        else:
            data = dict(cid=cid, uid=uid, status=status, nickname='测试', text='测试')
            res = requests.get(URL + '/myroom/setCommChannelGag', params=data, cookies=Common.generate_cookies(ban_uid))
            logging.info(res.json())

    @staticmethod
    def del_fg(cid):
        key = 'hm_channel_admin_{}'.format(cid)
        REDIS_INST.delete(key)
        # fg_data = json.loads(Common.REDIS_INST.get(key))
        # print(fg_data)
        # fg_data.pop(uid)
        # Common.REDIS_INST.set(key, json.dumps(fg_data))

    @staticmethod
    def set_fg(cid, uid):
        key = 'hm_channel_admin_{}'.format(cid)
        data = REDIS_INST.get(key)
        fg_data = json.loads(data) if data else {}
        fg_data[uid] = int(time.time())
        REDIS_INST.set(key, json.dumps(fg_data))

    # 初始化用户,房间禁言数据
    @staticmethod
    def init_gag(uid, cid):
        if uid:
            HmGag.delete().where((HmGag.cid == cid) & (HmGag.uid == uid)).execute()
            REDIS_INST.delete('hm_gag_user_{}'.format(uid))
            REDIS_INST.delete('hm_gag_channel_{}'.format(cid))
        return 0



    # 获取送礼记录
    @staticmethod
    def get_money_pay(uid, cid):
        count = MoneyPay.select().where((MoneyPay.uid == uid) & (MoneyPay.other_cid == cid) & (MoneyPay.ts < mon_last_time)).count()
        return count

    # 获取收礼记录
    @staticmethod
    def money_income(type, uid, user_id=0):
        m = 0
        if type == 'del':
            m = MoneyChannelIncome.delete().where(MoneyChannelIncome.uid == uid).execute()
        elif type == 'get':
            m = MoneyChannelIncome.select().where((MoneyChannelIncome.uid == uid) & (MoneyChannelIncome.addtime < mon_last_time) & (
                MoneyChannelIncome.other_uid == user_id)).first()
            m = m.money
        elif type == 'count':
            m = MoneyChannelIncome.select().where((MoneyChannelIncome.uid == uid) & (MoneyChannelIncome.addtime < mon_last_time) & (
                MoneyChannelIncome.other_uid == user_id)).count()
        return m

    # 获取/修改/删除粉丝值
    @staticmethod
    def loveliness(type, uid, cid=0, score=0):
        if type == 'get':
            res = HmLoveliness.select().where((HmLoveliness.uid == uid) & (HmLoveliness.cid == cid)).first().score
        elif type == 'set':
            print(333)
            res = HmLoveliness.update(score=score).where((HmLoveliness.uid == uid) & (HmLoveliness.cid == cid)).execute()
        elif type == 'del':
            res = HmLoveliness.delete().where(HmLoveliness.uid == uid).execute()
            print(res)
        else:
            res = False
        return res

    # 初始化粉丝
    @staticmethod
    def init_fans(uid):
        uid = str(uid)
        Common.loveliness('del', uid)
        fan_keys = REDIS_KEYS['fans']
        keys = []
        for key in fan_keys[0:2]:
            keys.extend(REDIS_INST.keys(key.format_map({'uid': uid, 'cid': '*'})))
        for key in fan_keys[2:6]:
            keys.append(key.format_map({'uid': uid}))
        for key in keys:
            REDIS_INST.delete(key)
        # 删除已获取爱心粉丝值用户
        key = REDIS_KEYS['fans'][6]
        data = json.loads(REDIS_INST.get(key))
        for key, value in data.items():
            if uid in value:
                data[key].remove(uid)
                REDIS_INST.set(key, json.dumps(data))
        return {'msg': '成功'}

    def subscribe(uid):
        key = REDIS_KEYS['subscribe'].format_map({'uid': uid})
        subscribe_data = REDIS_INST.get(key)
        subscribe_data = json.loads(subscribe_data)
        data = {}
        for i in range(1, 211):
            data[i] = []
        subscribe_data['subsList'] = data
        REDIS_INST.set(key, json.dumps(subscribe_data))

    @staticmethod
    def is_json(data):
        try:
            json.loads(data)
            return True
        except ValueError:
            return False
