#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import time
import hashlib
import random
import os
import aiohttp
import asyncio
import threading


datafile = os.getcwd()
uids = []
file1 = open(datafile + r'\uid.txt', 'r', encoding='utf-8')
for line in file1:
    line = line.strip('\n')
    uids.append(line)
file2 = open(datafile + r'\弹幕.txt', 'r', encoding='utf-8')
msgs = []
for line in file2:
    line = line.strip('\n')
    msgs.append(line)
# print(uids)
uid_count = len(uids)
# print(uid_count)
msgs_count = len(msgs)
# print(msgs)
file1.close()
file2.close()


def cookies(uid):
    if uid:
        key = 'HUOMAOTV!@#$%^&*137SECRET'
        uid = str(uid)
        ts = str(int(time.time()))
        a = uid + str(ts) + key
        b = a.encode('utf-8')
        token = str(hashlib.md5(b).hexdigest())
        headers = {'user_e100fe70f5705b56db66da43c140237c': uid,
                   'user_6b90717037ae096e2f345fde0c31e11b': token,
                   'user_2c691ee7b8307f7fadc5c2c9349dbd7b': ts}
        return headers
    else:
        return {}


async def test_async(domain, cid, uid, dm):

    print(dm)
    if dm != '0':
        dm = str(random.randint(1, 6))
    msg = msgs[random.randint(0, msgs_count - 1)]
    url = domain + '/chat/sendMsg?data=' + msg + '&cid=' + str(cid) + '&msg_type=msg&msg_send_type=msg&color_barrage=' + dm
    print(url)
    async with aiohttp.request('POST', url + str(), cookies=cookies(uid)) as r:
        data = await r.text()
    return data


def test(domain, cid, users, dm):
    start = time.time()
    event_loop = asyncio.get_event_loop()
    uidss = random.sample(uids, users)
    # print(uidss)
    tasks = [test_async(domain, cid, uid, dm) for uid in uidss]
    results = event_loop.run_until_complete(asyncio.gather(*tasks))
    # for result in results:
    #     print(result)
    # print('Use asyncio+aiohttp cost: {}'.format(time.time() - start))


def test_fy(domain, cid, users, ttime, dm):
    users = int(users)
    if users >= uid_count:
        users = uid_count
    while True:
        test(domain, cid, users, dm)
        time.sleep(int(ttime))

# test_fy('http://qa.new.huomaotv.com.cn', 12,3,2)


class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, '发言机器人', size=(250, 280))
        # panel面板
        panel = wx.Panel(self, -1,)
        # 文件UID数量：
        self.label4 = wx.StaticText(panel, -1, '文件UID数量:', (20, 15))
        # 文件UID数量
        self.text4 = wx.TextCtrl(panel, -1, str(uid_count), (110, 15), style=wx.TE_READONLY)
        # 静态文本环境选择
        self.label0 = wx.StaticText(panel, -1, '环境选择:', (20, 45))
        # 选择框框环境选择
        self.rb1 = wx.RadioButton(panel, -1, '线下', (110, 45))
        self.rb2 = wx.RadioButton(panel, -1, '线上', (170, 45))
        # self.text0 = wx.TextCtrl(panel, -1, '3', (110, 10))
        # 静态文本房间号
        self.label1 = wx.StaticText(panel, -1, '房间号cid:', (20, 75))
        # 输入框房间号
        self.text1 = wx.TextCtrl(panel, -1, '12', (110, 75))
        # 静态文本发言用户数
        self.label2 = wx.StaticText(panel, -1, '发言用户数:', (20, 105))
        # 输入框发言用户数
        self.text2 = wx.TextCtrl(panel, -1, '10', (110, 105))
        # 静态文本发言间隔
        self.label3 = wx.StaticText(panel, -1, '发言间隔:', (20, 135))
        # 输入框发言间隔
        self.text3 = wx.TextCtrl(panel, -1, '2', (110, 135))
        # 是否彩色弹幕
        self.label4 = wx.StaticText(panel, -1, '是否彩色弹幕:', (20, 165))
        self.text4 = wx.TextCtrl(panel, -1, '0', (110, 165))
        # 执行按键
        self.button1 = wx.Button(panel, -1, '执行', (130, 195))
        # 暂停按键
        self.Bind(wx.EVT_BUTTON, self.OnbuttonClick, self.button1)
        self.Centre()
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnbuttonClick(self, event):
        cid = self.text1.GetValue()
        users = self.text2.GetValue()
        ttime = self.text3.GetValue()
        dm = self.text4.GetValue()
        domain = self.rb1.GetValue()
        if domain:
            domain = 'http://qa.new.huomaotv.com.cn'
        else:
            domain = 'https://www.huomao.com'
        # print(cid, users, time, domain)
        test_fy(domain, cid, users, ttime, dm)

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
