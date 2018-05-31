#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/5/31 19:25
# Author : lixingyun
# Description :
from huomao.bag import Bag
from huomao.money import MoneyClass

import logging
logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S %p',
                    level=logging.INFO,
                    # filename='example.log',
                    filemode='w')
logger = logging.getLogger('peewee')
logger.setLevel('DEBUG')

MoneyClass.get_money_pay('1522', '13')