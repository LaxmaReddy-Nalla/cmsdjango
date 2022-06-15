# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.crm.views import dashboard
urlpatterns = [

    # The home page
    path('', dashboard, name='home'),
    path('settings', views.settings, name='settings'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
