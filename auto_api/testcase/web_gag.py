#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 18:27:48
# @Author  : lixingyun
import unittest
import sys

sys.path.append('../')
from lib import *
from common.common import Common
from config import super_uid

# Common.generate_room('gag', 3)
# Common.generate_user('gag', 20, True)
# exit()
'''数据准备'''
room = {'anchor': {'uid': '5632', 'name': 'gag1510207934'},
        'fg': {0: {'uid': '5633', 'name': 'gag1510207938'},
               1: {'uid': '5634', 'name': 'gag1510207940'},
               2: {'uid': '5635', 'name': 'gag1510207941'}},
        'room': {'cid': '119491', 'rid': '568788'}}
anchor = room['anchor']['uid']
cid = room['room']['cid']
user = {0: {'uid': '5678', 'name': 'gag1510299920'}, 1: {'uid': '5679', 'name': 'gag1510299922'}, 2: {'uid': '5680', 'name': 'gag1510299923'},
        3: {'uid': '5681', 'name': 'gag1510299925'}, 4: {'uid': '5682', 'name': 'gag1510299927'}, 5: {'uid': '5683', 'name': 'gag1510299928'},
        6: {'uid': '5684', 'name': 'gag1510299929'}, 7: {'uid': '5685', 'name': 'gag1510299931'}, 8: {'uid': '5686', 'name': 'gag1510299932'},
        9: {'uid': '5687', 'name': 'gag1510299934'}, 10: {'uid': '5688', 'name': 'gag1510299936'}, 11: {'uid': '5689', 'name': 'gag1510299937'},
        12: {'uid': '5690', 'name': 'gag1510299939'}, 13: {'uid': '5691', 'name': 'gag1510299940'}, 14: {'uid': '5692', 'name': 'gag1510299942'},
        15: {'uid': '5693', 'name': 'gag1510299943'}, 16: {'uid': '5694', 'name': 'gag1510299944'}, 17: {'uid': '5695', 'name': 'gag1510299946'},
        18: {'uid': '5696', 'name': 'gag1510299948'}, 19: {'uid': '5697', 'name': 'gag1510299949'}}
exps = {
    't': {'code': 4000, 'status': True, 'message': '处理成功！'},
    'f1': {'code': '2018', 'status': False, 'data': [], 'message': '没有权限'},
    'f2': {'code': '4302', 'status': False, 'message': '参数错误！'},
    'f3': {'code': '4418', 'status': False, 'message': '您无权对本房间房管进行禁言'},
    'f4': {'code': '4417', 'status': False, 'message': '您无权对本房间主播进行禁言'},
    'f5': {'code': '4416', 'status': False, 'message': '您无权对超管进行禁言'},
    'f6': {'code': '4421', 'status': False, 'message': '已被禁言'},
    'f7': {'code': '4424', 'status': False, 'message': '处理失败'},
    'f8': {'code': '4426', 'status': False, 'message': '您的权限不够,因不是您禁言的用户'},
    'yz': {'message': '抱歉,您已被禁言!详情请咨询客服!', 'status': False, 'code': 203},
}


# 二次验证方法
def ver(uid, type=1):
    def _ver():
        real_res = Common.send_msg(uid, cid)
        if type:
            exp_res = exps['yz']
        else:
            exp_res = {'code': 200}
        try:
            cmp_dict(exp_res, real_res)
            return True
        except:
            return False

    return _ver


class TestGag(unittest.TestCase):
    def setUp(self):
        # 接口信息
        self.name = '禁言'
        self.url = '/myroom/setCommChannelGag'
        self.method = 'get'
        # 默认报错信息
        self.info = ''
        # 默认登录用户
        self.user = ''
        # 默认请求数据
        self.data = {'cid': cid,  # 房间ID
                     'uid': user[0]['uid'],  # 禁言用户ID
                     'status': 24,
                     'nickname': '',
                     'text': ''
                     }

    '''参数必填检验'''

    def test_gag_01(self):
        '''参数必填检验-未登录'''
        self.exp_res = {'data': [], 'message': '未登录', 'code': '101', 'status': False}

    def test_gag_02(self):
        '''参数必填检验-cid'''
        self.user = anchor
        self.data['cid'] = ''
        self.exp_res = exps['f1']

    def test_gag_03(self):
        '''参数必填检验-uid'''
        self.user = anchor
        self.data['uid'] = ''
        self.exp_res = {'status': False, 'code': '4304', 'message': '用户不存在或参数错误！', 'data': []}

    '''业务-普通用户权限'''

    def test_gag_04(self):
        '''业务-普通用户禁言用户'''
        self.exp_res = exps['f1']
        self.user = user[0]['uid']
        self.data['uid'] = user[1]['uid']

    def test_gag_05(self):
        '''业务-普通用户禁言房管'''
        self.exp_res = exps['f1']
        self.user = user[0]['uid']
        self.data['uid'] = room['fg'][0]['uid']

    def test_gag_06(self):
        '''业务-普通用户禁言房主'''
        self.exp_res = exps['f1']
        self.user = user[0]['uid']
        self.data['uid'] = anchor

    def test_gag_07(self):
        '''业务-普通用户禁言超管'''
        self.exp_res = exps['f1']
        self.user = user[0]['uid']
        self.data['uid'] = super_uid

    '''业务-房管权限'''

    def test_gag_08(self):
        '''业务-房管权限-房管禁言普通用户'''
        self.exp_res = exps['t']
        self.user = room['fg'][0]['uid']
        self.data['uid'] = user[1]['uid']
        # 初始化禁言信息
        Common.init_gag(self.data['uid'], cid)
        self.ver = ver(self.data['uid'])

    def test_gag_09(self):
        '''业务-房管权限-房管禁言房管'''
        self.exp_res = exps['f3']
        self.user = room['fg'][0]['uid']
        self.data['uid'] = room['fg'][1]['uid']

    def test_gag_10(self):
        '''业务-房管权限-房管禁言房主'''
        self.exp_res = exps['f4']
        self.user = room['fg'][0]['uid']
        self.data['uid'] = anchor

    def test_gag_11(self):
        '''业务-房管权限-房管禁言超管'''
        self.exp_res = exps['f5']
        self.user = room['fg'][0]['uid']
        self.data['uid'] = super_uid

    '''业务-房主权限'''

    def test_gag_12(self):
        '''业务-房主权限-房主禁言普通用户'''
        self.exp_res = exps['t']
        self.user = anchor
        self.data['uid'] = user[2]['uid']
        # 初始化禁言信息
        Common.init_gag(self.data['uid'], cid)
        self.ver = ver(self.data['uid'])

    def test_gag_13(self):
        '''业务-房主权限-房主禁言房管'''
        self.exp_res = exps['t']
        self.user = anchor
        self.data['uid'] = room['fg'][2]['uid']
        # 初始化禁言信息
        Common.init_gag(self.data['uid'], cid)
        self.ver = ver(self.data['uid'])

    def test_gag_14(self):
        '''业务-房主权限-房主禁言房主'''
        self.exp_res = exps['f2']
        self.user = anchor
        self.data['uid'] = anchor

    def test_gag_15(self):
        '''业务-房主权限-房主禁言超管'''
        self.exp_res = exps['f5']
        self.user = anchor
        self.data['uid'] = super_uid

    # '''已被禁言用户,再被其他用户禁言操作'''
    #
    # def test_gag_13(self):
    #     '''用户已被房管1,24h禁言,再被房管1,永久禁言'''
    #     user = fg[0]
    #     assert_res(sys._getframe(), 'gag', user, exp_t, status=0, cid=cid, uid=users[3])
    #
    # def test_gag_14(self):
    #     '''用户已被房管1,24h禁言，不能被房管2禁言操作'''
    #     user = fg[1]
    #     assert_res(sys._getframe(), 'gag', user, exp_f6, cid=cid, uid=users[4])
    #
    # def test_gag_15(self):
    #     '''用户已被房管1,24h禁言,被房管2,永久禁言'''
    #     user = fg[1]
    #     assert_res(sys._getframe(), 'gag', user, exp_f6, status=0, cid=cid, uid=users[5])
    #
    # def test_gag_16(self):
    #     '''已被房管1禁言用户,被房主,24h禁言'''
    #     user = fz
    #     assert_res(sys._getframe(), 'gag', user, exp_t, cid=cid, uid=users[6])
    #
    # def test_gag_17(self):
    #     '''已被房管1禁言用户,被房主永久禁言'''
    #     user = fz
    #     assert_res(sys._getframe(), 'gag', user, exp_t, status=0, cid=cid, uid=users[7])
    #
    # def test_gag_18(self):
    #     '''已被房主禁言用户,被房管1,24h禁言'''
    #     user = fg[0]
    #     assert_res(sys._getframe(), 'gag', user, exp_f6, cid=cid, uid=users[8])
    #
    # def test_gag_19(self):
    #     '''已被房主禁言用户,被房管1,永久禁言'''
    #     user = fg[0]
    #     assert_res(sys._getframe(), 'gag', user, exp_f6, status=0, cid=cid, uid=users[9])

    def tearDown(self):
        # 比较结果
        assert_res(self)


class TestDelgag(unittest.TestCase):
    def setUp(self):
        # 接口信息
        self.name = '禁言'
        self.url = '/myroom/delCommUserGag'
        self.method = 'get'
        # 默认报错信息
        self.info = ''
        # 默认登录用户
        self.user = ''
        # 默认请求数据
        self.data = {'cid': cid,  # 房间ID
                     'uid': user[3]['uid'],  # 禁言用户ID
                     'status': 24,
                     'nickname': '',
                     'text': ''
                     }

    '''参数必填检验'''

    def test_delgag_01(self):
        '''参数必填检验-未登录'''
        self.exp_res = {'data': [], 'message': '未登录', 'code': '101', 'status': False}

    def test_delgag_02(self):
        '''参数必填检验-cid'''
        self.user = anchor
        self.data['cid'] = ''
        self.exp_res = exps['f7']

    def test_delgag_03(self):
        '''参数必填检验-uid'''
        self.user = anchor
        self.data['uid'] = ''
        self.exp_res = {'status': False, 'code': '4304', 'message': '用户不存在或参数错误！', 'data': []}

    '''业务-普通用户取消禁言权限'''

    def test_delgag_04(self):
        '''业务-普通用户取消禁言-被房管禁言的用户'''
        self.exp_res = exps['f1']
        self.user = user[3]['uid']
        uid = self.data['uid'] = user[4]['uid']
        # 初始化禁言信息
        Common.init_gag(uid, cid)
        # 房管禁言用户
        Common.gag(uid, room['fg'][0]['uid'], cid)
        self.ver = ver(uid)

    def test_delgag_05(self):
        '''业务-普通用户取消禁言-被房主禁言的用户'''
        self.exp_res = exps['f1']
        self.user = user[3]['uid']
        uid = self.data['uid'] = user[5]['uid']
        # 初始化禁言信息
        Common.init_gag(uid, cid)
        # 房主禁言用户
        Common.gag(uid, anchor, cid)
        self.ver = ver(uid)

    def test_delgag_06(self):
        '''业务-普通用户取消禁言-被超管禁言的用户'''
        self.exp_res = exps['f1']
        self.user = user[3]['uid']
        uid = self.data['uid'] = user[6]['uid']
        # 初始化禁言信息
        Common.init_gag(uid, cid)
        # 超管禁言用户
        Common.gag(uid, super_uid, cid, -1)
        self.ver = ver(uid)

    '''业务-房管取消禁言权限'''

    def test_delgag_07(self):
        '''业务-房管取消禁言权限-被本身禁言的用户'''
        self.exp_res = exps['t']
        self.user = room['fg'][0]['uid']
        uid = self.data['uid'] = user[7]['uid']
        # 初始化禁言信息
        Common.init_gag(uid, cid)
        # 房管禁言用户
        Common.gag(uid, self.user, cid)
        self.ver = ver(uid, 0)

    def test_delgag_08(self):
        '''业务-房管取消禁言权限-被其他房管禁言的用户'''
        self.exp_res = exps['f8']
        self.user = room['fg'][0]['uid']
        uid = self.data['uid'] = user[8]['uid']
        # 初始化禁言信息
        Common.init_gag(uid, cid)
        # 房管禁言用户
        Common.gag(uid, room['fg'][1]['uid'], cid)
        self.ver = ver(uid)

    def test_delgag_09(self):
        '''业务-房管取消禁言权限-被房主禁言的用户'''
        self.exp_res = exps['f8']
        self.user = room['fg'][0]['uid']
        uid = self.data['uid'] = user[9]['uid']
        # 初始化禁言信息
        Common.init_gag(uid, cid)
        # 房主禁言用户
        Common.gag(uid, anchor, cid)
        self.ver = ver(uid)

    def test_delgag_10(self):
        '''业务-房管取消禁言权限-被超管禁言的用户'''
        self.exp_res = exps['f7']
        self.user = room['fg'][0]['uid']
        uid = self.data['uid'] = user[10]['uid']
        # 初始化禁言信息
        Common.init_gag(uid, cid)
        # 超管禁言用户
        Common.gag(uid, super_uid, cid, -1)
        self.ver = ver(uid)

    '''业务-房主取消禁言权限'''

    def test_delgag_11(self):
        '''业务-房主取消禁言权限-被本身禁言的用户'''
        self.exp_res = exps['t']
        self.user = anchor
        uid = self.data['uid'] = user[11]['uid']
        # 初始化禁言信息
        Common.init_gag(uid, cid)
        # 房管禁言用户
        Common.gag(uid, self.user, cid)
        self.ver = ver(uid, 0)

    def test_delgag_12(self):
        '''业务-房主取消禁言权限-被房管禁言的用户'''
        self.exp_res = exps['t']
        self.user = anchor
        uid = self.data['uid'] = user[12]['uid']
        # 初始化禁言信息
        Common.init_gag(uid, cid)
        # 房管禁言用户
        Common.gag(uid, room['fg'][0]['uid'], cid)
        self.ver = ver(uid, 0)

    def test_delgag_13(self):
        '''业务-房管取消禁言权限-被超管禁言的用户'''
        self.exp_res = exps['f7']
        self.user = anchor
        uid = self.data['uid'] = user[13]['uid']
        # 初始化禁言信息
        Common.init_gag(uid, cid)
        # 超管禁言用户
        Common.gag(uid, super_uid, cid, -1)
        self.ver = ver(uid)

    def tearDown(self):
        # 比较结果
        assert_res(self)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDelgag('test_delgag_13'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
