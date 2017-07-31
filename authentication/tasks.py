#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-20 08:59:43
# @Author  : xuejun (xj174850@163.com)
# @Link    : https://github.com/NeuObito
# @Version : $Id$

import os

from ggs_settings.celery import app


@app.task
def send_register_email(email, send_type="register"):
    print("Hello World.")
