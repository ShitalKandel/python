from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def static(path):
    return settings.STATIC_URL + path       