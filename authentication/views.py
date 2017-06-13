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
        form = LoginForm(request.POST)
        print("===========")
        if form.is_valid():
            form.login()
        return JsonResponse("Hello World!")
