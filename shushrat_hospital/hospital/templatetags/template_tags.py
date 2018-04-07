from django import template
from hospital.models import *
from django.db.models import Q
import datetime

register = template.Library()


@register.filter(name='get_date')
def get_date(old_date, obj=None):
    new_date = old_date.date()
    return new_date

@register.filter(name='get_time')
def get_time(old_date, obj=None):
    new_time = old_date.time()
    return new_time