from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class agent_clients(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    agent = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    appointment_scheduled = models.DateTimeField(max_length=255,blank=True, null=True)
    product = models.CharField(max_length=200, null=True,blank=True)
    name = models.CharField(max_length=200, null=True,blank=True)
    surname = models.CharField(max_length=200, null=True,blank=True)
    gender = models.CharField(max_length=200, null=True,blank=True)
    phone_number = models.CharField(max_length=200, null=True,blank=True)
    source = models.CharField(max_length=200, null=True,blank=True)
    tag = models.CharField(max_length=200, default="new lead", null=True,blank=True)
    remarks = models.TextField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/agents_client/{self.id}/"

class AgentClientTags(models.Model):
    client_id = models.UUIDField(blank=True,null=True)
    client_tag = models.CharField(max_length=200, null=True,blank=True)
    tag_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.client_id)


class AgentClientRemarks(models.Model):
    client_id = models.UUIDField(blank=True,null=True)
    client_remarks = models.CharField(max_length=200, null=True,blank=True)
    remarks_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.client_id)