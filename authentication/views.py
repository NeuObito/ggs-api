#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, logout
from django.views.generic import View
from django.urls.resolvers import get_resolver
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import User
from .forms import LoginForm, RegisterForm

__author__ = "nabito"


class RegisterView(View):
    """
        实现注册功能。
    """
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.register()
        return JsonResponse({"msg": "Hello World."})

    def options(self, request):
        response = HttpResponse()
        response['Access-Control-Allow-Headers'] = "accept, content-type"
        response['Access-Control-Allow-Method'] = "POST"
        response['Access-Control-Allow-Origin'] = "*"

        return HttpResponse(response, content_type="application/json")


class LoginView(View):
    """
        实现登录功能。
    """
    def post(self, request):
        print(request)
        print(request.session)
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login()
            print(user)
            if user:
                login(request, user)
                return JsonResponse({"msg": "登录成功", "succode": 20001})

        return JsonResponse({"msg": "登录失败", "errcode": 10001})

    def options(self, request):
        response = HttpResponse()
        response['Access-Control-Allow-Headers'] = "accept, content-type"
        response['Access-Control-Allow-Method'] = "POST"
        response['Access-Control-Allow-Origin'] = "*"

        return HttpResponse(response, content_type="application/json")
