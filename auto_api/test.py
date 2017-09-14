#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/9/13 19:17
# Author : lixingyun
from db import *


s = HmSignin.select()
for ss in s:
    print(ss.uid)