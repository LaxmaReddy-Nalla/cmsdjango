from django import template
import datetime
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def trim(value):
    return value.strip()
@register.filter
def datefilter(value):
    string = str(value)[:19]
    date_time = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')
    return date_time


