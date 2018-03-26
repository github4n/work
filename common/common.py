#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 10:49:33
# @Author  : lixingyun
import time
import pymysql
import hashlib
import requests
import paramiko
import redis
import calendar
import json
import logging
from lxml import etree
from urllib import parse
from common.db.user import Userbase, Userinfo, Mobile, UserName, Uid
from common.db.money import Money, MoneyPay, MoneyChannelIncome
from common.db.contents import HmChannel, HmGag, HmLoveliness
from common.db.user_bag import UserBag
from peewee import fn

logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
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
LINUX_HOST = '10.10.23.14'
# 数据库配置
# DB_HOST = '10.10.23.15'
# DB_USER = 'huomao'
# DB_PASSWD = 'huomao'
# DB_PORT = 3306
# DB_CONFIG = {'host': DB_HOST, 'user': DB_USER, 'password': DB_PASSWD}
# 用户默认密码
USER_PWD = '1'
# 超管
SUPER_UID = '1870709'
timestamp = int(time.time())
run_date = time.localtime()
run_date_year = run_date.tm_year
run_date_month = run_date.tm_mon
days = calendar.monthrange(run_date_year, run_date_month)[1]
mon_last_time = time.mktime((run_date_year, run_date_month, days, 23, 59, 59, 0, 0, 0))

REDIS_KEYS = {
    'fans':
        [
            'hm_loveliness_fan_lv_news_{uid}_{cid}',  # 房间粉丝等级
            'hm_level_first_channel_{cid}_{uid}',  # 用户房间首次1级
            'hm_level_six_{uid}',  # 用户是否首次6级
            'hm_level_first_{uid}',  # 用户是否首次1级
            'hm_fans_platform_{uid}',  #
            'hm_more_six_platform_list_{uid}',  #
            'hm_XIAN_1000_GIFT'  # 是否送爱心已得到粉丝值
        ],
    'subscribe': 'hm_users_subscribe_channels{uid}'
}


class Common():
    # redis连接
    REDIS_INST = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

    def __init__(self, *args, **kwargs):
        pass

    # def execute_sql(self, db, sql):
    #     # 数据库连接
    #     MYSQL_INST = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, port=DB_PORT, db=db, charset='utf8')
    #     cur = MYSQL_INST.cursor()
    #     cur.execute(sql)
    #     data = cur.fetchone()
    #     cur.close()
    #     MYSQL_INST.commit()
    #     MYSQL_INST.close()
    #     return data
    # 连接linux服务器
    @staticmethod
    def connect():
        'this is use the paramiko connect the host,return conn'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            #        ssh.connect(host,username='root',allow_agent=True,look_for_keys=True)
            ssh.connect(LINUX_HOST, username='lxy', password='lxy', allow_agent=True)
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

    # 查找UID
    @staticmethod
    def find_uid(username):
        u = Userbase.select(Userbase.uid).where(Userbase.name == username).first()
        print(u)
        if u:
            return {'code': 100, 'status': True, 'msg': u.uid}
        else:
            return {'code': 101, 'status': False, 'msg': '没找到'}

    # 设置仙豆
    @staticmethod
    def set_xd(uid, xd):
        xd = 0 if not xd else xd
        return Common.REDIS_INST.set('hm_free_bean_{}'.format(uid), int(xd) if xd else 0)

    # 获取仙豆
    @staticmethod
    def get_xd(uid):
        return int(Common.REDIS_INST.get('hm_free_bean_{}'.format(uid)))

    # 设置用户猫币，猫豆
    @staticmethod
    def set_money(uid, coin=0, bean=0):
        coin = 0 if not coin else coin
        bean = 0 if not bean else bean
        money = Money.select().where(Money.uid == uid).first()
        # 判断用户是否存在记录，存在则修改，否则插入数据
        if money:
            return Money.update(coin=coin, bean=bean).where(Money.uid == uid).execute()
        else:
            return Money.create(uid=uid, coin=coin, bean=bean, ts=timestamp)

    # 获取用户余额
    @staticmethod
    def get_money(uid):
        money = Money.select().where(Money.uid == uid).first()
        return {'coin': money.coin, 'bean': money.bean}

    # 添加弹幕卡
    @staticmethod
    def add_dmk(uid, add_time=int(time.time()), expire_time=int(time.time()) + 10000, num=1):
        UserBag.create(uid=uid, get_way='admin_33', bag=100001, add_time=add_time, expire_time=expire_time, num=num, type=2, total=num)
        return
        # sql = "INSERT INTO user_bag_{} values(NULL,{},'{}',{},{},{},{},{},{})".format(Common.hash_table(uid), uid, 'admin_33', 100001, add_time,
        #                                                                               expire_time,
        #                                                                               num, 2, num)
        # return self.execute_sql('hm_user_bag', sql)

    # 获取弹幕卡
    @staticmethod
    def get_dmk(uid):
        u = UserBag.select(fn.Sum(UserBag.num)).where(
            (UserBag.uid == uid) & (UserBag.expire_time > int(time.time())) & (UserBag.bag == 100001)).first()
        return u.num
        # sql = "SELECT sum(num) FROM user_bag_{} WHERE uid={} and expire_time >{} and bag_id=100001 ".format(self.hash_table(uid), uid,
        #                                                                                                     int(time.time()))
        # return self.execute_sql('hm_user_bag', sql)[0]

    # 获取用户特定时间弹幕卡数量
    @staticmethod
    def get_time_dmk(uid, dmk_time):
        u = UserBag.select(fn.Sum(UserBag.num)).where((UserBag.uid == uid) & (UserBag.expire_time == dmk_time)).first()
        return u.num

    # 删除弹幕卡
    @staticmethod
    def del_dmk(uid):
        UserBag.delete().where(UserBag.uid == uid).execute()
        return
        # sql = "DELETE FROM user_bag_{} WHERE uid={}".format(self.hash_table(uid), uid)
        # return self.execute_sql('hm_user_bag', sql)

    # 绑定手机号
    @staticmethod
    def bd_sj(uid, mobileareacode='+86'):
        try:
            mobile = 15800000000 + int(uid)
            Mobile.create(mobile=mobile, uid=uid)
            Userbase.update(mobile=mobile, mobileareacode=mobileareacode).where(Userbase.uid == uid).execute()
            key = 'hm_userbaseinfo_{}'.format(uid)
            Common.REDIS_INST.hset(key, 'mobile', mobile)
            Common.REDIS_INST.hset(key, 'mobileareacode', mobileareacode)
            key_mobile = 'hm_user_mobile_prefix:{}_{}'.format(mobileareacode, mobile)
            Common.REDIS_INST.set(key_mobile, uid)
            return {'code': 100, 'status': True, 'msg': '绑定手机号成功'}
        except:
            return {'code': 1001, 'status': True, 'msg': '绑定手机号失败'}

    # 注册用户返回uid,或登录返回uid
    @staticmethod
    def register(username):
        password = Common.md5(USER_PWD)
        img = ''
        nickname = username+'nc'
        ret = {'code': 1001, 'status': False, 'msg': '用户名已存在或注册失败'}
        # r = requests.post(URL + '/user/lucky_reg',
        #                   data={'nick_name': username, 'user_pwd': USER_PWD, 'username': username, 'key': 'huomao_lucky'})
        # if r.json()['code'] != '100':
        #     return {'code': 900, 'status': False, 'msg': '注册失败'}
        # else:
        #     uid = r.json()['data']['uid']
        #     return {'code': 100, 'status': True, 'msg': '成功\tuid:{}\t密码:1'.format(uid), 'uid': str(uid)}
        # 验证用户名是否存在
        key_username = 'hm_user_name_redis_prefix:{}'.format(Common.md5(username))
        if Common.REDIS_INST.get(key_username) or UserName.select().where(UserName.username == username).first():
            return ret
        # 创建uid
        uid = Uid().create().id
        print(uid,Common.hash_table(uid))
        # 插入userbase表
        Userbase.create(uid=uid, name=username,email='',mobile='',openid='',weixin='',mobileareacode='')
        # 插入username表
        UserName.create(username=username, uid=uid)
        # 插入userinfo表
        Userinfo.create(uid=uid, password=password, img=img, lv=0)
        # 设置username,redis缓存
        Common.REDIS_INST.set(key_username,uid)
        # 设置uid,redis缓存
        data = dict(nickname=nickname,password=password,img=img,lv=0,regtime=int(time.time()))
        Common.REDIS_INST.set('hm_{}'.format(uid),json.dumps(data))
        # 设置nickname,redis缓存
        Common.REDIS_INST.set('hm_nickname_{}'.format(Common.md5(nickname)),uid)
        # 设置userbase,redis缓存:hm_userbaseinfo_{uid}
        data = dict(uid=uid,name=username,email='',email_activate_stat=0,
                    mobile='',openid='',weixin='',blog='',send_freebean=0,
                    get_experience=0,anchor_experience=0,mobileareacode='')
        # 不知道php为什么要json转义一层再存.
        for key,value in data.items():
            data[key] = json.dumps(value)
        Common.REDIS_INST.hmset('hm_userbaseinfo_{}'.format(uid),data)
        return {'code': 100, 'status': True, 'msg': '成功\tuid:{}\t密码:1'.format(uid), 'uid': str(uid)}

    # 申请直播并通过
    @staticmethod
    def sq_zb(uid):
        # 判断uid是否是主播
        if uid:
            uid = str(uid)
            res = requests.get(URL + '/member/checkUsersIdentify', cookies=Common.generate_cookies(uid))
            if res.json()['data']['isAnchor'] is True:
                return {'code': 900, 'status': False, 'msg': '已是主播'}
            else:
                Common.bd_sj(uid)
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

    # 更新房间状态
    @staticmethod
    def update_stat(cids, stat):
        if cids and stat:
            cids = str(cids)
            cids = cids.split(",")
            for cid in cids:
                channel = HmChannel.select().where(HmChannel.room_number == cid).first()
                cid = channel.id
                if cid:
                    data = {'is_live': stat,
                            'cid': cid,
                            }
                    requests.get(URL + '/plugs/updateRoomLiveStat', params=data)
            return {'code': 100, 'status': True, 'msg': '修改成功'}
        else:
            return {'code': 101, 'status': False, 'msg': '修改失败'}

    # 线上流同步线下
    @staticmethod
    def update_stream(room_xs, room_xx):
        try:
            res = requests.post(ADMIN_URL_ONLINE + '/channel/getChannelList', data={'keyWord': 'roomNum', 'keyContent': room_xs, 'page': 1},
                                cookies=ADMIN_COOKIES)
            stream = etree.HTML(res.text).xpath('//*[@id="matchTable"]/tr[2]/td[2]')[0].text
            # 更新表
            HmChannel.update(stream=stream).where(HmChannel.room_number == room_xx).execute()
            # 获取主播uid
            channel = HmChannel.select().where(HmChannel.room_number == room_xx).first()
            Common.REDIS_INST.hset('hm_channel_anchor_{}'.format(channel.uid), 'stream', '"' + stream + '"')
            return {'code': 100, 'status': True, 'msg': '成功'}
        except Exception as msg:
            print(msg)
            return {'code': 900, 'status': False, 'msg': '失败'}

    # 修改密码
    @staticmethod
    def update_password(uid, password):
        # 生产密码
        uid = str(uid)
        m = hashlib.md5()
        m.update(str(password).encode('utf-8'))
        newpassword = m.hexdigest()
        # 更新表
        Userinfo.update(password=newpassword).where(Userinfo.uid == uid).execute()
        # 更新redis
        data = json.loads(Common.REDIS_INST.get('hm_' + uid))
        data['password'] = newpassword
        Common.REDIS_INST.set('hm_' + uid, json.dumps(data))
        return {'code': 100, 'status': True, 'msg': '成功'}

    # 修改昵称
    @staticmethod
    def update_nick_name(uid, nick_name):
        uid = str(uid)
        # 更新redis
        data = json.loads(Common.REDIS_INST.get('hm_' + uid))
        data['nickname'] = nick_name
        Common.REDIS_INST.set('hm_' + uid, json.dumps(data))
        return {'code': 100, 'status': True, 'msg': '成功'}

    # 修改房间类型0普通，1横板娱乐，2竖版娱乐,hm_pushstream_type_{cid}  1PC 2手机 ,hm_mobile_screenType_outdoor_{cid} 1横屏 2竖屏
    @staticmethod
    def update_roomlx(room_number, status):
        def update_yl(data='no'):
            HmChannel.update(is_entertainment=data).where(HmChannel.room_number == room_number).execute()
            Common.REDIS_INST.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps(data))
            return 1

        if room_number and status or status == '0':
            channel = HmChannel.select().where(HmChannel.room_number == room_number).first()
            uid = channel.uid
            cid = channel.id
            if status == '0':
                # PC直播,非娱乐直播间
                update_yl()
                Common.REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 1)
            elif status == '1':
                # PC直播,娱乐直播间
                update_yl('yes')
                Common.REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 1)
            elif status == '2':
                # 手机直播,非娱乐,横屏
                update_yl()
                Common.REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 2)
                Common.REDIS_INST.set('hm_mobile_screenType_outdoor_{}'.format(cid), 1)
            elif status == '3':
                # 手机直播,非娱乐,竖屏
                update_yl()
                Common.REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 2)
                Common.REDIS_INST.set('hm_mobile_screenType_outdoor_{}'.format(cid), 2)
            elif status == '4':
                # 手机直播,娱乐,横屏
                update_yl('yes')
                Common.REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 2)
                Common.REDIS_INST.set('hm_mobile_screenType_outdoor_{}'.format(cid), 1)
            elif status == '5':
                # 手机直播,娱乐,竖屏
                update_yl('yes')
                Common.REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 2)
                Common.REDIS_INST.set('hm_mobile_screenType_outdoor_{}'.format(cid), 2)
            else:
                return {'code': 101, 'status': False, 'msg': '修改失败'}
            return {'code': 100, 'status': True, 'msg': '修改成功2'}
        else:
            return {'code': 102, 'status': False, 'msg': '修改失败'}

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
        Common.REDIS_INST.delete(key)
        # fg_data = json.loads(Common.REDIS_INST.get(key))
        # print(fg_data)
        # fg_data.pop(uid)
        # Common.REDIS_INST.set(key, json.dumps(fg_data))

    @staticmethod
    def set_fg(cid, uid):
        key = 'hm_channel_admin_{}'.format(cid)
        data = Common.REDIS_INST.get(key)
        fg_data = json.loads(data) if data else {}
        fg_data[uid] = int(time.time())
        Common.REDIS_INST.set(key, json.dumps(fg_data))

    # 初始化用户,房间禁言数据
    @staticmethod
    def init_gag(uid, cid):
        if uid:
            HmGag.delete().where((HmGag.cid == cid) & (HmGag.uid == uid)).execute()
            Common.REDIS_INST.delete('hm_gag_user_{}'.format(uid))
            Common.REDIS_INST.delete('hm_gag_channel_{}'.format(cid))
        return 0

    # 获取经验值
    @staticmethod
    def get_experience(uid):
        u = Userbase.select().where(Userbase.uid == uid).first()
        return u.get_experience, u.anchor_experience

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
            keys.extend(Common.REDIS_INST.keys(key.format_map({'uid': uid, 'cid': '*'})))
        for key in fan_keys[2:6]:
            keys.append(key.format_map({'uid': uid}))
        for key in keys:
            Common.REDIS_INST.delete(key)
        # 删除已获取爱心粉丝值用户
        key = REDIS_KEYS['fans'][6]
        data = json.loads(Common.REDIS_INST.get(key))
        for key, value in data.items():
            if uid in value:
                data[key].remove(uid)
                Common.REDIS_INST.set(key, json.dumps(data))
        return {'msg': '成功'}

    def subscribe(uid):
        key = REDIS_KEYS['subscribe'].format_map({'uid': uid})
        subscribe_data = Common.REDIS_INST.get(key)
        subscribe_data = json.loads(subscribe_data)
        data = {}
        for i in range(1, 211):
            data[i] = []
        subscribe_data['subsList'] = data
        Common.REDIS_INST.set(key, json.dumps(subscribe_data))

    def try_json(data):
        try:
            res = json.loads(data)
            print(res)
            return res
        except ValueError:
            print(data)
            return data
