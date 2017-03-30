from django.template import Template
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def render(context, template_str):
    template = Template(template_str)
    return mark_safe(template.render(context))