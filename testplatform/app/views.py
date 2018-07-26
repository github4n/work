from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse, JsonResponse, HttpResponseRedirect
from huomao.common import Common
from huomao.user import User
from huomao.channel import Channel
from huomao.money import MoneyClass
from huomao.test import test
import json

user = User()
channel = Channel()
money = MoneyClass()


def api_test(request):
    return render(request, 'api_test.html')


def chatroom(request):
    return render(request, 'chatroom.html')


def new_web(request, method=''):
    if method == '':
        return render(request, 'index.html')
    else:
        # 字符串转函数表达式
        return eval(method)(request)


def test_fun(request):
    test()
    return JsonResponse({'msg': '成功'})


def clear_all_cdn_cache(request):
    Common.clear_all_cdn_cache()
    return JsonResponse({'msg': '成功'})


def init_active(request):
    Common.init_active()
    return JsonResponse({'msg': '成功'})


def find_uid(request):
    name = request.POST.get('name')
    res = user.find_uid(name)
    return JsonResponse(res)


def set_money(request):
    uid = request.POST.get('uid')
    if uid:
        xd = request.POST.get('xd')
        coin = request.POST.get('coin')
        bean = request.POST.get('bean')
        noble_coin = request.POST.get('noble_coin')
        money.set_xd(uid, xd)
        money.set_money(uid, coin, bean)
        money.set_noble_coin(uid, noble_coin)
        return JsonResponse({'msg': '成功'})
    else:
        return JsonResponse({'msg': '失败'})


def bd_sj(request):
    uid = request.POST.get('uid')
    res = user.bd_sj(uid)
    return JsonResponse(res)


def register(request):
    name = request.POST.get('name_zc')
    res = user.register(name)
    response = HttpResponse(json.dumps(res))
    cookies = Common.generate_cookies(res.get('uid', 1522))
    for key, value in cookies.items():
        response.set_cookie(key, value, domain='.huomaotv.com.cn', max_age=86400)
    response.set_cookie('user_frontloginstat', 1, domain='.huomaotv.com.cn', max_age=86400 * 7)
    return response


def mn_login(request):
    uid = request.POST.get('uid')
    cookies = Common.generate_cookies(uid)
    response = HttpResponse('')
    for key, value in cookies.items():
        # response.set_cookie(key, value, domain='.huomaotv.com.cn', max_age=86400)
        response.set_cookie(key, value, domain='.huomaotv.com.cn', max_age=86400)
    # response.set_cookie('user_frontloginstat', 1, domain='.huomaotv.com.cn', max_age=86400 * 7)
    response.set_cookie('user_frontloginstat', 1, domain='.huomaotv.com.cn', max_age=86400 * 7)
    return response


def sq_zb(request):
    uid = request.POST.get('uid')
    res = user.sq_zb(uid)
    return JsonResponse(res)


def update_stream(request):
    room_xs = request.POST.get('room_xs')
    room_xx = request.POST.get('room_xx')
    res = channel.update_stream(room_xs, room_xx)
    return JsonResponse(res)


def update_stat(request):
    rooms = request.POST.get('rooms')
    stat = request.POST.get('status')
    res = channel.update_stat(rooms, stat)
    return JsonResponse(res)


def update_roomlx(request):
    room_number = request.POST.get('room_number')
    status = request.POST.get('status')
    res = channel.update_roomlx(room_number, status)
    return JsonResponse(res)


def init_fans(request):
    uid = request.POST.get('uid')
    res = Common.init_fans(uid)
    return JsonResponse(res)


def add_mobile_yzm(request):
    phone = request.POST.get('phone')
    Common.add_mobile_yzm(phone)
    return JsonResponse({'msg': '成功'})


def update_password(request):
    uid = request.POST.get('uid')
    password = request.POST.get('password')
    res = user.update_password(uid, password)
    return JsonResponse(res)


def download(request):
    file_name = request.GET['name']

    def file_iterator(file_name, chunk_size=512):
        file_name = '/home/lucky/share/django/testplatform/app/files/' + file_name
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    # the_file_name = '消息相关功能.xmind'
    response = StreamingHttpResponse(file_iterator(file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(file_name).encode('utf-8')
    return response
