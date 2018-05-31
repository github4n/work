#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/4/20 15:52
# Author : lixingyun
# Description :
from huomao.money import MoneyClass
from huomao.user import User

users = [
    'xiawei',
    'hongtao',
    'zhangbo',
    'taotao',
    'bominming',
    'xiongyunfeng',
    'lixingyun',
    'chenweibo',
    'chenzhongtan',
    'xuhuan',
    'yerui',
    'lvwenhan',
    'weixiang',
    'tuyu',
    'lijunfeng',
    'wangxiaoqian',
    'liujiadong',
    'xiexin',
    'taohang',
    'zhangzilong',
    'caihaichuan',
    'maoxiaoyan',
    'zhangmengyi',
    'zhangxiaolong',
    'xiaojiadong',
    'hejing',
    'liuzidong',
    'douwei',
    'gongmeiling',
    'wangleilei',
    'zhangxun',
    'xuxiaodan',
    'cuihuiyan',
    'shaoshunwei',
    'tianyou',
    'liyou',
    'zhoudajian',
    'fengdingwei',
    'zhanghaoran',
    'zhonghuan',
    'wangwei',
    'guohongpeng',
    'shensuoming',
    'maxiaodi',
    'niqiao',
    'lipengpeng',
    'donghaifei',
    'pananran',
    'xieyuchen',
    'luxusheng',
    'jishaofeng',
    'fangshi',
    'liming',
    'chenlinyang',
    'wangxiaoting',
    'pengcheng',
    'liujunsheng',
    'tongjiaxin',
    'gejiayun',
    'xuyang',
    'gaokaibo',
    'qiaoxinhui',
    'chenkaihao',
    'xuechao',
    'yuxun',
    'dileilei',
    'ninghongji',
    'zhuyiheng',
    'yanpeng',
    'shangchengjun',
    'zhangqiang',
    'jianghuanzhao',
    'hexuan',
    'xiangzhiwei',
    'zhukaixiang',
    'xuran',
    'jiangmingcheng',
    'liaochunhong',
    'wangyupeng',
    'zhangpiao',
    'huozengguang',
    'xuxinyu',
    'liucan',
    'sujinlong',
    'libaiyu',
    'chenchen',
    'chenchunxiang',
    'zhouyang',
    'wangzhiwei',
    'zhangzhe',
    'wuwenying',
    'shihaosen',
    'xiefei',
    'chenlin',
    'changjunqi',
    'baoyutao',
    'zhuxiao',
    'lisiyuan',
    'machao',
    'xiawenhao',
    'gaolingyun',
    'huangrui',
    'zhaoxu',
    'yubinbin',
    'yangjichao',
    'liyu',
    'liuyilin',
    'yuhan',
]

for i in users:
    name = 'hm_' + str(i) + '1'
    try:
        uid = User.register(name)['uid']
        print(name, uid)
        User.bd_sj(uid)
        MoneyClass.set_money(uid, 150000)
    except  Exception:
        print(Exception)





# for i in range(101):
#     name = 'tuyu' + str(i)
#     try:
#         uid = Common.register(name)['uid']
#         print(uid)
#         Common.bd_sj(uid)
#         Common.set_money(uid,999999,999999)
#         Common.set_xd(uid, 99999999)
#     except  Exception:
#         print(Exception)