#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
__author__ = "nabito"

from django.contrib.auth import login, logout
from django.views.generic import View
from django.urls.resolvers import get_resolver
from django.shortcuts import render
from django.http import HttpResponse

from .models import User
from .forms import LoginForm, RegisterForm


class RegisterView(View):
    """
        实现注册功能。
    """
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.register()
        return HttpResponse("Hello World!")


class LoginView(View):
    """
        实现登录功能。
    """
    def get(self, request):
        print("===========")
        return HttpResponse("Hello World!")
