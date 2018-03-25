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

class Email4(BaseModel):
    email = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'email_4'

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


class Mobile0(BaseModel):
    mobile = CharField(primary_key=True)
    uid = BigIntegerField()

    class Meta:
        db_table = 'mobile_0'


class Qq0(BaseModel):
    is_set_username = IntegerField()
    openid = CharField(primary_key=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unbinding = IntegerField(null=True)

    class Meta:
        db_table = 'qq_0'

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


class Userinfo0(BaseModel):
    img = TextField(null=True)
    lv = IntegerField()
    password = CharField(index=True)
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'userinfo_0'

class Username0(BaseModel):
    uid = BigIntegerField(primary_key=True)
    username = CharField(unique=True)

    class Meta:
        db_table = 'username_0'


class Wx0(BaseModel):
    access_token = CharField(null=True)
    refresh_token = CharField(null=True)
    uid = BigIntegerField()
    unbind = IntegerField(null=True)
    unionid = CharField(primary_key=True)

    class Meta:
        db_table = 'wx_0'
