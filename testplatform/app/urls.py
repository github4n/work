#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/7/26 15:41
# Author : lixingyun
# Description :
from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.new_web, name='index'),
    url(r'^api_test$', views.api_test),
    url(r'^chatroom$', views.chatroom),
    url(r'^new_web/$', views.new_web),
    url(r'^index/$', views.new_web),
    url(r'^new_web/([a-zA-Z0-9_]*)$', views.new_web),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/image/favicon.ico')),
]