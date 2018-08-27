#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/11/14 15:52
# Author : lixingyun
import time
import json
from websocket import create_connection
import struct
import threading
import requests
from huomao.common import Common
import random
import multiprocessing

ip_pool = ['219.141.153.41:80']

ws_url = "ws://gate-65.huomao.com:8090/sub"
url = 'http://www.huomao.com/'
uid = 18398171
proxies = {'http': random.choice(ip_pool)}
# ws_url = 'ws://gate.huomaotv.com.cn:8090/sub'
# url = 'http://qa.new.huomaotv.com.cn'
# uid = 1522
# proxies = False

ws = create_connection(ws_url)
rawHeaderLen = 16
packetOffset = 0
headerOffset = 4
verOffset = 6
opOffset = 8
seqOffset = 12


def connect(uid, cid):
    tokenBody = {"Uid": uid, "Rid": cid}
    token = bytes(json.dumps(tokenBody).encode())
    token_len = len(token)

    def auth():
        print('开始验证')
        fmt = f'!ihhii{token_len}s'
        data = struct.pack(fmt, rawHeaderLen + token_len, rawHeaderLen, 1, 7, 1, token)
        ws.send(data)

    def heartbeat():
        while True:
            data = struct.pack('!ihhii', rawHeaderLen, rawHeaderLen, 1, 2, 1)
            ws.send(data)
            time.sleep(30)

    auth()

    while True:
        result = ws.recv()
        # print(result)
        # 解包数据
        (packetLen, headerLen, ver, op, seq) = struct.unpack_from('!ihhii', result)
        # print((packetLen, headerLen, ver, op, seq))
        if op == 8:
            t = threading.Thread(target=heartbeat)
            t.start()
        elif op == 3:
            # print("receive: heartbeat")
            pass
        elif op == 5:
            msg = (result[headerLen:packetLen]).decode()
            t2 = threading.Thread(target=bx, args=(msg,))
            t2.start()
            # data = json.loads(msg)

            # for offset in range(0, result.__len__(), packetLen):
            #     (packetLen, headerLen, ver) = struct.unpack_from('!ihh', result,offset)
            #     print(packetLen, headerLen, ver)
            #     # print(result)
            #     print((result[headerLen:packetLen]).decode())


def bx(data):
    try:
        data = json.loads(data)
        if data.get('code') == '300002':
            cid = data['gift']['channel']['cid']
            print(cid, '有普通宝箱')
            ret = requests.get(f'{url}/channels/isHaveTreasure?cid={cid}', proxies=proxies).json()
            for key, value in ret.items():
                if key != 'count':
                    treasure_key = value['key']
                    countdown = int(value['countdown'])
                    t = threading.Thread(target=get_bx, args=(countdown, cid, treasure_key))
                    t.start()
        elif data.get('code') == '888888':
            cid = data['allStation']['bannerWords']['targetUrl']
            print(cid, '有赛事宝箱')
            ret = requests.get(f'{url}/eventBox/isHaveEventTreasure?cid={cid}',
                               cookies=Common.generate_cookies(uid),
                               proxies=proxies).json()
            if ret['status']:
                treasure_id = ret['data']['id']
                open_time = int(ret['data']['open_time'])
                t = threading.Thread(target=get_ssbx, args=(open_time, cid, treasure_id))
                t.start()
    except Exception as e:
        print(e)


def get_ssbx(open_time, cid, treasure_id):
    time.sleep(open_time)
    ret = requests.get(f'{url}/EventBox/getEventTreasure?treasure_id={treasure_id}&cid={cid}',
                       cookies=Common.generate_cookies(uid),
                       proxies=proxies)
    print(ret.json())


def get_bx(countdown, cid, treasure_key):
    time.sleep(countdown)
    ret = requests.get(f'{url}/chatnew/getTreasure?cid={cid}&treasure_key={treasure_key}',
                       cookies=Common.generate_cookies(uid),
                       proxies=proxies)
    print(ret.json())


connect(0, 1)
