from django.shortcuts import render
from django.http import StreamingHttpResponse
from .forms import TestForm
import common


def index(request):
    dictfun = {'set_money': set_money,
               'bd_sj': bd_sj,
               'zc': zc,
               'sq_zb': sq_zb,
               'update_stream': update_stream,
               'phone_fy': phone_fy,
               'phone_sl': phone_sl,
               'phone_sd': phone_sd,
               'updatestat': updatestat,
               'update_roomlx': update_roomlx,
               }
    if request.method == 'POST':
        form = TestForm(request.POST)
        print(form.errors)
        method = request.GET.get('method')
        method = dictfun.get(method)
        if method:
            res = method(request)
        return render(request, 'index.html', {'form': form, 'res': res})
    else:
        form = TestForm()
        return render(request, 'index.html', {'form': form})


def set_money(request):
    name = request.POST.get('name_money')
    xd = request.POST.get('xd', 0)
    mb = request.POST.get('mb', 0)
    md = request.POST.get('md', 0)
    uid = common.find_uid(name)
    if uid:
        common.set_xd(uid, xd)
        common.set_money(uid, mb, md)
        return {'msg': '设置成功'}
    else:
        return {'msg': '请输入正确的UID/用户名'}


def bd_sj(request):
    name = request.POST.get('name_sj')
    uid = common.find_uid(name)
    if uid:
        common.bd_sj(uid)
        return {'msg': '绑定成功'}
    else:
        return {'msg': '请输入正确的UID/用户名'}


def zc(request):
    name = request.POST.get('name_zc')
    uid = common.zc(name)
    if uid:
        return {'msg': '成功\tuid:' + str(uid) + '\t密码1'}
    else:
        return {'msg': '注册失败'}


def sq_zb(request):
    name = request.POST.get('name_sqzb')
    uid = common.find_uid(name)
    res = common.sq_zb(uid)
    if uid and res:
        return {'msg': '申请成功'}
    else:
        return {'msg': '申请失败'}


def update_stream(request):
    room_xs = request.POST.get('room_xs')
    room_xx = request.POST.get('room_xx')
    res = common.update_stream(room_xs, room_xx)
    if res['code'] == 0:
        return {'msg': '修改成功'}
    else:
        return {'msg': res['msg']}


def phone_fy(request):
    cid = request.POST.get('cid_fy')
    data = request.POST.get('data_fy')
    uid = request.POST.get('uid_fy')
    if common.phone_fy(cid, data, uid):
        return {'msg': '成功'}
    else:
        return {'msg': '失败'}


def phone_sl(request):
    cid = request.POST.get('cid_sl')
    uid = request.POST.get('uid_sl')
    t_count = request.POST.get('t_count')
    pos = request.POST.get('pos')
    gift = request.POST.get('giftid')
    print((cid, uid, t_count, pos, gift))
    if common.phone_sl(cid, uid, t_count, pos, gift):
        return {'msg': '成功'}
    else:
        return {'msg': '失败'}


def phone_sd(request):
    cid = request.POST.get('cid_sd')
    uid = request.POST.get('uid_sd')
    if common.phone_sd(cid, uid):
        return {'msg': '成功'}
    else:
        return {'msg': '失败'}


def updatestat(request):
    cids = request.POST.get('rooms')
    stat = request.POST.get('status')
    if common.updatestat(cids, stat):
        return {'msg': '成功'}
    else:
        return {'msg': '失败'}


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


def update_roomlx(request):
    room_number = request.POST.get('room_number')
    status = request.POST.get('status1')
    res = common.update_roomlx(room_number, status)
    if res:
        return {'msg': '成功'}
    else:
        return {'msg': '失败1'}
