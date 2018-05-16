#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/11/14 15:52
# Author : lixingyun
import time
import json
from websocket import create_connection
import struct
import threading
import multiprocessing

# url = "ws://gate-61.huomao.com:8090/sub"
url = 'ws://gate.huomaotv.com.cn:8090/sub'
ws = create_connection(url)

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
        fmt = '!ihhii{}s'.format(token_len)
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
            data = json.loads(msg)
            print(data)
            # for offset in range(0, result.__len__(), packetLen):
            #     (packetLen, headerLen, ver) = struct.unpack_from('!ihh', result,offset)
            #     print(packetLen, headerLen, ver)
            #     # print(result)
            #     print((result[headerLen:packetLen]).decode())



connect(23399, 1001)

