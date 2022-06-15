# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Accounts(models.Model):
    # id = models.AutoField()
    user_id = models.UUIDField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=255)
    password = models.TextField()
    email = models.CharField(max_length=255)
    created_on = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone_number = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    insurance_company = models.CharField(max_length=255, blank=True, null=True)
    insurance_license_number = models.TextField(blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'accounts'


# class CallLogs(models.Model):
#     call_sid = models.CharField(max_length=34, blank=True, null=True)
#     location = models.CharField(max_length=50, blank=True, null=True)
#     body = models.TextField()
#     asr_type = models.CharField(max_length=10, blank=True, null=True)
#     log_type = models.CharField(max_length=10, blank=True, null=True)
#     timestamp = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'call_logs'


# class Contacts(models.Model):
#     user = models.ForeignKey(Accounts, models.DO_NOTHING)
#     country_code = models.CharField(max_length=5)
#     phone_number = models.CharField(max_length=20)
#     email = models.CharField(max_length=255)
#     status = models.TextField(blank=True, null=True)  # This field type is a guess.
#     created_on = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'contacts'


class InitiateCalls(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    phone_number = models.CharField(max_length=20)
    call_sid = models.CharField(max_length=34, blank=True, null=True)
    stream_sid = models.CharField(max_length=34, blank=True, null=True)
    # rasa = models.ForeignKey('RasaCalls', models.DO_NOTHING, blank=True, null=True)
    call_initiated = models.BooleanField(default=False)
    fast_il = models.BooleanField(default=False)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    call_status = models.CharField(max_length=255, blank=True, null=True)
    call_at = models.DateTimeField(blank=True, null= True)
    bot = models.CharField(max_length=255, blank=True)
    asr = models.CharField(max_length=10, blank=True)
    surname = models.CharField(max_length=200,blank=True)
    name = models.CharField(max_length=255,blank=True)

    class Meta:
        managed = True
        db_table = 'initiate_calls'


# class RasaCalls(models.Model):
#     id = models.AutoField(unique=True)
#     sender_id = models.CharField(primary_key=True, max_length=255)
#     tagsl1 = models.CharField(max_length=255, blank=True, null=True)
#     created_on = models.DateTimeField(blank=True, null=True)
#     tagsl2 = models.CharField(max_length=255, blank=True, null=True)
#     tagsl3 = models.CharField(max_length=255, blank=True, null=True)
#     path = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rasa_calls'


# class Responses(models.Model):
#     call_sid = models.CharField(max_length=34)
#     response = models.TextField(blank=True, null=True)
#     type = models.CharField(max_length=10)
#     is_final = models.BooleanField(blank=True, null=True)
#     is_audio_interrupted = models.BooleanField(blank=True, null=True)
#     action = models.CharField(max_length=255, blank=True, null=True)
#     timestamp = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'responses'
