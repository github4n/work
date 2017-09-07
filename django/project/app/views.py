from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse, JsonResponse
from .forms import TestForm
from common.common import Common

common = Common()


def new_web(request, method=''):
    if method == '':
        return render(request, 'new_web.html')
    else:
        # 字符串转函数表达式
        return eval(method)(request)


def find_uid(request):
    name = request.POST.get('name')
    res = common.find_uid(name)
    return JsonResponse(res)


def set_money(request):
    uid = request.POST.get('uid')
    if uid:
        xd = request.POST.get('xd')
        coin = request.POST.get('coin')
        bean = request.POST.get('bean')
        common.set_xd(uid, xd)
        common.set_money(uid, coin, bean)
        return JsonResponse({'msg': '成功'})
    else:
        return JsonResponse({'msg': '失败'})

def bd_sj(request):
    uid = request.POST.get('uid')
    res = common.bd_sj(uid)
    return JsonResponse(res)


def zc(request):
    name = request.POST.get('name_zc')
    res = common.zc(name)
    return JsonResponse(res)


def sq_zb(request):
    uid = request.POST.get('uid')
    res = common.sq_zb(uid)
    return JsonResponse(res)


def update_stream(request):
    room_xs = request.POST.get('room_xs')
    room_xx = request.POST.get('room_xx')
    res = common.update_stream(room_xs, room_xx)
    return JsonResponse(res)


def update_stat(request):
    cids = request.POST.get('rooms')
    stat = request.POST.get('status')
    res = common.update_stat(cids, stat)
    return JsonResponse(res)


def update_roomlx(request):
    room_number = request.POST.get('room_number')
    status = request.POST.get('status')
    res = common.update_roomlx(room_number, status)
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



    # def phone_fy(request):
    #     cid = request.POST.get('cid_fy')
    #     data = request.POST.get('data_fy')
    #     uid = request.POST.get('uid_fy')
    #     if common.phone_fy(cid, data, uid):
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
    #     if common.phone_sl(cid, uid, t_count, pos, gift):
    #         return {'msg': '成功'}
    #     else:
    #         return {'msg': '失败'}
    #
    #
    # def phone_sd(request):
    #     cid = request.POST.get('cid_sd')
    #     uid = request.POST.get('uid_sd')
    #     if common.phone_sd(cid, uid):
    #         return {'msg': '成功'}
    #     else:
    #         return {'msg': '失败'}
