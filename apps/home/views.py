# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from apps.authentication.forms import ProfileForm, UserForm
from apps.authentication.models import Profile
from apps.authentication.midllewares.auth import auth_middleware
from apps.authentication.views import update_profile



@login_required(login_url="/login/")
@auth_middleware
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
@auth_middleware
def settings(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect(to='agent_client')
    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
    return render(request, 'home/settings.html',{ "u_form": u_form, "p_form" : p_form })


@auth_middleware
@login_required(login_url="/login/")
def pages(request): 
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
