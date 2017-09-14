from peewee import *

database = MySQLDatabase('hm_user', **{'user': 'huomao', 'host': '10.10.23.15', 'password': 'huomao'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Blog0(BaseModel):
    access_token = CharField(null=True)
    blogid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'blog_0'

class Blog2(BaseModel):
    access_token = CharField(null=True)
    blogid = CharField(primary_key=True)
    ts = IntegerField()
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'blog_2'

class Email0(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_0'

class Email1(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_1'

class Email10(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_10'

class Email11(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_11'

class Email12(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_12'

class Email13(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_13'

class Email14(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_14'

class Email15(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_15'

class Email16(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_16'

class Email17(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_17'

class Email18(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_18'

class Email19(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_19'

class Email2(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_2'

class Email20(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_20'

class Email21(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_21'

class Email22(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_22'

class Email23(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_23'

class Email24(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_24'

class Email25(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_25'

class Email26(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_26'

class Email27(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_27'

class Email28(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_28'

class Email29(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_29'

class Email3(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_3'

class Email30(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_30'

class Email31(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_31'

class Email4(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_4'

class Email5(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_5'

class Email6(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_6'

class Email7(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_7'

class Email8(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_8'

class Email9(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_9'

class MemberBadge0(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_0'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge1(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_1'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge10(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_10'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge11(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_11'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge12(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_12'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge13(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_13'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge14(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_14'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge15(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_15'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge16(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_16'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge17(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_17'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge18(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_18'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge19(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_19'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge2(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_2'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge20(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_20'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge21(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_21'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge22(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_22'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge23(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_23'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge24(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_24'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge25(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_25'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge26(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_26'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge27(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_27'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge28(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_28'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge29(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_29'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge3(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_3'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge30(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_30'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge31(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_31'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge4(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_4'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge5(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_5'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge6(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_6'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge7(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_7'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge8(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_8'
        indexes = (
            (('uid', 'bid'), False),
        )

class MemberBadge9(BaseModel):
    bid = IntegerField(null=True)
    currentstat = IntegerField(null=True)
    expiretime = IntegerField(null=True)
    gettime = IntegerField(null=True)
    owntime = IntegerField(null=True)
    uid = BigIntegerField(null=True)

    class Meta:
        db_table = 'member_badge_9'
        indexes = (
            (('uid', 'bid'), False),
        )

class Mobile0(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_0'

class Mobile1(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_1'

class Mobile10(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_10'

class Mobile11(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_11'

class Mobile12(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_12'

class Mobile13(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_13'

class Mobile14(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_14'

class Mobile15(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_15'

class Mobile16(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_16'

class Mobile17(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_17'

class Mobile18(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_18'

class Mobile19(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_19'

class Mobile2(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_2'

class Mobile20(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_20'

class Mobile21(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_21'

class Mobile22(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_22'

class Mobile23(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_23'

class Mobile24(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_24'

class Mobile25(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_25'

class Mobile26(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_26'

class Mobile27(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_27'

class Mobile28(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_28'

class Mobile29(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_29'

class Mobile3(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_3'

class Mobile30(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_30'

class Mobile31(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_31'

class Mobile4(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_4'

class Mobile5(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_5'

class Mobile6(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_6'

class Mobile7(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_7'

class Mobile8(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_8'

class Mobile9(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_9'

class Qq0(BaseModel):
    is_set_username = IntegerField()
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unbinding = IntegerField(null=True)

    class Meta:
        db_table = 'qq_0'

class Qq1(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unbinding = IntegerField(null=True)

    class Meta:
        db_table = 'qq_1'

class Qq10(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_10'

class Qq11(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unbinding = IntegerField(null=True)

    class Meta:
        db_table = 'qq_11'

class Qq12(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_12'

class Qq13(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_13'

class Qq14(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unbinding = IntegerField(null=True)

    class Meta:
        db_table = 'qq_14'

class Qq15(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_15'

class Qq16(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_16'

class Qq17(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_17'

class Qq18(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_18'

class Qq19(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_19'

class Qq2(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_2'

class Qq20(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_20'

class Qq21(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_21'

class Qq22(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_22'

class Qq23(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_23'

class Qq24(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_24'

class Qq25(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_25'

class Qq26(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_26'

class Qq27(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_27'

class Qq28(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_28'

class Qq29(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_29'

class Qq3(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_3'

class Qq30(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_30'

class Qq31(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_31'

class Qq4(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_4'

class Qq5(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_5'

class Qq6(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_6'

class Qq7(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_7'

class Qq8(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_8'

class Qq9(BaseModel):
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)

    class Meta:
        db_table = 'qq_9'

class Uid(BaseModel):
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'uid'

class Userbase1(BaseModel):
    anchor_experience = IntegerField()
    blog = CharField(null=True)
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_1'
        primary_key = False

class Userbase10(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_10'
        primary_key = False

class Userbase100(BaseModel):
    anchor_experience = IntegerField()
    blog = CharField(null=True)
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_100'
        primary_key = False

class Userbase11(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_11'
        primary_key = False

class Userbase12(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_12'
        primary_key = False

class Userbase13(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_13'
        primary_key = False

class Userbase14(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_14'
        primary_key = False

class Userbase15(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_15'
        primary_key = False

class Userbase16(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_16'
        primary_key = False

class Userbase17(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_17'
        primary_key = False

class Userbase18(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_18'
        primary_key = False

class Userbase19(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_19'
        primary_key = False

class Userbase2(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_2'
        primary_key = False

class Userbase20(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_20'
        primary_key = False

class Userbase21(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_21'
        primary_key = False

class Userbase22(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_22'
        primary_key = False

class Userbase23(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_23'
        primary_key = False

class Userbase24(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_24'
        primary_key = False

class Userbase25(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_25'
        primary_key = False

class Userbase26(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_26'
        primary_key = False

class Userbase27(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_27'
        primary_key = False

class Userbase28(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_28'
        primary_key = False

class Userbase29(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_29'
        primary_key = False

class Userbase3(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_3'
        primary_key = False

class Userbase30(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_30'
        primary_key = False

class Userbase31(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_31'
        primary_key = False

class Userbase32(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_32'
        primary_key = False

class Userbase33(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_33'
        primary_key = False

class Userbase34(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_34'
        primary_key = False

class Userbase35(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_35'
        primary_key = False

class Userbase36(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_36'
        primary_key = False

class Userbase37(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_37'
        primary_key = False

class Userbase38(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_38'
        primary_key = False

class Userbase39(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_39'
        primary_key = False

class Userbase4(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_4'
        primary_key = False

class Userbase40(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_40'
        primary_key = False

class Userbase41(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_41'
        primary_key = False

class Userbase42(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_42'
        primary_key = False

class Userbase43(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_43'
        primary_key = False

class Userbase44(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_44'
        primary_key = False

class Userbase45(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_45'
        primary_key = False

class Userbase46(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_46'
        primary_key = False

class Userbase47(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_47'
        primary_key = False

class Userbase48(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_48'
        primary_key = False

class Userbase49(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_49'
        primary_key = False

class Userbase5(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_5'
        primary_key = False

class Userbase50(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_50'
        primary_key = False

class Userbase6(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_6'
        primary_key = False

class Userbase7(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_7'
        primary_key = False

class Userbase8(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_8'
        primary_key = False

class Userbase9(BaseModel):
    anchor_experience = IntegerField()
    email = CharField(index=True, null=True)
    email_activate_stat = IntegerField(null=True)
    get_experience = BigIntegerField(null=True)
    mobile = CharField(index=True, null=True)
    mobileareacode = CharField(null=True)
    name = CharField(index=True, null=True)
    openid = CharField(index=True, null=True)
    send_freebean = BigIntegerField(null=True)
    uid = IntegerField(null=True, unique=True)
    weixin = CharField(index=True, null=True)

    class Meta:
        db_table = 'userbase_9'
        primary_key = False

class Userinfo0(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_0'

class Userinfo1(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_1'

class Userinfo10(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_10'

class Userinfo11(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_11'

class Userinfo12(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_12'

class Userinfo13(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_13'

class Userinfo14(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_14'

class Userinfo15(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_15'

class Userinfo16(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_16'

class Userinfo17(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_17'

class Userinfo18(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_18'

class Userinfo19(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_19'

class Userinfo2(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_2'

class Userinfo20(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_20'

class Userinfo21(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_21'

class Userinfo22(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_22'

class Userinfo23(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_23'

class Userinfo24(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_24'

class Userinfo25(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_25'

class Userinfo26(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_26'

class Userinfo27(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_27'

class Userinfo28(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_28'

class Userinfo29(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_29'

class Userinfo3(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_3'

class Userinfo30(BaseModel):
    img = CharField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_30'

class Userinfo31(BaseModel):
    img = CharField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_31'

class Userinfo4(BaseModel):
    email = CharField(null=True)
    img = TextField(null=True)
    lv = IntegerField()
    mobile = CharField(null=True)
    name = CharField(null=True)
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_4'

class Userinfo5(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_5'

class Userinfo6(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_6'

class Userinfo7(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_7'

class Userinfo8(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_8'

class Userinfo9(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_9'

class Username0(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_0'

class Username1(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_1'

class Username10(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_10'

class Username11(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_11'

class Username12(BaseModel):
    uid = BigIntegerField()
    username = CharField(primary_key=True)

    class Meta:
        db_table = 'username_12'

class Username13(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_13'

class Username14(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_14'

class Username15(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_15'

class Username16(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_16'

class Username17(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_17'

class Username18(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(index=True)

    class Meta:
        db_table = 'username_18'

class Username19(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_19'

class Username2(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_2'

class Username20(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_20'

class Username21(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_21'

class Username22(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_22'

class Username23(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_23'

class Username24(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_24'

class Username25(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_25'

class Username26(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_26'

class Username27(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_27'

class Username28(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_28'

class Username29(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_29'

class Username3(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_3'

class Username30(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_30'

class Username31(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_31'

class Username4(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_4'

class Username5(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_5'

class Username6(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_6'

class Username7(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_7'

class Username8(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_8'

class Username9(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_9'

class Wx0(BaseModel):
    access_token = CharField(null=True)
    refresh_token = CharField(null=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unionid = CharField(primary_key=True)

    class Meta:
        db_table = 'wx_0'

class Wx1(BaseModel):
    access_token = CharField(null=True)
    refresh_token = CharField(null=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unionid = CharField(primary_key=True)

    class Meta:
        db_table = 'wx_1'

class Wx12(BaseModel):
    access_token = CharField(null=True)
    refresh_token = CharField(null=True)
    ts = IntegerField()
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unionid = CharField(primary_key=True)

    class Meta:
        db_table = 'wx_12'

class Wx14(BaseModel):
    access_token = CharField(null=True)
    refresh_token = CharField(null=True)
    ts = IntegerField()
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unionid = CharField(primary_key=True)

    class Meta:
        db_table = 'wx_14'

class Wx15(BaseModel):
    access_token = CharField(null=True)
    refresh_token = CharField(null=True)
    ts = IntegerField()
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unionid = CharField(primary_key=True)

    class Meta:
        db_table = 'wx_15'

class Wx25(BaseModel):
    access_token = CharField(null=True)
    refresh_token = CharField(null=True)
    ts = IntegerField()
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unionid = CharField(primary_key=True)

    class Meta:
        db_table = 'wx_25'

class Wx26(BaseModel):
    access_token = CharField(null=True)
    refresh_token = CharField(null=True)
    ts = IntegerField()
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unionid = CharField(primary_key=True)

    class Meta:
        db_table = 'wx_26'

class Wx27(BaseModel):
    access_token = CharField(null=True)
    refresh_token = CharField(null=True)
    ts = IntegerField()
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unionid = CharField(primary_key=True)

    class Meta:
        db_table = 'wx_27'

class Wx7(BaseModel):
    access_token = CharField(null=True)
    refresh_token = CharField(null=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unionid = CharField(primary_key=True)

    class Meta:
        db_table = 'wx_7'

