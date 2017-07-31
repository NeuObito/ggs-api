#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-20 08:55:49
# @Author  : xuejun (xj174850@163.com)
# @Link    : https://github.com/NeuObito
# @Version : 0.1

from __future__ import absolute_import

import os
import django

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ggs_settings.settings')
django.setup()

app = Celery('ggs_settings')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
