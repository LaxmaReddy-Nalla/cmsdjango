# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import agent_clients
from .validators import validate_file_extension
class AgentClientForm(forms.ModelForm):
    class Meta:
        model = agent_clients
        fields = ('appointment_scheduled', 'product', 'name','surname','gender','phone_number','age','source')

class UploadFileForm(forms.Form):
    file = forms.FileField()
