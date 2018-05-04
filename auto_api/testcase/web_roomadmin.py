#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/8/8 17:24
# Author : lixingyun
import unittest
import sys
import time
import json

sys.path.append('../')
from lib import assert_res, cmp_dict
from huomao.common import Common

'''数据准备'''
# Common.generate_room('ra', 6)
# Common.generate_user('ra', 6)
# exit()
room = {'fg': {0: {'uid': '5666', 'name': 'ra1510284846'},
               1: {'uid': '5667', 'name': 'ra1510284847'},
               2: {'uid': '5668', 'name': 'ra1510284849'},
               3: {'uid': '5669', 'name': 'ra1510284851'},
               4: {'uid': '5670', 'name': 'ra1510284853'},
               5: {'uid': '5671', 'name': 'ra1510284854'}},
        'anchor': {'uid': '5665', 'name': 'ra1510284841'},
        'room': {'cid': '119495', 'rid': '703693'}}
anchor = room['anchor']['uid']
cid = room['room']['cid']
user = {0: {'uid': '5672', 'name': 'ra1510284856'}, 1: {'uid': '5673', 'name': 'ra1510284858'}, 2: {'uid': '5674', 'name': 'ra1510284859'},
        3: {'uid': '5675', 'name': 'ra1510284861'}, 4: {'uid': '5676', 'name': 'ra1510284863'}, 5: {'uid': '5677', 'name': 'ra1510284864'}}


# 二次验证方法
def ver(uid, type=1):
    def _ver():
        real_res = Common.send_msg(uid, cid)
        if type:
            exp_res = {'code': 200, 'data': {'extend': {'is_fg': '1'}}}
        else:
            exp_res = {'code': 200, 'data': {'extend': {'is_fg': '0'}}}
        try:
            cmp_dict(exp_res, real_res)
            return True
        except Exception as e:
            print(e)
            return False

    return _ver


class TestSetRoomAdmin(unittest.TestCase):
    def setUp(self):
        # 接口信息,后端只用了uid
        self.name = '设置房管'
        self.url = '/myroom/setRoomAdministrator'
        self.method = 'post'
        # 默认报错信息
        self.info = ''
        # 默认登录用户
        self.user = ''
        # 默认请求数据
        self.data = {
            'uid': '',
            'username': '',
        }
        # 删除当前房管信息
        Common.del_fg(cid)

    '''参数必填检验'''

    def test_setroomadmin_01(self):
        '''参数必填检验-未登录'''
        self.exp_res = {'message': '未登录', 'data': [], 'code': '101', 'status': False}

    def test_setroomadmin_02(self):
        '''参数必填检验-username'''
        self.exp_res = {'data': [], 'code': '4302', 'status': False, 'message': '该昵称不存在'}
        self.user = anchor
        self.data['uid'] = user[0]['uid']

    '''业务-用户权限'''

    def test_setroomadmin_03(self):
        '''业务-用户权限-用户设置普通用户为房管'''
        self.exp_res = {'message': '参数错误！', 'code': '4302', 'status': False, 'data': []}
        self.user = user[0]['uid']
        self.data['username'] = user[1]['name']

    '''业务-房管权限'''

    def test_setroomadmin_04(self):
        '''业务-用户权限-房管设置普通用户为房管'''
        self.exp_res = {'message': '参数错误！', 'code': '4302', 'status': False, 'data': []}
        self.user = room['fg'][0]['uid']
        # 因为初始化删除了房管,所以重新设置
        Common.set_fg(cid, self.user)
        self.data['username'] = user[2]['name']

    '''业务-房主权限'''

    def test_setroomadmin_05(self):
        '''业务-房主权限-房主设置普通用户为房管'''
        self.exp_res = {'code': 200, 'status': True, 'message': '处理成功！'}
        self.user = anchor
        self.data['username'] = user[2]['name']
        self.ver = ver(user[2]['uid'])

    def test_setroomadmin_06(self):
        '''业务-房主权限-房主设置房管为房管'''
        self.exp_res = {'code': '266', 'status': False, 'message': '已经是房管'}
        self.user = anchor
        Common.set_fg(cid, room['fg'][1]['uid'])
        self.data['username'] = room['fg'][1]['name']

    def test_setroomadmin_07(self):
        '''业务-房主权限-房主设置房主为房管'''
        self.exp_res = {'data': [], 'code': '4302', 'message': '无法对自己进行设置', 'status': False}
        self.user = anchor
        self.data['username'] = room['anchor']['name']

    '''业务-房管已达到上限'''

    def test_setroomadmin_08(self):
        '''业务-房管已达到上限'''
        self.exp_res = {'code': '4305', 'status': False, 'message': '房管最多10位'}
        self.user = anchor
        self.data['username'] = user[3]['name']
        Common.REDIS_INST.set('hm_channel_admin_{}'.format(cid), json.dumps({i: int(time.time()) for i in range(1, 11)}))

    def tearDown(self):
        # 比较结果
        assert_res(self)


class TestDelRoomAdmin(unittest.TestCase):
    def setUp(self):
        # 接口信息,后端只用uid
        self.name = '取消房管'
        self.url = '/myroom/delRoomAdministrator'
        self.method = 'post'
        # 默认报错信息
        self.info = ''
        # 默认登录用户
        self.user = ''
        # 默认请求数据
        self.data = {
            'uid': '',
            'username': '',
        }
        # 删除当前房管信息
        Common.del_fg(cid)

    '''参数必填检验'''

    def test_delroomadmin_01(self):
        '''参数必填检验-未登录'''
        self.exp_res = {'message': '未登录', 'data': [], 'code': '101', 'status': False}

    def test_delroomadmin_02(self):
        '''参数必填检验-uid'''
        self.exp_res = {'status': False, 'data': [], 'code': '4304', 'message': '用户不存在或参数错误！'}
        self.user = anchor
        self.data['username'] = user[4]['name']

    '''业务-用户权限'''

    def test_delroomadmin_03(self):
        '''业务-用户权限-用户取消房管'''
        self.exp_res = {'code': '4303', 'data': [], 'message': '房间号不存在或参数错误！', 'status': False}
        self.user = user[5]['uid']
        Common.set_fg(cid, room['fg'][2]['uid'])
        self.data['uid'] = room['fg'][2]['uid']

    '''业务-房管权限'''

    def test_delroomadmin_04(self):
        '''业务-用户权限-房管取消房管'''
        self.exp_res = {'data': [], 'code': '4303', 'message': '房间号不存在或参数错误！', 'status': False}
        self.user = room['fg'][3]['uid']
        Common.set_fg(cid, room['fg'][3]['uid'])
        Common.set_fg(cid, room['fg'][4]['uid'])
        self.data['uid'] = room['fg'][4]['uid']

    '''业务-房主权限'''

    def test_delroomadmin_05(self):
        '''业务-房主权限-房主取消房管'''
        self.exp_res = {'code': '4000', 'status': True, 'message': '处理成功！'}
        self.user = anchor
        Common.set_fg(cid, room['fg'][5]['uid'])
        self.data['uid'] = room['fg'][5]['uid']
        self.ver = ver(room['fg'][5]['uid'], 0)

    def test_delroomadmin_06(self):
        '''业务-房主权限-房主取消普通用户'''
        self.exp_res = {'message': '用户不存在或参数错误！', 'code': '4304', 'status': False, 'data': []}
        self.user = anchor
        self.data['uid'] = user[5]['name']

    def tearDown(self):
        # 比较结果
        assert_res(self)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDelRoomAdmin('test_delroomadmin_06'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
