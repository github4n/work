#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/4 16:54
# Author : lixingyun
# Description :
from .db.contents import HmChannel
import requests
import json
from lxml import etree
from .common import REDIS_INST, REDIS_INST2
from .config import ADMIN_URL_ONLINE, ADMIN_COOKIES


class Channel():
    # 更新房间状态
    @staticmethod
    def update_stat(cids, stat):
        if cids and stat:
            cids = str(cids)
            cids = cids.split(",")
            for cid in cids:
                channel = HmChannel.select().where(HmChannel.room_number == cid).first()
                if channel:
                    HmChannel.update(is_live=stat).where(HmChannel.room_number == cid).execute()
                    uid = channel.uid
                    key = 'hm_channel_views:{}'.format(uid)
                    REDIS_INST2.hset(key, 'is_live', stat)
                    REDIS_INST.hset('hm_channel_anchor_{}'.format(uid), 'is_live', json.dumps(stat))
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
            REDIS_INST.hset('hm_channel_anchor_{}'.format(channel.uid), 'stream', '"' + stream + '"')
            return {'code': 100, 'status': True, 'msg': '成功'}
        except Exception as msg:
            print(msg)
            return {'code': 900, 'status': False, 'msg': '失败'}

    # 修改房间类型0普通，1横板娱乐，2竖版娱乐,hm_pushstream_type_{cid}  1PC 2手机 ,hm_mobile_screenType_outdoor_{cid} 1横屏 2竖屏
    @staticmethod
    def update_roomlx(room_number, status):
        def update_yl(data='no'):
            HmChannel.update(is_entertainment=data).where(HmChannel.room_number == room_number).execute()
            REDIS_INST.hset('hm_channel_anchor_{}'.format(uid), 'is_entertainment', json.dumps(data))
            return 1

        if room_number and status or status == '0':
            channel = HmChannel.select().where(HmChannel.room_number == room_number).first()
            uid = channel.uid
            cid = channel.id
            if status == '0':
                # PC直播,非娱乐直播间
                update_yl()
                REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 1)
            elif status == '1':
                # PC直播,娱乐直播间
                update_yl('yes')
                REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 1)
            elif status == '2':
                # 手机直播,非娱乐,横屏
                update_yl()
                REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 2)
                REDIS_INST.set('hm_mobile_screenType_outdoor_{}'.format(cid), 1)
            elif status == '3':
                # 手机直播,非娱乐,竖屏
                update_yl()
                REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 2)
                REDIS_INST.set('hm_mobile_screenType_outdoor_{}'.format(cid), 2)
            elif status == '4':
                # 手机直播,娱乐,横屏
                update_yl('yes')
                REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 2)
                REDIS_INST.set('hm_mobile_screenType_outdoor_{}'.format(cid), 1)
            elif status == '5':
                # 手机直播,娱乐,竖屏
                update_yl('yes')
                REDIS_INST.set('hm_pushstream_type_{}'.format(cid), 2)
                REDIS_INST.set('hm_mobile_screenType_outdoor_{}'.format(cid), 2)
            else:
                return {'code': 101, 'status': False, 'msg': '修改失败'}
            return {'code': 100, 'status': True, 'msg': '修改成功2'}
        else:
            return {'code': 102, 'status': False, 'msg': '修改失败'}
