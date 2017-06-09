#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals


from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError

from .models import User

__author__ = "nabito"


class RegisterForm(forms.ModelForm):
    """
        用于注册的表单:
        表单中的字段必须与前端表单各项的name相同
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    confirmpassword = forms.CharField(required=True)

    def register(self):

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        confirmpassword = self.cleaned_data['confirmpassword']

        if password == confirmpassword:
            try:
                User.objects.create(email=email, password=password)
                return True
            except ObjectDoesNotExist as odne:
                raise ObjectDoesNotExist(odne)
            except DatabaseError as de:
                raise DatabaseError(de)

    class Meta:
        model = User
        fields = ['email', 'password', 'confirmpassword']


class LoginForm(forms.ModelForm):
    """
        用于登录的表单。
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    def login(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if authenticate(email=email, password=password):
            return User.objects.get(email=email)
        else:
            return None

    class Meta:
        model = User
        fields = ['username', 'password']
