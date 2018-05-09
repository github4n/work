#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 15:43
# Author : lixingyun
# Description :
import json
import configparser
import os
import time
import requests
import logging
from lxml import etree
from .db.user import Userbase, Userinfo, Mobile, UserName, Uid
from .common import REDIS_INST, Common
from .config import URL, ADMIN_URL, ADMIN_COOKIES
from .db.contents import HmChannel
from .db.noble import HmNobleRecord


class User():
    # 查找UID
    def find_uid(self, username):
        u = Userbase.select(Userbase.uid).where(Userbase.name == username).first()
        if u:
            return {'code': 100, 'status': True, 'msg': u.uid}
        else:
            return {'code': 101, 'status': False, 'msg': '没找到'}

    # 注册用户返回uid,或登录返回uid
    def register(self, username):
        # 默认密码1
        password = Common.md5('1')
        img = ''
        nickname = username + 'nc'
        ret = {'code': 1001, 'status': False, 'msg': '用户名已存在或注册失败'}
        # 验证用户名是否存在
        key_username = 'hm_user_name_redis_prefix:{}'.format(Common.md5(username))
        if REDIS_INST.get(key_username) or UserName.select().where(UserName.username == username).first():
            return ret
        # 创建uid
        uid = Uid().create().id
        # print(uid, Common.hash_table(uid))
        # 插入userbase表
        Userbase.create(uid=uid, name=username, email='', mobile='', openid='', weixin='', mobileareacode='')
        # 插入username表
        UserName.create(username=username, uid=uid)
        # 插入userinfo表
        Userinfo.create(uid=uid, password=password, img=img, lv=0)
        # 设置username,redis缓存
        REDIS_INST.set(key_username, uid)
        # 设置uid,redis缓存
        data = dict(nickname=nickname, password=password, img=img, lv=0, regtime=int(time.time()))
        REDIS_INST.set('hm_{}'.format(uid), json.dumps(data))
        # 设置nickname,redis缓存
        REDIS_INST.set('hm_nickname_{}'.format(Common.md5(nickname)), uid)
        # 设置userbase,redis缓存:hm_userbaseinfo_{uid}
        data = dict(uid=uid, name=username, email='', email_activate_stat=0,
                    mobile='', openid='', weixin='', blog='', send_freebean=0,
                    get_experience=0, anchor_experience=0, mobileareacode='')
        # 不知道php为什么要json转义一层再存.
        for key, value in data.items():
            data[key] = json.dumps(value)
        REDIS_INST.hmset('hm_userbaseinfo_{}'.format(uid), data)
        return {'code': 100, 'status': True, 'msg': '成功\tuid:{}\t密码:1'.format(uid), 'uid': str(uid)}

    # 按序注册用户返回uid
    def reg(self):
        # 获取文件的当前路径（绝对路径）
        cur_path = os.path.dirname(os.path.realpath(__file__))
        # 获取config.ini的路径
        config_path = os.path.join(cur_path, 'user.ini')
        conf = configparser.ConfigParser()
        # 读取配置
        conf.read(config_path)
        number = conf.get('user', 'number')
        # 设置配置
        conf.set('user', 'number', str(int(number) + 1))
        # 写入配置
        with open(config_path, 'w') as fw:
            conf.write(fw)
        fw.close()
        return self.register('t1stnoble' + number)['uid']

    # 申请直播并通过
    def sq_zb(self, uid):
        # 判断uid是否是主播
        if uid:
            # uid = str(uid)
            anchor_key = 'hm_channel_anchor_{}'.format(uid)
            if REDIS_INST.hget(anchor_key, 'id'):
                return {'code': 1001, 'status': False, 'msg': '已是主播'}
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
                res = requests.post(URL + '/anchor/submitApply', data=data, cookies=Common.generate_cookies(uid),
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

    # 绑定手机号
    def bd_sj(self, uid, mobileareacode='+86'):
        try:
            mobile = 15800000000 + int(uid)
            Mobile.create(mobile=mobile, uid=uid)
            Userbase.update(mobile=mobile, mobileareacode=mobileareacode).where(Userbase.uid == uid).execute()
            key = 'hm_userbaseinfo_{}'.format(uid)
            REDIS_INST.hset(key, 'mobile', mobile)
            REDIS_INST.hset(key, 'mobileareacode', mobileareacode)
            key_mobile = 'hm_user_mobile_prefix:{}_{}'.format(mobileareacode, mobile)
            REDIS_INST.set(key_mobile, uid)
            return {'code': 100, 'status': True, 'msg': '绑定手机号成功', 'mobile': mobile}
        except:
            return {'code': 1001, 'status': True, 'msg': '绑定手机号失败'}

    # 修改密码
    def update_password(self, uid, password):
        # 生成密码
        new_password = Common.md5(password)
        # 更新表
        Userinfo.update(password=new_password).where(Userinfo.uid == uid).execute()
        # 更新redis
        data = json.loads(REDIS_INST.get('hm_' + uid))
        data['password'] = new_password
        REDIS_INST.set('hm_' + uid, json.dumps(data))
        return {'code': 100, 'status': True, 'msg': '成功'}

    # 修改昵称
    def update_nick_name(self, uid, nick_name):
        uid = str(uid)
        # 更新redis
        data = json.loads(REDIS_INST.get('hm_' + uid))
        data['nickname'] = nick_name
        REDIS_INST.set('hm_' + uid, json.dumps(data))
        return {'code': 100, 'status': True, 'msg': '成功'}

    # 获取经验值
    @staticmethod
    def get_experience(uid):
        u = Userbase.select().where(Userbase.uid == uid).first()
        return u.get_experience, u.anchor_experience

    # 开通贵族
    @staticmethod
    def create_noble(uid, **kw):
        data = dict(level=1, cid=2, month=1, type=1, to_uid='')
        for key, value in kw.items():
            data[key] = value
        ret = requests.get(URL + '/noble/createNoble', params=data, cookies=Common.generate_cookies(uid)).json()
        logging.info(ret)
        return ret

    # 查询开通贵族收益
    @staticmethod
    def find_noble_anchor_profit(uid, pay_money=0):
        if pay_money == 0:
            u = HmNobleRecord.select().where((HmNobleRecord.uid == uid) & (HmNobleRecord.open_type == 1)).first()
            return float(u.anchor_profit) if u else 0
        else:
            u = HmNobleRecord.select().where(
                (HmNobleRecord.uid == uid) & (HmNobleRecord.pay_money == pay_money) & (HmNobleRecord.open_type == 1)).first()
            return float(u.anchor_profit) if u else 0
