#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/10/30 15:27
# Author : lixingyun
from peewee import *

database = MySQLDatabase('hm_user_bag', **{'user': 'huomao', 'password': 'huomao', 'host': '10.10.23.15'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class UserBag(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag0(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_0'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag1(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_1'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag10(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_10'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag11(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_11'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag12(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_12'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag13(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_13'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag14(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_14'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag15(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_15'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag16(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_16'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag17(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_17'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag18(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_18'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag19(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_19'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag2(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_2'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag20(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_20'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag21(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_21'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag22(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_22'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag23(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_23'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag24(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_24'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag25(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_25'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag26(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_26'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag27(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_27'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag28(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_28'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag29(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_29'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag3(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_3'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag30(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_30'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag31(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_31'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag4(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_4'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag5(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_5'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag6(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_6'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag7(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_7'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag8(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_8'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBag9(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    num = IntegerField(null=True)
    total = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'user_bag_9'
        indexes = (
            (('uid', 'expire_time', 'num', 'bag', 'type'), False),
        )

class UserBagUseRecord20171(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_1'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord201710(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    c = IntegerField(db_column='c_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_10'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord201711(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_11'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord201712(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_12'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20172(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_2'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20173(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_3'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20174(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    c = IntegerField(db_column='c_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_4'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20175(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    c = IntegerField(db_column='c_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_5'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20176(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    c = IntegerField(db_column='c_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_6'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20177(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    c = IntegerField(db_column='c_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_7'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20178(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    c = IntegerField(db_column='c_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_8'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20179(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    c = IntegerField(db_column='c_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2017_9'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20181(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_1'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord201810(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_10'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord201811(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_11'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord201812(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_12'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20182(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_2'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20183(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_3'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20184(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_4'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20185(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_5'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20186(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_6'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20187(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_7'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20188(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_8'
        indexes = (
            (('uid', 'type'), False),
        )

class UserBagUseRecord20189(BaseModel):
    add_time = IntegerField(null=True)
    bag = IntegerField(db_column='bag_id', null=True)
    expire_time = IntegerField(null=True)
    get_way = CharField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    use_time = IntegerField(null=True)
    use_way = CharField(null=True)
    user_bag = IntegerField(db_column='user_bag_id', null=True)

    class Meta:
        db_table = 'user_bag_use_record_2018_9'
        indexes = (
            (('uid', 'type'), False),
        )

