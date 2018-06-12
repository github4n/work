from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse, JsonResponse
from huomao.common import Common
from huomao.user import User
from huomao.channel import Channel
from huomao.money import MoneyClass
from huomao.test import test

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
    return JsonResponse(res)


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


def update_password(request):
    uid = request.POST.get('uid')
    password = request.POST.get('password')
    res = user.update_password(uid, password)
    return JsonResponse(res)


def download(request):
    file_name = request.GET['name']

    def file_iterator(file_name, chunk_size=512):
        file_name = '/home/lucky/share/django/project/app/files/' + file_name
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


def set_cookies(request):
    response = HttpResponse('test')
    response.set_cookie('cookies_test', 'test', domain='.huomaotv.com.cn')
    return response

    # def phone_fy(request):
    #     cid = request.POST.get('cid_fy')
    #     data = request.POST.get('data_fy')
    #     uid = request.POST.get('uid_fy')
    #     if Common.phone_fy(cid, data, uid):
    #         return {'msg': '成功'}
    #     else:
    #         return {'msg': '失败'}
    #
    #
    # def phone_sl(request):
    #     cid = request.POST.get('cid_sl')
    #     uid = request.POST.get('uid_sl')
    #     t_count = request.POST.get('t_count')
    #     pos = request.POST.get('pos')
    #     gift = request.POST.get('giftid')
    #     print((cid, uid, t_count, pos, gift))
    #     if Common.phone_sl(cid, uid, t_count, pos, gift):
    #         return {'msg': '成功'}
    #     else:
    #         return {'msg': '失败'}
    #
    #
    # def phone_sd(request):
    #     cid = request.POST.get('cid_sd')
    #     uid = request.POST.get('uid_sd')
    #     if Common.phone_sd(cid, uid):
    #         return {'msg': '成功'}
    #     else:
    #         return {'msg': '失败'}
