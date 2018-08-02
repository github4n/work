#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/7/13 14:26
# Author : lixingyun
# Description :
import time
import hashlib
import requests

cid = 1001
cuid = anchor_id = '92468'
domian = 'http://www.huomao.com'

urls_get = [
    '/zt/ceshi',
    '/noble/getNoble',
    '/plugs/getCacheTime',
    '/user/checkUserLoginStat',
    '/member/checkUsersIdentify',
    '/money/getUserMoney',
    '/member/retUserLVinfo',
    '/abcde/abcde.json?cur_page=web_channellist&cid=0&gid=0&labelID=0&cache_time=1532498424',
    '/ajax/checkAnchor?cid={}'.format(cid),
    '/getRoomInfo?cuid={}'.format(cuid),
    '/channels/getChannelAsyncInfoByCIDS?channel_ids={}&met=getLiveViews'.format(cid),
    '/subscribe/checkUserSubByCID?channel_id={}&channel_uid=92468&r=0.6584665426116061'.format(cid),
    '/active/winner_notes',
    '/ajax/getNewGift?cid={}&cache_time=1532498442&face_label=0'.format(cid),
    '/ajax/get_outdoor?cid={}'.format(cid),
    '/ajax/goimConf',
    '/guessnew/roomHasGuess/{}'.format(cid),
    '/ajax/getNewGuessAlert',
    '/rank/getNewRankList.json?cid={}&flag=0'.format(cid),
    '/room/getLevelList?cid={}'.format(cid),
    '/abcdef/abcdef.json?cur_page=web_channeldetailnew&position=room&cid={}'.format(cid),
    '/abcde/abcde.json?cur_page=web_channeldetail&position=room&cid={}'.format(cid),
    '/channels/getConmicInfo?cid={}'.format(cid),
    '/channels/isHaveTreasure?cid={}'.format(cid),
    '/eventBox/isHaveEventTreasure?cid={}'.format(cid),
    '/bag/isNewBag',
    '/active_file/WorldCup/getUserFootBallRecord',
    '/plugs/getHotWords',
    '/lottery/getLotteryStatus?room_number={}'.format(cid),
    '/channels/getLatestMsgList.json?cid={}'.format(cid),
    '/myroom/roomMainUser?cid={}'.format(cid),
    '/shield/getShieldList',
    '/channels/checkin_bp?channel_id={}'.format(cid),
    '/Popup/show'
]
urls_post = {
    '/task/minTask': dict(post_data=1),
    '/chatnew/joinMsg': dict(cid=cid, anchor_id=anchor_id, is_yule=0)
}



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

def test_requests(uid):
    user_cookies = generate_cookies(uid)
    for url in urls_get:
        r = requests.get(domian + url, cookies=user_cookies)
    for key, value in urls_post.items():
        requests.post(domian + key, data=value, cookies=user_cookies)