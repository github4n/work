from common.common import  Common
import  json

redis_inst = Common().REDIS_INST

# hm_mobile_active_type  手机端广告缓存



# for i in range(3062, 3162):
#     res = r.delete('hm_guard_raffle_once_2017-06-07_{}'.format(i))
#     print(res)mobile_screenType_outdoor
# res = r.get('hm_pushstream_type_100')
# res = r.keys('hm_pushstream*')
# res = [print(key, r.get(key)) for key in r.keys('hm_mobile_screenType_outdoor_2')]
# r.delete('hm_guard_raffle_once_2017-06-07_3851')

# r.rename('hm_guard_raffle_once_2017-06-07_3853','hm_guard_raffle_once_2017-06-06_3853')
# res = r.set('hm_pushstream_type_20', 2) 2手机，1pc
# res = r.set('hm_mobile_screenType_outdoor_20', 2) # 2竖 1横
res = redis_inst.get('hm_goddessUserSign_july_5455')
data = json.loads(res)
print(data)

data['continuitySign'] = 5
data['signInfo'] = {'20170921': True, '20170920': True, '20170919': True, '20170918': True, '20170917': True}
redis_inst.set('hm_goddessUserSign_july_5455', json.dumps(data))
exit()
# res = r.set('hm_mobile_screenType_outdoor_100', 2)

# res = r.set('hm_pushstream_type_100', 2)
# res = r.get('hm_1870709')
# res = redis_inst.get('hm_sign_user:csgo:1522')
# print(res)
# sign = json.loads(res)
# sign['signInfo']={"20170828":1}
# sign['total']=14
# redis_inst.set('hm_sign_user:csgo:1522',json.dumps(sign))
