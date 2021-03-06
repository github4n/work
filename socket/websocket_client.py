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
import multiprocessing

# ws_url = "ws://gate-65.huomao.com:8090/sub"
# url = 'https://www.huomao.com/'
ws_url = 'ws://gate.huomaotv.com.cn:8090/sub'
url = 'http://qa.new.huomaotv.com.cn'

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
            print("receive: heartbeat")
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
    data = json.loads(data)
    if data.get('code') == '300002':
        cid = data['gift']['channel']['rid']
        print(cid,'有宝箱')
        ret = requests.get(f'{url}/channels/isHaveTreasure?cid={cid}').json()
        for key, value in ret.items():
            if key != 'count':
                treasure_key = value['key']
                countdown = int(value['countdown'])
                t = threading.Thread(target=get_bx, args=(countdown, cid, treasure_key))
                t.start()



def get_bx(countdown, cid, treasure_key):
    time.sleep(countdown)
    ret = requests.get(f'{url}/chatnew/getTreasure?cid={cid}&treasure_key={treasure_key}',
                       cookies=Common.generate_cookies(1522))
    print(ret.json())


connect(0, 1)
