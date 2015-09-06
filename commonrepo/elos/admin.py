# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import ELO

class ELOAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'fullname', 'author']}),
        ('ELO Type',         {'fields': ['original_type']}),
    ]
    
admin.site.register(ELO, ELOAdmin)