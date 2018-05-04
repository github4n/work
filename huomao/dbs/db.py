from peewee import *

database = MySQLDatabase('hm_contents', **{'user': 'huomao', 'password': 'huomao', 'host': '10.10.23.15'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class ErrorCrontab(BaseModel):
    createtime = IntegerField(null=True)
    error_msg = CharField(null=True)
    message = TextField(null=True)
    msg = CharField(db_column='msg_id', null=True)
    retry_count = IntegerField(null=True)
    stat = CharField(null=True)
    type = CharField()
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'error_crontab'

class ErrorCrontab1(BaseModel):
    createtime = IntegerField(null=True)
    error_msg = CharField(null=True)
    message = TextField(null=True)
    msg = CharField(db_column='msg_id', null=True)
    retry_count = IntegerField(null=True)
    stat = CharField(null=True)
    type = CharField()
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'error_crontab1'

class HmActiveStar(BaseModel):
    admin_count = IntegerField()
    images = CharField()
    name = CharField()
    real_count = IntegerField()
    type = CharField()
    uid = TextField(null=True)

    class Meta:
        db_table = 'hm_active_star'

class HmAdvert(BaseModel):
    advert_code = CharField(null=True)
    area = IntegerField(index=True, null=True)
    contents = CharField(null=True)
    createtime = IntegerField(null=True)
    endtime = IntegerField(null=True)
    image_url = CharField(null=True)
    link = CharField(null=True)
    mobile_title = CharField(null=True)
    opusername = CharField(null=True)
    order = IntegerField(null=True)
    remark = CharField(null=True)
    starttime = IntegerField(null=True)
    status = IntegerField(null=True)
    title = CharField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_advert'
        indexes = (
            (('advert_code', 'status', 'starttime', 'endtime'), False),
        )

class HmAdvertRel(BaseModel):
    aid = IntegerField(null=True)
    opusername = CharField(null=True)
    rid = CharField(null=True)
    status = IntegerField(index=True, null=True)
    type = IntegerField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_advert_rel'
        indexes = (
            (('rid', 'type', 'aid'), True),
        )

class HmAdvertcategory(BaseModel):
    advert_code = CharField(null=True)
    advert_name = CharField(null=True)
    modulename = CharField(null=True)
    status = IntegerField(null=True)
    type = CharField(null=True)

    class Meta:
        db_table = 'hm_advertcategory'

class HmAnchor(BaseModel):
    admin = IntegerField(db_column='admin_id')
    area_code = CharField()
    check_time = IntegerField()
    create_time = IntegerField()
    desc_text = CharField()
    gender = IntegerField()
    gid = IntegerField()
    identity_code = CharField()
    identity_pic = CharField()
    identity_type = IntegerField()
    mobile = CharField()
    qq = CharField()
    realname = CharField()
    status = IntegerField(index=True)
    uid = IntegerField()

    class Meta:
        db_table = 'hm_anchor'
        indexes = (
            (('identity_type', 'gid'), False),
        )

class HmAnchorRecord2017(BaseModel):
    channel = CharField()
    cid = IntegerField(index=True)
    date = CharField(null=True)
    end_time = IntegerField()
    gid = IntegerField(index=True)
    pid = PrimaryKeyField()
    start_time = IntegerField()

    class Meta:
        db_table = 'hm_anchor_record_2017'
        indexes = (
            (('start_time', 'end_time'), False),
        )

class HmArea(BaseModel):
    domain = CharField()
    is_open = IntegerField()
    module = CharField(null=True)
    name = CharField()
    order = IntegerField()
    pid = IntegerField()

    class Meta:
        db_table = 'hm_area'
        indexes = (
            (('is_open', 'domain', 'order'), False),
            (('pid', 'order'), False),
        )

class HmAutorecommend(BaseModel):
    cid = IntegerField(null=True)
    end_order = IntegerField(null=True)
    endtime = IntegerField(null=True)
    gid = IntegerField(null=True)
    ischecked = IntegerField(null=True)
    opusername = CharField(null=True)
    order = IntegerField(null=True)
    recommend_ways = IntegerField(null=True)
    recommend_ways_end = IntegerField(null=True)
    recommendcode = CharField(null=True)
    recommendcode_end = CharField(null=True)
    starttime = IntegerField(null=True)
    status = IntegerField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_autorecommend'

class HmBSpecial(BaseModel):
    add_time = IntegerField(null=True)
    number = IntegerField(null=True)
    uid = IntegerField(index=True, null=True)

    class Meta:
        db_table = 'hm_b_special'

class HmBadge(BaseModel):
    bean = IntegerField(null=True)
    bid = PrimaryKeyField()
    catid = IntegerField(null=True)
    coin = DecimalField(null=True)
    img = CharField(null=True)
    name = CharField(null=True)
    optime = IntegerField(null=True)
    opusername = CharField(null=True)
    sort = IntegerField(null=True)
    userange = CharField(null=True)

    class Meta:
        db_table = 'hm_badge'

class HmBadgerelation(BaseModel):
    bid = IntegerField(null=True)
    cid = PrimaryKeyField()
    typeid = CharField(null=True)
    userange = CharField(null=True)

    class Meta:
        db_table = 'hm_badgerelation'

class HmCachemanage(BaseModel):
    action = CharField(null=True)
    cdn_cache_seperator = CharField(null=True)
    cdn_keyname = TextField(null=True)
    cdn_typename = CharField(null=True)
    cdnkey_suffixparams = TextField(null=True)
    cnname = CharField(null=True, unique=True)
    createtime = DateTimeField(null=True)
    is_show = IntegerField(null=True)
    opusername = CharField(null=True)
    order = IntegerField(null=True)
    redirecturl = TextField(null=True)
    redis_cache_seperator = CharField(null=True)
    redis_typename = CharField(null=True)
    rediskey_suffixparams = TextField(null=True)
    rediskeyname = CharField(null=True, unique=True)
    remark = CharField(null=True)
    updatetime = DateTimeField(null=True)

    class Meta:
        db_table = 'hm_cachemanage'

class HmChannel(BaseModel):
    addtime = IntegerField()
    channel = CharField()
    content = TextField(null=True)
    del_time = IntegerField(null=True)
    entertainment_time = IntegerField(null=True)
    event_endtime = IntegerField(null=True)
    event_starttime = IntegerField(null=True)
    gid = IntegerField(index=True)
    high_status = IntegerField(null=True)
    image = CharField(null=True)
    is_del = IntegerField(index=True, null=True)
    is_entertainment = CharField(null=True)
    is_event = CharField(null=True)
    is_high = IntegerField()
    is_index = IntegerField(index=True, null=True)
    is_index_live = IntegerField()
    is_index_top = IntegerField(null=True)
    is_index_type = IntegerField()
    is_live = IntegerField(index=True, null=True)
    is_push = IntegerField(null=True)
    is_replay = IntegerField()
    is_sign = IntegerField(index=True)
    is_sub = IntegerField()
    is_tuijian = IntegerField(null=True)
    is_zhuanma = CharField(null=True)
    live_last_start_time = IntegerField(null=True)
    logo = CharField(null=True)
    note = CharField()
    opusername = CharField(null=True)
    percent = CharField()
    room_number = IntegerField(index=True)
    roomadmin_num = IntegerField(null=True)
    sh_zt = IntegerField(index=True, null=True)
    status = IntegerField(index=True)
    stream = CharField(index=True)
    stream_key = CharField(null=True)
    superstar_info = TextField(null=True)
    tag = CharField(index=True)
    tel = CharField(null=True)
    tj_pic = CharField(null=True)
    tj_title = CharField(null=True)
    uid = IntegerField()
    updatetime = IntegerField(null=True)
    username = CharField(null=True)
    views = IntegerField()

    class Meta:
        db_table = 'hm_channel'

class HmChannel7X(BaseModel):
    ad_cnt = CharField(null=True)
    addtime = IntegerField()
    channel = CharField()
    content = TextField(null=True)
    del_time = IntegerField(null=True)
    eid = IntegerField(null=True)
    event_endtime = IntegerField(null=True)
    event_starttime = IntegerField(null=True)
    gid = IntegerField(index=True)
    has_ad = IntegerField()
    high_status = IntegerField()
    id = IntegerField()
    image = CharField(null=True)
    ip_show = IntegerField()
    is_del = IntegerField(index=True, null=True)
    is_entertainment = CharField(null=True)
    is_event = CharField(null=True)
    is_gf = IntegerField()
    is_high = IntegerField()
    is_index = IntegerField(index=True, null=True)
    is_index_live = IntegerField()
    is_index_top = IntegerField(null=True)
    is_index_type = IntegerField()
    is_live = IntegerField(index=True, null=True)
    is_new = IntegerField()
    is_push = IntegerField(index=True)
    is_replay = IntegerField()
    is_sign = IntegerField(index=True)
    is_sub = IntegerField()
    is_tuijian = IntegerField(null=True)
    is_zhuanma = CharField(null=True)
    live_last_start_time = IntegerField(null=True)
    logo = CharField()
    note = CharField()
    opusername = CharField()
    percent = CharField()
    push_info_time = IntegerField()
    push_live_time = IntegerField()
    push_time = IntegerField()
    room_number = IntegerField(unique=True)
    roomadmin_num = IntegerField()
    scope = CharField()
    score_count = IntegerField()
    score_total = IntegerField()
    sh_bz = CharField(null=True)
    sh_time = IntegerField(null=True)
    sh_uname = CharField(null=True)
    sh_zt = IntegerField(index=True, null=True)
    status = IntegerField(index=True)
    stream = CharField(index=True)
    stream_key = CharField()
    subscribe = IntegerField()
    superstar_info = TextField(null=True)
    tag = CharField(index=True)
    tel = CharField(null=True)
    tj_pic = CharField(null=True)
    tj_title = CharField(null=True)
    top = IntegerField(null=True)
    uid = IntegerField(unique=True)
    updatetime = IntegerField(null=True)
    username = CharField(null=True)
    videos = IntegerField()
    views = IntegerField()

    class Meta:
        db_table = 'hm_channel_7x'
        indexes = (
            (('id', 'stream'), True),
        )
        primary_key = CompositeKey('id', 'stream')

class HmChannelAmuse(BaseModel):
    header_image = CharField(null=True)
    level = IntegerField(null=True)
    name = CharField(null=True)
    opusername = CharField(null=True)
    path = CharField(null=True)
    pid = IntegerField(null=True)
    status = CharField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_channel_amuse'

class HmChannelArea(BaseModel):
    cid = IntegerField(unique=True)
    city = CharField(null=True)
    city_id = IntegerField(null=True)
    province = CharField(null=True)
    province_id = IntegerField(null=True)

    class Meta:
        db_table = 'hm_channel_area'

class HmChannelAttach1(BaseModel):
    cid = PrimaryKeyField()
    clarity_openstat = IntegerField(null=True)
    cover_image = CharField(null=True)
    entertainment_time = IntegerField(null=True)
    flash_chartleft = TextField(null=True)
    flash_chartright = CharField(null=True)
    is_duanbo = IntegerField(null=True)
    is_join = CharField(null=True)
    list_a_n_color = CharField(null=True)
    match_index_info = TextField(null=True)
    no_cash = CharField(null=True)
    notice = CharField(null=True)
    player_bg_img = CharField(null=True)
    player_bg_img_url = CharField(null=True)
    search_words = CharField(null=True)
    unionid = IntegerField(null=True)
    yl_pc_index_info = TextField(null=True)
    yl_tj_msg = CharField(null=True)
    yl_tj_pic = CharField(null=True)

    class Meta:
        db_table = 'hm_channel_attach1'

class HmChannelExtrainfo(BaseModel):
    ad_cnt = CharField(null=True)
    cid = PrimaryKeyField()
    eid = IntegerField(null=True)
    has_ad = IntegerField(null=True)
    ip_show = IntegerField(null=True)
    is_gf = IntegerField(null=True)
    is_high = IntegerField(null=True)
    is_new = IntegerField(null=True)
    is_sign = IntegerField(null=True)
    is_sub = IntegerField(null=True)
    logo = CharField(null=True)
    percent = CharField(null=True)
    push_info_time = IntegerField(null=True)
    push_live_time = IntegerField()
    push_time = IntegerField(null=True)
    scope = CharField(null=True)
    score_count = IntegerField(null=True)
    score_total = IntegerField(null=True)
    sh_bz = CharField(null=True)
    sh_time = IntegerField(null=True)
    sh_uname = CharField(null=True)
    videos = IntegerField(null=True)

    class Meta:
        db_table = 'hm_channel_extrainfo'

class HmChannelFlv(BaseModel):
    addtime = IntegerField(null=True)
    bucket = IntegerField(null=True)
    cid = IntegerField(null=True)
    key = CharField(null=True)
    ops = IntegerField(null=True)
    persistentid = CharField(db_column='persistentId', null=True)
    streamname = CharField(null=True)
    url = CharField(null=True)

    class Meta:
        db_table = 'hm_channel_flv'

class HmChannelGameorder(BaseModel):
    cid = IntegerField(null=True)
    gid = IntegerField(null=True)
    order = IntegerField(null=True)

    class Meta:
        db_table = 'hm_channel_gameorder'

class HmChannelJoinRobot(BaseModel):
    cid = IntegerField(null=True, unique=True)
    random = CharField(null=True)
    status = IntegerField(null=True)

    class Meta:
        db_table = 'hm_channel_join_robot'

class HmChannelLabel(BaseModel):
    createtime = IntegerField(null=True)
    desc = TextField(null=True)
    image = CharField(null=True)
    index_label_order = IntegerField(null=True)
    index_label_stat = IntegerField(null=True)
    index_label_tjmsg = CharField(null=True)
    index_label_tjpic = CharField(null=True)
    key = CharField(null=True)
    labelname = CharField(null=True)
    labeltype = IntegerField(null=True)
    labeltypecat = CharField(null=True)
    list_stat = IntegerField()
    listcolor = CharField()
    listhovercolor = CharField()
    listweight = IntegerField()
    mobile_img = CharField(null=True)
    opusername = CharField(null=True)
    show_img = CharField(null=True)
    sort = IntegerField(null=True)
    status = IntegerField(null=True)
    title = CharField(null=True)
    updatetime = IntegerField(null=True)
    url_rule = CharField(null=True)

    class Meta:
        db_table = 'hm_channel_label'

class HmChannelLabel1(BaseModel):
    createtime = IntegerField(null=True)
    desc = TextField(null=True)
    image = CharField(null=True)
    key = CharField(null=True)
    labelname = CharField(null=True)
    labeltype = IntegerField(null=True)
    labeltypecat = CharField(null=True)
    list_stat = IntegerField()
    listcolor = CharField()
    listhovercolor = CharField()
    listweight = IntegerField()
    mobile_img = CharField(null=True)
    opusername = CharField(null=True)
    sort = IntegerField(null=True)
    status = IntegerField(null=True)
    title = CharField(null=True)
    updatetime = IntegerField(null=True)
    url_rule = CharField(null=True)

    class Meta:
        db_table = 'hm_channel_label1'

class HmChannelLabelorder(BaseModel):
    cid = IntegerField(null=True)
    labelid = IntegerField(null=True)
    order = IntegerField(null=True)

    class Meta:
        db_table = 'hm_channel_labelorder'

class HmChannelLock(BaseModel):
    cid = IntegerField(null=True)
    lock_date = IntegerField(null=True)
    lock_msg = CharField(null=True)
    lock_time = IntegerField(null=True)
    opusername = CharField(null=True)
    status_msg = CharField(null=True)
    unlock_time = IntegerField(null=True)

    class Meta:
        db_table = 'hm_channel_lock'

class HmChannelLucky(BaseModel):
    ad_cnt = CharField(null=True)
    addtime = IntegerField()
    channel = CharField()
    content = TextField(null=True)
    del_time = IntegerField(null=True)
    eid = IntegerField(null=True)
    event_endtime = IntegerField(null=True)
    event_starttime = IntegerField(null=True)
    gid = IntegerField(index=True)
    has_ad = IntegerField()
    high_status = IntegerField()
    image = CharField(null=True)
    ip_show = IntegerField()
    is_del = IntegerField(index=True, null=True)
    is_event = CharField(null=True)
    is_gf = IntegerField()
    is_high = IntegerField()
    is_index = IntegerField(index=True, null=True)
    is_index_live = IntegerField()
    is_index_top = IntegerField(null=True)
    is_index_type = IntegerField()
    is_live = IntegerField(index=True, null=True)
    is_new = IntegerField()
    is_push = IntegerField(index=True)
    is_sign = IntegerField(index=True)
    is_sub = IntegerField()
    is_tuijian = IntegerField(null=True)
    is_zhuanma = CharField(null=True)
    live_last_start_time = IntegerField(null=True)
    logo = CharField()
    note = CharField()
    percent = CharField()
    push_info_time = IntegerField()
    push_live_time = IntegerField()
    push_time = IntegerField()
    room_number = IntegerField(index=True)
    scope = CharField()
    score_count = IntegerField()
    score_total = IntegerField()
    sh_bz = CharField(null=True)
    sh_time = IntegerField(null=True)
    sh_uname = CharField(null=True)
    sh_zt = IntegerField(index=True, null=True)
    status = IntegerField(index=True)
    stream = CharField(index=True)
    stream_key = CharField()
    subscribe = IntegerField()
    superstar_info = TextField(null=True)
    tag = CharField(index=True)
    tel = CharField(null=True)
    tj_pic = CharField(null=True)
    tj_title = CharField(null=True)
    top = IntegerField(null=True)
    uid = IntegerField()
    updatetime = IntegerField(null=True)
    username = CharField(null=True)
    videos = IntegerField()
    views = IntegerField()

    class Meta:
        db_table = 'hm_channel_lucky'

class HmChannelReplay(BaseModel):
    addtime = IntegerField()
    channel = CharField(null=True)
    cid = IntegerField()
    cname = CharField(null=True)
    flv = CharField(db_column='flv_id', null=True)
    opusername = CharField(null=True)
    played_flv = IntegerField(db_column='played_flv_id', null=True)
    room_number = IntegerField(null=True)
    stream_select = IntegerField()
    updatetime = IntegerField(null=True)
    username = CharField(null=True)

    class Meta:
        db_table = 'hm_channel_replay'

class HmChannelShop(BaseModel):
    admincontrol = IntegerField(db_column='adminControl', null=True)
    cid = IntegerField()
    createtime = IntegerField()
    is_ground = IntegerField()
    is_hot = IntegerField()
    item_url = CharField()
    num_iid = CharField()
    pict_url = CharField()
    price = CharField()
    room_number = CharField(null=True)
    title = CharField()

    class Meta:
        db_table = 'hm_channel_shop'

class HmChannelTag(BaseModel):
    popular_rule = TextField()
    relationcode = CharField()
    status = IntegerField()
    tag_cn = CharField()
    tag_en = CharField()
    tagid = PrimaryKeyField()

    class Meta:
        db_table = 'hm_channel_tag'

class HmChannelTest(BaseModel):
    ad_cnt = CharField(null=True)
    addtime = IntegerField()
    channel = CharField()
    content = TextField(null=True)
    del_time = IntegerField(null=True)
    eid = IntegerField(null=True)
    event_endtime = IntegerField(null=True)
    event_starttime = IntegerField(null=True)
    gid = IntegerField()
    has_ad = IntegerField()
    high_status = IntegerField()
    id = IntegerField()
    image = CharField(null=True)
    ip_show = IntegerField()
    is_del = IntegerField(null=True)
    is_event = CharField(null=True)
    is_gf = IntegerField()
    is_high = IntegerField()
    is_index = IntegerField(null=True)
    is_index_live = IntegerField()
    is_index_top = IntegerField(null=True)
    is_index_type = IntegerField()
    is_live = IntegerField(null=True)
    is_new = IntegerField()
    is_push = IntegerField()
    is_sign = IntegerField()
    is_sub = IntegerField()
    is_tuijian = IntegerField(null=True)
    is_zhuanma = CharField(null=True)
    live_last_start_time = IntegerField(null=True)
    logo = CharField()
    note = CharField()
    percent = CharField()
    push_info_time = IntegerField()
    push_live_time = IntegerField()
    push_time = IntegerField()
    room_number = IntegerField()
    scope = CharField()
    score_count = IntegerField()
    score_total = IntegerField()
    sh_bz = CharField(null=True)
    sh_time = IntegerField(null=True)
    sh_uname = CharField(null=True)
    sh_zt = IntegerField(null=True)
    status = IntegerField()
    stream = CharField()
    stream_key = CharField()
    subscribe = IntegerField()
    superstar_info = TextField(null=True)
    tag = CharField()
    tel = CharField(null=True)
    tj_pic = CharField(null=True)
    tj_title = CharField(null=True)
    top = IntegerField(null=True)
    uid = IntegerField()
    updatetime = IntegerField(null=True)
    username = CharField(null=True)
    videos = IntegerField()
    views = IntegerField()

    class Meta:
        db_table = 'hm_channel_test'
        primary_key = False

class HmChannelVideodemand(BaseModel):
    addtime = IntegerField()
    cid = IntegerField(null=True)
    close_endtime = IntegerField(null=True)
    close_starttime = IntegerField(null=True)
    close_weight = IntegerField(null=True)
    cover = CharField(null=True)
    is_guanbo = IntegerField(null=True)
    is_zhibo = IntegerField(null=True)
    live_endtime = IntegerField(null=True)
    live_starttime = IntegerField(null=True)
    live_weight = IntegerField(null=True)
    opusername = CharField(null=True)
    room_number = IntegerField(null=True)
    title = CharField(null=True)
    updatetime = IntegerField(null=True)
    url = CharField(null=True)

    class Meta:
        db_table = 'hm_channel_videodemand'

class HmChannelstat(BaseModel):
    cid = IntegerField(null=True)
    opusername = CharField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_channelstat'

class HmChanneltheme(BaseModel):
    channelids = TextField(null=True)
    createtime = IntegerField(null=True)
    description = CharField(null=True)
    opusername = CharField(null=True)
    order = IntegerField(null=True)
    recommendpos = CharField(db_column='recommendPos', null=True)
    status = IntegerField(null=True)
    themename = CharField(null=True)

    class Meta:
        db_table = 'hm_channeltheme'

class HmChannelviews(BaseModel):
    addtime = IntegerField(null=True)
    cid = IntegerField(null=True)
    default_rule = CharField(null=True)
    directshownumber = IntegerField(null=True)
    directshownumber_select = IntegerField(null=True)
    is_popular_lim_select = IntegerField(null=True)
    opusername = CharField(null=True)
    period_stat = CharField(null=True)
    popular_lim_num = IntegerField(null=True)
    popular_limcat = CharField(null=True)
    popular_tagid = IntegerField(null=True)
    rule_no_cache = TextField(null=True)
    rule_with_cache = TextField(null=True)
    rule_with_superstar = TextField(null=True)
    status = IntegerField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_channelviews'

class HmEventCommentator(BaseModel):
    cid = IntegerField(index=True, null=True)
    create_time = IntegerField(null=True)
    ecid = PrimaryKeyField()
    is_del = IntegerField(null=True)
    remark = CharField(null=True)
    sort = IntegerField(null=True)
    tj_msg = CharField(null=True)
    tj_pic = TextField(null=True)
    update_time = IntegerField(null=True)

    class Meta:
        db_table = 'hm_event_commentator'

class HmEventInfo(BaseModel):
    addtime = IntegerField()
    assign_time = IntegerField()
    channel = IntegerField(db_column='channel_id')
    end_time = IntegerField()
    event = IntegerField(db_column='event_id', index=True)
    game = IntegerField(db_column='game_id', null=True)
    home_rate = DecimalField()
    home_result = IntegerField(null=True)
    home_team = CharField()
    home_team_id = IntegerField()
    is_assign = IntegerField()
    is_del = IntegerField()
    is_open = IntegerField()
    is_settle = IntegerField()
    is_top = IntegerField(null=True)
    istop = IntegerField(null=True)
    last_operator = CharField(null=True)
    match_date = IntegerField()
    match_time = IntegerField()
    note = CharField()
    open_time = IntegerField()
    score = CharField(null=True)
    settle_time = IntegerField()
    uid = IntegerField()
    updatetime = IntegerField()
    url = CharField()
    victory_team = CharField()
    visiting_rate = DecimalField()
    visiting_result = IntegerField(null=True)
    visiting_team = CharField()
    visiting_team_id = IntegerField()
    yugao = IntegerField(db_column='yugao_id', index=True)

    class Meta:
        db_table = 'hm_event_info'
        indexes = (
            (('match_date', 'is_del'), False),
        )

class HmEventList(BaseModel):
    addtime = IntegerField()
    default_cid = IntegerField()
    end_time = IntegerField(index=True)
    event_img = CharField()
    event_jd = CharField(null=True)
    gid = IntegerField()
    images_2 = CharField()
    is_del = IntegerField(index=True)
    is_top = IntegerField()
    last_operator = CharField(null=True)
    match_bonus = CharField(null=True)
    match_day = IntegerField(null=True)
    match_logo = CharField(null=True)
    match_mode = CharField(null=True)
    match_place = CharField(null=True)
    match_rating = IntegerField(null=True)
    name = CharField()
    note = CharField()
    short_name = CharField()
    sort = IntegerField()
    sponsor = CharField(null=True)
    start_time = IntegerField(index=True)
    status = IntegerField(null=True)
    template_name = CharField()
    updatetime = IntegerField()
    url_rule = CharField()

    class Meta:
        db_table = 'hm_event_list'

class HmEventRaceImg(BaseModel):
    eid = IntegerField(null=True)
    image_url = CharField(null=True)
    is_top = IntegerField(null=True)
    opusername = CharField(null=True)
    title = CharField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_event_race_img'

class HmEventTeam(BaseModel):
    admin = IntegerField(db_column='admin_id', null=True)
    createtime = IntegerField(null=True)
    description = CharField(null=True)
    gid = IntegerField(null=True)
    is_top = IntegerField(null=True)
    last_operator = CharField(null=True)
    logo = CharField(null=True)
    other_members = CharField(null=True)
    team_members = CharField(null=True)
    team_zone = CharField(null=True)
    teamname = CharField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_event_team'

class HmEventbrand(BaseModel):
    brand_desc = CharField(null=True)
    brand_name = CharField(null=True)
    brand_pic = CharField(null=True)
    createtime = IntegerField(null=True)
    ebid = PrimaryKeyField()
    event_place = TextField(null=True)
    event_series = TextField(null=True)
    event_type = TextField(null=True)
    is_del = IntegerField(null=True)
    is_top = IntegerField(null=True)
    opusername = CharField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_eventbrand'

class HmFaqfeedback(BaseModel):
    addtime = IntegerField(null=True)
    area_name = CharField(null=True)
    bz = TextField(null=True)
    city_name = CharField(null=True)
    class_name = CharField(null=True)
    client = CharField(null=True)
    client_name = CharField(null=True)
    contactway = CharField(null=True)
    content = TextField(null=True)
    ext = TextField(null=True)
    has_do = IntegerField(null=True)
    ip = CharField(null=True)
    operators = CharField(null=True)
    pic_url = CharField()
    province_name = CharField(null=True)
    re_name = CharField(null=True)
    re_time = IntegerField()
    report_name = CharField()
    room_cid = CharField()
    room_name = CharField()
    sign = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField()

    class Meta:
        db_table = 'hm_faqfeedback'

class HmGag(BaseModel):
    addtime = IntegerField()
    ban_uid = IntegerField()
    channel = CharField(null=True)
    cid = IntegerField()
    is_root = IntegerField()
    mname = CharField()
    node = CharField(null=True)
    status = IntegerField(null=True)
    type = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_gag'

class HmGame(BaseModel):
    addtime = IntegerField()
    cdn = CharField()
    cname = CharField()
    desc = TextField(null=True)
    ename = CharField()
    event_logo = CharField()
    gid = PrimaryKeyField()
    images = CharField()
    images_2 = CharField()
    includelabels = TextField(null=True)
    index_display = IntegerField()
    is_display = IntegerField()
    is_show = IntegerField()
    is_show_tab = IntegerField(null=True)
    key = CharField(null=True)
    lives = IntegerField()
    lm_status = IntegerField(null=True)
    logo = CharField()
    opusername = CharField(null=True)
    push_time = IntegerField()
    sort = IntegerField()
    title = CharField(null=True)
    updatetime = IntegerField(null=True)
    url_rule = CharField()
    videos = IntegerField()
    views = IntegerField()

    class Meta:
        db_table = 'hm_game'

class HmGameChannelLabel(BaseModel):
    cid = IntegerField(null=True)
    gid = IntegerField(null=True)
    labelid = CharField(null=True)
    opusername = CharField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_game_channel_label'
        indexes = (
            (('gid', 'labelid', 'cid'), True),
        )

class HmGamecollection(BaseModel):
    cname = CharField(null=True)
    createtime = IntegerField(null=True)
    desc = TextField(null=True)
    ename = CharField(null=True)
    image = CharField(null=True)
    includegids = CharField(null=True)
    is_show_tab = IntegerField(null=True)
    key = CharField(null=True)
    opusername = CharField(null=True)
    sort = IntegerField(null=True)
    status = IntegerField(null=True)
    title = CharField(null=True)
    updatetime = IntegerField(null=True)
    url_rule = CharField(null=True)

    class Meta:
        db_table = 'hm_gamecollection'

class HmGiftMoney(BaseModel):
    addtime = CharField()
    cid = IntegerField()
    date = CharField()
    money = IntegerField()
    month = IntegerField()
    type = IntegerField()
    uid = IntegerField()
    week = IntegerField()
    year = IntegerField()

    class Meta:
        db_table = 'hm_gift_money'

class HmHelp(BaseModel):
    begin = IntegerField(null=True)
    content = TextField(null=True)
    is_hot = IntegerField()
    link = CharField(null=True)
    status = IntegerField(null=True)
    title = CharField(null=True)
    type = IntegerField(null=True)
    type_name = IntegerField()
    uname = CharField(null=True)
    updatetime = IntegerField(null=True)
    weight = IntegerField(null=True)

    class Meta:
        db_table = 'hm_help'

class HmHelpType(BaseModel):
    name = CharField()
    type = IntegerField()

    class Meta:
        db_table = 'hm_help_type'

class HmInvition(BaseModel):
    createtime = IntegerField(null=True)
    invite_code = CharField(null=True)
    is_achive_new = IntegerField(null=True)
    is_achive_old = IntegerField(null=True)
    new_uid = CharField(null=True)
    phone_number = IntegerField(null=True)
    uid = CharField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_invition'

class HmLoveliness(BaseModel):
    cid = IntegerField(index=True)
    is_sel = IntegerField()
    other_uid = IntegerField(index=True)
    score = IntegerField()
    settime = IntegerField()
    type = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_loveliness'
        indexes = (
            (('uid', 'score'), False),
        )

class HmLovelinessBak(BaseModel):
    cid = IntegerField()
    id = IntegerField()
    is_sel = IntegerField()
    other_uid = IntegerField()
    score = IntegerField()
    settime = IntegerField()
    type = IntegerField()
    uid = IntegerField()

    class Meta:
        db_table = 'hm_loveliness_bak'
        primary_key = False

class HmNewcategory(BaseModel):
    category_name = CharField()
    is_show = IntegerField(null=True)
    order = IntegerField(null=True)
    status = IntegerField(null=True)

    class Meta:
        db_table = 'hm_newcategory'

class HmNewscontent(BaseModel):
    content = TextField(null=True)
    createtime = IntegerField(index=True, null=True)
    desc = CharField(null=True)
    is_hot = IntegerField()
    is_top = IntegerField(null=True)
    key = CharField(null=True)
    link = CharField(null=True)
    pic = CharField(null=True)
    rel_content = TextField(null=True)
    rel_game = CharField(null=True)
    rel_match = CharField(null=True)
    showtype = CharField(index=True, null=True)
    status = IntegerField(index=True, null=True)
    title = CharField(null=True)
    top_weight = IntegerField(null=True)
    type = IntegerField(index=True, null=True)
    uid = IntegerField(null=True)
    uname = CharField(null=True)
    weight = IntegerField(null=True)

    class Meta:
        db_table = 'hm_newscontent'

class HmNewscontent1(BaseModel):
    content = TextField(null=True)
    createtime = IntegerField(null=True)
    desc = TextField(null=True)
    is_hot = IntegerField()
    is_top = IntegerField(null=True)
    key = CharField(null=True)
    link = CharField(null=True)
    pic = CharField(null=True)
    rel_content = TextField(null=True)
    showtype = CharField(null=True)
    status = IntegerField(null=True)
    title = CharField(null=True)
    top_weight = IntegerField(null=True)
    type = IntegerField(null=True)
    uid = IntegerField(null=True)
    uname = CharField(null=True)
    weight = IntegerField(null=True)

    class Meta:
        db_table = 'hm_newscontent1'

class HmPopularityClass(BaseModel):
    cname = CharField()
    ename = CharField()
    rand = IntegerField()
    relation_code = CharField()
    ts = IntegerField()

    class Meta:
        db_table = 'hm_popularity_class'

class HmPopularityRule(BaseModel):
    id = IntegerField()
    ts = IntegerField()
    x = DecimalField(primary_key=True)
    y = DecimalField()

    class Meta:
        db_table = 'hm_popularity_rule'

class HmReccatcontpos(BaseModel):
    createtime = IntegerField(null=True)
    opusername = CharField(null=True)
    rctcid = IntegerField(null=True)
    recommendcode = CharField(null=True)
    recommendname = CharField(null=True)
    rid = PrimaryKeyField()
    sort = IntegerField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_reccatcontpos'

class HmReccattype(BaseModel):
    cname = CharField(null=True)
    createtime = IntegerField(null=True)
    ename = CharField(null=True)
    opusername = CharField(null=True)
    rctid = PrimaryKeyField()
    sort = IntegerField(null=True)
    status = IntegerField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_reccattype'

class HmReccattypecont(BaseModel):
    cname = CharField(null=True)
    createtime = IntegerField(null=True)
    image = CharField(null=True)
    opusername = CharField(null=True)
    rctcid = PrimaryKeyField()
    sort = IntegerField(null=True)
    status = IntegerField(null=True)
    targettype = IntegerField(null=True)
    typeid = IntegerField(null=True)
    typename = CharField(null=True)
    updatetime = IntegerField(null=True)
    url = TextField(null=True)

    class Meta:
        db_table = 'hm_reccattypecont'

class HmRecommendcategory(BaseModel):
    recommendclass = CharField(null=True)
    recommendcode = CharField(null=True, unique=True)
    recommendname = CharField(null=True)
    remark = CharField(null=True)
    status = IntegerField(null=True)

    class Meta:
        db_table = 'hm_recommendcategory'

class HmRecommendchannel(BaseModel):
    createtime = IntegerField(null=True)
    eid = IntegerField(null=True)
    ext = CharField(null=True)
    gid = IntegerField(null=True)
    img = CharField(null=True)
    opusername = CharField(null=True)
    order = IntegerField(null=True)
    recommendcode = CharField(index=True, null=True)
    remark = CharField(null=True)
    rid = IntegerField(null=True)
    uid = IntegerField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_recommendchannel'

class HmRecommendevent(BaseModel):
    addtime = IntegerField(null=True)
    ext = CharField(null=True)
    images = CharField(null=True)
    linkurl = CharField(null=True)
    opusername = CharField(null=True)
    order = IntegerField(null=True)
    recommendcode = CharField(null=True)
    remark = CharField(null=True)
    rid = IntegerField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_recommendevent'

class HmReport(BaseModel):
    action = IntegerField()
    addtime = CharField()
    channel = CharField(db_column='channel_id')
    content = CharField()
    gift = IntegerField()
    is_del = IntegerField()
    note = CharField()
    opusername = CharField(null=True)
    report_uid = CharField()
    uid = CharField()
    updatetime = CharField()

    class Meta:
        db_table = 'hm_report'

class HmRoomNumber(BaseModel):
    is_special = IntegerField()
    room_number = IntegerField(unique=True)
    status = IntegerField()
    update_time = IntegerField()

    class Meta:
        db_table = 'hm_room_number'
        indexes = (
            (('is_special', 'status'), False),
        )

class HmShareActive(BaseModel):
    active_type = CharField()
    aid = IntegerField()
    opusername = CharField(null=True)
    share_content = TextField(null=True)
    share_image = CharField(null=True)
    share_title = CharField(null=True)
    type = IntegerField()

    class Meta:
        db_table = 'hm_share_active'

class HmShieldList(BaseModel):
    addtime = CharField()
    ban_acount = TextField()
    note = CharField()
    sid = PrimaryKeyField()
    uid = IntegerField(index=True)
    updatetime = CharField()

    class Meta:
        db_table = 'hm_shield_list'

class HmSignin201605(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_05'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin201606(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_06'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')



class HmSignin(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')



class HmSignin201607(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_07'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin201608(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_08'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin201609(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_09'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin201610(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_10'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin201611(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_11'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin201612(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_12'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20165(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_5'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20166(BaseModel):
    adddate = IntegerField(null=True)
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_6'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20167(BaseModel):
    adddate = IntegerField(null=True)
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_7'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20168(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_8'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20169(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2016_9'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20171(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_1'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin201710(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_10'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin201711(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_11'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin201712(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_12'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20172(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_2'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20173(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_3'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20174(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_4'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20175(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_5'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20176(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_6'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20177(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_7'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20178(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_8'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmSignin20179(BaseModel):
    conn_day = IntegerField()
    day_15 = IntegerField()
    day_3 = IntegerField()
    day_30 = IntegerField()
    day_7 = IntegerField()
    end_time = IntegerField()
    get_time = IntegerField()
    id = IntegerField()
    max_day = IntegerField()
    month = IntegerField(index=True)
    punch = TextField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_signin_2017_9'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmStreamDoLog(BaseModel):
    on_off = IntegerField()
    stream_name = CharField()
    time = IntegerField()
    why = CharField(null=True)

    class Meta:
        db_table = 'hm_stream_do_log'

class HmStreamKillList(BaseModel):
    on_off = IntegerField()
    stream_name = CharField()
    time = IntegerField()
    why = CharField()

    class Meta:
        db_table = 'hm_stream_kill_list'

class HmSubscribe(BaseModel):
    channel = IntegerField(db_column='channel_id', index=True)
    is_send = IntegerField(index=True)
    time = IntegerField()
    user = IntegerField(db_column='user_id', index=True)

    class Meta:
        db_table = 'hm_subscribe'
        indexes = (
            (('channel', 'user'), False),
        )

class HmSubscribeAdmin(BaseModel):
    cid = IntegerField()
    hand_operating = IntegerField()
    lasttime = IntegerField(null=True)
    opusername = CharField(null=True)
    rule_settings = CharField(null=True)
    type = IntegerField(null=True)

    class Meta:
        db_table = 'hm_subscribe_admin'

class HmSysConfig(BaseModel):
    description = CharField()
    value = TextField(null=True)
    variable = CharField(primary_key=True)

    class Meta:
        db_table = 'hm_sys_config'

class HmSysMessage(BaseModel):
    addtime = IntegerField(null=True)
    content = TextField()
    count = CharField(null=True)
    opusername = CharField(null=True)
    send_scope = TextField(null=True)
    sendtime = IntegerField(null=True)
    sys_stage = IntegerField(null=True)
    title = CharField()
    type = IntegerField(null=True)

    class Meta:
        db_table = 'hm_sys_message'

class HmTaskMin(BaseModel):
    final_rec_time = IntegerField()
    first_enter_time = IntegerField()
    record = TextField(null=True)
    task_time = IntegerField()
    task_type = IntegerField()
    time = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_task_min'

class HmTiebaNews(BaseModel):
    eid = IntegerField(null=True)
    image_url = CharField(null=True)
    is_top = IntegerField(null=True)
    news_link = CharField(null=True)
    news_time = IntegerField(null=True)
    news_title = CharField(null=True)
    opusername = CharField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_tieba_news'

class HmUsertask201610(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2016_10'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask201611(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2016_11'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask201612(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2016_12'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20166(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2016_6'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20167(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2016_7'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20168(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2016_8'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20169(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2016_9'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20171(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2017_1'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20172(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2017_2'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20173(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2017_3'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20174(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2017_4'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20175(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2017_5'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20176(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2017_6'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20177(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2017_7'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20178(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2017_8'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmUsertask20179(BaseModel):
    adddate = IntegerField()
    get_moneytime = IntegerField()
    id = IntegerField()
    money = IntegerField()
    task = IntegerField(db_column='task_id', index=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'hm_usertask_2017_9'
        indexes = (
            (('id', 'uid'), True),
        )
        primary_key = CompositeKey('id', 'uid')

class HmVideodemand(BaseModel):
    createtime = IntegerField(null=True)
    did = PrimaryKeyField()
    duration = IntegerField(null=True)
    gid = IntegerField(null=True)
    gname = CharField(null=True)
    link = CharField(null=True)
    opusername = CharField(null=True)
    pic = CharField(null=True)
    sort = IntegerField(null=True)
    subtitle = CharField(null=True)
    title = CharField(null=True)
    updatetime = IntegerField(null=True)

    class Meta:
        db_table = 'hm_videodemand'

class HmWebConfig(BaseModel):
    cfg_type = CharField(index=True)
    code = CharField()
    default = IntegerField()
    foreign_low = IntegerField()
    is_heigh = IntegerField()
    sort = IntegerField()
    status = IntegerField()
    val = CharField()

    class Meta:
        db_table = 'hm_web_config'

class HmWeekstargiftList(BaseModel):
    all_week_gift = CharField(db_column='all_week_gift_id')
    createtime = IntegerField()
    is_auto = IntegerField()
    opusername = CharField()
    price_range = CharField(null=True)
    updatetime = IntegerField(null=True)
    week = IntegerField()
    year = IntegerField()

    class Meta:
        db_table = 'hm_weekstargift_list'
        indexes = (
            (('week', 'year'), False),
        )

class HmWeekstargiftRecord(BaseModel):
    amount = IntegerField(null=True)
    anchor_uid = IntegerField()
    createtime = IntegerField()
    gift = IntegerField(db_column='gift_id')
    send_uid = IntegerField()
    week = IntegerField(null=True)
    year = IntegerField(null=True)

    class Meta:
        db_table = 'hm_weekstargift_record'
        indexes = (
            (('week', 'year', 'gift'), False),
        )

class IncomeCount(BaseModel):
    money = DecimalField()
    ts = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'income_count'

class LiveRecord11111(BaseModel):
    addtime = IntegerField()
    end_time = IntegerField()
    len = IntegerField(null=True)
    start_time = IntegerField()
    stream = CharField()
    stream_id = IntegerField(unique=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'live_record11111'
        indexes = (
            (('start_time', 'end_time'), False),
        )

class LiveRecord2016(BaseModel):
    addtime = IntegerField()
    end_time = IntegerField()
    len = IntegerField(null=True)
    start_time = IntegerField()
    stream = CharField()
    stream_id = IntegerField(unique=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'live_record_2016'
        indexes = (
            (('start_time', 'end_time'), False),
        )

class LiveRecord2017(BaseModel):
    addtime = IntegerField()
    end_time = IntegerField()
    len = IntegerField(null=True)
    start_time = IntegerField()
    stream = CharField()
    stream_id = IntegerField(unique=True)
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'live_record_2017'
        indexes = (
            (('start_time', 'end_time'), False),
        )

class StreamState(BaseModel):
    note = CharField()
    start_date = IntegerField(index=True)
    stream_end_time = IntegerField(index=True)
    stream_flashver = CharField()
    stream = PrimaryKeyField(db_column='stream_id')
    stream_name = CharField(index=True)
    stream_ser_ip = CharField()
    stream_start_time = IntegerField(index=True)
    stream_state = CharField(index=True)

    class Meta:
        db_table = 'stream_state'

class StreamState2016(BaseModel):
    note = CharField()
    start_date = IntegerField(index=True)
    stream_end_time = IntegerField(index=True)
    stream_flashver = CharField()
    stream = PrimaryKeyField(db_column='stream_id')
    stream_name = CharField(index=True)
    stream_ser_ip = CharField()
    stream_start_time = IntegerField(index=True)
    stream_state = CharField(index=True)

    class Meta:
        db_table = 'stream_state_2016'

class StreamState2016Bak(BaseModel):
    note = CharField()
    start_date = IntegerField(index=True)
    stream_end_time = IntegerField(index=True)
    stream_flashver = CharField()
    stream = PrimaryKeyField(db_column='stream_id')
    stream_name = CharField(index=True)
    stream_ser_ip = CharField()
    stream_start_time = IntegerField(index=True)
    stream_state = CharField(index=True)

    class Meta:
        db_table = 'stream_state_2016_bak'

class StreamState2017(BaseModel):
    note = CharField()
    start_date = IntegerField()
    stream_end_time = IntegerField()
    stream_flashver = CharField()
    stream = IntegerField(db_column='stream_id')
    stream_name = CharField()
    stream_ser_ip = CharField()
    stream_start_time = IntegerField()
    stream_state = CharField()

    class Meta:
        db_table = 'stream_state_2017'
        primary_key = False

class StreamState2017Bak(BaseModel):
    note = CharField()
    start_date = IntegerField(index=True)
    stream_end_time = IntegerField(index=True)
    stream_flashver = CharField()
    stream = PrimaryKeyField(db_column='stream_id')
    stream_name = CharField(index=True)
    stream_ser_ip = CharField()
    stream_start_time = IntegerField(index=True)
    stream_state = CharField(index=True)

    class Meta:
        db_table = 'stream_state_2017_bak'

class Username(BaseModel):
    age = IntegerField(null=True)
    name = CharField(null=True)

    class Meta:
        db_table = 'username'

