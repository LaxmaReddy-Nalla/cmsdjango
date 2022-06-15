# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Accounts,InitiateCalls

# Register your models here.
admin.site.register(Accounts)
admin.site.register(InitiateCalls)