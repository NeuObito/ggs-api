#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from .views import RegisterView, LoginView

urlpatterns = [
    url(r'user/$', RegisterView.as_view(), name="user-register"),
    url(r'session/$', LoginView.as_view(), name="user-login"),
]
