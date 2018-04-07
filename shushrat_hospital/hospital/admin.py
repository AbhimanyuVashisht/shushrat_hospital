# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Disease,Profile,Patiente,Opd

admin.site.register(Disease)
admin.site.register(Profile)
admin.site.register(Patiente)
admin.site.register(Opd)
# Register your models here.
