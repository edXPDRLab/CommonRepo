# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import template
from django.conf import settings

register = template.Library()

# settings value
@register.simple_tag
def get_settings_value(name):
    return getattr(settings, name, "")