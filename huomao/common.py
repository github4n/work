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
from lxml import etree
from urllib import parse

from .db.contents import HmGag
from .config import URL, REDIS_CONFIG, REDIS_CONFIG2,ADMIN_COOKIES, ADMIN_COOKIES_ONLINE,logger_huomao

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
        data['token'] =  Common.md5(value + SECRET_KEY_MOBILE)
        return data


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
            for key1 in sorted(data.keys()):
                value1 = data.get(key1)
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

    # 清楚cdn缓存
    @staticmethod
    def clear_cdn_cache(urls):
        if isinstance(urls,list):
            for url in urls:
                res = requests.post('http://bii3c.huomao.com/cachemanage/clearCdnCache', cookies=ADMIN_COOKIES, data={'url': url})
                res = res.json()
                print(url, res)
                requests.get(url)
        else:
            res = requests.post('http://bii3c.huomao.com/cachemanage/clearCdnCache', cookies=ADMIN_COOKIES, data={'url': urls})
            res = res.json()
            print(urls,res)
            requests.get(urls)
        print('执行完成')


    @staticmethod
    def clear_all_cdn_cache():
        urls = ['https://www.huomao.com/',
                'https://www.huomao.com/channel/all',
                'https://www.huomao.com/1',
                'https://www.huomao.com/zt/lucky']

        def get_js_css(urls):
            rets = []
            res = []
            for url in urls:
                ret = requests.get(url).text
                links = etree.HTML(ret).xpath('//link')
                scripts = etree.HTML(ret).xpath('//script')
                for link in links:
                    rets.append(link.get('href'))
                for script in scripts:
                    rets.append(script.get('src'))
            for ret in set(rets):
                if ret:
                    if '?v=' in ret:
                        res.append('https://www.huomao.com'+ret)
            return res

        Common.clear_cdn_cache(get_js_css(urls))

    # 添加手机验证码
    @staticmethod
    def add_mobile_yzm(mobile, yzm=123456):
        REDIS_INST.set('hm_plugs_mobile_post_{}'.format(mobile), yzm, 1800)

    @staticmethod
    def init_active():
        for key in REDIS_INST.keys('*mobile_active_*'):
            REDIS_INST.delete(key)


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
            logger_huomao.info(res.json())
        else:
            data = dict(cid=cid, uid=uid, status=status, nickname='测试', text='测试')
            res = requests.get(URL + '/myroom/setCommChannelGag', params=data, cookies=Common.generate_cookies(ban_uid))
            logger_huomao.info(res.json())

    # 初始化用户,房间禁言数据
    @staticmethod
    def init_gag(uid, cid):
        if uid:
            HmGag.delete().where((HmGag.cid == cid) & (HmGag.uid == uid)).execute()
            REDIS_INST.delete('hm_gag_user_{}'.format(uid))
            REDIS_INST.delete('hm_gag_channel_{}'.format(cid))
        return 0

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
