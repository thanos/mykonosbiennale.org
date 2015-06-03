import re
from django import template
from django.utils.safestring import mark_safe
register = template.Library()

from variables.models import Variable

@register.simple_tag
def variable(key):
    return mark_safe(Variable.objects.get(key=key).value)