#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/16 14:51
# Author : lixingyun
# Description :
from .common import REDIS_INST, Common


class Gift():
    @staticmethod
    def del_lj(uid, gift, cid):
        key = f'hm_add_new_gift_num_{uid}_{gift}_{cid}'
        REDIS_INST.delete(key)
