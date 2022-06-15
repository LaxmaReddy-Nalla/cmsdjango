# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sqlalchemy import desc
from django.contrib.postgres.fields import ArrayField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, blank=True)
    insurance_company = models.CharField(max_length=255, blank=True)
    insurance_license_number = models.CharField(max_length=255, blank=True)
    profile_active = models.BooleanField(default=False)
    agent_active = models.BooleanField(default=False)
    bots = ArrayField(models.CharField(max_length=255, blank=True), null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()