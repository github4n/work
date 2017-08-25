from django import forms


class TestForm(forms.Form):
    # 设置money
    name_money = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UID/用户名'}))
    xd = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '仙豆'}))
    mb = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '猫币'}))
    md = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '猫豆'}))
    # 手机
    name_sj = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UID/用户名'}))
    # 注册
    name_zc = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}))
    # 申请主播
    name_sqzb = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UID/用户名'}))
    # 流同步
    room_xs = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '线上房间号'}))
    room_xx = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '线下房间号'}))
    # 修改房间状态
    rooms = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '房间号(多个用,隔开)'}))
    status = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '直播状态1/0'}))
    # 手机发言
    cid_fy = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '房间cid'}))
    data_fy = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '发言内容data'}))
    uid_fy = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '发言用户uid'}))
    # 手机送礼
    cid_sl = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '房间cid'}))
    uid_sl = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '送礼用户uid'}))
    t_count = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '数量t_count'}))
    pos = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '位置pos'}))
    giftid = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '礼物IDgift'}))
    # 手机送豆
    cid_sd = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '房间cid'}))
    uid_sd = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '送豆用户uid'}))
    # 修改房间类型0普通，1横板娱乐，2竖版娱乐
    room_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '房间号'}))
    status1 = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0普通，1横板娱乐，2竖版娱乐'}))
