from peewee import *

database = MySQLDatabase('hm_money', **{'password': 'huomao', 'user': 'huomao', 'host': '10.10.23.15'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class BankCard(BaseModel):
    addtime = IntegerField()
    admin = IntegerField(db_column='admin_id')
    bank_name = CharField()
    bank_pic = CharField()
    card_holder = CharField()
    card = CharField(db_column='card_id')
    card_number = CharField(index=True)
    card_pic = CharField()
    card_type = IntegerField()
    cid = IntegerField()
    reason = CharField()
    status = IntegerField(index=True)
    uid = IntegerField()

    class Meta:
        db_table = 'bank_card'

class BankCash(BaseModel):
    addtime = IntegerField(index=True)
    bank_name = CharField()
    card_holder = CharField()
    card_number = CharField()
    cid = IntegerField(index=True)
    money = DecimalField()
    money_m = DecimalField()
    operating = CharField()
    order = CharField(db_column='order_id')
    reason = CharField()
    status = IntegerField(index=True)
    surplus = DecimalField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'bank_cash'

class ErrorCrontab(BaseModel):
    message = TextField(null=True)
    retry_count = IntegerField(null=True)
    stat = CharField(null=True)
    type = CharField()

    class Meta:
        db_table = 'error_crontab'

class HuodongState(BaseModel):
    10 = IntegerField(null=True)
    100 = IntegerField(null=True)
    1000 = IntegerField(null=True)
    10000 = IntegerField(null=True)
    blue_duration = IntegerField(null=True)
    is_blue = IntegerField(null=True)
    is_purple = IntegerField(null=True)
    is_red = IntegerField(null=True)
    is_xingui = IntegerField(null=True)
    is_zhengui = IntegerField(null=True)
    purple_duration = IntegerField(null=True)
    red_duration = IntegerField(null=True)
    uid = IntegerField(null=True)
    updatetime = DateTimeField(null=True)
    xingui_day = IntegerField(null=True)
    zhengui_day = IntegerField(null=True)

    class Meta:
        db_table = 'huodong_state'

class IncomeCount(BaseModel):
    money = DecimalField()
    money_bef = DecimalField()
    ts = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'income_count'

class Money0(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_0'

class Money1(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_1'

class Money10(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_10'

class Money11(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_11'

class Money12(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_12'

class Money13(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_13'

class Money14(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_14'

class Money15(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_15'

class Money16(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_16'

class Money17(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_17'

class Money18(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_18'

class Money19(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_19'

class Money2(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_2'

class Money20(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_20'

class Money21(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_21'

class Money22(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_22'

class Money23(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_23'

class Money24(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_24'

class Money25(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_25'

class Money26(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_26'

class Money27(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_27'

class Money28(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_28'

class Money29(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_29'

class Money3(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_3'

class Money30(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_30'

class Money31(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_31'

class Money4(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_4'

class Money5(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_5'

class Money6(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_6'

class Money7(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_7'

class Money8(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_8'

class Money9(BaseModel):
    bean = DecimalField(null=True)
    coin = DecimalField()
    ts = IntegerField()
    uid = BigIntegerField(unique=True)

    class Meta:
        db_table = 'money_9'

class MoneyAnchorSalary(BaseModel):
    gift_money = DecimalField()
    guess_money = DecimalField()
    issign = IntegerField()
    month = IntegerField()
    sale_giftmoney = DecimalField(db_column='sale_giftMoney')
    sale_guessmoney = DecimalField(db_column='sale_guessMoney')
    uid = IntegerField(index=True)
    year = UnknownField(null=True)  # year

    class Meta:
        db_table = 'money_anchor_salary'

class MoneyChannelIncome20161(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_1'

class MoneyChannelIncome201610(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_10'

class MoneyChannelIncome201611(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_11'

class MoneyChannelIncome201612(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_12'

class MoneyChannelIncome20162(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_2'

class MoneyChannelIncome20163(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_3'

class MoneyChannelIncome20164(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_4'

class MoneyChannelIncome20165(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_5'

class MoneyChannelIncome20166(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_6'

class MoneyChannelIncome20167(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_7'

class MoneyChannelIncome20168(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_8'

class MoneyChannelIncome20169(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2016_9'

class MoneyChannelIncome20171(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2017_1'

class MoneyChannelIncome20172(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2017_2'

class MoneyChannelIncome20173(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2017_3'

class MoneyChannelIncome20174(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2017_4'

class MoneyChannelIncome20175(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2017_5'

class MoneyChannelIncome20176(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2017_6'

class MoneyChannelIncome20177(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2017_7'

class MoneyChannelIncome20178(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2017_8'

class MoneyChannelIncome20179(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2017_9'

class MoneyChannelIncome2017Bak7(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField(index=True)
    cid = IntegerField(index=True)
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_channel_income_2017_bak_7'

class MoneyLemirecharge20176(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lm_acount = CharField(null=True)
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_lemirecharge_2017_6'

class MoneyLierenshoprecharge0(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_0'

class MoneyLierenshoprecharge1(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_1'

class MoneyLierenshoprecharge10(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_10'

class MoneyLierenshoprecharge11(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_11'

class MoneyLierenshoprecharge12(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_12'

class MoneyLierenshoprecharge13(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_13'

class MoneyLierenshoprecharge14(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_14'

class MoneyLierenshoprecharge15(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_15'

class MoneyLierenshoprecharge16(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_16'

class MoneyLierenshoprecharge17(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_17'

class MoneyLierenshoprecharge18(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_18'

class MoneyLierenshoprecharge19(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_19'

class MoneyLierenshoprecharge2(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2'

class MoneyLierenshoprecharge20(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_20'

class MoneyLierenshoprecharge201612(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2016_12'

class MoneyLierenshoprecharge20171(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2017_1'

class MoneyLierenshoprecharge20172(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2017_2'

class MoneyLierenshoprecharge20173(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2017_3'

class MoneyLierenshoprecharge20174(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2017_4'

class MoneyLierenshoprecharge20175(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2017_5'

class MoneyLierenshoprecharge20176(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2017_6'

class MoneyLierenshoprecharge20177(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2017_7'

class MoneyLierenshoprecharge20178(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2017_8'

class MoneyLierenshoprecharge20179(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_2017_9'

class MoneyLierenshoprecharge21(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_21'

class MoneyLierenshoprecharge22(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_22'

class MoneyLierenshoprecharge23(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_23'

class MoneyLierenshoprecharge24(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_24'

class MoneyLierenshoprecharge25(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_25'

class MoneyLierenshoprecharge26(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_26'

class MoneyLierenshoprecharge27(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_27'

class MoneyLierenshoprecharge28(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_28'

class MoneyLierenshoprecharge29(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_29'

class MoneyLierenshoprecharge3(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_3'

class MoneyLierenshoprecharge30(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_30'

class MoneyLierenshoprecharge31(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_31'

class MoneyLierenshoprecharge4(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_4'

class MoneyLierenshoprecharge5(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_5'

class MoneyLierenshoprecharge6(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_6'

class MoneyLierenshoprecharge7(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_7'

class MoneyLierenshoprecharge8(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_8'

class MoneyLierenshoprecharge9(BaseModel):
    acount = CharField(index=True)
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True, unique=True)
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)
    user = CharField(db_column='user_id')

    class Meta:
        db_table = 'money_lierenshoprecharge_9'

class MoneyPay20161(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_1'

class MoneyPay201610(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_10'

class MoneyPay201611(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_11'

class MoneyPay201612(BaseModel):
    acount = CharField()
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField()
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_12'

class MoneyPay20162(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_2'

class MoneyPay20163(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_3'

class MoneyPay20164(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_4'

class MoneyPay20165(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_5'

class MoneyPay20166(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_6'

class MoneyPay20167(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_7'

class MoneyPay20168(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_8'

class MoneyPay20169(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2016_9'

class MoneyPay20171(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2017_1'

class MoneyPay20172(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2017_2'

class MoneyPay20173(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2017_3'

class MoneyPay20174(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2017_4'

class MoneyPay20175(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2017_5'

class MoneyPay201755(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2017_55'

class MoneyPay20176(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2017_6'

class MoneyPay20177(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2017_7'

class MoneyPay20178(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2017_8'

class MoneyPay20179(BaseModel):
    acount = CharField(index=True)
    money = IntegerField()
    money_type = IntegerField()
    other_cid = IntegerField(null=True)
    other_uid = IntegerField(null=True)
    pay_num = IntegerField()
    pay_type = IntegerField()
    title = CharField()
    ts = IntegerField()
    uid = IntegerField(index=True)
    user_type = IntegerField()

    class Meta:
        db_table = 'money_pay_2017_9'

class MoneyRecharge20161(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2016_1'

class MoneyRecharge201610(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2016_10'

class MoneyRecharge201611(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2016_11'

class MoneyRecharge201612(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lierenaccount = CharField(null=True)
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2016_12'

class MoneyRecharge20162(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    status = IntegerField()
    title = CharField()
    type = IntegerField()
    uid = IntegerField()
    updatets = CharField()

    class Meta:
        db_table = 'money_recharge_2016_2'

class MoneyRecharge20163(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    status = IntegerField()
    title = CharField()
    type = IntegerField()
    uid = IntegerField()
    updatets = CharField()

    class Meta:
        db_table = 'money_recharge_2016_3'

class MoneyRecharge20164(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    status = IntegerField()
    title = CharField()
    type = IntegerField()
    uid = IntegerField()
    updatets = CharField()

    class Meta:
        db_table = 'money_recharge_2016_4'

class MoneyRecharge20165(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    status = IntegerField()
    title = CharField()
    type = IntegerField()
    uid = IntegerField()
    updatets = CharField()

    class Meta:
        db_table = 'money_recharge_2016_5'

class MoneyRecharge20166(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = IntegerField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField()
    title = CharField()
    type = IntegerField()
    uid = IntegerField()
    updatets = IntegerField()

    class Meta:
        db_table = 'money_recharge_2016_6'

class MoneyRecharge20167(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = IntegerField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField()
    title = CharField()
    type = IntegerField()
    uid = IntegerField()
    updatets = IntegerField()

    class Meta:
        db_table = 'money_recharge_2016_7'

class MoneyRecharge20168(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2016_8'

class MoneyRecharge20169(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField(null=True)
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2016_9'

class MoneyRecharge20171(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2017_1'

class MoneyRecharge20172(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2017_2'

class MoneyRecharge20173(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2017_3'

class MoneyRecharge20174(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2017_4'

class MoneyRecharge20175(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2017_5'

class MoneyRecharge20176(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lm_acount = CharField(null=True)
    lm_status = IntegerField(null=True)
    lm_uid = CharField(null=True)
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2017_6'

class MoneyRecharge20177(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lm_acount = CharField(null=True)
    lm_status = IntegerField(null=True)
    lm_uid = CharField(null=True)
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2017_7'

class MoneyRecharge201777(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lm_acount = CharField(null=True)
    lm_status = IntegerField(null=True)
    lm_uid = CharField(null=True)
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2017_77'

class MoneyRecharge20178(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lm_acount = CharField(null=True)
    lm_status = IntegerField(null=True)
    lm_uid = CharField(null=True)
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2017_8'

class MoneyRecharge20179(BaseModel):
    acount = CharField()
    clientip = CharField()
    content = CharField()
    createts = CharField()
    lm_acount = CharField(null=True)
    lm_status = IntegerField(null=True)
    lm_uid = CharField(null=True)
    mode = CharField()
    money = CharField()
    note = TextField(null=True)
    pay_mode = IntegerField()
    pay_money = CharField()
    recharge_user = CharField()
    source = CharField()
    status = IntegerField(index=True)
    title = CharField()
    type = IntegerField()
    uid = IntegerField(index=True)
    updatets = CharField(index=True)

    class Meta:
        db_table = 'money_recharge_2017_9'

class MtvChannelIncome(BaseModel):
    add_score = IntegerField()
    addtime = IntegerField()
    cid = IntegerField()
    id = IntegerField()
    ip = CharField()
    item = IntegerField()
    item_acount = IntegerField()
    money = DecimalField()
    money_type = IntegerField()
    nick = CharField()
    note = CharField()
    orderid = CharField()
    other_cid = IntegerField()
    other_uid = IntegerField()
    pay_type = IntegerField()
    uid = IntegerField()

    class Meta:
        db_table = 'mtv_channel_income'
        primary_key = False

class MtvDwMoneyBill(BaseModel):
    acount = CharField(index=True)
    addtime = CharField()
    after_beans = CharField()
    award_beans = IntegerField()
    before_beans = CharField()
    is_achieve = IntegerField()
    pay_mode = CharField()
    pay_money = CharField()
    type = IntegerField()
    uid = IntegerField()

    class Meta:
        db_table = 'mtv_dw_money_bill'

class User(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'user'

