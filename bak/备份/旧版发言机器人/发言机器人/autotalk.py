#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import socket
import time
import urllib.request
import urllib
import hashlib
import random
import json
import struct
import threading
import os


datafile = os.getcwd()


def headers(uid):
    if uid:
        key = 'HUOMAOTV!@#$%^&*137SECRET'
        uid = str(uid)
        ts = str(int(time.time()))
        a = uid + str(ts) + key
        b = a.encode('utf-8')
        token = str(hashlib.md5(b).hexdigest())
        headers = {'Cookie': 'user_e100fe70f5705b56db66da43c140237c=' + uid +
                   '; user_6b90717037ae096e2f345fde0c31e11b=' + token +
                   '; user_2c691ee7b8307f7fadc5c2c9349dbd7b=' + ts}
        return headers
    else:
        return {}

    # 请求|method:方法名|data:数据|uid:请求的headers|type:请求方式默认get


def request(url, method, data, requesttype=None, uid=None):
    if requesttype:
        data = urllib.parse.urlencode(data)
        # post数据需要转换bite
        data = data.encode('utf8')
        res = urllib.request.Request(url + method, data, headers(uid))
    else:
        data = urllib.parse.urlencode(data)
        res = urllib.request.Request(
            url + method + data, headers=headers(uid))
    data = urllib.request.urlopen(res)
    data1 = data.read().decode('utf-8')
    data2 = json.loads(data1[1:-1])
    # print(data1)
    # return data2['data']
    print(data2)
    return data2

# 连接聊天室


def connect(url, cid, uid, fydata):
    data = request(url, '/chat/getToken?', {'cid': cid}, 'post', uid=uid)
    data = data['data']
    HOST = data['host']
    PORT = int(data['port'])
    token = data['token']
    # print(HOST, PORT)
    # 定义socket类型，网络通信，TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # 关键代码binascii.a2b_hex
    a = b'{"sys":{"type":"pomelo-flash-tcp","pomelo_version":"0.7.x","version":"0.1.6b"},"user":null}'
    a = struct.pack('!hh' + str(len(a)) + 's', 256, len(a), a)
    print('连接system')
    s.send(a)
    data = s.recv(1024)
    # 发送某东西
    c = b'\x02\x00\x00\x00'
    print('发送某心跳')
    s.send(c)

    b = '\x00\x01 gate.gateHandler.lookupConnector{"channelId":"' + \
        cid + '","userId":' + uid + ',"log":true}'
    b = b.encode('utf-8')
    b = struct.pack('!hh' + str(len(b)) + 's', 1024, len(b), b)
    print('连接负载服务器')
    s.send(b)
    data = s.recv(1024)
    data2 = data.decode('utf-8')
    data3 = data2[6:]
    data3 = json.loads(data3)

    # s.close()
    host2 = data3['host']
    port2 = data3['port']
    # print((host2, port2))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host2, port2))
    # a = struct.pack('!hh' + str(len(a)) + 's', 256, len(a), a)
    print('再次连接system')
    s.send(a)
    data = s.recv(1024)
    e = b'\x02\x00\x00\x00'
    # c = struct.pack('!h', 512)
    print('发送某心跳')
    s.send(e)

    d = '\x00\x02 connector.connectorHandler.login{"channelId":"' + cid + '","token":"' + token + '","userId":' + uid + '}'
    d = d.encode('utf-8')
    d = struct.pack('!hh' + str(len(d)) + 's', 1024, len(d), d)
    print('连接聊天室')
    s.send(d)
    data = s.recv(1024)
    # print(data)
    datax = {'cid': cid,
             'data': fydata,
             'msg_type': 'msg',
             'msg_send_type': 'msg'}

    aa = request(url, '/chat/sendMsg?', datax, uid=uid)
    print('*' * 150)
    print(fydata)
    print(aa)
    print('*' * 150)
    if aa['code'] == 200:
        print('消息发送成功')


def fy(url, cid, uid, ttime=2):
    dir2 = datafile + r'\弹幕.txt'
    f = open(dir2, 'r', encoding='utf-8')
    tms = []
    for line in f:
        tms.append(line)
    while True:
        fydata = tms[random.randint(1, len(tms))]
        connect(url, cid, uid, fydata)
        time.sleep(ttime)

# cid房间号，users用户数量，发言间隔时间


def tmjqr(url, cid, users, ttime):
    dir1 = datafile + r'\uid.txt'
    f = open(dir1, 'r', encoding='utf-8')
    uids = []
    for line in f:
        line = line.strip('\n')
        uids.append(line)
    # 随机获取用户数量的uid
    uidss = random.sample(uids, users)
    # print(uidss)
    # for i in range(len(uidss)):
    #     print(cid, uidss[i])
    threads = []
    for i in range(len(uidss)):
        t = threading.Thread(target=fy, args=(url, cid, uidss[i], ttime))
        threads.append(t)

    for t in threads:
        t.start()


class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, '发言机器人', size=(250, 210))
        # panel面板
        panel = wx.Panel(self, -1,)
        # 静态文本环境选择
        self.label0 = wx.StaticText(panel, -1, '环境选择:', (20, 15))
        # 选择框框环境选择
        self.rb1 = wx.RadioButton(panel, -1, '线下', (110, 10))
        self.rb2 = wx.RadioButton(panel, -1, '线上', (170, 10))
        # self.text0 = wx.TextCtrl(panel, -1, '3', (110, 10))
        # 静态文本房间号
        self.label1 = wx.StaticText(panel, -1, '房间号cid:', (20, 45))
        # 输入框房间号
        self.text1 = wx.TextCtrl(panel, -1, '2', (110, 40))
        # 静态文本同时发言用户数
        self.label2 = wx.StaticText(panel, -1, '同时发言用户数:', (20, 75))
        # 输入框同时发言用户数
        self.text2 = wx.TextCtrl(panel, -1, '10', (110, 70))
        # 静态文本发言间隔
        self.label3 = wx.StaticText(panel, -1, '发言间隔:', (20, 105))
        # 输入框发言间隔
        self.text3 = wx.TextCtrl(panel, -1, '2', (110, 100))
        # 执行按键
        self.button = wx.Button(panel, -1, '执行', (20, 130))
        self.Bind(wx.EVT_BUTTON, self.OnbuttonClick, self.button)
        self.Centre()
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnbuttonClick(self, event):
        cid = self.text1.GetValue()
        users = self.text2.GetValue()
        ttime = self.text3.GetValue()
        urltype = self.rb1.GetValue()
        if urltype:
            url = 'http://qa.new.huomaotv.com.cn'
        else:
            url = 'http://www.huomao.com'
        print(url, cid, users, ttime)
        tmjqr(url, str(cid), int(users), int(ttime))

    def OnClose(self, evt):
        ret = wx.MessageBox('Do you really want to leave?', 'Confirm', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            os._exit(0)
            # do something here...
            evt.Skip()


app = wx.App()
f = MyFrame()
f.Show()
app.MainLoop()


