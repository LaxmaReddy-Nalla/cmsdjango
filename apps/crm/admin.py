from django.contrib import admin
from .models import agent_clients,AgentClientTags,AgentClientRemarks
# Register your models here.
admin.site.register(agent_clients)
admin.site.register(AgentClientTags)
admin.site.register(AgentClientRemarks)