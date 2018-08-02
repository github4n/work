from locust import HttpLocust, TaskSet, task
import time
import hashlib

cid = 3642
cuid = anchor_id = '357855'
domian = 'http://www.huomao.com'


urls_get = [
    '/zt/lucky',
    '/noble/getNoble',
    '/plugs/getCacheTime',
    '/user/checkUserLoginStat',
    '/member/checkUsersIdentify',
    '/money/getUserMoney',
    '/member/retUserLVinfo',
    '/abcde/abcde.json?cur_page=web_channellist&cid=0&gid=0&labelID=0&cache_time=1532498424',
    f'/ajax/checkAnchor?cid={cid}',
    f'/getRoomInfo?cuid={cuid}',
    f'/channels/getChannelAsyncInfoByCIDS?channel_ids={cid}&met=getLiveViews',
    f'/subscribe/checkUserSubByCID?channel_id={cid}&channel_uid=92468&r=0.6584665426116061',
    '/active/winner_notes',
    f'/ajax/getNewGift?cid={cid}&cache_time=1532498442&face_label=0',
    f'/ajax/get_outdoor?cid={cid}',
    '/ajax/goimConf',
    f'/guessnew/roomHasGuess/{cid}',
    '/ajax/getNewGuessAlert',
    f'/rank/getNewRankList.json?cid={cid}&flag=0',
    f'/room/getLevelList?cid={cid}',
    f'/abcdef/abcdef.json?cur_page=web_channeldetailnew&position=room&cid={cid}',
    f'/abcde/abcde.json?cur_page=web_channeldetail&position=room&cid={cid}',
    f'/channels/getConmicInfo?cid={cid}',
    f'/channels/isHaveTreasure?cid={cid}',
    f'/eventBox/isHaveEventTreasure?cid={cid}',
    '/bag/isNewBag',
    '/active_file/WorldCup/getUserFootBallRecord',
    '/plugs/getHotWords',
    f'/lottery/getLotteryStatus?room_number={cid}',
    f'/channels/getLatestMsgList.json?cid={cid}',
    f'/myroom/roomMainUser?cid={cid}',
    '/shield/getShieldList',
    f'/channels/checkin_bp?channel_id={cid}',
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



class UserBehavior(TaskSet):
    @task(1)
    def test(self):
        user_cookies = generate_cookies(357855)
        for url in urls_get:
            self.client.get(domian + url, cookies=user_cookies)
        for key, value in urls_post.items():
            self.client.post(domian + key, data=value, cookies=user_cookies)




class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
    host = 'http://www.huomao.com'


#locust -f Z:\share\locust\load_test.py