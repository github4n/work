import redis
r = redis.Redis(host='192.168.23.14', port=6379, db=0)
r.delete('hm_subject_guess_user_119207')
r.set('hm_subject_guess_119207', '[]')
