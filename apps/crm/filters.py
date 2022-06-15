import django_filters
from django_filters import DateFilter,CharFilter
from apps.home.models import *
from .models import *

class FilterCalls(django_filters.FilterSet):
    start_date = DateFilter(field_name='start_time', lookup_expr='gte')
    end_date = DateFilter(field_name='start_time', lookup_expr='lte')
    call_status = CharFilter(field_name='call_status',lookup_expr='icontains')
    class Meta:
        model = InitiateCalls
        fields = ['call_status']


class AppointmentFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='appointment_scheduled', lookup_expr='gte')
    end_date = DateFilter(field_name='appointment_scheduled', lookup_expr='lte')
    class Meta:
        model = agent_clients
        fields = ['']
        exclude = '__all__'