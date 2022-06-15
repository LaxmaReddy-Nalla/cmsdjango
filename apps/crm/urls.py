# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from apps.crm import views

urlpatterns = [
    # The home page
    path('agent_client', views.agent_client, name='agent_client'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('agent_client/add/', views.agent_client_add, name='agent_client_add'),
    path('start_calls', views.start_calls, name='start_calls'),
    path('download_even/<uuid:id>', views.create_icsfile, name="download_event"),
    path('download_excelfile', views.download_excelfile, name="download_excelfile"),
    path('download_startcall', views.download_startcall, name="download_startcall"),
    path('ajax_date', views.ajax_date, name="ajax_date"),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name="change_password"),
    path('delete_agent', views.delete_numbers, name='delete'),
    path('dell_all',views.delete_all,name='del_all'),
    path('lead_detail',views.lead_detail, name='lead'),
]
