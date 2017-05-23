#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
__author__ = "nabito"

from django import forms
from django.contrib.auth import authenticate
from django.utils.encoding import python_2_unicode_compatible

from .models import User


class RegisterForm(forms.ModelForm):
    """
        用于注册的表单。
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    def register(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create(email=email, password=password)
                return True
            except:
                return False

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']


class LoginForm(forms.ModelForm):
    """
        用于登录的表单。
    """
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)

    def login(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        if user.check_password(self.cleaned_data['password']):
            return user
        else:
            return None
