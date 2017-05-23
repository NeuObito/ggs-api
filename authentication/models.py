#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
__author__ = 'nabito'

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils.translation import ugettext_lazy as _


class GGSUserManager(BaseUserManager):
    """
        用户管理类。
    """
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("请输入邮箱或者手机号！")

        user = self.model(
            username = username,
            email = GGSUserManager.normalize_email(email),
            is_staff = False,
            is_active = True,
            is_superuser = False,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(
            username,
            email,
            password,
            **extra_fields
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
        自定义用户，需要在settings.py中指定这个User类为AUTH_USER_MODEL
    """
    GENDER_CHOICE = (
        ('M', '男'),
        ('F', '女'),
    )
    username = models.CharField(_('用户名'), unique=True, db_index=True, max_length=100, null=True)  # 设置数据库的索引为username
    password = models.CharField(_('密码'), max_length=128)
    email = models.EmailField(_('邮箱'), unique=True)
    telephone = models.CharField(_('用户手机号码'), max_length=11, null=True)
    gender = models.CharField(_('性别'), max_length=1, choices=GENDER_CHOICE, null=True)
    birthday = models.DateField(_('出生日期'), auto_now=False, null=True)
    avatar = models.ImageField(upload_to='./user/avatar/%Y/%m/%d', null=True)
    presentation = models.CharField(_('一句话介绍自己'), max_length=100, null=True)

    is_staff = models.BooleanField(_('是否在Admin中可用'), default=False)
    is_active = models.BooleanField(_('是否可用'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ("username",)
    objects = GGSUserManager()  # 在这里关联自定义的UserManager

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'ggsuer'


class EducationExperience(models.Model):
    """
        用户教育经历。
    """
    gguser = models.ForeignKey(User)
    # school_id = models.CharField(_('学校编号'), max_length=10)
    school_name = models.CharField(_('学校名称'), max_length=50)
    major = models.CharField(_('主修专业'), max_length=50)
    start_time = models.DateField(_('开始时间'), auto_now=False)
    end_time = models.DateField(_('结束时间'), auto_now=False)

    def __str__(self):
        return self.school_name

    class Meta:
        db_table = 'educationexperience'


class WorkExperience(models.Model):
    """
        用户教育经历。
    """
    gguser = models.ForeignKey(User)
    # company_id = models.CharField(_('公司编号'), max_length=10)
    company_name = models.CharField(_('公司名称'), max_length=50)
    position = models.CharField(_('职位'), max_length=50)
    start_time = models.DateField(_('开始时间'), auto_now=False)
    end_time = models.DateField(_('结束时间'), auto_now=False)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'workexperience'
