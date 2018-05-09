from peewee import *

database = MySQLDatabase('hm_noble', **{'host': '10.10.23.15', 'password': 'huomao', 'user': 'huomao'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class HmNobleInfo(BaseModel):
    anchor = IntegerField(db_column='anchor_id', index=True)
    end_time = IntegerField(index=True)
    level = IntegerField(index=True)
    start_time = IntegerField(index=True)
    type = IntegerField(index=True)
    uid = IntegerField(index=True)
    update_time = IntegerField()

    class Meta:
        db_table = 'hm_noble_info'

class HmNobleRecord(BaseModel):
    anchor = IntegerField(db_column='anchor_id', index=True, null=True)
    anchor_profit = DecimalField(null=True)
    end_time = IntegerField(index=True)
    level = IntegerField()
    month_num = IntegerField()
    op_time = IntegerField()
    op_username = CharField()
    open_type = IntegerField()
    pay_money = DecimalField(null=True)
    send_uid = IntegerField(null=True)
    start_time = IntegerField()
    type = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_record'

class HmNobleUser0(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_0'

class HmNobleUser1(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_1'

class HmNobleUser10(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_10'

class HmNobleUser11(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_11'

class HmNobleUser12(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_12'

class HmNobleUser13(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_13'

class HmNobleUser14(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_14'

class HmNobleUser15(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_15'

class HmNobleUser16(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_16'

class HmNobleUser17(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_17'

class HmNobleUser18(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_18'

class HmNobleUser19(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_19'

class HmNobleUser2(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_2'

class HmNobleUser20(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_20'

class HmNobleUser21(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_21'

class HmNobleUser22(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_22'

class HmNobleUser23(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_23'

class HmNobleUser24(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_24'

class HmNobleUser25(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_25'

class HmNobleUser26(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_26'

class HmNobleUser27(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_27'

class HmNobleUser28(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_28'

class HmNobleUser29(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_29'

class HmNobleUser3(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_3'

class HmNobleUser30(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_30'

class HmNobleUser31(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_31'

class HmNobleUser4(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_4'

class HmNobleUser5(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_5'

class HmNobleUser6(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_6'

class HmNobleUser7(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_7'

class HmNobleUser8(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_8'

class HmNobleUser9(BaseModel):
    add_time = IntegerField()
    anchor = IntegerField(db_column='anchor_id', null=True)
    end_time = IntegerField()
    level = IntegerField(index=True)
    returned_time = IntegerField()
    start_date = CharField(index=True)
    start_time = IntegerField()
    type = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_noble_user_9'

