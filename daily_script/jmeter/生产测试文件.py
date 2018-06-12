import time
import hashlib
import os


filepath = os.getcwd()


def cookies(uid):
    if uid:
        key = 'HUOMAOTV!@#$%^&*137SECRET'
        uid = str(uid)
        ts = str(int(time.time())+86400*30)
        a = uid + str(ts) + key
        b = a.encode('utf-8')
        token = str(hashlib.md5(b).hexdigest())
        cookiestext = 'user_e100fe70f5705b56db66da43c140237c=' + uid + ';user_6b90717037ae096e2f345fde0c31e11b=' + token + ';user_2c691ee7b8307f7fadc5c2c9349dbd7b=' + ts
        # headers = {'user_e100fe70f5705b56db66da43c140237c': uid,
        #            'user_6b90717037ae096e2f345fde0c31e11b': token,
        #            'user_2c691ee7b8307f7fadc5c2c9349dbd7b': ts}
        return uid + ',' + cookiestext
    else:
        return {}


file = open(filepath + r'\testjmeter.txt', 'w', encoding='utf-8')
for uid in range(3060, 3160):
    file.writelines(cookies(uid) + '\n')
# for i in range(0, 500):
#     file.writelines(cookies('3865') + '\n')