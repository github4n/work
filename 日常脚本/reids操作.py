from common import  redis_inst
import  json


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
# res = r.get('hm_goddessUserSign_july_4282')
# data = json.loads(res)
# data['continuitySign'] = 6
# data['signInfo'] = {'20170724': True, '20170723': True, '20170722': True, '20170721': True, '20170720': True, '20170719': True}
# r.set('hm_goddessUserSign_july_4282', json.dumps(data))
# res = r.set('hm_mobile_screenType_outdoor_100', 2)

# res = r.set('hm_pushstream_type_100', 2)
# res = r.get('hm_1870709')
res = redis_inst.get('hm_sign_user:csgo:1522')
print(res)
sign = json.loads(res)
sign['signInfo']={"20170828":1}
sign['total']=14
redis_inst.set('hm_sign_user:csgo:1522',json.dumps(sign))
