import re
from django import template

from festival.models import Artist

register = template.Library()



@register.assignment_tag
def artists(event, flags=0):
    return Artist.objects.filter(event = event).order_by('name')
